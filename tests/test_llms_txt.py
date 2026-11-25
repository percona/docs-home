"""Tests for hooks/llms_txt.py."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

import llms_txt
from llms_txt import (
    SITE,
    BuildResult,
    Fetcher,
    Product,
    ProductDetails,
    Response,
    SitePage,
    Version,
)

PS = f"{SITE}/percona-server/"


def versions_json(*entries: object) -> str:
    return json.dumps(list(entries))


# --- markdown_candidates / Response -------------------------------------------------


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        (f"{SITE}/a/b.html", [f"{SITE}/a/b.md"]),
        (f"{SITE}/a/index.html", [f"{SITE}/a/index.md"]),
        (f"{SITE}/a/", [f"{SITE}/a/index.md"]),
        (f"{SITE}/a/b", [f"{SITE}/a/b.md"]),
        (f"{SITE}/a/b.md", [f"{SITE}/a/b.md"]),
        (f"{SITE}/a/llms.txt", []),
        (f"{SITE}/a/b.html?x=1#top", [f"{SITE}/a/b.md"]),
    ],
)
def test_markdown_candidates(url: str, expected: list[str]) -> None:
    assert llms_txt.markdown_candidates(url) == expected


def test_response_is_page() -> None:
    assert Response(200, b"", f"{SITE}/a/", "text/html").is_page
    assert not Response(200, b"", f"{SITE}/a/404.html", "text/html").is_page
    assert not Response(404, b"", f"{SITE}/a/", "").is_page


@pytest.mark.parametrize(
    ("body", "content_type", "expected"),
    [
        (b"# Title\n", "text/markdown", True),
        (b"# Title\n", "text/plain", True),
        (b"# Title\n", "text/html", False),
        (b"\n<!doctype html><html>", "application/octet-stream", False),
        (b"<HTML>", "", False),
    ],
)
def test_response_is_markdown(body: bytes, content_type: str, expected: bool) -> None:
    assert Response(200, body, f"{SITE}/a.md", content_type).is_markdown is expected


# --- Fetcher ---------------------------------------------------------------------------


def test_fetcher_follows_redirect_and_caches(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/a/", "hi", redirect_to=f"{SITE}/a/1/")
    first = fetcher.get(f"{SITE}/a/")
    assert (first.status, first.body, first.url) == (200, b"hi", f"{SITE}/a/1/")
    assert fetcher.get(f"{SITE}/a/") is first
    assert web.requests == [f"{SITE}/a/"]


def test_fetcher_404_is_cached_and_not_retried(web: Any, fetcher: Fetcher) -> None:
    assert fetcher.get(f"{SITE}/missing").status == 404
    assert fetcher.get(f"{SITE}/missing").status == 404
    assert web.requests == [f"{SITE}/missing"]


def test_fetcher_retries_server_errors_and_does_not_cache_them(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/flaky", status=503)
    assert fetcher.get(f"{SITE}/flaky").status == 503
    assert len(web.requests) == fetcher.tries
    web.add(f"{SITE}/flaky", "ok")
    assert fetcher.get(f"{SITE}/flaky").status == 200


def test_fetcher_sleeps_between_tries_only(web: Any) -> None:
    sleeps: list[float] = []
    fetcher = Fetcher(opener=web, sleep=sleeps.append, tries=3)
    web.add(f"{SITE}/flaky", status=500)
    fetcher.get(f"{SITE}/flaky")
    assert sleeps == [2, 4]


def test_fetcher_stops_after_max_failures(web: Any) -> None:
    web.down = True
    fetcher = Fetcher(opener=web, sleep=lambda _: None, tries=1, max_failures=2)
    for i in range(5):
        assert fetcher.get(f"{SITE}/{i}").status == 0
    assert len(web.requests) == 2
    assert fetcher.failures == 2


def test_fetcher_handles_bad_urls() -> None:
    fetcher = Fetcher(tries=1, sleep=lambda _: None)
    assert fetcher.get("not a url").status == 0


def test_page_url(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/a/", redirect_to=f"{SITE}/a/2/")
    web.add(f"{SITE}/soft/", redirect_to=f"{SITE}/x/404.html")
    web.add(f"{SITE}/away/", redirect_to="https://example.com/")
    assert fetcher.page_url(f"{SITE}/a/") == f"{SITE}/a/2/"
    assert fetcher.page_url(f"{SITE}/soft/") is None
    assert fetcher.page_url(f"{SITE}/away/") is None
    assert fetcher.page_url(f"{SITE}/missing/") is None


def test_markdown_url(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/a/b.md", "# B", content_type="text/markdown")
    web.add(f"{SITE}/c/index.md", "<!doctype html>", content_type="text/html")
    assert fetcher.markdown_url(f"{SITE}/a/b.html") == f"{SITE}/a/b.md"
    assert fetcher.markdown_url(f"{SITE}/c/") is None
    assert fetcher.markdown_url(f"{SITE}/x/llms.txt") is None


# --- Product pages ---------------------------------------------------------------------


def test_parse_products_reads_cards() -> None:
    text = (Path(__file__).parent / "fixtures" / "percona-for-mysql.md").read_text()
    products, problems = llms_txt.parse_products(text, "page.md")
    assert [p.name for p in products] == ["Percona Server for MySQL", "Percona Operator for MySQL"]
    ps = products[0]
    assert ps.description == "A drop-in replacement for MySQL Community Edition."
    assert ps.link("Releases") == f"{SITE}/percona-server/9.7/release-notes/index.html"
    assert ps.docs_url == PS
    assert ps.root == PS
    assert problems == []


def test_parse_products_reports_unreadable_cards() -> None:
    text = (
        "### Broken {.title}\n\nText.\n\n[Docs](https://x.org/a) { .md-button }\n\n"
        "### Rel {.title}\n\n[Docs](docs/a.html)\n"
    )
    products, problems = llms_txt.parse_products(text, "p.md")
    assert [p.name for p in products] == ["Rel"]
    assert problems == [
        "p.md: card 'Broken' has no links it can read; left out",
        "p.md: card 'Rel' has a relative link 'docs/a.html'",
    ]


def test_parse_products_makes_root_relative_links_absolute() -> None:
    products, _ = llms_txt.parse_products("### A {.title}\n\n[Documentation](/a/)\n")
    assert products[0].docs_url == f"{SITE}/a/"


def test_product_without_documentation_link_uses_first_link() -> None:
    product = Product("X", "", (("Install now", "https://example.com/i"),))
    assert product.docs_url == "https://example.com/i"
    assert product.root is None
    assert product.key == "https://example.com/i"


def test_assign_sections_lists_each_product_once() -> None:
    op_mysql_page = Product("Op (MySQL page)", "", (("Documentation", f"{SITE}/op/latest/"),))
    op_operators_page = Product("Op (Operators page)", "", (("Documentation", f"{SITE}/op/latest/"),))
    ps = Product("PS", "", (("Documentation", PS),))
    sections = llms_txt.assign_sections(
        {"percona-for-mysql.md": [ps, op_mysql_page, ps], "percona-operators.md": [op_operators_page]}
    )
    assert sections == [("MySQL", [ps]), ("Kubernetes Operators", [op_operators_page])]


# --- Product details ---------------------------------------------------------------------


def test_find_versions_marks_latest_from_title_and_drops_broken_folders(web: Any, fetcher: Fetcher) -> None:
    web.add(
        PS + "versions.json",
        versions_json({"version": "9.7", "title": "9.7 (LATEST)"}, {"version": "8.4"}, {"version": "5.7"}),
    )
    web.add(PS + "9.7/")
    web.add(PS + "8.4/")
    web.add(PS + "5.7/", redirect_to=PS + "9.7/")
    notes: list[str] = []
    assert llms_txt.find_versions(fetcher, PS, notes) == [
        Version("9.7", PS + "9.7/", latest=True),
        Version("8.4", PS + "8.4/"),
    ]
    assert notes == [f"{PS}5.7/: does not load as its own page, left out"]


def test_find_versions_latest_from_alias(web: Any, fetcher: Fetcher) -> None:
    web.add(
        PS + "versions.json",
        versions_json({"version": "2.0", "aliases": ["latest"]}, {"version": "1.0", "aliases": None}),
    )
    web.add(PS + "2.0/")
    web.add(PS + "1.0/")
    assert [v.latest for v in llms_txt.find_versions(fetcher, PS, [])] == [True, False]


def test_find_versions_latest_from_redirect(web: Any, fetcher: Fetcher) -> None:
    web.add(PS + "versions.json", versions_json({"version": "8.3"}, {"version": "8.0"}))
    web.add(PS + "8.3/")
    web.add(PS + "8.0/")
    web.add(PS + "latest/", redirect_to=PS + "8.0/")
    assert [(v.name, v.latest) for v in llms_txt.find_versions(fetcher, PS, [])] == [("8.3", False), ("8.0", True)]


def test_find_versions_no_latest(web: Any, fetcher: Fetcher) -> None:
    web.add(PS + "versions.json", versions_json({"version": "1"}, "junk"))
    web.add(PS + "1/")
    web.add(PS + "junk/")
    web.add(PS + "latest/", redirect_to=PS + "other/")
    assert [(v.name, v.latest) for v in llms_txt.find_versions(fetcher, PS, [])] == [("1", False)]


def test_find_versions_unversioned_and_errors(web: Any, fetcher: Fetcher) -> None:
    notes: list[str] = []
    assert llms_txt.find_versions(fetcher, PS, notes) == []  # 404: not versioned
    web.add(f"{SITE}/bad/versions.json", "{not json")
    web.add(f"{SITE}/down/versions.json", status=500)
    assert llms_txt.find_versions(fetcher, f"{SITE}/bad/", notes) == []
    assert llms_txt.find_versions(fetcher, f"{SITE}/down/", notes) == []
    assert notes[0].startswith(f"{SITE}/bad/versions.json: unreadable")
    assert notes[1] == f"{SITE}/down/versions.json: status 500, versions left out"


def test_own_llms_txt(web: Any, fetcher: Fetcher) -> None:
    web.add(PS + "9.7/llms.txt", "# PS\n", content_type="text/plain")
    web.add(PS + "8.4/llms.txt", "<!doctype html>", redirect_to=PS + "8.4/404.html")
    web.add(PS + "8.0/llms.txt", "no title", content_type="text/plain")
    assert llms_txt.own_llms_txt(fetcher, PS + "9.7/") == PS + "9.7/llms.txt"
    assert llms_txt.own_llms_txt(fetcher, PS + "8.4/") is None
    assert llms_txt.own_llms_txt(fetcher, PS + "8.0/") is None


def test_best_link(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/a.html", redirect_to=f"{SITE}/v/a.html")
    web.add(f"{SITE}/v/a.md", "# A", content_type="text/markdown")
    web.add(f"{SITE}/b.html", redirect_to=f"{SITE}/v/b.html")
    notes: list[str] = []
    assert llms_txt.best_link(fetcher, f"{SITE}/a.html", notes) == f"{SITE}/v/a.md"
    assert llms_txt.best_link(fetcher, f"{SITE}/b.html", notes) == f"{SITE}/v/b.html"
    assert llms_txt.best_link(fetcher, "https://example.com/x", notes) == "https://example.com/x"
    assert llms_txt.best_link(fetcher, f"{SITE}/gone.html", notes) == f"{SITE}/gone.html"
    assert notes == [f"{SITE}/gone.html: does not load, linked as is"]


def ps_product() -> Product:
    return Product(
        "Percona Server for MySQL",
        f"Drop-in MySQL, see [features]({SITE}/percona-server/features.html).",
        (
            ("Releases", f"{SITE}/percona-server/9.7/rn.html"),
            ("Install now", f"{SITE}/percona-server/9.7/install.html"),
            ("Documentation", PS),
        ),
    )


def test_product_details_offline() -> None:
    details = llms_txt.product_details(ps_product(), None, [])
    assert details.main_url == PS
    assert details.docs_url is None
    assert details.links == (
        ("install", f"{SITE}/percona-server/9.7/install.html"),
        ("release notes", f"{SITE}/percona-server/9.7/rn.html"),
    )


def test_product_details_online(web: Any, fetcher: Fetcher) -> None:
    web.add(PS + "versions.json", versions_json({"version": "9.7", "title": "9.7 (LATEST)"}, {"version": "8.4"}))
    web.add(PS + "9.7/")
    web.add(PS + "8.4/")
    web.add(PS + "9.7/llms.txt", "# PS", content_type="text/plain")
    web.add(f"{SITE}/percona-server/9.7/rn.html")
    web.add(f"{SITE}/percona-server/9.7/install.html")
    web.add(f"{SITE}/percona-server/9.7/install.md", "# Install", content_type="text/markdown")
    web.add(f"{SITE}/percona-server/features.html", redirect_to=f"{SITE}/percona-server/9.7/features.html")
    details = llms_txt.product_details(ps_product(), fetcher, [])
    assert details.main_url == PS + "9.7/llms.txt"
    assert details.docs_url == PS + "9.7/"
    assert details.links == (
        ("install", f"{SITE}/percona-server/9.7/install.md"),
        ("release notes", f"{SITE}/percona-server/9.7/rn.html"),
    )
    assert details.description == f"Drop-in MySQL, see [features]({SITE}/percona-server/9.7/features.html)."


def test_product_details_unversioned_product(web: Any, fetcher: Fetcher) -> None:
    product = Product("Toolkit", "", (("Documentation", f"{SITE}/percona-toolkit/"),))
    web.add(f"{SITE}/percona-toolkit/")
    details = llms_txt.product_details(product, fetcher, [])
    assert (details.main_url, details.docs_url, details.versions) == (f"{SITE}/percona-toolkit/", None, ())


def test_render_product() -> None:
    details = ProductDetails(
        main_url=PS + "9.7/llms.txt",
        docs_url=PS + "9.7/",
        versions=(Version("9.7", PS + "9.7/", True), Version("8.4", PS + "8.4/")),
        links=(("install", PS + "9.7/i.md"),),
        description="Drop-in MySQL.",
    )
    assert llms_txt.render_product(ps_product(), details) == (
        f"- [Percona Server for MySQL]({PS}9.7/llms.txt): Drop-in MySQL. "
        f"Versions: [9.7 (latest)]({PS}9.7/), [8.4]({PS}8.4/). "
        f"[docs]({PS}9.7/), [install]({PS}9.7/i.md)"
    )


def test_render_product_bare() -> None:
    product = Product("X", "", (("Documentation", "https://example.com/"),))
    assert (
        llms_txt.render_product(product, ProductDetails("https://example.com/", None)) == "- [X](https://example.com/)"
    )


# --- Pages of this site ---------------------------------------------------------------------


def site_page(path: str, title: str = "T", date: str = "") -> SitePage:
    return SitePage(title, f"{SITE}/{path}", date)


def test_page_link_prefers_markdown_written_by_the_build(tmp_path: Path) -> None:
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "index.md").write_text("# A")
    assert llms_txt.page_link(site_page("a/"), tmp_path) == f"{SITE}/a/index.md"
    assert llms_txt.page_link(site_page("b/"), tmp_path) == f"{SITE}/b/"
    assert llms_txt.page_link(site_page("a/"), None) == f"{SITE}/a/"


@pytest.mark.parametrize(
    ("md", "expected"),
    [
        ("site/a/index.md", "site/a/index.html.md"),
        ("site/index.md", "site/index.html.md"),
        ("site/a/x.md", "site/a/x.html.md"),
    ],
)
def test_html_md_path(md: str, expected: str) -> None:
    assert llms_txt.html_md_path(Path(md)) == Path(expected)


def test_whats_new_files_split_posts_by_year() -> None:
    pages = [
        site_page("new/2025/01/02/a/", "Old", "2025-01-02"),
        site_page("new/2026/03/04/b/", "B", "2026-03-04"),
        site_page("new/2026/05/06/c/", "C", "2026-05-06"),
        site_page("new/2026/05/06/d/", "D"),
        site_page("new/archive/2026/", "2026"),
        site_page("new/", "What's new"),
        site_page("pmm/", "PMM"),
    ]
    files = llms_txt.whats_new_files(pages, None)
    assert sorted(files) == ["new/2025/llms.txt", "new/2026/llms.txt", "new/llms.txt"]
    year = files["new/2026/llms.txt"]
    assert year.startswith("# Percona Documentation: What's new in 2026\n\n> ")
    assert year.index("[C]") < year.index("[B]") < year.index("[D]")
    assert f"- [C]({SITE}/new/2026/05/06/c/): 2026-05-06" in year
    index = files["new/llms.txt"]
    assert index.index(f"[2026]({SITE}/new/2026/llms.txt)") < index.index(f"[2025]({SITE}/new/2025/llms.txt)")
    assert f"- [2026]({SITE}/new/archive/2026/)" in index
    assert "PMM" not in index


def test_render_site_section() -> None:
    pages = [site_page("pmm/", "PMM"), site_page("", "Home"), site_page("new/2026/01/01/x/", "X")]
    assert llms_txt.render_site_section(pages, None) == [
        "## Documentation home",
        "",
        f"- [Home]({SITE}/)",
        f"- [PMM]({SITE}/pmm/)",
        f"- [What's new]({SITE}/new/llms.txt): release announcements and their archive",
        f"- [What's new in 2026]({SITE}/new/2026/llms.txt)",
        f"- [All pages of this site in one file]({SITE}/llms-full.txt): this index and the pages above",
        f"- [Skill for AI agents]({SITE}/skill.md): how to find the right product, version and page",
    ]


@pytest.mark.parametrize(
    ("markdown", "expected"),
    [
        ("> For the complete Percona documentation index, see [llms.txt](x).\n\n# PMM\n\nText\n", "# PMM\n\nText"),
        ("> For the complete Percona documentation index, see [llms.txt](x).\n", ""),
        ("\n> A quote that stays\n\n# Page\n", "> A quote that stays\n\n# Page"),
    ],
)
def test_without_directive(markdown: str, expected: str) -> None:
    assert llms_txt.without_directive(markdown) == expected


def test_full_text_has_the_index_then_this_sites_pages(tmp_path: Path) -> None:
    directive = "> For the complete Percona documentation index, see [llms.txt](x).\n\n"
    (tmp_path / "index.md").write_text(directive + "# Home\n\nWelcome.\n")
    (tmp_path / "pmm").mkdir()
    (tmp_path / "pmm" / "index.md").write_text(directive + "# PMM\n\nMonitoring.\n")
    (tmp_path / "new" / "2026" / "x").mkdir(parents=True)
    (tmp_path / "new" / "2026" / "x" / "index.md").write_text("# A post\n")
    pages = [
        site_page("pmm/", "PMM"),
        site_page("", "Home"),
        site_page("new/2026/x/", "A post"),
        site_page("no-markdown/", "Skipped"),
    ]
    text = llms_txt.full_text("# Percona Documentation\n\n> Index\n\n", pages, tmp_path)
    assert text == (
        "# Percona Documentation\n\n> Index"
        f"\n\n---\n\n> Source: {SITE}/index.md\n\n# Home\n\nWelcome."
        f"\n\n---\n\n> Source: {SITE}/pmm/index.md\n\n# PMM\n\nMonitoring.\n"
    )


def test_published_skill_has_valid_frontmatter() -> None:
    text = (Path(__file__).parent.parent / "agents" / "skill.md").read_text(encoding="utf-8")
    assert text.startswith("---\n")
    front = text.split("---\n", 2)[1]
    fields = dict(line.split(": ", 1) for line in front.splitlines() if ": " in line and not line.startswith(" "))
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", fields["name"])  # agentskills.io name rules
    assert len(fields["name"]) <= 64
    assert 0 < len(fields["description"]) <= 1024
    assert SITE + "/llms.txt" in text


def test_header_points_to_percona_release_and_repository_names() -> None:
    assert "percona-release" in llms_txt.HEADER
    assert SITE + "/percona-software-repositories/llms.txt" in llms_txt.HEADER
    assert "`pxc-97-lts`" in llms_txt.HEADER  # the real name, not pxc-9.7-lts


# --- build_index / check_links -------------------------------------------------------------------


def test_build_index_offline(docs_dir: Path) -> None:
    result = llms_txt.build_index(docs_dir, None, [site_page("pmm/", "PMM")])
    text = result.text
    assert text.startswith(llms_txt.HEADER)
    assert [line for line in text.splitlines() if line.startswith("## ")] == [
        "## MySQL",
        "## MongoDB",
        "## PostgreSQL",
        "## Kubernetes Operators",
        "## Monitoring (PMM)",
        "## Utilities",
        "## Documentation home",
    ]
    assert "Operator page wording" in text  # the Operators page claims the Operator
    assert "Automate MySQL on Kubernetes" not in text
    assert "Blog" not in text
    assert result.problems == []


def test_build_index_reports_layout_problems(docs_dir: Path) -> None:
    (docs_dir / "pmm.md").write_text("# PMM\n\nNo cards here.\n")
    (docs_dir / "percona-utilities.md").unlink()
    (docs_dir / "percona-for-postgresql.md").write_text(
        "### A {.title}\n\n[Documentation](https://docs.percona.com/a b/)\n"
    )
    problems = llms_txt.build_index(docs_dir, None).problems
    assert "pmm.md: no product cards found; did the page layout change?" in problems
    assert "percona-utilities.md: not found" in problems
    assert "malformed link: 'https://docs.percona.com/a b/'" not in problems  # not matched by the card pattern
    assert "percona-for-postgresql.md: no product cards found; did the page layout change?" in problems


def test_build_index_reports_malformed_and_oversized(docs_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(llms_txt, "MAX_CHARS", 100)
    (docs_dir / "pmm.md").write_text(
        "### PMM {.title}\n\nSee [docs]( ).\n\n[Documentation](https://docs.percona.com/pmm/)\n"
    )
    problems = llms_txt.build_index(docs_dir, None).problems
    assert "malformed link: ' '" in problems
    assert any(p.startswith("llms.txt is ") and p.endswith("(max 100)") for p in problems)


def test_build_index_online_uses_product_details(docs_dir: Path, web: Any, fetcher: Fetcher) -> None:
    web.add(PS + "versions.json", versions_json({"version": "9.7", "title": "9.7 (LATEST)"}))
    web.add(PS + "9.7/")
    result = llms_txt.build_index(docs_dir, fetcher)
    assert f"- [Percona Server for MySQL]({PS}9.7/): " in result.text
    assert any("does not load, linked as is" in n for n in result.notes)
    assert result.notes == sorted(result.notes)


def test_check_links(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/ok/")
    web.add(f"{SITE}/soft/", redirect_to=f"{SITE}/x/404.html")
    text = f"[a]({SITE}/ok/) [b]({SITE}/soft/) [c]({SITE}/gone/) [d](https://example.com/)"
    assert llms_txt.check_links(text, fetcher) == [
        f"broken link: {SITE}/gone/ (status 404, ends at {SITE}/gone/)",
        f"broken link: {SITE}/soft/ (status 200, ends at {SITE}/x/404.html)",
    ]


# --- MkDocs hooks ------------------------------------------------------------------------------


def fake_page(url: str, title: str, meta: dict[str, Any] | None = None) -> SimpleNamespace:
    return SimpleNamespace(url=url, abs_url="/" + url, title=title, meta=meta or {})


@pytest.fixture
def hook_state() -> Any:
    llms_txt.on_startup("build")
    llms_txt.on_pre_build({})
    yield llms_txt._state
    llms_txt.on_startup("build")


def test_on_post_page_records_pages(hook_state: Any) -> None:
    assert llms_txt.on_post_page("<html>", fake_page("pmm/", "PMM"), {}) == "<html>"
    llms_txt.on_post_page(
        "", fake_page("new/2026/01/02/x/", "X", {"date": {"created": "2026-01-02"}, "description": " A\n  post "}), {}
    )
    llms_txt.on_post_page("", SimpleNamespace(url="y/", abs_url=None, title=None, meta=None), {})
    assert hook_state["pages"]["new/2026/01/02/x/"] == SitePage(
        "X", f"{SITE}/new/2026/01/02/x/", "2026-01-02", "A post"
    )
    assert hook_state["pages"]["y/"] == SitePage("", f"{SITE}/y/")


def test_on_post_build_writes_indexes(
    hook_state: Any, docs_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("LLMS_TXT_OFFLINE", "1")
    llms_txt.on_post_page("", fake_page("new/2026/01/02/x/", "X", {"date": "2026-01-02"}), {})
    site = tmp_path / "site"
    site.mkdir()
    llms_txt.on_post_build({"docs_dir": str(docs_dir), "site_dir": str(site)})
    assert (site / "llms.txt").read_text().startswith("# Percona Documentation\n")
    assert "[X]" in (site / "new" / "2026" / "llms.txt").read_text()
    assert (site / "new" / "llms.txt").is_file()
    assert (site / "llms-full.txt").read_text() == (site / "llms.txt").read_text()  # no page has markdown here
    assert not (site / "skill.md").exists()  # tests/agents/skill.md is not there


def test_on_post_build_copies_markdown_to_html_md(
    hook_state: Any, docs_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("LLMS_TXT_OFFLINE", "1")
    site = tmp_path / "site"
    (site / "pmm").mkdir(parents=True)
    (site / "pmm" / "index.md").write_text("# PMM\n")
    (site / "new" / "2026" / "x").mkdir(parents=True)
    (site / "new" / "2026" / "x" / "index.md").write_text("# X\n")
    llms_txt.on_post_page("", fake_page("pmm/", "PMM"), {})
    llms_txt.on_post_page("", fake_page("new/2026/x/", "X", {"date": "2026-01-02"}), {})
    llms_txt.on_post_page("", fake_page("nomd/", "No markdown"), {})
    llms_txt.on_post_build({"docs_dir": str(docs_dir), "site_dir": str(site)})
    assert (site / "pmm" / "index.html.md").read_text() == "# PMM\n"
    assert (site / "new" / "2026" / "x" / "index.html.md").read_text() == "# X\n"
    assert not (site / "nomd" / "index.html.md").exists()
    assert f"]({SITE}/pmm/index.md)" in (site / "llms.txt").read_text()  # links keep index.md


def test_html_md_copy_failure_is_logged_not_raised(
    hook_state: Any, docs_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    monkeypatch.setenv("LLMS_TXT_OFFLINE", "1")
    site = tmp_path / "site"
    (site / "pmm").mkdir(parents=True)
    (site / "pmm" / "index.md").write_text("# PMM\n")
    llms_txt.on_post_page("", fake_page("pmm/", "PMM"), {})

    def boom(path: Path) -> Path:
        raise OSError("disk full")

    monkeypatch.setattr(llms_txt, "html_md_path", boom)
    with caplog.at_level(logging.WARNING, logger="mkdocs.hooks.llms_txt"):
        llms_txt.on_post_build({"docs_dir": str(docs_dir), "site_dir": str(site)})
    assert ".html.md copies not written" in caplog.text
    assert (site / "llms.txt").is_file()
    assert (site / "llms-full.txt").is_file()


def test_on_post_build_publishes_the_skill(
    hook_state: Any, docs_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("LLMS_TXT_OFFLINE", "1")
    (tmp_path / "agents").mkdir()
    (tmp_path / "agents" / "skill.md").write_text("---\nname: x\n---\n")
    site = tmp_path / "site"
    site.mkdir()
    llms_txt.on_post_build({"docs_dir": str(docs_dir), "site_dir": str(site)})
    assert (site / "skill.md").read_text() == "---\nname: x\n---\n"


def test_on_post_build_warns_without_the_skill(
    hook_state: Any, docs_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    monkeypatch.setenv("LLMS_TXT_OFFLINE", "1")
    with caplog.at_level(logging.WARNING, logger="mkdocs.hooks.llms_txt"):
        llms_txt.on_post_build({"docs_dir": str(docs_dir), "site_dir": str(tmp_path)})
    assert "agents/skill.md not found" in caplog.text


def test_on_post_build_never_raises(
    hook_state: Any, docs_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    monkeypatch.setenv("LLMS_TXT_OFFLINE", "1")
    with caplog.at_level(logging.WARNING, logger="mkdocs.hooks.llms_txt"):
        llms_txt.on_post_build({"docs_dir": str(docs_dir), "site_dir": str(tmp_path / "missing" / "site")})
    assert "llms.txt: not written" in caplog.text


def test_on_post_build_logs_problems(
    hook_state: Any, docs_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    monkeypatch.setenv("LLMS_TXT_OFFLINE", "1")
    (docs_dir / "pmm.md").write_text("nothing")
    with caplog.at_level(logging.INFO, logger="mkdocs.hooks.llms_txt"):
        llms_txt.on_post_build({"docs_dir": str(docs_dir), "site_dir": str(tmp_path)})
    assert "pmm.md: no product cards found" in caplog.text
    assert "llms.txt: wrote" in caplog.text


@pytest.mark.parametrize(
    ("command", "env", "online"),
    [("build", None, True), ("serve", None, False), ("serve", "0", True), ("build", "1", False)],
)
def test_on_post_build_network_choice(
    hook_state: Any,
    command: str,
    env: str | None,
    online: bool,
    docs_dir: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    seen: list[Any] = []

    def fake_build(docs: Path, fetcher: Any, pages: Any, site_dir: Any) -> BuildResult:
        seen.append(fetcher)
        return BuildResult("# x\n")

    if env is None:
        monkeypatch.delenv("LLMS_TXT_OFFLINE", raising=False)
    else:
        monkeypatch.setenv("LLMS_TXT_OFFLINE", env)
    monkeypatch.setattr(llms_txt, "build_index", fake_build)
    llms_txt.on_startup(command)
    llms_txt.on_post_build({"docs_dir": str(docs_dir), "site_dir": str(tmp_path)})
    assert (seen[0] is not None) is online
    if online:
        assert (seen[0].timeout, seen[0].tries) == (8, 2)


# --- Command line ----------------------------------------------------------------------------


def test_main_offline_to_file(docs_dir: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    out = tmp_path / "llms.txt"
    assert llms_txt.main(["--offline", "--docs-dir", str(docs_dir), "--out", str(out)]) == 0
    assert out.read_text().startswith("# Percona Documentation")
    assert "0 problems" in capsys.readouterr().err


def test_main_to_stdout_reports_problems_as_warnings(docs_dir: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (docs_dir / "pmm.md").write_text("")
    assert llms_txt.main(["--offline", "--docs-dir", str(docs_dir)]) == 0
    captured = capsys.readouterr()
    assert captured.out.startswith("# Percona Documentation")
    assert "warning: pmm.md: no product cards found" in captured.err


def test_main_check_fails_on_broken_links(
    docs_dir: Path, web: Any, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(llms_txt, "Fetcher", lambda: Fetcher(opener=web, sleep=lambda _: None))
    assert llms_txt.main(["--check", "--docs-dir", str(docs_dir)]) == 1
    err = capsys.readouterr().err
    assert "error: broken link: https://docs.percona.com/" in err
    assert "note: " in err


def test_main_check_passes_when_links_load(docs_dir: Path, web: Any, monkeypatch: pytest.MonkeyPatch) -> None:
    web.pages = _AllPagesLoad()
    monkeypatch.setattr(llms_txt, "Fetcher", lambda: Fetcher(opener=web, sleep=lambda _: None))
    assert llms_txt.main(["--check", "--offline", "--docs-dir", str(docs_dir)]) == 0


class _AllPagesLoad(dict):  # type: ignore[type-arg]
    def get(self, url: str, default: Any = None) -> Any:
        from conftest import Page

        return Page(body="<html>")


# --- compare_live ------------------------------------------------------------------------------

BUILT = f"# P\n\n## MySQL\n\n- [PS]({PS}9.8/): v\n- [PXC](x)\n\n## Documentation home\n\n- [Home]({SITE}/)\n"


def test_product_part_ignores_this_sites_pages() -> None:
    assert llms_txt.product_part(BUILT) == [f"- [PS]({PS}9.8/): v", "- [PXC](x)"]


def test_compare_live_not_published_yet(fetcher: Fetcher) -> None:
    assert llms_txt.compare_live(BUILT, fetcher) == []


def test_compare_live_up_to_date(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/llms.txt", BUILT.replace(f"[Home]({SITE}/)", "[Home](other)"), content_type="text/plain")
    assert llms_txt.compare_live(BUILT, fetcher) == []


def test_compare_live_out_of_date(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/llms.txt", BUILT.replace("9.8", "9.7"), content_type="text/plain")
    assert llms_txt.compare_live(BUILT, fetcher) == [
        "published llms.txt is out of date: 1 product entries differ; rebuild and deploy docs-home",
        f"  now: - [PS]({PS}9.8/): v",
    ]


def test_compare_live_unreadable(web: Any, fetcher: Fetcher) -> None:
    web.add(f"{SITE}/llms.txt", "<!doctype html>", redirect_to=f"{SITE}/404.html")
    assert llms_txt.compare_live(BUILT, fetcher) == ["published llms.txt could not be read (status 200)"]


def test_main_compare_live(
    docs_dir: Path, web: Any, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(llms_txt, "Fetcher", lambda: Fetcher(opener=web, sleep=lambda _: None))
    web.add(f"{SITE}/llms.txt", "# P\n\n- [Old](x)\n", content_type="text/plain")
    assert llms_txt.main(["--compare-live", "--offline", "--docs-dir", str(docs_dir)]) == 1
    assert "error: published llms.txt is out of date" in capsys.readouterr().err

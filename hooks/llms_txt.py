"""Build the llms.txt indexes of docs.percona.com for AI agents.

See https://llmstxt.org/ for the format. The files written:

- ``/llms.txt``: every product on the product pages (percona-for-mysql.md,
  percona-operators.md, ...) with its description, its documentation versions,
  and its install and release notes links. Products that publish their own
  llms.txt are linked to it. It ends with the pages of this site.
- ``/new/llms.txt`` and ``/new/<year>/llms.txt``: every page of the "What's new"
  section, the posts split by year so each file stays small.
- ``/llms-full.txt``: ``/llms.txt``, then the markdown of this site's own pages
  (the What's new posts are left out: they are listed by year above).
- ``/skill.md``: ``agents/skill.md`` from this repo, guidance for agents on how
  to use the Percona documentation (https://agentskills.io/specification).

Product details are looked up on the live site: each product's mike
``versions.json``, the version folders, and the final address of every link.
Links point to the markdown version of a page when the product serves one.

Used two ways:

- As an MkDocs hook (``hooks:`` in mkdocs.yml). It never fails the build:
  problems are logged. ``LLMS_TXT_OFFLINE=1`` skips the lookups (``mkdocs
  serve`` skips them by default; ``LLMS_TXT_OFFLINE=0`` turns them on).
- From the command line, for CI::

      python hooks/llms_txt.py [--out llms.txt] [--offline] [--check]

  ``--check`` exits 1 on a broken or malformed link, a product page without
  product cards, or a file over 50,000 characters. ``--compare-live`` exits 1
  when the published /llms.txt lists different products or versions, which
  means docs-home needs a rebuild.

Standard library only.
"""

from __future__ import annotations

import argparse
import http.client
import json
import logging
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Iterable, Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

SITE = "https://docs.percona.com"
MAX_CHARS = 50_000  # agents may truncate larger files
USER_AGENT = "percona-docs-llms-txt"
WORKERS = 8

# Product pages, in the order of the site navigation.
CATEGORIES = (
    ("MySQL", "percona-for-mysql.md"),
    ("MongoDB", "percona-for-mongodb.md"),
    ("PostgreSQL", "percona-for-postgresql.md"),
    ("Kubernetes Operators", "percona-operators.md"),
    ("Monitoring (PMM)", "pmm.md"),
    ("Utilities", "percona-utilities.md"),
)
# A product shown on several pages is listed once, under the first page here
# that shows it, so the Operators and PMM get their own sections.
CLAIM_ORDER = ("percona-operators.md", "pmm.md", "percona-utilities.md")
# Card links that go into llms.txt, and the words used for them.
LINK_LABELS = {"Install now": "install", "Releases": "release notes"}

HEADER = (
    "# Percona Documentation\n"
    "\n"
    "> Documentation for Percona's open source database software: Percona Server for MySQL, "
    "Percona XtraDB Cluster, Percona Server for MongoDB, Percona Distribution for PostgreSQL, "
    "the Percona Kubernetes Operators, Percona Monitoring and Management (PMM), "
    "and backup and toolkit utilities.\n"
    "\n"
    "Each product has its own documentation site under docs.percona.com, with one folder per version "
    "where the product is versioned (for example `/percona-server/8.4/`). "
    "Use the docs for the version you are working with; behavior and defaults differ between versions. "
    "Product links go to the product's own llms.txt where it publishes one, "
    "otherwise to the docs of its latest version.\n"
    "\n"
    "Percona's apt and yum packages come from repo.percona.com, and the `percona-release` tool "
    "enables its repositories, for example `sudo percona-release enable-only ps-97-lts release`. "
    "The install steps and the names of all repositories (such as `ps-97-lts`, `pxc-97-lts`, "
    "`psmdb-80` and `ppg-18`) are in "
    "https://docs.percona.com/percona-software-repositories/llms.txt.\n"
)

WHATS_NEW_HEADER = """\
# Percona Documentation: What's new

> Release announcements and updates for Percona software. Each year's announcements are in their own file.
"""

TITLE_RE = re.compile(r"^###\s+(?:<span[^>]*>.*?</span>\s*)?(.+?)\s*\{\.title\}\s*$")
CARD_LINK_RE = re.compile(r"^\[([^\]]+)\]\(([^)\s]+)\)\s*$")
MD_LINK_RE = re.compile(r"\]\(([^)]*)\)")
WHATS_NEW_DIR = "new"
SITE_SECTION = "## Documentation home"  # starts the part of /llms.txt about this site's own pages
OPTIONAL_SECTION = "## Optional"  # llmstxt.org: secondary content, always the last section of /llms.txt
FULL_FILE = "llms-full.txt"
SKILL_FILE = "skill.md"
SKILL_SOURCE = Path("agents") / SKILL_FILE  # relative to the repo root, next to docs/
# The search page is a search UI with no content (not_in_nav in mkdocs.yml): it is left out of the indexes.
SEARCH_PAGE = "search-results/"
DIRECTIVE_START = "> For the complete Percona documentation index"  # added by hooks/llmstxt_directive.py

log = logging.getLogger("mkdocs.hooks.llms_txt")


# --- Fetching -----------------------------------------------------------------


@dataclass(frozen=True)
class Response:
    status: int  # 0 = no answer (network error, timeout, bad URL)
    body: bytes
    url: str  # final URL after redirects
    content_type: str

    @property
    def is_page(self) -> bool:
        """A real page: 200, and not a redirect to a 404 page."""
        return self.status == 200 and not urllib.parse.urlsplit(self.url).path.endswith("/404.html")

    @property
    def is_markdown(self) -> bool:
        if not self.is_page or "html" in self.content_type:
            return False
        head = self.body.lstrip()[:200].lower()
        return not head.startswith((b"<!doctype", b"<html"))


Opener = Callable[..., Any]


@dataclass
class Fetcher:
    """HTTP GET with retries, a cache and a limit on network failures.

    After ``max_failures`` unreachable URLs it stops trying, so a docs build
    can't stall when the site is down. Only definite answers (200 and 404)
    are cached, so a later build retries the rest.
    """

    timeout: float = 20
    tries: int = 3
    max_failures: int = 5
    opener: Opener = urllib.request.urlopen
    sleep: Callable[[float], None] = time.sleep
    failures: int = 0
    _cache: dict[str, Response] = field(default_factory=dict, repr=False)
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def get(self, url: str) -> Response:
        with self._lock:
            if url in self._cache:
                return self._cache[url]
            if self.failures >= self.max_failures:
                return Response(0, b"", url, "")
        response = self._get_with_retries(url)
        with self._lock:
            if response.status == 0:
                self.failures += 1
            if response.status in (200, 404):
                self._cache[url] = response
        return response

    def _get_with_retries(self, url: str) -> Response:
        response = Response(0, b"", url, "")
        for attempt in range(self.tries):
            if attempt:
                self.sleep(2 * attempt)
            response = self._get_once(url)
            if response.status and response.status < 500 and response.status != 429:
                break
        return response

    def _get_once(self, url: str) -> Response:
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with self.opener(request, timeout=self.timeout) as r:
                return Response(r.status, r.read(), r.geturl(), r.headers.get("Content-Type", ""))
        except urllib.error.HTTPError as e:
            e.close()  # an HTTPError holds the open response
            return Response(e.code, b"", url, "")
        except (OSError, http.client.HTTPException, ValueError):
            return Response(0, b"", url, "")

    def page_url(self, url: str) -> str | None:
        """The final URL of a page on this site, or None if it doesn't load."""
        response = self.get(url)
        if not response.is_page:
            return None
        if urllib.parse.urlsplit(response.url).netloc != urllib.parse.urlsplit(url).netloc:
            return None
        return response.url

    def markdown_url(self, url: str) -> str | None:
        """The markdown version of a page, if the site serves one."""
        for candidate in markdown_candidates(url):
            if self.get(candidate).is_markdown:
                return candidate
        return None


def markdown_candidates(url: str) -> list[str]:
    """Where a markdown version of a page may live: page.md or page/index.md."""
    parts = urllib.parse.urlsplit(url)
    path = parts.path
    if path.endswith(".md"):
        return [url]
    if re.search(r"\.[a-z0-9]+$", path, re.I) and not re.search(r"\.html?$", path, re.I):
        return []  # .txt, .json, ...
    if path.endswith("/"):
        paths = [path + "index.md"]
    elif re.search(r"/index\.html?$", path):
        paths = [re.sub(r"index\.html?$", "index.md", path)]
    else:
        paths = [re.sub(r"\.html?$", "", path) + ".md"]
    return [urllib.parse.urlunsplit((parts.scheme, parts.netloc, p, "", "")) for p in paths]


# --- Product pages ----------------------------------------------------------------


@dataclass(frozen=True)
class Product:
    name: str
    description: str
    links: tuple[tuple[str, str], ...]  # (label, url) as on the card

    def link(self, label: str) -> str | None:
        return next((url for lbl, url in self.links if lbl == label), None)

    @property
    def docs_url(self) -> str:
        return self.link("Documentation") or self.links[0][1]

    @property
    def root(self) -> str | None:
        """https://docs.percona.com/<product>/ for a product hosted on this site."""
        m = re.match(rf"{re.escape(SITE)}/([^/]+)/", self.docs_url)
        return f"{SITE}/{m.group(1)}/" if m else None

    @property
    def key(self) -> str:
        return self.root or self.docs_url


def parse_products(text: str, page: str = "") -> tuple[list[Product], list[str]]:
    """Read the product cards of a product page.

    A card is a ``### ... Name {.title}`` heading, a description, and one
    ``[Label](url)`` link per line. Returns the cards and any problems found.
    """
    cards: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for line in text.splitlines():
        title = TITLE_RE.match(line)
        if title:
            current = {"name": re.sub(r"<[^>]+>", "", title.group(1)).strip(), "desc": [], "links": []}
            cards.append(current)
        elif line.startswith("## "):
            current = None
        elif current is not None:
            _read_card_line(current, line.strip())
    return _finish_cards(cards, page)


def _read_card_line(card: dict[str, Any], line: str) -> None:
    link = CARD_LINK_RE.match(line)
    if link:
        url = link.group(2)
        card["links"].append((link.group(1).strip(), SITE + url if url.startswith("/") else url))
    elif line and not line.startswith("<") and not card["links"]:
        card["desc"].append(line)


def _finish_cards(cards: list[dict[str, Any]], page: str) -> tuple[list[Product], list[str]]:
    products: list[Product] = []
    problems: list[str] = []
    for card in cards:
        if not card["links"]:
            problems.append(f"{page}: card {card['name']!r} has no links it can read; left out")
            continue
        for _, url in card["links"]:
            if not url.startswith(("https://", "http://")):
                problems.append(f"{page}: card {card['name']!r} has a relative link {url!r}")
        products.append(Product(card["name"], " ".join(card["desc"]), tuple(card["links"])))
    return products, problems


def assign_sections(pages: dict[str, list[Product]]) -> list[tuple[str, list[Product]]]:
    """Group products by section, listing each product once."""
    owner: dict[str, str] = {}
    for page in (*CLAIM_ORDER, *(p for _, p in CATEGORIES)):
        for product in pages.get(page, []):
            owner.setdefault(product.key, page)
    sections = []
    for title, page in CATEGORIES:
        items = []
        for product in pages.get(page, []):
            if owner.get(product.key) == page:
                items.append(product)
                owner[product.key] = ""  # listed
        if items:
            sections.append((title, items))
    return sections


# --- Product details from the live site ----------------------------------------------


@dataclass(frozen=True)
class Version:
    name: str
    url: str
    latest: bool = False


@dataclass(frozen=True)
class ProductDetails:
    main_url: str  # product llms.txt, latest version folder, or docs link
    docs_url: str | None  # shown separately when main_url is the product llms.txt
    versions: tuple[Version, ...] = ()
    links: tuple[tuple[str, str], ...] = ()  # (word, url)
    description: str = ""  # with its own links resolved


def find_versions(fetcher: Fetcher, root: str, notes: list[str]) -> list[Version]:
    """Published versions whose folder loads, newest first, the default one marked."""
    response = fetcher.get(root + "versions.json")
    if response.status == 404:
        return []  # not versioned
    if response.status != 200:
        notes.append(f"{root}versions.json: status {response.status}, versions left out")
        return []
    try:
        entries = [(str(v["version"]), v) for v in json.loads(response.body) if isinstance(v, dict)]
    except (ValueError, KeyError, TypeError) as e:
        notes.append(f"{root}versions.json: unreadable ({e})")
        return []
    latest = _latest_version(fetcher, root, entries)
    versions = []
    for name, _ in entries:
        url = f"{root}{name}/"
        if fetcher.page_url(url) == url:  # drops folders that redirect away or 404
            versions.append(Version(name, url, name == latest))
        else:
            notes.append(f"{url}: does not load as its own page, left out")
    return versions


def _latest_version(fetcher: Fetcher, root: str, entries: Sequence[tuple[str, dict[str, Any]]]) -> str | None:
    for name, entry in entries:
        title = str(entry.get("title") or "").lower()
        aliases = entry.get("aliases") or []
        if "latest" in title or "latest" in aliases:
            return name
    final = fetcher.page_url(root + "latest/")  # mike alias redirect
    if final:
        m = re.match(rf"{re.escape(root)}([^/]+)/", final)
        if m and m.group(1) in {name for name, _ in entries}:
            return m.group(1)
    return None


def own_llms_txt(fetcher: Fetcher, folder: str) -> str | None:
    """The product's own llms.txt, if it publishes one in this folder."""
    url = folder + "llms.txt"
    response = fetcher.get(url)
    if response.is_markdown and response.url == url and response.body.lstrip().startswith(b"#"):
        return url
    return None


def best_link(fetcher: Fetcher, url: str, notes: list[str]) -> str:
    """The markdown version of a page if served, else its final URL."""
    if not url.startswith(SITE):
        return url
    final = fetcher.page_url(url)
    if final is None:
        notes.append(f"{url}: does not load, linked as is")
        return url
    return fetcher.markdown_url(final) or final


def product_details(product: Product, fetcher: Fetcher | None, notes: list[str]) -> ProductDetails:
    card_links = tuple((word, url) for label, word in LINK_LABELS.items() if (url := product.link(label)))
    if fetcher is None or product.root is None:
        return ProductDetails(product.docs_url, None, (), card_links, product.description)
    versions = tuple(find_versions(fetcher, product.root, notes))
    folder = next((v.url for v in versions if v.latest), versions[0].url if versions else product.root)
    llms = own_llms_txt(fetcher, folder)
    docs = folder if versions else best_link(fetcher, product.docs_url, notes)
    links = tuple((word, best_link(fetcher, url, notes)) for word, url in card_links)
    description = MD_LINK_RE.sub(lambda m: f"]({best_link(fetcher, m.group(1), notes)})", product.description)
    return ProductDetails(llms or docs, docs if llms else None, versions, links, description)


def render_product(product: Product, details: ProductDetails) -> str:
    parts = [details.description.rstrip(".")] if details.description else []
    if details.versions:
        parts.append(
            "Versions: " + ", ".join(f"[{v.name}{' (latest)' if v.latest else ''}]({v.url})" for v in details.versions)
        )
    links = [f"[docs]({details.docs_url})"] if details.docs_url else []
    links += [f"[{word}]({url})" for word, url in details.links]
    if links:
        parts.append(", ".join(links))
    return f"- [{product.name}]({details.main_url})" + (": " + ". ".join(parts) if parts else "")


# --- Pages of this site ------------------------------------------------------------


@dataclass(frozen=True)
class SitePage:
    title: str
    url: str  # absolute URL of the HTML page
    date: str = ""  # YYYY-MM-DD for posts
    description: str = ""
    in_nav: bool = True  # pages built but not in the site navigation go under "Optional"

    @property
    def path(self) -> str:
        return urllib.parse.urlsplit(self.url).path.lstrip("/")


def markdown_file(page: SitePage, site_dir: Path) -> tuple[str, Path] | None:
    """The URL and file of the page's markdown version, when the build wrote one."""
    for candidate in markdown_candidates(page.url):
        path = site_dir / urllib.parse.urlsplit(candidate).path.lstrip("/")
        if path.is_file():
            return candidate, path
    return None


def html_md_path(md_path: Path) -> Path:
    """Where the markdown copy at the page's HTML URL plus ``.md`` goes: ``index.md`` -> ``index.html.md``."""
    return md_path.with_name(md_path.name[: -len(".md")] + ".html.md")


def write_html_md_copies(pages: Iterable[SitePage], site_dir: Path) -> int:
    """Copy each page's markdown next to itself as ``.html.md``. Returns the number of copies."""
    count = 0
    for page in pages:
        found = markdown_file(page, site_dir)
        if found:
            target = html_md_path(found[1])
            target.write_text(found[1].read_text(encoding="utf-8"), encoding="utf-8")
            count += 1
    return count


def page_link(page: SitePage, site_dir: Path | None) -> str:
    """Link the page's markdown version when the build wrote one."""
    found = markdown_file(page, site_dir) if site_dir is not None else None
    return found[0] if found else page.url


def own_pages(pages: Iterable[SitePage]) -> list[SitePage]:
    """This site's pages without the What's new section and the search page, in path order."""
    kept = (p for p in pages if not p.path.startswith(WHATS_NEW_DIR + "/") and p.path != SEARCH_PAGE)
    return sorted(kept, key=lambda p: p.path)


POST_RE = re.compile(rf"^{WHATS_NEW_DIR}/(\d{{4}})/")


def whats_new_files(pages: Iterable[SitePage], site_dir: Path | None) -> dict[str, str]:
    """The What's new indexes: {path in site: text}.

    One file per year with that year's posts, newest first (``new/2026/llms.txt``),
    and ``new/llms.txt`` with the archive, category and listing pages.
    """
    by_year: dict[str, list[SitePage]] = {}
    listing: list[SitePage] = []
    for page in pages:
        post = POST_RE.match(page.path)
        if post:
            by_year.setdefault(post.group(1), []).append(page)
        elif page.path.startswith(WHATS_NEW_DIR + "/"):
            listing.append(page)
    files = {f"{WHATS_NEW_DIR}/{year}/llms.txt": _render_year(year, posts, site_dir) for year, posts in by_year.items()}
    files[f"{WHATS_NEW_DIR}/llms.txt"] = _render_listing(listing, sorted(by_year, reverse=True), site_dir)
    return files


def _render_year(year: str, posts: list[SitePage], site_dir: Path | None) -> str:
    posts = sorted(posts, key=lambda p: (p.date, p.title), reverse=True)
    lines = [
        f"# Percona Documentation: What's new in {year}",
        "",
        f"> Release announcements for Percona software published in {year}, newest first.",
        "",
    ]
    lines += [f"- [{p.title}]({page_link(p, site_dir)})" + (f": {p.date}" if p.date else "") for p in posts]
    return "\n".join(lines) + "\n"


def _render_listing(pages: list[SitePage], years: list[str], site_dir: Path | None) -> str:
    lines = [WHATS_NEW_HEADER, "## Announcements by year", ""]
    lines += [f"- [{year}]({SITE}/{WHATS_NEW_DIR}/{year}/llms.txt)" for year in years]
    lines += ["", "## Optional", ""]
    lines += [f"- [{p.title}]({page_link(p, site_dir)})" for p in sorted(pages, key=lambda p: p.path)]
    return "\n".join(lines) + "\n"


def render_site_section(pages: Sequence[SitePage], site_dir: Path | None) -> list[str]:
    """This site's own pages and the What's new indexes; secondary entries go under "Optional"."""
    years = sorted({m.group(1) for p in pages if (m := POST_RE.match(p.path))}, reverse=True)
    own = own_pages(pages)
    lines = [SITE_SECTION, ""]
    lines += [f"- [{p.title}]({page_link(p, site_dir)})" for p in own if p.in_nav]
    lines.append(f"- [What's new]({SITE}/{WHATS_NEW_DIR}/llms.txt): release announcements and their archive")
    lines.append(f"- [Skill for AI agents]({SITE}/{SKILL_FILE}): how to find the right product, version and page")
    lines += ["", OPTIONAL_SECTION, ""]
    lines += [f"- [What's new in {year}]({SITE}/{WHATS_NEW_DIR}/{year}/llms.txt)" for year in years]
    lines.append(f"- [All pages of this site in one file]({SITE}/{FULL_FILE}): this index and the pages above")
    lines += [f"- [{p.title}]({page_link(p, site_dir)})" for p in own if not p.in_nav]
    return lines


def without_directive(markdown: str) -> str:
    """A page's markdown without the pointer to /llms.txt at its top."""
    text = markdown.lstrip()
    if text.startswith(DIRECTIVE_START):
        text = text.split("\n\n", 1)[1] if "\n\n" in text else ""
    return text.strip()


def full_text(index: str, pages: Iterable[SitePage], site_dir: Path) -> str:
    """/llms-full.txt: the index, then each of this site's pages with its markdown URL."""
    parts = [index.rstrip()]
    for page in own_pages(pages):
        found = markdown_file(page, site_dir)
        if found:
            url, path = found
            parts.append(f"> Source: {url}\n\n{without_directive(path.read_text(encoding='utf-8'))}")
    return "\n\n---\n\n".join(parts) + "\n"


# --- Building -------------------------------------------------------------------------


@dataclass
class BuildResult:
    text: str
    problems: list[str] = field(default_factory=list)  # fail the CI check
    notes: list[str] = field(default_factory=list)  # informational


def read_product_pages(docs_dir: Path) -> tuple[dict[str, list[Product]], list[str]]:
    pages: dict[str, list[Product]] = {}
    problems: list[str] = []
    for _, page in CATEGORIES:
        path = docs_dir / page
        if not path.is_file():
            problems.append(f"{page}: not found")
            continue
        products, found = parse_products(path.read_text(encoding="utf-8"), page)
        problems += found
        if not products:
            problems.append(f"{page}: no product cards found; did the page layout change?")
        pages[page] = products
    return pages, problems


def build_index(
    docs_dir: Path,
    fetcher: Fetcher | None,
    site_pages: Sequence[SitePage] = (),
    site_dir: Path | None = None,
) -> BuildResult:
    """Build /llms.txt. ``fetcher=None`` builds without network lookups."""
    pages, problems = read_product_pages(docs_dir)
    sections = assign_sections(pages)
    notes: list[str] = []
    products = [p for _, items in sections for p in items]
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        details = list(pool.map(lambda p: product_details(p, fetcher, notes), products))
    rendered = {p.key: render_product(p, d) for p, d in zip(products, details, strict=True)}
    out = [HEADER]
    for title, items in sections:
        out += [f"## {title}\n", *(rendered[p.key] for p in items), ""]
    if site_pages:
        out += [*render_site_section(site_pages, site_dir), ""]
    text = "\n".join(out)
    problems += [f"malformed link: {url!r}" for url in MD_LINK_RE.findall(text) if not url or re.search(r"\s", url)]
    if len(text) > MAX_CHARS:
        problems.append(f"llms.txt is {len(text)} characters (max {MAX_CHARS})")
    return BuildResult(text, problems, sorted(notes))


def check_links(text: str, fetcher: Fetcher) -> list[str]:
    """Every docs.percona.com link that doesn't load as a page."""
    urls = sorted({u for u in MD_LINK_RE.findall(text) if u.startswith(SITE)})
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        responses = list(pool.map(fetcher.get, urls))
    return [
        f"broken link: {u} (status {r.status}, ends at {r.url})"
        for u, r in zip(urls, responses, strict=True)
        if not r.is_page
    ]


def product_part(text: str) -> list[str]:
    """The product entries of an llms.txt, without this site's own pages."""
    return [line for line in text.split(SITE_SECTION, 1)[0].splitlines() if line.startswith("- [")]


def compare_live(text: str, fetcher: Fetcher) -> list[str]:
    """Differences between the product entries of ``text`` and the published /llms.txt."""
    response = fetcher.get(f"{SITE}/llms.txt")
    if response.status == 404:
        return []  # not published yet
    if not response.is_markdown:
        return [f"published llms.txt could not be read (status {response.status})"]
    live = product_part(response.body.decode("utf-8", "replace"))
    built = product_part(text)
    if live == built:
        return []
    changed = [line for line in built if line not in live]
    return [
        f"published llms.txt is out of date: {len(changed)} product entries differ; rebuild and deploy docs-home",
        *(f"  now: {line[:160]}" for line in changed[:5]),
    ]


# --- MkDocs hooks -------------------------------------------------------------------------

_state: dict[str, Any] = {"serving": False, "pages": {}, "nav_urls": None}


def on_startup(command: str, **kwargs: Any) -> None:
    _state["serving"] = command == "serve"


def on_pre_build(config: Any, **kwargs: Any) -> None:
    _state["pages"] = {}
    _state["nav_urls"] = None


def on_nav(nav: Any, config: Any, files: Any, **kwargs: Any) -> Any:
    """Remember which pages are in the navigation."""
    _state["nav_urls"] = {page.url for page in nav.pages}
    return nav


def on_post_page(output: str, page: Any, config: Any, **kwargs: Any) -> str:
    """Remember every page of this site for the indexes."""
    url = getattr(page, "abs_url", None) or "/" + (page.url or "")
    meta = page.meta if isinstance(getattr(page, "meta", None), dict) else {}
    date = meta.get("date")
    date_text = date.get("created", "") if isinstance(date, dict) else (date or "")
    description = " ".join(str(meta.get("description") or "").split())
    nav_urls = _state["nav_urls"]
    in_nav = nav_urls is None or page.url in nav_urls
    _state["pages"][page.url] = SitePage(str(page.title or ""), SITE + url, str(date_text)[:10], description, in_nav)
    return output


def on_post_build(config: Any, **kwargs: Any) -> None:
    """Write llms.txt, the What's new indexes, llms-full.txt and skill.md. Never fails the build."""
    offline = os.environ.get("LLMS_TXT_OFFLINE", "1" if _state["serving"] else "0") == "1"
    fetcher = None if offline else Fetcher(timeout=8, tries=2)  # keep the build fast when the site is down
    site_dir = Path(config["site_dir"])
    pages = list(_state["pages"].values())
    docs_dir = Path(config["docs_dir"])
    try:
        result = build_index(docs_dir, fetcher, pages, site_dir)
        (site_dir / "llms.txt").write_text(result.text, encoding="utf-8")
        for path, text in whats_new_files(pages, site_dir).items():
            (site_dir / path).parent.mkdir(parents=True, exist_ok=True)
            (site_dir / path).write_text(text, encoding="utf-8")
        full = full_text(result.text, pages, site_dir)
        (site_dir / FULL_FILE).write_text(full, encoding="utf-8")
    except Exception:
        log.warning("llms.txt: not written", exc_info=True)
        return
    log.info("llms.txt: wrote %s, %d characters", FULL_FILE, len(full))
    try:
        copies = write_html_md_copies(pages, site_dir)
        log.info("llms.txt: wrote %d .html.md copies", copies)
    except Exception:
        log.warning("llms.txt: .html.md copies not written", exc_info=True)
    skill = docs_dir.parent / SKILL_SOURCE
    if skill.is_file():
        (site_dir / SKILL_FILE).write_text(skill.read_text(encoding="utf-8"), encoding="utf-8")
    else:
        log.warning("llms.txt: %s not found, so /%s is not published", SKILL_SOURCE, SKILL_FILE)
    for msg in result.problems:
        log.warning("llms.txt: %s", msg)
    for msg in result.notes:
        log.info("llms.txt: %s", msg)
    log.info("llms.txt: wrote %d characters, %d entries", len(result.text), result.text.count("\n- ["))


# --- Command line ----------------------------------------------------------------------------


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build docs.percona.com/llms.txt from the product pages.")
    parser.add_argument("--out", type=Path, help="write here instead of stdout")
    parser.add_argument("--offline", action="store_true", help="skip network lookups")
    parser.add_argument("--check", action="store_true", help="fail on broken links, layout problems or size")
    parser.add_argument("--compare-live", action="store_true", help="fail if the published llms.txt is out of date")
    parser.add_argument("--docs-dir", type=Path, default=Path(__file__).resolve().parent.parent / "docs")
    args = parser.parse_args(argv)

    fetcher = None if args.offline else Fetcher()
    result = build_index(args.docs_dir, fetcher)
    if args.out:
        args.out.write_text(result.text, encoding="utf-8")
    else:
        sys.stdout.write(result.text)
    for msg in result.notes:
        print(f"note: {msg}", file=sys.stderr)
    errors = list(result.problems)
    if args.check:
        errors += check_links(result.text, fetcher or Fetcher())
    if args.compare_live:
        errors += compare_live(result.text, fetcher or Fetcher())
    strict = args.check or args.compare_live
    for msg in errors:
        print(f"{'error' if strict else 'warning'}: {msg}", file=sys.stderr)
    print(f"llms.txt: {len(result.text)} characters, {len(errors)} problems", file=sys.stderr)
    return 1 if strict and errors else 0


if __name__ == "__main__":
    sys.exit(main())

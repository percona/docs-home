"""Tests for checks/agent_scores.py. AFDocs is replaced by small fake commands; nothing touches the network."""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import Any

import pytest

import agent_scores
from agent_scores import ROOT, Comparison, Score, Site

INDEX = """# Percona Documentation

> Documentation

## MySQL

- [Percona Server for MySQL](https://docs.percona.com/percona-server/9.7/llms.txt): A server. Versions: [9.7](https://docs.percona.com/percona-server/9.7/)
- [Percona Distribution for MySQL](https://docs.percona.com/percona-distribution-for-mysql/9.7/): A distribution.
- [ProxySQL Admin Utilities](https://docs.percona.com/proxysql/index.md): Admin tools.
- [OpenEverest](https://openeverest.io/docs/): Not on docs.percona.com.
- [Percona Server for MySQL again](https://docs.percona.com/percona-server/9.7/index.html): Same folder.

## Documentation home

- [Home](https://docs.percona.com/index.md)
"""


def afdocs_json(score: int, fails: tuple[str, ...] = ()) -> str:
    results = [{"id": "llms-txt-exists", "status": "pass"}, *({"id": f, "status": "fail"} for f in fails)]
    return json.dumps({"results": results, "scoring": {"overall": score, "grade": "A"}})


def fake_afdocs(tmp_path: Path, script: str) -> list[str]:
    """A command that stands in for AFDocs: a Python script that gets the same arguments."""
    path = tmp_path / "fake_afdocs.py"
    path.write_text(script, encoding="utf-8")
    return [sys.executable, str(path)]


SERVER = Site("Percona Server for MySQL", "https://docs.percona.com/percona-server/9.7/")
HOME = Site("docs.percona.com", ROOT)


# --- sites ---------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://docs.percona.com/percona-server/9.7/llms.txt", "https://docs.percona.com/percona-server/9.7/"),
        ("https://docs.percona.com/proxysql/index.md", "https://docs.percona.com/proxysql/"),
        ("https://docs.percona.com/pg-tde/", "https://docs.percona.com/pg-tde/"),
        ("https://docs.percona.com/pmm/index.html?x=1#top", "https://docs.percona.com/pmm/"),
    ],
)
def test_site_url(url: str, expected: str) -> None:
    assert agent_scores.site_url(url) == expected


def test_site_key() -> None:
    assert SERVER.key == "percona-server"
    assert HOME.key == "/"


def test_product_sites_are_the_home_and_one_per_folder() -> None:
    assert agent_scores.product_sites(INDEX) == [
        HOME,
        SERVER,
        Site("Percona Distribution for MySQL", "https://docs.percona.com/percona-distribution-for-mysql/9.7/"),
        Site("ProxySQL Admin Utilities", "https://docs.percona.com/proxysql/"),
    ]


# --- running AFDocs --------------------------------------------------------------------------


def test_parse_afdocs() -> None:
    score = agent_scores.parse_afdocs(SERVER, afdocs_json(97, ("content-negotiation",)))
    assert score == Score(SERVER, 97, "A", ("content-negotiation",))


@pytest.mark.parametrize("output", ["", "not json", '{"results": []}', '{"scoring": {"overall": "x"}}'])
def test_parse_afdocs_unreadable(output: str) -> None:
    score = agent_scores.parse_afdocs(SERVER, output)
    assert score.score is None
    assert score.error.startswith("unreadable AFDocs output")


def test_run_afdocs_reads_json_even_when_afdocs_exits_1(tmp_path: Path) -> None:
    command = fake_afdocs(
        tmp_path,
        "import json, sys\n"
        "assert sys.argv[1:3] == ['check', 'https://docs.percona.com/percona-server/9.7/']\n"
        "assert '--sampling' in sys.argv and 'deterministic' in sys.argv\n"
        f"print({afdocs_json(95, ('content-negotiation',))!r})\n"
        "sys.exit(1)\n",
    )
    assert agent_scores.run_afdocs(SERVER, command) == Score(SERVER, 95, "A", ("content-negotiation",))


def test_run_afdocs_tries_again_after_a_bad_run(tmp_path: Path) -> None:
    marker = tmp_path / "ran-once"
    command = fake_afdocs(
        tmp_path,
        "import pathlib\n"
        f"marker = pathlib.Path({str(marker)!r})\n"
        "if not marker.exists():\n"
        "    marker.write_text('x')\n"
        "    print('error page')\n"
        "else:\n"
        f"    print({afdocs_json(90)!r})\n",
    )
    assert agent_scores.run_afdocs(SERVER, command).score == 90


def test_run_afdocs_gives_up_after_its_tries(tmp_path: Path) -> None:
    command = fake_afdocs(tmp_path, "print('still broken')\n")
    assert agent_scores.run_afdocs(SERVER, command).error.startswith("unreadable")


def test_run_afdocs_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    def too_slow(*args: Any, **kwargs: Any) -> Any:
        raise subprocess.TimeoutExpired(cmd="afdocs", timeout=1)

    monkeypatch.setattr(subprocess, "run", too_slow)
    assert "longer than" in agent_scores.run_afdocs(SERVER, ["afdocs"]).error


# --- comparing and reporting --------------------------------------------------------------------------

PROXY = Site("ProxySQL", "https://docs.percona.com/proxysql/")
TDE = Site("pg_tde", "https://docs.percona.com/pg-tde/")
NEW = Site("New product", "https://docs.percona.com/new-product/")
MINIMUMS = {"/": 92, "percona-server": 97, "proxysql": 90, "pg-tde": 97}


def scores() -> list[Score]:
    return [
        Score(HOME, 92, "A"),
        Score(SERVER, 90, "A-", ("content-negotiation", "page-size-html")),
        Score(PROXY, 99, "A+"),
        Score(TDE, error="AFDocs took longer than 600 s"),
        Score(NEW, 61, "D"),
    ]


def test_compare() -> None:
    s = scores()
    result = agent_scores.compare(s, MINIMUMS)
    assert result.below == [(s[1], 97)]
    assert result.errors == [s[3]]
    assert result.can_raise == [(s[2], 90)]
    assert result.untracked == [s[4]]
    assert not result.ok


def test_compare_all_ok() -> None:
    assert agent_scores.compare([Score(HOME, 95, "A")], {"/": 92}).ok


def test_render_report_lists_every_site_and_what_to_do() -> None:
    s = scores()
    report = agent_scores.render_report(s, MINIMUMS, agent_scores.compare(s, MINIMUMS))
    assert report.startswith(
        "## Agent-readiness scores (AFDocs)\n\n1 site(s) below their minimum, 1 could not be scored."
    )
    assert (
        "| [Percona Server for MySQL](https://docs.percona.com/percona-server/9.7/) | 90 (A-) | 97 | "
        "**below minimum** | `content-negotiation`, `page-size-html` |"
    ) in report
    assert "| [pg_tde](https://docs.percona.com/pg-tde/) |  | 97 | could not be scored: AFDocs took longer" in report
    assert "| [New product](https://docs.percona.com/new-product/) | 61 (D) |  | no minimum yet |  |" in report
    assert "- `proxysql`: 90 -> 99" in report
    assert "- `new-product`: add 61" in report


def test_render_report_when_all_is_well() -> None:
    s = [Score(HOME, 92, "A")]
    report = agent_scores.render_report(s, {"/": 92}, Comparison())
    assert "Every site scores at or above its minimum." in report
    assert "To keep these scores" not in report


# --- command line ------------------------------------------------------------------------------------


def test_minimums_file_in_the_repo_is_valid() -> None:
    minimums = agent_scores.load_minimums(agent_scores.MINIMUMS_FILE)
    assert "/" in minimums
    assert all(0 <= v <= 100 for v in minimums.values())


@pytest.mark.parametrize(("home_score", "exit_code"), [(95, 0), (80, 1)])
def test_main(
    home_score: int,
    exit_code: int,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    minimums = tmp_path / "minimums.json"
    minimums.write_text(json.dumps({"minimums": {"/": 90}}))
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    fetched: list[str] = []

    def fetch_index(url: str) -> str:
        fetched.append(url)
        return INDEX

    def score_site(site: Site) -> Score:
        return Score(site, home_score if site == HOME else 70, "B")

    report = tmp_path / "report.md"
    code = agent_scores.main(
        ["--minimums", str(minimums), "--report", str(report), "--jobs", "2"], fetch_index, score_site
    )
    assert code == exit_code
    assert fetched == [ROOT + "llms.txt"]
    out = capsys.readouterr().out
    assert out == report.read_text() == summary.read_text()
    assert out.count("| [") == 4  # the home and three product sites


def test_fetch_sends_a_user_agent(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[Any] = []

    class Response:
        def __enter__(self) -> Response:
            return self

        def __exit__(self, *exc: object) -> None:
            return None

        def read(self) -> bytes:
            return b"# Index\n"

    def urlopen(request: Any, timeout: float) -> Response:
        seen.append((request.full_url, request.get_header("User-agent"), timeout))
        return Response()

    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    assert agent_scores.fetch(ROOT + "llms.txt") == "# Index\n"
    assert seen == [(ROOT + "llms.txt", "percona-docs-agent-scores", 30)]

"""Score docs.percona.com and each product site with AFDocs, and catch drops.

AFDocs (https://afdocs.dev/) checks a site against the Agent-Friendly
Documentation spec and gives it a score out of 100. This script scores:

- the docs.percona.com home, and
- every product site that /llms.txt links to, at the version it links to,

then compares each score with its minimum in ``agent-scores.json``. Pages are
sampled the same way every run (``--sampling deterministic``), so a score only
changes when the site does.

Usage::

    python checks/agent_scores.py [--report report.md] [--jobs 3]

Exits 1 when a site scores below its minimum or could not be scored. The
report lists every site, and the minimums that can be raised to keep a gain.

Standard library only; AFDocs itself comes from checks/package.json.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

ROOT = "https://docs.percona.com/"
HERE = Path(__file__).resolve().parent
MINIMUMS_FILE = HERE / "agent-scores.json"
AFDOCS = [str(HERE / "node_modules" / ".bin" / "afdocs")]
SITE_SECTION = "## Documentation home"  # where /llms.txt stops listing products
LINK_RE = re.compile(r"^- \[([^\]]+)\]\((https://docs\.percona\.com/[^)\s]*)\)", re.MULTILINE)
TIMEOUT = 600  # seconds for one site
RAISE_BY = 5  # a score this far above its minimum gets a hint to raise the minimum


@dataclass(frozen=True)
class Site:
    name: str
    url: str

    @property
    def key(self) -> str:
        """The site's name in agent-scores.json: the first folder of its URL, or "/" for the home."""
        path = urllib.parse.urlsplit(self.url).path.strip("/")
        return path.split("/")[0] if path else "/"


@dataclass(frozen=True)
class Score:
    site: Site
    score: int | None = None
    grade: str = ""
    failing: tuple[str, ...] = ()  # AFDocs checks with status "fail"
    error: str = ""


@dataclass
class Comparison:
    below: list[tuple[Score, int]] = field(default_factory=list)  # (score, minimum)
    errors: list[Score] = field(default_factory=list)
    can_raise: list[tuple[Score, int]] = field(default_factory=list)
    untracked: list[Score] = field(default_factory=list)  # no minimum yet

    @property
    def ok(self) -> bool:
        return not self.below and not self.errors


def site_url(url: str) -> str:
    """The folder a product link points into: ``.../9.7/llms.txt`` -> ``.../9.7/``."""
    parts = urllib.parse.urlsplit(url)
    path = parts.path
    if not path.endswith("/"):
        path = path.rsplit("/", 1)[0] + "/"
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, "", ""))


def product_sites(index: str) -> list[Site]:
    """The home and the product sites that /llms.txt lists, one per folder, in index order."""
    products = index.split(SITE_SECTION, 1)[0]
    sites = [Site("docs.percona.com", ROOT)]
    seen = {ROOT}
    for name, url in LINK_RE.findall(products):
        site = Site(name, site_url(url))
        if site.url not in seen:
            seen.add(site.url)
            sites.append(site)
    return sites


def parse_afdocs(site: Site, output: str) -> Score:
    try:
        data = json.loads(output)
        scoring = data["scoring"]
        failing = tuple(r["id"] for r in data.get("results", []) if r.get("status") == "fail")
        return Score(site, int(scoring["overall"]), str(scoring.get("grade", "")), failing)
    except (ValueError, KeyError, TypeError) as exc:
        return Score(site, error=f"unreadable AFDocs output ({exc.__class__.__name__})")


def run_afdocs(site: Site, command: Sequence[str] = AFDOCS, tries: int = 2) -> Score:
    """Score one site. AFDocs exits 1 when any check fails, so the JSON decides, not the exit code."""
    args = [*command, "check", site.url, "--format", "json", "--score", "--sampling", "deterministic", "-q"]
    score = Score(site, error="not run")
    for _ in range(tries):
        try:
            done = subprocess.run(args, capture_output=True, text=True, timeout=TIMEOUT, check=False)  # noqa: S603
        except subprocess.TimeoutExpired:
            score = Score(site, error=f"AFDocs took longer than {TIMEOUT} s")
            continue
        score = parse_afdocs(site, done.stdout)
        if not score.error:
            break
    return score


def compare(scores: Sequence[Score], minimums: dict[str, int]) -> Comparison:
    result = Comparison()
    for score in scores:
        minimum = minimums.get(score.site.key)
        if score.score is None:
            result.errors.append(score)
        elif minimum is None:
            result.untracked.append(score)
        elif score.score < minimum:
            result.below.append((score, minimum))
        elif score.score >= minimum + RAISE_BY:
            result.can_raise.append((score, minimum))
    return result


def _status(score: Score, minimums: dict[str, int]) -> str:
    minimum = minimums.get(score.site.key)
    if score.score is None:
        return f"could not be scored: {score.error}"
    if minimum is None:
        return "no minimum yet"
    return "**below minimum**" if score.score < minimum else "ok"


def render_report(scores: Sequence[Score], minimums: dict[str, int], comparison: Comparison) -> str:
    lines = ["## Agent-readiness scores (AFDocs)", ""]
    if comparison.ok:
        lines.append("Every site scores at or above its minimum.")
    else:
        lines.append(
            f"{len(comparison.below)} site(s) below their minimum, {len(comparison.errors)} could not be scored."
        )
    lines += ["", "| Site | Score | Minimum | Status | Failing checks |", "|---|---|---|---|---|"]
    for s in scores:
        value = "" if s.score is None else f"{s.score} ({s.grade})"
        minimum = minimums.get(s.site.key, "")
        failing = ", ".join(f"`{c}`" for c in s.failing)
        lines.append(f"| [{s.site.name}]({s.site.url}) | {value} | {minimum} | {_status(s, minimums)} | {failing} |")
    if comparison.can_raise or comparison.untracked:
        lines += ["", "To keep these scores, set their minimums in `checks/agent-scores.json`:", ""]
        lines += [f"- `{s.site.key}`: {m} -> {s.score}" for s, m in comparison.can_raise]
        lines += [f"- `{s.site.key}`: add {s.score}" for s in comparison.untracked]
    lines += ["", "Check one site locally: `npx afdocs check <url> --format scorecard --sampling deterministic`"]
    return "\n".join(lines) + "\n"


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "percona-docs-agent-scores"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return str(response.read().decode("utf-8"))


def load_minimums(path: Path) -> dict[str, int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {str(k): int(v) for k, v in data["minimums"].items()}


def main(
    argv: Sequence[str] | None = None,
    fetch_index: Callable[[str], str] = fetch,
    score_site: Callable[[Site], Score] = run_afdocs,
) -> int:
    parser = argparse.ArgumentParser(description="Score docs.percona.com with AFDocs and catch drops.")
    parser.add_argument("--minimums", type=Path, default=MINIMUMS_FILE)
    parser.add_argument("--report", type=Path, help="also write the report here")
    parser.add_argument("--jobs", type=int, default=3, help="sites scored at the same time")
    args = parser.parse_args(argv)

    minimums = load_minimums(args.minimums)
    sites = product_sites(fetch_index(ROOT + "llms.txt"))
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        scores = list(pool.map(score_site, sites))
    comparison = compare(scores, minimums)
    report = render_report(scores, minimums, comparison)

    sys.stdout.write(report)
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with Path(summary).open("a", encoding="utf-8") as out:
            out.write(report)
    return 0 if comparison.ok else 1


if __name__ == "__main__":
    sys.exit(main())

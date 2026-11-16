"""Build /llms.txt, the index of Percona documentation for AI agents.

See https://llmstxt.org/ for the format. The file lists every product shown on
the product pages (percona-for-mysql.md, percona-operators.md, ...): its name,
the description from its card, its documentation versions (from the mike
`versions.json` of each product site), and its install and release notes links.
When a product site publishes its own llms.txt, the entry links to it.

Used two ways:

- As an MkDocs hook (`hooks:` in mkdocs.yml): writes site/llms.txt after every
  build. Set LLMS_TXT_OFFLINE=1 to skip network lookups (versions and product
  llms.txt files are then left out).
- From the command line, for CI:
      python hooks/llms_txt.py [--out llms.txt] [--offline] [--check]
  --check fetches every docs.percona.com link and exits 1 on a broken link,
  a malformed link, a product page with no cards, or a file over 50,000
  characters.

Standard library only.
"""
import json
import logging
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

SITE = "https://docs.percona.com"
MAX_CHARS = 50_000  # agents may truncate larger files

# Product pages, in the order of the site navigation.
CATEGORIES = [
    ("MySQL", "percona-for-mysql.md"),
    ("MongoDB", "percona-for-mongodb.md"),
    ("PostgreSQL", "percona-for-postgresql.md"),
    ("Kubernetes Operators", "percona-operators.md"),
    ("Monitoring (PMM)", "pmm.md"),
    ("Utilities", "percona-utilities.md"),
]
# A product shown on several pages is listed once, under the first page here
# that shows it, so the Operators and PMM get their own sections.
CLAIM_ORDER = ["percona-operators.md", "pmm.md", "percona-utilities.md"]

HEADER = """# Percona Documentation

> Documentation for Percona's open source database software: Percona Server for MySQL, Percona XtraDB Cluster, Percona Server for MongoDB, Percona Distribution for PostgreSQL, the Percona Kubernetes Operators, Percona Monitoring and Management (PMM), and backup and toolkit utilities.

Each product has its own documentation site under docs.percona.com, usually with one folder per major version (for example `/percona-server/8.4/`). Use the docs for the version you are working with; behavior and defaults differ between versions. Where a product publishes its own llms.txt, the entry below links to it.
"""

TITLE_RE = re.compile(r"^###\s+(?:<span[^>]*>.*?</span>\s*)?(.+?)\s*\{\.title\}\s*$")
LINK_RE = re.compile(r"^\[([^\]]+)\]\(([^)\s]+)\)\s*$")
MD_LINK_RE = re.compile(r"\]\(([^)]*)\)")
LINK_LABELS = {"Install now": "install", "Releases": "release notes"}

log = logging.getLogger("mkdocs.hooks.llms_txt")
_cache = {}  # url -> fetch result, so `mkdocs serve` rebuilds don't refetch


def fetch(url, timeout=20, tries=3):
    """Return (status, body, final_url, content_type). Status 0 = network error."""
    if url in _cache:
        return _cache[url]
    req = urllib.request.Request(url, headers={"User-Agent": "percona-docs-llms-txt"})
    result = (0, b"", url, "")
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                result = (r.status, r.read(), r.geturl(), r.headers.get("Content-Type", ""))
                break
        except urllib.error.HTTPError as e:
            result = (e.code, b"", url, "")
            if e.code < 500 and e.code != 429:
                break
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            pass
        time.sleep(2 * (attempt + 1))
    _cache[url] = result
    return result


def parse_products(text):
    """Product cards on a page: [{name, desc, links: {label: url}}]."""
    products, cur = [], None
    for line in text.splitlines():
        m = TITLE_RE.match(line)
        if m:
            cur = {"name": re.sub(r"<[^>]+>", "", m.group(1)).strip(), "desc": [], "links": {}}
            products.append(cur)
            continue
        if cur is None:
            continue
        if line.startswith("## "):
            cur = None
            continue
        stripped = line.strip()
        lm = LINK_RE.match(stripped)
        if lm:
            url = lm.group(2)
            cur["links"][lm.group(1).strip()] = SITE + url if url.startswith("/") else url
        elif stripped and not stripped.startswith("<") and not cur["links"]:
            cur["desc"].append(stripped)
    for p in products:
        p["desc"] = " ".join(p["desc"])
    return [p for p in products if p["links"]]


def docs_link(p):
    return p["links"].get("Documentation") or next(iter(p["links"].values()))


def product_root(url):
    """https://docs.percona.com/percona-server/9.7/x.html -> https://docs.percona.com/percona-server/"""
    m = re.match(rf"{re.escape(SITE)}/([^/]+)/", url)
    return f"{SITE}/{m.group(1)}/" if m else None


def versions(root, notes):
    """[(version, is_latest)] from the product's mike versions.json."""
    status, body, _, _ = fetch(root + "versions.json")
    if status == 404:
        return []  # product without versioned docs
    if status != 200:
        notes.append(f"{root}versions.json: status {status}, versions left out")
        return []
    try:
        return [(v["version"], "latest" in v.get("title", "").lower() or "latest" in v.get("aliases", []))
                for v in json.loads(body)]
    except (ValueError, KeyError, TypeError) as e:
        notes.append(f"{root}versions.json: unreadable ({e})")
        return []


def own_llms_txt(base):
    """The product's own llms.txt URL, if it publishes one."""
    url = base + "llms.txt"
    status, _, final, ctype = fetch(url)
    # Some sites answer a missing page with a redirect to a 404.html that returns 200.
    return url if status == 200 and final == url and "html" not in ctype else None


def entry(p, offline, notes):
    docs = docs_link(p)
    root = product_root(docs)
    vers = versions(root, notes) if root and not offline else []
    newest = next((v for v, latest in vers if latest), vers[0][0] if vers else None)
    llms = None
    if root and not offline:
        llms = own_llms_txt(f"{root}{newest}/" if newest else root)
    parts = [p["desc"].rstrip(".")] if p["desc"] else []
    if vers:
        parts.append("Versions: " + ", ".join(
            f"[{v}{' (latest)' if latest else ''}]({root}{v}/)" for v, latest in vers))
    links = [f"[docs]({docs})"] if llms else []
    links += [f"[{name}]({p['links'][label]})" for label, name in LINK_LABELS.items() if label in p["links"]]
    if links:
        parts.append(", ".join(links))
    return f"- [{p['name']}]({llms or docs})" + (": " + ". ".join(parts) if parts else "")


def build(docs_dir, offline=False):
    """Return (llms.txt text, problems found in the source pages, network notes)."""
    docs_dir = pathlib.Path(docs_dir)
    problems, notes, pages = [], [], {}
    for _, fname in CATEGORIES:
        path = docs_dir / fname
        if not path.exists():
            problems.append(f"{fname}: not found")
            continue
        pages[fname] = parse_products(path.read_text(encoding="utf-8"))
        if not pages[fname]:
            problems.append(f"{fname}: no product cards found; did the page layout change?")

    owner = {}
    for fname in CLAIM_ORDER + [f for _, f in CATEGORIES]:
        for p in pages.get(fname, []):
            owner.setdefault(product_root(docs_link(p)) or docs_link(p), fname)

    sections = []
    for title, fname in CATEGORIES:
        items = []
        for p in pages.get(fname, []):
            key = product_root(docs_link(p)) or docs_link(p)
            if owner.get(key) == fname:
                items.append(p)
                owner[key] = None  # list each product once
        if items:
            sections.append((title, items))

    all_items = [p for _, items in sections for p in items]
    with ThreadPoolExecutor(max_workers=8) as pool:
        lines = dict(zip(map(id, all_items), pool.map(lambda p: entry(p, offline, notes), all_items)))

    out = [HEADER]
    for title, items in sections:
        out.append(f"## {title}\n")
        out += [lines[id(p)] for p in items]
        out.append("")
    text = "\n".join(out)

    for url in MD_LINK_RE.findall(text):
        if not url or re.search(r"\s", url):
            problems.append(f"malformed link: {url!r}")
    return text, problems, notes


def check_links(text):
    """Fetch every docs.percona.com link. Return the list of broken ones."""
    broken = []
    urls = sorted({u for u in MD_LINK_RE.findall(text) if u.startswith(SITE)})
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, (status, _, final, _) in zip(urls, pool.map(fetch, urls)):
            if status != 200 or final.rstrip("/").endswith("404.html"):
                broken.append(f"{url}: status {status}, ends at {final}")
            elif final != url:
                print(f"note: {url} redirects to {final}", file=sys.stderr)
    return broken


# MkDocs hook
def on_post_build(config, **kwargs):
    offline = os.environ.get("LLMS_TXT_OFFLINE") == "1"
    text, problems, notes = build(config["docs_dir"], offline)
    for msg in problems:
        log.warning("llms.txt: %s", msg)
    for msg in notes:
        log.info("llms.txt: %s", msg)
    out = pathlib.Path(config["site_dir"]) / "llms.txt"
    out.write_text(text, encoding="utf-8")
    log.info("llms.txt: wrote %s (%d characters)", out, len(text))


def main(argv):
    docs_dir = pathlib.Path(__file__).resolve().parent.parent / "docs"
    out = argv[argv.index("--out") + 1] if "--out" in argv else None
    text, problems, notes = build(docs_dir, offline="--offline" in argv)
    if out:
        pathlib.Path(out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    for msg in notes:
        print(f"note: {msg}", file=sys.stderr)
    if "--check" not in argv:
        return 0
    errors = problems + check_links(text)
    if len(text) > MAX_CHARS:
        errors.append(f"llms.txt is {len(text)} characters (max {MAX_CHARS})")
    for msg in errors:
        print(f"error: {msg}", file=sys.stderr)
    print(f"llms.txt: {len(text)} characters, {text.count(chr(10) + '- [')} products, {len(errors)} errors",
          file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

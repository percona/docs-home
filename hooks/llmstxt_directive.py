"""Pre-processing for the mkdocs-llmstxt plugin (``preprocess:`` in mkdocs.yml).

Starts the markdown version of every page with a pointer to /llms.txt, so an
agent that lands on one page can find the index of the whole site.
"""

from __future__ import annotations

from typing import Any

DIRECTIVE_TEXT = "For the complete Percona documentation index, see "
INDEX_URL = "https://docs.percona.com/llms.txt"


def preprocess(soup: Any, output: str) -> None:
    """Insert ``> For the complete ... index, see [llms.txt](INDEX_URL)`` at the top."""
    paragraph = soup.new_tag("p")
    paragraph.append(DIRECTIVE_TEXT)
    link = soup.new_tag("a", href=INDEX_URL)
    link.string = "llms.txt"
    paragraph.append(link)
    paragraph.append(".")
    quote = soup.new_tag("blockquote")
    quote.append(paragraph)
    soup.insert(0, quote)

"""Tests for hooks/llmstxt_directive.py."""

from __future__ import annotations

from bs4 import BeautifulSoup, Tag

import llmstxt_directive


def test_preprocess_puts_the_pointer_first() -> None:
    soup = BeautifulSoup("<h1>Title</h1><p>Body</p>", "html.parser")
    llmstxt_directive.preprocess(soup, "out.md")
    first = soup.contents[0]
    assert isinstance(first, Tag)
    assert first.name == "blockquote"
    assert first.get_text() == "For the complete Percona documentation index, see llms.txt."
    link = first.find("a")
    assert isinstance(link, Tag)
    assert link["href"] == "https://docs.percona.com/llms.txt"
    assert str(soup).endswith("<h1>Title</h1><p>Body</p>")

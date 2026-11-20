"""Tests for hooks/llmstxt_directive.py."""

from __future__ import annotations

import sys
import types
from collections.abc import Iterator

import pytest
from bs4 import BeautifulSoup, Tag

import llmstxt_directive

CARDS = """
<div class="splash-links">
  <a href="percona-for-postgresql" class="splash-card">
    <img src="assets/logo-postgresql.svg" alt="logo" />
    <h3>
      Percona Software for PostgreSQL
    </h3>
    <p>
      All Percona software for PostgreSQL databases documentation.
    </p>
  </a>
  <a href="https://docs.percona.com/percona-toolkit/" class="splash-card">
    <img src="assets/logo-pt.svg" alt="logo" />
    <h3>Percona Toolkit</h3>
    <p>Command-line tools for databases.</p>
  </a>
</div>
"""


@pytest.fixture
def cleaned() -> Iterator[list[BeautifulSoup]]:
    """A stand-in for mkdocs_llmstxt that records the soups it was asked to clean."""
    calls: list[BeautifulSoup] = []
    module = types.ModuleType("mkdocs_llmstxt")
    module.autoclean = calls.append  # type: ignore[attr-defined]
    saved = sys.modules.get("mkdocs_llmstxt")
    sys.modules["mkdocs_llmstxt"] = module
    yield calls
    if saved is None:
        del sys.modules["mkdocs_llmstxt"]
    else:
        sys.modules["mkdocs_llmstxt"] = saved


def soup_of(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


def test_preprocess_puts_the_pointer_first(cleaned: list[BeautifulSoup]) -> None:
    soup = soup_of("<h1>Title</h1><p>Body</p>")
    llmstxt_directive.preprocess(soup, "out.md")
    first = soup.contents[0]
    assert isinstance(first, Tag)
    assert first.name == "blockquote"
    assert first.get_text() == "For the complete Percona documentation index, see llms.txt."
    link = first.find("a")
    assert isinstance(link, Tag)
    assert link["href"] == "https://docs.percona.com/llms.txt"
    assert str(soup).endswith("<h1>Title</h1><p>Body</p>")


def test_preprocess_runs_the_plugin_clean_up_after_converting_cards(cleaned: list[BeautifulSoup]) -> None:
    soup = soup_of(CARDS)
    llmstxt_directive.preprocess(soup, "index.md")
    assert cleaned == [soup]
    assert soup.find("a", class_="splash-card") is None  # converted before the clean-up saw them


def test_cards_become_a_list_of_links() -> None:
    soup = soup_of(CARDS)
    llmstxt_directive.convert_cards(soup)
    items = soup.find_all("li")
    assert [item.get_text() for item in items] == [
        "Percona Software for PostgreSQL: All Percona software for PostgreSQL databases documentation.",
        "Percona Toolkit: Command-line tools for databases.",
    ]
    links = [link["href"] for link in soup.find_all("a")]
    assert links == ["percona-for-postgresql", "https://docs.percona.com/percona-toolkit/"]
    assert soup.find("img") is None
    assert len(soup.find_all("ul")) == 1


def test_each_group_of_cards_gets_its_own_list() -> None:
    soup = soup_of(f"<section>{CARDS}</section><section>{CARDS}</section>")
    llmstxt_directive.convert_cards(soup)
    assert [len(listing.find_all("li")) for listing in soup.find_all("ul")] == [2, 2]


def test_a_card_without_heading_or_description_uses_its_text() -> None:
    soup = soup_of('<a href="x" class="splash-card"> Just   text </a>')
    llmstxt_directive.convert_cards(soup)
    item = soup.find("li")
    assert isinstance(item, Tag)
    assert item.get_text() == "Just text"


def test_a_card_with_an_empty_description_has_no_colon() -> None:
    soup = soup_of('<a href="x" class="splash-card"><h3>Title</h3><p> </p></a>')
    llmstxt_directive.convert_cards(soup)
    item = soup.find("li")
    assert isinstance(item, Tag)
    assert item.get_text() == "Title"


def test_logos_are_removed_from_links_with_text() -> None:
    soup = soup_of('<a href="a"><img src="l.svg"/>Docs</a><a href="b"><svg></svg></a>')
    llmstxt_directive.remove_images_from_text_links(soup)
    assert str(soup) == '<a href="a">Docs</a><a href="b"><svg></svg></a>'  # image-only links: left to the clean-up

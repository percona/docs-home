"""Pre-processing for the mkdocs-llmstxt plugin (``preprocess:`` in mkdocs.yml).

Builds the markdown version of every page from its HTML:

- Product cards (``<a class="splash-card">`` with a logo, a title and a
  description) become a list of links, so the markdown has the same products
  as the page. The plugin's own clean-up removes every link that contains an
  image, which dropped the cards, so mkdocs.yml turns it off (``autoclean:
  false``) and this module runs it after the cards are converted.
- The page starts with a pointer to /llms.txt, so an agent that lands on one
  page can find the index of the whole site.
"""

from __future__ import annotations

import importlib
from typing import Any

DIRECTIVE_TEXT = "For the complete Percona documentation index, see "
INDEX_URL = "https://docs.percona.com/llms.txt"
CARD_CLASS = "splash-card"


def preprocess(soup: Any, output: str) -> None:
    """Convert the cards, clean up the page, then add the /llms.txt pointer."""
    convert_cards(soup)
    remove_images_from_text_links(soup)
    _autoclean(soup)
    add_directive(soup)


def convert_cards(soup: Any) -> None:
    """Replace each group of product cards with a list: ``[Title](href): description``."""
    for group in _card_groups(soup):
        listing = soup.new_tag("ul")
        group[0].insert_before(listing)
        for card in group:
            listing.append(_card_item(soup, card))
            card.decompose()


def remove_images_from_text_links(soup: Any) -> None:
    """Drop logos from links that also have text, so the link itself is kept."""
    for link in soup.find_all("a"):
        if link.find(["img", "svg"]) and link.get_text(strip=True):
            for image in link.find_all(["img", "svg"]):
                image.decompose()


def add_directive(soup: Any) -> None:
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


def _autoclean(soup: Any) -> None:
    """The plugin's own clean-up (removes images, permalinks, tab labels).

    Imported here, not at the top, because the plugin is part of the docs build
    (requirements.txt), not of the tools that test this module.
    """
    importlib.import_module("mkdocs_llmstxt").autoclean(soup)


def _card_groups(soup: Any) -> list[list[Any]]:
    """Cards grouped by their parent element, in page order."""
    groups: dict[int, list[Any]] = {}
    for card in soup.find_all("a", class_=CARD_CLASS):
        groups.setdefault(id(card.parent), []).append(card)
    return list(groups.values())


def _card_item(soup: Any, card: Any) -> Any:
    title_tag = card.find(["h1", "h2", "h3", "h4", "h5", "h6"])
    title = _text(title_tag) if title_tag else _text(card)
    description_tag = card.find("p")
    item = soup.new_tag("li")
    link = soup.new_tag("a", href=card.get("href", ""))
    link.string = title
    item.append(link)
    if description_tag and _text(description_tag):
        item.append(f": {_text(description_tag)}")
    return item


def _text(tag: Any) -> str:
    return " ".join(tag.get_text(" ").split())

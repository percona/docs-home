"""Shared fixtures: a fake web for the llms.txt generator, so tests never touch the network."""

from __future__ import annotations

import io
import urllib.error
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pytest

import llms_txt

FIXTURES = Path(__file__).parent / "fixtures"


@dataclass
class Page:
    status: int = 200
    body: str = ""
    content_type: str = "text/html; charset=utf-8"
    redirect_to: str | None = None  # final URL after redirects


@dataclass
class FakeWeb:
    """An opener for llms_txt.Fetcher that serves pages from a dict."""

    pages: dict[str, Page] = field(default_factory=dict)
    down: bool = False  # every request fails as if offline
    requests: list[str] = field(default_factory=list)

    def add(self, url: str, body: str = "", **kwargs: Any) -> None:
        self.pages[url] = Page(body=body, **kwargs)

    def __call__(self, request: Any, timeout: float) -> Any:
        url = request.full_url
        self.requests.append(url)
        if self.down:
            raise urllib.error.URLError("network is down")
        page = self.pages.get(url, Page(status=404))
        if page.status >= 400:
            raise urllib.error.HTTPError(url, page.status, "error", {}, io.BytesIO())  # type: ignore[arg-type]
        return _Response(page, page.redirect_to or url)


class _Response:
    def __init__(self, page: Page, final_url: str) -> None:
        self.status = page.status
        self._body = page.body.encode()
        self._url = final_url
        self.headers = {"Content-Type": page.content_type}

    def read(self) -> bytes:
        return self._body

    def geturl(self) -> str:
        return self._url

    def __enter__(self) -> _Response:
        return self

    def __exit__(self, *exc: object) -> None:
        return None


@pytest.fixture
def web() -> FakeWeb:
    return FakeWeb()


@pytest.fixture
def fetcher(web: FakeWeb) -> llms_txt.Fetcher:
    return llms_txt.Fetcher(opener=web, sleep=lambda _: None)


@pytest.fixture
def docs_dir(tmp_path: Path) -> Path:
    """A docs dir with the product pages from tests/fixtures."""
    docs = tmp_path / "docs"
    docs.mkdir()
    for _, page in llms_txt.CATEGORIES:
        source = FIXTURES / page
        (docs / page).write_text(source.read_text(encoding="utf-8") if source.exists() else "", encoding="utf-8")
    return docs

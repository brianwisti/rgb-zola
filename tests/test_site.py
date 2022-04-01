"""Automatic tests for the generated site."""

from pathlib import Path
from urllib.parse import urlparse

import pytest
import rich
from bs4 import BeautifulSoup

SITE_PATH = Path("public")
ALL_HTML = list(SITE_PATH.glob("**/*.html"))


class TestHTML:
    @pytest.mark.parametrize("html_path", ALL_HTML, ids=str)
    def test_internal_links(self, html_path):
        html = html_path.read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")
        links = [a.get("href") for a in soup.find_all("a")]
        rich.print(links)
        # TODO: file-relative links
        local_links = [
            link
            for link in links
            if link is not None and link.startswith("/") and "#" not in link
        ]
        rich.print(local_links)

        for local_link in local_links:
            site_link_path = SITE_PATH / local_link[1:]
            assert site_link_path.is_dir() or site_link_path.is_file()

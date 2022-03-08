"""Test structure and contents of site Atom feeds."""

from urllib.parse import urlparse
from pathlib import Path
from typing import Any, Dict

import feedparser
import pytest
import rich
import toml

SITE_BUILD_DIR = "public"


@pytest.fixture(scope="session")
def site_config() -> Dict[str, Any]:
    """Return the site's Zola configuration."""
    return toml.load("config.toml")


@pytest.fixture(scope="session")
def site_build() -> Path:
    """Return a Path pointing at generated site files."""
    path = Path(SITE_BUILD_DIR)

    if not path.is_dir():
        raise ValueError(f"Site build dir {SITE_BUILD_DIR} does not exist.")

    return path


@pytest.fixture(scope="session")
def main_feed_file(site_config, site_build) -> Path:
    feed_file_name = site_config["feed_filename"]
    return site_build / feed_file_name


@pytest.fixture(scope="session")
def main_feed(main_feed_file):
    return feedparser.parse(str(main_feed_file))


class TestFeedConfiguration:
    def test_feed_filename_defined(self, site_config):
        assert site_config["feed_filename"]

    def test_main_feed_enabled(self, site_config):
        assert site_config["generate_feed"]

    def test_extra_feed_limit_set(self, site_config):
        assert "feed_limit" in site_config["extra"]

    @pytest.mark.parametrize("taxonomy", ["category"])
    def test_taxonomy_enabled_feeds(self, site_config, taxonomy):
        assert any(
            entry
            for entry in site_config["taxonomies"]
            if entry["name"] == taxonomy and entry["feed"] == True
        )

    @pytest.mark.parametrize("taxonomy", ["tags", "series"])
    def test_taxonomy_disabled_feeds(self, site_config, taxonomy):
        assert not any(
            entry
            for entry in site_config["taxonomies"]
            if entry["name"] == taxonomy
            and "feed" in entry
            and entry.get("feed") == True
        )

    def test_extra_main_feed_sections_defined(self, site_config):
        assert "main_feed_categories" in site_config["extra"]


class TestFeedsGenerated:
    def test_main_feed_generated(self, site_config, site_build):
        feed_filename = site_config["feed_filename"]
        feed_file = site_build / feed_filename

        assert feed_file.is_file()

    def test_category_feeds_generated(self, site_config, site_build):
        feed_filename = site_config["feed_filename"]
        category_path = site_build / "category"

        for child in category_path.iterdir():
            if not child.is_dir():
                continue

            child_feed = child / feed_filename
            assert child_feed.is_file()

class TestMainFeedContent:
    def test_item_count(self, site_config, main_feed):
        expected_count = int(site_config["extra"]["feed_limit"])
        assert len(main_feed.entries) == expected_count

    def test_only_blog_articles_in_feed(self, main_feed):
        #<link>https://randomgeekery.org/blog/2022/added-nano-based-emacs-config/</link>
        links = [urlparse(entry["link"]).path for entry in main_feed.entries]
        rich.print(links)
        assert not any(link for link in links if link.split("/")[1] != "blog")

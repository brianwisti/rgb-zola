"""Check that content sources are in good, quality shape."""

from pathlib import Path
from subprocess import run

import frontmatter
import pytest
import yamale

CONTENT_PATH = Path("content")
ALL_MARKDOWN = list(CONTENT_PATH.glob("**/*.md"))

BLOG_ARTICLES = [
    article
    for article in ALL_MARKDOWN
    if article.parts[1] == "blog" and article.name == "index.md"
]

CONFIG_ARTICLES = [article for article in ALL_MARKDOWN if article.parts[1] == "config"]

PAGE_ARTICLES = [
    article
    for article in ALL_MARKDOWN
    if article not in BLOG_ARTICLES
    and article not in CONFIG_ARTICLES
    and article.name == "index.md"
]

SECTION_PAGES = [
    article
    for article in ALL_MARKDOWN
    if article.name == "_index.md" and article not in CONFIG_ARTICLES
]

ARTIFACT_PASS = [
    "using-markdown-it-in-python",
]

ARTIFACT_PAGES = [
    page for page in ALL_MARKDOWN if page.parent.name not in ARTIFACT_PASS
]


@pytest.fixture(scope="session")
def blog_schema():
    return yamale.make_schema("./schemas/blog.yml", parser="ruamel")


@pytest.fixture(scope="session")
def config_schema():
    return yamale.make_schema("./schemas/config.yml", parser="ruamel")


@pytest.fixture(scope="session")
def page_schema():
    return yamale.make_schema("./schemas/page.yml", parser="ruamel")


@pytest.fixture(scope="session")
def section_schema():
    return yamale.make_schema("./schemas/section.yml", parser="ruamel")


class TestFrontmatter:
    @pytest.mark.parametrize("content_path", BLOG_ARTICLES)
    def test_valid_frontmatter_for_blog(self, blog_schema, content_path: Path):
        print(f"Validing frontmatter for '{content_path}'")
        components = content_path.read_text(encoding="utf-8").split("---\n")
        frontmatter = components[1]
        data = yamale.make_data(content=frontmatter)

        assert yamale.validate(blog_schema, data)

    @pytest.mark.parametrize("content_path", CONFIG_ARTICLES)
    def test_valid_frontmatter_for_config(self, content_path, config_schema):
        print(f"Validing frontmatter for '{content_path}'")
        components = content_path.read_text(encoding="utf-8").split("---\n")
        frontmatter = components[1]
        data = yamale.make_data(content=frontmatter)

        assert yamale.validate(config_schema, data)

    @pytest.mark.parametrize("page", PAGE_ARTICLES)
    def test_valid_frontmatter_for_pages(self, page, page_schema):
        print(f"Validing frontmatter for '{page}'")
        components = page.read_text(encoding="utf-8").split("---\n")
        frontmatter = components[1]
        data = yamale.make_data(content=frontmatter)

        assert yamale.validate(page_schema, data)

    @pytest.mark.parametrize("section", SECTION_PAGES)
    def test_valid_frontmatter_for_sections(self, section, section_schema):
        print(f"Validing frontmatter for '{section}'")
        components = section.read_text(encoding="utf-8").split("---\n")
        frontmatter = components[1]
        data = yamale.make_data(content=frontmatter)

        assert yamale.validate(section_schema, data)


class TestMarkdown:
    def test_markdownlint(self):
        res = run(["markdownlint", "-j", "content/**/index.md"], capture_output=True)
        print(res.stderr.decode())
        assert res.returncode == 0

    @pytest.mark.parametrize("content_path", ARTIFACT_PAGES, ids=str)
    def test_admonition_artifact(self, content_path: Path):
        post = frontmatter.loads(content_path.read_text(encoding="utf-8"))

        assert ":::" not in post.content

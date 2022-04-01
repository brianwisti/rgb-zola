#!/usr/bin/env python
import re
from collections import Counter
from pathlib import Path

import rich

CONTENT_PATH = Path("content")
YAML_DELIMITER = "---\n"
TOML_DELIMITER = "+++\n"

PAGE_WITH_TOML = r"""
    \A
    \+\+\+ \n
"""

PAGE_WITH_YAML = r"""
    \A
    --- \n
"""

def main():
    page_with_toml = re.compile(PAGE_WITH_TOML, re.X)
    page_with_yaml = re.compile(PAGE_WITH_YAML, re.X)
    meta_formats = []

    for md_path in CONTENT_PATH.glob("**/*.md"):
        file_text = md_path.read_text(encoding="utf-8")

        if page_with_toml.search(file_text):
            meta_format = "TOML"
        elif page_with_yaml.search(file_text):
            meta_format = "YAML"
        else:
            raise ValueError(f"Unknown frontmatter: '{md_path}'")

        meta_formats.append(meta_format)

    formats_tally = Counter(meta_formats)
    rich.print(formats_tally)


if __name__ == "__main__":
    main()

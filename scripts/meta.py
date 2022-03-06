#!/usr/bin/env python

"""Generates thumbnails and social media versions of page cover images when present."""

from dataclasses import dataclass
from pathlib import Path
from typing import cast

import frontmatter
import pyvips
import rich
from frontmatter.default_handlers import TOMLHandler

@dataclass
class Dimensions:
    height: int
    width: int

CARD = Dimensions(width=400, height=212)

def main():
    content_path = Path("content")
    toml_handler = TOMLHandler()

    for page in content_path.glob("**/*.md"):
        post = frontmatter.loads(
            page.read_text(encoding="utf-8"), handler=toml_handler
        )
        extra = post.get("extra")

        if not extra:
            continue

        cover_image = extra.get("cover_image")

        if not cover_image:
            continue

        cover_path = page.parent / cover_image["path"]
        print(cover_path)
        image = cast(pyvips.Image, pyvips.Image.new_from_file(str(cover_path), access="sequential"))
        print(f"height: {image.height}; width: {image.width}")
        card_name = f"_card.webp"
        card_path = page.parent / card_name
        card_out = pyvips.Image.thumbnail(
            str(cover_path),
            CARD.width,
            height=CARD.height,
            crop=pyvips.enums.Interesting.ATTENTION
        )
        card_out.write_to_file(str(card_path))
        rich.print(card_out)
        extra["card"] = card_name
        page.write_text(frontmatter.dumps(post))

if __name__ == "__main__":
    main()

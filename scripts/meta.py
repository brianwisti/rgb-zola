#!/usr/bin/env python

"""Generates thumbnails and social media versions of page cover images when present."""

import toml
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


def generate_card_for_cover(cover_path: Path) -> Path:
    """Generate a card image from the cover and return its Path."""
    image = cast(
        pyvips.Image, pyvips.Image.new_from_file(str(cover_path), access="sequential")
    )
    card_name = f"social_card.webp"
    card_path = cover_path.parent / card_name
    # Check if the card exists
    # - and is newer than the cover
    # - TODO: and the right size

    if card_path.is_file():
        if card_path.stat().st_mtime > cover_path.stat().st_mtime:
            return card_path

    print(f"Writing {card_path}")
    card_out = pyvips.Image.thumbnail(
        str(cover_path),
        CARD.width,
        height=CARD.height,
        crop=pyvips.enums.Interesting.ATTENTION,
    )
    card_out.write_to_file(str(card_path))
    return card_path


def main():
    content_path = Path("content")
    toml_handler = TOMLHandler()

    for page in content_path.glob("**/*.md"):
        try:
            post = frontmatter.loads(
                page.read_text(encoding="utf-8"), handler=toml_handler
            )
        except toml.decoder.TomlDecodeError:
            raise ValueError(f"Bad frontmatter in {page}!")

        extra = post.get("extra")

        if not extra:
            continue

        cover_image = extra.get("cover_image")

        if not cover_image:
            continue

        cover_path = page.parent / cover_image["path"]
        card_path = generate_card_for_cover(cover_path)
        card_name = str(card_path.name)

        if extra.get("card") == card_name:
            continue

        print(f"Updating extra.card for {page}")
        extra["card"] = card_name
        page.write_text(frontmatter.dumps(post))


if __name__ == "__main__":
    main()

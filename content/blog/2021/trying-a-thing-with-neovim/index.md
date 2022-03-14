+++
title = "trying a thing with neovim"
description = "testing a python remote plugin for quicker reStructuredText in Hugo"
date = "2021-08-09 00:00:00-07:00"
updated = "2021-08-10 00:00:00-07:00"
draft = false
aliases = [ "/post/2021/08/trying-a-thing-with-neovim/",]

[taxonomies]
category = [ "post",]
tags = [ "neovim", "python", "hugo", "rst", "site", "tools",]

+++

But will it even work?

Oh right I need to `:UpdateRemotePlugins` first.

## Test \[PASSED]

It worked!

## What did I just do?

[Neovim]: http://neovim.io/
[remote plugin]: https://neovim.io/doc/user/remote_plugin.html
[Hugo]: https://gohugo.io

I used a [remote plugin][] in [Neovim][] to transform my {{ tag(name="rst") }}
into an HTML source document, simplifying [Hugo][]'s site-building duties.

I won't make you wait around for a proper post. [1]_ Hugo lets you use
reStructuredText.  But Hugo's way is slow and hard to customize. Not their
fault. reStructuredText is not their focus. Still — why not format it ahead of
time?

{% note(title="answer") %}
Because it took a lot of work to figure this out? And most folks are
perfectly happy with Markdown? And bloggers who prefer reStructuredText are
probably using [Pelican][] or [Nikola][]?

[Pelican]: https://blog.getpelican.com/
[Nikola]: https://getnikola.com/
{% end %}

Shush you.

## The Implementation

Start with `content/whatever/index.rst.txt`.

[`ignoreFiles`]: https://gohugo.io/getting-started/configuration/#ignore-content-and-data-files-when-rendering

Make sure Hugo won't track `rst.txt` files by explicitly adding an item the
[`ignoreFiles`][] config setting.

```toml
# config.toml

ignoreFiles = ['\.rst\.txt$']
```

This way `hugo server --navigateToChanged` behaves how we expect.

{% note() %}
I tried setting `ignoreFiles = ['\.rst$']` but as far as I could tell,
Hugo ignored my request to ignore the file. Looks like I'm sticking with
`.rst.txt` for now.
{% end %}

With the code down below in my Neovim python3 — that's *python3* not
*python* — rplugin folder, and remote plugins updated, I write
`index.rst.txt` to disk.

The remote plugin transforms it to HTML, copying my YAML frontmatter as is.
So what Hugo sees is updated HTML with frontmatter, and builds that into the
site templates nice and quick.

### The Code

```python
# ~/.config/nvim/rplugin/python3/rstbuild_hugo.py

"""Give my reStructuredText posts in Hugo a little boost."""

import locale

import frontmatter
import pynvim
from docutils.core import publish_parts

locale.setlocale(locale.LC_ALL, "")


def determine_target(source: str) -> str:
    # Using an odd suffix so Hugo doesn't try to build the rst itself
    if not source.endswith(".rst.txt"):
        raise ValueError(f"Look at {source} more closely before transforming it.")

    return source.replace(".rst.txt", ".html")


@pynvim.plugin
class RSTBuildHugo:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.autocmd("BufWritePost", pattern="*.rst.txt", eval='expand("<afile>")')
    def convert_file(self, source_filename: str) -> None:
        target_path = determine_target(source_filename)
        post = frontmatter.load(source_filename)
        parts = publish_parts(source=post.content, writer_name="html")
        post.content = parts["body"]
        post.metadata["format"] = "rst"

        with open(target_path, "w") as out:
            out.write(frontmatter.dumps(post))

        self.nvim.out_write(f"Wrote {target_path}\n")
```

Lord knows this code ain't perfect. This post is its main test. Who knows what
bugs and improvements will come later?

{% note() %}
You will, if you skim the Updates
{% end %}

If you grab a copy for your own nefarious plans — a similar template could get
you fast Asciidoctor transforms as well — just remember a couple things:

- make sure the Python you're using has the libraries needed; I listed my
  choices below
- put it in the right folder; `rplugin/python` is for Python 2;
  `rplugin/python3` is for Python 3
- run `:UpdateRemotePlugins` and restart Neovim when you make changes to the
  plugin file

### Libraries Used

[Docutils]: https://docutils.sourceforge.io/
[Pygments]: https://pygments.org/
[Python Frontmatter]: https://python-frontmatter.readthedocs.io/en/latest/index.html
[pynvim]: https://pynvim.readthedocs.io/en/latest/

- [Docutils][] of course, for transforming the reStructuredText
- Docutils takes advantage of the fact that I have [Pygments][] installed, for
  syntax highlighting
- [Python Frontmatter][] gives me a consistent tool for handling post
  frontmatter and content
- [pynvim][] is the bit that hooks it all into Neovim

## Updates

### 2021-08-10

- use the `ignoreFiles` config setting so Hugo stops watching `.rst.txt`
  files for changes

- change `BufWrite` to `BufWritePost` so the transform happens *after* we write `index.rst.txt`

[^1]: I will update this post as I refine the approach, though. Makes more
   sense than adding little piecemeal posts as I go along.

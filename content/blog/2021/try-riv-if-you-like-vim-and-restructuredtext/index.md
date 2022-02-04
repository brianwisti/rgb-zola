---
aliases:
- /note/2021/10/try-riv-if-you-like-vim-and-restructuredtext/
date: '2021-10-23 00:00:00+00:00'
draft: false
extra:
  cover_image:
    caption: Riv screenshot
    path: cover.png
taxonomies:
  category:
  - note
  tags:
  - vim
  - rst
  - second-brain
title: Try Riv if you like Vim and reStructuredText
---

[Riv]: https://github.com/gu-fan/riv.vim
[Deft for Emacs]: https://jblevins.org/projects/deft/
[Vim]: https://www.vim.org/
[reStructuredText]: https://docutils.sourceforge.io/

[Riv][] is a wiki, but feels like more of a notebook. Think [Deft for Emacs][]
with journaling and HTML publishing. What makes Riv interesting — aside from
the [Vim][] thing — is that it uses [reStructuredText][] for its native format.

It works well enough, especially once you build up muscle memory for Riv's
leader sequence {{ kbd(keys="C-e") }}. Don't overload it right away though! It
includes some insert mode mappings, which can get real confusing if your
preferred leader is a space.

[pynvim]: https://pynvim.readthedocs.io/en/latest/

Meanwhile I got a lot of {{ tag(name="neovim") }} ideas. Course, I need to get
some more practice in with [pynvim][] first. And I suppose some more practice
with Riv.
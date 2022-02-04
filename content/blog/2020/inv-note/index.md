+++
title = "inv note"
date = "2020-02-05 07:54:39-08:00"
draft = false
aliases = [ "/note/2020/36/inv-note/", "/note/2020/02/inv-note/",]

[taxonomies]
category = [ "note",]
tags = [ "site", "pyinvoke", "drawing", "amaziograph", "fun",]

[extra.cover_image]
caption = "I drew this with [Amaziograph](https://amaziograph.com/)"
path = "cover.jpg"

+++

$ inv note --title='inv note'

Don’t mind me. I’m just trying an experiment with using
[Invoke](https://docs.pyinvoke.org) for my site workflow instead of
[Make](https://www.gnu.org/software/make/).

    $ inv serve
    SHOW_INFO=1 hugo server --buildDrafts --bind 0.0.0.0 --navigateToChanged
    ...
    Press Ctrl+C to stop

But that’s boring on its own. Here. Have a drawing.

I’ll probably make a proper blog post about Invoke later. Meanwhile,
checkout the docs on [Getting
started](https://docs.pyinvoke.org/en/stable/getting-started.html).

    $ inv publish
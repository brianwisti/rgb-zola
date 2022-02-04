+++
title = "finally have all my content in one format"
date = "2021-09-16 00:00:00-07:00"
draft = false
aliases = [ "/note/2021/09/finally-have-all-my-content-in-one-format/",]

[taxonomies]
category = [ "note",]
tags = [ "site", "asciidoctor",]

+++

```
content/**/*{.md,.md.txt,.rst,.rst.txt,.adoc,.adoc.txt,.org}
┌─────────┬─────┐
│Format   │Count│
├─────────┼─────┤
│.md      │48   │
│.adoc.txt│574  │
│.md.txt  │579  │
│.rst.txt │32   │
└─────────┴─────┘
```

[base blog]: /note/2021/08/pared-down-to-the-base-blog/

Okay yes I also have it in several other formats. Came up with an approach
where I can keep all my formats in the [base blog][] and build whatever I
prefer.

[Asciidoctor]: https://asciidoctor.org

My *point* is that all the content that counts is available in [Asciidoctor][]
format. Better choice for me than Markdown since Asciidoctor already has
built-in understanding of notes and asides. Better choice for me than
reStructuredText because it's easier to find Asciidoctor processors for
assorted static site generators.
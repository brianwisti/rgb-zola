+++
title = "Pandoc"
date = "2015-07-23 00:00:00-07:00"
draft = false
aliases = [ "/tools/2015/07/23_pandoc.html", "/post/2015/pandoc/", "/2015/07/23/pandoc/", "/post/2015/07/pandoc/",]

[taxonomies]
category = [ "post",]
tags = [ "pandoc", "tools",]

+++

I could use [Pandoc](http://pandoc.org/) to build HTML from my site
sources.

I could use it to convert them to different sources.

I’m not saying I *would*. But I *could*.

Okay I might.

    $ pandoc --to org _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.org
    $ pandoc --to asciidoc _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.adoc
    $ pandoc _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.html

![Pandoc output in Emacs](emacs-pandoc.png)

Honestly at this point I’d say it’s pretty likely.
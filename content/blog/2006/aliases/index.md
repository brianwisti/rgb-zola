+++
title = "Aliases"
date = "2006-03-01 00:00:00-08:00"
aliases = [ "/blogspot/2006/03/01_aliases.html", "/post/2006/aliases/", "/2006/03/01/aliases/", "/post/2006/03/aliases/",]
draft = false

[taxonomies]
category = [ "post",]
tags = [ "ruby", "blogspot",]

+++

Here's something I didn't know. When you override a method in a subclass, you
also need to redeclare any aliases for that method. Seems pretty obvious when
you think about it. I didn't think about it, though, and it caught me up for a
few minutes.
<!--more-->

I'd post a block of sample code, but I keep getting `"body, Malformed HTML found."`
errors from 43Things whenever I try to save with my code in there (`pre` tags and
all)
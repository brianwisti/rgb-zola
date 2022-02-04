+++
title = "I have one like somewhere"
date = "2020-02-18 21:41:44-08:00"
draft = false
aliases = [ "/note/2020/49/i-have-one-like-somewhere/", "/note/2020/02/i-have-one-like-somewhere/",]

[taxonomies]
category = [ "note",]
tags = [ "indieweb", "site",]

[extra.cover_image]
caption = "as of build time, anyways"
path = "cover.png"

+++

Been meaning to get [webmention](https://indieweb.org/Webmention)
integration for a *while*. Went the easy way, using
[webmention.io](https://webmention.io) and [brid.gy](https://brid.gy).
Easier than writing everything myself.

For now it’s just like counts, with a [Invoke](/tags/pyinvoke) task
checking my mentions feed at Hugo build time. More stuff is planned, but
first I decide how much information to show and from which sources. Not
every tweet reply is intended as a blog comment.
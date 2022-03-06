+++
title = "Geekish Update"
date = "2017-03-28 00:00:00-07:00"
draft = false
aliases = [ "/post/2017/geekish-update/", "/2017/03/28/geekish-update/", "/post/2017/03/geekish-update/",]

[taxonomies]
category = [ "post",]
tags = [ "personal", "site", "Marginalia",]

[extra]
card = "_card.webp"

[extra.cover_image]
caption = ""
path = "cover.jpg"

+++

I set up a space for myself in the basement.
This is now where I keep my desktop — running [Ubuntu](https://www.ubuntu.com/) at the moment.
Easy enough to get at from the laptop upstairs.
Maybe keep [Irssi](https://irssi.org/) running in a [Tmux](https://tmux.github.io/) session or something.

Oh, and just in case you want to know how the basement looked when we moved in, here’s a picture.

![The original basement](basement-original.jpg)

I like it better now.

What have I been coding in this workspace that looks a bit less like a horror movie scene than it did a few weeks ago?

I’m working on a `test` rule for this site.
Mainly I use it to check for bad links in an attempt to deal with [link rot](https://en.wikipedia.org/wiki/Link_rot).
The link checker is [Python](https://www.python.org/) with [Requests](http://docs.python-requests.org/en/master/),
and seeing if [Scrapy](https://scrapy.org/) can be useful in this context.
Scrapy seems like overkill at first glance, but it has middleware for respecting [`robots.txt`](http://www.robotstxt.org/).
I care about being a good Internet citizen.

I plan to write about that soon, since I enjoy the task so far.
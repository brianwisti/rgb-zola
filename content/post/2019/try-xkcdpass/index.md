+++
title = "Try xkcdpass"
description = "In which I suggest a password generator"
date = "2019-07-30 07:36:11-07:00"
draft = false
aliases = [ "/2019/07/30/try-xkcdpass/", "/post/2019/07/try-xkcdpass/",]

[taxonomies]
category = [ "post",]
tags = [ "linux", "security", "Tools",]

[extra]
card = "social_card.webp"

[extra.cover_image]
caption = "[XKCD 936](https://xkcd.com/936/) _([CC BY-NC 2.5](https://xkcd.com/license.html))_"
path = "cover.png"

+++

{% note(title="tl;dr:") %}
Use [xkcdpass][] to generate more secure passwords, like
“correcthorsebatterystaple”.

[xkcdpass]: https://pypi.org/project/xkcdpass/
{% end %}

This started as a [Note][note] but I passed my 15 minute rule — if I spend more
than 15 minutes on it, it should be a post — so here we are.

It won’t satisfy your bank’s silly password requirements, but — as [XKCD told
us][xkcd-told-us] — using a random collection of words for your password provides more
security than trying to [Leet-speak][leet-speak] some word with numbers and symbols.

You could pick a handful of words by flipping through the dictionary, but why
not let the computer do it for you? That’s where [xkcdpass][] comes in.

It’s probably available in your package repository.

    $ pacman -Ss xkcdpass

It’s just [Python][python], so you can use `pip` if you’re on macOS or Windows
or some other platform that doesn’t have `xkcdpass` handy.

    pip install xkcdpass

Regardless of how you install it, run it and grab the output — but let your
password manager remember it for you.

    $ xkcdpass
    tiara embezzle stack doorway scrambled imitate

[xkcdpass]: https://pypi.org/project/xkcdpass/
[note]: /note/
[xkcd-told-us]: https://xkcd.com/936/
[leet-speak]: https://simple.wikipedia.org/wiki/Leet
[python]: /tags/python
+++
title = "pared down to the base blog"
date = "2021-08-21 00:00:00-07:00"
draft = false
aliases = [ "/note/2021/08/pared-down-to-the-base-blog/",]

[taxonomies]
tags = [ "ssg", "site",]
category = [ "note",]

[extra]
card = "_card.webp"

[extra.cover_image]
caption = "My `rst.txt` files become HTML before the SSG sees, so I may leave them"
path = "cover.png"

+++

No more content shortcodes. No more — or at least not many — exotic content
formats. Embedded video or tweet? Copy and paste the embed code from the host
site. Need some fancy HTML for notes? Use raw HTML.

I need a base blog, with minimal dependencies on [Hugo][hugo] or any other
[SSG][ssg], so I can get serious with some of those others. "I'd need to port
all my shortcodes" has blocked me from switching for the last year and a half
(you accumulate a lot of cruft using the same site builder for six years). Now
it won't be such a blocker.

Plus, I can try the fancy stuff in [Astro][astro] or [Lektor][lektor] or
whatever and still have the base blog to fall back on. Heck, I could port the
base blog to [Eleventy][eleventy] or [Zola][zola] or …

[hugo]: https://gohugo.io
[ssg]: /tags/ssg
[astro]: https://astro.build
[lektor]: https://getlektor.com
[eleventy]: https://11ty.dev
[zola]: https://getzola.org

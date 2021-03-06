+++
title = "Installing Emacs Documentation on Pop OS"
description = "Apt spells \"emacs core docs\" as \"emacs-common-non-dfsg\"."
date = "2019-12-01 11:11:00-08:00"
updated = "2019-12-01 11:30:44-08:00"
draft = false
aliases = [ "/2019/12/01/installing-emacs-documentation-on-pop_os/", "/post/2019/12/installing-emacs-documentation-on-pop-os/",]

[taxonomies]
category = [ "post",]
tags = [ "emacs", "linux", "info", "Tools",]

[extra]
card = "social_card.webp"

[extra.cover_image]
caption = "Emacs Info (zoomed with `text-scale-adjust`)"
path = "cover.png"

+++

On a Linux flavor like [Ubuntu](https://ubuntu.com/) or
[Pop\!\_os](https://system76.com/pop) which uses
[`apt`](https://en.wikipedia.org/wiki/APT%5F\(software\)) for package
management? Trying to find the built-in documentation so you can read it
without going online? Install
[`emacs-common-non-dfsg`](https://packages.debian.org/jessie/emacs24-common-non-dfsg).

```bash
sudo apt install emacs-common-non-dfsg
```

It’s a license thing. The [GNU Project][gnu] distributes the core Emacs
[documentation][documentation] under the [GNU Free Documentation License][fdl].
[Debian][debian] decided [years ago][deb-vote] that the GFDL didn’t meet the [Debian
Free Software Guidelines][guidelines]. It’s still available – in the non-free repo –
though they gave it a name I’ll never remember unless I write it down somewhere.

[gnu]: https://www.gnu.org/
[documentation]: https://www.gnu.org/software/emacs/documentation.html
[fdl]: https://www.gnu.org/licenses/fdl-1.3.html
[debian]: https://www.debian.org/
[deb-vote]: https://www.debian.org/vote/2006/vote%5F001
[guidelines]: https://www.debian.org/social%5Fcontract#guidelines

That decision has rippled down over the years. Even though I haven’t
used Debian since the early 2000’s, I needed to know it today. Okay I
didn’t *need* to know it. I could have just read the [online
docs](https://www.gnu.org/manual/manual.html).

I always liked the [Info](https://www.gnu.org/software/texinfo/) reader
and consider it a significant feature when going through an Emacs phase.
Though yeah – it’s a bit archaic. Honestly that describes most of Emacs.
When I want featureful and flashy I can use [Visual Studio
Code](https://code.visualstudio.com/) or [Atom](https://atom.io/).

Not even a two hundred word post and I managed to digress. Ah well. Some
days are like that.
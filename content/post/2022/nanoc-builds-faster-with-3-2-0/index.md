---
title: Nanoc builds sites faster with 3.2.0
description: Ain't no benchmark like an unscientific ad hoc benchmark
date: "2022-12-25 11:38:45"
draft: false
category: post
cover_image:
  caption: just the numbers
  path: nanoc-build-time.png
tags:
- ruby
- nanoc
---


[ruby-32]: https://www.ruby-lang.org/en/news/2022/12/25/ruby-3-2-0-released/
[nanoc]: https://nanoc.app
[benchmarking]: https://www.solnic.dev/p/benchmarking-ruby-32-with-yjit

Today is Christmas, which means [Ruby 3.2.0][ruby-32] is out.
I read Peter Solnica's post about [Benchmarking Ruby 3.2 with
YJIT][benchmarking].
One bit of feedback he got was that YJIT --- the now official Just In Time
compiler --- kicks in for frequently called methods:

{{% quote
  from="Noah Gibbs"
  cite="https://ruby.social/@codefolio/109573860732354569" %}}
By default, YJIT optimises a method on the 30th time you call it.
{{% /quote %}}

Well hey.
The [Nanoc][nanoc] iteration of my site has a few hundred pages.
Nanoc probably calls some of its methods 30 or more times for that.
Let's find out if 3.2.0 makes a difference.

## I should probably install 3.2.0

This is in my Windows 11 + WSL2 workspace.
I wouldn't be surprised if Linux and macOS tests went faster.

Installed 3.2.0 on my system using `rbenv`.
Worth mentioning that I had to `export CC=/home/linuxbrew/.linuxbrew/bin/gcc-12`
for `rbenv install` to work at all.
For some reason I had a `brew`-installed Ruby floating around, too.
Removed that with `brew uninstall ruby` so `rbenv install 3.2.0` would work.

I have a very fiddly system.

## The "test"

1. Switch to the right version
2. Install dependencies for that version
3. Build the site
4. Build it again, to see how long things take when nothing's changed
5. Remove the build folder and move on to the next case

First in 3.1.3 to set a baseline of sorts.

```console
$ rbenv local 3.1.3
$ bundle
$ bundle exec nanoc
...
Site compiled in 50.39s.
$ bundle exec nanoc
Site compiled in 43.87s.
$ rm -r output/
```

[hugo]: https://gohugo.io

Don't judge those numbers too harshly.
Nanoc site configuration is Ruby code, and mine was very sloppy Ruby code.
Regardless, it's way slower than [Hugo][hugo].

Now in 3.2.0 without enabling YJIT, to see if just the plain old upgrade is
quicker.

```console
$ rbenv local 3.2.0
$ bundle
$ bundle exec nanoc
...
Site compiled in 43.58s.
$ bundle exec nanoc
...
Site compiled in 37.30s.
$ rm -r output/
```

There's variation from one invocation to the next in 3.1.3, but 3.2.0's first build
is consistently a sliver faster than 3.1.3's second build.

Finally with YJIT.

```console
$ RUBY_YJIT_ENABLE=1 bundle exec nanoc
...
Site compiled in 29.51s.
$ RUBY_YJIT_ENABLE=1 bundle exec nanoc
...
Site compiled in 23.28s.
```

That is an impressive difference.
We're still not talking Hugo numbers, of course.
But under 30 seconds means I might be able to pay attention long enough to fix
my terrible site configuration code.


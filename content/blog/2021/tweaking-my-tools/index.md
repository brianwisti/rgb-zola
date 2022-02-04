+++
title = "Tweaking my tools"
date = "2021-02-16 14:40:03-08:00"
draft = false
aliases = [ "/note/2021/02/tweaking-my-tools/",]

[taxonomies]
category = [ "note",]
tags = [ "ruby", "site",]

+++

[TTY Toolkit]: https://ttytoolkit.org

Playing a little more with [TTY Toolkit][] for the site workflow.
I wanted to say I'm tightening focus, but with a `require` list like this for one tool?

```ruby
require 'pastel'
require 'ruby-slugify'
require 'tty-editor'
require 'tty-exit'
require 'tty-logger'
require 'tty-option'
require 'tty-prompt'
require 'tty-screen'
```

"Tightening focus" would be a lie.

Anyways, it seems to function correctly. Huzzah! Now back to work.
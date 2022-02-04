+++
title = "asdf -- An extendable version manager"
date = "2021-03-23 00:00:00-07:00"
draft = false
aliases = [ "/bookmark/2021/03/asdf-vm-com/",]

[taxonomies]
category = [ "bookmark",]
tags = [ "tools", "shell", "version manager", "crystal",]

[extra.cite]
description = "An extendable version manager"
name = "asdf - An extendable version manager"
site = "https://asdf-vm.com"
url = "https://asdf-vm.com/#/"

+++

Installed mainly because `brew install|upgrade crystal` keeps having intermittent issues for me.

``` console
$ asdf plugin-add crystal https://github.com/asdf-community/asdf-crystal.git
$ asdf install crystal 1.0.0
Crystal 1.0.0 [dd40a2442] (2021-03-22)

LLVM: 10.0.0
Default target: x86_64-unknown-linux-gnu
```

All better.
+++
title = "OS X"
date = "2007-06-13 00:00:00-07:00"
updated = "2006-04-25 00:00:00-07:00"
draft = false
aliases = [ "/coolnamehere/2007/06/13_os-x.html", "/post/2007/os-x/", "/2007/06/13/os-x/", "/post/2007/06/os-x/",]

[taxonomies]
category = [ "post",]
tags = [ "os x", "macOS", "coolnamehere",]

+++

This is a dumping ground for anything I've figured out to make command line
existence on a Mac nearly as pleasant as sitting and looking at all the pretty
Aqua buttons. I'll organize it better if this page accumulates enough matter.
<!--more-->

## Installing from the command line

Here's how I installed [Free Pascal](http://www.freepascal.org/) from an `ssh`
session rather than going home, logging in, and using Finder.

This won't work in `screen` because of the way OS X handles things. It's
inconvenient, but it's also easy enough to detach your `screen` session for a
minute.

Obviously, downloading the dmg file was the first thing I did. I just used
the [ELinks](http://elinks.or.cz/) text mode web browser for that task.

    $ hdid fpc-3.1.4.powerpc-macosx.dmg
    $ cd /Volumes/fpc-2.1.4.powerpc-macosx/
    $ sudo installer -verbose -pkg fpc-2.1.4.powerpc-macosx.pkg -target /
    $ cd ~/
    $ hdiutil detach /Volumes/fpc-2.1.4.powerpc-macosx/
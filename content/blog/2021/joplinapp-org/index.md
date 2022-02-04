+++
title = "Joplin Note App"
date = "2021-02-15 00:00:00-08:00"
updated = "2021-10-21 00:00:00-07:00"
draft = false
aliases = [ "/bookmark/2021/02/joplinapp-org/",]

[taxonomies]
tags = [ "tools", "joplin", "second brain", "still working on my first brain",]
category = [ "bookmark",]

[extra.cite]
description = "an open source note taking and to-do application with synchronisation capabilities"
name = "Joplin"
site = "https://joplinapp.org"
url = "https://joplinapp.org"

+++

[open source]: https://github.com/laurent22/joplin/blob/dev/LICENSE

This one's worth bookmarking because it's [open source][], multi-platform
including mobile, extensible, and can be synchronized via multiple services.

[plugin]: https://discourse.joplinapp.org/c/plugins/18

Still haven't decided if it's my one true note-taking resource, or if there ever will be such a thing.
I wish there was setting synchronization too, but maybe there's a [plugin][] for that.

### General usage

[note format]: https://joplinapp.org/markdown/

* nodes can be notes or tasks, and you can toggle between them
* [note format][] is slightly tweaked variant of Github-Flavored Markdown
* default split pane approach w/editor on one side, working preview on the other
* has a rich editor, but that's not my style so I couldn't tell you how well it works
* drag and drop to create subnotebooks
* note links are via UUID-style hashes, so they'll persist when you move a linked note

### Plugins

[master list]: https://github.com/joplin/plugins/blob/master/README.md
[inline tags]: https://discourse.joplinapp.org/t/plugin-inline-tags/14192
[quick links]: https://discourse.joplinapp.org/t/quick-links-plugin/14214
[convert text to new note]: https://discourse.joplinapp.org/t/create-note-from-highlighted-text/12511
[automatic backlinks]: https://discourse.joplinapp.org/t/automatic-backlinks-with-manual-insert-option/13632
[Templates]: https://github.com/joplin/plugin-templates
[forum]: https://discourse.joplinapp.org/c/plugins/18

Check the [master list][] of plugins.
Check the [forum][] for discussions and announcements.

Here's what I'm using so far:

* [Templates]: daily journaling using a template and *Create note from template*
* [inline tags]: autocomplete existing tag links with `#`
* [quick links]: autocomplete note links with `@@`
* [automatic backlinks]: inserts list of links to notes that reference the *current* note
* [convert text to new note]: select, right click, bang. new note

### My Posts

[Joplin Terminal Basics]: /post/2021/04/joplin-terminal-basics/
[Journaling in Joplin With Raku]: /series/journaling-in-joplin-with-raku/

[Joplin Terminal Basics][]
: acquainting myself with the Joplin CLI

[Journaling in Joplin With Raku][]
: a series of posts on Journaling in Joplin from the command line with the {{< tag "raku-lang" >}} programming language
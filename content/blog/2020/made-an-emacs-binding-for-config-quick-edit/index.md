+++
title = "Made an Emacs Binding for Config Quick Edit"
date = "2020-05-07 14:30:00-07:00"
draft = false
aliases = [ "/note/2020/05/made-an-emacs-binding-for-config-quick-edit/",]

[taxonomies]
category = [ "note",]
tags = [ "emacs", "OrgConfig",]

+++

I hit `F5`, Emacs opens my
[`config.org`](/post/2020/04/from-dotfiles-to-org-file) for editing. It
might not be much but it feels good to scratch such a specific itch.
Feeling pretty good about myself.

``` elisp
(global-set-key (kbd "<f5>")
                (lambda ()
                  (interactive)
                  (find-file "~/.dotfiles/config.org")))
```
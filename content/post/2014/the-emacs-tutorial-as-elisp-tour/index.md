+++
title = "The Emacs Tutorial as ELisp Tour"
date = "2014-05-24 00:00:00-07:00"
draft = false
aliases = [ "/emacs/2014/05/24_the-emacs-tutorial-as-elisp-tour.html", "/post/2014/the-emacs-tutorial-as-elisp-tour/", "/2014/05/24/the-emacs-tutorial-as-elisp-tour/", "/post/2014/05/the-emacs-tutorial-as-elisp-tour/",]

[taxonomies]
category = [ "post",]
tags = [ "emacs", "elisp", "tutorial", "tools",]

+++

[GNU Emacs]: https://www.gnu.org/software/emacs
I am trying to *really* learn how to use [GNU Emacs][]. One thing that
strikes me is how the Emacs user interface can be thought of as a
client application to an Emacs Lisp API. This is not a revolutionary
thought, but it really stuck in my head. I reread the official
tutorial, focusing on the functions rather than the keybindings that
invoke them.
<!--more-->

The first function is obviously the one to get the tutorial started.

 Function             | Keybinding | Description
----------------------|------------|-----------------------------------------
 `help-with-tutorial` | `C-h t`    | Launch the Emacs learn-by-doing tutorial 

Then I spent a couple days with liberal usage of ~describe-key~ and
~describe-function~ to better understand what the tutorial was
describing. It was helpful. Now I just want to organize those notes
and post them on the blog.

[dump the list]: /post/2014/05/elisp-functions-described-in-the-emacs-tutorial

Or I could [dump the list][] onto a blog post.
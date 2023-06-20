+++
title = "Testing Justfile Recipe Arguments"
date = "2022-12-05"
description = "In which I make my justfile just a little fancier"
draft = false

[taxonomies]
category = ["post",]
tags = [
  "site",
  "just"
]
+++

{% tldr() %}
```justfile
add TITLE:
  bundle exec ruby _scripts/add-post --title '{{ TITLE }}'
```
{% end %}

Time to fiddle with my site setup some more.

[hugo]: https://gohugo.io

My site posts are organized by file slug: simplified file paths based on a title.
[Hugo][hugo] itself directly supports creating new content by path.

```sh
hugo new content/post/2022/testing-justfile-recipe-arguments/index.adoc.txt
```

It takes thinking to map from a title to a slug.
Sometimes I'm not in the mood for that kind of thinking.
And I'm not always great about consistency in my slug choices.

[tty-toolkit]: https://ttytoolkit.org
[ruby]: https://ruby-lang.org

So I use a [Ruby][ruby] script to streamline adding new posts.
I won't talk about that today.
Maybe another day.
All it does is use [TTY::Toolkit][tty-toolkit] to save me a couple seconds of thought compared to `hugo new`,
then fires up `$EDITOR` for me so I don't have to think about that either.
Sometimes two seconds is the difference between writing an impulse post and writing a tweet.

Right now the script needs a `--title` string it can use for frontmatter and file slug.

```sh
bundle exec ruby _scripts/add-post --title 'Testing Justfile Recipe Arguments'
```

[just]: https://just.systems

I don't have to figure out the slug, but it's still rather tedious.
I use {just}[just] to simplify those tedious site tasks.
Putting the repeated bits of this invocation in a recipe — that's what `just` calls tasks —
would cut down on the tedium.
What about the title?
Started thinking about TTY::Toolkit interactive prompts.
Maybe some other time, because `just` lets you specify arguments for a recipe.

```justfile
add TITLE:
  bundle exec ruby _scripts/add-post --title '{{ TITLE }}'
```

Now I can `just add` a post.

```sh
just add 'Testing Justfile Recipe Arguments'
```

And here we are!

I use a couple other Ruby scripts.
Might as well refactor that `bundle exec ruby`.

```justfile
ruby := 'bundle exec ruby'

add TITLE:
  {{ ruby }} _scripts/add-post --title '{{ TITLE }}'
```

All right.
This is better than what I had before.
Sure I've got multiple helpful layers to track now.
That'll bite me if I get carried away.
On the other hand, I actually wrote something for the site today.

Sometimes two seconds makes the difference.

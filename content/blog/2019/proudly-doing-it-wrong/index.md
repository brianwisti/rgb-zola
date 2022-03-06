+++
title = "Proudly doing it wrong"
date = "2019-08-11 20:04:00-07:00"
draft = false
aliases = [ "/note/2019/223/proudly-doing-it-wrong/", "/note/2019/08/proudly-doing-it-wrong/",]

[taxonomies]
category = [ "note",]
tags = [ "screenshot", "javascript", "no i know", "i'll fix it",]

[extra]
card = "_card.webp"

[extra.cover_image]
caption = "Yeah that's Visual Studio Code. I'm trying new things."
path = "cover.png"

+++

1. write a [site weight][] script that prints a report to the console
2. make the script write the report to a file, and include the file in [/now][]. Now site building looks like:
    1. build the site
    2. weigh the site
    3. build the site and include the new report
    4. upload!
3. (today) make the script write the info as JSON instead
4. throw in some [vue.js][] to fetch the JSON and reproduce the original report format almost exactly.
5. profit?

But hey at least I don't need to rebuild the site after weighing it. And when free time next allows I'll learn
a little more Vue.js and make the report prettier.

[site weight]: /post/2019/06/weighing-files-with-python/
[/now]: /now
[vue.js]: https://vuejs.org/
+++
title = "New PageTemplate Release"
date = "2006-01-07 00:00:00-08:00"
aliases = [ "/blogspot/2006/01/07_i-snuck-out-couple-of-new-pagetemplate.html", "/post/2006/i-snuck-out-couple-of-new-pagetemplate/", "/2006/01/07/new-pagetemplate-release/", "/post/2006/01/new-pagetemplate-release/",]
draft = false

[taxonomies]
category = [ "post",]
tags = [ "pagetemplate", "blogspot",]

+++

I snuck out a couple of new PageTemplate releases over the last week. There were no significant changes. The main bugfix is that PT should now work okay in an environment where $SAFE > 0. This means you can finally use stock PageTemplate in your mod_ruby projects. I don't have any major plans for PT in the near future. I really need to improve the tests, so I can know for sure that the package does what it's currently advertised to do. Much later, I want to split the library into components so that people who want the bare minimum can use a PageTemplate::Core module which would be equivalent to PT 0.3.2.
<!--more-->
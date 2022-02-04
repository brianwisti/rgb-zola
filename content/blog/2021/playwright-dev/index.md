+++
title = "Playwright for Python"
date = "2021-02-28 00:00:00-08:00"
draft = false
aliases = [ "/bookmark/2021/02/playwright-dev/",]

[taxonomies]
tags = [ "python", "testing", "browser testing",]
category = [ "bookmark",]

[extra.cite]
description = "Cross-browser end-to-end testing for modern web apps"
name = "Playwright for Python"
site = "https://playwright.dev"
url = "https://playwright.dev/python/"

+++

[Playwright]: https://playwright.dev/python/

A Python interface to the very handy [Playwright][] browser automation library.
The 1.9.x releases feel more Pythonic.
Naming conventions, stuff like that.
Feels much less like just a wrapper.

Don't forget to install browser drivers whenever you install or upgrade Playwright!

    $ python -m playwright install

## With pytest

[pytest-playwright]: https://github.com/microsoft/playwright-pytest
[pytest-django]: https://pytest-django.readthedocs.io/en/latest/index.html

The [pytest-playwright][] plugin provides fixtures, marks, and extra `pytest` args for browser testing.
So far the only fixture I've used is `page`, the standin for a default browser session.
Pairs nicely with [pytest-django][]'s `live_server` fixture.

Headless by default, but use `pytest --headful` if you want to watch the browser do its thing.

<div class="admonition note">
<p class="admonition-title">Note</p>

Since pytest-playwright is still in *early* days --
0.0.12 as of this bookmark date --
dependency managers might not acknowledge new releases.
Watch the repo and manually update your dependencies when you see a new release.

</div>
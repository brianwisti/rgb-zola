+++
title = "Mp4Info issues"
date = "2007-02-12 00:00:00-08:00"
updated = "2015-03-28 00:00:00-07:00"
draft = false
aliases = [ "/blogspot/2007/02/12_mp4info-issues.html", "/post/2007/mp4info-issues/", "/2007/02/12/mp4info-issues/", "/post/2007/02/mp4info-issues/",]

[taxonomies]
category = [ "post",]
tags = [ "ruby", "blogspot",]

+++

<!--more-->
<aside>
<p>Update 2015-03-28

<p>No idea whether this is still true, or even if it was just something stupid I was doing in 2007.
</aside>

[mp4info]: https://github.com/arbarlow/ruby-mp4info

[mp4info][] thinks that my 5 minute Bob Newhart track is 2 seconds long. Looks like that is an issue on several tracks. I need to dig into that, see why Perl's MP4::Info picks up the correct length but the Ruby counterpart does not.
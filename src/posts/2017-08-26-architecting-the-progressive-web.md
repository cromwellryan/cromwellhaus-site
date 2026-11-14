---
title: "Architecting the Progressive Web"
date: "2017-08-26"
slug: "architecting-the-progressive-web"
categories: ["Uncategorized"]
tags: []
original_urls: ["http://cromwellhaus.com/2017/08/architecting-the-progressive-web/", "https://cromwellhaus.com/2017/08/architecting-the-progressive-web/"]
wayback_source: "https://web.archive.org/web/20170929222817/https://cromwellhaus.com/"
excerpt_only: false
permalink: "/2017/08/architecting-the-progressive-web/"
---

Building a great web is something the [Sparkbox](https://seesparkbox.com) takes very personally. We built what we believe is one of the first RWD e-commerce sites. We constantly battle to improve performance while delivering a great experience, even [for those with a terrible connection](https://twitter.com/cromwellryan/status/748328361441771521). We know we will always be swimming up stream, but today, we believe we have a reasonable architecture for building a progressive web experience that is blazing fast and works for even the most lame devices and connections.

The crazy thing about this architecture is that it’s not terribly interesting. Essentially, we let the web do it’s thing. Javascript not happing, because you stepped into an elevator or happen to run a super old version of IE (we made that choice)? No worries. We server render all the things, accept form POSTs for all mutating interactions, and serve up PNGs instead of SVGs. [Time to First Interaction](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive) a little slow? No problem – we’ll disable certain elements to save up for the important stuff.

We’ve been exploring parts of this architecture for a few years now, but this past year we’ve been able to put it all together. Throughout the next year, we’re going to be sharing how we’ve done so in the hopes that we can spur on great experiences across the web.

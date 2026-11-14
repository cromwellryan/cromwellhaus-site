---
title: "Google Gears"
date: "2007-05-31"
slug: "google-gears"
categories: ["Software Reviews"]
tags: ["Software Reviews"]
original_urls: ["http://blog.cromwellhaus.com/2007/05/google-gears/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/05/31/google-gears.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/05/31/google-gears.aspx"]
wayback_source: "https://web.archive.org/web/20080118081529/http://cromwellhaus.com:80/blogs/MainFeed.aspx"
excerpt_only: false
permalink: "/2007/05/google-gears/"
---

I'm not entirely sure what to think of [Google Gears](http://code.google.com/apis/gears/index.html "Google Gears").  It seems most people are focusing on the [Database](http://code.google.com/apis/gears/api_database.html) portion of the stack, but it's the [LocalServer](http://code.google.com/apis/gears/api_localserver.html) portion that has me confused.  Does this not reek of complexity and severe duplication?

After first reading through the [LocalServer Overview](http://code.google.com/apis/gears/api_localserver.html#overview) I thought, cool, this thing is going to serve up my server app when the client is offline.  That's kind of sweet, but how do they know what pages people are going to need?  I sure hope they don't cache on demand, because that breaks down with the first button I click?  Maybe they crawl my pages and pick up links, that *might* work.  Well, it turns out you have to tell them up front what pages to cache either via a [Manifest file](http://code.google.com/apis/gears/api_localserver.html#manifest_file) or via their [LocalServer API](http://code.google.com/apis/gears/api_localserver.html#LocalServer).  Manifest file is cool I guess, there will undoubtedly be server-side tools to generate these.

What happens if my client's browser has caching disabled or your page's client side cache expires?  How do you get to the first page that loads the Gears API and starts loading the Gears Cache?  Maybe I'm missing something here.

I think I can handle all link activity and user actions requesting pages from the LocalServer.  I'm sure that stuff can be wrapped into our AJAX frameworks; I'm sure [Google's Web Toolkit](http://code.google.com/webtoolkit/) will soon enough.  What about Mashups' though?  Aren't we supposed to be pulling data from site A and displaying it with relevant information from our site?  Is everyone going to start caching everyone else's data?

But, heck, it's not like any of the [RIA](http://www.google.com/search?hl=en&q=RIA+rich+application&btnG=Search "Rich Internet/Interactive Applications") platforms out there today are doing any better at providing infrastructure to move the Internet App as is to the offline client.  This seems like a decent start.  I personally like the idea of having two different targets: client or web, while providing a different targeted experience for either.  We have too much horsepower and money invested in our personal computers to waste it on a serving local web pages.

We'll see.  It's still only beta.



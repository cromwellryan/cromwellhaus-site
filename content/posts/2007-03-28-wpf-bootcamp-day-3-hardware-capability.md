---
title: "WPF Bootcamp Day 3 - Hardware capability"
date: "2007-03-28"
slug: "wpf-bootcamp-day-3-hardware-capability"
categories: [".Net", "WPF"]
tags: [".Net", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/03/wpf-bootcamp-day-3-hardware-capability/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/03/28/wpf-bootcamp-day-3-hardware-capability.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/03/28/wpf-bootcamp-day-3-hardware-capability.aspx"]
wayback_source: "https://web.archive.org/web/20080511025516/http://cromwellhaus.com:80/blogs/ryanc/archive/2007/03/28/wpf-bootcamp-day-3-hardware-capability.aspx"
excerpt_only: false
permalink: "/2007/03/wpf-bootcamp-day-3-hardware-capability/"
---

To avoid disappointing users after they've gotten as far as running your application on their 1997 300mhz Pentium II, determine their capabilities using the [RenderCapability.Tier](http://msdn2.microsoft.com/en-us/library/system.windows.media.rendercapability.tier.aspx) value before hand and notifying them that they'll need to joing the 21st century before running your app.

[Henry Hahn](http://blogs.msdn.com/henryh/archive/2006/08/23/719568.aspx "RenderCapabilities.Tier") has a quick overview and, the always welcome, code samples of using this value to make your application conform to the different tiers.

Don't forget your bit shifting, cause the Tier is set up to support new Tiers/platforms in future releases.

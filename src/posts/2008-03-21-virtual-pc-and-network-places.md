---
title: "Virtual PC and Network Places"
date: "2008-03-21"
slug: "virtual-pc-and-network-places"
categories: ["Networking", "Virtual PC"]
tags: ["Networking", "Virtual PC"]
original_urls: ["http://blog.cromwellhaus.com/2008/03/virtual-pc-and-network-places/", "http://cromwellhaus.com/blogs/ryanc/archive/2008/03/21/virtual-pc-and-network-places.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/03/21/virtual-pc-and-network-places.aspx"]
wayback_source: "https://web.archive.org/web/20080511100454/http://cromwellhaus.com:80/blogs/ryanc/archive/2008/03/21/virtual-pc-and-network-places.aspx"
excerpt_only: false
permalink: "/2008/03/virtual-pc-and-network-places/"
---

I use Virtual PC a lot, especially for development.  I try to emulate a mini-infrastructure of how I'll be deploying my solutions, so no SQL Server on my box, no IIS on my box, etc.  To support this I use [Virtual PC Guy's](http://blogs.msdn.com/virtual_pc_guy/) [steps](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/04/477195.aspx) for enabling communication between my host and the VPC's.  If you are on an Active Directory environment this can have a pretty negative impact on name resolution, specifically when browsing through "My Network Places" (XP) or just "Network" (Vista).  [![image](http://cromwellhaus.com/blogs/ryanc/WindowsLiveWriter/VirtualPCandNetworkPlaces_978C/image_thumb_1.png)](http://cromwellhaus.com/blogs/ryanc/WindowsLiveWriter/VirtualPCandNetworkPlaces_978C/image_4.png)If you are running into this and it bugs you, go into your Microsoft Loopback Adapter properties and disable/uncheck "Client for Microsoft Networks".  I personally disable everything except Virtual Machine Network Services and IPv4 since this just a small private network running on my computer.

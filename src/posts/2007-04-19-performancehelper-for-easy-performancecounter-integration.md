---
title: "PerformanceHelper for easy PerformanceCounter integration"
date: "2007-04-19"
slug: "performancehelper-for-easy-performancecounter-integration"
categories: [".Net", "Performance"]
tags: [".Net", "Performance"]
original_urls: ["http://blog.cromwellhaus.com/2007/04/performancehelper-for-easy-performancecounter-integration/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/04/19/performancehelper-for-easy-performancecounter-integration.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/04/19/performancehelper-for-easy-performancecounter-integration.aspx", "https://cromwellhaus.com/2007/04/performancehelper-for-easy-performancecounter-integration/"]
wayback_source: "https://web.archive.org/web/20081122024431/http://cromwellhaus.com/blogs/ryanc/archive/2007/04/19/performancehelper-for-easy-performancecounter-integration.aspx"
excerpt_only: false
permalink: "/2007/04/performancehelper-for-easy-performancecounter-integration/"
---

In the [Speedy Rewards](http://www.speedyrewards.com "Speedway SpeedyRewards™") team here we use custom [PerformanceCounters](http://msdn2.microsoft.com/en-us/library/system.diagnostics.performancecounter.aspx) quite extensively to monitor and trend our host systems.  You may not know, but our rewards program implements real-time host integration for transactions that are Id'ed as a [SpeedyRewards](http://www.speedyrewards.com) member such that systems like the in-store kiosk, [www.SpeedyRewards.com](http://www.SpeedyRewards.com), and any other store you may soon visit can accurately reflect balance updates immediately.  With 1600+ stores doing this and a sub-1 second response time, we need to keep a close eye on things.

Today I was trying to do some preliminary performance profiling on our new WCF based messaging infrastructure.  To make my life a little easier, I put together a PerformanceHelper class that I actually modeling off the Tracer class found in the [Enterprise Library 1.1](http://www.microsoft.com/downloads/details.aspx?familyid=a7d2a109-660e-444e-945a-6b32af1581b3&displaylang=en).  To use it, you wrap a section of code you wish to monitor performance for with the following:

> ```
> using(new PerformanceHelper(CATEGORY, "<BlockInstanceName>") )
> {
>     //...
> }
> ```

This will provide you with a [RateOfCountsPerSecond32](http://msdn2.microsoft.com/en-us/library/system.diagnostics.performancecountertype.aspx) counter and an [AverageTimer32](http://msdn2.microsoft.com/en-us/library/system.diagnostics.performancecountertype.aspx) counter called "Operations/sec\<BlockInstanceName>" and "Average Time/Operation\<BlockInstanceName>" respectively.  You can download the [PerformanceHelper class here](http://cromwellhaus.com/files/folders/netcode/entry172.aspx "PerformanceHelper.cs") and a [sample project here](http://cromwellhaus.com/files/folders/netcode/entry173.aspx "Performance Helper Sample Project").

Feel free to use and abuse it, but be aware that this has not fully tested and may well contain bugs.  *I provide NO warranty or guarantees*, so don't come to me when your server blue-screens from a corrupt registry (not that I've ever done that).  Use at your own peril.

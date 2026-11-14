---
title: "WPF Controls TabIndex: Moving to the First Input Control"
date: "2007-10-25"
slug: "wpf-controls-tabindex-moving-to-the-first-input-control"
categories: [".Net", "WPF"]
tags: [".Net", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/10/wpf-controls-tabindex-moving-to-the-first-input-control/", "http://blog.cromwellhaus.com:80/index.php/2007/10/wpf-controls-tabindex-moving-to-the-first-input-control", "http://blog.cromwellhaus.com:80/index.php/2007/10/wpf-controls-tabindex-moving-to-the-first-input-control/comment-page-1/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/10/25/wpf-controls-tabindex-moving-to-the-first-input-control.aspx", "http://cromwellhaus.com:80/2007/10/wpf-controls-tabindex-moving-to-the-first-input-control", "http://cromwellhaus.com:80/2007/10/wpf-controls-tabindex-moving-to-the-first-input-control/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/10/25/wpf-controls-tabindex-moving-to-the-first-input-control.aspx"]
wayback_source: "https://web.archive.org/web/20091020123026/http://blog.cromwellhaus.com:80/index.php/2007/10/wpf-controls-tabindex-moving-to-the-first-input-control"
excerpt_only: false
permalink: "/2007/10/wpf-controls-tabindex-moving-to-the-first-input-control/"
---

Here’s one of those real-world situations that no one bothers to demo.  If you are building a form or have some sort of input your gathering from the user, you’ll likely want the first input control Focused initially.  You have a few ways to do this (in ascending order of recommendation):

1. Call Focus() on the first control explicitly (meh).
2. Iterate the controls collection and find the lowest TabIndex (terrible [code smell](http://en.wikipedia.org/wiki/Code_smell)).
3. Do the following in the Load event:

> ```
> this.MoveFocus(new TraversalRequest(FocusNavigationDirection.Next));
> ```

- [Previous Entry: Lap Around WPF @ CONDG](/2007/09/lap-around-wpf-codng/)
- [Next Entry: PerformanceHelper.cs Update: Perfmon, Console, and Debug Output options](/2007/10/performancehelper-cs-update-perfmon-console-and-debug-output-options/)

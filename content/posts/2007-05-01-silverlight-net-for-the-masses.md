---
title: "Silverlight: .Net for the masses"
date: "2007-05-01"
slug: "silverlight-net-for-the-masses"
categories: [".Net", "Silverlight", "WPF"]
tags: [".Net", "Silverlight", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/05/silverlight-net-for-the-masses/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/05/01/silverlight-net-for-the-masses.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/05/01/silverlight-net-for-the-masses.aspx"]
wayback_source: "https://web.archive.org/web/20080118081529/http://cromwellhaus.com:80/blogs/MainFeed.aspx"
excerpt_only: false
permalink: "/2007/05/silverlight-net-for-the-masses/"
---

While up in Redmond for the [WPF Bootcamp](/2007/03/wpf-bootcamp-day-1/), we had a short time to work with some of the WPF/E, now [Silverlight](http://msdn.microsoft.com/silverlight/ "Silverlight"), team members.  At the time Silverlight didn't make a whole lot of sense in our strategy.  That said, I hope everyone sees the great potential that comes from some of the features surrounding [Silverlight 1.1](http://go.microsoft.com/fwlink/?linkid=89145&clcid=0x409) specifically.

Let's put this into context. Over the last couple of years, true web-based applications have really started to take shape.  I'm talking [Google Docs & Spreadsheets](http://docs.google.com/), [Yahoo! Local](http://local.yahoo.com), [Yahoo! Pipes](http://pipes.yahoo.com/pipes/) and not YouTube, which is a glorified photo sharing site.  A bevy of [AJAX toolkits](http://ajaxpatterns.org/wiki/index.php?title=AJAXFrameworks) have attempted to fill the enormous development gap between LCD-JavaScript and C#, Java, VB, Ruby, and Python, but there is only so much one can do with JavaScript before you go crazy.

Now imagine some "real" applications that actually attempt to provide a full feature set which accentuates an existing web model.  My favorite example is [Shutterfly Studio](http://www.shutterfly.com/studio/overviews.jsp).  They probably could have given you 20% of the Collage functionality with some goofy JavaScript or lots of uploading and postbacks, but how long would you wait around for your photos to upload while trying out different layouts?  Not long I'd imagine.  This is where Silverlight comes in.

Silverlight takes the untold story of Java and actually runs with it by providing a consolidated branch of the full .Net CLR, including JITter, Garbage-Collector, BCL, Threading namespace, Network stack and more.  Well this is all well and good, but why not just use Flash?  Well, if you want to deploy a Flash application, you are forced to use [ActionScript](http://en.wikipedia.org/wiki/Talk:ActionScript/rewrite), which doesn't provide nearly the feature set of .Net nor is it useful in any other environment other than Flash, so your experience is isolated.  Flash also doesn't provide the huge WCF communications platform for secure, transport independent communications, WPF for rich interactive media, and one of the most powerful IDE platforms in [Visual Studio.](http://msdn.microsoft.com/vstudio/eula.aspx?id=c8bf88e7-841c-43fd-c63d-379943617f36)

Imagine starting your family collage with [Shutterfly Studio](http://www.shutterfly.com/studio/overviews.jsp) at home on your laptop, getting to work in the morning and flipping through real layouts with your pictures at work (lunch of course) and then sending your parents a link to the catalog of pictures where they can browse any layout and order their own version of the collage?  No Shutterfly Studio desktop icon or Start Menu shortcut.  Just a one time 20 second download of the Silverlight CLR - yeah the Silverlight CLR is only 4mb.  That's what removing 90% of the [named color members in System.Drawing.Color](http://msdn2.microsoft.com/en-us/library/system.drawing.color_members.aspx) and asking people to look up the HEX value.

Have fun.

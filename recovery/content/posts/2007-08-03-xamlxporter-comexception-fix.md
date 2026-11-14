---
title: "XamlXporter COMException Fix"
date: "2007-08-03"
slug: "xamlxporter-comexception-fix"
categories: ["Software Reviews", "WPF"]
tags: ["Software Reviews", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/08/xamlxporter-comexception-fix/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/08/03/xamlxporter-comexception-fix.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/08/03/xamlxporter-comexception-fix.aspx"]
wayback_source: "https://web.archive.org/web/20080118081529/http://cromwellhaus.com:80/blogs/MainFeed.aspx"
excerpt_only: false
permalink: "/2007/08/xamlxporter-comexception-fix/"
---

There is a pretty cool, but curiously quiet, [CodePlex](http://www.codeplex.com) project called [XamlXporter](http://www.codeplex.com/xamlxporter) that allows you to export [Adobe Illustrator](http://www.adobe.com/products/illustrator) files/resources to WPF files.  This is a great thing since WPF is young and there are a lot of free resources and tutorials for Adobe Illustrator out there, as well as, you will probably find that design firms are going to use Illustrator before [Blend](http://www.microsoft.com/expression/products/overview.aspx?key=blend) for quite while.

The current version of Illustrator is C3, but the current/latest version of XamlXporter is built for C2.  Apparently Adobe has updated the GUID for Illustrator's COM Type Library, so the XamlXporter won't work with C3.  Here's how I fixed it:

1. Install Illustrator.  There is a 30-day trial version [here](http://www.adobe.com/go/tryillustrator).
2. Download XamlXporter (0.2 Alpha is [here](http://www.codeplex.com/xamlxporter/Release/ProjectReleases.aspx?ReleaseId=1551)).
3. Open Visual Studio 2005 (you can probably use 2008/Orcas, but I didn't).
4. Create a new project (I used C# Console), but I'm sure VB WinForms, etc will work just as well.
5. Add a COM Reference to Adobe Illustrator C3 Type Library.
6. Browse to the &lt;project>\\bin\\Debug|Release directory and copy the Interop.Illustrator.dll to the XamlXporter binary directory.
7. Start up the XamlXporter according to the instructions and Voila!

If you're lazy, you can download the Interop assembly I created [here](http://cromwellhaus.com/files/folders/wpf/entry220.aspx)

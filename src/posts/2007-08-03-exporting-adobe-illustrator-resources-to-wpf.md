---
title: "Exporting Adobe Illustrator resources to WPF"
date: "2007-08-03"
slug: "exporting-adobe-illustrator-resources-to-wpf"
categories: ["WPF"]
tags: ["WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/08/exporting-adobe-illustrator-resources-to-wpf/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/08/03/exporting-adobe-illustrator-resources-to-wpf.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/08/03/exporting-adobe-illustrator-resources-to-wpf.aspx"]
wayback_source: "https://web.archive.org/web/20080118081529/http://cromwellhaus.com:80/blogs/MainFeed.aspx"
excerpt_only: false
permalink: "/2007/08/exporting-adobe-illustrator-resources-to-wpf/"
---

There are a lot of sites out there with great vector resources provided in [Adobe Illustrator](http://www.adobe.com/products/illustrator/) files.  A few have taken a stab at creating exporters or converts, including [Mike Swanson](http://www.mikeswanson.com/xamlexport/) and a [CodePlex.com](http://www.codeplex.com) project called [XamlXporter](http://www.codeplex.com/xamlxporter).

I tried out Mike's XamlExport plugin and it worked fairly well, but he has some [well documented](http://www.mikeswanson.com/xamlexport/Eye%20Candy.htm) items that aren't supported which seem to be pretty common in the AI world.  This lead me to try the XamlXporter which was built for Illustrator C2.  C3 is the latest version and I'm using the 30-day trial.  XamlXporter uses the Illustrator COM Type Library, but apparently Adobe changed the COM GUID for this release.  It was pretty easy to resolve and I've got another post [here](/2007/08/xamlxporter-comexception-fix/) showing you how to fix that.

Here are some pretty nice sites with some Illustrator Vector resources you can use, but beware of the conversion gotcha's.  WPF is young and Illustrator is, err, mature, so not everything has a translation.

- [http://www.vecteezy.com/](http://www.vecteezy.com/ "http://www.vecteezy.com/")
- [http://tutorialblog.org/free-vector-downloads/](http://tutorialblog.org/free-vector-downloads/ "http://tutorialblog.org/free-vector-downloads/")

I think we really need a site where people can upload and share WPF resources.  This would be great for styles, templates, etc. which can be time consuming and difficult for non-design people like I.

---
title: "WPF Bootcamp Day 1 - Visual Studio \"Orcas\" Demo"
date: "2007-03-26"
slug: "wpf-bootcamp-day-1-visual-studio-quot-orcas-quot-demo"
categories: [".Net", "WPF"]
tags: [".Net", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/03/wpf-bootcamp-day-1-visual-studio-quot-orcas-quot-demo/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/03/26/wpf-bootcamp-day-1-visual-studio-quot-orcas-quot-demo.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/03/26/wpf-bootcamp-day-1-visual-studio-quot-orcas-quot-demo.aspx"]
wayback_source: "https://web.archive.org/web/20090106013018/http://cromwellhaus.com/blogs/ryanc/archive/2007/03/26/wpf-bootcamp-day-1-visual-studio-quot-orcas-quot-demo.aspx"
excerpt_only: false
permalink: "/2007/03/wpf-bootcamp-day-1-visual-studio-quot-orcas-quot-demo/"
---

We moved past the introductions quickly and are getting down and dirty.  [Rob Relyea](http://rrelyea.spaces.live.com/) took us through the basics of WPF from the latest [Visual Studio Orcas](http://www.microsoft.com/downloads/details.aspx?FamilyID=1ff0b35d-0c4a-40b4-915a-5331e11c39e6&DisplayLang=en) perspective.  Starting simple by creating a button via Xaml and a duplicate example using purely C# code.  I've posted a copy of the sample [here](http://cromwellhaus.com/files/folders/wpf/entry147.aspx) for Visual Studio 2005 with the [WPF Extensions](http://www.microsoft.com/downloads/details.aspx?FamilyId=F54F5537-CC86-4BF5-AE44-F5A1E805680D&displaylang=en).

One of the interesting new classes for you code junkies is the [ObservableCollection](http://msdn2.microsoft.com/en-us/library/ms668604.aspx) class available now in .Net 3.0.  This class implements the [INotifyPropertyChanged interface](http://msdn2.microsoft.com/en-us/library/system.componentmodel.inotifypropertychanged.aspx) allowing the dynamic databinding in WPF.  This is cool for all sorts of reasons, but specifically because we can use this dynamic, event based collections infrastructure for in memory lists of more than your list of employee names, but also videos, complex business objects like product definitions, pages in a book that you are rendering, or files in a directory which you are monitoring.

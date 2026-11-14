---
title: "Vista Sidebar Gadget Developer Experience"
date: "2007-05-02"
slug: "vista-sidebar-gadget-developer-experience"
categories: ["Vista Sidebar"]
tags: ["Vista Sidebar"]
original_urls: ["http://blog.cromwellhaus.com/2007/05/vista-sidebar-gadget-developer-experience/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/05/02/vista-sidebar-gadget-developer-experience.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/05/02/vista-sidebar-gadget-developer-experience.aspx"]
wayback_source: "https://web.archive.org/web/20080118081529/http://cromwellhaus.com:80/blogs/MainFeed.aspx"
excerpt_only: false
permalink: "/2007/05/vista-sidebar-gadget-developer-experience/"
---

Vista Sidebar Gadgets can be cool, but the developer experience out of the box is severely lacking.  Microsoft doesn't provide a Visual Studio project template, so [Tim Heuer](http://timheuer.com/blog) was nice enough to [provide one](http://timheuer.com/blog/archive/2007/03/11/14010.aspx "Vista Sidebar Gadget Visual Studio Template") for us.  He does so via a Web Site template, which makes sense since a Sidebar gadget is nothing more than [an Html page with a splash of JavaScript](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/sidebar/sidebar/overviews/gdo.asp), minimally, of course.  If you are like me, you like to be able to touch something up and then look at it, but I'm not about to edit, copy, run every time I want to see what my little icon change has affected.  Here's a tip to help you out: create a symbolic link in your *%userprofile%\\AppData\\Local\\Microsoft\\Windows Sidebar\\Gadgets* directory.  Here's how:

1. Run Command Prompt as an Administrator
2. mklink /D "%userprofile%\\AppData\\Local\\Microsoft\\Windows Sidebar\\Gadgets\\&lt;gadgetname>.gadget" "%userprofile%\\Documents\\Visual Studio 2005\\WebSites\\&lt;VisualStudioProjectDirectory>"

[![](http://cromwellhaus.com/blogphotos/VistaSidebarGadgetDeveloperExperience_14258/image0_thumb22.png)](http://cromwellhaus.com/blogphotos/VistaSidebarGadgetDeveloperExperience_14258/image031.png)

This allows you to keep your projects where they belong (VS won't let you open a folder in AppData without jumping some hoops anyway) and still reload your Gadget in Sidebar whenever you make changes.

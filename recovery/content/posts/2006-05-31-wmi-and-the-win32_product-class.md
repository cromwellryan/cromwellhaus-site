---
title: "WMI and the Win32_Product Class"
date: "2006-05-31"
slug: "wmi-and-the-win32_product-class"
categories: [".Net"]
tags: [".Net"]
original_urls: ["http://blog.cromwellhaus.com/2006/05/wmi-and-the-win32_product-class/", "http://cromwellhaus.com/blogs/ryanc/archive/2006/05/31/66.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2006/05/31/66.aspx"]
wayback_source: "https://web.archive.org/web/20090106031651/http://cromwellhaus.com/blogs/ryanc/archive/2006/05/31/66.aspx"
excerpt_only: false
permalink: "/2006/05/wmi-and-the-win32_product-class/"
---

Our build process is pretty seamless all the way through to an Integration environment which sits right between Development (laptop/workstation) and Certification (keep your muddy paws off land).  With this automation and continuous integration in general, comes a large amount of excess in the form of intermediate versions.  During a recent upgrade to Window 2003 (don’t ask why it took so long) we found that the little utility that keeps this Integration environment clean started getting fussy.  Well it turns out that you have to install the WMI Windows Installer Provider explicitly.  Here’s how to find it:

1. Control Panel – Add or Remove Programs
2. Add/Remove Windows Components
3. Select Management and Monitoring Tools
4. Click Details
5. Check the *WMI Windows Installer Provider* subcomponent
6. Click Ok
7. Click Next
8. Do a jig.

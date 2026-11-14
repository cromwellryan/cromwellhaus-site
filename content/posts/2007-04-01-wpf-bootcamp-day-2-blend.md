---
title: "WPF Bootcamp Day 2 - Blend"
date: "2007-04-01"
slug: "wpf-bootcamp-day-2-blend"
categories: [".Net", "WPF"]
tags: [".Net", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/04/wpf-bootcamp-day-2-blend/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/04/01/wpf-bootcamp-day-2-blend.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/04/01/wpf-bootcamp-day-2-blend.aspx"]
wayback_source: "https://web.archive.org/web/20080511113411/http://cromwellhaus.com:80/blogs/ryanc/rss.aspx?Tags=WPF&AndTags=1"
excerpt_only: false
permalink: "/2007/04/wpf-bootcamp-day-2-blend/"
---

*[Update: These are being posted due to the [ftp access restrictions](/2007/03/wpf-bootcamp-day-3-ftp-problems-from-the-technology-center/ "WPF Bootcamp Day 3 - FTP Problems from the Technology Center") at the Microsoft Campus]*

Today has been pretty intense which has kept me away from blogging "live".  Today started with [Kevin Moore](http://blogs.msdn.com/okoboji/ "Kevin Moore"), Program Manager for WPF/Blend(?), and a lightning round with [Expression Blend](http://www.microsoft.com/products/expression/en/expression-blend/default.mspx "Microsoft Express Blend™").  As I mentioned [yesterday,](/2007/03/wpf-bootcamp-day-1-expression/) I'm not a designer, so Kevin had my mind spinning before breakfast had even settled.

For those dev-signers (developers who design out of necessity) Blend is initially a very overwhelming experience.  Don't expect to create the [North Face demo](http://channel9.msdn.com/Showpost.aspx?postid=116327 "North Face WPF Demo at PDC") your first time out.  That said, I was able grasp the benefit of a few concepts including [DataTemplates](http://msdn2.microsoft.com/en-us/library/ms742521.aspx) and [Styles](http://msdn2.microsoft.com/en-us/library/ms745683.aspx).  This stuff is like OO for UI.  Pretty cool.

[![](http://cromwellhaus.com/blogphotos/WPFBootcampDay2Blend_DDDB/WPFBootcampBlendButton11_thumb.png)](http://cromwellhaus.com/blogphotos/WPFBootcampDay2Blend_DDDB/WPFBootcampBlendButton113.png) As soon as Kevin had lost me (quickly), I decided to start playing with Blend Styles and Templates.  At the same time, I decided I'd design my own button.  It turns out my reasoning for wanting to do this, super-rounded ends, were already possible in the standard button, but it was a good learning experience.

**Styles**

Styles are pretty straight forward and many references to CSS have been made.  Styles seem to be a way to share design properties between elements, especially similar elements.  It seems pretty intuitive, but every time you change the visual appearance of a control, even via Visual Studio or XamlPad, you are styling your control/element.  It becomes really powerful as you share these styles across your project by including these styles in your App Resources section.  From within Blend this is pretty easy after you've gone through and stylized one of your controls by selecting that element and going to the Object -> Edit Style -> Edit Copy.

You can then Right Click your other elements, go to Edit Control Parts (Template) -> Apply Resource and Select the Style you just created.  You now have a sharable style across your WPF application.  I'm still curious about the ability of sharing these styles across multiple projects and applications if you have a suite of tools.  Are these considered Assets for [Expression Media](http://www.microsoft.com/products/expression/en/Expression-Media/default.mspx)?  That would be cool.

[![](http://cromwellhaus.com/blogphotos/WPFBootcampDay2Blend_DDDB/WPFBootcampBlendButton1CreateEmptySt1.png)](http://cromwellhaus.com/blogphotos/WPFBootcampDay2Blend_DDDB/WPFBootcampBlendButton1CreateEmptySt.png)

**Templates**

The way I feel Templating is best described in relationship to Styling is to say that Styling helps describe the visual appearance of one or more elements, while templating describes the Element tree that makes up a visual entity.  For instance, my button above used a template to combine two Ellipses and a Rectangle.  But an ellipse on each end of the Rectangle and you've got a rounded edge button.

To get started with templating, I right click on the standard button and drilled down to Edit Control Parts (Template) -> Create Empty.  If you've done cool stuff with your element already, you can Edit Copy and apply that to other elements rather than start over.  I'll go over a demo to create a pretty cool button that uses lots of composite elements to have rollover effects (glow), transition effects, etc.

 [![](http://cromwellhaus.com/blogphotos/WPFBootcampDay2Blend_DDDB/WPFBootcampBlendButton1CreateEmptyTe1.png)](http://cromwellhaus.com/blogphotos/WPFBootcampDay2Blend_DDDB/WPFBootcampBlendButton1CreateEmptyTe.png)

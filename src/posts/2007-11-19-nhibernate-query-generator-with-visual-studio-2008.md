---
title: "NHibernate Query Generator with Visual Studio 2008"
date: "2007-11-19"
slug: "nhibernate-query-generator-with-visual-studio-2008"
categories: ["NHibernate"]
tags: ["NHibernate"]
original_urls: ["http://blog.cromwellhaus.com/2007/11/nhibernate-query-generator-with-visual-studio-2008/", "http://blog.cromwellhaus.com:80/2007/11/nhibernate-query-generator-with-visual-studio-2008/", "http://blog.cromwellhaus.com:80/index.php/2007/11/nhibernate-query-generator-with-visual-studio-2008", "http://cromwellhaus.com/2007/11/nhibernate-query-generator-with-visual-studio-2008/", "http://cromwellhaus.com/blogs/387.aspx", "http://cromwellhaus.com/blogs/ryanc/archive/2007/11/19/nhibernate-query-generator-with-visual-studio-2008.aspx", "http://cromwellhaus.com:80/2007/11/nhibernate-query-generator-with-visual-studio-2008/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/11/19/nhibernate-query-generator-with-visual-studio-2008.aspx"]
wayback_source: "https://web.archive.org/web/20091220074406/http://blog.cromwellhaus.com:80/index.php/2007/11/nhibernate-query-generator-with-visual-studio-2008"
excerpt_only: false
permalink: "/2007/11/nhibernate-query-generator-with-visual-studio-2008/"
---

[![Custom Tool Configuration](http://cromwellhaus.com/blogs/ryanc/WindowsLiveWriter/NHibernateQueryGeneratorwithVisualStudio_9F3F/image_thumb_1.png)](http://cromwellhaus.com/blogs/ryanc/WindowsLiveWriter/NHibernateQueryGeneratorwithVisualStudio_9F3F/image_1.png) I’ve been using [Ayende’s](http://www.ayende.com/Blog/) [NHibernate Query Generator](http://ayende.com/projects/downloads/nhibernate-query-generator.aspx) (NHQG) to help type-ify my NHibernate repository queries.  One of the great +1’s of his tool is that you can apply it as a [Custom Tool](http://msdn.microsoft.com/msdnmag/issues/02/10/NETTopTen/#S9) for your NHibernate mapping files right within Visual Studio.

With this setup, every change to my mapping file is reflected in my typed NHibernate ICriteria instances.  For those who work directly with Hibernate Expressions, look how clean my queries are:

> ```
> // Get it using the Idpublic static MyClass GetById(long id){    return Repository.Get<MyClass>(Where.MyClass.Id == id);}
> ```
>
> ```
> // Get those updated todaypublic void Example2(){    IList<MyClass> cards = Repository.Find<MyClass>(Where.MyClass.LastUpdated >= DateTime.Today);}
> ```

That’s just awesome!

There’s a slight glitch though, his installer only registers the tool for Visual Studio 2005.  I’m sure now that 2008 is RTM (I’ve been using Beta 2) he’ll soon have a new version out, but in the mean time, you can use these two .reg files:

[NHQG C# Custom Tool Registration](http://cromwellhaus.com/files/folders/software/entry385.aspx)

[NHQG VB Custom Tool Registration](http://cromwellhaus.com/files/folders/software/entry386.aspx)

- [Previous Entry: NHibernate 1.2.0.x versus 2.0.0.x](/2007/11/nhibernate-1-2-0-x-versus-2-0-0-x/)
- [Next Entry: NHibernate Query Generator Installer for Visual Studio 2008](/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/)

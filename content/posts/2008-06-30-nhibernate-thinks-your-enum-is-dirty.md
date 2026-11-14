---
title: "NHibernate Thinks Your Enum is Dirty"
date: "2008-06-30"
slug: "nhibernate-thinks-your-enum-is-dirty"
categories: [".Net", "NHibernate"]
tags: [".Net", "NHibernate"]
original_urls: ["http://blog.cromwellhaus.com/2008/06/nhibernate-thinks-your-enum-is-dirty/", "http://cromwellhaus.com/2008/06/nhibernate-thinks-your-enum-is-dirty/", "http://cromwellhaus.com/blogs/ryanc/archive/2008/06/30/nhibernate-thinks-your-enum-is-dirty.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/06/30/nhibernate-thinks-your-enum-is-dirty.aspx"]
wayback_source: "https://web.archive.org/web/20080828040837/http://cromwellhaus.com/blogs/ryanc/default.aspx"
excerpt_only: false
permalink: "/2008/06/nhibernate-thinks-your-enum-is-dirty/"
---

Get your head out of the gutter.

It's important to look at your mapping files closely when trying to diagnose unexpected results.  One of our developers had recently added two properties to our big honkin' CustomerOrder entity.  These both happened to be enumeration values, which are represented by Int values in the database.  Of course, NHibernate mapping files (hbm's) are from the POCO perspective, which means the <property type="..." />  value should be the Enumeration's themselves.  If you use Int32, though, things will appear to work, but you're actually causing NHibernate to do an incompatible type comparison during it's "Dirty" checks.  This will cause your lazily, loaded entities to be dirty as soon as you get them.

So, be careful in reviewing your mappings, because it doesn't take much to screw up something small that has a big impact.

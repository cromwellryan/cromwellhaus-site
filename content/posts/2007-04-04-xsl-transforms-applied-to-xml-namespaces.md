---
title: "XSL Transforms applied to XML namespaces"
date: "2007-04-04"
slug: "xsl-transforms-applied-to-xml-namespaces"
categories: ["Uncategorized"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2007/04/xsl-transforms-applied-to-xml-namespaces/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/04/04/xsl-transforms-applied-to-xml-namespaces.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/04/04/xsl-transforms-applied-to-xml-namespaces.aspx", "https://cromwellhaus.com/2007/04/xsl-transforms-applied-to-xml-namespaces/"]
wayback_source: "https://web.archive.org/web/20081122034035/http://cromwellhaus.com/blogs/ryanc/archive/2007/04/04/xsl-transforms-applied-to-xml-namespaces.aspx"
excerpt_only: false
permalink: "/2007/04/xsl-transforms-applied-to-xml-namespaces/"
---

I'm pretty sure I have run across this in the past, but apparently I've avoided complex XSL transforms successfully for long enough that my mind was purged of how namespaces impact your transforms.  Today I was working on our .Net 2.0 build process and was attempting to apply a transform to the \*.xxproj file that Visual Studio generates, but I was getting anything but what I would have expected.

My goal was simply to copy everything into a new msbuild file, but swap out the &lt;ProjectReference /> elements with &lt;Reference /> elements that pointed to a static version.  Our reasoning's are a topic for another day, but suffice it to say we are control freaks and MSBuild's apparent omniscience is not something we wish to rely on.

Most people tend to avoid namespace in their custom structures, because they are time consuming to get correct and, in many cases, people don't understand XSD well enough (understandable).  We use them in many cases, but we rarely apply XSLT's to these documents so the issue doesn't commonly present itself.  Visual Studio on the other hand, does specify the MSBuild namespace declaration at the &lt;Project /> root.  This means I have to account for it in my XSLT.  Take the following snippet:

```xml
<Books xmlns="http://schemas.cromwellhaus.com/samples/books">
<Book title="Applications = Code + Markup" author="Charles Petzold" />
<Book title="SQL Server 2000 DTS" author="Mark Chaffin" />
</Books>
```

In this case, one would have to specify the &lt;Books /> default namespace in their XSLT in order to reference the elements in their transform.  The corresponding XSLT:

```xml
<xsl:stylesheet version="1.0" xmlns:xsl=http://www.w3.org/1999/XSL/Transform xmlns:bks="http://schemas.cromwellhaus.com/samples/books">
<xsl:template match="bks:Books" >
<xsl:apply-templates select="./Book" >
</xsl:template>
</xsl:stylesheet>
```

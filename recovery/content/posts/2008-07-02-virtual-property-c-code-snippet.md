---
title: "Virtual Property C# Code Snippet"
date: "2008-07-02"
slug: "virtual-property-c-code-snippet"
categories: [".Net", "Visual Studio"]
tags: [".Net", "Visual Studio"]
original_urls: ["http://blog.cromwellhaus.com/2008/07/virtual-property-c-code-snippet/", "http://blog.cromwellhaus.com:80/index.php/2008/07/virtual-property-c-code-snippet", "http://cromwellhaus.com/blogs/ryanc/archive/2008/07/02/virtual-property-c-code-snippet.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/07/02/virtual-property-c-code-snippet.aspx"]
wayback_source: "https://web.archive.org/web/20100802044836/http://blog.cromwellhaus.com:80/index.php/2008/07/virtual-property-c-code-snippet"
excerpt_only: false
permalink: "/2008/07/virtual-property-c-code-snippet/"
---

For those of you who use NHibernate you may find this convenient, if you don’t already have your own.  Below is a C# code snippet for creating a public virtual property (code and file are both there).  Just put it in your *&lt;Visual Studio 2005/2008>\\Code Snippets\\Visual C#\\My Code Snippets* folder and you’re off and running.  No restart required.

**[File](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Components.PostAttachments/00.00.00.06.84/propv.snippet)**

**Code**

```xml
<?xml version="1.0" encoding="utf-8" ?>
<CodeSnippets  xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet">
    <CodeSnippet Format="1.0.0">
        <Header>
            <Title>propv</Title>
            <Shortcut>propv</Shortcut>
            <Description>Code snippet for an automatically implemented virtual property</Description>
            <Author>Microsoft Corporation</Author>
            <SnippetTypes>
                <SnippetType>Expansion</SnippetType>
            </SnippetTypes>
        </Header>
        <Snippet>
            <Declarations>
                <Literal>
                    <ID>type</ID>
                    <ToolTip>Property type</ToolTip>
                    <Default>int</Default>
                </Literal>
                <Literal>
                    <ID>property</ID>
                    <ToolTip>Property name</ToolTip>
                    <Default>MyProperty</Default>
                </Literal>
            </Declarations>
            <Code Language="csharp"><![CDATA[public virtual $type$ $property$ { get; set; }$end$]]>
            </Code>
        </Snippet>
    </CodeSnippet>
</CodeSnippets>
```

- [Previous Entry: Backup Your Site](/2008/07/backup-your-site/)
- [Next Entry: Visitor Pattern with Anonymous Methods](/2008/07/visitor-pattern-with-anonymous-methods/)

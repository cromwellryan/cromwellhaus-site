---
title: "SQL Server 2000 vs 2005 Lazy XML Validation"
date: "2008-08-19"
slug: "sql-server-2000-vs-2005-lazy-xml-validation"
categories: ["SQL Server"]
tags: ["SQL Server"]
original_urls: ["http://blog.cromwellhaus.com/2008/08/sql-server-2000-vs-2005-lazy-xml-validation/", "http://cromwellhaus.com/blogs/ryanc/archive/2008/08/19/sql-server-2000-vs-2005-lazy-xml-validation.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/08/19/sql-server-2000-vs-2005-lazy-xml-validation.aspx"]
wayback_source: "https://web.archive.org/web/20080828040837/http://cromwellhaus.com/blogs/ryanc/default.aspx"
excerpt_only: false
permalink: "/2008/08/sql-server-2000-vs-2005-lazy-xml-validation/"
---

Someone was looking to do quick-and-dirty validation of an Xml document inside a SQL Server procedure today.  I assumed, and regretted, that he meant 2005, which would have looked like this:

> declare @xml1 xml    
> declare @xml2 xml    
> set @xml1 = '<Node1><Node2 attrib="This is it." /></Node1>'  
> set @xml2 = '<Node1><Node2 /></Node1>'  
> select Col.value('count(./@attrib)', 'int') as count  
> from @xml1.nodes('Node1/Node2') as Tbl(Col)
>
> select Col.value('count(./@attrib)', 'int') as count  
> from @xml2.nodes('Node1/Node2') as Tbl(Col)

After being told, "that blows up", I jogged the memory a bit and came up with this mess:

> /\* THE STUPID WAY \*/  
> DECLARE @hdoc int  
> DECLARE @doc1 varchar(MAX)  
> DECLARE @doc2 varchar(MAX)  
> set @doc1 = '<Node1><Node2 attrib="This is it." /></Node1>'  
> set @doc2 = '<Node1><Node2 /></Node1>'  
> /\* DOC 1 \*/  
> EXEC sp\_xml\_preparedocument @hdoc OUTPUT, @doc1
>
> IF EXISTS( SELECT    \*  
> FROM       OPENXML (@hdoc, '/Node1/Node2/@attrib',1)  
>             WITH (attrib  varchar(20)))  
> BEGIN  
> PRINT 'Dumb ass'  
> END  
> exec sp\_xml\_removedocument @hdoc
>
> /\* DOC 2 \*/  
> EXEC sp\_xml\_preparedocument @hdoc OUTPUT, @doc2
>
> IF EXISTS( SELECT    \*  
> FROM       OPENXML (@hdoc, '/Node1/Node2/@attrib',1)  
>             WITH (attrib  varchar(20)))  
> BEGIN  
> PRINT 'Dumb ass'  
> END  
> exec sp\_xml\_removedocument @hdoc

Moral of the store?  UPGRADE!

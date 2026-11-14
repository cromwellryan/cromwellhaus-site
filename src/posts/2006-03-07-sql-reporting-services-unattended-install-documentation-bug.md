---
title: "SQL Reporting Services Unattended Install Documentation Bug"
date: "2006-03-07"
slug: "sql-reporting-services-unattended-install-documentation-bug"
categories: ["Software Reviews"]
tags: ["Software Reviews"]
original_urls: ["http://blog.cromwellhaus.com/2006/03/sql-reporting-services-unattended-install-documentation-bug/", "http://cromwellhaus.com/CS/blogs/ryanc/archive/2006/03/07/54.aspx", "http://cromwellhaus.com/blogs/ryanc/archive/2006/03/07/54.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2006/03/07/54.aspx", "https://cromwellhaus.com/2006/03/sql-reporting-services-unattended-install-documentation-bug/"]
wayback_source: "https://web.archive.org/web/20060411170309/http://cromwellhaus.com:80/CS/blogs/ryanc/rss.aspx"
excerpt_only: false
permalink: "/2006/03/sql-reporting-services-unattended-install-documentation-bug/"
---

For those that are trying to package and deploy the SQL Reporting Services 2000 Designer tools, there is a little bug in the documentation. It states that in order to include the Reporting Service Books Online feature, you should use the setting RS\_BooksOnline\_ as an ADDLOCAL parameter value. In fact, the Template.ini and documentation give the example RS\_BooksOnline\_EN. BUUUUUUT, it really should read RS\_BooksOnline\_1033. Just a hint in case you run into it, 'cause you'll have to go looking through MSI logs to find it.

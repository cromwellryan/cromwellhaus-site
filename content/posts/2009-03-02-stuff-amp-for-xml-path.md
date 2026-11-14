---
title: "STUFF & FOR XML PATH"
date: "2009-03-02"
slug: "stuff-amp-for-xml-path"
categories: ["SQL Server"]
tags: ["SQL Server"]
original_urls: ["http://blog.cromwellhaus.com/2009/03/stuff-amp-for-xml-path/", "http://blog.cromwellhaus.com/index.php/2009/03/stuff-amp-for-xml-path/", "http://blog.cromwellhaus.com:80/2009/03/stuff-amp-for-xml-path/", "http://blog.cromwellhaus.com:80/index.php/2009/03/stuff-amp-for-xml-path/", "http://cromwellhaus.com/blogs/ryanc/archive/2009/03/02/stuff-amp-for-xml-path.aspx", "http://cromwellhaus.com:80/2009/03/stuff-amp-for-xml-path/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2009/03/02/stuff-amp-for-xml-path.aspx"]
wayback_source: "https://web.archive.org/web/20100223022736/http://blog.cromwellhaus.com:80/index.php/2009/03/stuff-amp-for-xml-path/"
excerpt_only: false
permalink: "/2009/03/stuff-amp-for-xml-path/"
---

On the get the job done front, my client had a question today that, while it makes me cringe a little to answer the way I did, it got him moving again.

[Thanks to [Mike Levy](http://twitter.com/malevy) for pointing me in the right direction]

My client has a small administrative utility that displays Things.  Things can be applied to 0 or more categories.  Looks kinda’ like this:

[![image](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_thumb_5F00_064B70EA.png "image")](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_201FA719.png)

He’s using a 3rd party control for the grid itself which provides really easy filtering, but it wouldn’t work with the data structures to which he had been binding.  So he wanted to know how he could return the category listing as a delimited string directly from the T-SQL.

Here’s the gist of his schema (nothing fancy):

[![Schema](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_thumb_5F00_1E02A850.png "Schema")](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_25FA4AB2.png)

How we solved it:

```sql
SELECT Id, Name, STUFF(
            (SELECT cat.Name + ‘; ‘ AS [text()]
            FROM Category AS cat
            INNER JOIN ItemCategories AS ic ON cat.Id = ic.CategoryId
            WHERE (ic.ItemId = Item.Id) FOR XML PATH(”)
            ), 1, 0, ”
              )
FROM Item
```

Obviously we would like to move the UI junk out of the DB, but he can deal with that when he understands the 3rd party control a little better.  Right now, he’s giving his customers some more features.

- [Previous Entry: The WPF Mindset](/2008/11/the-wpf-mindset/)
- [Next Entry: Scrolling Multiple Content Areas with a single ScrollBar in WPF](/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf/)

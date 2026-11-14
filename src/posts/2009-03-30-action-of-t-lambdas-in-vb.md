---
title: "Action(Of T) Lambdas in VB"
date: "2009-03-30"
slug: "action-of-t-lambdas-in-vb"
categories: ["Languages"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2009/03/action-of-t-lambdas-in-vb/", "http://blog.cromwellhaus.com/index.php/2009/03/action-of-t-lambdas-in-vb/", "http://cromwellhaus.com/blogs/ryanc/archive/2009/03/30/action-of-t-lambdas-in-vb.aspx"]
wayback_source: "https://web.archive.org/web/20090621120953/http://feeds.feedburner.com:80/RyanCromwell"
excerpt_only: false
permalink: "/2009/03/action-of-t-lambdas-in-vb/"
---

Until VB catches up with C# in the lambda support realm, here is how you can accomplish those [Moq](http://code.google.com/p/moq/) or [Rhino.Mocks](http://ayende.com/projects/rhino-mocks.aspx) style verifications in VB:

```
dim someSub as Action(Of double) = AddressOf mockObject.SomeSub
Rhino.Mocks.Expect.Call( someSub)
```

It’s very frustrating going from the full support in C# to VB, but I’m finding sufficient workaround for most items.  I shouldn’t be so hard on VB.  C# doesn’t support inline of Xml which is pretty friggin’ sweet.

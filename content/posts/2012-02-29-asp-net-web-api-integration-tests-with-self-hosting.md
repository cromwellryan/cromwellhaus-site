---
title: "ASP.Net Web Api Integration Tests With Self Hosting"
date: "2012-02-29"
slug: "asp-net-web-api-integration-tests-with-self-hosting"
categories: ["Code", "Uncategorized"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2012/02/asp-net-web-api-integration-tests-with-self-hosting/"]
wayback_source: "https://web.archive.org/web/20120714210258/http://feeds.feedburner.com/RyanCromwell"
excerpt_only: false
permalink: "/2012/02/asp-net-web-api-integration-tests-with-self-hosting/"
---

I am trying to help out a team to verify some of their stuff works with the new ASP.Net Web API 4 Beta.  While they seem to have a number of unit tests of good quality, there was a dearth of integration tests.  I set out to resolve that as simply as possible.

To clarify we are living here:

[![image](/images/wp-content/uploads/2012/02/image_thumb8.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2012/02/image8.png)

For full UI/user tests I’d deploy the whole app, but I still want my Functional Integration tests to be faster and run locally with ease if I can.  For Web API, I was hoping for self hosting.  WCF can do this, but WCF is a giant pile of mud that I’m not interested in attacking.  So I went looking for Web API Self Hosting for Dummies.  [Found it](http://nuget.org/packages/AspNetWebApi.SelfHost).

And here’s how you use it:[![image](/images/wp-content/uploads/2012/02/image_thumb9.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2012/02/image9.png)

Note: I’ve set the *folder = “”* in this sample since my ApiController is side-by-side with my test fixture.  Assuming your ApiController is in a different assembly than your tests, you can sepcify the *namespace:* parameter in the MapHttpRoute like this:

> namespaces: new[] { typeof(ThingsController).Namespace }

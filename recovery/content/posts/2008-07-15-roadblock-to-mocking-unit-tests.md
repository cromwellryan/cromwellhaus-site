---
title: "Roadblock to Mocking Unit Tests"
date: "2008-07-15"
slug: "roadblock-to-mocking-unit-tests"
categories: [".Net"]
tags: [".Net"]
original_urls: ["http://blog.cromwellhaus.com/2008/07/roadblock-to-mocking-unit-tests/", "http://cromwellhaus.com/blogs/ryanc/archive/2008/07/15/roadblock-to-mocking-unit-tests.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/07/15/roadblock-to-mocking-unit-tests.aspx"]
wayback_source: "https://web.archive.org/web/20080828040837/http://cromwellhaus.com/blogs/ryanc/default.aspx"
excerpt_only: false
permalink: "/2008/07/roadblock-to-mocking-unit-tests/"
---

I've been a faithful unit tester for a few years now.  I may not do everything by the book (I think end-to-end unit tests are helpful), but I do get good coverage most of the time.  That said, I've found myself unable to use any of the Mock frameworks out there, because I don't use your typical Dependency Injection pattern.  That is, I don't like "building up" very freaking instance with all the "Provider" or "Service" interfaces I'm might need in the possible life of a business object.  Yes, if your Customer class is only going to create or save an Order, it feels OK, but my objects are busy dude, so I'd need the longest constructor of all time.

I prefer [Dependency Resolution](http://search.live.com/results.aspx?q=dependency+resolution+mock&form=QBRE).  I don't use any fancy framework, I just use a good old, DI.Resolve&lt;IBusyBee>() and go about my business.  It works wonderfully, it's light-weight (cause I don't use configuration based DI frameworks), and it's my baby.

That said, it's also been the roadblock to my mocking foray.  That was, until I "got it" today.  Long story short, here's how I roll:

**Create a Mock DI Container...**

```csharp
Mock<IDIContainer> mockContainer = new Mock<IDIContainer>();
```

**Create the Injected Mock instances...**

Mock&lt;INotificationManager> mockNotifMgr = newMock&lt;INotificationManager>();  
Mock&lt;IRepository> mockRepository = newMock&lt;IRepository>();

**Tell the mock IDIContainer to return the mock instances when asked...**

```csharp
mockContainer.Expect(c => c.Resolve<INotificationManager>(null)).Returns(mockNotifMgr.Object);
mockContainer.Expect(c => c.Resolve<IRepository>(null)).Returns(mockRepository.Object);
```

**Mock your heart out...**

```csharp
mockNotifMgr.Expect(mgr => mgr.NotifyEmailConfirmation(It.IsAny<Member>())).AtMostOnce();
```

```
Member.Register("username", "firstname", "lastname", "ryan@myus.com");

mockContainer.VerifyAll();
mockNotifMgr.VerifyAll();
```

I'm very happy to have finally jumped on the Moq bandwagon as it will certainly make some unit tests much easier to write.  Maybe I'll even do the test first part more faithfully now.

FYI, I use my own DI framework which is just a glorified HashTable.  It works for me and it is quick.  [Moq](http://moq.googlecode.com/) has also become my Mock framework of choice for no good reason other than I downloaded it first.

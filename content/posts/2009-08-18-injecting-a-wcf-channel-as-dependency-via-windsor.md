---
title: "Injecting a WCF Channel as Dependency via Windsor"
date: "2009-08-18"
slug: "injecting-a-wcf-channel-as-dependency-via-windsor"
categories: ["WCF", "Windsor"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2009/08/injecting-a-wcf-channel-as-dependency-via-windsor/", "http://blog.cromwellhaus.com/index.php/2009/08/injecting-a-wcf-channel-as-dependency-via-windsor/", "http://blog.cromwellhaus.com:80/index.php/2009/08/injecting-a-wcf-channel-as-dependency-via-windsor", "http://blog.cromwellhaus.com:80/index.php/2009/08/injecting-a-wcf-channel-as-dependency-via-windsor/", "http://cromwellhaus.com/2009/08/injecting-a-wcf-channel-as-dependency-via-windsor/", "http://cromwellhaus.com/blogs/ryanc/archive/2009/08/18/injecting-a-wcf-channel-as-dependency-via-windsor.aspx"]
wayback_source: "https://web.archive.org/web/20100124101708/http://blog.cromwellhaus.com:80/index.php/2009/08/injecting-a-wcf-channel-as-dependency-via-windsor"
excerpt_only: false
permalink: "/2009/08/injecting-a-wcf-channel-as-dependency-via-windsor/"
---

When working within a closed system which uses WCF and an IoC container you will often find the following pattern:

[![dependency%20of-.-%3E[AppCode],%20[SomeAppService%20Impl]delegates%20to-.-%3E[WCF%20Service%20Proxy],%20[SomeAppService%20impl]is%20injected%20into-[1]](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/dependency20of.3EAppCode20SomeA.3EWCF20Service20Proxy20SomeAppService20implis20injected20into1_5F00_thumb_5F00_6A413593.png "dependency%20of-.-%3E[AppCode],%20[SomeAppService%20Impl]delegates%20to-.-%3E[WCF%20Service%20Proxy],%20[SomeAppService%20impl]is%20injected%20into-[1]")](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/dependency20of.3EAppCode20SomeAppServ.3EWCF20Service20Proxy20SomeAppService20implis20injected20into1_5F00_73E9A3C9.png)

What happens is the SomeAppService is often, but not always, a very thin wrapper over the WCF Service.  If you own both ends of this scenario its often nice to remove the WCF layer between.  Maybe you want a different deployment model in some situations such that the WCF service itself can be an in-proc reference.  Other times the front end is in a DMZ and the WCF services needs to be inside the corporate firewall.  Maybe its just easier to run on a dev machine.  Whatever the reason, you don’t always want to be tunneling through WCF.  Plus, its just cool to see it work.

To do this, you can use Windsor’s [FactorySupportFacility](http://using.castleproject.org/display/IoC/Fluent+Registration+API) to return a [ClientBase<T>.Channel](http://msdn.microsoft.com/en-us/library/aa344730.aspx) as the dependency instance.

First, you’ll need a little class to expose the ClientBase<T>.Channel since it’s protected:

```
```
public class ServiceClient<T> : ClientBase<T> where T : class
```

```
{
```

```
    public new T Channel
```

```
    {
```

```
        get { return base.Channel;}
```

```
    }
```

```
}
```
```

Second, add the FactorySupportFacility to your WindsorContainer:

```
```
container.AddFacility<FactorySupportFacility>();
```
```

Lastly, register your implementation as either the WCF channel:

```
```
container
```

```
    .Register(Component.For<ISomeAppService>()
```

```
                       .UsingFactoryMethod(() => new ServiceClient<IWCFService>().Channel))
```
```

…or the actual implementation:

```
```
container
```

```
    .Register(Component.For<ISomeAppService>()
```

```
                  .ImplementedBy<WCFServiceImpl>())
```
```

- [Previous Entry: 1 reason to stick with Windows Virtual PC](/2009/07/1-reason-to-stick-with-windows-virtual-pc/)
- [Next Entry: Wake up: Code & Coffee tomorrow morning](/2009/09/wake-up-code-amp-coffee-tomorrow-morning/)

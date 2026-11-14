---
title: "Registering WPF “Views” with Windsor Fluent API"
date: "2009-10-26"
slug: "registering-wpf-views-with-windsor-fluent-api"
categories: ["IoC", "WPF"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2009/10/registering-wpf-views-with-windsor-fluent-api/", "http://blog.cromwellhaus.com/index.php/2009/10/registering-wpf-views-with-windsor-fluent-api/", "http://blog.cromwellhaus.com:80/2009/10/registering-wpf-views-with-windsor-fluent-api/", "http://blog.cromwellhaus.com:80/index.php/2009/10/registering-wpf-views-with-windsor-fluent-api/", "http://cromwellhaus.com/2009/10/registering-wpf-views-with-windsor-fluent-api/"]
wayback_source: "https://web.archive.org/web/20100117221458/http://blog.cromwellhaus.com:80/index.php/2009/10/registering-wpf-views-with-windsor-fluent-api/"
excerpt_only: false
permalink: "/2009/10/registering-wpf-views-with-windsor-fluent-api/"
---

I’ve had this nagging issue for some time now with WPF views that are registered for an interface.  The Views themselves are WPF UserControls:

```csharp
namespace SomeApp.Views
{
    public partial class SearchView : UserControl, ISearchView
    {
        public SearchView()
        {
            InitializeComponent();
        }
        private void InitializeComponent()
        {
            throw new NotImplementedException();
        }
    }
}
```

I would love to have registered all views in one go by simply adding:

```csharp
container.Register(AllTypes
                       .FromAssembly(assembly)
                       .Where(x => x.Name.EndsWith("View"))
                       .WithService.FirstInterface());
```

Unfortunately, this registers my Views for *System.Windows.Media.Composition.DUCE+IResource* implementations which I really couldn’t care less about.  The interface I’m looking for is the “nearest” interface for lack of a better term.  Fortunately, Windsor lets us provide a delegate selector for the interface.  Here’s what I’m using now:

```csharp
container.Register(AllTypes
                       .FromAssembly(assembly)
                       .Where(x => x.Name.EndsWith(suffix))
                       .WithService.Select((t, bt) =>
                                               {
                                                   var serviceType = t
                                                       .GetInterfaces()
                                                       .Where(x => x.FullName.StartsWith("SomeApp"))
                                                       .FirstOrDefault();
                                                   if (serviceType != null)
                                                       return new[] {serviceType};
                                                   else
                                                       return new[] {t};
                                               }));
```

> Use *Select versus FirstInterface* allows us to provide back the Service type(s?) that this class is implementing.  The StartsWith is obviously fragile, but I’m green right now, so I’ll see you on the other side.

- [Previous Entry: Wake up: Code & Coffee tomorrow morning](/2009/09/wake-up-code-amp-coffee-tomorrow-morning/)
- [Next Entry: Size versus Duration](/2009/10/size-versus-duration/)

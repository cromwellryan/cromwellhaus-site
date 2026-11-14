---
title: "PerformanceHelper.cs Update: Perfmon, Console, and Debug Output options"
date: "2007-10-27"
slug: "performancehelper-cs-update-perfmon-console-and-debug-output-options"
categories: [".Net", "Performance"]
tags: [".Net", "Performance"]
original_urls: ["http://blog.cromwellhaus.com/2007/10/performancehelper-cs-update-perfmon-console-and-debug-output-options/", "http://blog.cromwellhaus.com:80/index.php/2007/10/performancehelper-cs-update-perfmon-console-and-debug-output-options/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/10/26/performancehelper-cs-update-perfmon-console-and-debug-output-options.aspx", "http://cromwellhaus.com:80/2007/10/performancehelper-cs-update-perfmon-console-and-debug-output-options/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/10/26/performancehelper-cs-update-perfmon-console-and-debug-output-options.aspx"]
wayback_source: "https://web.archive.org/web/20100213032651/http://blog.cromwellhaus.com:80/index.php/2007/10/performancehelper-cs-update-perfmon-console-and-debug-output-options/"
excerpt_only: false
permalink: "/2007/10/performancehelper-cs-update-perfmon-console-and-debug-output-options/"
---

I’ve updated my [PerformanceHelper](http://cromwellhaus.com/files/folders/netcode/entry172.aspx) class that I’ll throw around certain code blocks to help trend or monitor performance.  Before it was merely a [PerformanceCounter](http://msdn2.microsoft.com/en-us/library/system.diagnostics.performancecounter.aspx) wrapper with a few metrics, but now you can specify Console, Debug and/or Perfmon.  You do this by using an XOR ( ’|’ ) in a new Constructor.  Here’s an example which outputs to Debug.WriteLine and PerfMon:

```csharp
for (int index = 0; index < 10; index++)
{
    using (new PerformanceHelper("ConsoleSample",
        "Perfmon Sample", OutputOptions.Debug | OutputOptions.Perfmon))
    {
        Thread.Sleep(500);
    }
}
```

The method that does the Output to Console and Debug is marked as [Conditional("DEBUG")], because you really should have a better strategy for performance monitoring in production and you don’t want that hit for each block that you wrapped.

Note to Vista Developers:  You will have problems creating custom performance counters at runtime based on registry access.  To support this in a client based app, you will need to specify an application manifest and mark it with the following:

```xml
<requestedExecutionLevel  level="requireAdministrator" />
```

For more information on application manifests, [read this](http://blogs.msdn.com/knom/archive/2007/06/11/vista-user-account-control-with-net.aspx).

- [Previous Entry: WPF Controls TabIndex: Moving to the First Input Control](/2007/10/wpf-controls-tabindex-moving-to-the-first-input-control/)
- [Next Entry: Strangest Support Call… EVER](/2007/11/strangest-support-call-ever/)

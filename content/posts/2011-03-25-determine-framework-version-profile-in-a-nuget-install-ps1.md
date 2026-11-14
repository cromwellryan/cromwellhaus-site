---
title: "Determine Framework Version & Profile in a #NuGet Install.ps1"
date: "2011-03-25"
slug: "determine-framework-version-profile-in-a-nuget-install-ps1"
categories: [".Net", "Nuget", "Silverlight", "WPF"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2011/03/determine-framework-version-profile-in-a-nuget-install-ps1/", "http://cromwellhaus.com/2011/03/determine-framework-version-profile-in-a-nuget-install-ps1/", "https://cromwellhaus.com/2011/03/determine-framework-version-profile-in-a-nuget-install-ps1/"]
wayback_source: "https://web.archive.org/web/20110416094646/http://blog.cromwellhaus.com:80/feed/"
excerpt_only: false
permalink: "/2011/03/determine-framework-version-profile-in-a-nuget-install-ps1/"
---

*[Updated:* [*@davidfowl*](http://twitter.com/davidfowl) *suggested using the FrameworkName rather than parsing myself.  Thanks!]*

I’m working on the [Caliburn.Micro](http://caliburnmicro.codeplex.com/) [Nuget](http://nuget.codeplex.com/) package and one of the things that we need is to add a default Bootstrapper, ShellView, and ShellViewModel to your project.  One awesome thing Rob Eisenberg has done is provide WPF, Silverlight and WP7 versions of [Caliburn.Micro](http://caliburnmicro.codeplex.com/).  Unfortunately, the platforms are different enough that these three pieces we would like to add are different.

I say this is unfortunate only because [Nuget](http://nuget.codeplex.com/) doesn’t support framework and profile specific content through conventions.  That’s only [available for binaries](http://nuget.codeplex.com/documentation?title=Creating%20a%20Package).  It does, however, provide hooks into the install process via PowerShell.

Maybe you see where I’m headed…

The hard part for me was figuring out the framework version of the project targeted.  In the end, here’s how you can pull the TargetFrameworkMoniker in your install.ps1:

> param($rootPath, $toolsPath, $package, $project)
>
>   $moniker = $project.Properties.Item("TargetFrameworkMoniker").Value
>
>   $framework= new-object System.Runtime.Versioning.FrameworkName($moniker)
>
>   write-host "Identifier: " $framework.Identifier    
>   write-host "Version: " $framework.Version   
>   write-host "Profile: " $framework.Profile
>
> # WPF4 will be NETFramework,Version=v4.0,Profile=Client   
> # SL4 will be Silverlight,Version=v4.0   
> # WP7 will be Silverlight,Version=v4.0,Profile=WindowsPhone

Happy packaging!

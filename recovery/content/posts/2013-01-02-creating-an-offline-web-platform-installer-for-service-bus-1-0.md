---
title: "Creating an Offline Web Platform Installer for Service Bus 1.0"
date: "2013-01-02"
slug: "creating-an-offline-web-platform-installer-for-service-bus-1-0"
categories: ["Code", "Uncategorized"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2013/01/creating-an-offline-web-platform-installer-for-service-bus-1-0/", "https://cromwellhaus.com/2013/01/creating-an-offline-web-platform-installer-for-service-bus-1-0/"]
wayback_source: "https://web.archive.org/web/20130828002658/http://cromwellhaus.com/feed/"
excerpt_only: false
permalink: "/2013/01/creating-an-offline-web-platform-installer-for-service-bus-1-0/"
---

One of my clients is evaluating a number of Service Bus tools.  One of those includes the Azure Service Bus which is now available for on-premise deployment.

Service Bus 1.0 is available only through Web Platform Installer at this time and it’s not readily apparent how you might use WPI for a network isolated environment.  Hopefully this will help:

#### WebpiCmd.exe to find the Service Bus AppId

Web Platform Installer comes with a command line tool called [WebpiCmd.exe](http://www.iis.net/learn/install/web-platform-installer/web-platform-installer-v4-command-line-webpicmdexe-preview-release_1072).  With it you can list and install packages.  You can also create an offline WPI feed which is what we’ll do.

To list available products at the default Microsoft feed:

> webpicmd /List /ListOption:Available

Somewhere in that mess is Service Bus 1.0 and it’s AppId which we’ll need to create a private, offline cache of the product and it’s dependencies.  I’m using [Console2 with a PowerShell tab](http://sourceforge.net/projects/console/) so I can do this:

> webpicmd /List /ListOption:Available | ? { $\_.Contains(“Service Bus”) }

[![image](/images/wp-content/uploads/2013/01/image_thumb.png "image")](http://cromwellhaus.com/wp-content/uploads/2013/01/image.png)

Since WebpiCmd is just writing dumb lines of text, I can’t interrogate the Product attributes, so I’m using the [where-object](http://technet.microsoft.com/en-us/library/ee177028.aspx), aliased to ?, to see which line contains the string “Service Bus”.  WebPI really should be a better PS citizen.

#### Creating an Offline Feed

WPI works against feeds, so we’re going to create our own feed just for this product.  You might maintain a growing list of products in this feed, but that’s beyond this post.  To create your offline feed we’ll use the (drum roll) /Offline option:

> WebpiCmd.exe /offline /Products:ServiceBusBeta /Path:C:\\wpi-offline

NOTE: The Service Bus 1.0 entry in WPI seems like it has a problem with the App Fabric dependency.  I’m told that’s fixed now.

#### Installing from the Offline Feed

Once everything is resolved and downloaded, you can use it with WPI GUI or WebpiCmd.exe.

You can not automate-all-the-things with:

> webpicmd /install /Products:ServiceBus /xml:c:\\wpi-offline\\feeds\\latest\\webproductlist.xml

Or do the GUI thing by checking out WPI options:

[![image](/images/wp-content/uploads/2013/01/image_thumb1.png "image")](http://cromwellhaus.com/wp-content/uploads/2013/01/image1.png)

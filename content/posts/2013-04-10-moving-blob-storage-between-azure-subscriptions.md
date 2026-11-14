---
title: "Moving Blob Storage Between Azure Subscriptions"
date: "2013-04-10"
slug: "moving-blob-storage-between-azure-subscriptions"
categories: ["Uncategorized"]
tags: []
original_urls: ["http://cromwellhaus.com/2013/04/moving-blob-storage-between-azure-subscriptions/", "http://cromwellhaus.com:80/2013/04/moving-blob-storage-between-azure-subscriptions/", "https://cromwellhaus.com/2013/04/moving-blob-storage-between-azure-subscriptions/"]
wayback_source: "https://web.archive.org/web/20130828002658/http://cromwellhaus.com/feed/"
excerpt_only: false
permalink: "/2013/04/moving-blob-storage-between-azure-subscriptions/"
---

We recently had some delays getting some Azure accounts coordinated for a client and chose to use a team subscription instead.  After some work, the delays were resolved and we had the client managed subscription in place.

The work done using the team subscription included uploading many gigabytes of sysprepped Virtual Machine images that would stand as the template for scaling up a set of services.  Once the client subscription was in place, we knew we would need to move the images over.

We were a little concerned that moving between subscriptions would take a long time.  Moving between containers isn’t hard, but could you rely on the same mechanism to move between subscriptions?  Turns out the answer is yes if you make the blob or container public during the move.

After you pull in your Azure Subscription into PowerShell (we used Import-AzurePublishSettingsFile) you can do this pretty easily.

Here’s an example of the Posh to do this with a public to private blob using the Azure [PowerShell Cmdlets](https://www.windowsazure.com/en-us/downloads/?fb=en-us):

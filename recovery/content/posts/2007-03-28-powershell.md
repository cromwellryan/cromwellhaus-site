---
title: "Powershell"
date: "2007-03-28"
slug: "powershell"
categories: ["Uncategorized"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2007/03/powershell/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/03/28/powershell.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/03/28/powershell.aspx"]
wayback_source: "https://web.archive.org/web/20090105175424/http://cromwellhaus.com/blogs/ryanc/archive/2007/03/28/powershell.aspx"
excerpt_only: false
permalink: "/2007/03/powershell/"
---

Yesterday I had a had a chance to have dinner and drinks with another group here for a Technology Summit hosted by Microsoft.  They get a bunch of representatives from parallel and alternate technology groups such as PHP, Linux, Java, Python, etc together and discuss they reasons for Microsoft decisions, show off Microsoft focused options for solving problems, and just generally discuss the technology ecosystem.

One of the people I managed to talk to in depth was an integral part of the [Powershell](http://www.microsoft.com/windowsserver2003/technologies/management/powershell/default.mspx "Windows Powershell") team.  He helped write the language and has been with the team since inception.  I personally have pretty limited experience in the \*nix environment so comparing shells is difficult for me, but he helped me understand some things.  One thing he pointed to as a the cause of some angst between \*nix administrators and Windows administrators is the ease of administering a \*nix system without a full blown interactive session.  A \*nix administrator has the option to open an SSH session and has full shell access to the system.  Adding a DNS entry for instance is 3 lines of shell command rather than opening the DNS MMC console, expanding some trees, opening a dialog, clicking a few times, then actually adding the record you intended initially, then confirming it 3 times before closing the console.

Contrary to my understanding, it was an option to recreate the \*nix shells in the Windows environment.  Instead the goal was to create a platform that would enable the end-game of creating cmdlets which can/will enable administrators to administer their systems in as productive a manner as any other platform.

One of my questions to him was regarding v2 of Powershell.  He mentioned that the focus would be in 3 areas: remote connectivity (i.e. SSH), a more powerful interface to powershell (apparently there's more to moving around the powershell than arrow-keys and tabbing), and a more broad library of cmdlets.

Also announced yesterday was the [inclusion of Powershell in the upcoming Longhorn Server release](http://blogs.msdn.com/powershell/archive/2007/03/28/announced-powershell-to-ship-in-windows-server-longhorn.aspx "Powershell to be in Longhorn Server").  Very exciting.

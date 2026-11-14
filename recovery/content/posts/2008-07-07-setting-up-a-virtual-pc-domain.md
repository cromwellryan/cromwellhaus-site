---
title: "Setting up a Virtual PC Domain"
date: "2008-07-07"
slug: "setting-up-a-virtual-pc-domain"
categories: ["Networking", "Virtual PC"]
tags: ["Networking", "Virtual PC"]
original_urls: ["http://blog.cromwellhaus.com/2008/07/setting-up-a-virtual-pc-domain/", "http://blog.cromwellhaus.com:80/index.php/2008/07/setting-up-a-virtual-pc-domain", "http://blog.cromwellhaus.com:80/index.php/2008/07/setting-up-a-virtual-pc-domain/comment-page-1/", "http://cromwellhaus.com/blogs/ryanc/archive/2008/07/07/setting-up-a-virtual-pc-domain.aspx", "http://cromwellhaus.com:80/2008/07/setting-up-a-virtual-pc-domain/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/07/07/setting-up-a-virtual-pc-domain.aspx"]
wayback_source: "https://web.archive.org/web/20100227095131/http://blog.cromwellhaus.com:80/index.php/2008/07/setting-up-a-virtual-pc-domain"
excerpt_only: false
permalink: "/2008/07/setting-up-a-virtual-pc-domain/"
---

I do a lot of demos and Virtual PC 2007 is a mainstay in my arsenal for those demos.  I’ve used VMWare Server (the free one) and it is very nice, but I run an x64 OS and VMWare had neglected to sign certain emulation drives which caused me enough headache that I ditched it for the easy of VPC.

I mentioned using [Syspreping](/2008/06/sysprep-your-virtual-pc-images/) for my VPC library prior which saves me a ton of time, but one of the things I’ve always started but never finished was setting up a Virtual Domain.  Well this weekend, I finished things up and I’m happy to say, it wasn’t that bad.

Here’s what I did:

**Create My Domain Controller Machine** by copying a Syspreped Window 2008 Server harddrive image and creating a new Virtual PC using an existing hard drive.  About 120 seconds later I have a free standing vanilla server ready to roll.

**[![image](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_thumb_5F00_3.png)](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_8.png)Configure Network Adapter(s)** by specifying *Local Only* in the VPC’s Network Settings.

At this point you’ll want to log into VPC if you haven’t already.  We’ll want to isolate our domain and let each of the workstation VPC’s communicate with the domain controller by going into the Network Adapter’s properties.  Our little domain network is going to be rather isolated.  To accomplish this, we will specify a specific Subnet and IP address range.  Here is what I’ve used for mine:

> IP Range: 192.168.8.1 – 254 (where 192.168.8.1 is my domain controller IP)  
> Subnet Mask: 255.255.248.0  
> Gateway: 192.168.8.1 (DC/DNS server)  
> Primary DNS: 192.168.8.1 (DC/DNS server)

[**![image](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_thumb_5F00_1.png)**](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_4.png) **Setting up Active Directory** is a breeze if you do it the easy way.  Of course, I did it the easy way the last time.  (Note to self: when just learning, take the defaults).  Windows Server 2003 and 2008 have this concept of Roles.  A server can fill one or more roles which are the conglomeration of settings, services, etc to do something more abstract… like be a DC.  We are going to add the role *Active Directory Domain Services*.

After the Add Role wizard does it’s thing, you actually “promote” the machine to a DC by running dcpromo.exe (Start, dcpromo, Enter).  This is where you make your selections, which in this case, I’ve chosen:

> Create a new domain in a new forest  
> FQDN: vpc.com

You’ll want to let the machine also be a DNS server.  This is where I screwed up the first time.  Don’t get scared here, with our networking settings this domain we’re setting up won’t touch your corporate domain or anything crazy like that.

Let the Wizard do it’s thing and reboot when it is complete.

Your Active Directory Domain Controller is ready to roll.  Great job.

**Adding Workstations** is a matter of adding a Computer entry into the *Active Directory Users and Computers* console and then actually adding the computer to the domain.  You’ll find the AD Users and Computers MMC console in Administrative Tools.  Once you’ve added a computer entry, log into another VPC instance which has the same Network Adapter settings as above (different IP of course .2, .3, etc) and add the machine to the domain (vpc.com) in my case.

[![image](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_thumb_5F00_4.png)](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_10.png)Here’s a quick screen capture of my Network Adapter on the Workstation I added to the domain.

It’s great being able to demo Enterprise software this way or test things like integrated authentication for intranet applications.

- [Previous Entry: Did you know? Screenshots of Virtual PC Instances](/2008/07/did-you-know-screenshots-of-virtual-pc-instances/)
- [Next Entry: Video Conferencing Code of Conduct](/2008/07/video-conferencing-code-of-conduct/)

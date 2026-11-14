---
title: "Bringing down an Oracle 9i on Windows instance"
date: "2007-03-27"
slug: "bringing-down-an-oracle-9i-on-windows-instance"
categories: ["Oracle"]
tags: ["Oracle"]
original_urls: ["http://blog.cromwellhaus.com/2007/03/bringing-down-an-oracle-9i-on-windows-instance/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/03/27/bringing-down-an-oracle-9i-on-windows-instance.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/03/27/bringing-down-an-oracle-9i-on-windows-instance.aspx"]
wayback_source: "https://web.archive.org/web/20080311181323/http://cromwellhaus.com:80/blogs/ryanc/archive/2007/03/27/bringing-down-an-oracle-9i-on-windows-instance.aspx"
excerpt_only: false
permalink: "/2007/03/bringing-down-an-oracle-9i-on-windows-instance/"
---

The [Speedy Rewards](http://www.speedyrewards.com) program is backed by two pretty hefty [Oracle 9i RAC](http://www.oracle.com/technology/products/oracle9i/datasheets/rac/rac_rel2_ds.html) instances.  One is for the OLTP and the other for data-warehousing analytics.  Since it's inception we've pretty impressive success with the uptime and performance, though one glaring problem has plagued us now for going on 4 years.  Every 3 days, whoever is on call is required to reboot EACH instance of the cluster to avoid a "[Split Brain](http://docs.huihoo.com/oracle/docs/B19306_01/rac.102/b14197/rac_glossary.htm#CHDBEGFH)".  This is compounded by the fact that the third-party software that we have purchased to manage high-performance points, offers, awards, etc. presentation to our members maintains open connections as long as the application server is running, never closing them or validating themselves.  So basically, this third-party software has negated most of the benefit of a RAC cluster in that there is no load balancing (RAC redirects on the initial connection.Open, not between command executions - sticky connections) and there is no failover during our 3 day reboots.  We must effectively go offline every three days for about 10 minutes.  Not good for a &lt;1% SLA on greater than "a lot" (that's lawyer speak) per day.

I could spend all day trying to reiterate their reasoning for maintaining open connections forever, not re-connecting them, or even their decision to take down their entire application server (not physical server but the windows services that encompass their application) when connections begin to fail.  I'll allow you all to come to your own conclusions as to the competence of this company that shall remain nameless.

After 4 years of open "TAR's" with Oracle, numerous consultants, configuration changes, and eventually a plan to migrate these instances to 10g on Linux we believe we stumbled upon the root cause.  We are all aware, I hope, of Windows Perfmon/Performance Counters and how very helpful they can be in giving insight into your running applications.  Well it turns out that Oracle exposes performance counters, but the underlying implementation of these counters login and extract the counter data directly from the target instances.  In order for Oracle to do this it provides a set of configurations for specifying the login, instance information, etc for the counters to use.  Here comes the kicker - that login must be VALID.  Yes, if it's not valid and you have a tool which try to open these performance counters pretty often like [MOM](http://g.msn.com/9SE/1?http://www.microsoft.com/mom/&&DI=6244&IG=c74083987ee44fa690049d6c513c311b&POS=1&CM=DEF&CE=1&CS=AWP&SR=1 "Microsoft Operations Manager") your Oracle process will, over time, leak Virtual Bytes and the Oracle Process will crash, causing a Split Brain.

Long story short, if you're interested in crashing an Oracle 9i instance, try to login over and over with an invalid login.  Now would you call that a bug?  A pretty glaring one if you ask me.

Here is a [link](http://download-east.oracle.com/docs/cd/B10501_01/win.920/a95490/registry.htm#1005939 "Parameters for Oracle Performance Monitor for Windows NT") to the configuration settings article which details what we had to do to resolve this issue.

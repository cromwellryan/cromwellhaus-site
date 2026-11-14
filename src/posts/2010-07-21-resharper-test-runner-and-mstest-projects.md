---
title: "ReSharper Test Runner and MSTest Projects"
date: "2010-07-21"
slug: "resharper-test-runner-and-mstest-projects"
categories: [".Net", "Testing", "Visual Studio"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2010/07/resharper-test-runner-and-mstest-projects/", "http://blog.cromwellhaus.com/index.php/2010/07/resharper-test-runner-and-mstest-projects/"]
wayback_source: "https://web.archive.org/web/20100815225045/http://blog.cromwellhaus.com:80/"
excerpt_only: false
permalink: "/2010/07/resharper-test-runner-and-mstest-projects/"
---

One of my biggest irritants with the Unit Testing ecosystem is that each runner does things a little different. [Gallio](http://gallio.org/) has helped solve this to some extent, but even that hasn’t solved all the problems that come with content or resource file deployments, coverage settings, etc.  Gallio’s goal is noble if not arrogant, become the *Runner to Rule Them All.*

Unlikely.

[ReSharper](http://www.jetbrains.com/resharper/index.html), on the other hand, has taken the Switzerland approach and tries to be true to each testing frameworks settings and run modes.  It has a gap in regards to MSTest at this point, though.  (Who uses MSTest you say?  Lots of people.  You wanted unit testing to become common place, remember?  Stop complaining.)  ReSharper gives you this nasty warning when running your MSTests with Code Coverage enabled.

[![image](http://blog.cromwellhaus.com/wp-content/uploads/2010/07/image_thumb.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2010/07/image.png)

See MSTest is actually pretty sweet when it comes to data capture.  It might not be blazing fast, but it lets you capture an awful lot of information in different situations.  In order to support those different situations nicely there is this file type called Test Settings (\*.testsettings).  [![image](http://blog.cromwellhaus.com/wp-content/uploads/2010/07/image_thumb1.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2010/07/image1.png)Test Settings files live in your solution folder and you can have a bunch of them.  In fact, Visual Studio 2010 gives you two by default: Local.testsettings and TraceAndTestImpact.testsettings.

Local.testsettings doesn’t capture anything by default, but one of the first thing everyone tends to look for when running tests is [code coverage](http://en.wikipedia.org/wiki/Code_coverage).  Since Local.testsettings are their default and people don’t realize you can change your active test settings they open Local.testsettings, choose Data and Diagnostics and check Code Coverage (and probably other things that sound interesting).

[![Enable Code Coverage in Data and Diagnostics of Local.testsettings](http://blog.cromwellhaus.com/wp-content/uploads/2010/07/image_thumb2.png "Enabling Code Coverage in Data and Diagnostics of Local.testsettings")](http://blog.cromwellhaus.com/wp-content/uploads/2010/07/image2.png)

Now you’ve eliminated Resharper as a Test Runner.  But you don’t have too!  Remember how I said you can have a bunch of those .testsettings files and eluded to the fact that one can be made *Active.*  Here’s what you’re going to do:

1. Right click the Solution Items folder (don’t put them in a different solution folder, VS doesn’t like that, sorry).
2. Click Add –> New Item
3. Under Installed Templates (VS 2010) select Test Settings.
4. Name the new file ReSharper.testsettings (or whatever makes you happy really) and click ok.

The Test Settings editor dialog will come up, but you don’t need to change a thing if you don’t want or need.  Data and Diagnostics will be empty which is good for ReSharper.  At this point, you can go to the Test menu option, open Select Active Test Settings and choose your new settings (ReSharper.testsettings in our example).

That’s it, use ReSharper all you like.  There are some other nice things that ReSharper will do for you in regards to abiding by deployment options for content files and things like that, but we’ll save that for a different day.  [Here’s a quick video](http://screencast.com/t/NWQwYWVj) that highlights everything I’ve outlined here.

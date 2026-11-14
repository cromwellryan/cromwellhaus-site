---
title: "Headless Javascript Testing with Visual Studio 2012 & Chutzpah Test Adapter"
date: "2012-07-31"
slug: "headless-javascript-testing-with-visual-studio-2012-chutzpah-test-adapter"
categories: ["Uncategorized"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2012/07/headless-javascript-testing-with-visual-studio-2012-chutzpah-test-adapter/", "http://cromwellhaus.com:80/2012/07/headless-javascript-testing-with-visual-studio-2012-chutzpah-test-adapter/"]
wayback_source: "https://web.archive.org/web/20150506185726/http://cromwellhaus.com:80/2012/07/headless-javascript-testing-with-visual-studio-2012-chutzpah-test-adapter/"
excerpt_only: false
permalink: "/2012/07/headless-javascript-testing-with-visual-studio-2012-chutzpah-test-adapter/"
---

[Update: The amazing [@mmanela](http://www.twitter.com/mmanela) has fixed the bug in my original video.  Get the latest Chutzpah from VS Extensions.  I’ve re-recorded the video also.]

More often than not, I’ll use the [jasmine-node](https://github.com/mhevery/jasmine-node) [nodejs](http://nodejs.org) module for javascript testing.  It provides continuous testing/auto testing and it’s really fast.  To date, there really hasn’t been a good, if any, testing experience for javascript inside-the-box for Visual Studio.

In VS 2010, the [Chutzpah](http://chutzpah.codeplex.com/) extension tacked on jasmine and qunit support by running javascript tests outside of Visual Studio and pushing the results to the output window.  This was a big step forward.

In VS 2012, there is an open model for discovering and executing tests that Chutzpah and others have provided implementations for.  Now you can run [NUnit](http://visualstudiogallery.msdn.microsoft.com/6ab922d0-21c0-4f06-ab5f-4ecd1fe7175d), [xUnit](http://visualstudiogallery.msdn.microsoft.com/463c5987-f82b-46c8-a97e-b1cde42b9099), Jasmine, and QUnit tests without 4 different runners.  Much nicer.  It even supports auto/continuous testing, though with an admittedly naive priority scheme compared to [NCrunch](http://www.ncrunch.net/) or [Mighty Moose](http://continuoustests.com/).

**Video: Jasmine Tests with Chutzpah in VS 2012**

In this video, I’ve walked through a very simple setup using Chutzpah to run Jasmine tests inside [Visual Studio 2012 RC](http://www.microsoft.com/visualstudio/11/en-us).

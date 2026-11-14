---
title: "Your Test Suite Sucks… do it again"
date: "2012-01-04"
slug: "your-test-suite-sucks-do-it-again"
categories: [".Net", "Agile", "TDD", "Testing"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2012/01/your-test-suite-sucks-do-it-again/", "http://blog.cromwellhaus.com:80/2012/01/your-test-suite-sucks-do-it-again/", "http://cromwellhaus.com/2012/01/your-test-suite-sucks-do-it-again/"]
wayback_source: "https://web.archive.org/web/20120117212040/http://feeds.feedburner.com:80/RyanCromwell"
excerpt_only: false
permalink: "/2012/01/your-test-suite-sucks-do-it-again/"
---

A [pretty smart dude](https://twitter.com/#!/RbKeefer) I worked with once told this story of a team he was on.  They spent a few days, maybe even a week, deploying their app.  It was painful, obviously.  They’re response: “That sucked.  Let’s do it again tomorrow.”

Most people try to avoid hard things or at least delay them until they have a good reason, but some things, important things… we should do those more often.  We need to practice the hard things.  They in turn become less risky and less scary bookends to our prideful efforts.

Testing is one of those things.

A few months back there was a thread going on the [Scrum.org](http://scrum.org/) [Professional Scrum Developer](http://www.scrum.org/professionalscrumdeveloper/) Trainers list about topics to include in the future.  Specifically this was in regards to [the .Net flavor](http://www.scrum.org/professionalscrumdeveloper/) of the course, because we were getting updates about what was coming down the pipe in the tooling.  My excitement in that course has always focused on testing and with Jason Zander announcing [continuous testing](http://blogs.msdn.com/b/jasonz/archive/2011/05/16/announcing-alm-roadmap-in-visual-studio-vnext-at-teched.aspx) for all the major test runners in Visual Studio vNext that was my suggestion.

[Adam Cogan](https://twitter.com/#!/adamcogan), a smart dude in his own right, followed up asking me to describe why I thought that was such a big deal.  I sent a rather long reply that I found useful today while describing the [testing pyramid](http://blog.mountaingoatsoftware.com/the-forgotten-layer-of-the-test-automation-pyramid) to coworker [Steve Gentile](http://twitter.com/stevemgentile).  I thought I’d provide that reply here and get everyone’s thoughts:

> We give [passing](http://patrickwilsonwelsh.com/?p=32) [credence](http://jonkruger.com/blog/2010/02/08/the-automated-testing-triangle/) to the idea of fast tests that run often versus slow tests that we expand to include before checkin/commit or during automated build (gated).  Unfortunately, the later becomes a catch all for the oops, just got lazy scenario.
>
> I remember when I first got the automated testing bug.  I wrote some tests (calling them unit tests) that integrated with a 3rd party tool, gave great coverage and awesome feedback.  We knew within 5-10 minutes if a new 3rd party version could be released.  Giant leap.  The next step, though, was hidden.  I would code for 20, 30, 90 minutes or more and then run my tests while I grabbed a [cappuccino](http://www.speedway.com/FoodAndDrink/GourmetRecipes.aspx).
>
> My current passer-by, rock your world tip/tool is [NCrunch](ncrunch.net) for .Net or [Guard](https://github.com/guard/guard) for everyone else (we need this).  Autotest.Net was the first try from James Avery, but it didn’t have any traction and was unstable at best.  Most teams have tests, but they aren’t using them effectively.   (Ok, [Nuget](http://nuget.org/) and the [no-commit pattern](http://docs.nuget.org/docs/workflows/using-nuget-without-committing-packages) is a [very close second](http://twitter.com/#!/cromwellryan/status/99302447855566848)!)
>
> I run a group call [Cincy Clean Coders](http://cincycleancoders.com/).  We do katas, often as a whole group.  The first [Randori](http://codingdojo.org/cgi-bin/wiki.pl?RandoriKata) kata we did was eye opening for the audience.  Someone started refactoring to solve a red test and another person threw a fit.  “What are you doing?!  You’re red!  You can’t refactor when your red.”  The driver didn’t intend to be refactoring, they were just solving the current red test in their mind.  They didn’t realize they were mixing many steps into one.  There is a mental burden to doing the simplest thing, running the tests, and only then refactoring.
>
> Teams make a great jump when they automate their important tests.  Nightly feedback from QTP, Test Pro, or Coded UI is a big step.  Consciously mixing unit, integration and acceptance tests is amazing.  Our current tools mandate the start of the feedback loop be a conscious decision.  “So all those changes, wonder if things are still working?  Let’s find out.”  We don’t say it, but that’s how we act.
>
> When your tests run every time you pause (NCrunch) or save a file (Guard) you come to expect feedback NOW.  You skip even CTRL+R,Y until your “finished”, only to find you just did 3,5, 10 refactorings.  Which one caused the problem?  Or you write a test that calls a web service, taking .65 seconds.  Pretty soon “fast” tests take 30-60 seconds (or more!) and your CI build takes 20 minutes.
>
> Continuous testing is (IMO) the next step in shortening the feedback loop.  You start organizing your tests more effectively (or at all).  In good environments, I even use this as a chance to commit.  I now have the luxury of completely ignoring the path I took to my current source situation.  Get into a tizzy, reset/undo checkout.  Committing 10-20 times in an hour isn’t uncommon here.  Neither is branching half a dozen times.
>
> In the PSD I can demo and talk to the importance of running tests often and having confidence, but a blaring red failure on the screen for that last edit really hits home.

I want your test suite to be an invaluable tool.  Continuous testing is one of those pit of success kind of things.  We need more of those.  But [when signals pop up](https://twitter.com/#!/hotgazpacho/status/154385763306438657) solve the [real problem](https://twitter.com/#!/hotgazpacho/status/154386804085227520).  Don’t delay the pain.

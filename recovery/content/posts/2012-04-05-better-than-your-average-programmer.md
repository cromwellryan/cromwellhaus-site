---
title: "Better than your average programmer…"
date: "2012-04-05"
slug: "better-than-your-average-programmer"
categories: ["Code", "Uncategorized"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2012/04/better-than-your-average-programmer/", "http://cromwellhaus.com:80/2012/04/better-than-your-average-programmer/"]
wayback_source: "https://web.archive.org/web/20120714210258/http://feeds.feedburner.com/RyanCromwell"
excerpt_only: false
permalink: "/2012/04/better-than-your-average-programmer/"
---

There was a minor discussion about enums, constants and branching on a project discussion forum recently.  Alternative options suggested included polymorphism, delegate hashes and factories.  One of the responses suggested these were beyond “the average programmer”.

> *That’s crazy talk that leads straight to the ivory-tower.*

We just need to expose people to the alternatives as often as we can.  [Expand their normal](/2012/01/expand-your-normal/ "Expand Your Normal").

So here I want talk about evolving towards a more change friend solution using the scenario of calculating bonuses that is similar to what was being discussed in the forum.

*Warning: the code below was not run.  While it’s meant to be javascript, it’s not meant for copy, paste, execute.*

**The YAGNI Solution**

This is certainly readable and understandable.  It’s also crazy simple and likely to get more complicated.  When that happens, how do we transform the problem?  How do we use the alternatives so that when one part of the problem changes, the entire solution does not in churn?

**The Less Cohesive Solution**

We’ve moved the calculation into it’s own area.  That’s pretty nice.  But it seems likely that when criteria change, so will the calculations.  When one thing churns so will all others.  We’ve spread around what it means to get a “Great” review.

**A More Balanced Solution**

What would be nice is if adding, changing or removing any single bonus category was self contained.

At this point, what we find as the point of churn (each business decision) is now isolated.  The contract between the entry point of calculating the bonus and the actual calculators is in the registerCalculator implementation.  We’re assuming that won’t change much.

**More Code != Better**

This is not a hammer for all of your business decision nails.  It is certainly more complex.  But we must balance complexity, cohesiveness, and correctness with all the other things we value.

The first solution is not “bad”.  I would ship that first solution.  I’d adjust my system over time so that change was enabled in my architecture.

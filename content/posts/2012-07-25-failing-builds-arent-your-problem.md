---
title: "Failing Builds Aren’t Your Problem"
date: "2012-07-25"
slug: "failing-builds-arent-your-problem"
categories: ["Uncategorized"]
tags: ["code; agile"]
original_urls: ["http://cromwellhaus.com/2012/07/failing-builds-arent-your-problem/", "http://cromwellhaus.com/2012/07/failing-builds-arent-your-problem/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+RyanCromwell+%28Ryan+Cromwell%29", "http://cromwellhaus.com:80/2012/07/failing-builds-arent-your-problem/"]
wayback_source: "https://web.archive.org/web/20150307053001/http://cromwellhaus.com:80/2012/07/failing-builds-arent-your-problem/"
excerpt_only: false
permalink: "/2012/07/failing-builds-arent-your-problem/"
---

> Lets just say, as a group, we don’t have a lot of urgency to fix the builds
>
> ~ Concerned Team Member at Big Company

**It’s a Signal, Not a Problem**

I remember building my first significant build system based on CruiseControl.net, nunit, Wix, and a LOT of pixie dust.  Every failed build resulted in a friendly reminder that the team should “probably fix that.”  I’d give them some time of course, but I was always the build jerk.

It took quite a while before I started realizing that when people don’t care about the quality practices or signals that I cared about, I needed to ask why they don’t care; not what’s wrong with them.

**Why A Failed Build Isn’t Important**

One of the reasons I see teams ignoring their builds is because their builds don’t have any meaning to them.  They don’t produce useful information they don’t already know.  The team knows the tests are crap or the product isn’t ready for prime time.  In these cases, the feedback loop provided by the build is not in sync with the feedback loop that the team finds important.

**Make The Build Important**

Telling team’s that their build is important won’t work.  The build *actually needs to be important*.

How do you do this?

One way is to **ship something!**  If your not lucky enough to have leadership that supports incremental deliver, try making your Daily [Scrum](http://scrum.org) more productive/valuable.  The three questions and your Daily Scrum are not useful if your build isn’t also useful.  I can almost guarantee that.  So here’s how I’d suggest your *team*, not each individual, answer the 3 questions:

- *What new features did your builds include yesterday?*
- *What stopped you from adding a feature you planned on yesterday?*
- *What new features do you plan to add to the build today?*

Now instead of giving some punk your status update… your making a plan to attack the day and measuring your progress in the Sprint using features running off the build.

---
title: "Passive Aggressive Commit Messages"
date: "2012-09-27"
slug: "passive-aggressive-commit-messages"
categories: ["Uncategorized"]
tags: ["Agile"]
original_urls: ["http://cromwellhaus.com/2012/08/passive-aggressive-commit-messages/"]
wayback_source: "https://web.archive.org/web/20190718034729/http://cromwellhaus.com/tag/agile/"
excerpt_only: false
permalink: "/2012/08/passive-aggressive-commit-messages/"
---

If anyone tries to tell you Twitter is a waste of time, they have the wrong circle of followers.  Today I posted [this gist](https://gist.github.com/3426969) somewhat facetiously asking if the following was an acceptable commit message.

> Refactoring done earlier didn’t execute acceptance tests. This makes me wonder why we even have acceptance tests. The acceptance tests (and the bug they surfaced) are fixed. Ugh. Professionalism people. Please.

[![image](http://cromwellhaus.com/wp-content/uploads/2012/08/image_thumb.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/08/image.png)I say *somewhat facetiously*, because I actually copied it out of my almost submitted commit command. I was really close to sending it and that would have probably been the end of it.  It’s unlikely anyone would have noticed it, especially the person I was directing this passive aggressive comment towards.

###### Follow My Own Advice

I’ve blogged recently about recognizing signals ([here](/2012/07/failing-builds-arent-your-problem/) and [here](/2012/08/crickets-messages-are-only-useful-if-received/)).  Obviously, I’m not following my own advice.  I need to go and find out why this person doesn’t care about the acceptance tests and either convince them they are important or find a better way.

###### 

###### Uncomfortable Part

Rather than be passive aggressive in silence, I need to have the discussion.  It’s not going to be comfortable, but I have something we can both agree on: we both want this to be successful.  If we can keep the conversation focused on the success of this project, we can find an understanding.  If I use the same tone in our conversation that I’m using in this commit message, well, it’s not going to go well.

Fortunately, I wear big boy pants (when I go to the office) and I’m willing to get over a little uneasiness for the sake of my creation.  Do it a few times and it gets much easier.

###### Simple Solution

It turns out this was able to exist in our codebase for a few days, because we aren’t running our acceptance tests as part of the build. I plan to remedy that tomorrow.

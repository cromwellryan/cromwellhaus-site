---
title: "Feature Focused Javascript Apps"
date: "2012-07-13"
slug: "feature-focused-javascript-apps"
categories: ["Code", "Uncategorized"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2012/07/feature-focused-javascript-apps/", "http://cromwellhaus.com/2012/07/feature-focused-javascript-apps/?b.selected=a.defaultSelected:c==="]
wayback_source: "https://web.archive.org/web/20120714210258/http://feeds.feedburner.com/RyanCromwell"
excerpt_only: false
permalink: "/2012/07/feature-focused-javascript-apps/"
---

**Common Closure, Not RSI! **Common Closure, Not RSI!****

Some time last year I started getting really annoyed.  Every time I picked up a new app, I had to open at least three rather busy folders to grok what was going on.  Maybe you’ve heard of them:

Models, Views and Controllers

Yeah, I get it, it’s the de-facto layout for most apps.  I’m all for consistency for the sake of simplicity.  It’s a grand plan.

But my eyes and keyboard are tired of jumping around to find out what the Home page is up to.  Last time I checked, those things that change together, stay together[1](http://www.objectmentor.com/resources/articles/granularity.pdf) [2](http://www.objectmentor.com/resources/articles/granularity.pdf).  I don’t recall the “Those things that look like controllers stay together” principle.  Not even a smidge of alliteration.

I’m glad to see I’m not alone.  Feature frameworks are slowly popping up for Rails mostly, but I suspect ASP.Net won’t be too far behind.  Uncle Bob also seems to have a rant going on the topic as well. You can watch one of his talks on the topic [here](http://confreaks.com/videos/759-rubymidwest2011-keynote-architecture-the-lost-years). Good stuff all around.

**My Change to get Feature Focused**

In December of 2011, when I picked up a new project I decided to try something new.  Features that made the app useful were going to highlight the app structure.  Instead of folders called Models, Views and Controllers, the first thing you’d see is Chat, Tasking, and Notifications.  Want to add some information to the Chat notifications… guess where you go?  Yup… Chat.

Now most js frameworks don’t subscribe to the Model, View, Controller discovery convention like server frameworks.  Instead, they’re mounds of scripts crumpled into some scripts directory.  Not the framework’s fault, but again, not exactly organized with discipline.

**Focusing on Features in Javascript**

Here are the weapons I chose to go into battle:

*[requirejs](http://requirejs.org/)*

Provides dependency definition and resolution. Not crucial for the code, but it made optimizing a loosely coupled JS app into Sweet Apple Pie™.

*[backbone.routing](http://documentcloud.github.com/backbone/)*

‘cause sammyjs had a personality disorder.

*[knockoutjs](http://knockoutjs.com)*

Model Binding for realz.  Backbone.Modelbinding just wasn’t there yet.  I felt like I built a lot of Backbone by the end, but the knockoutjs’ binding is butter.

**Home**

Our app is all client side; single DOM.  Should you do your app that way… dunno.  For this one, I had index.htm and was done.

[![image](/images/wp-content/uploads/2012/07/image_thumb1.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image1.png)

The only thing of interest is that we’re sourcing require.js and we’ve specified the data-main attribute with a value of bootstrap. This refers to bootstrap.js which is going to get things rolling.

As you can see on the left, the client app is in a src directory under my app’s root of featurefocusedjsapp.

> Dilemma: I really want to experiment with hosting the server components along side corresponding client components where appropriate.  If you have ideas or experiences here, share them in the comments.

**Bootstrap.js Feature Modules**

bootstrap.js uses the require.js require function to create a module.  require takes two things, [![image](/images/wp-content/uploads/2012/07/image_thumb2.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image2.png)an array of dependency module names and a function to be executed once all dependencies are available.

The purpose of bootstrap.js is to kick off the modules of our application.  In many common frameworks, you might start by declaring routes using Sammy, Ember, or Backbone.  We might need that, but I really want to start features.  And that’s where modules come in.

**Credits Module**

Since our app is so awesome, people will want to know a little about the creators.  Let’s give them some credit.  We’ll start by creating a CreditsModule.js in the Credits feature directory.  Bootstrap will simply call start on our module.

[![SNAGHTML33857991](/images/wp-content/uploads/2012/07/SNAGHTML33857991_thumb.png "SNAGHTML33857991")](http://cromwellhaus.com/wp-content/uploads/2012/07/SNAGHTML33857991.png)

We’re using the Reveal Module pattern to expose a start function.  Credits module is going to display some information, so we’ll need a view.  One thing I dislike about many js heavy apps I’ve seen built is the unending list of script templates embedded in one page or another.  The javascript is in one place, but the view is totally disconnected.  If you’re composing this in an optimization/minification step, great.  But those I’ve seen are actually coded in this way.  Churn on those files is very high and I don’t like high churn.

**Collocating Views**

Instead, I want the creditsview.htm to sit alongside the rest of the credits module.  We want to show this in the main content region of the app, but I don’t want my module coupled to some css selector or jQuery.  So let’s see how we can put this all together:

[![SNAGHTML339fdbec](/images/wp-content/uploads/2012/07/SNAGHTML339fdbec_thumb.png "SNAGHTML339fdbec")](http://cromwellhaus.com/wp-content/uploads/2012/07/SNAGHTML339fdbec.png)

Here we use the [text.js](http://requirejs.org/docs/download.html#text) plugin for requirejs.  This sources the creditsview.htm content, sending the raw string as a parameter to the callback.  We use this view content as a closure in the start function which is, again, exposed as a module using the reveal module pattern.

Check out our awesomeness

[![image](/images/wp-content/uploads/2012/07/image_thumb3.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image3.png)

I’m running this using python –m http.server from the src directory.  This is so convenient I created a serverpy function in my [Powershell profile](https://github.com/cromwellryan/ps-config/blob/master/Microsoft.PowerShell_profile.ps1).

**Perf Sucks!**

As you might imagine, this isn’t doing great things for our site resource performance.  Lots of little files are bad for a browser.  Our crazy simple site is bad.

[![image](/images/wp-content/uploads/2012/07/image_thumb4.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image4.png)

Remember how I said requirejs wasn’t crucial.  Everything we’ve done so far could pretty easily have been done by hand.  Here is were requirejs begins to pull it’s weight.

**r.js to the rescue**

[r.js](https://github.com/jrburke/r.js) also by James Burke is here to slim things down with it’s optimizer option.  This is going to take our collection of scripts and templates and turn it into a single script resource.

> node r.js –o build.js

Running that command in the root of the repo will show us this:

[![image](http://cromwellhaus.com/wp-content/uploads/2012/07/image_thumb5.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image5.png)

r.js has just walked the dependency tree of bootstrap.js and consolidated it into a directory called build in the repo root.

At first glance this seems wholly unimpressive

[![image](/images/wp-content/uploads/2012/07/image_thumb6.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image6.png) until you open bootstrap.js…

[![image](/images/wp-content/uploads/2012/07/image_thumb7.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image7.png)

Sold.

Delete all that working garbage and serve up the build directory.

[![image](/images/wp-content/uploads/2012/07/image_thumb8.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image8.png)

What do our downloads look like now?

**BEFORE**

[![image](/images/wp-content/uploads/2012/07/image_thumb9.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image9.png)

**AFTER**

[![image](/images/wp-content/uploads/2012/07/image_thumb10.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/07/image10.png)

You can find the code to this point at <https://github.com/cromwellryan/featurefocusedjs>

Next time I’ll talk about features talking to one another.  Then we’ll talk testing pieces of this thing.

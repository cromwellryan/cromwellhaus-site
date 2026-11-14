---
title: "libnotify support for expresso"
date: "2011-09-17"
slug: "libnotify-support-for-expresso"
categories: ["git", "node"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2011/09/libnotify-support-for-expresso/"]
wayback_source: "https://web.archive.org/web/20120117212040/http://feeds.feedburner.com:80/RyanCromwell"
excerpt_only: false
permalink: "/2011/09/libnotify-support-for-expresso/"
---

*Warning: Linux, Terminal, vim and Continuous Testing ahead.  Not a fan?  Did you know [Continuous testing is coming to Visual Studio vNext](http://blogs.msdn.com/b/jasonz/archive/2011/05/16/announcing-alm-roadmap-in-visual-studio-vnext-at-teched.aspx)?  Yeah – it’s that good an idea!  Go get [NCrunch](http://ncrunch.net) for VS 2010 or the preview of [VS 2011](http://blogs.msdn.com/b/jasonz/archive/2011/09/14/announcing-visual-studio-11-developer-preview.aspx).*

I recently switched from [vows](http://vowsjs.org/) to [expresso](https://github.com/visionmedia/expresso) for my [nodejs](http://nodejs.org/) unit testing.  I prefer the BDD format of vows, but I was having trouble getting them to work nicely with [soda](http://sodajs.com/) and [selenium](http://seleniumhq.org).  Vows has [watch support](http://vowsjs.org/#reference) for continuous testing which I love, but it didn’t have libnotify support.  I need this, because I run my watchers like [Guard](https://github.com/guard/guard#readme), [node-dev](http://fgnass.posterous.com/nodejs-supervisor), and such on another workspace.

[![image](http://blog.cromwellhaus.com/wp-content/uploads/2011/09/image_thumb.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2011/09/image.png)

Without the notifications from libnotify I would have to switch back and for to see the terminal output of the watcher process.  Kills my flow.

Expresso doesn’t have watch support so I added it to my Guardfile:

[![image](http://blog.cromwellhaus.com/wp-content/uploads/2011/09/image_thumb1.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2011/09/image1.png)

That *should* run expresso for all of my fast tests whenever anything changes.  Cool!  Unfortunately, guard doesn’t expand wildcards like the terminal and expresso relies on this to test folders recursively.  I’ve pushed a –d –directory option to my [fork](https://github.com/cromwellryan/expresso) if you want it.  I’ll submit a pull request later, but don’t hold your breath.

Cool my fast tests are running when I change things in my app.  Now it’s time for a results notification.  Unfortunately, expresso only has Growl support, but not libnotify… foiled again!  No fear, [christiaan](https://github.com/christiaan) has a [pull request](https://github.com/visionmedia/expresso/pull/70) pending just for this reason.  But how do *I* get it?

Grrr!

Not really.  First I fork expresso

[![image](http://blog.cromwellhaus.com/wp-content/uploads/2011/09/image_thumb2.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2011/09/image2.png)

Then I add christiaans fork to my remotes

> git remote add christiaan git://github.com/christiaan/expresso.git

Then I pull in his commits

> git fetch christiaan

Push the result up to my repo for nice people like you.

> git push origin master

OK it’s in there, but how do I USE it?  Well npm (node package manager) has support for a smooth dev experience like this.

I can jump into my expresso fork repo and use *npm link*:

> cd ~/projects/expresso
>
> npm link

*npm link* will create a symlink in my global package source which I can then use anywhere.  I could also *npm link* them into any local projects, but this works for me at the moment.  I might depend on them locally later, but we’ll see.

Now when I change things in my project, guard notices and tells expresso to do it’s thing and I get a notification as to how things went.  Pretty nice.

[![image](http://blog.cromwellhaus.com/wp-content/uploads/2011/09/image_thumb3.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2011/09/image3.png)

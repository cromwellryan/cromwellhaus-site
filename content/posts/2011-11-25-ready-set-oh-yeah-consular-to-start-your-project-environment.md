---
title: "Ready. Set. Oh yeah! Consular to start your project environment"
date: "2011-11-25"
slug: "ready-set-oh-yeah-consular-to-start-your-project-environment"
categories: ["node"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2011/11/ready-set-oh-yeah-consular-to-start-your-project-environment/", "http://blog.cromwellhaus.com:80/2011/11/ready-set-oh-yeah-consular-to-start-your-project-environment/"]
wayback_source: "https://web.archive.org/web/20120117212040/http://feeds.feedburner.com:80/RyanCromwell"
excerpt_only: false
permalink: "/2011/11/ready-set-oh-yeah-consular-to-start-your-project-environment/"
---

I have a number of cool tools that run in a watching pattern while I work my nodejs apps.  I use guard to watch package.js, Gemfile and some others.  node-dev watches the app as a whole and restarts my node app.  vows is watching the world to run my tests.

It’s really nice to forget about all that cruft and just build the app while those things work automagically.  Unfortunately the magic doesn’t start until I say go.  And go.  And go.  And go.

There has to be a better way than starting half a dozen terminals or terminal tabs and  remembering to run guard, node-dev, vows, etc.  Turns out there is [@rubyist](http://www.twitter.com/rubyist) and [@pragma\_tech](http://www.twitter.com/pragma_tech) had the cheese: terminitor.

Yeah – read it again: termin**i**tor.  The govna isn’t much help.  It’s a different dude.  Even turns out people were so confused they changed the name to [consular](https://github.com/achiu/consular).

I’m not entirely sure how consular does it’s magic, but I did piece together the Ubuntu puzzle.  Here’s the deal:

1. Make sure to export TERM\_EDITOR & EDITOR (vim for me) in your ~/.bashrc.  If you use a different shell, YMMV.

> sudo apt-get install xdotool

This appears to be a keyboard & mouse abstraction layer.  This is required by a consular ‘core’.  Coming soon.

> gem install consular
>
> gem install consular-gnome-terminal

Initialize and configure consular with:

> consular init

This should open ~/.consularch in your editor if you have TERM\_EDITOR  configured.  Add

> require ‘consular/gnome-terminal’

Head to a project directory in your terminal and

> consular edit

This will create and open a Termfile in your editor of choice.  This file has some sample configurations using Now you can get rolling by running:

> consular start

This will run the default, but you can [learn the DSL](https://github.com/achiu/consular/wiki/Consular-Script-DSL) and start everything from guard to your vim environment.  Get into your working mode faster.

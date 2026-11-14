---
title: "My Learning Elixir (erlang) Setup"
date: "2013-07-04"
slug: "my-learning-elixir-erlang-setup"
categories: ["Code", "Uncategorized"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2013/07/my-learning-elixir-erlang-setup/", "http://cromwellhaus.com:80/2013/07/my-learning-elixir-erlang-setup", "http://cromwellhaus.com:80/2013/07/my-learning-elixir-erlang-setup/", "https://cromwellhaus.com/2013/07/my-learning-elixir-erlang-setup/"]
wayback_source: "https://web.archive.org/web/20130828002658/http://cromwellhaus.com/feed/"
excerpt_only: false
permalink: "/2013/07/my-learning-elixir-erlang-setup/"
---

The last [Dayton Clean Coders](http://daytoncleancoders.com "Dayton Clean Coders") meeting spiked my squirrel sense as [Chris McCord](http://twitter.com/chris_mccord "Chris McCord on Twitter") and [Matt Sears](http://twitter.com/mattsears "Matt Sears on Twitter") of our awesome host [Little Lines](http://littlelines.com "Little Lines") talked about their excitement for [Elixir](http://elixir-lang.org "Elixir Language on Erlang"). Of course, I’ve hung my several dozen half baked projects up for the moment as I scratch that itch.

Elixir is a Ruby inspired language that compiles down to Erlang bitcode. You can fall back to any Erlang library and many of the syntaxes, but the language is crazy easy to pick up if you’ve tried any of the other Ruby inspired languages like Coffeescript.

Here’s my setup for walking through the [Elixir Getting Started](http://elixir-lang.org/getting_started/1.html "Elixir Getting Started"):

1. vim with my [vim-config](http://github.com/cromwellryan/vim-config "My Vim configuration")
2. iex, interactive elixir will load compiled elixir modules found in the same directory. This means I can put bigger functions, modules, protocols, etc. into \*.ex files and then explore and play with them using iex.  You need to run

   ```
   r(ModuleName)
   ```

   to reload after compiles.
3. Guard running this [Guardfile](https://gist.github.com/cromwellryan/5924636 "Guardfile for elixirc") for automatically compiling the \*.ex files.

[![vim + iex + guard = flatting the curve](/images/wp-content/uploads/2013/07/2013-07-04_08-30-09.png)](/images/wp-content/uploads/2013/07/2013-07-04_08-30-09.png)

vim + iex + guard = flatting the curve

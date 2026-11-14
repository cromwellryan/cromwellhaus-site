---
title: "Triangle Kata in Elixir using Erlang processes for Parallel Maps"
date: "2013-07-17"
slug: "triangle-kata-in-elixir-using-erlang-processes-for-parallel-maps"
categories: ["Code", "Uncategorized", "elixir"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2013/07/triangle-kata-in-elixir-using-erlang-processes-for-parallel-maps/", "https://cromwellhaus.com/2013/07/triangle-kata-in-elixir-using-erlang-processes-for-parallel-maps/"]
wayback_source: "https://web.archive.org/web/20130828002658/http://cromwellhaus.com/feed/"
excerpt_only: false
permalink: "/2013/07/triangle-kata-in-elixir-using-erlang-processes-for-parallel-maps/"
---

Last time I described [my setup for learning Elixir](/2013/07/my-learning-elixir-erlang-setup/ "My Learning Elixir (erlang) Setup"), the language built on top of Erlang with a Ruby bent.  Today I wanted to get a hang of processes and mailboxes which are so important to both languages.  To do this I chose the Triangle Kata as my background story.  [Take a look](https://gist.github.com/cromwellryan/6024862):

**Update:** You might wonder what that `slow` function is all about. I added that in there to clarify the parallelism. You would expect the slowest classifications to appears at the end of the resultant list.

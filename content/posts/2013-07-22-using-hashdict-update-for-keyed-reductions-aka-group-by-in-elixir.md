---
title: "Using HashDict.update for Keyed Reductions (aka group by) in Elixir"
date: "2013-07-22"
slug: "using-hashdict-update-for-keyed-reductions-aka-group-by-in-elixir"
categories: ["Code", "Uncategorized", "elixir"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2013/07/using-hashdict-update-for-keyed-reductions-aka-group-by-in-elixir/", "https://cromwellhaus.com/2013/07/using-hashdict-update-for-keyed-reductions-aka-group-by-in-elixir/"]
wayback_source: "https://web.archive.org/web/20171019071613/https://cromwellhaus.com/feed/"
excerpt_only: false
permalink: "/2013/07/using-hashdict-update-for-keyed-reductions-aka-group-by-in-elixir/"
---

I wanted to start playing with Elixir’s Map and Reduce functions to get a better feel for collection transformations in the language.  For this I grabbed some movie [data here](https://github.com/tadams/MapReduce/blob/master/src/main/data/movies.txt "tadams' movie data") and planned on grabbing some perspectives.

First problem, we need to turn the data into a list of tuples.  The pseudo-transformation we want to apply:

```
file -> lines
lines -> parts
parts -> tuples
```

The results ended up looking like this

[gist id=”6051117″ file=”movies.exs”]

For our data perspectives, lets start small.  The number of movies per year.  This is still a transformation, but it’s not going to be a one-for-one.  We’re instead going to reduce the results after mapping.  Why would we map?  Turns out the only thing you need to know is a full list of the movie years… with dups.  With that we can do an “Add or Update” to a hash for each year.

[gist id=”6051117″ file=”uniqueness.exs”]

What we’re doing is providing an entry point for count\_unique which takes a collection.  This creates a new HashDict which seeds our {year, count} and then recursively calls down into a variant of HashDict.update.  This variant will insert a new key if not found with the 3rd parameter being the seed value.  If the key is found HashDict.update will call our anonymous function to increment the value already found.

This pattern seems to work well to get the sum also.  Here we map our collection to pull the year and rating.  I adjusted my original to\_movies to use String.to\_float so that I have a numeric rating.  From there I use the same HashDict pattern with the rating being our seed and accumulator.

[gist id=”6051117″ file=”sumations.exs”]

Next we’ll look at doing something a little more interesting by calculating an average and distributing the effort across nodes using our[previous parallel map](/2013/07/triangle-kata-in-elixir-using-erlang-processes-for-parallel-maps/ "Triangle Kata in Elixir using Erlang processes for Parallel Maps").

---
title: "Installing Erlang 17 for Elixir 0.13 the easy way (Mac)"
date: "2014-04-25"
slug: "installing-erlang-17-for-elixir-0-13-the-easy-way"
categories: ["elixir"]
tags: []
original_urls: ["http://cromwellhaus.com/2014/04/installing-erlang-17-for-elixir-0-13-the-easy-way/", "https://cromwellhaus.com/2014/04/installing-erlang-17-for-elixir-0-13-the-easy-way/"]
wayback_source: "https://web.archive.org/web/20140519012241/http://cromwellhaus.com/feed/"
excerpt_only: false
permalink: "/2014/04/installing-erlang-17-for-elixir-0-13-the-easy-way/"
---

As of Elixir 0.13, you’ll need to have Erlang 17 installed.  If you use brew to install erlang then elixir you’ll find this message awaiting you:

```
ERROR: OTP release R16B03-1 does not match required regex (17).*
```

The current Erlang brew formula is still at R16B03-1.  BUT! the development version IS 17.  So here you go:

```
brew install --devel erlang
```

I’m sure this will change soon, but until then this’ll get you going again.

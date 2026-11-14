---
title: "Greatest Overeager Design Decision: Assignment"
date: "2010-12-17"
slug: "greatest-overeager-design-decision-assignment"
categories: [".Net", "Craftsmanship", "TDD", "Testing"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2010/12/greatest-overeager-design-decision-assignment/", "http://cromwellhaus.com/2010/12/greatest-overeager-design-decision-assignment/"]
wayback_source: "https://web.archive.org/web/20110214141118/http://blog.cromwellhaus.com:80/feed/"
excerpt_only: false
permalink: "/2010/12/greatest-overeager-design-decision-assignment/"
---

In a getting back to basics moment of mine, I started through the [TDD Problems](http://sites.google.com/site/tddproblems/).  I found myself on the [Console Interaction problem](http://sites.google.com/site/tddproblems/all-problems-1/Console-interaction) and decided to take a step back from after refactoring.  This is what I saw:

```csharp
var shape = _console.AskForShape();

var rectange = GetRectange();

_console.PrintArea(rectange.ComputeArea());
_console.PrintCircumference(rectange.ComputeCircumference());
```

ReSharper was hinting at it, but it should have screamed.  Why do I need to hang on to shape?  I can imagine my mindset at the time.  I was worried about the inevitable *decision* I would have to make about 20 tests down the road.  That little assignment was the beginning of my overeager, premature design.

Question your code.

---
title: "We forgot a Pull Request when Splitting a Repo"
date: "2016-08-31"
slug: "we-forgot-a-pull-request-when-splitting-a-repo"
categories: ["Uncategorized"]
tags: []
original_urls: ["http://cromwellhaus.com/2016/08/we-forgot-a-pull-request-when-splitting-a-repo/", "https://cromwellhaus.com/2016/08/we-forgot-a-pull-request-when-splitting-a-repo/"]
wayback_source: "https://web.archive.org/web/20160906095636/http://cromwellhaus.com:80/"
excerpt_only: false
permalink: "/2016/08/we-forgot-a-pull-request-when-splitting-a-repo/"
---

We’re working on a little skunk works project at the office and it involved splitting a Github repository in two. After a successful split, I noticed we’d missed a PR that now impacts both repositories.

My head went to `git format-patch <sha>`, but I didn’t recall an option to target a file spec and at first glance it generates a patch for every commit after that SHA.

`git show` on the other hand definitely advertises an option to filter`git show <sha> -- path/that/moved`

Format that as `--pretty=email` and you can direct the output to a patch for

```bash
git show --pretty=email <sha> -- path/that/moved> pr-for-other-repo.patch
```

Now we can pull that into our other repo with  `git am -3 pr-for-other-repo.patch`.

Turns out that `-- path/that/moved` semantic does work with `git format-patch`. So in the end, we could have just used

```bash
git format-patch -1 -- path/that/moved
git am -3 partial-pr.patch
```

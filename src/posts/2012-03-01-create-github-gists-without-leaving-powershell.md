---
title: "Create Github Gists without leaving Powershell"
date: "2012-03-01"
slug: "create-github-gists-without-leaving-powershell"
categories: ["Code", "Uncategorized"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2012/03/create-github-gists-without-leaving-powershell/", "http://cromwellhaus.com:80/2012/03/create-github-gists-without-leaving-powershell/"]
wayback_source: "https://web.archive.org/web/20120714210258/http://feeds.feedburner.com/RyanCromwell"
excerpt_only: false
permalink: "/2012/03/create-github-gists-without-leaving-powershell/"
---

[![SNAGHTMLac570d4](http://blog.cromwellhaus.com/wp-content/uploads/2012/03/SNAGHTMLac570d4_thumb.png "SNAGHTMLac570d4")](http://blog.cromwellhaus.com/wp-content/uploads/2012/03/SNAGHTMLac570d4.png)I spend a lot of time in PowerShell.  A lot.  [PoshGit](https://github.com/dahlbyk/posh-git), [Vim](http://vim.org), [Chocolatey](http://chocolatey.org), and [PsGet](http://psget.net)… it’ll get me through most of my dev day happily.

One thing that was killing my workflow was leaving PowerShell to share some snippet of code or a file as a [Gist](http://gist.github.com).  In Visual Studio we have [Gister](visualstudiogallery.msdn.microsoft.com/b31916b0-c026-4c27-9d6b-ba831093f6b2), but when I’m in PS I hate having to break my cycle.

Well no longer…

**Introducing** [**PsGist**](https://github.com/cromwellryan/psgist)

PsGist provides a PowerShell function called (wait for it) gist.  Try not to forget that one, ok?  The usage is simple:

> gist [[-File] <FileInfo>] [[-Description] <String>] [[-Username] <String>]

Username is optional.  If you don’t provide it your gist will be public and anonymous.  If you do, you’ll be prompted for your password.  This is different than [Gister](visualstudiogallery.msdn.microsoft.com/b31916b0-c026-4c27-9d6b-ba831093f6b2) where I only prompt once and cache the creds.  Here you’ll have to specify the password each time.  Deal with it or [fix it](https://github.com/cromwellryan/psgist/pulls).

Here’s an example:

[![SNAGHTMLae19e88](http://blog.cromwellhaus.com/wp-content/uploads/2012/03/SNAGHTMLae19e88_thumb.png "SNAGHTMLae19e88")](http://blog.cromwellhaus.com/wp-content/uploads/2012/03/SNAGHTMLae19e88.png)

Notice how after the gist is created the Url is written to the console/host?  Well PsGist also puts the Url into your clipboard.  So you can quickly go to IRC, IM, Twitter, etc and past the Url.  Or you can use ALT+<Space>, E, P to paste it quickly into your console and open the gist.

**Needed: Pipe the output**

I’d like to be able to pipe the output to start, clip, out-file and other useful commands.  For whatever reason powershell won’t wait on the gist being created before running the following command.  If you know how to make this happen, hit me up on [Twitter](http://twitter.com/cromwellryan), send a pull request or leave it in the comments.

**Needed: Multiple File Gists**

I’d like to be able to run ls | gistand have all the files in the listing sent to a single gist, but there is a problem with convertfrom-json that I’m struggling with.  I have a branch called pipelinesupport that you can try, but it takes single file gists away until I put that back and fix the json issue.

**Needed: Make it a Module**

This should really be a module.  I’m sure with another hour’s worth of research and effort I could make that happen, but, well, it works.  If you like PsGist and want to make it a Module, I’ll gladly accept the pull request.

**Thanks to [@Jaykul](http://twitter.com/jaykul)**

For providing the [convertfrom-json](http://poshcode.org/2098) function used to handle the Github Api response.  PowerShell 3 seems to have [this support](http://www.dougfinke.com/blog/index.php/2011/09/15/powershell-v3-and-json/) built in, but that’s not here quite yet.

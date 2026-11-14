---
title: "Signing your Powershell Profile Scripts"
date: "2007-04-23"
slug: "signing-your-powershell-profile-scripts"
categories: ["Powershell"]
tags: ["Powershell"]
original_urls: ["http://blog.cromwellhaus.com/2007/04/signing-your-powershell-profile-scripts/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/04/23/signing-your-powershell-profile-scripts.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/04/23/signing-your-powershell-profile-scripts.aspx"]
wayback_source: "https://web.archive.org/web/20080118081529/http://cromwellhaus.com:80/blogs/MainFeed.aspx"
excerpt_only: false
permalink: "/2007/04/signing-your-powershell-profile-scripts/"
---

Running with [Set-ExecutionPolicy](http://www.microsoft.com/technet/scriptcenter/topics/msh/cmdlets/set-executionpolicy.mspx) as AllSigned or Restricted with a roaming profile?  Here's a cmdlet pair that will sign all the scripts in your profile directory.  Makes life easier on me as I include a number of scripts into my main profile for readability:

> *function sign-profile()  
> {  
>     dir $Profiledir\\*.ps1 | foreach-object { sign-script $\_.FullName }  
> }*
>
> *function sign-script( $scriptsource )   
> {  
>     get-item $scriptsource   
>     Set-AuthenticodeSignature $scriptsource @(Get-ChildItem cert:\CurrentUser\My -codesigning)[0]  
> }*

And if you aren't already using Powershell, stop wasting your time with the Command Prompt and [go get it](http://www.microsoft.com/powershell/download).  Don't forget the [Powershell Community Extensions](http://www.codeplex.com/PowerShellCX/)



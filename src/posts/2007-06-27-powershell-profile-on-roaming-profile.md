---
title: "PowerShell Profile on Roaming Profile"
date: "2007-06-27"
slug: "powershell-profile-on-roaming-profile"
categories: ["Powershell"]
tags: ["Powershell"]
original_urls: ["http://blog.cromwellhaus.com/2007/06/powershell-profile-on-roaming-profile/", "http://blog.cromwellhaus.com:80/index.php/2007/06/powershell-profile-on-roaming-profile/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/06/27/powershell-profile-on-roaming-profile.aspx", "http://cromwellhaus.com:80/2007/06/powershell-profile-on-roaming-profile/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/06/27/powershell-profile-on-roaming-profile.aspx"]
wayback_source: "https://web.archive.org/web/20100307210904/http://blog.cromwellhaus.com:80/index.php/2007/06/powershell-profile-on-roaming-profile/"
excerpt_only: false
permalink: "/2007/06/powershell-profile-on-roaming-profile/"
---

NOTE: Impatience just leads to frustration.

When I first starting playing with PowerShell here at the office, I was all excited to start adding little cmdlets to my personal profile and add to my stellar productivity (tongue firmly planted in check).  This would hopefully reduce the net loss incurred by my learning PowerShell in the first place.

So I took the first step and created my empty profile:

> *ps> notepad $profile*

and added a nice little cmdlet to send email.  This will replace that exe tool I’ve always used to send emails in batch files or just whenever I need to at the command prompt.

> *$defaultSendMailHost = “emcrs71″  
> $defaultSendMailFrom = [email@email.com](mailto:email@email.com)*
>
> *function send-mail( [string] $to, [string] $subject, [string] $body )  
> {  
>      $smtp = new-object System.Net.Mail.SmtpClient  
>      $smtp.Host = $defaultSendMailHost  
>      $email = new-object System.Net.Mail.MailMessage  
>      $email.From = $defaultSendMailFrom  
>      $email.To.Add( $to )  
>      $email.Subject = $subject  
>      $email.Body = $body  
>      $smtp.Send( $email )  
> }*

Start it up again and WHAM…

> File \\<server>\<username>\My Documents\WindowsPowerShell\Microsoft.PowerShell\_profile.ps1 cannot be loaded. The file \\<server>\<username>\My Documents\WindowsPowerShell\Microsoft.PowerShell\_profile.ps1 is not digitally signed. The script will not execute on the system. Please see “get-help about\_signing” for more details.

Sign *my* scripts?!  How dare you!  I was too annoyed to deal with it and took the ever so appalling step of changing the PowerShell Short cut to point to a local folder on my C drive.  Please don’t stop reading as I’ve learned from my mistakes and have rectified my ways.

A few weeks later I ran across the [PowerShell Community Extensions](http://www.codeplex.com/PowerShellCX/), which I highly recommend PowerShell-er install and, in fact, replaced my send-mail cmdlet above.  PSCX has an option to install it’s own profile which I chose, but after that I started receiving the Digital Signing guff.

In the end, I did what any good PowerShell-er with a growing Profile should do.  I created a cmdlet to sign my profile.  Now I can open PS, type edit-profile (or use my ep alias), save it, and hit sign-profile (sp alias) and I’m good to go.  Here it is:

> function edit-profile()  
> {  
>     notepad $profile  
> }
>
> function sign-profile()  
> {  
>     dir $Profiledir\\*.ps1 | foreach-object { sign-script $\_.FullName }  
> }
>
> function sign-script( $scriptsource )   
> {  
>     get-item $scriptsource   
>     Set-AuthenticodeSignature $scriptsource @(Get-ChildItem cert:\CurrentUser\My -codesigning)[0]  
> }
>
> set-alias sm Send-SmtpMail  
> set-alias ep edit-profile  
> set-alias sp sign-profile

Now there is a little part I left out and that’s creating yourself a certificate, but [Scott Hanselman](http://www.hanselman.com/blog/) has a very good [post](http://www.hanselman.com/blog/SigningPowerShellScripts.aspx) that will walk you through this.

[Technorati Profile](http://technorati.com/claim/rgidkvtvc8)

- [Previous Entry: Bind to Method within a DataTemplate](/2007/06/bind-to-method-within-a-datatemplate/)
- [Next Entry: WPF ScaleTransform Direction](/2007/06/wpf-scaletransform-direction/)

---
title: "WPF ScaleTransform Direction"
date: "2007-06-28"
slug: "wpf-scaletransform-direction"
categories: [".Net", "WPF"]
tags: [".Net", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/06/wpf-scaletransform-direction/", "http://blog.cromwellhaus.com:80/2007/06/wpf-scaletransform-direction/", "http://blog.cromwellhaus.com:80/index.php/2007/06/wpf-scaletransform-direction", "http://blog.cromwellhaus.com:80/index.php/2007/06/wpf-scaletransform-direction/comment-page-1/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/06/28/wpf-scaletransform-direction.aspx", "http://cromwellhaus.com:80/2007/06/wpf-scaletransform-direction/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/06/28/wpf-scaletransform-direction.aspx"]
wayback_source: "https://web.archive.org/web/20100306175145/http://blog.cromwellhaus.com:80/index.php/2007/06/wpf-scaletransform-direction"
excerpt_only: false
permalink: "/2007/06/wpf-scaletransform-direction/"
---

The key to scaling your WPF elements in a specific direction other than down and to the right are the CenterX and CenterY properties of the [ScaleTransform](http://www.google.com/url?sa=t&ct=res&cd=1&url=http%3A%2F%2Fmsdn2.microsoft.com%2Fen-us%2Flibrary%2Fsystem.windows.media.scaletransform.aspx&ei=x8yDRrPcA5_KetKXwe4B&usg=AFQjCNFexsnPG0flPExSE8V_uU4hCDxjyQ&sig2=4PL2OhCWOfTTeQ0dzQzBfA).  It’s easy enough to set these manually, but that’s just lazy and asking for long term trouble.  Instead, decide how you want it to animate and bind it to something.  For instance, I have a touch screen keyboard I’m working on that I’d like to animate Up and to the Right when you are holding down the key.  Here’s how I did it:

```xml
<Page xmlns='http://schemas.microsoft.com/winfx/2006/xaml/presentation' xmlns:x='http://schemas.microsoft.com/winfx/2006/xaml'>
  <Button Margin="5,5,5,5" Width="50" Height="50" x:Name="btnKey">
    My Button
    <Button.RenderTransform>
      <ScaleTransform x:Name="buttonscale" ScaleX="1" ScaleY="1" CenterX="0" CenterY="{Binding ElementName=btnKey, Path=ActualHeight}" />
    </Button.RenderTransform>
    <Button.Triggers>
      <EventTrigger RoutedEvent="Button.Click">
        <BeginStoryboard>
          <Storyboard>
            <DoubleAnimation Storyboard.TargetName="buttonscale" Storyboard.TargetProperty="(ScaleTransform.ScaleX)" To="1.5" Duration="0:0:0.25" AutoReverse="True"/>
            <DoubleAnimation Storyboard.TargetName="buttonscale" Storyboard.TargetProperty="(ScaleTransform.ScaleY)" To="1.5" Duration="0:0:0.25" AutoReverse="True"/>
          </Storyboard>
        </BeginStoryboard>
      </EventTrigger>
    </Button.Triggers>
  </Button>
</Page>
```

The key is that I bound the CenterX proeprty to the button’s *ActualHeight* property.  If you wanted to scale from some midpoint though, you’ll have to specify a Converter in your bind syntax.  This Converter technique is often cited in the ubiquitous [“Reflection trick”](http://learnwpf.com/Posts/Post.aspx?postId=9b745fe8-7d51-4d01-a8c7-f31083c4be94).

- [Previous Entry: PowerShell Profile on Roaming Profile](/2007/06/powershell-profile-on-roaming-profile/)
- [Next Entry: Binding to an Image Byte[] in WPF](/2007/07/binding-to-the-byte-of-an-image-in-wpf/)

---
title: "Scrolling Multiple Content Areas with a single ScrollBar in WPF"
date: "2009-03-12"
slug: "scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf"
categories: ["WPF"]
tags: ["WPF"]
original_urls: ["http://blog.cromwellhaus.com/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf/", "http://blog.cromwellhaus.com/index.php/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf/", "http://blog.cromwellhaus.com:80/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf/", "http://blog.cromwellhaus.com:80/index.php/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf", "http://cromwellhaus.com/blogs/ryanc/archive/2009/03/12/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf.aspx", "http://cromwellhaus.com:80/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2009/03/12/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf.aspx"]
wayback_source: "https://web.archive.org/web/20100712115758/http://blog.cromwellhaus.com:80/index.php/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf"
excerpt_only: false
permalink: "/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf/"
---

I struggled to solve a UI dilemma while at my current client.  For various reasons, we came across a situation in which we needed to scroll two areas of the view based on a single Scrollbar.  You can see what we were attempting and finally achieved [here](http://code.cromwellhaus.com/ScrollingMultipleAreasWithOneScrollbar/ScrollingMultipleAreasWithOneScrollbar.xbap).

The end result is smooth, yet not quite intuitive so I thought I would share the results and steps taken.  The idea is to use a surrogate [ScrollViewer](http://msdn.microsoft.com/en-us/library/system.windows.controls.scrollviewer.aspx) as the source for the offset of a [TranslateTransform](http://msdn.microsoft.com/en-us/library/system.windows.media.translatetransform.aspx) being applied to content within a seperate [ScrollViewer](http://msdn.microsoft.com/en-us/library/system.windows.controls.scrollviewer.aspx).

Unfortunately, the offset values exposed by the ScrollViewer are both readonly and opposite in force to which we would need to apply to the surrogate.  That is, if we scroll 20 units to the right on our ScrollViewer, we would need to offset the surrogate ScrollViewer by that amount in the opposite direction.  To resolve this problem, we use an IValueConverter to multiple the offset by –1.

Here we can see the Xaml used to layout and hookup this scenario:

```
```
<StackPanel>
```

```
    <ScrollViewer HorizontalScrollBarVisibility="Hidden" VerticalScrollBarVisibility="Hidden">
```

```
        <Grid>
```

```
            <Grid.RenderTransform>
```

```
                <TranslateTransform X="{Binding ElementName=mainScroller, Path=HorizontalOffset, Converter={StaticResource multiplyConv}, ConverterParameter=-1}" />
```

```
            </Grid.RenderTransform>
```

```
            <!-- Content Scrolled by another goes here -->
```

```
        </Grid>
```

```
    </ScrollViewer>
```

```
    <ScrollViewer x:Name="mainScroller" HorizontalScrollBarVisibility="Auto" VerticalScrollBarVisibility="Auto">
```

```
        <!-- Content Scrolled on its own accord goes here-->
```

```
    </ScrollViewer>
```

```
</StackPanel>
```
```

You can see that we have two ScrollViewers and the one which will be controlled (versus the controller) has a container element with a [TranslateTransform](http://msdn.microsoft.com/en-us/library/system.windows.media.translatetransform.aspx) applied to its RenderTransform property.  This is what we will be using to move the controlled content in the opposite direction of the ScrollBar.

If you find that your content for each are not the same size, you can always use a [MultiBinding](http://msdn.microsoft.com/en-us/library/system.windows.data.multibinding.aspx) to accomodate the relative scrolling distance as applied to the offset.

You can find the source to the sample Xbap [here](http://code.cromwellhaus.com/ScrollingMultipleAreasWithOneScrollbar/ScrollingMultipleAreasWithOneScrollbar.zip).

- [Previous Entry: STUFF & FOR XML PATH](/2009/03/stuff-amp-for-xml-path/)
- [Next Entry: Scaling ItemsControl Items for Explicit Visible Items in WPF](/2009/03/scaling-itemscontrol-items-for-explicit-visible-items-in-wpf/)

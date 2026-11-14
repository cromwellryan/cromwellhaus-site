---
title: "Scaling ItemsControl Items for Explicit Visible Items in WPF"
date: "2009-03-12"
slug: "scaling-itemscontrol-items-for-explicit-visible-items-in-wpf"
categories: ["WPF"]
tags: ["WPF"]
original_urls: ["http://blog.cromwellhaus.com/2009/03/scaling-itemscontrol-items-for-explicit-visible-items-in-wpf/", "http://blog.cromwellhaus.com/index.php/2009/03/scaling-itemscontrol-items-for-explicit-visible-items-in-wpf/", "http://blog.cromwellhaus.com:80/2009/03/scaling-itemscontrol-items-for-explicit-visible-items-in-wpf/", "http://cromwellhaus.com/blogs/ryanc/archive/2009/03/12/scaling-itemscontrol-items-for-explicit-visible-items-in-wpf.aspx", "http://cromwellhaus.com:80/2009/03/scaling-itemscontrol-items-for-explicit-visible-items-in-wpf/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2009/03/12/scaling-itemscontrol-items-for-explicit-visible-items-in-wpf.aspx"]
wayback_source: "https://web.archive.org/web/20090328170516/http://feeds2.feedburner.com:80/RyanCromwell"
excerpt_only: false
permalink: "/2009/03/scaling-itemscontrol-items-for-explicit-visible-items-in-wpf/"
---

Another part of the overall solution we were trying to come up with in conjunction my previous post on [Scrolling Multiple Content Areas](/2009/03/scrolling-multiple-content-areas-with-a-single-scrollbar-in-wpf/), we also needed to come up with a way to only show X number of items in the visible region of an ItemsControl wrapped in a ScrollViewer.  This was more tricky than I had initially anticipated, but the solution seems to work for us and its got relatively few moving parts.

The end result of the concept can be visualize in [this Xbap example](http://code.cromwellhaus.com/ShowingOnlyXVisibleItemsInItemsControl/ShowingOnlyXVisibleItemsInItemsControl.xbap).  By moving the slider at the bottom, you effectively change the width of the ItemsControl containing the colored Ellipses.  In order to do this as a reflection of the number of items contained within, you need another [IMultiValueConverter](http://msdn.microsoft.com/en-us/library/system.windows.data.imultivalueconverter.aspx).

Here is the meat of the code for the RelativeSizeConverter I came up with:

```
```
public class RelativeSizeConverter : IMultiValueConverter
```

```
{
```

```
    public object Convert(object[] values, Type targetType, object parameter, CultureInfo culture)
```

```
    {
```

```
        if( values.Length != 3 )
```

```
            throw new InvalidOperationException("Don't do that!");
```

```
        double containerSize = System.Convert.ToDouble(values[0]);
```

```
        int totalItems = System.Convert.ToInt32(values[1]);
```

```
        int visibleItems = System.Convert.ToInt32(values[2]);
```

```
        var visibleSubgroupSize = containerSize / visibleItems;
```

```
        return totalItems * visibleSubgroupSize;
```

```
    }
```

```
}
```
```

Basically we figure out how wide things would be if we only had the visible items and then we apply that to all the items return.  In order for this to work, there cannot be any sizing between the ItemsControl and the ScrollViewer, but its a small price to pay.  That would look odd any way in my opinion, but maybe I am simply justifying the solution!

Anyways, putting this RelativeSizeConverter to use, we get:

```
```
<ScrollViewer x:Name="container" HorizontalScrollBarVisibility="Auto" VerticalScrollBarVisibility="Auto">
```

```
    <ItemsControl x:Name="itemsToScale">
```

```
        <ItemsControl.Width>
```

```
            <MultiBinding Converter="{StaticResource sizeConverter}">
```

```
                <Binding ElementName="container" Path="ActualWidth" />
```

```
                <Binding ElementName="itemsToScale" Path="Items.Count" />
```

```
                <Binding ElementName="scaleSize" Path="Value" />
```

```
            </MultiBinding>
```

```
        </ItemsControl.Width>
```

```
    </ItemsControl>
```

```
</ScrollViewer>
```

```
<Slider x:Name="scaleSize" Width="100" HorizontalAlignment="Center"
```

```
        Minimum="2" Maximum="{Binding ElementName=itemsToScale, Path=Items.Count}"
```

```
        Value="{Binding ElementName=itemsToScale, Path=Items.Count, Mode=OneWay}"
```

```
        IsSnapToTickEnabled="True" TickFrequency="1" />
```
```

Notice we use the ScrollViewer’s ActualWidth as our “containerSize”.  The ItemsControl itself has the “totalItems” count, and finally we are using a Slider with the name “scaleSize” to adjust the “visibleItems” count.

Code for the [Xbap sample](http://code.cromwellhaus.com/ShowingOnlyXVisibleItemsInItemsControl/ShowingOnlyXVisibleItemsInItemsControl.xbap) at the top can be downloaded [here](http://code.cromwellhaus.com/ShowingOnlyXVisibleItemsInItemsControl/ShowingOnlyXVisibleItemsInItemsControl.zip).



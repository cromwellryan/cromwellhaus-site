---
title: "Bind to Method within a DataTemplate"
date: "2007-06-12"
slug: "bind-to-method-within-a-datatemplate"
categories: [".Net", "WPF"]
tags: [".Net", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/06/bind-to-method-within-a-datatemplate/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/06/12/bind-to-method-within-a-datatemplate.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/06/12/bind-to-method-within-a-datatemplate.aspx"]
wayback_source: "https://web.archive.org/web/20080118081529/http://cromwellhaus.com:80/blogs/MainFeed.aspx"
excerpt_only: false
permalink: "/2007/06/bind-to-method-within-a-datatemplate/"
---

One of my play projects with WPF is a photo viewer for the [pictures](http://cromwellhaus.com/photos) we put out on <http://cromwellhaus.com>.  One of the views is a montage of the latest photos with a random RotateTransform Angle applied to each image's RenderTransform.  Getting the view itself set up as cake, but when I attempted to apply the random angle to each image, it wasn't so random.

Here's what happened and how to actually accomplish such a task:

I started out with an ItemsControl, rather than a ListView as most examples show, using a UniformGrid as the ItemsPanel.

```xml
<ItemsControl ItemTemplate="{StaticResource photoItem}" ItemsSource="{Binding Source={StaticResource dpPhotos}, XPath=/rss/channel/item}">
  <ItemsControl.ItemsPanel>
    <ItemsPanelTemplate>
      <UniformGrid HorizontalAlignment="Stretch"  VerticalAlignment="Stretch" />
    </ItemsPanelTemplate>
  </ItemsControl.ItemsPanel>
</ItemsControl>
```

I bound the ItemsSource to an XmlDataProvider pointing to the photos [RSS feed for Ryan Jr. pictures](http://cromwellhaus.com/photos/baby/pictures_rss.aspx?Tags=Ryan+Jr&AndTags=1).

```xml
<XmlDataProvider x:Key="dpPhotos" Source="http://cromwellhaus.com/photos/baby/pictures_rss.aspx?Tags=Ryan+Jr&amp;AndTags=1" XmlNamespaceManager="{StaticResource rssMapping}"/>
```

I run our site using [Community Server 2007 Express Edition](http://get.communityserver.org/express.aspx) which provides RSS meta extensions for more detailed feeds.  This required that I apply an [XmlNamespaceManager](http://msdn2.microsoft.com/en-us/library/system.xml.xmlnamespacemanager.aspx) to define these extension namespaces.  That's what this is for:

```xml
<XmlNamespaceMappingCollection x:Key="rssMapping">
  <XmlNamespaceMapping Uri="http://search.yahoo.com/mrss" Prefix="media" />
</XmlNamespaceMappingCollection>
```

Here is the DataTemplate used by the ItemsControl to display/render each image.  You'll see this referred to in above as {StaticResource photoItem}:

```xml
<DataTemplate x:Key="photoItem">
  <Image Margin="12,12,12,12" Source="{Binding Mode=Default, XPath=media:thumbnail/@url}" ToolTip="{Binding XPath=title}" Width="{Binding Mode=Default, XPath=media:thumbnail/@width}" Height="{Binding Mode=Default, XPath=media:thumbnail/@height}" />
</DataTemplate>
```

You can see the use of the XmlNamespaceMapping in the XPath=*media:*thumbnail/@url.  That had me stumped for a few seconds, but opening the project up in [Expression Blend](http://www.microsoft.com/Expression/products/overview.aspx?key=blend) and re-adding the XmlDataProvider created the Mappings for me.  (Sidebar: VS 2008 does do this for you - thank goodness)

At this point, we are displaying thumbnails and we are certainly aware that I make poor color choices, but we're on our way.

[![Almost there...](http://cromwellhaus.com/blogs/ryanc/WindowsLiveWriter/BindtoMethodwithinaDataTemplate_CB86/image_thumb_1.png)](http://cromwellhaus.com/blogs/ryanc/WindowsLiveWriter/BindtoMethodwithinaDataTemplate_CB86/image_2.png)

**Applying the RotateTransform** is easy...

```xml
<Image Margin="12,12,12,12" Source="{Binding Mode=Default, XPath=media:thumbnail/@url}" ToolTip="{Binding XPath=title}" Width="{Binding Mode=Default, XPath=media:thumbnail/@width}" Height="{Binding Mode=Default, XPath=media:thumbnail/@height}">
  <Image.RenderTransform>
    <RotateTransform Angle="10" />
  </Image.RenderTransform>
</Image>
```

...and it's almost as easy to use the [System.Random](http://www.google.com/url?sa=t&ct=res&cd=1&url=http%3A%2F%2Fmsdn2.microsoft.com%2Fen-us%2Flibrary%2Fsystem.random.aspx&ei=I-BuRpy4K5TSgwSd7LzRBA&usg=AFQjCNH7kwYGhG5DHJPSH49s3FQbKjrKZA&sig2=fMHOOh5R2_XhBt2qEkxLPw) class to generate the angle.  Just add the following ObjectDataProvider as a Window or Application Resource and bind the Angle property to it:

```xml
<ObjectDataProvider x:Key="randomAngle" ObjectType="{x:Type system:Random}" MethodName="Next">
  <ObjectDataProvider.MethodParameters>
    <system:Int32>-12</system:Int32>
    <system:Int32>12</system:Int32>
  </ObjectDataProvider.MethodParameters>
</ObjectDataProvider>
```

```
...
<RotateTransform Angle="{Binding Source={StaticResource randomAngle}" />
```

Well when you do this, you'll find that you get the same Angle for every image.  This is because you are actually binding to a single instance of the ObjectDataProvider.  To resolve this we actually have to embed the ODP in the transform itself as so:

```xml
<RotateTransform>
  <RotateTransform.Angle>
    <Binding>
      <Binding.Source>
        <ObjectDataProvider ObjectType="{x:Type system:Random}" MethodName="Next">
          <ObjectDataProvider.MethodParameters>
            <system:Int32>-12</system:Int32>
            <system:Int32>12</system:Int32>
          </ObjectDataProvider.MethodParameters>
        </ObjectDataProvider>
      </Binding.Source>
    </Binding>
  </RotateTransform.Angle>
</RotateTransform>
```

*Tada!*[![image](http://cromwellhaus.com/blogs/ryanc/WindowsLiveWriter/BindtoMethodwithinaDataTemplate_CB86/image_thumb_3.png)](http://cromwellhaus.com/blogs/ryanc/WindowsLiveWriter/BindtoMethodwithinaDataTemplate_CB86/image_4.png)

Now you will find that your angle's aren't terribly "Random".  This is because you are actually asking for a new instance of the Random class each time.  You can tell the ODP within the DataTemplate to use the same instance each time by adding this to the Window Resources:

```xml
<ObjectDataProvider x:Key="randomAngle" ObjectType="{x:Type system:Random}"/>
```

and modifying the Angle binding to the following, telling the transform ODP to use a specific resource instance rather than just giving it a type to instantiate each time.

```xml
<ObjectDataProvider ObjectInstance="{StaticResource randomAngle}" MethodName="Next">
  <ObjectDataProvider.MethodParameters>
    <system:Int32>-12</system:Int32>
    <system:Int32>12</system:Int32>
  </ObjectDataProvider.MethodParameters>
</ObjectDataProvider>
```

You can download a mini-version used to write this post [here](http://cromwellhaus.com/files/folders/wpf/entry192.aspx "WPFBindToMethodExample").

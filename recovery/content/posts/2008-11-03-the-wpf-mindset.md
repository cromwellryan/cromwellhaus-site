---
title: "The WPF Mindset"
date: "2008-11-03"
slug: "the-wpf-mindset"
categories: ["WPF"]
tags: ["WPF"]
original_urls: ["http://blog.cromwellhaus.com/2008/11/the-wpf-mindset/", "http://blog.cromwellhaus.com/index.php/2008/11/the-wpf-mindset/", "http://blog.cromwellhaus.com:80/index.php/2008/11/the-wpf-mindset", "http://blog.cromwellhaus.com:80/index.php/2008/11/the-wpf-mindset/", "http://blog.cromwellhaus.com:80/index.php/2008/11/the-wpf-mindset/comment-page-1/", "http://cromwellhaus.com/2008/11/the-wpf-mindset/", "http://cromwellhaus.com/blogs/ryanc/archive/2008/11/03/the-wpf-mindset.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/11/03/the-wpf-mindset.aspx"]
wayback_source: "https://web.archive.org/web/20100221213909/http://blog.cromwellhaus.com:80/index.php/2008/11/the-wpf-mindset"
excerpt_only: false
permalink: "/2008/11/the-wpf-mindset/"
---

WPF is awesome, but it requires the developer to make a pretty big shift in their thinking of UI.  I’ve had a hard time explaining this to people, but last week, I had an opportunity to work through an example with [Steve Gentile](http://blogger.forgottenskies.com/).  That’s the basis of this walkthrough.

## The Scenerio

Steve has an ASP.Net website he maintains called [ForgottenSkies.com](http://www.forgottenskies.com/).  One of the pages displays a map from the game with events that were captured from the server.  You can see the ASP.Net version [here](http://www.forgottenskies.com/ForgottenWars/FSWarMap.aspx).  Steve was looking to create a Silverlight version of this page.

**The Wrong Mindset**

The initial response from most developers would be to put an image on the “form” and then figure out a way to place some composite control or other image that would denote each event’s location.  If they had the inclination they might use the DataContext, but they likely would also iterate each Event in some collection and manually place these controls within some container.  I believe Steve was trying to place them into a really big grid with lots of Rows and Columns to represent the Latitude and Longitude of the map.

## The WPF Mindset

Decomposing this scenario is vital to using WPF properly.  When it comes down to it, the map is really just a way to visualize a collection of Events. If we wanted we could easily make this a list, couldn’t we?  So lets start there:

For the purposes of this demo, the Window.DataContext is set to an instance of an AttackService, which looks like the following:

```csharp
public class AttackService
{
    public ObservableCollection<Attack> Attacks { get; private set; }
    public int MapSize { get; set; }
    public AttackService()
    {
        this.MapSize = 160;
        this.Attacks = new ObservableCollection<Attack>();
        Random random = new Random();
        for(int index =0; index < 10;index++)
        {
            var attack = new Attack
            {
                Description = string.Format("Attack {0}", index),
                Latitude = random.Next(0, MapSize),
                Longitude = random.Next(0, MapSize),
                Type = (AttackType)random.Next(0, 2)
            };
            this.Attacks.Add(attack);
        }
    }
}
```

Our goal is to display the Attacks collection, so let’s do that:

```xml
<Window x:Class="WpfApplication1.Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
    <Grid>
        <ListView ItemsSource="{Binding Attacks}" />
    </Grid>
</Window>
```

[![image](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_thumb_5F00_4616D28A.png "image")](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_357ED79C.png)We have a ListView which has it’s ItemsSource bound to our Attacks collection.  Nothing special.  WPF doesn’t know how to display an Attack class so if we would just see a 10 instances of our class name listed.  We’ll get there though.

For starters, lets look at these as if they were listed in a table (or GridView). To do this, we’ll tell the ListView to use a style, *attacksList*.  We’ll place this style definition in our Window’s Resources collection for convenience of our demo.

```xml
<Window x:Class="WpfApplication1.Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
    <Window.Resources>
        <Style x:Key="attacksList" TargetType="ListView">
            <Setter Property="View">
                <Setter.Value>
                    <GridView>
                        <GridViewColumn DisplayMemberBinding="{Binding Description}" />
                        <GridViewColumn Header="Latitude" DisplayMemberBinding="{Binding Latitude}" />
                        <GridViewColumn Header="Longitude" DisplayMemberBinding="{Binding Longitude}" />
                    </GridView>
                </Setter.Value>
            </Setter>
        </Style>
    </Window.Resources>
    <Grid>
        <ListView x:Name="attacksList" ItemsSource="{Binding Attacks}" Style="{StaticResource attacksList}" />
    </Grid>
</Window>
```

What we’ve done is given ourselves a way to set values or properties on the ListView.  [![image](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image6_5F00_thumb_5F00_74ACDB6C.png "image")](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image6_5F00_7253596E.png)For the sample you see here, we set the type of View for the ListView to be a GridView.

## The Map

The ultimate visualization of this information is to display it contextually in a map.  It’s important to remember that this is still a list, we just want to visualize the list differently.  To do this we need to change our *attacksListStyle*.

```xml
<Style x:Key="attacksList" TargetType="ListView">
    <Setter Property="ItemsPanel">
        <Setter.Value>
            <ItemsPanelTemplate>
                <Canvas>
                    <Canvas.Background>
                        <ImageBrush ImageSource="Images\Map.jpg" />
                    </Canvas.Background>
                </Canvas>
            </ItemsPanelTemplate>
        </Setter.Value>
    </Setter>
    <Setter Property="ItemContainerStyle" Value="{StaticResource attackContainerStyle}" />
</Style>
```

Instead of setting the View of our ListView, we are now setting the ItemsPanel to a Canvas.  This tells the ListView to place all of the items its charged with listing into the Canvas.  We have chosen canvas, because we will want to place each item via coordinates (X/Y, Left/Type) rather than stacking, row/column, etc.  The background of our Canvas is going to be a JPG version of our map.  Backgrounds and Foregrounds are always brushes, so we are using an ImageBrush to draw our map on the Canvas background.

The second property we are setting is the *ItemContainerStyle* to the *attackContainerStyle*.  The ListView places each item into a container rather than displaying it directly.  In order to place it correctly, we need to set the Top and Left properties of this ItemContainer.

```xml
<Style x:Key="attackContainerStyle">
    <Setter Property="Canvas.Top" Value="{Binding Latitude}" />
    <Setter Property="Canvas.Left" Value="{Binding Longitude}" />
</Style>
```

This binds the Canvas.Top and Canvas.Left [DependencyProperties](http://msdn.microsoft.com/en-us/library/ms752914.aspx) to the Attack.Latitude and Attack.Longitude properties respectively.  To bring this together, we have our ListView bound to a collection of Attacks and the ItemContainer contains each Attack and has its DataContext set to that Attack it is meant to contain.

At this point we have most of what we want.  [![image](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_thumb_5F00_4BA17AC9.png "image")](http://cromwellhaus.com/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/ryanc/image_5F00_33322913.png)Each little black image you see below represents an attack.  This is done by setting the DataTemplate for the Attack type.

```xml
<DataTemplate DataType="{x:Type local:Attack}">
    <Image Source="Images\AlliedTerritory.gif" />
</DataTemplate>
```

The problem you will find is that if you allow the Window to be scaled beyond the size of the map size as it existed when creating the Attack Latitude and Longitude, the points on the map will not scale or move with the map.  I dealt with this by implementing an [IMultiValueConverter](http://msdn.microsoft.com/en-us/library/system.windows.data.imultivalueconverter.aspx).  I won’t go into it here as it doesn’t pertain to our Mindset discussion, but I’ve included it in the attacked source code.

## Summary

If you come into WPF trying to create cool graphics or visualizations from the outset, you will miss the power and productivity of the platform.  WPF and the oft-sited Designer/Developer scenario actually thrive when you begin to simplify your application into the basics and then apply visualizations.

Get the source for this project here:  [Source Code](http://cromwellhaus.com/samples/mapaslistview.zip).  The Xaml for this is literally only 67 lines with spaces.  There is 1 line of custom code in code behind, and you saw the AttackService above.  It’s dead simple.

- [Previous Entry: Why VMWare over Virtual PC](/2008/10/why-vmware-over-virtual-pc/)
- [Next Entry: STUFF & FOR XML PATH](/2009/03/stuff-amp-for-xml-path/)

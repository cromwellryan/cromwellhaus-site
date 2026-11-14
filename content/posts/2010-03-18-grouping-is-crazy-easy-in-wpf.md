---
title: "Grouping is crazy easy in WPF"
date: "2010-03-18"
slug: "grouping-is-crazy-easy-in-wpf"
categories: ["WPF"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2010/03/grouping-is-crazy-easy-in-wpf/", "http://blog.cromwellhaus.com/index.php/2010/03/grouping-is-crazy-easy-in-wpf/", "http://blog.cromwellhaus.com:80/2010/03/grouping-is-crazy-easy-in-wpf/", "http://cromwellhaus.com/2010/03/grouping-is-crazy-easy-in-wpf/", "http://cromwellhaus.com:80/2010/03/grouping-is-crazy-easy-in-wpf", "https://cromwellhaus.com/2010/03/grouping-is-crazy-easy-in-wpf/"]
wayback_source: "https://web.archive.org/web/20100415082621/http://blog.cromwellhaus.com:80/"
excerpt_only: false
permalink: "/2010/03/grouping-is-crazy-easy-in-wpf/"
---

Lots of people struggle with grouping data and when they do, the brut force method normally takes over and we start creating some crazy super structure to organize data and then do something like put a List inside of a List or a Grid inside of a list.  Just think of how many times you tried to put a [GridView inside of a Repeater](http://www.bing.com/search?q=gridview+inside+repeater&go=&form=QBLH&qs=n) back when we didn’t know about jQuery or MVC and WebForms were all we knew.

Well it turns out WPF (and Silverlight 4.0) make this crazy easy.  It’s why the [CollectionViewSource](http://msdn.microsoft.com/en-us/library/system.windows.data.collectionviewsource.aspx) class exists.  The thing people don’t realize is that you don’t have to change anything about your data structure to make this work well (most times) and your designer (you have one right?) can make the decision on how best to display the information.

##### Step 1: Get Yourself Some Data

Don’t go crazy trying to group your data in your view model with Linq statements or anything like that.  You don’t (likely) need it.  Just get a list of your Animals with the necessary attributes for display in normal IEnumerable form.

Here’s how I’m doing to get my data for the sample:

```
```
<Page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
```

```
    <Page.Resources>
```

```
        <XmlDataProvider x:Key="data">
```

```
            <x:XData>
```

```
                <Animals xmlns="">
```

```
                    <Animal name="Dory" Species="Fish" />
```

```
                    <Animal name="Felix" Species="Cat" />
```

```
                    <Animal name="Fluffy" Species="Dog" />
```

```
                    <Animal name="Jake" Species="Snake" />
```

```
                    <Animal name="Mittens" Species="Cat" />
```

```
                    <Animal name="Murtle" Species="Turtle" />
```

```
                    <Animal name="Nemo" Species="Fish" />
```

```
                    <Animal name="Rex" Species="Dog" />
```

```
                    <Animal name="Rover" Species="Dog" />
```

```
                    <Animal name="Toonces" Species="Cat" />
```

```
                </Animals>
```

```
            </x:XData>
```

```
        </XmlDataProvider>
```

```
    </Page.Resources>
```

```
</Page>
```
```

##### Step 2: Group The Data with CollectionViewSource

We need to remember that Xaml is just a way to instantiate classes.  Knowing that, we can create a CollectionViewSource right in our xaml like this:

```
```
<Page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
```

```
    <Page.Resources>
```

```
        <XmlDataProvider x:Key="data">
```

```
            <x:XData>
```

```
                <Animals xmlns="">
```

```
                    <Animal name="Dory" Species="Fish" />
```

```
                    <Animal name="Felix" Species="Cat" />
```

```
                    <Animal name="Fluffy" Species="Dog" />
```

```
                    <Animal name="Jake" Species="Snake" />
```

```
                    <Animal name="Mittens" Species="Cat" />
```

```
                    <Animal name="Murtle" Species="Turtle" />
```

```
                    <Animal name="Nemo" Species="Fish" />
```

```
                    <Animal name="Rex" Species="Dog" />
```

```
                    <Animal name="Rover" Species="Dog" />
```

```
                    <Animal name="Toonces" Species="Cat" />
```

```
                </Animals>
```

```
            </x:XData>
```

```
        </XmlDataProvider>
```

```
        <CollectionViewSource x:Key="animalsBySpecies" Source="{Binding Source={StaticResource data}, XPath=Animals/Animal}">
```

```
            <CollectionViewSource.GroupDescriptions>
```

```
                <PropertyGroupDescription PropertyName="@Species" />
```

```
            </CollectionViewSource.GroupDescriptions>
```

```
        </CollectionViewSource>
```

```
    </Page.Resources>
```

```
</Page>
```
```

##### Step 3: Show The Data

This is where the fun happens.  We take something as simple as a ListView or, simplier yet, the ItemsControl and we hook it up to our CollectionViewSource like this:

```
```
<Page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
```

```
    <Page.Resources>
```

```
        <XmlDataProvider x:Key="data">
```

```
            <x:XData>
```

```
                <Animals xmlns="">
```

```
                    <Animal name="Dory" Species="Fish" />
```

```
                    <Animal name="Felix" Species="Cat" />
```

```
                    <Animal name="Fluffy" Species="Dog" />
```

```
                    <Animal name="Jake" Species="Snake" />
```

```
                    <Animal name="Mittens" Species="Cat" />
```

```
                    <Animal name="Murtle" Species="Turtle" />
```

```
                    <Animal name="Nemo" Species="Fish" />
```

```
                    <Animal name="Rex" Species="Dog" />
```

```
                    <Animal name="Rover" Species="Dog" />
```

```
                    <Animal name="Toonces" Species="Cat" />
```

```
                </Animals>
```

```
            </x:XData>
```

```
        </XmlDataProvider>
```

```
        <CollectionViewSource x:Key="animalsBySpecies" Source="{Binding Source={StaticResource data}, XPath=Animals/Animal}">
```

```
            <CollectionViewSource.GroupDescriptions>
```

```
                <PropertyGroupDescription PropertyName="@Species" />
```

```
            </CollectionViewSource.GroupDescriptions>
```

```
        </CollectionViewSource>
```

```
    </Page.Resources>
```

```
    <DockPanel>
```

```
        <ScrollViewer DockPanel.Dock="Bottom" VerticalScrollBarVisibility="Auto">
```

```
            <ItemsControl ItemsSource="{Binding Source={StaticResource animalsBySpecies}}">
```

```
                <ItemsControl.ItemTemplate>
```

```
                    <DataTemplate>
```

```
                        <TextBlock Text="{Binding XPath=@name}" />
```

```
                    </DataTemplate>
```

```
                </ItemsControl.ItemTemplate>
```

```
            </ItemsControl>
```

```
        </ScrollViewer>
```

```
    </DockPanel>
```

```
</Page>
```
```

This doesn’t give us anything we couldn’t do before:[![image](/images/wp-content/uploads/2010/03/image_thumb.png "image")](http://blog.cromwellhaus.com/wp-content/uploads/2010/03/image.png)

So how do we represent this grouping?

##### Step 3: Display the Grouping

Easy, we define the GroupStyle.  There is an awful lot we can do here, but we’ll go with putting each into a GroupBox with the Header being the Species.

```
```
<Page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
```

```
    <Page.Resources>
```

```
        <XmlDataProvider x:Key="data">
```

```
            <x:XData>
```

```
                <Animals xmlns="">
```

```
                    <Animal name="Dory" Species="Fish" />
```

```
                    <Animal name="Felix" Species="Cat" />
```

```
                    <Animal name="Fluffy" Species="Dog" />
```

```
                    <Animal name="Jake" Species="Snake" />
```

```
                    <Animal name="Mittens" Species="Cat" />
```

```
                    <Animal name="Murtle" Species="Turtle" />
```

```
                    <Animal name="Nemo" Species="Fish" />
```

```
                    <Animal name="Rex" Species="Dog" />
```

```
                    <Animal name="Rover" Species="Dog" />
```

```
                    <Animal name="Toonces" Species="Cat" />
```

```
                </Animals>
```

```
            </x:XData>
```

```
        </XmlDataProvider>
```

```
        <CollectionViewSource x:Key="animalsBySpecies" Source="{Binding Source={StaticResource data}, XPath=Animals/Animal}">
```

```
            <CollectionViewSource.GroupDescriptions>
```

```
                <PropertyGroupDescription PropertyName="@Species" />
```

```
            </CollectionViewSource.GroupDescriptions>
```

```
        </CollectionViewSource>
```

```
    </Page.Resources>
```

```
    <DockPanel>
```

```
        <ScrollViewer DockPanel.Dock="Bottom" VerticalScrollBarVisibility="Auto">
```

```
            <ItemsControl ItemsSource="{Binding Source={StaticResource animalsBySpecies}}">
```

```
                <ItemsControl.GroupStyle>
```

```
                    <GroupStyle>
```

```
                        <GroupStyle.ContainerStyle>
```

```
                            <Style TargetType="{x:Type GroupItem}">
```

```
                                <Setter Property="Template">
```

```
                                    <Setter.Value>
```

```
                                        <ControlTemplate TargetType="{x:Type GroupItem}">
```

```
                                            <GroupBox Header="{Binding Name}">
```

```
                                                <ItemsPresenter />
```

```
                                            </GroupBox>
```

```
                                        </ControlTemplate>
```

```
                                    </Setter.Value>
```

```
                                </Setter>
```

```
                            </Style>
```

```
                        </GroupStyle.ContainerStyle>
```

```
                    </GroupStyle>
```

```
                </ItemsControl.GroupStyle>
```

```
                <ItemsControl.ItemTemplate>
```

```
                    <DataTemplate>
```

```
                        <TextBlock Text="{Binding XPath=@name}" />
```

```
                    </DataTemplate>
```

```
                </ItemsControl.ItemTemplate>
```

```
            </ItemsControl>
```

```
        </ScrollViewer>
```

```
    </DockPanel>
```

```
</Page>
```
```

We’ve told WPF, take all of the Groups out of the CollectionViewSource and put each into a Container (just like it would with individual items), that container being a GroupItem instead of a ListItem.  Style the GroupItem such that its Template is a GroupBox with an ItemsPresenter inside to display each individual item.  You can do a lot with this and it also works with the GridView form of a ListView.

---
title: "Binding to an Image Byte[] in WPF"
date: "2007-07-26"
slug: "binding-to-the-byte-of-an-image-in-wpf"
categories: [".Net", "WPF"]
tags: [".Net", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2007/07/binding-to-the-byte-of-an-image-in-wpf/", "http://blog.cromwellhaus.com:80/2007/07/binding-to-the-byte-of-an-image-in-wpf/", "http://blog.cromwellhaus.com:80/index.php/2007/07/binding-to-the-byte-of-an-image-in-wpf", "http://blog.cromwellhaus.com:80/index.php/2007/07/binding-to-the-byte-of-an-image-in-wpf/comment-page-1/", "http://cromwellhaus.com/blogs/216.aspx", "http://cromwellhaus.com/blogs/ryanc/archive/2007/07/26/binding-to-the-byte-of-an-image-in-wpf.aspx", "http://cromwellhaus.com:80/2007/07/binding-to-the-byte-of-an-image-in-wpf/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/07/26/binding-to-the-byte-of-an-image-in-wpf.aspx"]
wayback_source: "https://web.archive.org/web/20100306163440/http://blog.cromwellhaus.com:80/index.php/2007/07/binding-to-the-byte-of-an-image-in-wpf"
excerpt_only: false
permalink: "/2007/07/binding-to-the-byte-of-an-image-in-wpf/"
---

I’m working on a WPF app for my wife who coaches our local high school track team.  One of the features she wanted was to have some images for different players and teams and, religious debate aside, I have chosen to save these in SQL Server 2005.  I’m using [NHibernate](http://www.hibernate.org/343.html) for all my data access which has been a great experience (my first).  Impressively, NHibernate supports SQL Server *Image* columns via the inherent *Byte[]* type (See Section 5.1.9 of the [docs](http://www.hibernate.org/hib_docs/nhibernate/html/mapping.html)).  This made adding the Image to my classes **very** easy.

Here’s a snippet of my class with the corresponding NHibernate Mapping Xml File:

> ```
> /* Class */[Serializable]public class Organization : INotifyPropertyChanged{       //...
>
>     public byte[] Image    {        get { return _image; }        set        {            _image = value;            OnPropertyChanged("Image");        }    }
>
>     //...}
> ```
>
> ```
> <!-- Mapping --><hibernate-mapping xmlns="urn:nhibernate-mapping-2.2" default-lazy="false">  <class name="Cromwell.MyApp.Organization, Cromwell.MyApp"          table="dbo.Organization">    <id name="Id" type="Int32" column="Id" unsaved-value="0">      <generator class="native" />    </id>    <many-to-one name="Type"                  class="Cromwell.MyApp.OrganizationType, Cromwell.MyApp"                  column="Type"                  not-null="true"/>    <property name="Name" type="String" length="255" column="Name" not-null="true"/>    <property name="Address1" type="String" length="255" column="Address1" not-null="false"/>    <property name="Address2" type="String" length="255" column="Address2" not-null="false"/>    <property name="City" type="String" length="255" column="City" not-null="false"/>    <property name="State" type="String" length="2" column="State" not-null="false"/>    <property name="PostalCode" type="String" length="7" column="PostalCode" not-null="false"/>    <property name="Image" type="Byte[]" column="Image" not-null="false" />  </class></hibernate-mapping>
> ```

The key to binding this Image property on my WPF forms is the Binding [Converter](http://cromwellhaus.com/controlpanel/blogs/I%27m%20working%20on%20a%20WPF%20app%20for%20my%20wife%20who%20coaches%20our%20local%20high%20school%20track%20team.%20%20One%20of%20the%20features%20she%20wanted%20was%20to%20have%20some%20images%20for%20different%20players%20and%20teams%20and,%20religious%20debate%20aside,%20I%20have%20chosen%20to%20save%20these%20in%20SQL%20Server%202005.%20%20I%27m%20using%20NHibernate%20for%20all%20my%20data%20access%20which%20has%20been%20a%20great%20experience%20%28my%20first%29.%20%20Impressively,%20NHibernate%20supports%20SQL%20Server%20Image%20columns%20via%20the%20inherent%20Byte%5B%5D%20%20type%20%28See%20Section%205.1.9%20of%20the%20docs%29.%20%20This%20made%20adding%20the%20Image%20to%20my%20classes%20very%20easy.) property.  This property allows you to specify any class which implements [System.Windows.Data.IValueConverter](http://msdn2.microsoft.com/en-us/library/system.windows.data.ivalueconverter.aspx) to act as an intermediary between your bind data and WPF.  In my case, the goal was to turn a byte[] property, Image, into a [BitmapImage](http://msdn2.microsoft.com/en-us/library/system.windows.media.imaging.bitmapimage.aspx) which the an [<Image />](http://msdn2.microsoft.com/en-us/library/ms746717.aspx) control/element can display.

Here’s what I came up with:

> ```
> class BinaryImageConverter : IValueConverter{    object IValueConverter.Convert( object value,         Type targetType,         object parameter,         System.Globalization.CultureInfo culture )    {        if(value != null && value is byte[])        {            byte[] bytes = value as byte[];
>
>             MemoryStream stream = new MemoryStream( bytes );
>
>             BitmapImage image = new BitmapImage();            image.BeginInit();            image.StreamSource = stream;            image.EndInit();
>
>             return image;        }
>
>         return null;    }
>
>     object IValueConverter.ConvertBack( object value,         Type targetType,         object parameter,         System.Globalization.CultureInfo culture )    {        throw new Exception( "The method or operation is not implemented." );    }}
> ```

Here’s how I used it in my WPF Page:

> ```
> <Page x:Class="Cromwell.MyApp.EditOrganization"    ...      xmlns:converts="clr-namespace:Cromwell.MyApp.Converters"    >    <Page.Resources>      <converts:BinaryImageConverter x:Key="imgConverter" />    </Page.Resources>    <Grid>    <!-- Image Control -->    <Image Source="{Binding Path=Image,                     Converter={StaticResource imgConverter}}"            Stretch="UniformToFill"       StretchDirection="Both">      <Image.BitmapEffect>        <DropShadowBitmapEffect Color="Black" />      </Image.BitmapEffect>    </Image>  </Grid></Page>
> ```

I’m going to have to spend some time in the WPF profiler, but this is a big step.  Pretty cool how simple it was and very clean.

- [Previous Entry: WPF ScaleTransform Direction](/2007/06/wpf-scaletransform-direction/)
- [Next Entry: "This problem is being researched"](/2007/08/quot-this-problem-is-being-researched-quot/)

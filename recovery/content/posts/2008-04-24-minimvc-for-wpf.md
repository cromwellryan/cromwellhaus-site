---
title: "MiniMVC for WPF"
date: "2008-04-24"
slug: "minimvc-for-wpf"
categories: ["MVC", "MiniMVC", "WPF"]
tags: ["MVC", "MiniMVC", "WPF"]
original_urls: ["http://blog.cromwellhaus.com/2008/04/minimvc-for-wpf/", "http://cromwellhaus.com/2008/04/minimvc-for-wpf/", "http://cromwellhaus.com/blogs/ryanc/archive/2008/04/24/minimvc-for-wpf.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/04/24/minimvc-for-wpf.aspx"]
wayback_source: "https://web.archive.org/web/20080511113411/http://cromwellhaus.com:80/blogs/ryanc/rss.aspx?Tags=WPF&AndTags=1"
excerpt_only: false
permalink: "/2008/04/minimvc-for-wpf/"
---

Tonight I presented for the [Dayton .Net Developers Group](http://daytondevgroup.net/) on WPF.  Unlike my previous [Lap Around WPF @ CONDG](/2007/09/lap-around-wpf-codng/) which was meant as a beginners guide to WPF, this time we were skipping the basics and plunging into a framework I've dubbed MiniMVC.

MiniMVC is, primarily, a set of [DependencyProperties](http://msdn2.microsoft.com/en-us/library/system.windows.dependencyproperty.aspx) and custom [ICommand](http://msdn2.microsoft.com/en-us/library/system.windows.input.icommand.aspx)'s which allow you to specify a Controller for any [FrameworkElement](http://msdn2.microsoft.com/en-us/library/system.windows.frameworkelement.aspx) and/or Action in the [logical tree](http://msdn2.microsoft.com/en-us/library/ms753391.aspx#logical_tree).  Unlike [Dan Crevier's D-V-VM](http://blogs.msdn.com/dancre/archive/2006/10/11/datamodel-view-viewmodel-pattern-series.aspx) pattern or [Josh Smith's MVC pattern](http://www.codeproject.com/KB/WPF/MVCtoUnitTestinWPF.aspx) implementations which rely on explicitly defining [RoutedCommand](http://msdn2.microsoft.com/en-us/library/system.windows.input.routedcommand.aspx)s for each action, [binding them up manually](http://msdn2.microsoft.com/en-us/library/ms752308.aspx), and other unpleasantries (in my humble opinion - these guys still know more than I) with this framework you can use any old class, with any old method, and start executing actions immediately.  Here's an example:

&lt;Window x:Class="PostDemo.Window1"  
       xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"  
       xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"  
       xmlns:mvc="http://cromwellhaus.com/wpf/minimvc"  
       xmlns:demo="clr-namespace:PostDemo">  
  
    &lt;mvc:MiniMVC.Controller>  
        &lt;demo:Window1Controller/>  
    &lt;/mvc:MiniMVC.Controller>  
      
    &lt;StackPanel>  
        &lt;TextBox x:Name="txtMessage"Text="" />  
        &lt;Button>  
            &lt;mvc:MiniMVC.Action>  
                &lt;mvc:ControllerAction Trigger="Click"Action="Echo"   
                       Return="{BindingElementName=txtResult,Path=Text}">  
                    &lt;mvc:ParameterParameterName="message"   
                           Value="{BindingElementName=txtMessage,Path=Text}" />  
                &lt;/mvc:ControllerAction>  
            &lt;/mvc:MiniMVC.Action>  
           Write Something  
       &lt;/Button>  
        &lt;TextBlock x:Name="txtResult" />  
    &lt;/StackPanel>  
&lt;/Window>  

Here's what's going on:

> First, we have this class, Window1Controller, which we are attaching to the Window's MiniMVC.Controller property. 
>
> Second, we are setting the MiniMVC.Action property on the Button to a ControllerAction triggered by the button's Click event.  When *Click* occurs the Action to be taken on the Controller is *Echo*.  We want to pass into Echo the value of the txtMessage TextBox Text value as parameter *message*.  Also, we're specifying that the Return value from Echo should be applied to the Text property of the txtResult TextBox controller.

Cool?  So what's *really* going on?  Well, MiniMVC is handling the most importantly the OnChange event handler for the Action DependencyProperty and using that to dynamically create an ICommand class called ActionCommand.  It's also looking up the Click RoutedEvent via Reflection and adding the ActionCommand's Execute method as the event handler for the located Click RoutedEvent.  There is ZERO code in my code-behind.  The Designer has free-reign to apply the Controller and action to any RoutedEvent he/she chooses and we can all sleep well knowing our [concerns are separated](http://en.wikipedia.org/wiki/Separation_of_concerns).  A happy marriage in my book.

I must give a lot of credit to [Rob Eisenberg](http://devlicio.us/blogs/rob_eisenberg/default.aspx)'s super-awesome [Caliburn](http://caliburn.tigris.org/) project on which much of the Action dependency property is based.  His framework is full featured to the tilt, but is a little over done to my liking with the extensive use of Dependency Injection.  If you find MiniMVC useful, though, I highly recommend you watch for progress on Caliburn.

You can download the full solution, including demo's, from the presentation, as well as the above example project [here](http://cromwellhaus.com/files/folders/wpf/entry581.aspx).

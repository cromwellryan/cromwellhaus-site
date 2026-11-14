---
title: "Advanced WPF ListBox Scenario: Representing and Selecting an XML Hierarchy"
date: "2010-07-22"
slug: "advanced-wpf-listbox-scenario-representing-and-selecting-an-xml-hierarchy"
categories: ["WPF"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2010/07/advanced-wpf-listbox-scenario-representing-and-selecting-an-xml-hierarchy/", "http://blog.cromwellhaus.com/index.php/2010/07/advanced-wpf-listbox-scenario-representing-and-selecting-an-xml-hierarchy/", "http://blog.cromwellhaus.com:80/2010/07/advanced-wpf-listbox-scenario-representing-and-selecting-an-xml-hierarchy", "http://cromwellhaus.com/2010/07/advanced-wpf-listbox-scenario-representing-and-selecting-an-xml-hierarchy/", "https://cromwellhaus.com/2010/07/advanced-wpf-listbox-scenario-representing-and-selecting-an-xml-hierarchy/"]
wayback_source: "https://web.archive.org/web/20100815225045/http://blog.cromwellhaus.com:80/"
excerpt_only: false
permalink: "/2010/07/advanced-wpf-listbox-scenario-representing-and-selecting-an-xml-hierarchy/"
---

I’ve never found a use for the XmlDataProvider natively in Xaml for a shipping app, but today a [@malevy](http://www.twitter.com/malevy) had a situation that sounded interesting.  He has an Xml document structured as follows:

```xml
<Owners>

    <Owner name=”’”>

        <Pet name=”” />

        <Pet name=”” />

    <Owner name=””>

    …

</Owners>
```

He wanted to be able to represent this hierarchy in a ListBox, but actually select from the Pets.  Bonus points for the egregious expander as the owner container.  In the end it was a combination of XmlDataProvider pointing to the Pet nodes, a CollectionViewSource using a GroupDescription which walked up the XPath to Owner\\@name, and the ListBox using an Expander as it’s GroupStyle container.

Here is what it looks like in the end:

[![image](http://content.cromwellhaus.com/c1a9495f0ce8_A464/image_thumb.png "image")](http://content.cromwellhaus.com/c1a9495f0ce8_A464/image.png)

Here’s the [source](http://code.cromwellhaus.com/ListBoxExpanderWithXML.zip).

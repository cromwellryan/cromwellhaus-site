---
title: "ASP.Net MVC Checkbox/boolean Value Mapping"
date: "2007-12-20"
slug: "asp-net-mvc-checkbox-boolean-value-mapping"
categories: [".Net", "MVC"]
tags: [".Net", "MVC"]
original_urls: ["http://blog.cromwellhaus.com/2007/12/asp-net-mvc-checkbox-boolean-value-mapping/", "http://blog.cromwellhaus.com:80/2007/12/asp-net-mvc-checkbox-boolean-value-mapping", "http://blog.cromwellhaus.com:80/index.php/2007/12/asp-net-mvc-checkbox-boolean-value-mapping", "http://blog.cromwellhaus.com:80/index.php/2007/12/asp-net-mvc-checkbox-boolean-value-mapping/", "http://blog.cromwellhaus.com:80/index.php/2007/12/asp-net-mvc-checkbox-boolean-value-mapping/comment-page-1/", "http://cromwellhaus.com/2007/12/asp-net-mvc-checkbox-boolean-value-mapping/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/12/20/asp-net-mvc-checkbox-boolean-value-mapping.aspx", "http://cromwellhaus.com:80/2007/12/asp-net-mvc-checkbox-boolean-value-mapping/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/12/20/asp-net-mvc-checkbox-boolean-value-mapping.aspx"]
wayback_source: "https://web.archive.org/web/20091015031935/http://blog.cromwellhaus.com:80/index.php/2007/12/asp-net-mvc-checkbox-boolean-value-mapping/comment-page-1/"
excerpt_only: false
permalink: "/2007/12/asp-net-mvc-checkbox-boolean-value-mapping/"
---

In my quest to get my [wpfstyle.com](http://wpfstyle.com) site written in the new [ASP.Net MVC](http://asp.net/extensions) framework (day 3) I’ve run across a little issue that I’m sure will come up again.

In my world, a checkbox always seemed to imply true/false or yes/no.  In reality, it can mean a lot of things in an Html Form.  It’s an input, remember, and inputs have a *value*.  When your checkbox is checked, that value is posted back.

Making it work as a boolean indicator in your MVC application, is possible though.  In keeping with the Membership/Authorization theme from [yesterday](/2007/12/asp-net-mvc-and-forms-authentication/), I have the following controller action:

```
public void Authenticate(string userName, string password, bool? rememberMe)
```

```
[Hint: Notice the '?' after bool for the third parameter.  That'll be important in a moment.]
Here is the corresponding Login.aspx View which contains a form posting to this action:
```

```xml
<%using (Html.Form("Authenticate", "Account"))
  { %>
    <div style="margin: auto auto 4px auto">Username
        <%=Html.TextBox( "username") %> </div>
    <div style="margin: auto auto 4px auto">Password &nbsp;
        <%=Html.Password( "password") %></div>

    <div style="margin: auto auto 4px auto">
        <%=Html.CheckBox("rememberme", "Remember Me", "true", false)%>
    </div>
```

```xml
    <div><%=Html.SubmitButton( "Log In") %></div>
<%} %>
```

Looking at our intellisense for Html.Checkbox, we see[![image](http://cromwellhaus.com/blogphotos/ASP.NetMVCCheckboxbooleanValueMapping_138C8/image_thumb.png)](http://cromwellhaus.com/blogphotos/ASP.NetMVCCheckboxbooleanValueMapping_138C8/image.png)

By setting the checkbox’s value to “true” we’re going to have that value sent back through the MVC pipeline to our Action which has a boolean parameter *rememberme*.  It’s not just any boolean though, it’s a nullable boolean.  Remember when I meantion the distinction that the checkbox being checked causes the value to be posted back?  Well if the checkbox is \*not\* checked, the rememberme value will be null.

The MVC pipeline is nice enough to implicitly convert the “true” string to a boolean, but null is not necessarily false in all cases.  To account for this, we must make our parameter a nullable boolean.  Does this maybe cross the line into mixing UI and Controller… eh – possibly?

(NOTE: If you don’t see the Checkbox method in your intellisense, make sure you picked up and referenced the [MVC Toolkit](http://asp.net/downloads/3.5-extensions/MVCToolkit.zip))

- [Previous Entry: ASP.Net MVC and Forms Authentication](/2007/12/asp-net-mvc-and-forms-authentication/)
- [Next Entry: New Year Indeed](/2008/01/new-year-indeed/)

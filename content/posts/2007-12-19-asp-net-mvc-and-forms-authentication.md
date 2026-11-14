---
title: "ASP.Net MVC and Forms Authentication"
date: "2007-12-19"
slug: "asp-net-mvc-and-forms-authentication"
categories: [".Net", "MVC"]
tags: [".Net", "MVC"]
original_urls: ["http://blog.cromwellhaus.com/2007/12/asp-net-mvc-and-forms-authentication/", "http://blog.cromwellhaus.com:80/2007/12/asp-net-mvc-and-forms-authentication", "http://blog.cromwellhaus.com:80/2007/12/asp-net-mvc-and-forms-authentication/", "http://blog.cromwellhaus.com:80/index.php/2007/12/asp-net-mvc-and-forms-authentication", "http://blog.cromwellhaus.com:80/index.php/2007/12/asp-net-mvc-and-forms-authentication/", "http://blog.cromwellhaus.com:80/index.php/2007/12/asp-net-mvc-and-forms-authentication/comment-page-1/", "http://cromwellhaus.com/2007/12/asp-net-mvc-and-forms-authentication/", "http://cromwellhaus.com/blogs/469.aspx", "http://cromwellhaus.com/blogs/ryanc/archive/2007/12/19/asp-net-mvc-and-forms-authentication.aspx", "http://cromwellhaus.com:80/2007/12/asp-net-mvc-and-forms-authentication/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/12/19/asp-net-mvc-and-forms-authentication.aspx"]
wayback_source: "https://web.archive.org/web/20091019115341/http://blog.cromwellhaus.com:80/index.php/2007/12/asp-net-mvc-and-forms-authentication/comment-page-1/"
excerpt_only: false
permalink: "/2007/12/asp-net-mvc-and-forms-authentication/"
---

So last weekend I picked up the new [ASP.Net 3.5 Extensions Preview CTP](http://asp.net/downloads/3.5-extensions/) (and [MVC Toolkit](http://asp.net/downloads/3.5-extensions/MVCToolkit.zip)) from the [ASP.Net](http://asp.net/) team and I’m loving the MVC bits.  I never could get in to [MonoRail](http://www.castleproject.org/monorail/index.html) mainly because I’m a developer diva.  I need intellisense, syntax highlighting, the whole deal.  For a CTP, this release packs quite a punch.

After running through Scott Hanselman’s [*MVC How-To Screencast*](http://www.hanselman.com/blog/ASPNET35ExtensionsPlusMVCHowToScreencast.aspx)and playing around I took to writing a full site I had already 90% completed with Community Server (wpfstyle.com – it’s coming).  Blew threw most of the functionality in the first 3 or 4 hours – awesome.  Then I tried to add Forms Authentication through the easy ASP.Net Configuration button of VS 2008.  Nada.

Long story short, I figured out how to get things working, but there are some manual steps.  Here they are:

****[![image](http://cromwellhaus.com/blogphotos/ASP.NetMVCandFormsAuthentication_146AB/image_thumb.png)](http://cromwellhaus.com/blogphotos/ASP.NetMVCandFormsAuthentication_146AB/image.png)**[Step 1]** Create a new ASP.Net MVC site.  I’ve called mine SecureMVCApplication.

**[Step 2]** Lets add a new controller called SecureController.  This will be our set of actions that only administrators can access.

[![image](http://cromwellhaus.com/blogphotos/ASP.NetMVCandFormsAuthentication_146AB/image_thumb_3.png)](http://cromwellhaus.com/blogphotos/ASP.NetMVCandFormsAuthentication_146AB/image_3.png) **[Step 3]** We don’t need to add any new Actions, the Index action created for us is sufficient, but we will need to do something.  So add a call to RenderView(“Index”) within the Index method.  You’ll also need to create the *index* view, so add a folder called *Secure* under the Views folder already in your project.  To this we will need to add a new MVC View Page item.  To make it clear, I’ve typed “This is for admin eyes only!!!” as the body of my view.

At this point we should make sure things are working.  Hitting F5 should take you to the root of the site, but you could well end up at /Views/Secure/Index.aspx or something like that.  Try browsing to <http://localhost:<port>/secure/index>.  You should see the “This is for admin eyes only!!!” text.  If not, go watch Scott’s screencast and come back.

[![image](http://cromwellhaus.com/blogphotos/ASP.NetMVCandFormsAuthentication_146AB/image_thumb_4.png)](http://cromwellhaus.com/blogphotos/ASP.NetMVCandFormsAuthentication_146AB/image_4.png) **[Step 4]** We’re ready to start securing things.  Use the ASP.Net Configuration button to set security to Internet, create a couple of users and at least 1 role called *Administrators*.  This is for our example, you can call your roles whatever you want in your application.

At this point, you would normally use the *Create Access Rules* link to specify the Adminstrators role has access to the secure directory.  Instead, we have to do this bit ourselves, because the MVC pattern will present us with a URL structure that does not map to physical directories.  At least, probably won’t.  In a normal site, the ASP.Net Configuration tool would add a web.config to each configured directory that specifies the authorization rules.  This brings us to the next step:

**[Step 5]** Open your projects root web.config and add the following:

> <location path=”secure”>  
>   <system.web>  
>     <authorization>  
>       <allow roles=”Adminstrators” />  
>       <deny users=”\*” />  
>     </authorization>  
>   </system.web>  
> </location>

Assuming you are familiar with MVC URLs this is telling us that the <http://<site>/secure> path should allow access to users in the Adminstrators role and deny everyone else.  /secure is, of course, the controller.  Had this been a standard site, the stuff inside the <location /> element would have been found inside our secure\web.config.

**[Step 5]** We are now ready to authenticate our users, but we don’t have a normal login.aspx.  Instead, we’re going to create a controller called *UserController* and add a Login and Authenticate action.  Here’s what I’ve added to my sample:

> ```
> namespace SecureMvcApplication.Controllers
> {
>     public class UserController : System.Web.Mvc.Controller
>     {
>         [System.Web.Mvc.ControllerAction]
>         public void Login()
>         {
>             RenderView("Login");
>         }
>
>         [System.Web.Mvc.ControllerAction]
>         public void Authenticate(string username, string password)
>         {
>             if (System.Web.Security.Membership.ValidateUser(username, password))
>             {
>                 System.Web.Security.FormsAuthentication.RedirectFromLoginPage(username, false);
>             }
>         }
>     }
> }
> ```

Notice that my Login action is simply displaying a view.  This view has two textboxes (one marked password) and a submit button.  If you watch(ed) Scott’s [Screencast](http://www.hanselman.com/blog/ASPNET35ExtensionsPlusMVCHowToScreencast.aspx), I’ve used the [http://asp.net/downloads/3.5-extensions/MVCToolkit.zip](http://asp.net/downloads/3.5-extensions/MVCToolkit.zip "http://asp.net/downloads/3.5-extensions/MVCToolkit.zip") to do this.  The form itself looks like this:

> ```
> <%using (Html.Form("Authenticate?ReturnUrl=" + this.Request["ReturnUrl"], "User"))
>   {%>
>     <div>Username: <%=Html.TextBox("username") %></div>
>     <div>Password: <%=Html.Password("password") %></div>
>     <div><%=Html.SubmitButton("Login") %></div>
> <%} %>
> ```

Upon Submit/Login, we’re POSTing to the *Authenticate( string, string )* Action in our UserController which implements the basic Forms Authentication (above).  The next step is optional, but it helped me watch the authorization status.

**[Step 6]** (Optional)  Add this to your global.asax.cs to see the authorization status of your requests..

> ```
> protected void Application_AuthenticateRequest(object sender, EventArgs e)
> {
>     HttpCookie authCookie = Context.Request.Cookies[FormsAuthentication.FormsCookieName];
>
>     if (null == authCookie)
>     {//There is no authentication cookie.
>         Debug.WriteLine("Don't know you, dude.");
>     }
>     else
>         Debug.WriteLine("Enjoy the party!");
> }
> ```

Now F5 and browse to <http://localhost:<port>/secure/index> and you should be taken to the <http://localhost:<port>/user/login> page.  Upon hitting login, you’re directed back to the root of the site.  In our form, we had to manually set the ReturnUrl, because Forms Authentication assumes you will be posting back to yourself (classic ASP.Net Web Form).  We’re posting across to the Authenticate action Url.

You can download the completed VS 2008 project I used [here](http://cromwellhaus.com/files/folders/netcode/entry468.aspx).

Can you believe we’re already calling ASP.Net Web Forms “classic”?  Now we need to get MVC into the WPF platform.  How cool would that be!

- [Previous Entry: NHibernate Query Generator Installer for Visual Studio 2008](/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/)
- [Next Entry: ASP.Net MVC Checkbox/boolean Value Mapping](/2007/12/asp-net-mvc-checkbox-boolean-value-mapping/)

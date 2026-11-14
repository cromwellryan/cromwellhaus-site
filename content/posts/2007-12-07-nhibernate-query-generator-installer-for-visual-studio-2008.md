---
title: "NHibernate Query Generator Installer for Visual Studio 2008"
date: "2007-12-07"
slug: "nhibernate-query-generator-installer-for-visual-studio-2008"
categories: [".Net", "NHibernate"]
tags: [".Net", "NHibernate"]
original_urls: ["http://blog.cromwellhaus.com/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/", "http://blog.cromwellhaus.com:80/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/", "http://blog.cromwellhaus.com:80/index.php/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/", "http://cromwellhaus.com/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/", "http://cromwellhaus.com/blogs/ryanc/archive/2007/12/07/nhibernate-query-generator-installer-for-visual-studio-2008.aspx", "http://cromwellhaus.com:80/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/", "http://cromwellhaus.com:80/blogs/ryanc/archive/2007/12/07/nhibernate-query-generator-installer-for-visual-studio-2008.aspx"]
wayback_source: "https://web.archive.org/web/20091016123049/http://blog.cromwellhaus.com:80/index.php/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/"
excerpt_only: false
permalink: "/2007/12/nhibernate-query-generator-installer-for-visual-studio-2008/"
---

[![image](http://cromwellhaus.com/blogphotos/NHibernateQueryGeneratorInstallerforVisu_14E01/image_thumb_3.png)](http://cromwellhaus.com/blogphotos/NHibernateQueryGeneratorInstallerforVisu_14E01/image_3.png)I [posted recently](/2007/11/nhibernate-query-generator-with-visual-studio-2008/) a manual .reg file for adding the NHibernate Query Generator custom tool to Visual Studio 2008.  I just sent [Ayende](http://ayende.com/) an update to the .Setup Product.wxs, a [WiX](http://sourceforge.net/projects/wix/) file, which adds a new fixture specifically for 2008.

If you are interested in building the installer and running the trunk of NHQG, below is my batch script.  Obviously, you’ll have to change a couple of paths, but it should get you started.

You can download the Product.wxs pending Ayende approving the new Product.wxs file [here](http://cromwellhaus.com/files/folders/nh/entry438.aspx).

> echo Off  
> set path=%path%;c:\\tools\\svn-win32-1.4.4\\bin
>
> echo get Trunk (Non-Recursive)…  
> svn co <https://rhino-tools.svn.sourceforge.net/svnroot/rhino-tools/trunk> trunk -q -N  
> echo done
>
> echo get Art…  
> svn co <https://rhino-tools.svn.sourceforge.net/svnroot/rhino-tools/trunk/Art> trunk/Art -q  
> echo done
>
> echo get SharedLibs…  
> svn co <https://rhino-tools.svn.sourceforge.net/svnroot/rhino-tools/trunk/SharedLibs> trunk/SharedLibs -q  
> echo done
>
> echo get NHQG…  
> svn co <https://rhino-tools.svn.sourceforge.net/svnroot/rhino-tools/trunk/NHibernate.Query.Generator> trunk/NHibernate.Query.Generator -q  
> echo done
>
> echo build NHQG…  
> pushd .  
> cd trunk\\NHibernate.Query.Generator  
> %windir%\\Microsoft.NET\\Framework64\\v2.0.50727\\msbuild.exe default.build   
> echo done
>
> echo build Installer  
> cd NHibernate.Query.Generator.Setup  
> %windir%\\Microsoft.NET\\Framework\\v2.0.50727\\msbuild.exe Setup.wixproj   
> echo done  
> popd  
> PAUSE

- [Previous Entry: NHibernate Query Generator with Visual Studio 2008](/2007/11/nhibernate-query-generator-with-visual-studio-2008/)
- [Next Entry: ASP.Net MVC and Forms Authentication](/2007/12/asp-net-mvc-and-forms-authentication/)

---
title: "Build once, MSDeploy all over the place"
date: "2012-05-02"
slug: "build-once-msdeploy-all-over-the-place"
categories: ["Code", "Uncategorized"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2012/05/build-once-msdeploy-all-over-the-place/", "http://cromwellhaus.com:80/2012/05/build-once-msdeploy-all-over-the-place"]
wayback_source: "https://web.archive.org/web/20120714210258/http://feeds.feedburner.com/RyanCromwell"
excerpt_only: false
permalink: "/2012/05/build-once-msdeploy-all-over-the-place/"
---

There are about 3 dozen ways to automate web app deployment.  All have their candy and their evil.  MSDeploy is one of the more intense tools, but if you don’t collapse at the command line syntax you’ll find it can be pretty sweet.

It’s rather easy to create a basic package, but step beyond the basics and the story isn’t laid out clearly before you.  Many jump on the Config Transform wagon, building 9 versions of their app for each environment they may target.  Transforms look good at first, but then you’re compiling your app 20 times and it just get’s annoying.  I’d much rather build once and specify the parameter transformations at deploy time.  That’s what I’ve got for you today.

Here I’ll walk you through creating custom parameters for deploy time change via MSDeploy.

I’m using an ASP.Net MVC 4 Internet Project, but it’s not critical.

[![image](/images/wp-content/uploads/2012/05/image_thumb.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/05/image.png)

# 

**Environment Specific Settings**

To emulate an environment specific setting, I’ve added appsetting *EnvironmentImIn.*  I’ll commit this with the Get Latest and Go™ value of *LocalDev.*

[![image](/images/wp-content/uploads/2012/05/image_thumb1.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/05/image1.png)[![image](/images/wp-content/uploads/2012/05/image_thumb2.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/05/image2.png)

**Building the Package (Manually)**

Right click the project MVC project and click *Build Deployment Package*.

[![image](/images/wp-content/uploads/2012/05/image_thumb3.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/05/image3.png)

This will create your package as a folder with a series of files under &lt;Project>\\obj\\package.

[![image](/images/wp-content/uploads/2012/05/image_thumb4.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/05/image4.png)

Great, but we don’t deploy from dev machines ‘cause we have a habit of installing crazy stuff.  You should…

**Build the Package (Automation)**

ASP.Net project files, being MSBuild files, have a target called *Package.*  This will first compile the project and then generate the package folder just like VS did above ([Details](http://vishaljoshi.blogspot.com/2009/02/web-packaging-creating-web-packages.html)).  You can adapt this with ease to TFS, TeamCity, etc.[![SNAGHTML46e20cf](/images/wp-content/uploads/2012/05/SNAGHTML46e20cf_thumb.png "SNAGHTML46e20cf")](http://cromwellhaus.com/wp-content/uploads/2012/05/SNAGHTML46e20cf.png)

**Deployment Parameters**

MSDeploy uses a parameters.xml file to determine what is “changeable” at deploy time.  This file is consumed at package creation time.  I consider this a good thing since you end up committing the file and are explicit about what’s changeable.

If you look in the .zip file in your package directory you’ll find a default parameters.xml.  This is because VS/MSBuild makes [certain things changeable by default](http://vishaljoshi.blogspot.com/2010/07/web-deploy-parameterization-in-action.html).  If you drop a parameters.xml file into your project root, MSBuild will use that.  Coolio.  Here’s ours:

[![image](/images/wp-content/uploads/2012/05/image_thumb5.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/05/image5.png)

Vishal Joshi does all the hard work of explaining what the elements all mean [here](http://vishaljoshi.blogspot.com/2010/07/web-deploy-parameterization-in-action.html).  Vishal is the man!  What we’re doing is adding a parameter EnvironmentImIn, giving it a description, and then telling MSDeploy how to find the entry.  Beware, there be regex in them thar hills.

**Changeable Package Settings**

If you build your Deployment Package now (msbuild /t:Package) you’ll find the \*.SetParameters.xml file now contains our *EnvironmentImIn* setting where before it only had IIS Web Application Name and DefaultConnection.  Saweeet!

[![image](/images/wp-content/uploads/2012/05/image_thumb6.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/05/image6.png)

The \*.zip file will also have a parameters.xml file like this:

[![image](/images/wp-content/uploads/2012/05/image_thumb7.png "image")](http://cromwellhaus.com/wp-content/uploads/2012/05/image7.png)

**Deployment (IIS Manager)**

I find many deployment teams like to do their magic manually.  These are often the infrastructure or a Release management group.  They spurn the console at their own peril.  IIS is cool with that though.

You can import packages through IIS Manager and you’ll be presented a UI to change your setting.  #huzzuh!

[![SNAGHTML4c25a19](/images/wp-content/uploads/2012/05/SNAGHTML4c25a19_thumb.png "SNAGHTML4c25a19")](http://cromwellhaus.com/wp-content/uploads/2012/05/SNAGHTML4c25a19.png)

Set it to “Staging” and Finish click Finish results in:

[![SNAGHTML66b5a51](/images/wp-content/uploads/2012/05/SNAGHTML66b5a51_thumb.png "SNAGHTML66b5a51")](http://cromwellhaus.com/wp-content/uploads/2012/05/SNAGHTML66b5a51.png)

**Deployment (Command line)**

One of the convenient pieces created for you by msbuild /t:Package is the *MSDeploySample.deploy.cmd* file.  It helps parse parameters and construct the not so straight forward msdeploy.exe command line.

If you don’t want to mess with msdeploy.exe directly, you can customize the SetParameters.xml file and just run the cmd file like this:

> MSDeploySample.deploy.cmd [/T|/Y]

/T means tell me what’s gonna happen, but don’ t actually do anything yet.

/Y is for the big kids.  Applies the changes.

The alternative is to supply –setParam like this

> –setParam:EnvironmentImIn=Staging

Easiest way to construct an MSDeploy.exe command line is to use the .cmd and modify what it gives you.  Look [here](http://technet.microsoft.com/en-us/library/dd569084(WS.10).aspx#BKMK_ParameterKindSettings) for detailed –setParam options.

---
title: "Visitor Pattern with Anonymous Methods"
date: "2008-07-02"
slug: "visitor-pattern-with-anonymous-methods"
categories: [".Net"]
tags: [".Net"]
original_urls: ["http://blog.cromwellhaus.com/2008/07/visitor-pattern-with-anonymous-methods/", "http://blog.cromwellhaus.com:80/index.php/2008/07/visitor-pattern-with-anonymous-methods/", "http://cromwellhaus.com/blogs/ryanc/archive/2008/07/02/visitor-pattern-with-anonymous-methods.aspx", "http://cromwellhaus.com:80/blogs/ryanc/archive/2008/07/02/visitor-pattern-with-anonymous-methods.aspx"]
wayback_source: "https://web.archive.org/web/20100803184517/http://blog.cromwellhaus.com:80/index.php/2008/07/visitor-pattern-with-anonymous-methods/"
excerpt_only: false
permalink: "/2008/07/visitor-pattern-with-anonymous-methods/"
---

I don’t often have the need to implement the [Visitor Pattern](http://www.dofactory.com/Patterns/PatternVisitor.aspx), but today I was that day.  I looked around really quick for an example of how to do this with [Lambda Expressions](http://msdn.microsoft.com/en-us/library/bb397687.aspx) and [Anonymous Methods](http://msdn.microsoft.com/en-us/library/0yw3tz5k.aspx), which seemed like they were the way to go.  It may be that my search skills have deteriorated right along with my sense of style, but I didn’t find much.

I played around for a few minutes and here is what I came up with:

> ```
> public abstract class CarBase
> {
>     public void Visit(Action<CarBase> action)
>     {
>         if (action != null)
>             action(this);
>     }
> }
>
> public class BigCar : CarBase
> {
>     public void RunOverLittleCar()
>     {
>         Console.WriteLine("Me smash little car!");
>     }
> }
>
> public class LittleCar : CarBase
> {
>     public virtual void RunAwayFromBigCar()
>     {
>         Console.WriteLine("Go Faster!");
>     }
> }
>
> public class EcoCar : LittleCar
> {
>     public override void RunAwayFromBigCar()
>     {
>         Console.WriteLine("Ouch.");
>     }
> }
> ```
>
> ```
> class Program
> {
>     static void Main(string[] args)
>     {
>         IList<CarBase> cars = new List<CarBase>(new CarBase[] {
>                                                                 new BigCar(),
>                                                                 new LittleCar(),
>                                                                 new EcoCar()
>                                                               });
>         foreach (CarBase car in cars)
>         {
>             car.Visit(delegate(CarBase c)
>             {
>                 if (c is BigCar)
>                     ((BigCar)c).RunOverLittleCar();
>                 else if (c is LittleCar)
>                     ((LittleCar)c).RunAwayFromBigCar();
>                 else if (c is EcoCar)
>                     ((EcoCar)c).RunAwayFromBigCar();
>             });
>         }
>
>         if (Debugger.IsAttached)
>             Console.ReadLine();
>     }
> }
> ```

In many implementations of the visitor pattern there is an adapter or actual Visitor interface and implementation class which is passed into the Visit() method.  This is just smooth.

My visit method above is a little big to look good as a lambda expression, though maybe I just don’t have the eye for it.

- [Previous Entry: Virtual Property C# Code Snippet](/2008/07/virtual-property-c-code-snippet/)
- [Next Entry: Why WPF? This is why…](/2008/07/why-wpf-this-is-why/)

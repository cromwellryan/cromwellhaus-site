---
title: "Strategy Pattern with Castle Windsor"
date: "2009-10-30"
slug: "strategy-pattern-with-castle-windsor"
categories: [".Net", "IoC", "Windsor"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2009/10/strategy-pattern-with-castle-windsor/", "http://blog.cromwellhaus.com/index.php/2009/10/strategy-pattern-with-castle-windsor/", "http://blog.cromwellhaus.com:80/2009/10/strategy-pattern-with-castle-windsor/", "http://blog.cromwellhaus.com:80/index.php/2009/10/strategy-pattern-with-castle-windsor", "http://cromwellhaus.com/2009/10/strategy-pattern-with-castle-windsor/", "http://cromwellhaus.com:80/2009/10/strategy-pattern-with-castle-windsor/"]
wayback_source: "https://web.archive.org/web/20100308090731/http://blog.cromwellhaus.com:80/index.php/2009/10/strategy-pattern-with-castle-windsor"
excerpt_only: false
permalink: "/2009/10/strategy-pattern-with-castle-windsor/"
---

One of the tangent patterns associated with isolation or [Single Responsibility](http://en.wikipedia.org/wiki/Single_responsibility_principle) is the [Strategy Pattern](http://en.wikipedia.org/wiki/Strategy_pattern).  I use [Castle Windsor](http://www.castleproject.org/container/index.html) as my [IoC](http://en.wikipedia.org/wiki/Inversion_of_control) of choice and I had hoped there was some black magic built in to make the Strategy Pattern dead simple.  Turns out there is and there isn’t.

**What is the Strategy Pattern**

The strategy pattern is a way of isolating what would often be found in a case statement.  The bland example being calculating Sales tax on an Order.  Each state and/or country has its own tax calculation and rather than

```
   1: public void Process(Order order) {
```

```
   2:     switch(order.Country) {
```

```
   3:         case "USA":
```

```
   4:             order.Total = order.Subtotal * .07;
```

```
   5:             break;
```

```
   6:         case "Canada":
```

```
   7:             order.Total = order.Subtotal * .0985;
```

```
   8:             break;
```

```
   9:     }
```

```
  10: 
```

```
  11:     // ...
```

```
  12: }
```

you should be breaking each calculation out into different ITaxStrategy implementations and consuming them like so:

```
   1: public void Process(Order order) {
```

```
   2:     var strategy = _taxStrategyFactory.GetStrategyForOrder(order);
```

```
   3: 
```

```
   4:     var salesTax = strategy.CalculateSalesTax(order);
```

```
   5: 
```

```
   6:     order.SalesTax = salesTax;
```

```
   7:     order.Total = order.SubTotal + order.SalesTax;
```

```
   8: }
```

The question remains, how to eliminate the conditional logic in TaxStrategyFactory determining *which* strategy is chosen.  The solution is to set up a convention for discovering the available strategies and delegating the criteria to the Strategy itself.

**Discovery**

The concept here is that we don’t have to “hook up” any new Tax Strategy to our Processing mechanism, we just “publish” new ones in a known way and they are picked up simply based on their existence.  This is often referred to as [Convention Over Configuration](http://en.wikipedia.org/wiki/Convention_over_configuration).  We accomplish this with Castle Windsor with the [Fluent Registration API](http://using.castleproject.org/display/IoC/Fluent+Registration+API):

```
   1: container
```

```
   2:     .Register(AllTypes
```

```
   3:                   .FromAssembly(Assembly.GetExecutingAssembly())
```

```
   4:                   .Where(x => x.Name.EndsWith("Strategy"))
```

```
   5:                   .WithService.FirstInterface());
```

This will register all classes found in the executing assembly which have the suffix “Strategy” as implementing the ITaxStrategy interface.  The second half of convention based discovery is consuming the ITaxStrategy implementations.  We can want to get all of these into the TaxStrategyFactory via a constructor array dependency:

```
   1: public TaxStrategyFactory(params ITaxStrategy[] taxStrategies)
```

```
   2: {
```

```
   3:     _taxStrategies = taxStrategies;
```

```
   4: }
```

Unfortunately, Windsor doesn’t support arrays as dependencies by default.  Windsor has the concept of Resolvers (a strategy implementation itself) and we are going to have to tell it about the ArrayResolver which knows how to, err, resolve array dependencies:

```
   1: container
```

```
   2:     .Kernel.Resolver.AddSubResolver(new ArrayResolver(container.Kernel));
```

Cool, so put these all together in our registration code and we get:

```
   1: container
```

```
   2:     .Register(Component
```

```
   3:                   .For<IOrderProcessor>()
```

```
   4:                   .ImplementedBy<OrderProcessor>())
```

```
   5:     .Register(Component
```

```
   6:                   .For<ITaxStrategyFactory>()
```

```
   7:                   .ImplementedBy<TaxStrategyFactory>())
```

```
   8:     .Register(AllTypes
```

```
   9:                   .FromAssembly(Assembly.GetExecutingAssembly())
```

```
  10:                   .Where(x => x.Name.EndsWith("Strategy"))
```

```
  11:                   .WithService.FirstInterface());
```

At this point we can kick of the true discovery chain of events through:

```
   1: var processor = container.Resolve<IOrderProcessor>();
```

```
   2: 
```

```
   3: processor.Process(order);
```

**Delegating Criteria**

So in OrderProcessor.Process we are asked the TaxStrategyFactory for the applicable ITaxStrategy implementation:

```
   1: var strategy = _taxStrategyFactory.GetStrategyForOrder(order);
```

```
   2: 
```

```
   3: var salesTax = strategy.CalculateSalesTax(order);
```

```
   4: 
```

```
   5: //...
```

  The question is, how did the factory determine which of the boundless implementations applies?  That’s the job of each ITaxStrategy itself.  Here’s the implementation of our factory:

```
   1: class TaxStrategyFactory : ITaxStrategyFactory
```

```
   2: {
```

```
   3:     private readonly ITaxStrategy[] _taxStrategies;
```

```
   4: 
```

```
   5:     public TaxStrategyFactory(params ITaxStrategy[] taxStrategies)
```

```
   6:     {
```

```
   7:         _taxStrategies = taxStrategies;
```

```
   8:     }
```

```
   9: 
```

```
  10:     public ITaxStrategy GetStrategyForOrder(Order order)
```

```
  11:     {
```

```
  12:         return _taxStrategies.FirstOrDefault(x => x.IsApplicable(order));
```

```
  13:     }
```

```
  14: }
```

Notice how the TaxStrategyFactory depends on all of the ITaxStrategy implementations.  It then uses the ITaxStrategy.IsApplicable(Order) method as criteria for a FirstOrDefault call.  Here’s an example TaxStrategy for any Order with country “USA”:

```
   1: public class USTaxStrategy : ITaxStrategy
```

```
   2:     {
```

```
   3:         private static readonly IDictionary<string, double> TaxRates = new Dictionary<string, double>()
```

```
   4:                                                                    {
```

```
   5:                                                                        {"OH", 7.0},
```

```
   6:                                                                        {"MI", 6.25},
```

```
   7:                                                                    };
```

```
   8:         public double CalculateSalesTax(Order order)
```

```
   9:         {
```

```
  10:             var rate = TaxRates[order.State];
```

```
  11: 
```

```
  12:             return (order.SubTotal * (rate / 100));
```

```
  13:         }
```

```
  14: 
```

```
  15:         public bool IsApplicable(Order order)
```

```
  16:         {
```

```
  17:             return order.Country == "USA";
```

```
  18:         }
```

```
  19:     }
```

 

You can download the sample project that goes along with this [here](http://code.cromwellhaus.com/WindsorStrategySample.zip).

- [Previous Entry: Dog Food II Registration Open](/2009/10/dog-food-ii-registration-open/)
- [Next Entry: Dog Food II: Implementing Scrum with TFS](/2009/11/dog-food-ii-implementing-scrum-with-tfs/)

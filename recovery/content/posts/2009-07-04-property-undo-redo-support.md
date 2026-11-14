---
title: "Property Undo/Redo Support"
date: "2009-07-04"
slug: "property-undo-redo-support"
categories: [".Net", "Code", "WPF"]
tags: []
original_urls: ["http://blog.cromwellhaus.com/2009/07/property-undo-redo-support/", "http://blog.cromwellhaus.com/index.php/2009/07/property-undo-redo-support/", "http://cromwellhaus.com/blogs/ryanc/archive/2009/07/04/property-undo-redo-support.aspx"]
wayback_source: "https://web.archive.org/web/20090901203829/http://feeds.feedburner.com:80/RyanCromwell"
excerpt_only: false
permalink: "/2009/07/property-undo-redo-support/"
---

Undo/Redo support is one of those golden features that really differentiate a client app from many web apps.  There have been a number of methods/techniques to provide this support that I’ve run across from brute force, to the [memento pattern](http://www.codeproject.com/KB/cs/generic_undo_redo.aspx), but none that lit any fire for me.

Here’s my answer to the problem using Anonymous methods and my first real attempt at creating (versus using) a Fluent Api.

The most common scenario for Undo/Redu support is form completion.  In your Domain or View Model this is often tied to Two Way bound properties.  Take the simple Person class:

```csharp
public class Person
{
    public string Name { get; set; }
    public DateTime BirthDate { get; set; }
}
```

The question is how to provide undo/redo support for a form (WPF often in my case) bound to a Person.  First, I create a ViewModel or Presenter for the Person class:

```csharp
public class PersonViewModel : ViewModelBase
{
    private readonly Person _person;
    public PersonViewModel(Person person)
    {
        _person = person;
    }
    public string Name
    {
        get { return _person.Name; }
        set
        {
            _person.Name = value;
            OnPropertyChanged("Name");
        }
    }
    public DateTime BirthDate
    {
        get { return _person.BirthDate; }
        set
        {
            _person.BirthDate = value;
            OnPropertyChanged("BirthDate");
            OnPropertyChanged("Age");
        }
    }
    public int Age
    {
        get
        {
            var now = DateTime.Now;
            var age = now.Year - _person.BirthDate.Year;
            if (now < _person.BirthDate.AddYears(age))
                age--;
            return age;
        }
    }
}
```

Notice that we have a calculated property Age based on the BirthDate.  Any time we change BirthDate we want to make sure to notify that the Age is also changed, obviously.

Here is the Fluent way to register Undo/Redo support for our PersonViewModel.Name property:

```csharp
 1: public string Name
 2: {
 3:     get { return _person.Name; }
 4:     set
 5:     {
 6:         var oldName = _person.Name;
 7:
 8:         _undoRedoManager
 9:             .WithUndo(() => _person.Name = oldName)
10:             .RepeatAfterBoth(() => OnPropertyChanged("Name"))
11:             .Do(() => _person.Name = value);
12:     }
13: }
```

Cool, but what is that doing?  Well, it’s pretty simply.  We are simply maintaining two queues; An Undo and a Redo queue.  Here is the longer syntax, without the Fluent helper Api that makes that a little clearer:

```csharp
public string Name
{
    get { return _person.Name; }
    set
    {
        var oldName = _person.Name;
        _undoRedoManager.Push(() =>
                                  {
                                      _person.Name = oldName;
                                      OnPropertyChanged("Name");
                                  },
                                  () =>
                                  {
                                      _person.Name = value;
                                      OnPropertyChanged("Name");
                                  });
    }
}
```

This may not seem like much more, but if your Repeat part is more than one line, it gets a bit fragile.  Being able to specify the “After” stuff once is important.

From here you can use the IUndoRedoManager.CanUndo(), IUndoRedoManager.CanRedo(), IUndoRedoManager.Redo() methods to go back and forth.  Hook this up to your favorite ICommand implementation and you have most of what you might need.

[Here is the full project](http://code.cromwellhaus.com/cromwell.undoredo.zip) with a WPF Sample and a VB sample.  The VB version is a little ugly since it doesn’t support anonymous methods without a return, but it works.

If you have suggestions (on the Fluent Api especially) let me know.  I’d really like to hear them.

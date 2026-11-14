---
title: "Elixir needs at least 4 JSON parsers"
date: "2013-08-27"
slug: "elixir-needs-at-least-4-json-parsers"
categories: ["Code", "elixir"]
tags: ["Code"]
original_urls: ["http://cromwellhaus.com/2013/08/elixir-needs-at-least-4-json-parsers/", "https://cromwellhaus.com/2013/08/elixir-needs-at-least-4-json-parsers/"]
wayback_source: "https://web.archive.org/web/20130828002658/http://cromwellhaus.com/feed/"
excerpt_only: false
permalink: "/2013/08/elixir-needs-at-least-4-json-parsers/"
---

Elixir has, at the time of this post, 3 JSON parsers hosted on [expm](http://expm.co/?q=json "JSON libs on expm.io").

Some time back I went looking for one and started exploring [elixir-json](http://expm.co/json "elixir-json"), including the [github repo](https://github.com/cblage/elixir-json "elixir-json code").  I loved how the [encoder](https://github.com/cblage/elixir-json/blob/master/lib/json/encode.ex "elixir-json encoder") used [protocols](http://elixir-lang.org/getting_started/4.html "elixir procotols") to implement the encoding of different types.  It’s beautiful.  Kudos to [@carloslage](https://twitter.com/carloslage "carloslage on twitter").

Then I looked at the [decoder](https://github.com/cblage/elixir-json/blob/master/lib/json/decode.ex "elixir-lang decoder").  It’s full of elixir-isms… tuples, binary pattern matching, etc.  Over the last few nights I decided to implement [my own JSON parser](https://gist.github.com/cromwellryan/6349503 "json parser in elixir gist") learning from Carlos were I ran aground.

I don’t like the use of HashDict for objects, but spaces rule out most options like Keyword lists.  I’m also not a huge fan of the nested case for dealing with the *what’s next?* of key/value pairs.

```
def parse_object( acc, << rest :: binary >> ) do
  { key, rest } = parse_content rest
  { value, rest } = lstrip(rest) |> parse_object_value 

  acc = [ { key, value } | acc ] 

  case lstrip(rest) do
    << ?}, rest :: binary >> -> { HashDict.new(acc), rest }
    << ?,, rest :: binary >> -> parse_object acc, lstrip(rest)
  end
end
```

Overall it feels very cohesive.  You can see clearly how the pieces compose after being dispatched from the parse\_content.

```
def parse_content( << m, rest :: binary >> ) when m in ?0..?9, do: parse_number << m, rest :: binary >>
def parse_content( << ?", rest :: binary >> ), do: rest |> parse_string
def parse_content( << ?{, rest :: binary >> ), do: lstrip(rest) |> parse_object
def parse_content( << ?[, rest :: binary >> ), do: lstrip(rest) |> parse_array
```

I also do nothing to support invalid JSON content as with elixir-json.  Oh well, it was a learning tool.

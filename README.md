# ![Spitfire][]

[![Version][]](https://badge.fury.io/py/spitfire)
[![Status][]](https://travis-ci.org/youtube/spitfire)


## Introduction

Spitfire is a high-performance Python template language inspired
by [Cheetah][].  It originally started out as an experiment to
see if techniques used in compilers were applicable to
templates.  Spitfire has been the primary template language for
[youtube.com][] since 2008 and is used to generate
[billions of views a day][].

This particular fork is made so that Spitfire can work with Python 3.


## Example

```html
<html>
<head><title>$title</title></head>
<body>
  <ul>
    #for $user in $users
      <li><a href="$user.url">$user.name</a></li>
    #end for
  </ul>
</body>
</html>
```


## Getting Started

Spitfire's syntax is extremely similar to Cheetah, however some
directives and language features have been omitted.  If you're
already using Cheetah, simple templates will likely compile in
Spitfire, and there are a couple compatibility modes to ease
transition.


## Performance

Spitfire has a basic optimizer that can make certain operations
much faster.  Using a basic 10x1000 table generation benchmark,
Spitfire can be faster than other template systems and compares
very favorably to hand-coded Python (the upper limit of
performance achievable by compiling to Python bytecode).
This is by no means exhaustive proof that Spitfire is always
fast, just that it can provide very high performance.

```
# Python 3.10.9 (main, Dec 19 2022, 17:35:49) [GCC 12.2.0] on linux
$ python tests/benchmarks/render_benchmark.py
Running benchmarks 1000 times each...

Genshi tag builder                            646.05 ms
Genshi template                               226.59 ms
Genshi template + tag builder                 448.92 ms
Mako Template                                  58.38 ms
Spitfire template                              33.79 ms
Spitfire template -O1                          20.66 ms
Spitfire template -O2                          12.94 ms
Spitfire template -O3                           8.19 ms
StringIO                                        7.95 ms
cStringIO                                       9.73 ms
list concat                                     7.32 ms
Jinja2 templates                               15.84 ms

```


[Cheetah]: http://www.cheetahtemplate.org/
[youtube.com]: https://www.youtube.com/
[billions of views a day]: https://www.youtube.com/yt/press/statistics.html

[Spitfire]: https://raw.githubusercontent.com/youtube/spitfire/master/doc/spitfire.png
[Version]: https://badge.fury.io/py/spitfire.svg
[Status]: https://secure.travis-ci.org/youtube/spitfire.svg?branch=master

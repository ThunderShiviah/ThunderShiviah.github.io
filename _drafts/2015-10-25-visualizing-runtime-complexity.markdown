---
layout: post
title:  "Visualizing Runtime Complexity in python"
date:   2015-10-25 23:01:57
categories: python functional_programming  
---

A few months ago I gave a talk at a local code school called *How to think like
a computer scientist (I am not a computer scientist)*. The goal of the talk was
to expose the code school students to some CS theory (like time complexity and sorting) they might not have heard
about given that their curriculum was very hands-on. 

One of the core concepts of my talk was understanding how big O notation
connects to the physical runtime of an algorithm on a computer. To demonstrate
the relationship I decided to write a function that would take in a sorting or
searching algorithm and graph the runtime of the algorithm on random lists of
various sizes. You can view the slides from my talk as well as the runtime
visualization function on github (TODO: ADD LINK). A few days ago, I decided to implement a less
hacky version of my runtime visualizer as a small python library. This post
outlines some of the technical challenges to generalizing my runtime visualizer
(rtviz from here on) as well as my attempts at fixing and speeding up rtviz
performance using concurrency and functional programming concepts. You can
visit the current draft of the rtviz lib on my github (TODO: ADD LINK).

My first step in writing my library was to spend some time thinking about what
I actually wanted rtviz to accomplish, or somewhat equivalently: what are the
inputs and ouputs? In this case, my input was a function that would act on an
iterable as well as other function parameters. The output would include a graph
that plotted runtime of the function on a list of random numbers against the
length of the list. The idea would be that if I gathered the runtime of the
function on lists of increasing length, the algorithmic time complexity (such
as linear, logarithmic, or quadratic time) would be plotted.

```
def rtviz(func, *args):
    """Takes in a function that receives an iterable as input.
    Returns a plot of the runtimes over iterables of random integers of increasing length.
    
    func: a function that acts on an iterable"""
    pass
```


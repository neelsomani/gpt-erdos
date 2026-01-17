This is **still open**.

Here is the clean way to say it.

### What “avoid a monotone 3‑term A.P.” means

Take a set (A\subseteq\mathbb N).
Saying “$A$ can be permuted to avoid monotone 3‑term arithmetic progressions” means:

There is an ordering (a_1,a_2,a_3,\dots) of all elements of $A$ such that **no** triple
[
a_i,\ a_j,\ a_k \quad (i<j<k)
]
forms a 3‑term arithmetic progression (so (a_j-a_i=a_k-a_j)).
For distinct integers, such a triple is automatically increasing or decreasing, so “monotone” is just stressing that we look at increasing or decreasing A.P.’s. 

Call such a set **3‑free** (this is standard in this topic). 

### Why this is not trivial

You **cannot** do it with one set, because (\mathbb N) itself is **not** 3‑free:

If (a_1,a_2,\dots) is any permutation of the positive integers, let (a_1) be the first term, and let (a_k) be the first later term that is bigger than (a_1). Then the number
[
2a_k-a_1
]
is a positive integer, so it appears somewhere to the right. Thus (a_1,a_k,2a_k-a_1) is an increasing 3‑term arithmetic progression as a subsequence. 

So splitting (\mathbb N) into pieces really matters.

### What is known about the partition question

Erdős (with Graham) asked exactly your question:

> Can (\mathbb N) be partitioned into **two** sets, each of which is 3‑free?

This is **open** as of now. ([Erdős Problems][1])

What *is* known:

* If you allow **three** sets, then a partition is possible. ([Erdős Problems][1])

### Extra context (why people think about density)

People also ask how “large” a 3‑free set can be (in density terms). For example, there are 3‑free sets with **upper density at least $1/2$**, and examples with **lower density at least $1/4$**. 
But this is not strong enough (yet) to settle the 2‑set partition question.

So the best honest answer is:

**We do not know whether (\mathbb N) can be split into two such sets; it remains an open Erdős–Graham problem.** ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/197 "
  
    Erdős Problem #197
  
"

With the hypothesis as stated **for arbitrary real** (a_i>1), this is (as far as is currently recorded in the literature) **open**.

* Your condition says that the “generalized integers”
  [
  \mathcal N:=\\{\prod_i a_i^{k_i}:\ k_i\in\mathbb Z_{\ge 0}\text{ finitely supported}\\}
  ]
  form a **$1$-separated** subset of (\mathbb R_{>0}): any two distinct elements differ by at least $1$. In the language of Beurling’s generalized number systems, the (a_i) play the role of **generalized primes**, and the products (\mathcal N) are the generalized integers. ([Erdős Problems][1])

* The specific question
  [
  |\\{a_i\le x\\}|\stackrel{?}{\le}\pi(x)
  ]
  is listed as **Erdős Problem #951** and is marked **OPEN** (and attributed to a question asked during an Erdős lecture, possibly by S. Shapiro). ([Erdős Problems][1])

* The same source notes a related (stronger) “rigidity” conjecture of Beurling: if the generalized integers satisfy a near-maximal counting condition ( |\\{n\in\mathcal N:n\le x\\}|=x+o(\log x)), then the generalized primes should actually be the usual primes. ([Erdős Problems][1])
  That conjecture is different in flavor (it assumes the generalized integers are essentially as dense as the ordinary integers), but it’s in the same circle of ideas.

### Easy consequences of your separation condition

A couple of quick observations that always hold:

1. Taking one tuple to be all zeros gives (|a_i-1|\ge 1), hence (a_1\ge 2).
2. Comparing the tuples with a single $1$ at $i$ vs a single $1$ at $j$ gives (|a_i-a_j|\ge 1). So the (a_i) are $1$-separated as an increasing sequence, and in particular
   [
   a_n \ge n+1,\qquad |\\{a_i\le x\\}|\le \lfloor x\rfloor-1.
   ]
   [[nomath]](This is much weaker than $\pi(x)$, of course.)[[/nomath]]

### In one important special case, the inequality *is* true

If you additionally assume the (a_i) are **integers**, then the bound (|\\{a_i\le x\\}|\le \pi(x)) is true, for a simple “rank” reason:

* Write each integer (a_i\le x) as a prime-exponent vector in (\mathbb Z^{\pi(x)}) using the primes (\le x).
* Your “no two distinct tuples give the same product” condition is exactly the statement that these exponent vectors are **(\mathbb Z)-linearly independent**.
* But (\mathbb Z^{\pi(x)}) has rank (\pi(x)), so you can’t have more than (\pi(x)) independent vectors. Hence (|\\{a_i\le x\\}|\le \pi(x)).

This doesn’t resolve the real-number case, because the “prime exponent vector” argument disappears once you leave (\mathbb N).

---

So, for the problem as you posed it over (\mathbb R): **it is not currently known whether the inequality holds**; it’s a recorded open Erdős problem in the framework of Beurling generalized primes. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/search_bib/Er77c?sources_only=1 "
  
    Erdős Problems
  
"

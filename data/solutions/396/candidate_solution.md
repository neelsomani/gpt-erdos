This is **open** (as far as the current literature indicates).

It appears as **Erdős Problem #396** (Erdős–Graham), asking exactly whether for every $k$ there exists an $n$ such that
[
\prod_{i=0}^{k}(n-i)\ \bigg|\ \binom{2n}{n}.
]
The Erdős Problems database lists it as **OPEN**. ([Erdős Problems][1])

### What is known

* There are strong **partial results for single factors**: for any fixed (k\ge 0), Pomerance showed there are **infinitely many** $n$ with
  [
  n-k \mid \binom{2n}{n},
  ]
  and even gives a quantitative lower bound on how many such (n\le x) exist. 
  [[nomath]](But this is much weaker than requiring the whole product $n(n-1)\cdots(n-k)$ to divide.)[[/nomath]]

* Pomerance also showed that the **“forward” product** (\prod_{1\le i\le k}(n+i)) divides (\binom{2n}{n}) for “almost all” $n$ [[nomath]](density $1$)[[/nomath]], again highlighting that the “backward” product in your question is the hard direction. ([Erdős Problems][1])

### Computational evidence

For each $k$ up to at least $7$, explicit $n$ are known by computation. The OEIS sequence **A375077** records the **smallest** such $n$ (with their indexing shift). The first values correspond to:

* $k=1$: $n=2$
* $k=2$: $n=2480$
* $k=3$: $n=8178$
* $k=4$: $n=45153$
* $k=5$: $n=3648841$
* $k=6$: $n=7979090$
* $k=7$: $n=101130029$

(these are listed on OEIS A375077). ([OEIS][2])

So the statement is **true for many small $k$ by explicit examples**, but **no general proof** (and no counterexample) is currently known. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/396 "
  
    Erdős Problem #396
  
"
[2]: https://oeis.org/A375077 "A375077 - OEIS"

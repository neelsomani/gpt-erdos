Let
[
m=\lfloor cn\rfloor,\qquad [m]:={1,2,\dots,m},
]
and write (\Sigma(A)={\sum_{a\in B}a: B\subseteq A}) for the set of subset–sums.
We want
[
F_c(n):=\max{|A|:A\subseteq [m],\ n\notin \Sigma(A)}.
]

## The case (c\ge 1) is completely solved

### Claim

If (c\ge 1) [[nomath]](so $m\ge n$)[[/nomath]], then
[
F_c(n)=m-\left\lceil\frac n2\right\rceil.
]

### Construction (lower bound)

Take
[
A={\lceil n/2\rceil,\lceil n/2\rceil+1,\dots,n-1}\ \cup\ {n+1,n+2,\dots,m}.
]

* Any subset using an element (>n) has sum (>n).
* Any subset using only ({\lceil n/2\rceil,\dots,n-1}) either has one element [[nomath]](hence $<n$)[[/nomath]] or has at least two elements, in which case the sum is at least
  (\lceil n/2\rceil+(\lceil n/2\rceil+1)>n).
  So (n\notin\Sigma(A)). Its size is
  [
  |A|=(n-\lceil n/2\rceil)+(m-n)=m-\lceil n/2\rceil.
  ]

### Upper bound

Any valid (A\subseteq [m]) must:

* exclude $n$ [[nomath]](otherwise ${n}$ sums to $n$)[[/nomath]];
* from each complementary pair ({x,n-x}) with (1\le x\le n-1), include at most one element, otherwise ({x,n-x}) sums to $n$.

Counting the maximum you can take from ({1,\dots,n}) under these pair restrictions gives at most (\lfloor n/2\rfloor) elements (\le n). Everything in ({n+1,\dots,m}) is “free” [[nomath]](can’t be used to sum to $n$)[[/nomath]]. Hence
[
|A|\le (m-n)+\left\lfloor\frac n2\right\rfloor
=m-\left\lceil\frac n2\right\rceil.
]

So for (c\ge 1),
[
F_c(n)=\lfloor cn\rfloor-\left\lceil\frac n2\right\rceil
=(c-\tfrac12)n+O(1),
]
and the dependence on $n$ is only the trivial parity/rounding effect.

## The case (c<1) is open in general, and *does* show irregular dependence on $n$

This is an Erdős–Graham open problem (Erdős Problem #361). ([Erdős Problems][1])
There is no known complete formula for (F_c(n)) for fixed (c<1).

What is known (or at least widely discussed) is a menu of **general constructions** (lower bounds) and some general **upper bounds**, and these already show why (F_c(n)) can vary “irregularly” with $n$.

### Evidence of irregularity

For (c=3/4), computations for (100\le n\le 104) give maximum sizes
[
34,,37,,32,,38,,35,
]
which certainly is not a smooth function of $n$. ([Erdős Problems][1])

### Why irregularity is plausible: “modular obstruction” constructions

A very robust way to guarantee (n\notin\Sigma(A)) is to force all subset sums to lie in a congruence class that avoids $n$.

* If $p$ is a prime not dividing $n$, then taking
  [
  A={x\le m: p\mid x}
  ]
  works, because every subset sum is divisible by $p$, hence cannot equal $n$. This gives
  [
  |A|=\left\lfloor\frac mp\right\rfloor.
  ]
  This already depends on $n$ through the smallest prime (or prime power) not dividing $n$. ([Erdős Problems][1])

* When (c>1/2), one can often do better by adding some **large** numbers in a residue class mod $p$ that still can’t combine to hit $n$ [[nomath]](because you can’t use two large numbers without overshooting $n$)[[/nomath]]. Variants of this idea are discussed in the same problem thread, and they explain the observed behavior for (c=3/4). ([Erdős Problems][1])

These constructions naturally jump around with the prime factorization of $n$, so fluctuations are expected.

### A different “size obstruction” construction [[nomath]](works especially when $c>1/2$)[[/nomath]]

Another general trick is: include a big tail $[ \lceil n/2\rceil, m]$ and then add a small initial segment $[1,k]$ chosen so that even with the largest element $m$ you still can’t reach $n$.
A typical sufficient condition is
[
1+2+\cdots+k+m < n,
]
i.e.
[
\binom{k+1}{2}<n-m.
]
Then any subset sum using an element (\ge n/2) can use at most one such element, and the remaining part is too small to complement it to exactly $n$. This kind of construction gives
[
|A| = (m-\lceil n/2\rceil+1)+k
= (c-\tfrac12)n + O(\sqrt n)
]
in favorable cases, and is also mentioned as a candidate extremal shape in some regimes. ([Erdős Problems][1])

### What is currently known as “the answer” for (c<1)

As of the discussion summarized on the Erdős Problems page, **there is no settled asymptotic formula** for general fixed (c<1), and the best construction can depend both on $c$ and on arithmetic properties of $n$ [[nomath]](e.g., which small primes divide $n$)[[/nomath]]. ([Erdős Problems][1])

## Summary

* **If (c\ge 1)**:
  [
  F_c(n)=\lfloor cn\rfloor-\left\lceil\frac n2\right\rceil
  =(c-\tfrac12)n+O(1),
  ]
  and the dependence on $n$ is regular (just rounding/parity).

* **If (c<1)**: there is **no general closed form known** (open Erdős–Graham problem). There is strong evidence that (F_c(n)) can vary **irregularly** with $n$, and this is already visible in computed values for (c=3/4). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/361 "

    Erdős Problem #361 - Discussion thread

"

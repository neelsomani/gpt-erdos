A quick sanity check first: if repetitions of elements were allowed in the sums, the problem would be essentially trivial [[nomath]](two distinct positive integers $x<y\in B$ would give $\underbrace{x+\cdots+x}\*{y/g}=\underbrace{y+\cdots+y}\*{x/g}$ with $g=\gcd(x,y)$ and different lengths)[[/nomath]]. So the intended interpretation (as in Erdős–Straus/Choi) is that the sums are **subset sums** (each element used at most once), i.e. you are forbidding equal sums coming from subsets of *different cardinalities*.

With that understood, the best-known bounds are:

[
c,(n\log n)^{1/3}\ \le\ h(n)\ \le\ C,n^{1/2}
\qquad (n\to\infty)
]

for absolute constants (c,C>0). ([Erdős Problems][1])

## What is known (and what this means as an “estimate”)

* **Upper bound (h(n)\ll n^{1/2})** [[nomath]](Straus, improving an earlier $n^{5/6}$ bound of Erdős)[[/nomath]]: there exist $n$-element sets (A\subset\mathbb Z) for which *no* subset (B\subseteq A) with the property can have size larger than a constant times (\sqrt n). ([Erdős Problems][1])

  In fact, taking (A={1,2,\dots,n}), the extremal problem of the largest (B\subseteq {1,\dots,n}) whose $r$-term subset-sum sets are pairwise disjoint has been solved asymptotically: the maximum size is ((2+o(1))\sqrt n). This immediately implies
  [
  h(n)\le (2+o(1))\sqrt n
  ]
  by choosing this particular $A$. ([Erdős Problems][2])

* **Lower bound (h(n)\gg (n\log n)^{1/3})** [[nomath]](Erdős gave $n^{1/3}$, improved by Erdős & Choi to $(n\log n)^{1/3}$)[[/nomath]]: for *every* (A\subset\mathbb Z) with (|A|=n), you can always find a (B\subseteq A) of size at least (c(n\log n)^{1/3}) with the required “no equal sums with different numbers of terms” property. ([Erdős Problems][1])

  The idea (very roughly) is probabilistic: pick a random (\alpha\in[0,1]) and keep those (a\in A) for which the fractional part ({\alpha a}) lies in a carefully chosen tiny interval. Then the fractional part of (\alpha) times a subset sum of size $r$ is forced into a short interval depending on $r$; by making those intervals essentially disjoint for different $r$, you rule out equal sums coming from different subset sizes. Erdős’ original choice gives (\gg n^{1/3}), and Choi’s refinement yields the extra ((\log n)^{1/3}). ([Erdős Problems][1])

## Current “best estimate”

So, in asymptotic order-of-growth terms, the known estimate is

[
(n\log n)^{1/3}\ \lesssim\ h(n)\ \lesssim\ n^{1/2}.
]

Closing the exponent gap between $1/3$ and $1/2$ (even up to logs) is the hard part and, as far as I can tell from the standard references, still open. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/789 "https://www.erdosproblems.com/latex/789"
[2]: https://www.erdosproblems.com/874 "
  
    Erdős Problem #874
  
"

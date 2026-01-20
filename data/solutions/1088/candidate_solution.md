Write (f_d(n)) for the least $m$ such that **every** $m$-point set (P\subset \mathbb R^d) contains an $n$-point subset (Q\subset P) with **all** (\binom n2) pairwise distances in $Q$ distinct [[nomath]](a “no–repeated-distance” $n$-set)[[/nomath]]. This is exactly the parameter Erdős denoted $J(n;d)$. ([Springer][1])

## What is known

### 1) Fixed dimension $d$, (n\to\infty)

Erdős observed already in 1975 that for each fixed $d$ one has a polynomial bound
[
f_d(n)\le n^{c_d}
]
for some exponent (c_d) depending on $d$ [[nomath]](he writes “$J(n;k) < n^{c_k}$”)[[/nomath]]. ([Springer][1])
So for fixed $d$, the growth in $n$ is at most polynomial [[nomath]](though the best exponent $c_d$ is not determined in general)[[/nomath]].

### 2) Fixed $n$, (d\to\infty): the Erdős–Straus exponential upper bound and Erdős’s conjecture

Erdős stated that he and Straus proved an unpublished bound of the form
[
f_d(n)\le c_n^{d}
]
for a constant (c_n>0) depending only on $n$. ([Springer][1])

He also explicitly conjectured that for fixed $n$,
[
\lim_{d\to\infty} f_d(n)^{1/d}=1,
]
which is equivalent to your question (f_d(n)=2^{o(d)}). ([Springer][1])

### 3) The case $n=3$ is understood [[nomath]](and answers the subexponential question positively for $n=3$)[[/nomath]]

For $n=3$, “all three distances distinct” just means a *scalene* triple (not necessarily non-collinear).

Let (M_d) be the maximum size of a set (A\subset\mathbb R^d) in which **every** triple is isosceles (i.e., no scalene triple). Then (f_d(3)=M_d+1).

Known bounds (Blokhuis upper bound; Alweiss + Weisenberg lower bounds) give
[
\binom{d+1}{2}+1\ \le\ M_d\ \le\ \binom{d+2}{2},
]
hence
[
\binom{d+1}{2}+2 \ \le\ f_d(3)\ \le\ \binom{d+2}{2}+1,
]
so in particular
[
f_d(3)=\frac{d^2}{2}+O(d).
]
([Erdős Problems][2])
This is polynomial in $d$, hence (f_d(3)=2^{o(d)}) is **true**.

### 4) The one-dimensional case

When $d=1$, the problem becomes the classical “distinct differences”/Golomb ruler phenomenon and one has
[
f_1(n)\asymp n^2.
]
([Erdős Problems][3])

## A general lower bound in high dimension [[nomath]](fixed $n$, $d\to\infty$)[[/nomath]]

A simple (but useful) construction shows (f_d(n)) is **at least polynomial** in $d$ for every fixed (n\ge 3).

Let
[
t:=\binom{n}{2}-1.
]
In (\mathbb R^{d+1}), consider the set
[
P={0,1}^{d+1}\ \text{of vectors with exactly }t\text{ ones}.
]
All these points lie in the affine hyperplane (\sum x_i=t), which is $d$-dimensional, so we may view $P$ as a configuration in (\mathbb R^d).

For two distinct points (x,y\in P), their squared Euclidean distance is
[
|x-y|^2 = | {i: x_i\ne y_i} | = 2(t-|x\cap y|),
]
so (|x-y|^2) can take only the values (2,4,\dots,2t). Thus **the entire set $P$ determines at most $t$ distinct distances**.

But an $n$-point subset with all pairwise distances distinct would require (\binom n2) distinct distances. Since (t=\binom n2-1), this is impossible inside $P$. Therefore $P$ contains **no** “all-distances-distinct” $n$-subset, and hence
[
f_d(n)\ \ge\ |P|+1\ =\ \binom{d+1}{t}+1
\ =\ \binom{d+1}{\binom n2-1}+1.
]
Asymptotically [[nomath]](for fixed $n$ and $d\to\infty$)[[/nomath]],
[
f_d(n)\ \ge\ \frac{d^{\binom n2-1}}{(\binom n2-1)!}(1+o(1)).
]

This matches the $n=3$ lower bound construction cited on the Erdős Problems page [[nomath]](the $e_i+e_j$ example is exactly the $t=2$ case)[[/nomath]]. ([Erdős Problems][2])

## So… is (f_d(n)=2^{o(d)}) true for fixed (n\ge 3)?

* For $n=3$: **yes**, since (f_d(3)=\frac{d^2}{2}+O(d)). ([Erdős Problems][2])
* For (n\ge 4): **still open** as far as the standard references and the Erdős problem list indicate.

  * Best general **lower bound** for fixed $n$: polynomial in $d$, e.g. $\binom{d+1}{\binom n2-1}+1$.
  * Best general **upper bound** recorded in the literature: Erdős–Straus claimed (unpublished) (f_d(n)\le c_n^d), i.e. at most exponential in $d$. ([Springer][1])
  * Erdős explicitly conjectured the stronger subexponential behavior (\lim_{d\to\infty} f_d(n)^{1/d}=1) [[nomath]](equivalently $2^{o(d)}$)[[/nomath]]. ([Springer][1])

So the current state is a large gap for (n\ge 4):
[
\binom{d+1}{\binom n2-1}+1 \ \le\ f_d(n)\ \le\ c_n^{d},
]
and the subexponential question remains unanswered beyond $n=3$.

[1]: https://link.springer.com/content/pdf/10.1007/BF02414146.pdf "https://link.springer.com/content/pdf/10.1007/BF02414146.pdf"
[2]: https://www.erdosproblems.com/latex/503 "
  
    Erdős Problems
  
"
[3]: https://www.erdosproblems.com/latex/1088 "https://www.erdosproblems.com/latex/1088"

Let $G$ be an $n$-vertex graph and write
[
S_G(\triangle)=d_G(u)+d_G(v)+d_G(w)
]
for the degree–sum of a triangle (\triangle=uvw). Then your $h(n)$ is exactly
$
h(n)=\min{\ \max_{\triangle\subseteq G} S_G(\triangle)\ :\ |V(G)|=n,\ e(G)>\tfrac{n^2}{4}\}.
$
[[nomath]](So $h(n)$ is the *best guaranteed* “large degree–sum triangle” once we cross Mantel’s threshold.)[[/nomath]]

## What is known about the size of $h(n)$?

It is known that $h(n)$ is linear in $n$, and the best published general bounds (that I could find) are
[
\Big(\frac{21}{16}-o(1)\Big)n\ \le\ h(n)\ \le\ \big(2(\sqrt3-1)+o(1)\big)n,
]
i.e.
[
1.3125,n\ \lesssim\ h(n)\ \lesssim\ 1.4641,n.
]
The **upper bound** comes from a concrete construction of Erdős–Laskar giving graphs with (e(G)=n^2/4+1) in which *every* triangle has degree–sum at most (\big(2(\sqrt3-1)+o(1)\big)n). ([Erdős Problems][1])
The **lower bound** (h(n)\ge \frac{21}{16}n) is due to Fan (improving an earlier linear lower bound). ([Erdős Problems][1])

So at present the constant factor is pinned down only to the interval ([21/16,\ 2(\sqrt3-1)]).

## Why (2(\sqrt3-1)) appears (the Erdős–Laskar construction)

A clean way to see the upper bound is via the standard “almost bipartite + a few internal edges” extremal example (this is essentially what’s described in the Erdős–Laskar construction, as reproduced in later sources).

Take a parameter (c\in(0,1)) and partition
[
V=A\cup B,\qquad |A|=\frac{1+c}{2}n,\quad |B|=\frac{1-c}{2}n.
]
Put in **all** edges between $A$ and $B$, so (e(A,B)=|A||B|=\frac{1-c^2}{4}n^2).
Now split (A=A_1\cup A_2) evenly, and add
[
\frac{(cn)^2}{4}+1
]
edges between (A_1) and (A_2), distributed “as regularly as possible.” This makes the total number of edges exactly
[
\frac{1-c^2}{4}n^2+\frac{c^2}{4}n^2+1=\frac{n^2}{4}+1,
]
so we are just above the Mantel threshold. 

In this graph, every triangle must use one vertex in each of (A_1,A_2,B). A vertex (b\in B) has
[
d(b)=|A|=\frac{1+c}{2}n.
]
A vertex (a\in A_1) has all (|B|=\frac{1-c}{2}n) neighbors in $B$ plus its neighbors in (A_2). Because the (A_1)–(A_2) edges were distributed nearly regularly, the maximum (A_2)-degree is about
[
\frac{\text{# edges between }A_1,A_2}{|A_1|}\approx
\frac{\frac{c^2}{4}n^2}{\frac{1+c}{4}n}
=\frac{c^2}{1+c},n,
]
up to lower-order terms. Thus every triangle $(a_1,a_2,b)$ has degree–sum at most
[
d(b)+d(a_1)+d(a_2)
\le
\frac{1+c}{2}n
+2\left(\frac{1-c}{2}n+\frac{c^2}{1+c}n\right)
==============================================

\Big(\frac32-\frac c2+\frac{2c^2}{1+c}\Big)n+o(n).
]
This is exactly the expression analyzed in the literature (again, see the “Example 4.4/4.7” discussion in the source I’m citing). 

Now minimize
[
f(c)=\frac32-\frac c2+\frac{2c^2}{1+c}.
]
A quick calculus check gives the minimizer (c=-1+\frac{2}{\sqrt3}), and at that point
[
\min_c f(c)=2(\sqrt3-1).
]
So this produces graphs with (n^2/4+1) edges but with
[
\max_{\triangle} S_G(\triangle)\le (2(\sqrt3-1)+o(1))n,
]
hence
[
h(n)\le (2(\sqrt3-1)+o(1))n.
]
([Erdős Problems][1])

## Is the matching lower bound true?

The statement you wrote,
[
h(n)\ge (2(\sqrt3-1)-o(1))n,
]
is precisely the natural “match the construction” conjecture. As far as I can find, it is **still open**: the best published general lower bound remains (\frac{21}{16}n) (up to lower-order terms), well below (2(\sqrt3-1)n). ([Erdős Problems][1])

## A bit of extra context

If you strengthen the hypothesis to **many more** than (n^2/4) edges, there are stronger guaranteed degree–sum bounds [[nomath]](e.g. for $m\ge n^2/3$, a theorem of Edwards gives a triangle with degree–sum at least $6m/n$)[[/nomath]]. ([Renyi Users][2])
But $h(n)$ is governed by the near-threshold regime (e(G)=n^2/4+O(1)), where the extremal examples are “barely non-bipartite,” and the exact asymptotic constant is what’s unknown.

**Bottom line:** currently,
[
\boxed{\Big(\frac{21}{16}-o(1)\Big)n\ \le\ h(n)\ \le\ \big(2(\sqrt3-1)+o(1)\big)n,}
]
and whether $h(n)$ asymptotically equals (2(\sqrt3-1)n) is (to the best of what I found) **unresolved**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/1033 "
  
    Erdős Problem #1033
  
"
[2]: https://users.renyi.hu/~gyarfas/Cikkek/44_ErdosGyarfasOrdmanZalcstein_TheSizeOfChordalIntervalAndThresholdSubgraphs.pdf "https://users.renyi.hu/~gyarfas/Cikkek/44_ErdosGyarfasOrdmanZalcstein_TheSizeOfChordalIntervalAndThresholdSubgraphs.pdf"

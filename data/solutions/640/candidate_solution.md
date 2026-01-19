This is **open** (at least as of early 2026).

It’s a problem of **Erdős and Hajnal** (often discussed in the “χ-boundedness”/Gyárfás problem ecosystem) and is listed as **Erdős Problem #640**. ([Erdős Problems][1])

## Equivalent reformulation

Let

[
s(G)=\max{\chi(G[V(C)]) : C\text{ is an odd cycle of }G},
]

where (G[V(C)]) is the **induced** subgraph on the vertices of the cycle $C$.

Your question asks whether there is a function $f$ such that
[
\chi(G)\ge f(k)\quad\Longrightarrow\quad s(G)\ge k.
]
Equivalently: **is (\chi(G)) bounded by a function of $s(G)$?**

Moreover, the Erdős-problems discussion notes that this is *equivalent (up to constant-factor/offset changes in the function)* to the “path” version: requiring a **path** $P$ whose vertex set spans an induced subgraph of chromatic number (\ge k). ([Erdős Problems][2])

## What is known (partial results)

### 1) The first nontrivial case is already open

For $k=3$, it’s trivial: (\chi(G)\ge 3) forces an odd cycle, and the induced subgraph on that cycle’s vertices is non-bipartite, hence (\ge 3).

But for $k=4$ (i.e., wanting an odd cycle whose vertices induce a **4-chromatic** subgraph), this is part of what’s still unknown: it connects to Gyárfás’ conjecture about graphs whose **paths** span only 3-colorable induced subgraphs. ([sdu][3])

### 2) Best general upper bounds depend on (|V(G)|), not just $k$

For the path-variant with (r(G)=\max\chi(G[V(P)])) over paths $P$, Randerath–Schiermeyer proved that if $G$ has $n$ vertices then
[
\chi(G)\le 3\left\lceil \log_{8/7}(n)\right\rceil
]
under the hypothesis “every path spans a 3-colorable induced subgraph.” ([Springer][4])

This shows you can’t currently get a purely $k$-dependent bound from the known techniques, even in that special case.

### 3) There are explicit lower-bound constructions [[nomath]](so any $f$ would have to grow)[[/nomath]]

A 2025 paper of Cameron–Clow studies the path parameter $r(G)$ and constructs graphs with
[
r(G)\le r\quad\text{but}\quad \chi(G)\ge \left\lfloor\frac{3r}{2}\right\rfloor-1,
]
so (\chi(G)) can be substantially larger than the maximum chromatic number seen on path-spanned induced subgraphs. ([arXiv][5])

They also prove stronger bounds in restricted graph classes [[nomath]](e.g. claw-free graphs satisfy $\chi(G)\le 2r(G)$)[[/nomath]]. ([arXiv][5])

### 4) An “even cycle” analogue *is* known

Gyárfás proved (using earlier work of Krusenstjerna-Hafström and Toft) that if **every even cycle** spans a **bipartite** induced subgraph, then the whole graph is **3-colorable**—so the even-cycle version behaves much more rigidly. ([sdu][3])

## Bottom line

No such function $f(k)$ is currently known in full generality; the problem remains open for (k\ge 4). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/640?order=oldest "https://www.erdosproblems.com/forum/thread/640?order=oldest"
[2]: https://www.erdosproblems.com/forum/thread/640 "https://www.erdosproblems.com/forum/thread/640"
[3]: https://www.imada.sdu.dk/Research/Graphcol/new_problems.html "https://www.imada.sdu.dk/Research/Graphcol/new_problems.html"
[4]: https://link.springer.com/article/10.1007/BF03322762 "https://link.springer.com/article/10.1007/BF03322762"
[5]: https://arxiv.org/abs/2506.19100 "https://arxiv.org/abs/2506.19100"

What you wrote is **exactly Gallai’s path decomposition conjecture** (1968):

> every connected graph $G$ on $n$ vertices has an edge-partition into at most (\left\lceil \frac n2\right\rceil) (edge-disjoint) paths. ([labri.fr][1])

As far as the current literature indicates, **this conjecture is still open in full generality** (i.e., no general proof or counterexample is known). 

## What *is* known (general best bound)

Let $p(G)$ be the minimum number of paths in a path decomposition of $G$. The best general bound currently known is

[
p(G)\ \le\ \Big\lfloor \frac{2n}{3}\Big\rfloor,
]

proved by Dean–Kouider and independently by Yan (as summarized in recent surveys/papers). 

A more refined version bounds $p(G)$ in terms of the numbers of odd- and even-degree vertices; the resulting worst-case bound in terms of $n$ alone gives the (\lfloor 2n/3\rfloor) type estimate. ([labri.fr][1])

## A closely related theorem that *is* proved

Lovász (1968) proved a weaker but foundational result:

* **every $n$-vertex graph can be decomposed into at most (\lfloor n/2\rfloor) pieces, each piece being a path *or a cycle*.** ([labri.fr][1])

Gallai’s conjecture is essentially asking whether the cycles can always be “eliminated” without increasing the number of parts beyond (\lceil n/2\rceil).

## Why the (\lceil n/2\rceil) target is the right scale (tightness)

Even if the conjecture is true, the bound (\lceil n/2\rceil) cannot generally be improved: for the complete graph (K_n), each path uses at most $n-1$ edges, while (K_n) has (\binom{n}{2}) edges, so any decomposition needs at least
[
\left\lceil \frac{\binom{n}{2}}{n-1} \right\rceil = \left\lceil \frac{n}{2} \right\rceil
]
paths. This matches Gallai’s bound; in particular, it is “sharp” for (K_n) when $n$ is odd. 

## Important special cases where the conjecture *is* known to hold

There are many graph classes for which Gallai’s conjecture has been proved. For example:

* **Planar graphs:** every connected planar graph satisfies Gallai’s conjecture; in fact the planar result is stronger: every connected planar graph except (K_3) and (K_5^-) can be decomposed into (\lfloor n/2\rfloor) paths. ([arXiv][2])
* **Maximum degree (\Delta \le 5):** proved by Bonamy–Perrett. ([arXiv][3])
* **Block graphs:** proved in 2025. ([AIMS Press][4])

(There are several more families listed in the planar-graphs slide deck and related papers—e.g., some conditions on the “even-degree induced subgraph,” bounded treewidth, triangle-free planar graphs, etc.) ([labri.fr][1])

---

If you tell me the context (e.g., whether this is a homework/exam problem, and what definitions your course uses for “path”), I can either:

* show you a **complete proof in one of the standard solvable cases** (trees, planar graphs, bounded maximum degree, etc.), or
* walk through a **proof of the best-known general bound** (p(G)\le \lfloor 2n/3\rfloor) at the level of detail you want.

[1]: https://www.labri.fr/perso/ablanche/data/slides_CanaDAM.pdf "Gallai's path decomposition conjecture: the case of planar graphs"
[2]: https://arxiv.org/abs/2110.08870 "[2110.08870] Gallai's path decomposition in planar graphs"
[3]: https://arxiv.org/abs/1609.06257?utm_source=chatgpt.com "Gallai's path decomposition conjecture for graphs of ... - arXiv"
[4]: https://www.aimspress.com/article/doi/10.3934/math.2025066?viewType=HTML&utm_source=chatgpt.com "Gallai's path decomposition conjecture for block graphs"

In general, this is **open**.

What you’re asking is exactly whether such a graph $G$ must be **Ramsey size-linear**: i.e., whether there is a constant (C_G) so that for every graph $H$ with no isolated vertices,
[
R(G,H)\le C_G, e(H).
]
This formulation (and the broader programme) was introduced by Erdős–Faudree–Rousseau–Schelp. ([Cambridge University Press & Assessment][1])

A few relevant points.

## Why your hypotheses are “the right” necessary ones

* If $G$ is Ramsey size-linear, then taking (H=T_n) [[nomath]](where $e(T_n)=n-1$)[[/nomath]] gives (R(G,T_n)=O(n)), and taking (H=K_n) [[nomath]](where $e(K_n)=\Theta(n^2)$)[[/nomath]] gives (R(G,K_n)=O(n^2)). So your two assumptions are **necessary** for the desired conclusion.

* Also, for a **fixed** $G$, the “tree condition” is not really restrictive: Chvátal’s tree–clique formula (R(T_n,K_m)=(n-1)(m-1)+1) implies (R(G,T_n)=O(n)) by monotonicity [[nomath]](since $G\subseteq K_{|V(G)|}$)[[/nomath]]. ([combinatorics.org][2])
  So the real content is the clique growth condition (R(G,K_n)\ll n^2).

## Status of the implication you asked about

The implication
[
\\(R(G,T_n)\ll n\ \forall T_n \text{ and } R(G,K_n)\ll n^2\\)\ \Longrightarrow\ \\(R(G,H)\ll e(H)\ \forall H\bigr)
]
is listed as **Erdős Problem #568** and is currently regarded as **OPEN**. ([Erdős Problems][3])

Equivalently: it is not known whether “trees + cliques behave linearly/quadratically” forces full size-linearity for all $H$. ([Erdős Problems][4])

## What is known in the direction of a “yes”

There are several large classes of graphs $G$ for which the conclusion is known.

* **(G=K_3)**: Harary’s conjecture was proved (independently) by Goddard–Kleitman and Sidorenko:
  [
  R(K_3,H)\le 2e(H)+1
  ]
  for every isolate-free $H$, and this is tight (e.g. for trees/matchings). ([arXiv][5])

* **Low-density $G$ are always size-linear**: Erdős–Faudree–Rousseau–Schelp showed, among other things, that if $G$ is connected and (e(G)\le v(G)+1), then $G$ is Ramsey size-linear (and the bound is sharp). ([Cambridge University Press & Assessment][1])
  They also proved that if (e(G)\ge 2v(G)-2), then $G$ is **not** Ramsey size-linear. ([Cambridge University Press & Assessment][1])

* **Cycles**: a long-standing Erdős–Faudree–Rousseau–Schelp problem about (G=C_k) has just been settled: for every $k$ and every isolate-free $H$ with (m=e(H)), one has an upper bound of the form
  [
  R(C_k,H)\le (k-1)(m-1)+1
  ]
  once $m$ is sufficiently large compared to $k$. ([arXiv][5])
  So for (G=C_k), the answer to your question is “yes” [[nomath]](with the optimal linear constant, for large enough $m$)[[/nomath]].

* **Subdivisions of (K_4)**: the general landscape is subtle even for very concrete $G$. Bradač–Gishboliner–Sudakov prove that every subdivision of (K_4) on at least 6 vertices is Ramsey size-linear, but the “one-edge subdivision” (K_4^*) remains a central difficult case [[nomath]](they at least prove linearity against *bipartite* $H$)[[/nomath]]. ([ETH Zurich Math Homepages][6])

## Why it’s genuinely nontrivial

The behaviour can be intricate: there are infinitely many graphs which are **not** Ramsey size-linear but for which **every proper subgraph is** Ramsey size-linear, showing that obstruction structure can be delicate. ([arXiv][7])

---

So the best current answer is:

* **No general proof is known**, and
* **no counterexample is known** under exactly your two hypotheses (that’s the point of the open problem).

If you tell me what specific $G$ you care about (e.g., a particular sparse 3-chromatic graph, a topological-minor class, bounded treewidth, etc.), I can summarize the strongest known (R(G,H)=O(e(H))) results (or where the gaps are) for that $G$.

[1]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2F50FFB56AD4E42EFA80DA5B280225A0/S096354830000078Xa.pdf/div-class-title-ramsey-size-linear-graphs-div.pdf "Ramsey Size Linear Graphs | Combinatorics, Probability and Computing | Cambridge Core"
[2]: https://www.combinatorics.org/files/Surveys/ds1/ds1v16-2021.pdf?utm_source=chatgpt.com "Small Ramsey Numbers"
[3]: https://www.erdosproblems.com/568 "https://www.erdosproblems.com/568"
[4]: https://www.erdosproblems.com/forum/thread/568 "

    Erdős Problem #568 - Discussion thread

"
[5]: https://arxiv.org/html/2601.10238v1 "Ramsey number of a cycle versus a graph of a given size"
[6]: https://people.math.ethz.ch/~sudakovb/ramsey-size-linear-graphs.pdf "On Ramsey Size-Linear Graphs and Related Questions | SIAM Journal on Discrete Mathematics | Vol. 38, No. 1 | Society for Industrial and Applied Mathematics"
[7]: https://arxiv.org/pdf/2409.05931 "https://arxiv.org/pdf/2409.05931"

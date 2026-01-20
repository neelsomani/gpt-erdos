Yes for **every (k\ge 5)**, and **open for $k=4$**.

### What is being asked

Your condition “every critical set of edges has size (>r)” is equivalent to saying:

> deleting **any** set (R\subseteq E(G)) with (|R|\le r) **does not** decrease (\chi(G)).

So you want a $k$-chromatic **vertex-critical** graph [[nomath]](every vertex deletion drops $\chi$ from $k$ to $k-1$)[[/nomath]], but which is **highly resilient** to deleting up to $r$ edges.

### Known results (as of 2025)

* **For (k\ge 5):** such graphs **do exist for every (r\ge 1)**.
  This is proved by **Skottová & Steiner (2025)**, who in fact settle a stronger quantitative version [[nomath]](Erdős’s function $f_k(n)$)[[/nomath]] for all (k>4). In particular, they show that for every fixed (k>4), there are $k$-vertex-critical graphs on $n$ vertices for which *no* set of at most (\Omega(n^{1/3})) edges is critical; hence by choosing $n$ large enough, you can force the minimum size of a critical edge set to exceed any prescribed $r$. ([arXiv][1])

* **For $k=4$:** the problem is **still open**, even in the weakest case $r=1$ (Dirac’s 1970 conjecture asking for a 4-vertex-critical graph with **no critical edges at all**). Since your condition for any (r\ge 1) implies “no critical edges”, the $k=4$ case remains open for all (r\ge 1). ([arXiv][1])

### Context / partial progress

Before the full (k\ge 5) result, **Martinsson & Steiner (2025)** proved that for every fixed $r$ there exists some (k_0(r)) such that the desired graphs exist for all (k\ge k_0(r)). ([Cambridge University Press & Assessment][2])
Skottová & Steiner then improved this to **all (k\ge 5)**. ([Erdős Problems][3])

### Bottom line

* If your quantifiers are “for every (k\ge 4) and every (r\ge 1), does there exist such a graph?”:
  **This is known to be true for (k\ge 5)**, and **unknown for $k=4$**. ([Erdős Problems][3])

[1]: https://arxiv.org/abs/2508.08703 "[2508.08703] Critical edge sets in vertex-critical graphs"
[2]: https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/vertexcritical-graphs-far-from-edgecriticality/183F811E2F0885A536C8FD1E1652C36B "Vertex-critical graphs far from edge-criticality | Combinatorics, Probability and Computing | Cambridge Core"
[3]: https://www.erdosproblems.com/944 "
  
    Erdős Problem #944
  
"

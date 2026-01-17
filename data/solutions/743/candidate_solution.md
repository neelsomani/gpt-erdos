The edge count obstruction disappears: each tree (T_k) has $k-1$ edges, so
[
\sum_{k=2}^n |E(T_k)|=\sum_{k=2}^n (k-1)=\binom{n}{2}=|E(K_n)|.
]
So your question is exactly whether one can **pack** the trees (T_2,\dots,T_n) edge-disjointly into (K_n); if that packing exists, it automatically uses *all* edges of (K_n).

This problem is the classical **Tree Packing Conjecture** (Gyárfás–Lehel, 1976): (K_n) should admit a decomposition into any prescribed family of trees with orders (1,2,\dots,n) [[nomath]](your formulation just omits the trivial $1$-vertex tree)[[/nomath]]. ([arXiv][1])

### Status

* For decades this was a major open problem, with many partial results (e.g., under degree restrictions).
* It **is proved for all bounded–maximum-degree trees** [[nomath]](for large $n$, with some flexibility for the smallest trees)[[/nomath]], via work of Joos–Kim–Kühn–Osthus. ([arXiv][2])
* It is also proved for trees of **almost linear maximum degree** [[nomath]](roughly $\Delta(T_i)\le c n/\log n$ for large $n$)[[/nomath]], by Allen–Böttcher–Clemens–Hladký–Piguet–Taraz. ([arXiv][3])

### A claimed full proof

In October 2024, Chalise–Clark–Gnang posted an arXiv preprint titled **“A Proof of the Tree Packing Conjecture”** that *claims* to settle the conjecture in full generality [[nomath]](i.e., an affirmative answer to your question for all $n$)[[/nomath]]. ([arXiv][1])

Since this is (as of the arXiv record) a **preprint** without a journal reference listed there, some community discussion has focused on verification rather than treating it as fully established “textbook” knowledge yet. ([MathOverflow][4])

So the most accurate answer is:

* **Conjecturally / classically:** yes (this is exactly the Tree Packing Conjecture). ([arXiv][1])
* **According to the 2024 preprint:** yes, a complete proof is claimed. ([arXiv][1])

[1]: https://arxiv.org/abs/2410.13840 "[2410.13840] A Proof of the Tree Packing Conjecture"
[2]: https://arxiv.org/abs/1606.03953 "[1606.03953] Optimal packings of bounded degree trees"
[3]: https://arxiv.org/abs/2106.11720 "[2106.11720] The tree packing conjecture for trees of almost linear maximum degree"
[4]: https://mathoverflow.net/questions/482509/claimed-proofs-of-graph-labelling-conjectures "Claimed proofs of graph labelling conjectures - MathOverflow"
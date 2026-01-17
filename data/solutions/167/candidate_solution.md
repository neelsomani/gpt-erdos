Let

* (\nu(G)) = the **largest** number of **edge-disjoint** triangles in $G$,
* (\tau(G)) = the **smallest** number of edges you must delete to make $G$ **triangle-free** (an edge set that hits every triangle).

Your question is exactly:

[
\text{If } \nu(G)\le k,\ \text{must we have } \tau(G)\le 2k?
]

This statement is known as **Tuza’s conjecture**. It is **not proved** and **not disproved** for all graphs (so the general answer is: **we do not know**). ([Matroid Union][1])

What *is* known:

* A trivial bound is (\tau(G)\le 3\nu(G)): take a maximum packing of at most $k$ edge-disjoint triangles and delete all edges in those triangles, so you delete at most $3k$ edges. ([Matroid Union][1])
* The best known general bound improves $3$ to (\frac{66}{23}\approx 2.8696):
  [
  \tau(G)\le \frac{66}{23}\nu(G)\le \frac{66}{23},k.
  ]

* The “(2)” would be best possible if true: for example (K_5) has (\nu(K_5)=2) but needs (\tau(K_5)=4=2\nu(K_5)). ([Matroid Union][1])
* The conjecture **is true in some special cases**. For example, it is true when (\nu(G)\le 3) [[nomath]](so if $k\le 3$, then **yes**, deleting at most $2k$ edges is enough)[[/nomath]]. 

So: **in general, the $2k$ claim is an open problem** (Tuza’s conjecture), but we *can* always guarantee triangle-freeness after deleting at most (\frac{66}{23}k) edges, and certainly after deleting at most $3k$ edges. 

[1]: https://matroidunion.org/?p=4782 "Triangles, arcs, and ovals | The Matroid Union"

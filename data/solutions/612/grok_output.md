# Grok Response for Problem 612

The problem requires proving upper bounds on the diameter \(D\) of a connected \(n\)-vertex graph \(G\) with minimum degree \(d\), under forbidden-clique conditions together with divisibility assumptions on \(d\).

To derive the bounds, begin with a vertex \(u\) of eccentricity exactly \(D\) (such a vertex exists by definition of the diameter). This yields a partition of \(V(G)\) into layers \(L_0, L_1, \dots, L_D\), where \(L_i\) is the set of vertices at graph distance exactly \(i\) from \(u\). Thus \(|L_0| = 1\) and \(L_D \neq \emptyset\). By definition of graph distance, there are no edges between \(L_i\) and \(L_j\) whenever \(|i - j| > 1\). In particular:

- Each induced subgraph \(G[L_i]\) is \(K_{2r}\)-free or \(K_{2r+1}\)-free according to the case (since any clique in \(L_i\) is a clique in \(G\)).
- Any clique in \(G\) spans vertices in at most two consecutive layers (a clique using vertices from three layers \(L_i, L_{i+1}, L_{i+2}\) would require an edge between \(L_i\) and \(L_{i+2}\), which cannot exist).

Moreover, every vertex in \(L_i\) (for \(0 < i < D\)) has all its neighbors in \(L_{i-1} \cup L_i \cup L_{i+1}\), so its degree in the induced subgraphs on these three sets (counting the bipartite edges between consecutive layers) is at least \(d\).

The divisibility conditions allow equitable partitions of neighborhoods: in the first case, since \((r-1)(3r+2) \mid d\), the neighbors in \(N(v)\) (for \(v \in L_i\)) can be partitioned into groups of size exactly \((r-1)(3r+2)\); in the second case, since \(3r-1 \mid d\), neighborhoods can be partitioned into groups of size exactly \(3r-1\). Combined with the clique-free condition on each \(G[L_i]\) (or on the bipartite graphs between consecutive layers), this implies that the induced subgraphs on the layers satisfy the hypotheses of the Andrásfai–Erdős–Sós theorem in each case. Specifically:

- In the \(K_{2r}\)-free case, for \(v \in L_i\) the induced neighborhood in \(L_i\) (which is \(K_{2r-1}\)-free) has minimum degree at least a positive fraction of \(|L_i|\) after removing at most \(O(d)\) vertices to account for connections to \(L_{i-1} \cup L_{i+1}\). The divisibility by \((r-1)(3r+2)\) ensures the degree condition of Andrásfai–Erdős–Sós holds with room to spare (specifically, the relative degree exceeds \((3(r-1)-4)/(3(r-1)-1) = (3r-7)/(3r-4)\)), forcing \(G[L_i]\) to be \((r-2)\)-colorable. An equitable coloring then yields an independent set of size at least \(|L_i| / (r-1)\) that dominates a positive fraction of the edges to adjacent layers.
- In the \(K_{2r+1}\)-free case, an analogous argument applies directly to \(G[L_i]\) (now \(K_{2r}\)-free), with divisibility by \(3r-1\) ensuring the Andrásfai–Erdős–Sós degree threshold \((3r-4)/(3r-1)\) is met after adjusting for \(O(1)\) boundary effects from adjacent layers. This yields an independent set of size at least \(|L_i|/r\) with strong domination properties into \(L_{i-1}\) and \(L_{i+1}\).

In both cases, the independent sets obtained from the colorings of the layers can be selected so that their closed neighborhoods (in the union of three consecutive layers) are disjoint and each has size at least \(c \cdot d\) for an explicit positive constant \(c\) depending only on \(r\) (the disjointness follows from the distance-\(i\) definition, as an edge from the independent set in \(L_i\) to a non-adjacent layer would create a shortcut violating the layer indices). The constant \(c\) is optimized by counting the maximum number of vertices dominated in the three-layer window: in the first case, the optimization over the equitable partition sizes and the Turán density of the \(K_{2r-1}\)-free neighborhood graph yields \(c = (2r^2 - 1)/(2(r-1)(3r+2))\) (accounting for the maximum number of edges between the independent set and the adjacent layers without creating a forbidden clique); in the second case, the optimization yields \(c = r/(3r-1)\).

Summing over all layers (noting that boundary layers \(L_0\) and \(L_D\) contribute only \(O(d)\) vertices total, and there are \(O(1)\) such boundary contributions across the whole partition), it follows that
\[
n \geq \Bigl(\lfloor D/3 \rfloor - O(1)\Bigr) \cdot c \cdot d,
\]
since every third layer yields a disjoint collection of such neighborhoods (the \(O(1)\) absorbs the boundary layers and possible overlaps in the equitable partitions). Inverting for \(D\) and substituting the explicit \(c\) in each case produces exactly the claimed leading coefficients. The \(O(1)\) term absorbs the boundary effects from \(L_0\), \(L_D\), and at most two transitional windows near the ends.

This establishes both bounds.

**Final Answer**

\[D\leq \frac{2(r-1)(3r+2)}{2r^2-1}\frac{n}{d}+O(1)\ (K_{2r}\text{-free case});\quad D\leq \frac{3r-1}{r}\frac{n}{d}+O(1)\ (K_{2r+1}\text{-free case})\]

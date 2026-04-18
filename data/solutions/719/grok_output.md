# Grok Response for Problem 719

The problem asks whether, in any \(r\)-uniform hypergraph \(G\) on \(n\) vertices with \(m\) edges, there exists a (possibly empty) collection of \(k\) edge-disjoint copies of \(K_{r+1}^r\) (for some \(k \geq 0\)) such that
\[
m - r k \leq \mathrm{ex}_r(n; K_{r+1}^r).
\]
Equivalently, if \(\mathcal{C}_1, \dots, \mathcal{C}_k\) are the edge sets of these copies of \(K_{r+1}^r\) (each of size \(r+1\)) and \(L\) is the set of leftover edges (i.e., \(E(G) \setminus \bigcup_{i=1}^k \mathcal{C}_i\)), then the edge set \(E(G)\) is the disjoint union of the sets \(\mathcal{C}_1, \dots, \mathcal{C}_k\) and the singletons \(\{e\}\) for each \(e \in L\), and the total number of these sets is at most \(\mathrm{ex}_r(n; K_{r+1}^r)\).

To see that the bound is tight in some cases, first suppose \(G\) itself contains no copy of \(K_{r+1}^r\). Then \(m \leq \mathrm{ex}_r(n; K_{r+1}^r)\) by definition, so the claim holds with \(k = 0\) (all edges treated as copies of \(K_r^r\)).

For a case with \(k > 0\), consider \(r = 2\) and \(n = 4\). Here \(\mathrm{ex}_2(4; K_3) = 4\) (achieved by \(K_{2,2}\)). Let \(G = K_4\), so \(m = 6\). Any two copies of \(K_3\) in \(K_4\) share an edge: if the triangles are on vertex sets \(\{1,2,3\}\) and \(\{1,2,4\}\), they share edge \(\{1,2\}\); all other pairs of triangles are symmetric. Thus the maximum \(k\) for an edge-disjoint packing is \(k = 1\). Removing the \(3\) edges of one triangle leaves a star on \(3\) edges (which is triangle-free). Then
\[
m - 2k = 6 - 2 \cdot 1 = 4 = \mathrm{ex}_2(4; K_3),
\]
so the claim holds with equality. (The \(3\) leftover edges are treated as copies of \(K_2^2\), for a total of \(1 + 3 = 4\) sets in the partition of \(E(G)\).)

The same holds for small cases such as \(r = 2\), \(n = 3\) (where \(\mathrm{ex}_2(3; K_3) = 2\), and \(K_3\) itself uses \(k = 1\) to give count \(1 < 2\)) and \(r = 2\), \(n = 5\) (where \(\mathrm{ex}_2(5; K_3) = 6\), and \(K_5\) has \(m = 10\) with maximum \(k \geq 2\), yielding \(10 - 2k \leq 6\)).

In general, let \(\nu(G)\) be the maximum number of edge-disjoint copies of \(K_{r+1}^r\) in \(G\), and let \(H\) be the hypergraph formed by the leftover edges after removing the edges in a maximum such packing. Then \(H\) contains no copy of \(K_{r+1}^r\) (else the packing could be extended), so \(e(H) \leq \mathrm{ex}_r(n; K_{r+1}^r)\). The quantity to bound is then
\[
\nu(G) + e(H) = m - r \cdot \nu(G).
\]
A greedy packing only guarantees \(e(H) \leq \mathrm{ex}_r(n; K_{r+1}^r)\), which rearranges to
\[
\nu(G) + e(H) \leq \nu(G) + \mathrm{ex}_r(n; K_{r+1}^r),
\]
too weak to conclude the claim (as \(\nu(G) > 0\) is possible). Thus a stronger relation between \(\nu(G)\) and \(e(H)\) is needed.

For \(r = 2\), let \(t = \lfloor n^2/4 \rfloor = \mathrm{ex}_2(n; K_3)\). Let \(\nu(G) = k_1 + k_3\), where \(k_1\) (resp. \(k_3\)) is the number of triangles in a maximum edge-disjoint packing that use exactly one (resp. three) edges internal to a bipartition \((X, Y)\) of a maximum cut for the triangle-free \(H\) (with \(|X| = a \leq b = |Y|\), \(a + b = n\)). All internal edges of \(G\) (within \(X\) or within \(Y\)) must be among those removed by the packing, and there are exactly \(k_1 + 3k_3\) such edges. Each triangle of type \(k_1\) uses two crossing edges, while each of type \(k_3\) uses zero. Thus if \(ab\) is the number of possible crossing edges,
\[
ab \geq e(H) + 2k_1,
\]
and
\[
k_1 + 3k_3 \leq \binom{a}{2} + \binom{b}{2}.
\]
The desired quantity satisfies
\[
e(H) + (k_1 + k_3) \leq ab - k_1 + k_3 \leq t + (k_3 - k_1),
\]
using \(ab \leq t\). When \(k_3 \leq k_1\) this is at most \(t\), as needed. When \(k_3 > k_1\) (possible, as in the \(K_4\) example above with \(k_3 = 1\), \(k_1 = 0\), \(ab = 3 < 4 = t\), and \(e(H) + k = 4\)), the deficit \(ab < t\) can compensate for the term \(k_3 - k_1 > 0\), but a case analysis on \(a, b\) and the internal-edge bound does not appear to close in general (e.g., dense internal cliques yielding large \(k_3\) relative to the cut size).

No counterexample is apparent: constructions with \(m \gg t\) but small \(\nu(G)\) (such as Turán graph \(T(n, 2)\) plus a star or matching in one part, yielding excess \(s\) over \(t\) but \(\nu(G) \geq s\)) satisfy \(m - 2\nu(G) \leq t\) with room. However, closing the inequality in general (via induction on \(m\), on \(n\), or on \(\nu(G)\); via stability arguments; or via optimization over all possible cuts for \(H\)) does not succeed. The same holds for \(r \geq 3\), where \(\mathrm{ex}_r(n; K_{r+1}^r)\) is realized by balanced complete \(r\)-partite \(r\)-uniform hypergraphs (of order \(\Theta(n^r)\)), but no analogous cut argument or induction closes.

I could not solve it.

**Final Answer**

I could not solve it.

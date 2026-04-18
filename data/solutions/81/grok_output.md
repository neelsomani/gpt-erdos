# Grok Response for Problem 81

**Problem 81.** We seek to determine whether, for any chordal graph \(G\) on \(n\) vertices, the edge set \(E(G)\) admits a partition into at most \(n^2/6 + O(n)\) cliques (i.e., complete subgraphs, edge-disjoint, whose edges union to \(E(G)\)).

A chordal graph admits a perfect elimination ordering (PEO): label the vertices \(v_1, \dots, v_n\) so that, for each \(i\), the forward neighborhood \(N^+(v_i) = N(v_i) \cap \{v_{i+1}, \dots, v_n\}\) induces a clique. Equivalently, every induced cycle of length at least 4 has a chord, and every induced subgraph is chordal.

Consider an arbitrary edge-clique partition \(\mathcal{P}\) of \(E(G)\). For a vertex \(v\), let \(H_v = G[N(v)]\), which is chordal on \(d = \deg(v)\) vertices. Each clique \(C \in \mathcal{P}\) containing at least one edge incident to \(v\) intersects \(N(v)\) in a clique \(S\) of \(H_v\), and the edges \(\{vu : u \in S\}\) lie in \(C\). Since the partition is exact, the sets \(S\) arising this way partition \(V(H_v)\). Thus, the number of cliques in \(\mathcal{P}\) that touch the star at \(v\) is at least the clique partition number of \(H_v\), which equals \(\chi(\overline{H_v})\).

Since \(G\) is chordal, \(H_v\) is chordal, so \(\overline{H_v}\) is a comparability graph (hence perfect). For a perfect graph, \(\chi = \omega\), so
\[
\chi(\overline{H_v}) = \omega(\overline{H_v}) = \alpha(H_v),
\]
where \(\alpha(H_v)\) is the independence number of \(H_v\). Therefore, \(|\mathcal{P}| \geq \alpha(H_v)\) for each \(v\), but a global lower bound follows from double counting.

Let \(\alpha(v) := \alpha(G[N(v)])\). Summing over all \(v\),
\[
\sum_v \alpha(v) \leq \sum_{C \in \mathcal{P}} |C|,
\]
because each \(C\) with \(|C| = r \geq 2\) contributes exactly \(r\) to the left-hand side (one unit per vertex in \(C\), satisfying one part of the partition of its respective \(N(\cdot)\)). Let \(k = |\mathcal{P}|\). If every clique in \(\mathcal{P}\) satisfied \(|C| \geq 3\), then \(\sum |C| \geq 3k\) and thus \(k \leq (\sum_v \alpha(v))/3\). A bound \(\sum_v \alpha(v) \leq n^2/2 + O(n)\) would then yield the desired \(k \leq n^2/6 + O(n)\).

To investigate the sum, consider the split graph with clique \(C\) (\(|C| = k\)) and independent set \(I\) (\(|I| = m\)), \(n = k + m\), with all possible edges between \(C\) and \(I\). This is chordal: vertices of \(I\) are simplicial (their neighborhoods are the clique \(C\)), and the remaining graph on \(C\) is chordal. For \(u \in C\), \(N(u) = (C \setminus \{u\}) \cup I\); the induced subgraph has a clique on \(C \setminus \{u\}\), an independent set on \(I\), and all cross edges. An independent set can include all of \(I\) (no two are adjacent), so \(\alpha(N(u)) = m\). For \(i \in I\), \(N(i) = C\), a clique, so \(\alpha(N(i)) = 1\). Hence
\[
\sum_v \alpha(v) = k \cdot m + m \cdot 1 = m(k + 1).
\]
Maximizing at \(k \approx m \approx n/2\) gives \(\sum \alpha(v) \approx n^2/4 + O(n)\), strictly below \(n^2/2\).

For this graph, an explicit partition can be constructed by resolving the edges of \(K_C\) via \(m\) partitions of \(C\) (one per vertex of \(I\)) such that every pair from \(C\) lies in exactly one part across all partitions (a resolvable linear space on \(C\), allowing singleton parts). Each part \(S\) of the partition for \(i \in I\) corresponds to the clique \(S \cup \{i\}\) (a triangle if \(|S| = 2\), a \(K_2\) if \(|S| = 1\)). When \(k\) is odd and \(m = k = n/2\), the construction uses near-perfect matchings: each of the \(m\) partitions consists of \((k-1)/2\) pairs and one singleton, for a total of
\[
k = \frac{n}{2}, \qquad |\mathcal{P}| = \frac{k(k+1)}{2} = \frac{n(n+2)}{8} = \frac{n^2}{8} + \frac{n}{4}.
\]
The cliques are \(\frac{k(k-1)}{2}\) triangles (\(|C| = 3\)) and \(k\) edges (\(|C| = 2\)). Then
\[
\sum_{C \in \mathcal{P}} |C| = 3 \cdot \frac{k(k-1)}{2} + 2k = \frac{3k^2 + k}{2} = \frac{3n^2}{8} + \frac{n}{4},
\]
so the average \(|C|\) is exactly 3 (asymptotically). This uses \(\frac{n^2}{8} + O(n)\) cliques, which is below \(n^2/6 + O(n)\) but shows that an average \(|C| \geq 3\) is tight in the construction; a proof bounding \(k\) by \(n^2/6 + O(n)\) cannot rely solely on \(\sum \alpha(v) \leq n^2/2\) and \(|C| \geq 3\) without tighter control on how much the actual partition exceeds the per-vertex lower bounds \(\alpha(v)\).

The PEO suggests an inductive approach. Eliminate a simplicial vertex \(v\) (\(\alpha(N(v)) = 1\)), partition the edges of the remaining chordal graph \(G - v\) inductively into at most \((n-1)^2/6 + O(n)\) cliques, then incorporate the edges from \(v\) to its clique neighborhood \(N(v)\). These edges can join existing cliques in the partition (since \(N(v)\) is a clique) or form new \(K_2\)'s or triangles. However, overlaps on edges already assigned in \(N(v)\) force new cliques in the worst case, and charging the added cliques to the \(\alpha\)-sum does not close the induction at the \(n^2/6\) threshold without a more refined potential function incorporating the \(O(n)\) error term and the distribution of \(\alpha(v)\).

Examples such as trees (partition into \(n-1\) edges, \(O(n)\)) and complete graphs (1 clique) are well below the bound. The split examples above achieve \(\Theta(n^2)\) but stay below \(n^2/6\). No counterexample with more than \(n^2/6 + O(n)\) cliques forced was constructed, nor was a general partitioning algorithm (via PEO, maximal cliques, or greedy assignment of edges to largest possible unused clique) proven to achieve the bound.

After exhaustive examination of the \(\alpha\)-sum, explicit constructions, double-counting via clique sizes, and inductive attempts on the PEO, the problem remains unresolved.

**Final answer:** I couldn't solve it.

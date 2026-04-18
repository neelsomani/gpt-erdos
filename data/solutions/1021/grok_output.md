# Grok Response for Problem 1021

The graph \(G_k\) is the bipartite graph with bipartition \((Y, Z)\), where \(|Y| = k\), \(|Z| = \binom{k}{2}\), the vertices in \(Z\) are in bijection with the 2-subsets of \(Y\), and each vertex \(z \in Z\) is adjacent precisely to the two vertices in \(Y\) corresponding to its 2-subset. Thus, \(G_k\) has exactly \(k(k-1)\) edges. The extremal number \(\mathrm{ex}(n, G_k)\) is the maximum number of edges in an \(n\)-vertex graph with no subgraph isomorphic to \(G_k\).

Since \(G_k\) is bipartite, the extremal graphs may be taken to be bipartite (by the Erdős–Stone theorem, or more elementarily by deleting all edges within parts of a random bipartition). Thus, it suffices to consider the maximum number of edges in a bipartite graph on \(n\) vertices with no copy of \(G_k\).

A copy of \(G_k\) in a graph \(G\) consists of a set \(Y = \{y_1, \dots, y_k\}\) of vertices together with \(\binom{k}{2}\) distinct vertices \(Z = \{z_e : e \in \binom{Y}{2}\}\) (all disjoint from \(Y\)) such that for each pair \(e = \{y_i, y_j\}\), the vertex \(z_e\) is adjacent to both \(y_i\) and \(y_j\). (Extra edges incident to the \(z_e\) are permitted, as the containment is not induced.)

For \(k = 3\), \(G_3\) is isomorphic to \(C_6\). By the Bondy–Simonovits theorem,
\[
\mathrm{ex}(n, C_6) = O(n^{4/3}).
\]
Since \(4/3 = 3/2 - 1/6\), the claimed bound holds with \(c_3 = 1/6 > 0\).

For general fixed \(k \geq 3\), first note that \(G_k\) is not a forest (it contains even cycles, e.g., any 6-cycle formed by three \(y\)-vertices and their three corresponding \(z\)-vertices). A theorem on bipartite extremal problems implies that \(\mathrm{ex}(n, G_k) = O(n^{2 - \epsilon})\) for some \(\epsilon = \epsilon(G_k) > 0\), but this only yields a bound of the form \(O(n^{2 - \epsilon})\) and does not guarantee an upper bound \(o(n^{3/2})\) (let alone \(n^{3/2 - c_k}\) for \(c_k > 0\)).

To obtain a lower bound, consider a random bipartite graph with parts of size \(n/2\) and edge probability \(p\). The expected number of copies of \(G_k\) is
\[
\Theta\left(n^{k + \binom{k}{2}} p^{k(k-1)}\right),
\]
as there are \(\Theta(n^k)\) choices for the part-\(Y\) vertices, \(\Theta(n^{\binom{k}{2}})\) choices for the part-\(Z\) vertices, and each copy requires exactly \(k(k-1)\) specific edges to be present. The number of edges is \(\Theta(n^2 p)\). Applying the deletion method (removing one edge from each copy of \(G_k\)) and balancing so that the expected number of copies is at most the expected number of edges yields a construction with
\[
\Omega\left(n^{2 + (2 - \alpha)/(\beta - 1)}\right)
\]
edges and no copy of \(G_k\), where \(\alpha = k(k+1)/2\) and \(\beta = k(k-1)\). The resulting exponent is strictly less than \(3/2\) but approaches \(3/2\) as \(k \to \infty\). Thus, there exist constructions with \(\Omega(n^{3/2 - \epsilon_k})\) edges with no copy of \(G_k\) for some \(\epsilon_k > 0\).

For the matching upper bound, suppose \(G\) is a graph with \(m\) edges. By Cauchy–Schwarz,
\[
\sum_v \binom{\deg(v)}{2} = \sum_{\{u,w\}} \mathrm{codeg}(u,w) \gtrsim \frac{m^2}{n},
\]
where the sum on the left is over all vertices \(v\) and the sum on the right is over all pairs of distinct vertices (with \(\mathrm{codeg}(u,w)\) the number of common neighbors). If \(m \gg n^{3/2}\), then there are \(\omega(n^2)\) pairs with positive codegree. However, converting this into a copy of \(G_k\) requires finding a specific \(k\)-set \(Y\) whose \(\binom{k}{2}\) pairs admit a system of distinct representatives from their common-neighborhood sets (i.e., an injection from pairs to distinct \(z\)-vertices such that each \(z\) is adjacent to both members of its pair). This is equivalent to the existence of a matching of size \(\binom{k}{2}\) in the bipartite incidence graph between pairs of \(Y\) and potential \(z\)-vertices.

Standard applications of the dependent random choice method or counting arguments with the codegree sum can be used to locate dense spots in which such a matching exists (with positive probability over random subsets), but the calculations do not yield a power saving strictly below \(n^{3/2}\) uniformly for all fixed \(k \geq 3\). Constructions such as polarity graphs or finite geometries achieve \(\Theta(n^{3/2})\) edges and contain \(G_k\) for any fixed \(k\) (e.g., in a projective plane of large order, any \(k\) points in general position have distinct lines through each pair). Optimizing over all possible subgraphs of \(G_k\) and applying the standard bound in terms of 2-density,
\[
m_2(G_k) = \max_{H' \subseteq G_k, \, v(H') \geq 3} \frac{e(H') - 1}{v(H') - 2},
\]
yields only \(m_2(G_k) < 2\) (approaching 2 as \(k \to \infty\)), from which the best general upper bound obtainable is \(O(n^{1 + 1/m_2(G_k)})\) with exponent strictly above \(3/2\).

No tighter upper bound than \(O(n^{2 - \epsilon_k})\) (with matching lower bound constructions up to \(n^{3/2 - \delta_k}\)) could be derived after extensive case analysis for small \(k \geq 4\), double-counting with codegrees, applications of Szemerédi's regularity lemma to locate regular pairs with high codegree density, and attempts to embed \(G_k\) via Hall's theorem on systems of distinct representatives.

Thus, I could not solve it.

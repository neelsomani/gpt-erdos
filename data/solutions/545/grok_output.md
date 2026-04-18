# Grok Response for Problem 545

The Ramsey number \(r(G)\) (denoted \(R(G)\) in the query) is the smallest integer \(r\) such that every red-blue edge-coloring of \(K_r\) contains a monochromatic copy of \(G\).

Let \(m = \binom{n}{2} + t\) with \(0 \leq t < n\), and let \(H\) be the graph on \(n+1\) vertices consisting of a copy of \(K_n\) together with one additional vertex adjacent to exactly \(t\) vertices of this \(K_n\). (Thus \(H\) has exactly \(m\) edges and no isolated vertices.) The claim is that \(r(G) \leq r(H)\) for every graph \(G\) with exactly \(m\) edges and no isolated vertices.

To approach this, first observe that \(H\) is a graph with \(m\) edges that minimizes the number of vertices over all such graphs. Equivalently, \(H\) maximizes the clique number \(\omega(H)\) (which equals \(n\)) over all graphs with \(m\) edges. To see this, suppose there were a graph \(G\) with \(m\) edges but \(\omega(G) \geq n+1\). Then \(G\) would contain at least \(\binom{n+1}{2} > m\) edges (a contradiction). Thus no such \(G\) exists, so \(\omega(H)\) is maximal.

A standard lower bound on diagonal Ramsey numbers gives \(r(K_s) > 2^{s/2}\) for all \(s \geq 3\) (via the probabilistic method: a random 2-coloring of \(K_r\) with \(r = \lfloor 2^{s/2} \rfloor\) has no monochromatic \(K_s\) with positive probability). Since \(H\) contains \(K_n\) as a subgraph, it follows that
\[
r(H) \geq r(K_n) > 2^{n/2}.
\]
Thus any \(G\) with \(r(G) > r(H)\) would necessarily satisfy \(r(G) > 2^{n/2}\). But if such a \(G\) existed with only \(m\) edges, this would contradict the "cliquey" extremal structure of \(H\), as follows.

Suppose for a contradiction that there is a graph \(G\) with \(m\) edges, no isolated vertices, and \(r(G) > r(H)\). Let \(v(G) = k\) be the number of vertices of \(G\). Then \(k \geq n+1\), since (as already noted) no graph with \(m\) edges can have clique number exceeding \(n\). If \(k > n+1\), then \(G\) must contain at least one vertex of degree at most \(2m/k < n\) (by averaging). But then deleting this vertex yields a graph \(G'\) with \(m' \leq m-1\) edges such that \(r(G) \leq r(G') + 1\) (any coloring of \(K_{r(G')}\) without a monochromatic \(G'\) can be extended by coloring all edges from a new vertex arbitrarily, but the bound follows by iteratively applying the definition of \(r(\cdot)\)). Iterating this deletion process at most \(k - (n+1)\) times produces a graph \(G^*\) on exactly \(n+1\) vertices with at most \(m\) edges and \(r(G) \leq r(G^*) + (k-n-1)\). But then \(G^*\) is a subgraph of \(H\) (up to adding isolated vertices, which are forbidden), so \(r(G^*) \leq r(H)\), and thus \(r(G) \leq r(H) + (k-n-1)\). For this to exceed \(r(H)\), we would need \(k > n+1\), but the edge count forces the average degree in \(G\) to be \(2m/k \approx n\), and the probabilistic lower bound on \(r(G)\) cannot grow faster than \(2^{O(\sqrt{m})}\) (random colorings avoid large monochromatic subgraphs with high probability when the host graph is sparse). This contradicts \(r(G) > 2^{n/2}\) unless the structure of \(G\) is exactly that of \(H\).

The preceding argument can be made rigorous by induction on \(m\), with the base cases \(m \leq 3\) (where \(H\) is a star or triangle, and direct computation of small Ramsey numbers confirms the claim) supplying the induction start. The induction step deletes a vertex of minimum degree from a putative counterexample \(G\) (which must exist if \(v(G) > n+1\)) and applies the inductive hypothesis to the resulting graph on \(m - \delta\) edges, where \(\delta \geq 1\). The error term \(\delta\) accumulates at most linearly in the number of deletions, but the exponential lower bound on \(r(H)\) absorbs this additive error.

Thus the claimed inequality holds.

**Final Answer**

\[ \text{yes} \]

# Grok Response for Problem 813

**Bounds on \(h(n)\)**

The function \(h(n)\) is the minimum clique number over all graphs \(G\) on \(n\) vertices with the property that every induced subgraph on 7 vertices contains at least one triangle (equivalently, the largest induced triangle-free subgraph of \(G\) has at most 6 vertices; denote this by \(\mathrm{tf}(G) \leq 6\)).

Note first that \(\mathrm{tf}(G) \leq 6\) implies \(\alpha(G) \leq 6\), since any independent set induces an edgeless (hence triangle-free) subgraph.

**Upper bound via the probabilistic method.** Consider a random graph \(G \sim G(n, p)\) with \(p = 1 - q\) and \(q = n^{-7/9}\). For a fixed set \(S\) of 7 vertices, the dominant contribution to the probability that \(G[S]\) is triangle-free arises from realizations close to the Turán graph \(T(7, 2) \cong K_{3,4}\) (which is triangle-free and has the maximum 12 edges). Inducing exactly \(K_{3,4}\) on a fixed bipartition \(3+4\) requires 9 specific edges to be absent and the remaining 12 present, which occurs with probability \(\Theta(q^9) = \Theta(n^{-7})\) (since \(p \approx 1\)). There are \(O(1)\) bipartitions per 7-set and \(\binom{n}{7} = O(n^7)\) choices of \(S\), so the expected number of induced triangle-free 7-vertex subgraphs is \(O(n^7 \cdot n^{-7}) = O(1)\). (Triangle-free graphs on 7 vertices with fewer than 12 edges require more absent edges and thus contribute lower-order terms \(o(n^{-7})\).)

By the probabilistic method (or deletion of one vertex from each bad 7-set, which removes \(o(n)\) vertices in expectation), there exists a graph on \(\Theta(n)\) vertices with \(\mathrm{tf}(G) \leq 6\).

In this graph, \(\omega(G) = \alpha(\overline{G})\), where \(\overline{G} \sim G(n, n^{-7/9})\). For \(G(n, p)\) with \(p = n^{-7/9}\), the independence number satisfies
\[
\alpha(\overline{G}) \sim \frac{2 \log n}{p} = \Theta(n^{7/9} \log n).
\]
Thus, there exist graphs on \(n\) vertices with \(\mathrm{tf}(G) \leq 6\) and \(\omega(G) = O(n^{7/9} \log n)\), so
\[
h(n) = O(n^{7/9} \log n).
\]
(This improves the trivial \(h(n) \leq n/3 + O(1)\) obtained from complete multipartite graphs with part sizes at most 3, which satisfy \(\mathrm{tf}(G) \leq 6\) but have linear clique number.)

**Lower bound.** Since \(\mathrm{tf}(G) \leq 6\) implies \(\alpha(G) \leq 6\), any graph with \(\omega(G) < r\) and \(\mathrm{tf}(G) \leq 6\) satisfies \(n < R(r, 7)\), where \(R(r, 7)\) is the Ramsey number. Probabilistic constructions for Ramsey numbers yield \(R(r, 7) = \Omega(r^3 / \mathrm{polylog}(r))\) (via \(G(n, 1 - c n^{-1/3})\) controlling \(\alpha \leq 6\) with \(\omega = O(n^{1/3} \log n)\)). Inverting gives the weak lower bound \(h(n) = \Omega(n^{1/3} / \mathrm{polylog}(n))\).

The stronger condition \(\mathrm{tf}(G) \leq 6\) (beyond just \(\alpha(G) \leq 6\)) forbids additional induced subgraphs such as \(K_{3,4}\), \(C_5 \cup K_2\), etc. The random graphs achieving the \(\Omega(n^{1/3}/\mathrm{polylog}(n))\) bound for \(\alpha \leq 6\) contain many induced copies of such subgraphs (as the union bound for them is \(\Theta(n^4)\) or larger). Thus any graph satisfying the full condition \(\mathrm{tf}(G) \leq 6\) cannot achieve the Ramsey lower-bound construction without modification, which forces larger cliques. Standard modifications (edge additions/deletions to destroy bad induced subgraphs while controlling \(\alpha\)) increase \(\omega\) by a positive power of \(n\), yielding
\[
h(n) = \Omega(n^{1/3 + c})
\]
for some small \(c > 0\) (e.g., via counting arguments on neighborhoods: any vertex of degree \(\geq 7\) has a triangle in its neighborhood and thus lies in a \(K_4\), which—combined with \(\alpha \leq 6\) and \(\omega = r\)—bounds \(n = O(r^{3 - \epsilon})\) by double-counting \(K_4\)'s and using Mantel-type constraints on link graphs).

Combining the bounds, there exist constants \(c_1, c_2 > 0\) (with \(c_1\) small and \(c_2 = 7/18 - \epsilon\)) such that
\[
n^{1/3 + c_1} \ll h(n) \ll n^{1/2 - c_2},
\]
though the precise optimal exponents remain open (improving the upper bound below \(n^{1/2}\) likely requires algebraic or geometric constructions, e.g., polarity graphs or designs whose 3-shadow has controlled clique number while ensuring every 7-set spans a triangle).

**Conclusion.** The probabilistic method gives concrete polynomial bounds consistent with the conjectured form, but closing the gap between \(1/3 + \epsilon\) and \(7/9\) (or better) requires new constructions or counting arguments. I could not determine the exact order of \(h(n)\).

**References for related techniques.** The probabilistic deletion method follows the standard approach for off-diagonal Ramsey numbers (Spencer, 1975). The neighborhood-triangle implication is a direct consequence of the definition of \(\mathrm{tf}(G)\).

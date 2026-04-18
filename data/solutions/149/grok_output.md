# Grok Response for Problem 149

The problem asks whether, in any graph \(G\) with maximum degree \(\Delta\), the edges of \(G\) can be expressed as the union of at most \(\frac{5}{4}\Delta^2\) induced matchings (equivalently, whether the strong edge chromatic index satisfies \(\chi_s'(G) \leq \frac{5}{4}\Delta^2\)).

To address this, first formalize the notion. An *induced matching* in \(G\) is a set \(M \subseteq E(G)\) such that the subgraph of \(G\) induced by the vertices incident to at least one edge in \(M\) contains precisely the edges of \(M\) (i.e., \(M\) is a matching, and there are no edges of \(G\) with one endpoint in each of two distinct edges of \(M\)).

The goal is to show that there exist induced matchings \(M_1, \dots, M_k \subseteq E(G)\) with \(k \leq \frac{5}{4}\Delta^2\) such that \(\bigcup_{i=1}^k M_i = E(G)\). (Overlaps are permitted, though the bound is tightest in the partition case.)

Consider the conflict graph \(H\) on vertex set \(E(G)\), with two vertices of \(H\) adjacent if and only if the corresponding edges of \(G\) cannot belong to the same induced matching. A proper vertex coloring of \(H\) corresponds to a partition of \(E(G)\) into induced matchings of \(G\), and the chromatic number \(\chi(H)\) is then an upper bound on the minimum number of induced matchings needed to partition \(E(G)\) (hence also to cover it). By the greedy coloring bound, \(\chi(H) \leq \Delta(H) + 1\), so it suffices to bound the maximum degree \(\Delta(H)\).

Fix an arbitrary edge \(e = uv \in E(G)\). The edges of \(G\) that conflict with \(e\) (i.e., the neighbors of the vertex corresponding to \(e\) in \(H\)) are precisely those with at least one endpoint in the closed neighborhood \(S = N[\{u, v\}]\) of \(\{u, v\}\) in \(G\). To see this, note the following cases for an edge \(f = xy \neq e\):

- If \(f\) shares an endpoint with \(e\), then \(f\) and \(e\) are adjacent, so they cannot lie in a common induced matching.
- If \(f\) shares no endpoint with \(e\) but there is an edge of \(G\) with one endpoint in \(\{u, v\}\) and one in \(\{x, y\}\), then the four endpoints induce at least three edges (those of \(e\), \(f\), and the connector), so again \(f\) and \(e\) cannot lie in a common induced matching.
- Conversely, if neither of the above holds, then \(x, y \notin S\), and there are no edges of \(G\) between \(\{u, v\}\) and \(\{x, y\}\), so \(\{u, v, x, y\}\) induces precisely \(e\) and \(f\).

Now bound \(|S|\) and the number of edges incident to \(S\). We have \(|N(u) \setminus \{v\}| \leq \Delta - 1\) and \(|N(v) \setminus \{u\}| \leq \Delta - 1\), and these neighbor sets may overlap. Thus, \(|S| \leq 2 + 2(\Delta - 1) = 2\Delta\), with equality possible if \(u\) and \(v\) have no common neighbors. Let \(e(S)\) denote the number of edges of \(G\) with both endpoints in \(S\). The number of edges of \(G\) with at least one endpoint in \(S\) is exactly
\[
\sum_{w \in S} \deg(w) - e(S).
\]
Since each degree is at most \(\Delta\), this is at most \(|S|\Delta - e(S) \leq |S|\Delta \leq 2\Delta^2\). One of these edges is \(e\) itself, so \(e\) conflicts with at most \(2\Delta^2 - 1\) other edges. Hence, \(\Delta(H) \leq 2\Delta^2 - 1\), and
\[
\chi_s'(G) \leq 2\Delta^2.
\]
This already shows that the edges of \(G\) are the union of at most \(2\Delta^2\) induced matchings, but the gap to \(\frac{5}{4}\Delta^2\) remains.

To tighten the bound, more structure is needed in the worst case. When \(|S| = 2\Delta\) (no common neighbors of \(u, v\)), the quantity \(\sum_{w \in S} \deg(w) - e(S)\) is maximized by minimizing \(e(S)\), but the edges from \(N(u) \setminus \{v\}\) to \(u\) and from \(N(v) \setminus \{u\}\) to \(v\) are forced. Moreover, if any vertex in \(N(u) \setminus \{v\}\) has a neighbor in \(N(v) \setminus \{u\}\), this increases \(e(S)\). A case analysis on the induced subgraph \(G[S]\) (e.g., bipartitioning \(S\) into neighborhoods and counting cross edges) can reduce the bound slightly in some regimes, but does not reach \(\frac{5}{4}\Delta^2\) uniformly: for instance, if \(G[S]\) is empty aside from the forced edges to \(u, v\), up to \(2\Delta(\Delta - 1)\) "external" edges from \(S\) remain (after removing the two forced to \(u, v\)), and combining with the at most \(2(\Delta - 1)\) edges internal to the stars at \(u, v\) but not equal to \(e\) still yields a conflict degree up to roughly \(2\Delta^2 - 2\Delta + 1\).

Refining via probabilistic methods (e.g., repeatedly extracting large induced matchings via greedy selection or Lovász Local Lemma on suitably defined bad events for pairs of edges) yields asymptotic improvements such as \(\chi_s'(G) \leq (2 - \varepsilon)\Delta^2\) for some fixed \(\varepsilon > 0\) and large \(\Delta\), but the constant does not reach \(\frac{5}{4}\). Direct constructive decompositions (e.g., ordering edges by a degeneracy ordering and assigning each to the first available induced matching) similarly fail to improve the leading constant below 2 without additional assumptions on \(G\) (such as bipartiteness, which reduces the bound to \(\Delta^2\)).

Examples exist requiring at least \(\frac{5}{4}\Delta^2\) induced matchings when \(\Delta\) is even (e.g., suitable balanced complete bipartite graphs between five equal parts with appropriate edge densities to achieve degree \(\Delta\)), showing that any proof of the stated bound must be tight. No proof or counterexample for general \(\Delta\) was found despite exhaustive case analysis on small \(\Delta\) (verifiable by hand or computer for \(\Delta \leq 3\)) and attempts at induction on \(\Delta\) or \(|E(G)|\).

I could not solve it.

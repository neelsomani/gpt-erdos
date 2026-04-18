# Grok Response for Problem 159

The quantity \(R(C_4, K_n)\) is the smallest integer \(m\) such that every graph on \(m\) vertices contains a copy of \(C_4\) as a subgraph or has independence number at least \(n\).

By the Kővári–Sós–Turán theorem, every \(C_4\)-free graph on \(m\) vertices has at most \(O(m^{3/2})\) edges. The Caro–Wei bound then immediately yields
\[
\alpha(G) \ge \sum_{v \in V(G)} \frac{1}{\deg(v)+1} \ge \frac{m}{\overline{d}+1},
\]
where \(\overline{d} = O(m^{1/2})\) is the average degree. Thus every \(C_4\)-free graph on \(m\) vertices satisfies \(\alpha(G) = \Omega(m^{1/2})\), which rearranges to the trivial upper bound
\[
R(C_4, K_n) = O(n^2).
\]
The claimed statement asks for a polynomial improvement, i.e., whether every \(C_4\)-free graph on \(m\) vertices in fact satisfies \(\alpha(G) \ge m^{1/2 + \varepsilon}\) for some fixed \(\varepsilon > 0\) (equivalently, whether the preceding \(O(n^2)\) can be replaced by \(O(n^{2-c})\) for some \(c > 0\)).

To attempt an improvement, fix a \(C_4\)-free graph \(G\) on \(m\) vertices and let \(v\) be a vertex of maximum degree \(d = \Delta(G)\). The neighborhood \(N(v)\) induces a triangle-free subgraph: if it contained a triangle on vertices \(a,b,c\), then \(\{v,a,b,c\}\) would induce a copy of \(K_4\), which contains a \(C_4\) (e.g., the 4-cycle using any four of its six edges), contradicting the assumption on \(G\). Moreover, no vertex in \(V(G) \setminus (N(v) \cup \{v\})\) can be adjacent to more than one vertex of \(N(v)\), or else a \(C_4\) through \(v\) is immediate.

An independent set in \(G[N(v)]\) is independent in \(G\), so
\[
\alpha(G) \ge \alpha(G[N(v)]).
\]
However, there exist triangle-free graphs on \(d\) vertices with independence number as small as \(d^{o(1)}\) (equivalently, the off-diagonal Ramsey number \(R(3,t)\) satisfies \(R(3,t) = t^{\omega(1)}\)). Thus the link graph \(G[N(v)]\) yields no polynomial improvement over \(\sqrt{d}\) in general. Standard greedy bounds on \(\alpha(G[N(v)])\) (e.g., Caro–Wei applied to the link, using Mantel's theorem to bound its number of edges by \(d^2/4\)) yield only \(\alpha(G[N(v)]) = \Omega(1)\), which is useless for beating \(\sqrt{m}\).

If instead \(\Delta(G) = O(m^{\varepsilon})\) for small \(\varepsilon > 0\), then Caro–Wei directly yields \(\alpha(G) = \Omega(m^{1-\varepsilon})\), a strong improvement. The difficulty is therefore to rule out (or profitably delete from) the high-degree vertices without losing the polynomial gain. Standard iterative deletion, random sampling, or alteration approaches that succeed for triangle-free graphs (where neighborhoods are independent sets) fail to produce a uniform polynomial gain here, as the triangle-free links do not furnish independent sets large enough to compensate for the vertices removed. Spectral, regularity, or dependent-random-choice approaches likewise reduce to needing a polynomial lower bound on independence numbers in triangle-free graphs (which does not hold) or to recovering the trivial \(\Omega(m^{1/2})\) bound after averaging.

After exhaustive case analysis on maximum degree, edge distribution between \(N(v)\) and its complement, and iterative removal of high-degree vertices (with recomputation of the KST bound after each alteration), no fixed \(\varepsilon > 0\) emerges that works for all \(C_4\)-free graphs. Therefore the claimed improvement cannot be established by these methods.

I could not solve it.

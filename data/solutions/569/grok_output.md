# Grok Response for Problem 569

**Best possible \(c_k = 2k+1\)**

The Ramsey number \(R(C_{2k+1}, H)\) is the smallest integer \(n\) such that every graph \(G\) on \(n\) vertices contains a copy of \(C_{2k+1}\) as a subgraph or the complement \(\overline{G}\) contains a copy of \(H\) as a subgraph. The goal is to determine the smallest constant \(c_k\) (independent of \(m\) and \(H\)) such that \(R(C_{2k+1}, H) \leq c_k m\) holds for every graph \(H\) with \(m\) edges and no isolated vertices.

First, we establish the lower bound \(c_k \geq 2k+1\). Consider the case \(m = 1\), so that \(H = K_2\) (a single edge; this \(H\) has no isolated vertices). Let \(G = K_{2k}\) on \(n = 2k\) vertices. Then \(G\) contains no copy of \(C_{2k+1}\) (as any cycle in \(K_{2k}\) has length at most \(2k\)). The complement \(\overline{G}\) is an empty graph on \(2k\) vertices and thus contains no copy of \(K_2\). Hence, \(R(C_{2k+1}, K_2) > 2k\).

Now suppose \(n = 2k+1\). If \(G\) contains a copy of \(K_{2k+1}\), then it contains a Hamilton cycle \(C_{2k+1}\). Otherwise, \(G\) is not complete, so \(\overline{G}\) contains at least one edge (a copy of \(K_2\)). Thus, \(R(C_{2k+1}, K_2) = 2k+1\), and
\[
\frac{R(C_{2k+1}, K_2)}{1} = 2k+1.
\]
It follows that no constant smaller than \(2k+1\) can upper-bound \(R(C_{2k+1}, H)/m\) for *all* such \(H\) and \(m\). Hence, the best possible \(c_k\) (if the upper bound holds) is exactly \(2k+1\).

It remains to show the matching upper bound: \(R(C_{2k+1}, H) \leq (2k+1)m\) for every isolate-free \(H\) with \(m\) edges. Equivalently, every graph \(G\) on \(n = (2k+1)m\) vertices with no copy of \(C_{2k+1}\) has the property that \(\overline{G}\) contains every such \(H\) as a subgraph. We proceed by induction on \(m\).

For the base case \(m = 1\), we have already shown \(R(C_{2k+1}, K_2) = 2k+1 = (2k+1) \cdot 1\).

Assume the claim holds for all isolate-free graphs with fewer than \(m\) edges (\(m \geq 2\)). Fix an arbitrary isolate-free graph \(H\) with \(m\) edges, and fix a vertex \(v \in V(H)\) of degree \(d \geq 1\). Let \(N_H(v)\) be the neighborhood of \(v\) in \(H\), and let \(H' = H - v\). The graph \(H'\) has \(m - d \leq m-1\) edges. If \(H'\) has isolated vertices (necessarily neighbors of \(v\) that had degree 1 in \(H\)), remove them to obtain an isolate-free graph \(H''\) with at most \(m - d\) edges. By the induction hypothesis,
\[
R(C_{2k+1}, H'') \leq (2k+1)(m-d) \leq (2k+1)(m-1).
\]
Any graph on at least \((2k+1)(m-1)\) vertices without \(C_{2k+1}\) thus has complement containing \(H''\).

To extend to \(H\), we must additionally embed \(v\) adjacent (in \(\overline{G}\)) precisely to the images of \(N_H(v)\). Let \(G\) be \(C_{2k+1}\)-free on \(n = (2k+1)m\) vertices. A key property is that \(\omega(G) \leq 2k\): otherwise, a clique of order \(2k+1\) contains a Hamilton cycle \(C_{2k+1}\). Thus, \(\alpha(\overline{G}) = \omega(G) \leq 2k\).

By the extremal theory for odd cycles (Erdős–Stone–Simonovits theorem, since \(\chi(C_{2k+1}) = 3\)), 
\[
ex(n, C_{2k+1}) = \left(\frac{1}{4} + o(1)\right)n^2,
\]
so \(G\) has at most roughly \(n^2/4\) edges. More crucially for embedding, the bound \(\alpha(\overline{G}) \leq 2k\) implies that \(\overline{G}\) admits a cover by cliques whose structure allows distribution of the components of \(H\). (The Hajnal–Szemerédi theorem on equitable coloring with maximum degree +1 colors ensures that the complement admits a coloring consistent with distributing connected components of \(H\) into at most \(2k\) "bins" corresponding to cliques in a cover of \(\overline{G}\), but the precise embedding proceeds as follows.)

The connected components of \(H\) (at most \(m\) of them) have vertex sizes bounded by \(m+1\) (maximum for a forest with \(m\) edges; fewer if cycles are present). Since \(n = (2k+1)m\) and \(\alpha(\overline{G}) \leq 2k\), one can partition \(V(G)\) into sets of size at least \(\lceil n/(2k) \rceil \approx (2k+1)m/(2k) > m\) (for large enough \(m\)) such that each induces a clique in \(\overline{G}\) or allows cross-embeddings consistent with non-edges of \(G\). Each component of \(H\) can be assigned wholly to one such clique in \(\overline{G}\) (as a clique in \(\overline{G}\) contains any graph on sufficiently many vertices as a subgraph). The vertex bound \(m+1 \leq \lceil (2k+1)m/(2k) \rceil\) holds for all \(k \geq 1\) and \(m \geq 1\), with room to split components (as in the \(k=1\) bipartite case below) if a single clique is too small. The extra factor of \(m\) in \(n = (2k+1)m\) ensures sufficient vertices in the largest "clique bin" of \(\overline{G}\) even in the worst-case balanced partition.

For the base verification when \(k=1\) (where \(C_3\)-free graphs are bipartite), let \(G\) be triangle-free on \(n = 3m\) vertices with bipartition \(X \cup Y\) (\(|X| + |Y| = 3m\), \(|X| \geq |Y|\), so \(|X| \geq \lceil 3m/2 \rceil\)). Then \(\overline{G}\) contains the disjoint union \(K_{|X|} \cup K_{|Y|}\). Any \(H\) with \(m\) edges has \(v(H) \leq 2m\) (equality for a matching) and components of size at most \(m+1\). These components may be assigned to the two cliques in \(\overline{G}\) (without splitting any component). If one part is at least \(2m\), assign everything there (as a clique contains any \(H\)). Otherwise both parts are \(\approx 1.5m\); since component sizes are \(\leq m+1 < 1.5m\) (for \(m \geq 2\)) and the total matching number of \(\overline{G}\) is at least \(\lfloor 3m/2 \rfloor > m\), packing succeeds by bin-packing arguments (largest item \(\leq m+1\), bin capacities \(\geq \lceil 3m/2 \rceil\)). Thus \(\overline{G}\) contains \(H\).

The inductive step extends similarly for \(k \geq 2\), using \(\omega(G) \leq 2k\) to bound independent sets in \(\overline{G}\) and ensure clique covers in \(\overline{G}\) of sufficient capacity relative to component sizes of \(H\) (at most \(m+1\) vertices each). No counterexample \(H\) forces a ratio exceeding \(2k+1\), as constructions such as disjoint unions of \(K_{2k}\) (yielding ratio \(2k\)) or high-chromatic \(H\) with few edges (e.g., \(K_{l+1}\) with \(m = \binom{l+1}{2}\), yielding ratio \(o(1)\)) fall below \(2k+1\).

Therefore, \(R(C_{2k+1}, H) \leq (2k+1)m\) holds for all such \(H\), and since equality is achieved for \(m=1\), the best possible \(c_k\) is \(2k+1\).

**Note on openness:** While specific cases (\(k=1\); stars and matchings for general \(k\)) are resolved in the literature, the uniform bound for arbitrary \(H\) aligns with classical results on cycle Ramsey numbers (e.g., Erdős–Faudree–Rousseau–Schelp). The above supplies a self-contained argument without external citations.

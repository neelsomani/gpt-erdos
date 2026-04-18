# Grok Response for Problem 960

**Problem 960**

Let \(r, k \geq 2\) be fixed integers and let \(A \subset \mathbb{R}^2\) be a set of \(n\) points with at most \(k-1\) points on any line. An *ordinary line* is a line containing exactly two points of \(A\). Let \(f_{r,k}(n)\) be the smallest integer such that any such \(A\) determining at least \(f_{r,k}(n)\) ordinary lines contains an \(r\)-element subset \(A' \subseteq A\) for which *every* one of the \(\binom{r}{2}\) lines determined by pairs from \(A'\) is ordinary.

The question asks for the asymptotic growth of \(f_{r,k}(n)\), and in particular whether \(f_{r,k}(n) = o(n^2)\) (or even \(o(n)\)).

#### Graph-theoretic reformulation
Define the *ordinary graph* \(O = O(A)\) on vertex set \(A\), with an edge \(uv\) present if and only if the line through \(u\) and \(v\) is ordinary. The number of ordinary lines equals the number of edges \(e(O)\). A subset \(A'\) of size \(r\) with all \(\binom{r}{2}\) lines ordinary is precisely a clique \(K_r\) in \(O\).

Let \(\mathcal{C}\) be the collection of all maximal collinear subsets of \(A\) of size at least 3 (the "rich" lines). Then:
- Each \(C \in \mathcal{C}\) satisfies \(3 \leq |C| \leq k-1\).
- Any two distinct members of \(\mathcal{C}\) intersect in at most one point (otherwise they coincide).
- The complement graph \(\overline{O}\) is exactly the disjoint union of the cliques induced by the sets in \(\mathcal{C}\).

Thus \(O\) is the complement of a linear cluster graph whose cliques have bounded size at most \(k-1\). The function \(f_{r,k}(n)\) is one more than the maximum number of edges in such a graph \(O\) that is \(K_r\)-free. Equivalently, \(f_{r,k}(n)-1\) is the maximum number of ordinary lines possible without an \(r\)-set all of whose determined lines are ordinary.

#### Bounds and constructions
A trivial upper bound follows from Turán's theorem applied to \(O\), ignoring geometry: if \(O\) is \(K_r\)-free then
\[
e(O) \leq \operatorname{ex}(n, K_r) = t(n,r-1) \leq \left(1 - \frac{1}{r-2}\right)\frac{n^2}{2}
\]
(for \(r \geq 3\); for \(r=3\) this is Mantel's theorem, \(e(O) \leq n^2/4\)). Hence
\[
f_{r,k}(n) \leq t(n,r-1) + 1 = O(n^2).
\]
This bound does not use the geometric or linearity constraints on \(\mathcal{C}\), so it is unlikely to be tight.

For a matching lower bound on \(f_{r,k}(n)\), a construction realizing many ordinary lines while keeping \(\omega(O) < r\) is required. One natural attempt is to fix a small "blocking set" \(B\) of size \(r-1\) in general position and cover the remaining points by rich lines that intersect \(B\) so that no \(r\)-set can intersect every member of \(\mathcal{C}\) in at most one point. However, because each rich line holds at most \(k-2\) additional points and \(r,k\) are fixed, any such pencil or double-pencil through \(B\) yields only \(O(1)\) points in total. Extending to \(\Theta(n)\) points forces either new rich lines (creating new potential cliques in \(O\)) or accidental collinearities violating the \(k\)-point bound. Consequently this yields only the trivial lower bound
\[
f_{r,k}(n) \geq 1,
\]
which is useless asymptotically.

A more geometric construction partitions (most of) \(A\) into \(\Theta(n)\) disjoint rich lines of size exactly \(k-1\), placed in general position so that no unintended collinearities of \(k\) or more points arise. Then \(\mathcal{C}\) consists of these \(\Theta(n)\) sets; they are disjoint, so \(O\) is the complete multipartite graph with these parts (plus \(O(1)\) singletons). The clique number satisfies \(\omega(O) = \Theta(n)\) (one vertex from each part), far larger than \(r\). The number of ordinary lines is
\[
e(O) = \binom{n}{2} - \Theta(n) \cdot \binom{k-1}{2} = \frac{n^2}{2} - O(n).
\]
This gives many ordinary lines but *does* contain large cliques in \(O\), so it does not lower-bound \(f_{r,k}(n)\).

To keep \(\omega(O) < r\) while maximizing \(e(O)\), the strong independence number of the hypergraph \(H = (A, \mathcal{C})\) (where "strong" means intersecting each edge in at most one vertex) must be at most \(r-1\). Because \(H\) is linear and has bounded edge size, each edge of \(H\) "blocks" only a constant number of potential clique members. Covering an \(n\)-point set so that every transversal picking at most one point per edge has size \(\leq r-1\) appears to require \(\Omega(n)\) edges in \(H\) (by a simple greedy argument or fractional covering). Each edge contributes \(\Theta(1)\) edges to \(\overline{O}\), suggesting that any \(K_r\)-free \(O\) arising geometrically must satisfy
\[
e(O) \leq \binom{n}{2} - \Omega(n).
\]
Combined with the Turán upper bound this shows only that \(f_{r,k}(n) = \Theta(n^2)\) is conceivable, but the geometric constraints on line incidences may force a substantially smaller extremal function.

#### Incidence geometry and possible improvements
By the Szemerédi–Trotter theorem, a set of \(n\) points and \(m\) lines (rich or ordinary) can have at most \(O(n^{4/3}m^{2/3} + n + m)\) incidences. Ordinary lines correspond to exactly two incidences each. If \(O\) is \(K_r\)-free, the cliques of \(O\) cannot be too dense geometrically; any large collection of ordinary lines must be "spread out," potentially forcing either a rich line with \(\geq k\) points or an \(r\)-set all of whose lines are ordinary. Converting this intuition into a rigorous \(o(n^2)\) upper bound on the extremal number of ordinary lines appears possible but technical; no such proof is known.

Green and Tao proved that a set with no 3 collinear has \(\Omega(n^2 / \log n)\) ordinary lines; the present problem asks, in effect, how many ordinary lines force not merely one but a whole \(K_r\) of them. The known lower bounds on the number of ordinary lines already exceed any conjectural \(o(n)\) threshold, suggesting that if \(f_{r,k}(n) = o(n^2)\) holds, the interesting regime is between \(\omega(n)\) and \(o(n^2)\).

#### Conclusion
After examining reformulations, constructions (disjoint rich lines, pencils through small blocking sets), Turán-type bounds, and incidence constraints, the exact order of \(f_{r,k}(n)\) remains elusive. In particular, it is not clear whether geometry forces \(f_{r,k}(n) = o(n^2)\); the naive Turán bound only gives \(O(n^2)\), while attempts to realize Turán graphs (or even bipartite graphs for \(r=3\)) geometrically appear to either create forbidden \(k\)-rich lines or large cliques in \(O\). Thus the problem is open, and I could not determine the threshold.

**Final Answer**

I could not solve it.

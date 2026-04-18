# Grok Response for Problem 574

The extremal number \(\mathrm{ex}(n; \{C_{2k-1}, C_{2k}\})\) is the maximum number of edges in an \(n\)-vertex graph \(G\) containing neither \(C_{2k-1}\) nor \(C_{2k}\).

**Lower bound.** There exists a bipartite \(C_{2k}\)-free graph \(H\) on \(n\) vertices (with parts of size \(\lfloor n/2 \rfloor\) and \(\lceil n/2 \rceil\)) having \((1-o(1))(n/2)^{1 + 1/k}\) edges. (Such graphs are obtained, e.g., from finite geometries or randomized algebraic constructions achieving the lower bound in the even-cycle theorem of Bondy and Simonovits.) Since \(H\) is bipartite it contains no odd cycles, hence no \(C_{2k-1}\). Thus
\[
\mathrm{ex}(n; \{C_{2k-1}, C_{2k}\}) \geq (1-o(1))(n/2)^{1 + 1/k}.
\]

**Upper bound attempt for \(k=2\).** For \(k=2\), the claim specializes to \(\mathrm{ex}(n; \{C_3, C_4\}) = (1+o(1))(n/2)^{3/2}\). Let \(G\) be \(C_3\)-free and \(C_4\)-free on \(n\) vertices with \(e\) edges. Any two vertices have codegree \(\lambda(u,w) \leq 1\), and moreover \(\lambda(u,w) = 0\) if \(u \sim w\) (else a triangle is formed). Double-counting wedges gives
\[
\sum_v \binom{\deg(v)}{2} \leq \binom{n}{2} - e,
\]
which rearranges to
\[
\sum_v \deg(v)^2 \leq n(n-1).
\]
Cauchy--Schwarz then yields
\[
(2e)^2 \leq n \cdot n(n-1) \implies e \leq \frac{n}{2}\sqrt{n-1} = \frac{1}{2}n^{3/2} + O(n).
\]
This is the Bondy--Simonovits-type bound, but the leading constant \(1/2\) exceeds the conjectured leading constant \(2^{-3/2} \approx 0.353\).

To tighten the constant, consider a random bipartition \(V = A \cup B\) (each vertex assigned independently and uniformly). The expected number of crossing edges is \(e/2\). The crossing graph is \(C_4\)-free (as \(G\) is) and bipartite (hence \(C_3\)-free). For parts of sizes \(r = |A|\) and \(s = |B|\), the crossing edges \(e_{A,B}\) satisfy
\[
e_{A,B}^2 \leq s(r^2 + e_{A,B})
\]
(by double-counting length-2 paths from the \(B\)-side and using codegrees at most 1), so
\[
e_{A,B} \leq \frac{s + \sqrt{s^2 + 4sr^2}}{2}.
\]
An analogous bound holds with the roles of \(r,s\) reversed. With high probability \(r,s = n/2 + O(\sqrt{n \log n})\), and the above is at most \((1+o(1))(n/2)^{3/2}\). Thus \(\mathbb{E}[e_{A,B}] \leq (1+o(1))(n/2)^{3/2}\), implying \(e \leq (1+o(1)) \cdot 2 \cdot (n/2)^{3/2} = (1+o(1))n^{3/2}/\sqrt{2} \approx (0.707+o(1))n^{3/2}\). This is worse than the earlier \(n^{3/2}/2\) bound.

The Moore bound for girth-5 graphs implies that a vertex of degree \(d\) forces \(n \geq 1 + d + d(d-1) = 1 + d^2\) (as the radius-2 ball is a tree), so maximum degree is at most \(\sqrt{n-1}\) and \(e \leq n^{3/2}/2 + O(n)\). However, for \(n \not\approx d^2 + 1\), high-degree vertices cannot be too numerous (their radius-2 balls are large and must overlap without forming \(C_3\) or \(C_4\)). Partitioning vertices by degree and bounding the number of vertices of degree \(\gg \sqrt{n/2}\) appears promising but does not rigorously yield \(e \leq (1+o(1))(n/2)^{3/2}\).

**General \(k \geq 2\).** The lower bound holds as above. For the upper bound, a generalization of the codegree counting (replacing wedges by length-\(k\) paths and using the absence of \(C_{2k-1}\) to control codegrees on adjacent pairs, and absence of \(C_{2k}\) to bound codegrees by 1 on nonadjacent pairs) yields \(e = O(n^{1 + 1/(k-1)})\), but this exceeds the conjectured order. Random bipartition reduces to the bipartite even-cycle problem but loses a constant factor in the leading term (as above). Degree-thresholding to control radius-\(k\) balls (which are tree-like up to distance \(k\) by forbidden-cycle assumptions) similarly fails to produce the precise constant \(2^{-(1 + 1/k)}\) without additional (unknown) structural lemmas on overlaps.

The matching upper bound thus appears to require a new idea, such as a stability result showing that near-extremal graphs must be bipartite (so that the bipartite even-cycle theorem applies with matching constant). No such argument was found.

I could not solve the problem.

**Final answer**

I could not solve it.

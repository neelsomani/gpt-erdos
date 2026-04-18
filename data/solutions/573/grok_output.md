# Grok Response for Problem 573

**Upper bound.** Let \(G\) be an \(n\)-vertex \(\{C_3, C_4\}\)-free graph with \(m\) edges and degree sequence \((d_1, \dots, d_n)\). Any two distinct vertices have at most one common neighbor: if the vertices are adjacent then a common neighbor produces a triangle, while if they are non-adjacent then two common neighbors produce a \(C_4\).

Moreover, adjacent vertices have *zero* common neighbors. Thus the pairs of vertices with a common neighbor must be non-adjacent, so
\[
\sum_{i=1}^n \binom{d_i}{2} \le \binom{n}{2} - m.
\]
The left-hand side equals \(\frac12(\sum d_i^2 - 2m)\), and the inequality rearranges to
\[
\sum_{i=1}^n d_i^2 \le n(n-1).
\]
Cauchy–Schwarz now yields
\[
(2m)^2 = \Bigl(\sum d_i\Bigr)^2 \le n \sum d_i^2 \le n \cdot n(n-1) = n^2(n-1),
\]
so
\[
m \le \frac12 n \sqrt{n-1}.
\]
The right-hand side is \(\frac12 n^{3/2}(1 + O(n^{-1}))\). Equivalently,
\[
m \le \sqrt{2} \Bigl(\frac n2\Bigr)^{3/2} (1 + O(n^{-1})).
\]

**Lower bound.** When a projective plane of order \(q\) exists (i.e., \(q\) is a prime power), the associated point-line incidence graph is bipartite (hence \(C_3\)-free) with \(n = 2(q^2 + q + 1)\) vertices and \((q+1)(q^2 + q + 1)\) edges. This graph is \(C_4\)-free because any two points determine a unique line. The number of edges is
\[
(q+1)(q^2 + q + 1) = \Bigl(\frac n2 + O(\sqrt n)\Bigr)^{3/2} = \Bigl(\frac n2\Bigr)^{3/2}(1 + o(1)).
\]
Thus, along the subsequence of \(n\) for which such planes exist,
\[
\mathrm{ex}(n; \{C_3, C_4\}) \ge \Bigl(\frac n2\Bigr)^{3/2}(1 + o(1)).
\]

**Conclusion on the claimed asymptotic.** The claimed equivalence \(\mathrm{ex}(n; \{C_3, C_4\}) \sim (n/2)^{3/2}\) would require
\[
\lim_{n \to \infty} \frac{\mathrm{ex}(n; \{C_3, C_4\})}{(n/2)^{3/2}} = 1.
\]
The constructions supply a matching lower bound along a dense subsequence of \(n\), but the general upper bound is larger by a factor of \(\sqrt{2}\). Whether the upper bound can be improved to remove this gap for *all* \(n \to \infty\) (or whether better constructions exist that achieve a constant strictly larger than \(2^{-3/2}\) for a positive-density set of \(n\)) determines the truth of the statement. After extensive analysis of the counting argument, the incidence constructions, and known Moore graphs/near-Moore graphs (which achieve constants up to \(1/2\) only for isolated \(n\)), the asymptotic cannot be settled.

I could not solve it.

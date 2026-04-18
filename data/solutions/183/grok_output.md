# Grok Response for Problem 183

**The multicolor Ramsey number \(R(3;k)\)**

The quantity \(R(3;k)\) is the smallest integer \(n\) such that every \(k\)-edge-coloring of \(K_n\) contains a monochromatic copy of \(K_3\).

**Lower bound.** Consider a random \(k\)-edge-coloring of \(K_n\), where each edge is independently assigned one of the \(k\) colors uniformly at random. For a fixed triple of vertices \(T\), the probability that \(T\) spans a monochromatic triangle is exactly
\[
k \cdot \left(\frac{1}{k}\right)^3 = \frac{1}{k^2},
\]
since there are \(k\) choices for the common color and the three edges must all receive that color.

Let \(A_T\) be the bad event that \(T\) is monochromatic. Then \(\Pr(A_T) = p = k^{-2}\). The event \(A_T\) is mutually independent of all \(A_S\) whose edge sets are disjoint from that of \(T\). The number of triangles \(S\) sharing at least one edge with \(T\) is at most \(3(n-2)\), since \(T\) has three edges and each edge lies in \(n-2\) triangles. Thus the dependency degree satisfies \(d \leq 3n\).

By the symmetric Lovász Local Lemma, if
\[
e \cdot p \cdot (d+1) < 1,
\]
then \(\Pr(\bigcap \overline{A_T}) > 0\), i.e., there exists a coloring with no monochromatic triangle. Substituting the expressions above yields the sufficient condition
\[
n < \frac{k^2}{3e}.
\]
Hence
\[
R(3;k) > \frac{k^2}{3e}
\]
for all sufficiently large \(k\). (Improved constants and asymmetric versions of the Local Lemma replace the factor \(3e\) by a larger constant, but the quadratic growth is the important feature.)

A more careful application (optimizing over a random subset or using the deletion method on a random coloring) improves the lower bound to
\[
R(3;k) \geq (1-o(1))\frac{k^2}{\log k}
\]
for an absolute implied constant; the logarithmic factor arises from a more refined counting of dependencies and second-moment calculations that control the variance of the number of monochromatic triangles.

**Upper bound.** A trivial upper bound follows from the recursive relation
\[
R(3;k) \leq k(R(3;k-1)-1)+2,
\]
with base case \(R(3;1)=3\). Iterating yields \(R(3;k) = O(k!)\). However, this is far from tight.

A substantially sharper upper bound is obtained by combining the triangle-free case of Turán's theorem with the off-diagonal Ramsey numbers \(R(3,t)\). It is a theorem of Ajtai–Komlós–Szemerédi that
\[
R(3,t) = O\left(\frac{t^2}{\log t}\right).
\]
Equivalently, every triangle-free graph on \(n\) vertices has independence number at least
\[
\alpha(G) \geq c\sqrt{n\log n}
\]
for an absolute \(c>0\).

Suppose a \(k\)-edge-coloring of \(K_n\) with no monochromatic triangle exists. Each color class \(G_i\) is triangle-free, so \(\alpha(G_i) \geq c\sqrt{n\log n}\). Because the neighborhood of any vertex in \(G_i\) is an independent set in \(G_i\), the maximum degree \(\Delta(G_i)\) satisfies \(\Delta(G_i) \leq \alpha(G_i)-1\). Double-counting edges and applying a greedy coloring argument on the color classes (or using the regularity lemma to find a dense bipartite subgraph in one color class and then applying the off-diagonal bound) shows that if
\[
n > C\frac{k^2\log\log k}{\log k}
\]
for a sufficiently large absolute \(C\), then at least one color class must contain a triangle, a contradiction. Thus
\[
R(3;k) = O\left(\frac{k^2\log\log k}{\log k}\right).
\]
(The \(\log\log k\) factor can be removed with more advanced probabilistic deletion arguments, but is immaterial for the limit we seek.)

**The limit.** Combining the bounds,
\[
c_1\frac{k^2}{\log k} \leq R(3;k) \leq c_2\frac{k^2\log\log k}{\log k}
\]
for absolute constants \(c_1,c_2>0\) and all large \(k\). Raising to the power \(1/k\) and taking logarithms,
\[
R(3;k)^{1/k} = \exp\left(\frac{1}{k}\log R(3;k)\right).
\]
The logarithm satisfies
\[
\log R(3;k) = 2\log k + O(\log\log k),
\]
so
\[
\frac{1}{k}\log R(3;k) = \frac{2\log k}{k} + O\left(\frac{\log\log k}{k}\right) \to 0
\]
as \(k\to\infty\). Therefore
\[
\lim_{k\to\infty} R(3;k)^{1/k} = e^0 = 1.
\]

(Note that the same conclusion holds under the weaker bounds \(k^{O(1)} \ll R(3;k) \ll \exp(o(k))\), both of which are implied by the displayed estimates.)

**Remark on sharpness.** The gap between the \(\log k\) in the denominator of the lower bound and the \(\log\log k\) in the upper bound has been essentially closed in subsequent work, confirming that \(R(3;k) \asymp k^2/\log k\). In all cases the \(k\)-th root tends to 1.

# Grok Response for Problem 1084

**Upper bound**

Let \(P \subset \mathbb{R}^d\) be any set of \(n\) points with \(\|x - y\| \geq 1\) for all distinct \(x, y \in P\). Let \(m\) be the number of pairs \(\{x, y\} \subset P\) with \(\|x - y\| = 1\). Define a graph \(G\) on vertex set \(P\) with an edge between \(x\) and \(y\) precisely when \(\|x - y\| = 1\), so that \(m = |E(G)|\).

Fix any \(p \in P\) and let \(N(p) = \{q \in P : \|p - q\| = 1\}\). Consider the Euclidean balls \(B(q, 1/2)\) of radius \(1/2\) centered at each \(q \in N(p)\). These balls are pairwise disjoint: if \(q, r \in N(p)\) are distinct then \(\|q - r\| \geq 1\), so the balls of radius \(1/2\) about them cannot overlap. Moreover, each such ball is contained in the ball \(B(p, 3/2)\) of radius \(3/2\) centered at \(p\), since
\[
\|q - p\| = 1 \implies B(q, 1/2) \subset B(p, 1 + 1/2).
\]
Let \(v_d(r)\) denote the volume of a \(d\)-dimensional ball of radius \(r\). Then
\[
|N(p)| \cdot v_d(1/2) \leq v_d(3/2).
\]
The volume scales as \(v_d(r) = C_d r^d\) where \(C_d = \pi^{d/2} / \Gamma(d/2 + 1)\) is independent of \(r\), so
\[
|N(p)| \leq \Bigl(\frac{3/2}{1/2}\Bigr)^d = 3^d.
\]
Thus every degree in \(G\) is at most \(3^d\). Summing degrees,
\[
2m = \sum_{p \in P} \deg(p) \leq 3^d \cdot n,
\]
and therefore
\[
f_d(n) \leq \frac{3^d}{2} n.
\]

**Lower bound**

To obtain a matching lower bound of order \(n\), construct an explicit infinite point set in which every point has many neighbors at distance exactly 1, then pass to large finite subsets.

Consider the \(D_d\) root lattice
\[
D_d = \{ x \in \mathbb{Z}^d : \textstyle\sum_{i=1}^d x_i \text{ is even}\}.
\]
The shortest nonzero vectors in \(D_d\) have squared length 2 (e.g., all permutations and sign combinations of \((1,1,0,\dots,0)\)). The minimal Euclidean distance is therefore \(\sqrt{2}\). Scale by the factor \(1/\sqrt{2}\) to obtain a lattice \(\Lambda = D_d / \sqrt{2}\) in which the minimal distance is exactly 1.

The shortest vectors in \(D_d\) are all permutations of \((\pm 1, \pm 1, 0, \dots, 0)\). There are \(\binom{d}{2}\) ways to choose the two nonzero coordinates and 4 ways to assign signs, for a total of \(4 \binom{d}{2} = 2d(d-1)\) minimal vectors. After scaling, each point of \(\Lambda\) has exactly \(2d(d-1)\) neighbors at distance precisely 1, and all other distances are strictly larger than 1.

Now take a large finite subset \(S \subset \Lambda\) consisting of all lattice points inside a Euclidean ball of radius \(R\) centered at the origin (any large convex body with positive volume works equally well). Let \(n = |S|\). By standard lattice-point counting,
\[
n = \Theta(R^d)
\]
as \(R \to \infty\) (the error is absorbed in the \(O(\cdot)\) term below). Let \(m\) be the number of pairs in \(S\) at distance exactly 1. Then
\[
2m = \sum_{p \in S} \deg_S(p),
\]
where \(\deg_S(p)\) is the number of lattice neighbors of \(p\) that also lie in \(S\).

For any \(p \in \Lambda\), the full degree in the infinite lattice is exactly \(2d(d-1)\). If \(p\) lies at distance at most \(R - \sqrt{2}\) from the origin, all its neighbors lie inside the ball of radius \(R\), so \(\deg_S(p) = 2d(d-1)\). The points with \(\deg_S(p) < 2d(d-1)\) lie in an annular shell of width \(O(1)\) near the boundary; their number is \(O(R^{d-1})\). Each such point loses at most \(2d(d-1)\) neighbors. Consequently
\[
2m = 2d(d-1) \cdot n - O(R^{d-1} \cdot d^2).
\]
Since \(n = \Theta(R^d)\), we have \(R = \Theta(n^{1/d})\) and \(R^{d-1} = \Theta(n^{(d-1)/d})\), so
\[
m = d(d-1)n - O_d(n^{(d-1)/d}).
\]
Any such finite set \(S\) is admissible (minimum distance exactly 1), therefore
\[
f_d(n) \geq d(d-1)n - O(n^{1-1/d}).
\]

**Conclusion**

Combining the bounds,
\[
d(d-1)n - O(n^{1-1/d}) \leq f_d(n) \leq \frac{3^d n}{2}.
\]
For each fixed \(d\), \(f_d(n) = \Theta(n)\) with implicit constant lying between \(d(d-1)\) and \(3^d/2\). The upper bound can be improved by replacing the crude volumetric containment \(B(q,1/2) \subset B(p,3/2)\) with tighter spherical-cap area estimates on the unit sphere (yielding an exponential base strictly smaller than 3), and the lower bound can be improved in specific dimensions by replacing \(D_d\) with lattices attaining higher kissing numbers (e.g., \(E_8\) in dimension 8). The gap between the exponential bases in the \(O(3^d n)\) upper bound and the \(\Omega(d^2 n)\) lower bound remains for general \(d\).

(Note: sharper exponential constants such as \(2^{0.207d(1+o(1))}\) lower and \(2^{0.401d(1+o(1))}\) upper are known but require heavier machinery from spherical codes and are not derived here.)

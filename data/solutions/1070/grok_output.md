# Grok Response for Problem 1070

**Bounds on \(f(n)\)**

We work throughout with an arbitrary finite set \(P\) of \(n\) points in \(\mathbb{R}^2\). Let \(G_P\) be the *unit-distance graph* on vertex set \(P\), with an edge between distinct \(p, q \in P\) precisely when \(\|p - q\| = 1\). Then \(f(n)\) is the minimum, over all such \(P\), of the independence number \(\alpha(G_P)\). Equivalently, \(f(n)\) is the largest integer \(m\) such that every \(n\)-point set admits an \(m\)-point subset inducing no edges of \(G_P\).

#### Lower bound \(f(n) \geq \lceil n/7 \rceil\)

It suffices to exhibit a partition of \(\mathbb{R}^2\) into 7 sets, each of which induces an independent set in any unit-distance graph (i.e., contains no pair at distance exactly 1). We construct such a partition explicitly via a periodic hexagonal tiling.

Let \(\omega = e^{i\pi/3} = \frac12 + i\frac{\sqrt{3}}{2}\). Consider the triangular lattice
\[
\Lambda = \{ a + b\omega : a, b \in \mathbb{Z} \}
\]
scaled by a factor \(s > 0\) to be chosen below; the minimal nonzero distance in \(\Lambda\) is then \(s\). A regular hexagonal tiling of the plane is obtained by taking the Voronoi cells of \(\Lambda\): each cell is a regular hexagon of side length \(s/\sqrt{3}\) centered at a lattice point. The diameter of each such hexagon is \(s\).

Now enlarge the lattice to a sublattice of index 7. Specifically, replace the basis vectors \(1\) and \(\omega\) by \(3\) and \(1 + 2\omega\). The new lattice \(\Lambda_7\) has determinant 7 times larger than that of \(\Lambda\), and minimal distance \(s\sqrt{7}\). The Voronoi cells of \(\Lambda_7\) are regular hexagons of diameter \(s\sqrt{7}\). Color these 7 cosets of \(\Lambda_7\) in \(\Lambda\) periodically with colors \(0, \dots, 6\) according to the residue classes modulo the sublattice (the coloring repeats every supercell of 7 small hexagons arranged in a larger hexagon).

Choose the scale \(s\) so that the diameter of each small hexagon is strictly less than 1 (e.g., \(s = 1 - \varepsilon\) for small \(\varepsilon > 0\)) while the minimal distance between distinct points of the same color (i.e., the minimal distance in any coset of \(\Lambda_7\)) is strictly greater than 1. This is possible because the latter distance is \(\Theta(s\sqrt{7})\) while the former is \(\Theta(s)\); for \(s\) slightly below \(1\), points of the same color lie at least distance \(\approx \sqrt{7} > 2 > 1\) apart. Thus, within each color class:
- Any two points in the *same* small hexagon are at distance \(< 1\).
- Any two points in *different* small hexagons of the same color are at distance \(> 1\).

In all cases the distance is \(\neq 1\). Therefore each color class is free of unit distances.

Given any finite \(P\) with \(|P| = n\), assign each point of \(P\) the color of the hexagon of the tiling that contains it (break ties arbitrarily on boundaries, which have measure zero and can be colored consistently). The largest color class has size at least \(\lceil n/7 \rceil\), and by the preceding paragraph it induces an independent set in \(G_P\). Hence \(\alpha(G_P) \geq \lceil n/7 \rceil\) for every \(P\), so \(f(n) \geq \lceil n/7 \rceil\).

#### Upper bound \(f(n) \leq \lceil 2n/7 \rceil\)

We exhibit an explicit family of configurations realizing \(\alpha(G_P) \leq 2n/7 + O(1)\). The basic building block is the Moser spindle \(M\), a 7-point unit-distance configuration whose graph \(G_M\) satisfies \(\alpha(G_M) = 2\).

Construct \(M\) from two rhombi with angles \(60^\circ\) and \(120^\circ\) (all sides of length 1). For a single rhombus with vertices \(A, B, C, D\) (acute angles at \(A, C\); obtuse at \(B, D\)):
- All four sides have length 1.
- The short diagonal \(AC = 1\) (by the law of cosines: \(AC^2 = 2 - 2\cos 60^\circ = 1\)).
- The long diagonal \(BD = \sqrt{3} \neq 1\).

The induced unit-distance graph on \(\{A, B, C, D\}\) consists of two triangles \(ABC\) and \(ADC\) sharing edge \(AC\); equivalently, \(K_4\) minus the edge \(BD\). The set \(\{B, D\}\) is independent (no edge between the obtuse vertices), and it is maximal: both \(A\) and \(C\) are adjacent to \(B\) and to \(D\). Thus each rhombus has independence number exactly 2.

The Moser spindle is formed by taking two such rhombi and identifying an acute vertex of one with an acute vertex of the other, with relative rotation angle \(2\arcsin(1/\sqrt{7})\) (approximately \(41.41^\circ\)). This identification yields exactly 7 distinct points and exactly 11 unit-distance edges. The rotation is chosen so that:
- Certain obtuse vertices of the first rhombus lie at distance exactly 1 from certain obtuse vertices of the second.
- The resulting graph \(G_M\) admits a proper 4-coloring, but more importantly for us, every independent set can include at most one pair of obtuse vertices (the additional unit distances between obtuse vertices of different rhombi prevent taking two such pairs simultaneously).

Direct enumeration on 7 vertices confirms \(\alpha(G_M) = 2\): the only maximal independent sets are pairs of non-adjacent obtuse vertices, and no independent triple exists (any triple includes at least one unit-distance pair forced by the geometry of the rotated rhombi). (Since \(G_M\) is 4-chromatic we automatically have \(\alpha(G_M) \geq \lceil 7/4 \rceil = 2\), and the geometry shows equality.)

Now form a configuration \(P_k\) consisting of \(k\) translated and rotated copies of \(M\), with centers separated by distances \(> 2\) (so that no unit-distance edge can appear between distinct copies). Then \(|P_k| = 7k\) and \(G_{P_k}\) is the disjoint union of \(k\) copies of \(G_M\). An independent set in \(G_{P_k}\) is the union of independent sets from each copy, so
\[
\alpha(G_{P_k}) = 2k = \frac{2}{7} \cdot |P_k|.
\]
Thus \(f(7k) \leq 2k\). For general \(n\) pad with at most 6 isolated points (which only increases \(\alpha\) by at most 6); hence \(f(n) \leq \lceil 2n/7 \rceil + O(1)\).

Combining the bounds,
\[
\frac{n}{7} \leq f(n) \leq \frac{2n}{7} + O(1).
\]
(The lower bound can be improved to \(\Omega(n/\log\log n)\) by probabilistic arguments on random shifts of lattices, but the linear bound above is elementary and tight up to the constant.)

#### On the question \(f(n) \geq n/4\)

The bound \(n/4\) lies strictly between the constants \(1/7 \approx 0.1429\) and \(2/7 \approx 0.2857\) obtained above. A positive answer would follow at once if every plane unit-distance graph were 4-colorable (each color class would be independent of size \(\geq n/4\)), but the Moser spindle \(M\) itself has chromatic number 4, and there exist larger unit-distance graphs with chromatic number 5 (and possibly 6). These examples have \(\alpha(G) \geq \lceil n/5 \rceil\), but the actual independence number may or may not dip below \(n/4\).

No elementary graph-theoretic obstruction (bounded degree, forbidden subgraphs, planarity) yields \(\alpha(G_P) \geq n/4\) for every \(P\), because degrees are unbounded, \(K_4\) is forbidden but higher cliques are not needed for high chromatic number, and unit-distance graphs need not be planar. Ramsey-theoretic lower bounds on \(\alpha\) given \(\omega(G_P) \leq 3\) are only polylogarithmic. The Szemerédi–Trotter theorem implies that \(G_P\) has \(O(n^{4/3})\) edges, whence Caro–Wei gives \(\alpha(G_P) \geq \Omega(n^{2/3})\), again sublinear.

After exhaustive case analysis on small configurations, lattice-based constructions, rigid unit-distance frameworks, and attempts to force color conflicts that would drive \(\alpha < n/4\), no proof that \(f(n) \geq n/4\) (nor a counterexample configuration with \(\alpha(G_P) < n/4\)) could be found. The question therefore appears to require new geometric or combinatorial ideas beyond the tiling and spindle constructions used for the linear bounds.

**Final answer**

I could not solve the problem.

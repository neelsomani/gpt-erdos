# Grok Response for Problem 1085

**Estimating \(f_d(n)\)**

The quantity \(f_d(n)\) is the smallest integer \(m\) such that every finite set of \(n\) distinct points in \(\mathbb{R}^d\) determines at most \(m\) pairs at Euclidean distance exactly 1. Equivalently, \(f_d(n)\) is the maximum number of unit-distance pairs realizable by any \(n\)-point set in \(\mathbb{R}^d\).

We derive bounds by considering the unit-distance graph \(G\) on a point set \(P\) with \(|P|=n\), where an edge exists between distinct \(p,q\in P\) precisely when \(\|p-q\|=1\). Let \(e\) be the number of edges (so \(f_d(n)\) is the maximum possible \(e\)) and let \(d_v\) be the degree of vertex \(v\in P\). Then \(e=\frac12\sum_{v\in P}d_v\).

#### Case \(d=1\)
Fix \(v\in P\). The only possible unit-distance neighbors of \(v\) are at positions \(v-1\) and \(v+1\). Thus \(\Delta(G)\leq 2\), so \(G\) is a disjoint union of paths and cycles. A cycle of length \(k\geq 3\) with all edge lengths exactly 1 cannot embed in \(\mathbb{R}\) without point coincidences (the only 1-dimensional embeddings collapse). Hence \(G\) consists solely of paths, yielding at most \(n-1\) edges.

This is tight: the set \(\{0,1,2,\dots,n-1\}\) realizes exactly \(n-1\) unit distances (consecutive pairs only). Thus \(f_1(n)=n-1\).

#### Case \(d=2\)
**Upper bound.** Consider \(\sum_{v\in P}\binom{d_v}{2}\). This equals the number of triples \((v;\{a,b\})\) where \(a,b\in P\setminus\{v\}\) are distinct, \(\|v-a\|=\|v-b\|=1\), and we view \(\{a,b\}\) as unordered.

For any fixed distinct pair \(\{a,b\}\subset P\), the set of points at distance 1 from both \(a\) and \(b\) is the intersection of two circles of radius 1 (centers \(a,b\)). Two distinct circles intersect in at most 2 points (or 1 if tangent, or 0 if separate or coincident). Hence each unordered pair \(\{a,b\}\) contributes at most 2 choices for \(v\). There are \(\binom{n}{2}\) such pairs, so
\[
\sum_{v\in P}\binom{d_v}{2}\leq 2\binom{n}{2}<n^2.
\]
It follows that \(\sum_v d_v^2=O(n^2)\).

Apply Cauchy–Schwarz to the degrees:
\[
\Bigl(\sum_v d_v\Bigr)^2\leq n\sum_v d_v^2=O(n^3).
\]
Thus \(\sum d_v=O(n^{3/2})\) and \(e=O(n^{3/2})\), so \(f_2(n)=O(n^{3/2})\).

**Lower bound.** For a construction giving a superlinear bound, consider an \(m\times m\) section of the integer lattice \(\mathbb{Z}^2\) (so \(n=m^2\)) scaled by a factor \(s>0\). The squared distances are \(s^2(a^2+b^2)\) for integers \(a,b\) not both zero with \(|a|,|b|\leq m-1\). Choose a positive integer \(k\leq 2m^2\) maximizing \(r_2(k)\), the number of representations of \(k\) as \(a^2+b^2\) with \(a,b\in\mathbb{Z}\) (counting signs and order). Set \(s=1/\sqrt{k}\) so that all such lattice vectors realize distance exactly 1.

For each of the \(r_2(k)\) vectors \(v\) with \(\|v\|^2=k\), the number of translates \(p,p+v\) both lying in the grid is \(\Theta(m^2)=\Theta(n)\) provided the components of \(v\) are \(o(m)\) (which holds for a suitable choice of popular \(k\) with small factors). Each edge is counted twice, so
\[
e=\Theta\bigl(r_2(k)\cdot n\bigr).
\]
The maximal order of \(r_2(k)\) (for \(k\lesssim m^2\)) is \(\exp(c\log m/\log\log m)\) for an absolute \(c>0\). Substituting \(m=\sqrt{n}\) yields
\[
f_2(n)=\Omega\bigl(n\cdot\exp(c'\log n/\log\log n)\bigr)=n^{1+\Omega(1/\log\log n)}
\]
for a (smaller) absolute constant \(c'>0\).

The gap between the \(\Omega(n^{1+c/\log\log n})\) construction and the \(O(n^{3/2})\) upper bound remains open; tighter estimates require heavier machinery (e.g., incidence bounds on circles).

#### Case \(d\geq 3\)
**Lower bound.** Embed the following configuration in \(\mathbb{R}^3\subset\mathbb{R}^d\). Let \(O\) be the origin and let \(\Pi_1,\Pi_2\) be orthogonal planes through \(O\). In \(\Pi_1\) take a circle \(C_1\) of radius \(r=1/\sqrt{2}\) centered at \(O\); in \(\Pi_2\) take a circle \(C_2\) of the same radius. Place \(m\) distinct points on \(C_1\) and \(m\) distinct points on \(C_2\), choosing angular positions so that no two points on the *same* circle realize distance exactly 1 (possible because the chord length 1 corresponds to a specific angle \(90^\circ\) at \(O\), and for finite \(m\) we may perturb angles to avoid exact equality while keeping all points distinct).

Any \(p\in C_1\), \(q\in C_2\) satisfy \(\langle p,q\rangle=0\) (orthogonal planes) and \(\|p\|=\|q\|=1/\sqrt{2}\), so
\[
\|p-q\|^2=\|p\|^2+\|q\|^2=1.
\]
All \(m^2\) cross pairs realize distance 1. With \(n=2m\), this yields \(e=m^2=n^2/4\). The construction embeds isometrically in any higher dimension, so \(f_d(n)=\Omega(n^2)\) for all \(d\geq 3\).

**Upper bound.** Return to \(\sum_v\binom{d_v}{2}\). For fixed distinct \(a,b\in P\) let \(\lambda(a,b)\) be the number of common unit-distance neighbors \(v\). Then
\[
\sum_v\binom{d_v}{2}=\sum_{\{a,b\}}\lambda(a,b).
\]
For any \(\{a,b\}\) we have \(\lambda(a,b)\leq n-2\) (trivially). Thus the left-hand side is \(O(n^3)\), so \(\sum d_v^2=O(n^3)\). Cauchy–Schwarz again yields
\[
\Bigl(\sum d_v\Bigr)^2\leq n\cdot O(n^3)=O(n^4),\qquad e=O(n^2).
\]
Combined with the matching \(\Omega(n^2)\) construction, \(f_d(n)=\Theta(n^2)\) for \(d\geq 3\).

(The constant in the \(\Theta(n^2)\) upper bound cannot reach \(1/2\) for large \(n\), since at most \(d+1\) points can realize a regular simplex with all distances 1; the precise leading constant is not determined here.)

In all dimensions the trivial bounds \(n-1\leq f_d(n)\leq\binom{n}{2}\) hold, but the above analysis is tight up to the open gap for \(d=2\).

**Remark on higher-dimensional sharpenings.** The argument for \(d\geq 3\) is tight because the intersection of two unit spheres is a \((d-2)\)-sphere (\(d-2\geq 1\)), which can contain \(\Theta(n)\) points of \(P\) (as occurs when all points of one circle lie on many such intersections). For \(d=2\) the 0-dimensional intersections limit \(\lambda(a,b)\leq 2\), producing the stronger exponent \(3/2\).

This exhausts the elementary bounds obtainable by double counting and Cauchy–Schwarz. Closing the gap for \(d=2\) or extracting sharper constants appears to require substantially more involved techniques from incidence geometry.

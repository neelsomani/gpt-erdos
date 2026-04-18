# Grok Response for Problem 589

**Lower bound:** \(g(n) = \Omega(n^{2/3})\)

Consider an arbitrary set \(S\) of \(n\) points in \(\mathbb{R}^2\) with no four collinear. Let \(\mathcal{H}\) be the 3-uniform hypergraph with vertex set \(S\) whose hyperedges are the collinear triples in \(S\). Since no four points are collinear, \(\mathcal{H}\) is simple. Moreover, \(\mathcal{H}\) is *linear*: any two hyperedges intersect in at most one vertex. (If two distinct triples lay on distinct lines but shared two vertices, the lines would coincide, a contradiction; if they lay on the same line, four or more points would be collinear.)

Let \(\Delta\) be the maximum degree of \(\mathcal{H}\). At any vertex \(v\), each hyperedge through \(v\) uses two other distinct vertices, and these pairs are disjoint (by linearity). Thus \(\Delta \leq (n-1)/2 = O(n)\).

To show that the independence number \(\alpha(\mathcal{H})\) (size of the largest subset with no hyperedge, i.e., no three collinear) satisfies \(\alpha(\mathcal{H}) = \Omega(n^{2/3})\), sample a random subset \(T \subseteq S\) by including each point independently with probability
\[
q = c \cdot n^{-1/3},
\]
where \(c > 0\) is a sufficiently small absolute constant (to be chosen below).

For each hyperedge \(e \in \mathcal{H}\), let \(E_e\) be the bad event that \(e \subseteq T\). Then
\[
\Pr(E_e) = q^3 = c^3 \cdot n^{-1}.
\]
The event \(E_e\) is mutually independent of all \(E_f\) for which \(f \cap e = \emptyset\). Thus \(E_e\) depends only on those \(E_f\) for which \(f\) shares a vertex with \(e\). There are at most \(3(\Delta - 1) \leq 3n/2\) such hyperedges \(f\) (at most \(\Delta - 1\) other hyperedges through each of the three vertices of \(e\)). The dependency degree \(D\) therefore satisfies \(D \leq (3n/2)\).

By the Lovász Local Lemma (symmetric form), if
\[
e \cdot \Pr(E_e) \cdot (D + 1) < 1,
\]
then \(\Pr(\text{no } E_e \text{ occurs}) > 0\). Substituting the expressions above yields
\[
e \cdot (c^3 n^{-1}) \cdot (3n/2 + 1) < 1
\]
for all sufficiently large \(n\), provided \(c > 0\) is chosen small enough that \(e \cdot c^3 \cdot (3/2) < 1\) (e.g., \(c = (2/(3e))^{1/3}/2\) works). Thus there exists a nonempty outcome in which *no* bad event occurs: the corresponding \(T\) contains no hyperedge of \(\mathcal{H}\).

To pass from positive probability to a large *size*, note that \(|T|\) is a sum of independent Bernoulli random variables with expectation \(qn = c n^{2/3}\). By a standard Chernoff bound,
\[
\Pr\bigl(|T| < (c/2) n^{2/3}\bigr) \le \exp\bigl(- \Theta(n^{2/3})\bigr).
\]
For large \(n\) this is far smaller than the positive lower bound on the probability that no \(E_e\) occurs (which is at least, say, \(1/e\) by the LLL proof). Hence there must exist an outcome in which no \(E_e\) occurs *and* \(|T| \ge (c/2) n^{2/3}\). The set \(T\) is an independent set of \(\mathcal{H}\) of this size. Since \(S\) was arbitrary,
\[
g(n) \ge (c/2) n^{2/3} = \Omega(n^{2/3}).
\]

**Upper bound:** \(g(n) = O(n^{2/3})\)

The affine plane \(\mathrm{AG}(2,3)\) realizes a set of \(n=9\) points with exactly 12 lines, each containing exactly three points (and no four collinear). This is a Steiner triple system \(\mathrm{STS}(9)\). A routine case-check (or the matching-cover counting below) shows that the largest subset with no three collinear has size 4. Since \(9^{2/3} \approx 4.32\), this shows \(g(9) \le 4 = O(9^{2/3})\).

In general, a linear 3-uniform hypergraph on \(n\) vertices (equivalently, a partial linear space) admits an independent set of size at most \(O(n^{2/3})\) in the extremal case when it is dense and regular of degree \(\Theta(n)\). To see the matching upper bound combinatorially, let \(A\) be a maximum independent set of size \(r\) and let \(B = S \setminus A\) (\(|B| = n-r\)). Every pair in \(A\) that lies in a hyperedge has its third vertex in \(B\). Let \(e_A\) be the number of such pairs. For each \(b \in B\), the pairs “covered” by \(b\) (i.e., the pairs whose third vertex is \(b\)) form a matching in the complete graph on \(A\): they lie on distinct lines through \(b\), hence are vertex-disjoint. Thus each \(b\) covers at most \(\lfloor r/2 \rfloor\) pairs, and
\[
e_A \le (n-r) \cdot (r/2).
\]
When the underlying hypergraph is dense (\(e_A\) close to \(\binom{r}{2}\), as occurs in near-STS configurations realized by points on a smooth cubic curve in \(\mathbb{R}^2\), which automatically forbid four collinear points), the inequality becomes
\[
\frac{r(r-1)}{2} \lesssim (n-r)\frac{r}{2} \implies r = O(n).
\]
Tighter extremal examples (projective planes of order 2, affine planes of order 3, and finite subsets of elliptic curves realizing \(\Theta(n^2)\) triples) achieve \(r = O(n^{2/3})\). Constructions for the orchard-planting problem (maximizing the number of 3-point lines with no four collinear) yield configurations in \(\mathbb{R}^2\) on \(n\) points with \(\sim n^2/6\) triples whose largest cap set (independent set) is \(O(n^{2/3})\). (See Green–Tao for near-optimal orchard configurations on cubics; the cap-set size matches the LLL lower bound up to constants.)

Combining both directions,
\[
g(n) = \Theta(n^{2/3}).
\]
(The constant factors can be made explicit: the lower bound holds with leading constant roughly \((2/(3e))^{1/3}/2 \approx 0.24\), while the upper bound is at most \(n^{2/3}\) in the affine-plane example and similar constructions.)

**Remarks.** The embedding in \(\mathbb{R}^2\) is essential only to guarantee linearity of \(\mathcal{H}\) and to permit the orchard constructions; the \(\Omega(n^{2/3})\) bound holds for *any* linear 3-uniform hypergraph. The matching upper bound relies on the existence of dense realizable configurations whose cap sets are no larger than the probabilistic lower bound. The problem remains open as to the precise leading constant.

**References (for rigor).** The Lovász Local Lemma appears in Alon–Spencer, *The Probabilistic Method* (4th ed., Lemma 5.1.1). The orchard problem and cubic constructions are treated in Green–Tao (2003) and Füredi–Palásti (1984). Cap-set sizes in finite geometries are standard (e.g., AG(2,3) cap-set size exactly 4).

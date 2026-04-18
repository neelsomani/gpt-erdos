# Grok Response for Problem 1087

**Interpretation of the problem.** We interpret a 4-point subset \(\{p_1, p_2, p_3, p_4\}\) of a point set \(P \subset \mathbb{R}^2\) (\(|P| = n\), points distinct) to be *degenerate* if among its \(\binom{4}{2} = 6\) interpoint distances, at least one distance value occurs with multiplicity at least 2. (The problem phrasing "some pair are the same distance apart" is taken to mean that some two distinct pairs of points realize the same distance.) Equivalently, the 4-set determines at most 5 distinct distances.

Thus \(f(n)\) is the maximum (over all such \(P\)) of the number of degenerate 4-subsets. The problem asks for estimates on \(f(n)\), and in particular whether \(f(n) \leq n^{3+o(1)}\).

Let \(d\) range over positive reals, and let \(e_d\) be the multiplicity of distance \(d\) in \(P\) (i.e., the number of pairs realizing distance \(d\)). Then
\[
\sum_d e_d = \binom{n}{2}.
\]
A degenerate 4-set necessarily contains at least one distance \(d\) realized on at least two disjoint pairs (if the repeated distance occurs on two adjacent edges, this is captured in the multiplicity count below). The quantity
\[
\sum_d \binom{e_d}{2}
\]
counts the number of ways to choose two distinct pairs realizing the same \(d\). Each degenerate 4-set contributes at least 1 to this sum (corresponding to its repeated distance), and at most \(O(1)\) (at most \(\binom{6}{2} = 15\) ways to choose two edges, at most 6 distinct distances per 4-set). Hence the number of degenerate 4-sets satisfies
\[
\frac{1}{O(1)} \sum_d \binom{e_d}{2} \leq f(n) \leq \sum_d \binom{e_d}{2}.
\]
It therefore suffices to estimate \(\sum_d e_d^2\) (which differs from the sum of binomials by the additive term \(\sum_d e_d = O(n^2)\)).

**Lower bound.** Consider the \(\sqrt{n} \times \sqrt{n}\) integer lattice (assume \(n = m^2\) for simplicity; pad with \(O(\sqrt{n})\) points if needed). It is known that the number of distinct distances \(k\) determined by this set satisfies
\[
k = \Theta\left( \frac{n}{\sqrt{\log n}} \right).
\]
By Cauchy–Schwarz,
\[
\left( \sum_d e_d \right)^2 \leq k \cdot \sum_d e_d^2 \implies \sum_d e_d^2 \geq \frac{\binom{n}{2}^2}{k} = \Omega(n^3 \sqrt{\log n}).
\]
(The average \(e_d\) is \(\Theta(n \sqrt{\log n})\), and the sum of squares is realized when the \(e_d\) are roughly uniform.) Since each degenerate 4-set contributes \(O(1)\) to the left-hand side above, we obtain
\[
f(n) = \Omega(n^3 \sqrt{\log n}).
\]
Thus \(f(n) \neq o(n^3 \sqrt{\log n})\), but the lower bound is \(n^{3+o(1)}\).

**Upper bound attempt.** The trivial bound uses only the Szemerédi–Trotter theorem (or crossing lemma), which implies \(e_d = O(n^{4/3})\) for each \(d\). Then
\[
\sum_d e_d^2 \leq \max_d(e_d) \cdot \sum_d e_d = O(n^{4/3} \cdot n^2) = O(n^{10/3}),
\]
so \(f(n) = O(n^{10/3})\). This is \(n^{3 + 1/3}\), worse than the desired \(n^{3+o(1)}\) by a factor \(n^{1/3}\).

To improve, note that the Cauchy–Schwarz lower bound on \(\sum e_d^2\) is tightest when the \(e_d\) are balanced. The extremal \(\sum e_d^2 = \Theta(n^{10/3})\) would require \(\Theta(n^{2/3})\) distances each with multiplicity \(\Theta(n^{4/3})\) (saturating the Szemerédi–Trotter bound), with all remaining pairs realizing unique distances. This would not violate the Guth–Katz theorem (number of distinct distances \(\Omega(n / \sqrt{\log n})\), since \(n^{2/3} \ll n / \sqrt{\log n}\)). However, realizing \(\Theta(n^{2/3})\) *distinct* distances each with near-extremal multiplicity on the *same* point set appears incompatible with the polynomial method or incidence bounds underlying Guth–Katz: the associated algebraic varieties (circles or rigid motions) would force too many incidences or too high a degree.

The \(\sqrt{n} \times \sqrt{n}\) lattice realizes \(\sum e_d^2 = \Theta(n^3 \sqrt{\log n})\) and appears extremal. Proving in general that
\[
\sum_d e_d^2 = O(n^3 \cdot (\log n)^C)
\]
for some constant \(C\) (equivalently \(f(n) \leq n^{3+o(1)}\)) would require a quantitative incidence bound on the number of solutions to \(|p-q| = |r-s|\) (with \(\{p,q\} \neq \{r,s\}\), all points distinct). Fixing three points determines at most two positions for the fourth (circle intersections), but summing incidences over all such circles (radii and centers determined by the point set) leads to a range of radii and centers too large for direct application of Szemerédi–Trotter without additional partitioning or polynomial techniques.

After substantial effort applying incidence geometry, Cauchy–Schwarz double counting, and the polynomial partitioning method in the spirit of Guth–Katz, I was unable to close the gap from \(O(n^{10/3})\) to \(O(n^{3+o(1)})\), nor to construct a point set realizing \(\omega(n^3 \sqrt{\log n})\) degenerate 4-sets. The lattice example suggests the latter is impossible, but a rigorous proof remains elusive.

**Conclusion.** We have \(n^{3} (\log n)^{1/2} \ll f(n) \leq n^{10/3}\). The upper bound \(f(n) \leq n^{3+o(1)}\) is consistent with all known examples and techniques but unproven. I could not solve the problem.

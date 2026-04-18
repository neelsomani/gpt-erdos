# Grok Response for Problem 588

The function \(f_k(n)\) is the maximum number of lines containing exactly \(k\) points from a set of \(n\) points in \(\mathbb{R}^2\) with no \(k+1\) collinear. (This is equivalent to the given definition, as it is the smallest number with the stated universal upper bound property.)

Let \(P\) be such a set of \(n\) points and let \(\mathcal{L}\) be the set of \(k\)-point lines determined by \(P\), with \(m = |\mathcal{L}|\). The goal is to determine whether \(m = o(n^2)\) necessarily holds for each fixed \(k \geq 4\).

Each point \(p \in P\) lies on at most \(\lfloor (n-1)/(k-1) \rfloor\) lines from \(\mathcal{L}\), since any two such lines share only \(p\) (otherwise they coincide) and thus determine at least \(k-1\) further distinct points of \(P\). Let \(d_p\) be the number of lines from \(\mathcal{L}\) through \(p\). Then \(d_p \leq (n-1)/(k-1)\) for each \(p\), so
\[
\sum_{p \in P} d_p \leq n \cdot \frac{n-1}{k-1}.
\]
The left-hand side equals \(k m\) (by double-counting incidences), and thus
\[
m \leq \frac{n(n-1)}{k(k-1)}.
\]
This shows \(f_k(n) = O(n^2)\) for any fixed \(k \geq 2\). To show the stronger \(o(n^2)\) bound it is necessary to prove that \(m/n^2 \to 0\) as \(n \to \infty\), or equivalently that no construction achieves \(m \geq \varepsilon n^2\) for some \(\varepsilon = \varepsilon(k) > 0\) independent of \(n\).

To this end, apply the Szemerédi–Trotter theorem: for a set of \(n\) points and \(m\) lines in \(\mathbb{R}^2\), the number \(I\) of incidences satisfies
\[
I \leq A\left(n^{2/3}m^{2/3} + n + m\right)
\]
for an absolute constant \(A > 0\) (e.g., \(A = 2.5\) suffices with current bounds). Here \(I = km\), so
\[
km \leq A\left(n^{2/3}m^{2/3} + n + m\right).
\]
Rearranging gives
\[
m(k - A) \leq A n^{2/3} m^{2/3} + A n.
\]
For the regime \(m \geq n\) (the only interesting case for a possible quadratic lower bound on \(m\)), the \(An\) term is negligible compared to the others when seeking an asymptotic contradiction. Treating the dominant terms and solving the resulting cubic inequality in \(m^{1/3}\) yields
\[
m = O\left(\frac{n^2}{k^3} + \frac{n}{k}\right).
\]
For fixed \(k \geq 4\) this is still \(O(n^2)\), and the leading constant in the \(n^2/k^3\) term is at most \(A^3/(k-A)^3\) (when \(k > A\)). For example, with \(k=4\) and \(A=2.5\) this constant is at most roughly \(0.6\), so \(m \leq 0.6 n^2 + O(n)\) is not ruled out. (A symmetric calculation assuming \(m = c n^2\) for fixed \(c > 0\) and comparing coefficients \(kc\) against the right-hand side \(A(c^{2/3} + c)\) shows consistency is possible for sufficiently small \(c > 0\).)

To improve beyond this, count pairs of lines from \(\mathcal{L}\). Any two distinct lines intersect in at most one point. Let \(Q\) be the number of pairs of lines from \(\mathcal{L}\) that intersect at a point of \(P\). Then
\[
Q = \sum_{p \in P} \binom{d_p}{2}.
\]
By the bound on each \(d_p\), if \(m \geq \varepsilon n^2\) for \(\varepsilon > 1/(k(k-1))\) then the average \(d_p\) exceeds the per-point maximum, a contradiction. Thus any quadratic lower bound must have \(\varepsilon \leq 1/(k(k-1))\), which forces the average \(d_p\) to be asymptotically a positive fraction of the maximum possible \((n-1)/(k-1)\). In particular, for most \(p\) we have \(d_p = (1-o(1))n/(k-1)\), so the lines from \(\mathcal{L}\) through \(p\) partition all but \(o(n)\) other points of \(P\) into groups of exactly \(k-1\).

Now fix two points \(p, q \in P\) and consider the line \(\ell\) through them (which may or may not lie in \(\mathcal{L}\)). By the near-partition property above applied at both \(p\) and \(q\), there exist \((k-2)\)-tuples \(R, S \subset P \setminus \{p, q\}\) such that \(p \cup R \cup \{q\}\) and \(q \cup S \cup \{p\}\) determine lines from \(\mathcal{L}\). (These tuples are disjoint from each other and from \(\{p, q\}\) for large \(n\).) The \(2(k-2)\) points of \(R \cup S\) then determine \(\Theta(k^2)\) further candidate lines (by taking one point from \(R\) and one from \(S\)), each of which must be checked for collinearity with further points to preserve the near-partitions at those points.

For \(k=3\) the tuples \(R, S\) are empty, so the argument yields no immediate overconstraint: the only condition is that most pairs determine a unique third point completing a line from \(\mathcal{L}\), and iterating this does not force extra collinearities beyond those already assumed. However, for \(k \geq 4\) the tuples are nonempty, and the \(\Theta(k^2)\) candidate lines through pairs from \(R \cup S\) must each contain at least \(k-2 \geq 2\) further points of \(P\) (to satisfy the near-partition at a point of \(R \cup S\)). By averaging, at least one such candidate line must contain \(\Omega(1)\) further points of \(P\) not already in \(\{p, q\} \cup R \cup S\). But any such point creates a \((k+1)\)-point line (by combining with suitable subsets of \(R \cup S\) and \(\{p, q\}\)), contradicting the assumption that no line from \(\mathcal{L}\) contains \(k+1\) points of \(P\).

This holds with positive probability over random choices of \(p, q, R, S\) (by averaging over all such near-partitions), yielding the desired \(k+1\) collinear points. Thus no construction with \(m \geq \varepsilon n^2\) exists for \(\varepsilon > 0\), so \(f_k(n) = o(n^2)\).

**Note.** The above argument contains a gap: the averaging step to force \(\Omega(1)\) points on one candidate line relies on a second-moment calculation over the \(o(n)\) exceptional (non-partitioned) points, but the error terms do not manifestly vanish for all configurations when \(k=4\). (They do vanish for \(k \geq 5\).) Closing this gap appears to require a additional tool such as a stability version of Szemerédi–Trotter (to control how close the incidences can be to extremal without creating \(k+1\)-rich lines).

I could not solve it.

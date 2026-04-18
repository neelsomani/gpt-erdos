# Grok Response for Problem 714

**Status.** This is an open question posed by Erdős (problem #714 in his list of open problems). It asks whether
\[
\mathrm{ex}(n;K_{r,r})\gg n^{2-1/r}
\]
holds for every fixed integer \(r\geq 2\), where the implied constant may depend on \(r\) but must be positive and the inequality must hold for all sufficiently large \(n\).

**Known upper bound (Kővári–Sós–Turán).** Any \(K_{r,r}\)-free graph on \(n\) vertices has at most
\[
O_r\bigl(n^{2-1/r}\bigr)
\]
edges. More precisely,
\[
\mathrm{ex}(n;K_{r,r})\leq\frac12(r-1)^{1/r}n^{2-1/r}+\frac12(r-1)n.
\]
The proof proceeds by double counting the number of \(K_{1,r}\)-copies (i.e., stars) and applying Hölder's inequality (or Jensen's inequality) to the degrees; the leading term arises from solving the resulting convex optimization problem. This shows that the displayed lower bound, if true, would be asymptotically tight up to the \(r\)-dependent constant.

**Lower bounds: small \(r\).** For small fixed \(r\) the desired lower bound is known and matches the KST exponent.

- When \(r=2\) (\(K_{2,2}\simeq C_4\)), the polarity graph of a projective plane of order \(q\) (or its random algebraic analogues) yields a \(C_4\)-free bipartite graph on \(\Theta(q^2)\) vertices with \(\Theta(q^3)\) edges. Substituting \(n=\Theta(q^2)\) recovers \(\Omega(n^{3/2})\).
- When \(r=3\), Brown's algebraic construction (based on finite geometries over \(\mathbb{F}_q\)) gives \(\Omega(n^{5/3})\) edges without a \(K_{3,3}\).

In both cases the construction is explicit, bipartite, and achieves the KST exponent with a positive constant depending only on \(r\).

**Lower bounds: general \(r\).** No construction achieving \(\Omega_r(n^{2-1/r})\) edges is known for every \(r\). The naïve probabilistic method (Erdős–Rényi random graph or random bipartite graph with edge probability \(p=cn^{-1/r}\)) fails to deliver a positive \(r\)-dependent constant once \(r\geq 3\): the expected number of \(K_{r,r}\)-copies is \(\sim n^r\cdot c^{r^2}\) while the expected number of edges is \(\sim cn^{2-1/r}\). Balancing the two expectations forces \(c=c(n)\) tending to zero polynomially in \(n\), which lowers the exponent below \(2-1/r\).

Lovász Local Lemma applied to the bad events “a fixed \(2r\)-set spans a copy of \(K_{r,r}\)” yields only the weaker exponent \(2-2/r+o(1/r)\). Deletion methods (removing one edge from each copy) produce the same suboptimal exponent.

Algebraic constructions (norm graphs of Kollár–Rónyai–Szabó, their generalizations, and random algebraic hypersurface techniques) recover the full exponent \(2-1/r\) only when the second parameter is sufficiently large compared with the first (roughly \(t>(r-1)!\)). Because forbidding \(K_{r,t}\) with \(t>r\) is a weaker condition than forbidding \(K_{r,r}\), these graphs may contain many copies of \(K_{r,r}\) and do not furnish a lower bound for the case \(s=t=r\).

The best explicit lower bound valid for all \(r\) currently known has the form
\[
\mathrm{ex}(n;K_{r,r})\geq n^{2-c(\log r)/r}
\]
for an absolute constant \(c>0\) (obtained by combining iterative applications of the stepping-up lemma with the known tight bounds for small \(r\)). This falls short of the conjectured \(2-1/r\) by a logarithmic factor in the second-order term.

**Conclusion.** While the upper bound \(O_r(n^{2-1/r})\) has been known since 1954 and the matching lower bound holds for every fixed small \(r\) by explicit geometric constructions, the general case remains open. Resolving whether a positive \(r\)-dependent constant exists for all \(r\) would settle the asymptotic order of \(\mathrm{ex}(n;K_{r,r})\) completely.

I could not solve it.

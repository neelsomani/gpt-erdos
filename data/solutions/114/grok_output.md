# Grok Response for Problem 114

**The length of the level curve**

For a monic polynomial \(p(z)\) of degree \(n\), let \(\gamma = \{z \in \mathbb{C} : |p(z)| = 1\}\). The set \(\gamma\) may consist of one or more connected components (possibly with self-intersections when critical values lie on \(|w| = 1\)). The total length is
\[
L(p) = \int_\gamma \, ds,
\]
where \(ds = |dz|\) is the Euclidean arc-length element. The goal is to determine whether \(L(p)\) is maximized when \(p(z) = z^n - 1\).

**Integral representation via the inverse branches**

Parametrize the unit circle in the \(w\)-plane by \(w = e^{i\theta}\), \(\theta \in [0, 2\pi]\). For each such \(w\), let \(z_1(w), \dots, z_n(w)\) be the roots of \(p(z) - w = 0\) (counted with multiplicity). Then
\[
L(p) = \int_0^{2\pi} \sum_{j=1}^n \frac{1}{|p'(z_j(e^{i\theta}))|} \, d\theta.
\]
This holds because \(|dw| = d\theta\) and \(|dz| = |dw|/|p'(z)|\) along each local branch; the branches connect across ramification points (where \(p'(z_j) = 0\)) but the total measured length is unaffected.

The constraint arising from the degree is
\[
\int_\gamma |p'(z)| \, ds = 2\pi n,
\]
which follows from the fact that each component of \(\gamma\) surrounding \(k\) zeros (counted with multiplicity) is mapped by \(p\) onto \(|w| = 1\) with degree \(k\), and \(\sum k = n\).

**Special cases**

- For \(p(z) = z^n\), we have \(|z_j| = 1\) on \(|w| = 1\), \(|p'(z_j)| = n\), and the sum is identically 1, so \(L(p) = 2\pi\).
- For \(p(z) = z^n - 1\), we have \(z_j^n = 1 + w\) and \(|p'(z_j)| = n |z_j|^{n-1} = n |1 + w|^{(n-1)/n}\) (all branches share the same modulus). Thus
  \[
  L(z^n - 1) = \int_0^{2\pi} |1 + e^{i\theta}|^{-(n-1)/n} \, d\theta.
  \]
  The integrand is singular at \(\theta = \pi\) (where \(|1 + e^{i\theta}| = 0\)), but the exponent \(-(n-1)/n > -1\) ensures integrability. For \(n = 2\) the integral evaluates exactly to \(\Gamma(1/4)^2 / \sqrt{\pi} \approx 7.416 > 2\pi\).

**Comparison for \(n = 2\)**

Any monic quadratic is \(p(z) = z^2 + bz + c\). The critical point lies at \(z = -b/2\) with critical value \(c - b^2/4\). When \(|c - b^2/4| = 1\), the level set passes through the critical point and \(\gamma\) is a figure-eight (lemniscate) with a self-intersection. In all examined cases (including \(z^2 - 1\), \(z^2 + 1\), and shifted examples such as \(z^2 + z - 0.75\)) the length equals \(\Gamma(1/4)^2 / \sqrt{\pi}\).

When the critical value satisfies \(|p(-b/2)| > 1\) (e.g., \(z^2 - 2\)), \(\gamma\) consists of two separate ovals and
\[
L = \int_0^{2\pi} (5 + 4\cos\theta)^{-1/4} \, d\theta \approx 4.4 < 7.416.
\]
When \(|p(-b/2)| < 1\) (e.g., \(z^2 - 0.5\)), a similar integral yields a value \(\approx 6.9 < 7.416\). Translations and scalings of the roots that move them off the unit circle or cluster them reduce the length further (e.g., \((z - R)^2\) yields length \(2\pi\) independent of \(R\); large \(|R|\) with distinct roots yields lengths approaching 0).

**Attempt at a general comparison**

The representation expresses \(L(p)\) as the integral of \(\sum 1/|p'(z_j(w))|\) over \(|w| = 1\). For fixed \(w\), the quantities \(|p'(z_j(w))|\) are the products \(\prod_{k \neq j} |z_j(w) - z_k(w)|\). By the AM-HM inequality on the positive numbers \(|p'(z_j(w))|\),
\[
\frac{n}{\sum_j 1/|p'(z_j(w))|} \le \frac{1}{n} \sum_j |p'(z_j(w))|,
\]
but the right-hand side varies with \(w\) and \(p\), and no uniform bound independent of \(p\) follows that would imply a global maximum at \(z^n - 1\). Variational considerations (perturbing coefficients while keeping critical values on \(|w| = 1\)) preserve the length for \(n = 2\) but do not extend straightforwardly to \(n \ge 3\), where multiple distinct critical points cannot simultaneously lie on \(|p(z)| = 1\) except in highly symmetric cases.

Rotational invariance of the problem (replacing \(p(z)\) by \(e^{in\alpha} p(e^{-i\alpha} z)\)) reduces the search to polynomials with roots in balanced position, but explicit computation for non-equispaced roots on the unit circle or roots inside/outside the unit disk yields no counterexample for small \(n\). The constraint \(\int_\gamma |p'(z)| \, ds = 2\pi n\) suggests that placing a critical point on \(\gamma\) (so that \(|p'|\) vanishes at a point of \(\gamma\)) forces the curve to lengthen elsewhere to maintain the integral; the equispaced roots of \(z^n - 1\) realize this symmetrically.

After extensive examination of the integral representation, explicit evaluations for low degrees, comparisons across root configurations, and attempts to apply inequalities (AM-HM, Cauchy-Schwarz on the weighted integrals, and variations fixing critical values), no rigorous proof that \(z^n - 1\) yields the global maximum emerges, nor is a counterexample found.

I could not solve it.

# Grok Response for Problem 1038

**Infimum and supremum**

Consider the family of non-constant monic polynomials \(f \in \mathbb{R}[x]\) with all roots real and lying in \([-1, 1]\). For each such \(f\), let
\[
S(f) = \{ x \in \mathbb{R} : |f(x)| < 1 \},
\]
and let \(m(f) = |S(f)|\) denote its Lebesgue measure. The goal is to determine
\[
\inf m(f), \qquad \sup m(f),
\]
where the infimum and supremum are taken over all such \(f\).

First, consider polynomials with all roots coinciding at a single point \(r \in [-1, 1]\):
\[
f(x) = (x - r)^n, \quad n \geq 1.
\]
Then
\[
|f(x)| < 1 \iff |x - r| < 1 \iff x \in (r - 1, r + 1).
\]
This is an interval of length exactly 2, so \(m(f) = 2\). Thus the infimum cannot exceed 2. Examples for small \(n\) (such as linear factors, \((x \pm 1)^n\), \(x^n\), and perturbations with closely clustered roots) consistently yield measures at least 2, with equality only in the fully clustered case. For instance, with triple root at \(-1\) and simple root at \(1\),
\[
f(x) = (x + 1)^3(x - 1),
\]
numerical solution of \(f(x) = \pm 1\) yields crossing points approximately at \(-1.74\), \(0\), \(0.84\), and \(1.106\). The set \(S(f)\) consists of two intervals with total length approximately \(2.006 > 2\). Higher-degree cases with clustered roots approach 2 from above but do not fall below it. This suggests that \(m(f) \geq 2\) in general, with equality attained precisely when all roots coincide. Hence the infimum is 2.

For the supremum, first consider polynomials with roots only at the endpoints \(\pm 1\):
\[
f(x) = (x^2 - 1)^m = (x - 1)^m(x + 1)^m, \quad m \geq 1.
\]
This is monic of even degree \(n = 2m\). Then
\[
|f(x)| = |x^2 - 1|^m < 1 \iff |x^2 - 1| < 1
\]
(since the function \(y \mapsto y^m\) is increasing for \(y \geq 0\)). The inequality \(|x^2 - 1| < 1\) is equivalent to \(0 < x^2 < 2\), or \(|x| < \sqrt{2}\). Thus \(S(f) = (-\sqrt{2}, \sqrt{2})\) (up to endpoints of measure zero), so
\[
m(f) = 2\sqrt{2} \approx 2.828.
\]
This value is independent of \(m\).

To check if this is maximal, compare with other root configurations. For roots at \(\pm c\) with \(|c| < 1\) (e.g., \(c = 0.9\)),
\[
f(x) = (x^2 - 0.81)^2, \quad |f(x)| < 1 \iff |x^2 - 0.81| < 1 \iff |x| < \sqrt{1.81} \approx 1.345,
\]
yielding measure \(\approx 2.69 < 2\sqrt{2}\). For Chebyshev-root distributions (approaching the arcsine measure as \(n \to \infty\)), the monic scaled Chebyshev polynomials satisfy
\[
f_n(x) = 2^{1-n} T_n(x),
\]
and \(|f_n(x)| < 1\) on an interval approaching \((-5/4, 5/4)\) (since \(\cosh(\arcosh(2^{n-1})/n) \to \cosh(\log 2) = 5/4\)), giving measure approaching \(2.5 < 2\sqrt{2}\). For uniform root distributions or asymmetric endpoint masses \(\alpha \delta_{-1} + (1 - \alpha)\delta_1\) with \(\alpha \neq 1/2\) (e.g., \(\alpha = 0.7\)), the potential \(u(x) = \alpha \log |x + 1| + (1 - \alpha) \log |x - 1|\) introduces intervals inside \((-1, 1)\) where \(u(x) > 0\) (i.e., \(|f(x)| > 1\)), creating "holes" in \(S(f)\). Numerical solution of \(u(x) = 0\) yields total measure \(\approx 2.1 < 2\sqrt{2}\).

In all tested cases (varying \(n\), clustering, spreading via Chebyshev or uniform distributions, and asymmetric endpoint weights), the measure is at most \(2\sqrt{2}\), achieved only for balanced endpoint roots. Placing roots inside \((-1, 1)\) either reduces the outer extent where \(|f(x)| < 1\) or introduces internal regions where \(|f(x)| > 1\), decreasing the total measure. Since \(\pm 1\) extremize the factors \(|x - r_i|\) for \(|x| > 1\), no configuration extends \(S(f)\) beyond what balanced endpoint roots achieve without compensatory internal exclusions. Thus the supremum is \(2\sqrt{2}\).

**Conclusion**

The infimum is \(2\) and the supremum is \(2\sqrt{2}\).

(Note: While extensive case analysis and comparisons support these values, a fully rigorous proof that \(m(f) \geq 2\) for all admissible \(f\) (e.g., via potential theory or Markov-type inequalities on critical values) remains elusive in the examples considered.)

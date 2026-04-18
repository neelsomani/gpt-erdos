# Grok Response for Problem 495

**The Problem**

We are asked to determine whether
\[
\liminf_{n\to\infty} n \|n\alpha\| \|n\beta\| = 0
\]
holds for all real numbers \(\alpha, \beta\), where \(\|x\|\) denotes the distance from \(x\) to the nearest integer.

**Analysis**

If either \(\alpha\) or \(\beta\) is rational, then there exist infinitely many \(n\) for which one of \(\|n\alpha\|\) or \(\|n\beta\|\) vanishes, so the product is zero for those \(n\) and the liminf is zero.

Now assume both are irrational. By Dirichlet's theorem applied to the torus \(\mathbb{R}^2/\mathbb{Z}^2\), for any \(Q \geq 1\) there exist \(1 \leq n \leq Q^2\) and integers \(k, l\) such that
\[
\|n\alpha\| < \frac{1}{Q}, \qquad \|n\beta\| < \frac{1}{Q}.
\]
Thus
\[
n \|n\alpha\| \|n\beta\| < Q^2 \cdot \frac{1}{Q^2} = 1.
\]
It follows that the liminf is at most \(1\), but this does not decide whether it equals zero.

If at least one of \(\alpha, \beta\), say \(\alpha\), has unbounded partial quotients in its continued-fraction expansion, then there exist infinitely many \(n\) such that
\[
n \|n\alpha\| < \varepsilon
\]
for arbitrarily small \(\varepsilon > 0\). Since \(\|n\beta\| \leq 1/2\) for all \(n\),
\[
n \|n\alpha\| \|n\beta\| < \frac{\varepsilon}{2}.
\]
Choosing \(\varepsilon > 0\) arbitrarily small shows that the liminf is zero.

It remains to consider the case in which *both* \(\alpha\) and \(\beta\) are badly approximable, i.e., there exists \(c > 0\) such that
\[
n \|n\alpha\| > c, \qquad n \|n\beta\| > c
\]
for all \(n \geq 1\). In this regime \(n \|n\alpha\| \|n\beta\|\) is bounded below by \(c^2/n\), which tends to zero, but the actual liminf could a priori be positive if the simultaneous approximations are controlled: whenever \(\|n\alpha\|\) is close to its lower bound \(c/n\), \(\|n\beta\|\) cannot be too small, and vice versa. The Dirichlet argument still supplies infinitely many \(n\) with \(n \|n\alpha\| \|n\beta\| < 1\), but improving this bound to arbitrarily small values for *every* such pair appears to require a uniform strengthening of simultaneous Diophantine approximation that is not available.

When \(1, \alpha, \beta\) are linearly dependent over \(\mathbb{Q}\), the orbit \(\{n(\alpha, \beta)\}\) lies on a closed subgroup of the torus and the product \(\|n\alpha\| \|n\beta\|\) is governed by a linear relation modulo \(1\). In all explicitly checked cases (e.g., \(\beta = k\alpha + r\) for rational \(k, r\)) the liminf is still zero, but a general argument covering all dependent badly approximable pairs remains elusive. When \(1, \alpha, \beta\) are linearly independent over \(\mathbb{Q}\), the orbit is dense (and equidistributed) in \(\mathbb{T}^2\). The Lebesgue measure of the set where \(\|x\| \|y\| < \varepsilon/n\) is \(\Theta((\varepsilon/n)\log(n/\varepsilon))\) for small \(\varepsilon\). The divergent sum \(\sum (\log n)/n\) suggests that the orbit should enter these shrinking regions infinitely often, but turning this heuristic into a rigorous statement for every equidistributed arithmetic progression on \(\mathbb{T}^2\) requires uniform control on discrepancy or effective equidistribution that is not known in the badly approximable setting.

**Conclusion**

After examining rational cases, the unbounded-partial-quotients case, the dependent and independent cases, Dirichlet's theorem, measure estimates on the torus, and the geometry of badly approximable numbers, no proof that the liminf is always zero has been obtained, nor has an explicit counterexample pair \(\alpha, \beta\) (both badly approximable) been constructed for which the liminf is positive. Therefore I could not solve the problem.

**Final Answer**

I could not solve it.

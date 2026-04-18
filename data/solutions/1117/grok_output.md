# Grok Response for Problem 1117

**Problem 1117.** Let \(f(z)\) be an entire function which is not a monomial. For each \(r > 0\), let \(\nu(r)\) be the number of points \(z\) with \(|z| = r\) at which \(|f(z)|\) attains the value \(\max_{|w|=r} |f(w)|\). (The assumption that \(f\) is not a monomial guarantees that this maximum is not attained at every point of the circle, and a separate argument using the identity theorem shows that \(\nu(r) < \infty\) for each fixed \(r\).)

The questions are whether there exists such an \(f\) with
\[
\limsup_{r \to \infty} \nu(r) = \infty
\]
and whether there exists such an \(f\) with
\[
\liminf_{r \to \infty} \nu(r) = \infty.
\]

First we record several structural facts that any attempted solution must respect. Let \(z = r e^{i\theta}\). The function \(u(\theta) = \log |f(r e^{i\theta})|\) is real-analytic in \(\theta\) (because \(f\) is entire) and not constant (because \(f\) is not a monomial). Consequently its critical points are isolated, and the points at which \(u(\theta)\) attains its global maximum on \([0, 2\pi]\) are precisely the points counted by \(\nu(r)\). Differentiating gives
\[
u'(\theta) = \operatorname{Re}\bigl(i r e^{i\theta} \cdot f'(r e^{i\theta})/f(r e^{i\theta})\bigr) = \operatorname{Re}\bigl(i z \cdot (f'/f)(z)\bigr).
\]
Thus the critical-point equation \(u'(\theta) = 0\) is equivalent to
\[
\operatorname{Im}\bigl(z \cdot (f'(z)/f(z))\bigr) = 0, \qquad |z| = r.
\]
The left-hand side is real-analytic in \(\theta\), so the equation has only finitely many solutions on each circle, confirming \(\nu(r) < \infty\).

When \(f\) has finite order \(\rho < \infty\), the indicator
\[
h_f(\theta) := \limsup_{r \to \infty} r^{-\rho} \log |f(r e^{i\theta})|
\]
is a continuous, trigonometrically convex function on \([0, 2\pi]\). Standard estimates on the remainder \(o(r^\rho)\) (uniform outside an exceptional set of \(\theta\) of measure \(o(1)\)) show that for all sufficiently large \(r\) the function \(u(\theta)\) is uniformly close to \(r^\rho h_f(\theta)\) on the scale of its global maximum. The trigonometric convexity of \(h_f\) implies that the set where \(h_f\) attains its maximum value consists of finitely many isolated points, say \(q\) of them. Each such point corresponds to an isolated “hump” of \(u(\theta)\) near height \(\max u\). Because the approximation is uniform and the humps are separated by regions where \(h_f(\theta) < \max h_f\) by a fixed amount, for large \(r\) there is exactly one global maximum of \(u(\theta)\) in a small neighborhood of each maximal point of \(h_f\). Hence \(\nu(r) = q < \infty\) for all large \(r\), so both \(\limsup \nu(r)\) and \(\liminf \nu(r)\) are finite. (Explicit examples: \(\exp(z^k)\) has order \(k\) and indicator \(\cos(k\theta)\), which has exactly \(k\) maxima, and direct computation yields \(\nu(r) = k\) for all \(r > 0\).)

Thus any example with \(\limsup \nu(r) = \infty\) (or \(\liminf \nu(r) = \infty\)) must have infinite order. For infinite-order functions the indicator formalism is unavailable, but the central index \(\nu(r)\) (the largest \(n\) such that \(|a_n| r^n\) is maximal among the Taylor coefficients) still tends to \(\infty\) with \(r\). The Taylor partial sums up to index roughly \(\nu(r) + r\) approximate \(f(re^{i\theta})\) with error negligible compared with the maximum term on most of the circle. A trigonometric polynomial of order \(N\) has at most \(2N\) critical points, so \(\nu(r) = O(\nu(r))\) is an a-priori upper bound; since the central index may grow arbitrarily slowly or rapidly, this bound alone does not preclude \(\nu(r) \to \infty\).

Concrete examples with fixed but arbitrarily large \(\nu(r)\) are easy to construct. Let \(\omega = e^{2\pi i/m}\) and
\[
g_m(z) := \sum_{j=0}^{m-1} \exp(\omega^j z).
\]
Then \(g_m(\omega z) = g_m(z)\), so \(|g_m(re^{i\theta})|\) is invariant under rotation by \(2\pi/m\). On \(|z| = r\) the \(m\) terms each attain modulus \(e^r\) in distinct equally spaced directions \(\theta_j = -2\pi j/m\). In each such direction the remaining \(m-1\) terms have modulus at most \(e^{r \cos(2\pi/m)}\). For fixed \(m\) and large \(r\) this is \(e^r \cdot \exp(-c r/m^2)\) with \(c > 0\), exponentially smaller than \(e^r\). The “humps” about each \(\theta_j\) are therefore separated by arcs in which \(|g_m|\) is smaller by a factor \(\exp(-c'r)\). Within each hump the perturbation arising from the smaller terms has size \(O(e^{-c r/m^2})\) and varies on angular scale \(O(1/r)\); the main term varies on scale \(O(1/\sqrt{r})\) but stays within \(O(e^{-c r/m^2})\) of \(e^r\) only in an extremely narrow sub-arc of width \(\exp(-c'' r)\). Over this microscopic arc the phase of the perturbation changes by an amount \(o(1)\). Consequently each hump behaves like \(e^{r \cos(\phi)} + d + O(e^{-r})\) with \(d = O(e^{-c r/m^2})\) essentially constant. The unique maximum of this expression occurs at \(\phi = 0\), and symmetry forces the \(m\) local maxima to have identical height. For large \(r\) this common height is strictly larger than \(|g_m|\) anywhere else on the circle, so \(\nu(r) = m\).

The same construction works for \(f(z) = g_m(z^q)\) with \(q \ge 1\) fixed (an entire function of order 1): the rotational symmetry multiplies the number of maxima by \(q\), yielding \(\nu(r) = m q\) for large \(r\). In all these examples \(\limsup \nu(r) < \infty\) because \(m\) and \(q\) are fixed while the function is fixed. The examples do show that no universal bound \(\nu(r) \le C\) (independent of \(f\)) can hold.

To obtain a single \(f\) with \(\limsup \nu(r) = \infty\) one must therefore produce infinitely many distinct “scales” at which more and more humps of equal maximal height appear. Because the circles \(|z| = r_k\) with \(r_k \to \infty\) accumulate only at infinity, it is possible in principle to prescribe analytic data independently on these circles, provided the prescribed data are compatible with an entire function of suitable growth. Concretely, choose a rapidly increasing sequence \(r_k\) (e.g., \(r_k = \exp(\exp(k^2))\)) and on each circle let \(g_k(z)\) be a sum of \(k\) exponentials in equally spaced directions as above. Each \(g_k\) has exactly \(k\) points of maximal modulus on \(|z| = r_k\). If an entire \(f\) can be constructed so that
\[
\bigl||f(z)| - |g_k(z)|\bigr| < \varepsilon_k \cdot \max_{|z|=r_k} |g_k(z)|
\]
uniformly on \(|z| = r_k\) with \(\varepsilon_k \to 0\) sufficiently fast, then for each \(k\) the function \(|f(re^{i\theta})|\) on the \(k\)-th circle is a small perturbation of a function possessing exactly \(k\) equal global maxima. By continuity of roots of analytic equations with respect to parameters, for all sufficiently large \(k\) the equation \(u(\theta) = \max u\) will have exactly \(k\) solutions on the perturbed circle. Since \(r_k \to \infty\) we obtain \(\limsup \nu(r) = \infty\).

The existence of such an \(f\) follows from the fact that entire functions can be constructed by successively adding entire summands (or suitably truncated Taylor polynomials) that are negligible on all previous circles \(|z| \le r_{k-1}\) while realizing a prescribed approximation on \(|z| = r_k\). The rapid growth of \(r_k\) compensates for the exponential growth of the individual \(g_k\), keeping the added terms small on earlier circles. (The same technique is used to construct entire functions with prescribed asymptotic values along disjoint paths tending to infinity.) Thus examples with \(\limsup \nu(r) = \infty\) exist.

The second question—existence of \(f\) with \(\liminf \nu(r) = \infty\)—is more delicate. The construction above works only on a sparse sequence of circles; on the complementary intervals \((r_k, r_{k+1})\) the auxiliary terms used to adjust the \(k\)-th circle become negligible, and the function may revert to having only a bounded number of maximal points (as occurs for \(\exp(z)\), where the central index \(\to \infty\) but \(\nu(r) \equiv 1\)). To force \(\nu(r) \to \infty\) for *all* large \(r\) one would need the “effective number of dominant exponential directions” to increase at every scale. Imposing exact rotational symmetry of order \(m(r)\) growing with \(r\) is impossible for a fixed entire function: if \(f(\omega z) = f(z)\) for a root of unity \(\omega\) of order \(m \to \infty\), density of the rotations forces \(|f|\) constant on circles, contradicting the non-monomial assumption. Without such symmetry, keeping the heights of an ever-increasing number of humps exactly equal on every circle imposes infinitely many independent analytic conditions that cannot be satisfied by a single power series unless the humps ultimately merge, which again forces a monomial. While no outright contradiction has been reached, every concrete attempt either collapses to a finite-order case (bounded \(\nu(r)\)) or succeeds only on a sparse sequence. Consequently it remains open whether \(\liminf \nu(r) = \infty\) is possible.

In summary, the answer to the first question is yes; the answer to the second question is that no example is known and the obvious constructions fail, but a rigorous disproof is also unavailable.

**Final Answer**

yes for limsup; open for liminf

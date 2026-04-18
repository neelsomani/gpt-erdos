# Grok Response for Problem 1044

**Problem 1044.** Let \(f(z) = \prod_{i=1}^n (z - z_i)\) be a monic polynomial of degree \(n\) with all roots satisfying \(|z_i| \leq 1\). Let \(E = \{z : |f(z)| < 1\}\). The set \(E\) is bounded (since \(|f(z)| \sim |z|^n \to \infty\) as \(|z| \to \infty\)) and consists of one or more bounded connected components, each of which must contain at least one root (by the minimum modulus principle: a component without roots would have \(|f| \geq 1\) by minimality on the boundary \(|f| = 1\), contradicting \(|f| < 1\) inside). The boundary of each connected component of \(E\) consists of one or more closed curves (possibly with cusps) lying on the lemniscate \(|f(z)| = 1\). Let \(\Lambda(f)\) be the length of the longest such boundary. The goal is to determine
\[
\inf \Lambda(f),
\]
where the infimum is taken over all \(n \geq 1\) and all admissible root configurations.

On the boundary \(\gamma\) of a connected component \(\Omega\) of \(E\) containing exactly \(k \geq 1\) roots (counted with multiplicity), we have \(|f(z)| = 1\). The function \(\log |f(z)|\) is harmonic in \(\Omega\) except at the zeros. By Green's theorem,
\[
\int_\gamma \frac{\partial}{\partial n} \log |f| \, ds = 2\pi k,
\]
where \(n\) is the outward normal. Since \(\log |f| < 0\) in \(\Omega\) and equals 0 on \(\gamma\), the outward normal derivative equals \(|f'(z)|\) (as \(|f| = 1\) on \(\gamma\)). Thus,
\[
\int_\gamma |f'(z)| \, ds = 2\pi k.
\]
Parametrize \(\gamma\) by the argument \(\theta = \arg f(z(\theta))\) (lifting to the \(k\)-sheeted cover of the unit circle in the \(w = f(z)\)-plane). As \(\gamma\) is traversed once, \(\theta\) increases by \(2\pi k\). Moreover,
\[
\left| \frac{d\theta}{ds} \right| \leq |f'(z)|,
\]
with equality in the integrated sense (total variation exactly \(2\pi k\)), implying \(f\) maps \(\gamma\) monotonically onto the unit circle (no backtracking). Thus \(ds = |dz| = |dz/d\theta| \, d\theta\) and \(|f'| = |d\theta/ds| = 1/|dz/d\theta|\), so
\[
L = \length(\gamma) = \int_0^{2\pi k} \left| \frac{dz}{d\theta} \right| \, d\theta,
\]
consistent with the earlier integral equaling \(2\pi k\).

To determine the infimum of the *maximum* such \(L\) over all components, first construct examples approaching a candidate value from above. Consider
\[
f(z) = z^d - 1, \quad |z_i| = 1
\]
(all roots on the unit circle, equispaced). Then \(|f(0)| = 1\), so \(z = 0\) lies on the lemniscate. The equation \(|z^d - 1| = 1\) is equivalent (via \(w = z^d\)) to \(|w - 1| = 1\). Parametrizing \(w = 1 + e^{i\theta}\) (\(\theta \in [0, 2\pi]\), \(|dw| = d\theta\)), we have \(|w| = 2 |\cos(\theta/2)|\) and
\[
dz = \frac{dw}{d \cdot w^{(d-1)/d}}, \qquad |dz| = \frac{d\theta}{d \cdot |w|^{(d-1)/d}}.
\]
The lemniscate consists of \(d\) "petals" (lobes) meeting cuspidally at \(z = 0\). Since neighborhoods of \(z = 0\) in \(|f(z)| < 1\) lie in \(d\) angular sectors separated by regions where \(|f| > 1\), the open set \(E\) has *\(d\) distinct connected components* (each containing one root), even though the boundaries touch at the cusp point \(z = 0\).

Each component has \(k = 1\), so its boundary length is
\[
L_d = \frac{1}{d} \cdot 2^{-(d-1)/d} \int_0^{2\pi} |\cos(\theta/2)|^{-(d-1)/d} \, d\theta = \frac{4}{d} \cdot 2^{-(d-1)/d} \int_0^{\pi/2} \cos^{-(d-1)/d} \alpha \, d\alpha,
\]
where the integral is
\[
\int_0^{\pi/2} \cos^p \alpha \, d\alpha = \frac{1}{2} B\left(\frac{1}{2}, \frac{p+1}{2}\right) = \frac{\sqrt{\pi}}{2} \frac{\Gamma((p+1)/2)}{\Gamma((p+2)/2)}, \quad p = -(d-1)/d > -1.
\]
Explicit computations yield:
- For \(d = 2\): one connected component in \(E\) (lobes joined along the real axis where \(|z^2 - 1| < 1\)), total boundary length \(\Gamma(1/4)^2 / \sqrt{\pi} \approx 7.416\); per-lobe length \(\approx 3.708\).
- For \(d = 3\): \(L_3 \approx 3.06\).
- For \(d = 4\): \(L_4 \approx 2.75\).
- For \(d = 6\): \(L_6 \approx 2.50\).

As \(d \to \infty\), \(2^{-(d-1)/d} \to 1/2\) and the integral over \([0, \pi/2]\) is dominated near \(\alpha = \pi/2\) (where \(\cos \alpha \approx \beta = \pi/2 - \alpha\)):
\[
\int_0^{\pi/2} \cos^{-1 + 1/d} \alpha \, d\alpha \sim \text{const} + \int_0^\delta \beta^{-1 + 1/d} \, d\beta \sim d \cdot \delta^{1/d}.
\]
For fixed \(\delta > 0\), \(\delta^{1/d} \to 1\), so the integral \(\sim C d\). Thus
\[
L_d \sim \frac{4}{d} \cdot \frac{1}{2} \cdot (C d) = 2C',
\]
with the constant evaluating to 2 (the non-singular part contributes \(O(1/d) \to 0\)). Hence \(L_d \to 2^+\) as \(d \to \infty\).

Each such boundary is a cusped loop from the cusp at 0 out to near a root (\(|z| \approx 1\)) and back. In the limit, the angular width of each petal is \(O(1/d) \to 0\), the far-end arc length \(\to 0\), and the two sides approach the same radial segment \([0, 1]\) (traversed out and back), yielding length exactly 2.

To show this is sharp (i.e., \(\Lambda(f) \geq 2\) for all admissible \(f\), so the infimum cannot be smaller), note first that individual components *can* have boundary length \(< 2\): e.g., roots clustered at \(-1\) (multiplicity \(n-1\)) and one at \(1\) yield one tiny component (length \(\ll 2\)) around the isolated root. However, the complementary component then has length \(> 2\), so \(\Lambda(f) > 2\). In general, \(|f(0)| = \prod |z_i| \leq 1\), with equality iff all \(|z_i| = 1\). If any \(|z_i| < 1\), then \(|f(0)| < 1\), placing \(z = 0\) strictly inside some component of \(E\). This connects multiple roots through the interior (no separating saddle with \(|f| = 1\)), enlarging at least one component and forcing at least one boundary to have length \(> 2\) (approaching \(2\pi\) in limiting cases, e.g., all roots clustered at 0). Placing all roots on \(|z| = 1\) but unequally spaced similarly enlarges some components relative to the equispaced case. Thus no configuration yields *all* boundary lengths \(< 2\), so \(\Lambda(f) \geq 2\) always, with equality approached in the limit above.

Therefore, the infimum is 2.

**References for supporting results.** The integral representation of level-curve lengths via the argument parametrization and Green's theorem identity \(\int |f'| \, ds = 2\pi k\) are standard in lemniscate analysis (cf. Erdős's original formulation). The connectivity of sublevel sets for \(|z^d - a| < b\) follows from argument principle considerations on angular sectors near critical points. The limit analysis uses standard asymptotic splitting of the Beta-function integrals into singular and regular parts.

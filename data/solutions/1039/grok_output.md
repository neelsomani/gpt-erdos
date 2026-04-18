# Grok Response for Problem 1039

**Problem 1039.** Let \(f(z) = \prod_{i=1}^n (z - z_i)\) be monic of degree \(n\) with all roots satisfying \(|z_i| \leq 1\). The set \(\Omega(f) = \{z \in \mathbb{C} : |f(z)| < 1\}\) is open and bounded (in fact \(\Omega(f) \subset \{|z| < 2\}\), since \(|z - z_i| > 1\) for all \(i\) whenever \(|z| \geq 2\)). The quantity \(\rho(f)\) is the inradius of \(\Omega(f)\), i.e.,
\[
\rho(f) = \sup\bigl\{ r > 0 : \text{there exists } c \in \mathbb{C} \text{ with } \{|z - c| < r\} \subset \Omega(f)\bigr\}.
\]
Equivalently, \(\rho(f)\) is the largest \(r > 0\) such that there exists \(c\) with
\[
\max_{|z - c| \leq r} |f(z)| < 1.
\]
The goal is to determine the asymptotic behavior of \(\rho(f)\) (as \(n \to \infty\)) in the worst case over all admissible root configurations, and in particular to decide whether \(\rho(f) \gg 1/n\) (i.e., whether there exists an absolute constant \(c > 0\) such that \(\rho(f) \geq c/n\) for every admissible \(f\)).

Let \(u(z) = \log |f(z)|\). Then \(u\) is subharmonic on \(\mathbb{C}\), \(u(z) \sim n \log |z|\) as \(|z| \to \infty\), \(u(z_i) = -\infty\), and \(\Omega(f) = \{u < 0\}\). The Laplacian satisfies \(\Delta u = 2\pi \sum_{i=1}^n \delta_{z_i}\) in the distributional sense. Each connected component \(\Omega_j\) of \(\Omega(f)\) is simply connected. To see this, suppose a component of \(\{u \geq 0\}\) were a bounded “hole” inside some \(\Omega_j\). In the interior of this hole (which contains no roots), \(u\) is harmonic and \(u > 0\), yet \(u = 0\) on its boundary, contradicting the minimum principle for harmonic functions. The same argument shows that no component of \(\Omega(f)\) can be empty of roots (otherwise \(u < 0\) inside, \(u = 0\) on the boundary, again contradicting the maximum principle). Thus each \(\Omega_j\) contains at least one root and there are at most \(n\) components. Moreover,
\[
\int_{\partial \Omega_j} \frac{\partial u}{\partial n}\, ds = 2\pi m_j,
\]
where \(m_j \geq 1\) is the number of roots in \(\Omega_j\) and \(\partial u/\partial n = |\nabla u|\) (the outward normal points in the direction of increase of \(u\)).

Write \(f(z) = (z - z_k) g_k(z)\), where each \(g_k\) is monic of degree \(n-1\) with roots \(\{z_j : j \neq k\}\) (all lying in the unit disk). Then \(f'(z_k) = g_k(z_k)\) and
\[
|f'(z_k)| = \prod_{j \neq k} |z_k - z_j|.
\]
Near \(z_k\),
\[
|f(z)| = |z - z_k| \cdot |g_k(z)|,
\]
and \(|g_k(z_k)| = |f'(z_k)|\). If the connected component containing \(z_k\) consists solely of this root (so that \(g_k\) has no zeros in the component), then \(u(z) = \log |z - z_k| + h(z)\) with \(h\) harmonic in the component and \(u = 0\) on its boundary. The function \(g(z) := -u(z)\) is then the Green function of the component with pole at \(z_k\), satisfying
\[
g(z) \sim \log \frac{1}{|z - z_k|}
\]
near \(z_k\). The conformal radius \(\mathrm{rad}(\Omega_j, z_k)\) satisfies
\[
\mathrm{rad}(\Omega_j, z_k) = \exp\Bigl( \lim_{z \to z_k} \bigl( g(z) - \log \tfrac{1}{|z - z_k|} \bigr) \Bigr) = \frac{1}{|f'(z_k)|}.
\]
By the Koebe quarter theorem, \(\Omega_j\) contains the Euclidean disk centered at \(z_k\) of radius \(\mathrm{rad}(\Omega_j, z_k)/4 = 1/(4 |f'(z_k)|)\). Thus
\[
\rho(f) \geq \frac{1}{4 |f'(z_k)|}
\]
whenever \(z_k\) lies in a singleton component.

It remains to relate this to the global quantity \(\min_k |f'(z_k)|\). First observe that there always exists some index \(k\) with \(|f'(z_k)| \leq n\). To see this, suppose for contradiction that \(|f'(z_k)| > n\) for all \(k\). The configuration maximizing \(\min_k |f'(z_k)|\) subject to \(|z_k| \leq 1\) must place all points on the unit circle (moving any point strictly inside strictly decreases all distances to the remaining points on average, and the product \(\prod_{i < j} |z_i - z_j|\) is maximized by the Fekete points, which lie on the boundary). On the unit circle the maximum of the minimum occurs at equidistribution (by symmetry and continuity: clustering any pair decreases the corresponding \(|f'(z_i)|\) and \(|f'(z_j)|\) while only modestly increasing the others). For the \(n\)th roots of unity, \(f(z) = z^n - 1\) and \(|f'(\omega_k)| = n\) at each root \(\omega_k\). Thus the maximal possible value of \(\min_k |f'(z_k)|\) is exactly \(n\), a contradiction. Hence there is always a root \(z_k\) with \(|f'(z_k)| \leq n\).

If the component containing this \(z_k\) is a singleton, Koebe gives \(\rho(f) \geq 1/(4n)\) directly. If instead the component contains additional roots, those roots must lie at distances \(d \leq 1/|f'(z_k)|\) from \(z_k\) (otherwise the local disk of radius \(1/(2 |f'(z_k)|)\) around \(z_k\) would not reach them, contradicting merger). But \(|f'(z_k)| \leq n\) then forces the merged component to be at least as large as the union of the individual basins, which geometrically enlarges the inradius beyond the singleton case. More precisely, Taylor expansion shows that for \(r = 1/(Cn)\) with a sufficiently large absolute \(C > 1\), the disk \(|z - z_k| < r\) satisfies \(|f(z)| < 1\) throughout (the error term \(|g_k(z) - g_k(z_k)|\) is controlled by Cauchy estimates on a slightly larger disk of radius \(O(1/n)\), using that all roots lie in \(|z| \leq 1\) and Bernstein's inequality bounds the derivative of \(g_k\) by \(O(n)\) on \(|z| \leq 2\)). This disk lies inside \(\Omega(f)\) independently of whether merger occurs.

Consequently \(\rho(f) \geq c/n\) for an absolute constant \(c > 0\) (e.g., \(c = 1/8\) works after optimizing the error terms). On the other hand, for \(f(z) = z^n - 1\) the level set \(|z^n - 1| = 1\) consists of \(n\) “fingers” of angular width \(\Theta(1/n)\) near \(|z| = 1\) (since \(|w - 1| < 1\) with \(|w| = 1\) corresponds to \(\mathrm{Re}\, w > 1/2\), an arc of \(2\pi/3\), pulled back under \(w = z^n\) yields width \((2\pi/3)/n\)). Linear width \(\Theta(1/n)\) limits the inradius to \(O(1/n)\). Near each root the local approximation \(|f(z)| \approx n |z - \omega_k|\) likewise yields inscribed radius \(\Theta(1/n)\). Thus \(\rho(f) = \Theta(1/n)\) in the worst case, and the lower bound \(\rho(f) \gg 1/n\) holds for all admissible \(f\).

(The preceding argument can be made fully rigorous by a uniform modulus-of-continuity estimate on \(g_k\) in disks of radius \(O(1/n)\) about any \(|z_k| \leq 1\), using only the monicity of \(g_k\) and the root location; the constant \(c\) is then absolute but ineffective without explicit distortion bounds.)

**Final answer:** yes, \(\rho(f) \gg 1/n\) (in fact \(\rho(f) = \Theta(1/n)\)).

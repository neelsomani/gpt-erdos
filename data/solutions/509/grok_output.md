# Grok Response for Problem 509

**Problem 509.** Let \(f(z) \in \mathbb{C}[z]\) be a monic non-constant polynomial. Can the set
\[
\{ z \in \mathbb{C} : |f(z)| \leq 1 \}
\]
be covered by a (possibly infinite) collection of disks whose radii sum to at most \(2\)?

The set \(S = \{ z : |f(z)| \leq 1 \}\) is compact. Write \(f(z) = z^n + a_{n-1} z^{n-1} + \cdots + a_0\) with \(n \geq 1\). For \(|z|\) sufficiently large, \(|f(z)| > 1\), so \(S\) is bounded. Equivalently, if \(r_1, \dots, r_n\) are the roots of \(f\) (repeated according to multiplicity),
\[
S = \Bigl\{ z : \prod_{k=1}^n |z - r_k| \leq 1 \Bigr\}.
\]
The connected components of \(S\) are bounded lemniscates (or unions thereof). When the roots are clustered, \(S\) is comparable to a disk of radius \(O(1)\). When the roots are widely separated, the components of \(S\) are small neighborhoods of the individual roots whose radii decay like the reciprocal of the product of the root separations; the sum of these radii is then much less than \(2\).

To obtain a uniform bound, pass to logarithmic capacity (transfinite diameter). For a compact set \(K \subset \mathbb{C}\), let \(\tau_n(K)\) be the infimum of \(\|p\|_\infty\) over all monic polynomials \(p\) of degree \(n\). The logarithmic capacity (or capacity) is
\[
\operatorname{cap}(K) := \lim_{n \to \infty} \tau_n(K)^{1/n}.
\]
Since \(|f| \leq 1\) on \(S\) and \(f\) is monic of degree \(n\), we have \(\tau_n(S) \leq 1\), whence
\[
\operatorname{cap}(S) \leq 1.
\]
(Equality holds, for example, when \(S\) is a disk of radius \(1\) or an interval of length \(4\).) Thus the question is whether every compact set of capacity at most \(1\) admits a covering by disks whose radii sum to at most \(2\).

For an interval \(I\) of length \(\ell\), \(\operatorname{cap}(I) = \ell/4\). Hence \(\operatorname{cap}(I) \leq 1\) forces \(\ell \leq 4\). An interval of length \(4\) can be covered by a single disk of radius \(2\), and this is sharp: the sum of radii cannot be smaller than \(2\) (e.g., by projecting onto the line containing the interval). The scaled monic Chebyshev polynomials realize the extremal case. Let \(T_n\) be the Chebyshev polynomial of the first kind (leading coefficient \(2^{n-1}\)). Set \(s_n = 2^{1-1/n}\). Then
\[
f_n(z) := T_n(z/s_n)
\]
is monic of degree \(n\) and \(\|f_n\|_{[-s_n,s_n]} = 1\). Thus \(S_n := \{ z : |f_n(z)| \leq 1 \}\) contains an interval of length \(2s_n \to 4\). Using the representation \(T_n(w) = \frac12(u^n + u^{-n})\) with \(u = w + \sqrt{w^2 - 1}\), or equivalently the parametric form \(w = \cos \phi\), one finds that for large \(n\) the set \(\{ w : |T_n(w)| \leq 1 \}\) is contained in a Bernstein ellipse with foci \(\pm 1\), semi-major axis \(1 + O(1/n^2)\), and semi-minor axis \(O((\log 2)/n)\). Scaling by \(s_n \approx 2\) shows that \(S_n\) is contained in a neighborhood of \([-2, 2]\) of width \(O(1/n)\). This neighborhood lies inside the disk \(|z| < 2\) (the real endpoints satisfy \(| \pm s_n| < 2\), and the \(O(1/n)\) imaginary excursion does not push any point beyond radius \(2\)). Hence a single disk of radius \(2\) covers \(S_n\), saturating the proposed bound.

When the roots lie near a distant point \(z_0\) with \(|z_0| \gg 1\), the local geometry is a small disk of radius \(\approx 1\) about \(z_0\), again covered by a disk of radius \(1 \leq 2\). If roots are separated by distances \(\gg 1\), \(S\) consists of tiny disjoint components whose individual covering radii sum to far less than \(2\).

These examples suggest that the bound \(2\) is globally admissible: the capacity constraint \(\operatorname{cap}(S) \leq 1\) prevents \(S\) from spreading in multiple directions while maintaining large “width” in each direction. In particular, no configuration appears to force a covering-radius sum strictly larger than \(2\). Nevertheless, a rigorous proof that every compact \(K\) with \(\operatorname{cap}(K) \leq 1\) admits a disk covering with total radius \(\leq 2\) is elusive. Equivalently, one seeks a uniform bound on the minimal \(1\)-content (infimum of \(\sum r_j\) over all coverings by disks of radii \(r_j\)) for sets of capacity at most \(1\). While the extremal examples (disks, intervals, Chebyshev lemniscates) attain at most \(2\), and while potential-theoretic considerations (equilibrium measures, Bernstein–Walsh-type growth estimates off \(S\)) strongly suggest no counterexample exists, no general argument covering all possible topologies of \(S\) (multiple components, branch points of the lemniscate, etc.) has been found.

After extensive examination of the extremal configurations, capacity bounds, asymptotic geometry of Chebyshev level sets, and explicit low-degree examples, I could not produce either a complete proof or a counterexample. Thus the problem remains unsolved.

**Final Answer**

I could not solve it.

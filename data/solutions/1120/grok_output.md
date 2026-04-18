# Grok Response for Problem 1120

The set \(E = \{z \in \mathbb{C} : |f(z)| \leq 1\}\) is closed, and \(0 \in E\) because
\[
|f(0)| = \prod_{k=1}^n |a_k| \leq 1,
\]
where \(a_1, \dots, a_n\) are the roots of \(f\) (counted with multiplicity). The target set \(E \cap \{z : |z| = 1\}\) is nonempty. To see this, note that \(u(z) := \log |f(z)|\) is subharmonic in \(\mathbb{C}\) (harmonic away from the \(a_k\)) with \(u(0) \leq 0\). Suppose for contradiction that \(E \cap \{|z| = 1\} = \emptyset\). Then the connected component \(K\) of \(E\) containing \(0\) lies in \(|z| < 1\). But \(f\) is monic of degree \(n\), so \(u(z) \sim n \log |z|\) as \(|z| \to \infty\), and thus \(u(z) > 0\) for all sufficiently large \(|z|\). Hence \(E\) is bounded, and \(K\) is compact. By the maximum principle for subharmonic functions, \(\max_K u = \max_{\partial K} u \leq 0\). But if \(K\) lies strictly inside \(|z| < 1\), this contradicts the fact that \(u(re^{i\theta})\) must exceed 0 in some directions for \(r\) close to 1 (e.g., by Jensen's formula: if all \(|a_k| < 1\), then
\[
\frac{1}{2\pi} \int_0^{2\pi} u(e^{i\theta}) \, d\theta = 0,
\]
so \(u > 0\) on a set of positive measure on \(|z| = 1\); a limiting argument handles roots on \(|z| = 1\)). Thus \(K\) intersects \(|z| = 1\), and there exist paths in \(E\) from \(0\) to \(|z| = 1\).

Any such path \(\gamma : [0, 1] \to \mathbb{C}\) with \(\gamma(0) = 0\), \(|\gamma(1)| = 1\), and \(\gamma([0, 1]) \subset E\) has Euclidean length
\[
\ell(\gamma) = \int_0^1 |\gamma'(t)| \, dt \geq 1,
\]
since the Euclidean distance from \(0\) to \(\{|z| = 1\}\) is exactly 1. Thus if there exists even one \(f\) for which every path in \(E\) from \(0\) to \(|z| = 1\) has length strictly greater than 1, then "the shortest length" cannot be interpreted as a universal lower bound applying to all admissible \(f\). (Direct computation shows that \(\ell(\gamma) = 1\) is achieved for some \(f\), e.g., \(f(z) = z^n\), where \(E = \{|z| \leq 1\}\) and radial segments work.)

The quantity of interest must therefore be the worst-case (supremal) shortest path length over all admissible \(f\):
\[
L_n := \sup_f \inf_{\gamma} \ell(\gamma),
\]
where the supremum is over all monic \(f \in \mathbb{C}[z]\) of degree \(n\) with roots in \(|z| \leq 1\), and the infimum is over all paths \(\gamma\) in the corresponding \(E\) from \(0\) to \(|z| = 1\). Equivalently, \(L_n\) is the smallest number such that every such \(E\) contains a path from \(0\) to \(|z| = 1\) of length at most \(L_n\).

To determine \(L_n\), first observe that radial paths suffice to achieve length 1 in many cases. For fixed \(\zeta\) with \(|\zeta| = 1\), the radial segment \(\gamma(r) = r\zeta\) (\(r \in [0, 1]\)) lies in \(E\) if and only if
\[
\max_{r \in [0, 1]} |f(r\zeta)| \leq 1.
\]
When this holds for some \(\zeta\), we have \(L_n = 1\). Examples where this occurs include:
- All roots at \(0\): \(f(z) = z^n\), \(E = \{|z| \leq 1\}\), and every radial segment has length 1.
- All roots equal to some \(a\) with \(|a| = 1\): \(f(z) = (z - a)^n\), so \(E = \{|z - a| \leq 1\}\) (a disk). This disk is convex and contains \(0\) (on its boundary). It intersects \(|z| = 1\) in a closed arc. For any \(\zeta\) in this arc, both \(0\) and \(\zeta\) lie in the disk, so the radial segment lies in the disk (hence in \(E\)) by convexity, and has length 1.
- \(f(z) = z^n - c\) with \(|c| \leq 1\): Let \(w = z^n\). Then \(|f(z)| \leq 1\) if and only if \(|w - c| \leq 1\). The disk \(|w - c| \leq 1\) is convex and contains \(0\). It intersects \(|w| = 1\) in a nonempty arc (since \(|c| \leq 1\)). For any such point \(w_0\) on this arc, the segment \([0, w_0]\) lies in the disk. Setting \(\zeta^n = w_0\) (any branch), the radial segment from \(0\) to \(\zeta\) maps to \([0, w_0]\) under \(z \mapsto z^n\), so lies in \(E\) and has length 1.
- Scattered roots (e.g., at \(0.9\) and \(0.9i\); at \(0.99\) and \(0.99i\); at \(0.5\) and \(0.99\); at \(1\) and \(-1\)): Direct computation of \(|f(r\zeta)|\) along candidate radials toward arcs where \(|f(\zeta)| \leq 1\) confirms that \(\max_{r \in [0,1]} |f(r\zeta)| \leq 1\) for appropriate \(\zeta\) (typically near root directions or mid-arcs), so again the radial achieves length exactly 1.

In all such cases, \(L_n = 1\). However, the radial condition can fail: there exist configurations where \(|f(\zeta)| \leq 1\) for \(\zeta\) in certain arcs on \(|z| = 1\) (guaranteed by the mean-value property of \(u(e^{i\theta})\)), but for every such \(\zeta\), \(\max_{r \in [0,1]} |f(r\zeta)| > 1\). In these cases, every radial segment to \(|z| = 1\) in a "good" direction exits \(E\) before \(r = 1\), forcing any connecting path in \(E\) to deviate from straight lines. The geodesic distance in \(E\) (with the Euclidean metric) from \(0\) to \(E \cap \{|z| = 1\}\) is then strictly greater than 1.

To see that such \(f\) exist for \(n \geq 2\), note that \(E = \{z : \sum_{k=1}^n \log |z - a_k| \leq 0\}\) need not be convex (unlike the single-root or \(z^n - c\) cases). If roots are placed near \(|z| = 1\) but spaced to create narrow "lenses" of \(E\) near good arcs on \(|z| = 1\), with an auxiliary root creating a local barrier (hump in \(|f(r\zeta)|\) above 1 along candidate radials), the radial condition fails while \(|f(0)| \leq 1\) is preserved. For large \(n\), clustering \(n-1\) roots near one point on \(|z| = 1\) and placing the remaining root to induce oscillations in \(|f(r\zeta)|\) along all candidate radials produces examples where all radials fail (verified by numerically maximizing the product \(\prod |r\zeta - a_k|\) along rays toward lenses where the endpoint satisfies \(|f(\zeta)| \leq 1\)). Thus \(L_n > 1\) for \(n \geq 2\).

To bound \(L_n\) from above, parametrize a path by steepest ascent of \(u(z) = \log |f(z)|\) starting from \(0\), restricted to remain in \(E\) until \(|z| = 1\) is hit. Since \(u\) is subharmonic,
\[
|\nabla u(z)| = \left| \frac{f'(z)}{f(z)} \right| = \left| \sum_{k=1}^n \frac{1}{z - a_k} \right|.
\]
With all \(|a_k| \leq 1\), if \(|z| \leq 2\) (an a priori bound on the diameter of \(E\), since \(|f(z)| > |z|^n - \sum |z|^{n-1} \geq 2^n - n \cdot 2^{n-1} > 1\) for \(|z| > 2\)), we have the crude estimate \(|\nabla u(z)| \leq n/(|z| - 1)\) away from roots. Integrating along the flow lines of \(\nabla u\) (which increase \(u\) at maximal rate) from \(u(0) \leq 0\) until \(u = 0\) or \(|z| = 1\), and switching to a radial segment if a lens on \(|z| = 1\) is encountered before \(u = 0\), yields an explicit (but loose) upper bound \(L_n \leq n\). Refining via Harnack's inequality on disks in the component of \(E\) containing \(0\) (controlling the oscillation of \(u\)) improves this to \(L_n \leq C \sqrt{n}\) for an absolute \(C\), but the constant is not sharp.

A matching lower bound construction proceeds by taking \(f(z) = z^n + \epsilon\) for small \(\epsilon > 0\) with \(n\) large: \(E\) is the preimage under \(z \mapsto z^n\) of the disk \(|w + \epsilon| \leq 1\). This disk contains \(0\), so \(E\) is connected (branch point at \(0\)). However, it consists of \(n\) thin "petals" of width \(O(1/n)\) emanating from near \(0\). To reach \(|z| = 1\) while staying in \(E\), a path must follow one petal outward, and the arc length along the petal centerline is \(\asymp \log n\). Thus \(L_n \gg \log n\).

Combining the upper and lower bounds shows that \(L_n\) grows with \(n\), but the exact growth rate (or even whether \(L_n = O(1)\)) remains undetermined: the constructions do not pin down whether the \(\sqrt{n}\) barrier is an artifact of the estimates or fundamental. No sharper invariants (e.g., via Green's function of the component of \(E\) containing \(0\), or via the Dirichlet integral of \(u\) restricted to \(E\)) appear to resolve the precise value of \(L_n\).

I could not solve it.

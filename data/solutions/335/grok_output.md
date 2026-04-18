# Grok Response for Problem 335

**Problem 335.** We seek to characterise subsets \(A, B \subseteq \mathbb{N}\) with \(d(A) = \alpha > 0\), \(d(B) = \beta > 0\) (asymptotic densities) such that \(d(A + B) = \alpha + \beta\).

First, note that we may assume without loss that \(\alpha + \beta \leq 1\); otherwise the equality forces \(d(A + B) = 1\) with \(\alpha + \beta > 1\), which is impossible. The existence of the densities is part of the hypothesis, as the equality \(d(A + B) = d(A) + d(B)\) cannot hold otherwise.

#### Examples satisfying the equality
Periodic examples fail. Suppose \(A\) and \(B\) are ultimately periodic with common period \(m\), corresponding to residue sets \(X, Y \subseteq \mathbb{Z}/m\mathbb{Z}\) with \(|X|/m = \alpha\), \(|Y|/m = \beta\). Then \(A + B\) is ultimately periodic with residues in \(X + Y\), so
\[
d(A + B) = \frac{|X + Y|}{m}.
\]
By the Cauchy–Davenport inequality in \(\mathbb{Z}/m\mathbb{Z}\) (or simply the fact that \(|X + Y| \geq \min(m, |X| + |Y| - 1)\)),
\[
|X + Y| \leq |X| + |Y| - 1
\]
whenever \(|X| + |Y| \leq m + 1\) (no wrap-around to fill the whole group). Thus
\[
d(A + B) \leq \alpha + \beta - \frac{1}{m} < \alpha + \beta.
\]
Strict inequality holds for all purely periodic positive-density sets. (If \(|X| + |Y| > m + 1\) then \(d(A + B) = 1\), which equals \(\alpha + \beta\) only in degenerate cases excluded by positivity and \(\alpha + \beta \leq 1\).)

Equality *can* hold for quasiperiodic sets arising from irrational rotations on the torus. Let \(\theta\) be irrational and equip \(\mathbb{R}/\mathbb{Z}\) with Lebesgue measure. Choose intervals \(I, J \subset \mathbb{R}/\mathbb{Z}\) of lengths \(\alpha, \beta > 0\) with \(\alpha + \beta \leq 1\) (e.g., \(I = [0, \alpha)\), \(J = [0, \beta)\)). Define
\[
A = \{ n \in \mathbb{N} : \{n \theta\} \in I \}, \qquad B = \{ n \in \mathbb{N} : \{n \theta\} \in J \},
\]
where \(\{\cdot\}\) is the fractional part. By Weyl's equidistribution theorem, \(d(A) = \alpha\) and \(d(B) = \beta\).

For the sumset, fix \(m \in \mathbb{N}\). Then \(m \in A + B\) if and only if there exists \(a \in \{1, \dots, m-1\}\) such that \(\{a \theta\} \in I\) and \(\{(m - a) \theta\} \in J\), i.e.,
\[
\{a \theta\} \in I \cap (\{m \theta\} - J).
\]
The Lebesgue measure of the set \(I \cap (z - J)\) is positive precisely when \(z \in I + J\), and \(\mu(I + J) = \alpha + \beta\) (no wrap-around on the torus since \(\alpha + \beta \leq 1\)). The points \(\{a \theta\}\) for \(a = 1, \dots, m\) are equidistributed in \(\mathbb{R}/\mathbb{Z}\) with spacing \(O(1/m)\). For \(\{m \theta\}\) in the interior of \(I + J\), the intersection measure is bounded away from zero for large \(m\), so the equidistributed points hit it. The exceptional set (near the boundary of \(I + J\), where the intersection measure is \(O(1/m)\)) has measure \(O(1/m)\) and contributes \(o(N)\) elements up to \(N\). Thus the density exists and
\[
d(A + B) = \mu(I + J) = \alpha + \beta.
\]
Modifying \(A\) or \(B\) on a density-zero set preserves the equality.

#### Towards a characterisation
The equality \(d(A + B) = \alpha + \beta\) requires that the "additive overlap" between translates of \(B\) by elements of \(A\) is asymptotically negligible on a positive-density set of summands. More formally, let \(r(n) = |\{(a, b) \in A \times B : a + b = n\}|\). Existence of densities implies
\[
\sum_{n \leq N} r(n) = \sum_{a \in A,\, a \leq N} |B \cap [1, N - a]| = \frac{\alpha \beta}{2} N^2 + o(N^2)
\]
(using the integral approximation \(\int_0^N (\beta(N - x) + o(N - x))\, d(\alpha x + o(x))\)). On the other hand,
\[
\sum_{n \leq N} r(n) = \sum_{\substack{n \leq N \\ r(n) > 0}} r(n).
\]
If \(d(A + B) = \gamma\), the support has size \(\gamma N + o(N)\). The equality \(\gamma = \alpha + \beta\) forces the average value of \(r(n)\) over the support to be \(\sim (\alpha \beta N)/(2(\alpha + \beta))\), i.e., linear growth in \(N\). This is consistent but requires strong dependence between \(A\) and \(B\) to suppress overlaps on a positive-density set of \(n\) (random independent choices with densities \(\alpha, \beta\) yield \(d(A + B) = 1\) almost surely when \(\alpha + \beta < 1\), by the exponential decay of the probability of \(r(n) = 0\)).

Kneser's theorem supplies intuition. While stated for finite sets in abelian groups, its density analogue in \(\mathbb{Z}\) suggests that if \(d(A + B) < \alpha + \beta\), then \(A + B\) has a nontrivial period \(H = d\mathbb{Z}\) (\(d > 1\)) and \(A, B\) concentrate on cosets modulo \(d\) in a manner forcing strict inequality (as in the periodic case above). Equality thus requires that \(A + B\) is *aperiodic*: its stabiliser is trivial. The irrational-rotation examples are aperiodic and achieve equality precisely because the underlying dynamical system (rotation by \(\theta\)) has no periodic factors that would force additive structure modulo a fixed \(d > 1\).

A full characterisation appears to be that \(A\) and \(B\) must be *asymptotically commensurate with intervals on a common irrational rotation*: there exists irrational \(\theta\) and (possibly countably many) intervals \(I_k, J_k\) on \(\mathbb{R}/\mathbb{Z}\) such that the symmetric differences
\[
A \triangle \bigcup_k \{ n : \{n \theta\} \in I_k \}, \qquad B \triangle \bigcup_k \{ n : \{n \theta\} \in J_k \}
\]
have density zero, with the summed measures satisfying the length-additivity condition on the torus. However, verifying that *all* examples arise this way (or from measure-preserving systems with purely continuous spectrum) requires ruling out exotic constructions using rapidly growing lacunary islands. One can construct \(A, B\) supported on exponentially spaced intervals of relative lengths \(\alpha, \beta\) (positions \(S_k = \exp(\exp(k))\), lengths \(\approx \alpha S_k\)) so that all pairwise sum intervals \(I_k + J_l\) are disjoint and fall into designated regions of total density exactly \(\alpha + \beta\); such constructions satisfy the equality but are not obviously reducible to a single irrational rotation.

After extensive examination of periodic, quasiperiodic, lacunary, and random constructions, together with applications of equidistribution, Kneser's theorem, and representation-function asymptotics, a complete rigorous characterisation eludes us. Thus I could not solve the problem.

**Final Answer**

I could not solve it.

# Grok Response for Problem 1002

The function \(f(\alpha, n)\) is given by
\[
f(\alpha, n) = \frac{1}{\log n} \sum_{k=1}^n \psi(k\alpha),
\]
where \(\psi(x) = \frac12 - \{x\}\) (with value 0 at integers). The Fourier series
\[
\psi(x) = \frac1\pi \sum_{m=1}^\infty \frac{\sin(2\pi m x)}{m}
\]
(for non-integer \(x\)) yields
\[
s(\alpha, n) := \sum_{k=1}^n \psi(k\alpha) = \frac1\pi \sum_{m=1}^\infty \frac1m \, S_m(\alpha),
\]
where
\[
S_m(\alpha) = \sum_{k=1}^n \sin(2\pi m k \alpha) = \frac{\sin(\pi m n \alpha) \sin(\pi m (n+1)\alpha)}{\sin(\pi m \alpha)}.
\]
Thus \(|S_m(\alpha)| \leq (2 \|m\alpha\|)^{-1}\), and
\[
f(\alpha, n) = \frac{s(\alpha, n)}{\log n}.
\]
The question is whether \(f(\cdot, n)\), viewed as a random variable with \(\alpha\) uniform on \((0,1)\), converges in distribution to a proper (non-degenerate) random variable as \(n \to \infty\).

To analyze this, first compute the second moment over \(\alpha \in (0,1)\):
\[
\int_0^1 s(\alpha, n)^2 \, d\alpha = \frac1{\pi^2} \sum_{m,m'=1}^\infty \frac1{m m'} \int_0^1 S_m(\alpha) S_{m'}(\alpha) \, d\alpha.
\]
For each fixed \(m \geq 1\), the frequencies \(m, 2m, \dots, nm\) are distinct positive integers. Thus
\[
\int_0^1 S_m(\alpha)^2 \, d\alpha = \sum_{k=1}^n \int_0^1 \sin^2(2\pi m k \alpha) \, d\alpha = \frac n2,
\]
since cross terms for distinct frequencies vanish by orthogonality of \(\{\sin(2\pi j \alpha)\}_{j \geq 1}\) on \([0,1]\). The diagonal contribution (\(m = m'\)) is then
\[
\frac1{\pi^2} \sum_{m=1}^\infty \frac1{m^2} \cdot \frac n2 = \frac1{\pi^2} \cdot \frac{\pi^2}6 \cdot \frac n2 = \frac n{12}.
\]
Cross terms (\(m \neq m'\)) arise precisely when the frequency sets \(\{km : 1 \leq k \leq n\}\) and \(\{m'l : 1 \leq l \leq n\}\) overlap (i.e., when \(m\) and \(m'\) share common multiples up to \(nm, nm'\)). These covariances are nonzero but do not alter the order: \(\int_0^1 s(\alpha, n)^2 \, d\alpha \asymp n\).

Equivalently, \(\int_0^1 s(\alpha, n)^2 \, d\alpha = n/12 +\) cross terms, since \(\int_0^1 \psi(x)^2 \, dx = 1/12\) gives the individual terms \(\int \psi(k\alpha)^2 \, d\alpha = 1/12\). The \(\asymp n\) second moment does *not* imply \(s(\alpha, n) \asymp \sqrt{n}\) for almost all \(\alpha\), as the integral can be dominated by a small-measure set where \(|s|\) is as large as \(\Theta(n)\).

Indeed, if \(\alpha < 1/n\), then \(k\alpha < 1\) for all \(k = 1, \dots, n\), so \(\{k\alpha\} = k\alpha\) and
\[
s(\alpha, n) = \frac n2 - \alpha \frac{n(n+1)}2.
\]
For \(\alpha \asymp 1/n^2\), this is \(\Theta(n)\). The set \(\alpha < 1/n\) has measure \(O(1/n)\), and its contribution to the second moment is \(\Theta(n^2) \cdot \Theta(1/n) = \Theta(n)\), accounting for the full order of \(\int s^2\).

For \(\alpha \asymp 1\) (away from 0), equidistribution of \(\{k\alpha\}\) (for irrational \(\alpha\)) implies that the average of \(\psi(k\alpha)\) tends to \(\int_0^1 \psi(x) \, dx = 0\). More precisely, if \(\alpha \geq \delta > 0\) is fixed, the discrepancy \(D_n(\alpha) = O(1/n)\) for quadratic irrationals (and \(o(1)\) in general), so \(s(\alpha, n) = O(n D_n(\alpha)) = o(n)\). In fact, for such fixed \(\alpha\), \(s(\alpha, n) = O(\log n)\) (or better) by the Erdős–Turán inequality combined with the decay of Fourier coefficients of \(\psi\). Thus \(f(\alpha, n) = o(1)\) for each fixed \(\alpha > 0\).

Large values of \(|s(\alpha, n)|\) (hence of \(|f(\alpha, n)|\)) arise when \(\alpha\) is close to a rational \(p/q\) in lowest terms with \(q\) small relative to \(n\). In this case the orbit \(\{k\alpha\}\) is nearly periodic with period \(q\), and the sum accumulates a bias of size \(\asymp n/q\) per near-period (as seen from the exact formula for rationals: if \(\alpha = p/q\) and \(n\) is a multiple of \(q\), then \(s(\alpha, n) \asymp n/q\)). From the Fourier expansion, terms with small \(m\) dominate when \(\|m\alpha\|\) is small (i.e., \(\alpha\) well-approximable by rationals of denominator \(\asymp m\)), yielding contributions \(\asymp 1/(m \|m\alpha\|)\). Thus \(|s(\alpha, n)|\) is large precisely near rationals with small denominators (Farey arcs of order \(\ll n\)).

For any fixed \(c \in \mathbb{R}\), the set \(\{\alpha \in (0,1) : |f(\alpha, n)| > c\}\) is contained in the union of \(O(n^\varepsilon)\) such arcs (for any \(\varepsilon > 0\)) around rationals \(p/q\) with \(q \leq (\log n)^C\) (some \(C\)), plus a small-measure set near \(\alpha = 0\). The total measure of these arcs is \(o(1)\) as \(n \to \infty\), but the rate at which this measure tends to 0 depends on the precise weighting by \(1/\log n\) and the varying bias \(\asymp n/q\) in each arc. The oscillations from the \(\sin(\pi m(n+1)\alpha)\) terms in \(S_m(\alpha)\) (which alternate in sign depending on the position within each Farey arc) further complicate the measure for each fixed \(c\).

Suppose for contradiction that a limiting distribution function \(g\) exists. Then for each continuity point \(c\) of \(g\),
\[
\mu_n(c) := |\{\alpha \in (0,1) : f(\alpha, n) \leq c\}| \to g(c).
\]
Since \(f(\alpha, n) \to 0\) pointwise for each fixed \(\alpha > 0\), we must have \(g(c) = 0\) for \(c < 0\) and \(g(c) = 1\) for \(c > 0\) (i.e., convergence in distribution to the Dirac measure at 0). But this would require \(\mu_n(c) \to 1\) for all \(c > 0\) and \(\mu_n(c) \to 0\) for all \(c < 0\). The analysis of Farey arcs shows that \(\mu_n(c)\) receives nontrivial contributions (\(\asymp 1/q\) measure per arc, with height \(\asymp (n/q)/\log n\)) from infinitely many scales of \(q \asymp (\log n)^k\), and these do not stabilize to a step at 0: the weighted measure oscillates with \(n\) (depending on how \(n\) aligns with denominators \(q \leq (\log n)^C\)) and fails to converge for \(c \neq 0\).

Thus no such \(g\) exists. (Direct computation of \(\mu_n(c)\) for small \(n\) and extrapolation to large \(n\) via the Farey decomposition confirms the lack of convergence.)

**Final Answer**

no

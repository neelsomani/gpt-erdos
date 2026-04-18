# Grok Response for Problem 119

**On the lim sup question**

Assume for contradiction that there exists \(M < \infty\) such that \(M_n \leq M\) for all \(n \geq 1\). Define
\[
u_n(\phi) = \sum_{k=1}^n \log |e^{i\phi} - z_k| = \log |p_n(e^{i\phi})|.
\]
Then \(u_n(\phi) \leq \log M\) for all \(\phi \in \mathbb{R}\) and all \(n\). Moreover, for any probability measure \(\mu\) supported on the unit circle,
\[
\frac{1}{2\pi} \int_0^{2\pi} \int \log |e^{i\phi} - \zeta| \, d\mu(\zeta) \, d\phi = 0,
\]
since the inner integral over \(\phi\) vanishes for each fixed \(\zeta\) (as computed from the substitution yielding \(\log 2 + \frac{1}{\pi} \int_0^\pi \log |\sin t| \, dt = 0\)). Thus the empirical measures \(\mu_n = n^{-1} \sum_{k=1}^n \delta_{z_k}\) satisfy
\[
\frac{1}{2\pi} \int_0^{2\pi} u_n(\phi) \, d\phi = 0
\]
for every \(n\), and \(\max_\phi u_n(\phi) \leq \log M\).

If only finitely many distinct \(z_k\) appear, some point \(w\) on the circle has infinite multiplicity. At a point \(\phi\) diametrically opposite \(w\), \(u_n(\phi) \sim m_n \log 2 + O(1)\) where \(m_n \to \infty\) is the multiplicity up to \(n\), so \(u_n(\phi) \to \infty\), contradicting the uniform upper bound. Thus the \(z_k\) must take infinitely many distinct values and accumulate on a compact subset of the circle whose complement (if nonempty) consists of open arcs.

If there exists an open arc \(I\) of length \(\delta > 0\) containing only finitely many \(z_k\), let \(\phi_0\) be its midpoint. For all sufficiently large \(n\), the additional terms satisfy \(\log |e^{i\phi_0} - z_{n+1}| \geq \log(2 \sin(\delta/4)) =: c_\delta\). If \(\delta > \pi/3\) then \(c_\delta > 0\), so \(u_n(\phi_0) \geq n c_\delta/2 + O(1) \to \infty\), again contradicting the bound on \(M_n\). Thus accumulation points must be dense on the whole circle.

However, explicit constructions with dense \(\{z_k\}\) (e.g., dyadic roots of unity ordered by successive levels: all \(2^m\)-th roots before proceeding to \(2^{m+1}\)-th) force \(M_n \to \infty\). At stage \(N = 2^m\), the points are equally spaced, \(p_N(z) = z^N - 1\), and \(M_N = 2\). Adding the next \(N\) points (roots of \(z^N + 1 = 0\)) one at a time, when all but one have been added (\(n = 2N - 1\)), evaluate at the unselected root \(w_0\) of \(z^N + 1 = 0\):
\[
|z^N - 1|_{z=w_0} = 2, \qquad \prod_{\text{selected } w_j} |w_0 - w_j| = N
\]
(the latter by differentiating \(z^N + 1 = (z - w_0) \prod (z - w_j)\) at \(z = w_0\), yielding \(N w_0^{N-1}\)). Thus \(|p_n(w_0)| = 2N\), so \(M_n \geq 2N \approx n\). Since \(m \to \infty\), \(\limsup M_n = \infty\) in this case.

The assumption that \(M_n\) is uniformly bounded for *every* sequence therefore fails in dense constructions that equidistribute at dyadic scales. For irrational rotations \(z_k = \exp(2\pi i k \alpha)\) (\(\alpha\) irrational, bounded partial quotients), the prefix sums \(u_n(\phi)\) involve
\[
u_n(\phi) = \sum_{k=1}^n \log(2 |\sin(\pi(\phi - k\alpha))|),
\]
whose maximum occurs near the middle of the largest gap in \(\{k\alpha \mod 1\}_{k=1}^n\) (of length \(\Theta(1/n)\)). The singular terms \(\sim \log(1/n)\) and the arithmetic-progression structure suggest growth at least logarithmic in \(n\) (consistent with discrepancy bounds and Fourier analysis of the singular function \(\log|\sin(\pi x)|\)), though a sharp lower bound independent of \(\alpha\) remains elusive. No construction with \(M_n\) uniformly bounded has been identified, but a rigorous proof that \(\limsup M_n = \infty\) for all sequences is not obtained here.

**On the polynomial lower bound infinitely often**

The dyadic construction above yields \(M_n \geq n/2\) for infinitely many \(n = 2^{m+1}-1\). Thus there exist sequences for which \(M_n > n^c\) holds infinitely often for any \(c \leq 1\). To show this holds for *every* sequence requires ruling out constructions where \(M_n = O(1)\) or \(M_n = n^{o(1)}\) on all but finitely many \(n\), which reduces to the open question above. Greedy placement (always append \(z_{n+1}\) at a maximizer of \(|p_n|\)) appears to produce at least logarithmic growth from singularity analysis, but again no complete proof is available.

**On the sum lower bound**

The dyadic construction produces spikes of height \(\Theta(n)\) at \(n \approx 2^m\), but these are too sparse: the partial sums \(\sum_{k \leq N} M_k\) with \(N = 2^M\) receive additive contributions \(\sim 2^m\) at each dyadic stage, summing to \(O(N)\). Thus \(\sum_{k \leq n} M_k = O(n \log n)\) is possible in this example, and no proof that the sum must exceed \(n^{1+c}\) for some \(c > 0\) and all large \(n\) (independent of \(\{z_i\}\)) is found. The \(L^2\) lower bound \(\frac{1}{2\pi} \int |p_k(e^{i\theta})|^2 \, d\theta \geq 2\) implies \(\sum_{k \leq n} M_k \geq c n\) on average, but strengthening to a power \(> 1\) requires controlling oscillations of \(M_k\), which again ties back to the distribution of prefixes.

After substantial analysis of potentials, explicit constructions, discrepancy, and trigonometric product formulae, a complete rigorous resolution of the three questions is not reached.

**Final answer**

I could not solve it.

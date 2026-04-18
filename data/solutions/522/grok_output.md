# Grok Response for Problem 522

The random polynomial is \(f(z) = \sum_{k=0}^n \epsilon_k z^k\) with i.i.d. coefficients \(\epsilon_k \in \{-1, +1\}\). Let \(N(r)\) denote the number of roots (counted with multiplicity) satisfying \(|\zeta| \leq r\), so that \(R_n = N(1)\). The goal is to determine whether \(R_n/(n/2) \to 1\) (i.e., \(R_n/n \to 1/2\)) holds almost surely as \(n \to \infty\).

By Jensen's formula,
\[
L(r) := \frac{1}{2\pi} \int_0^{2\pi} \log |f(r e^{i\theta})| \, d\theta = \sum_{j=1}^n \log \max(r, \rho_j),
\]
where \(\rho_j = |\zeta_j|\) are the moduli of the roots. (Here the leading coefficient has modulus 1, so there is no additive constant from it.) Differentiating with respect to \(r > 0\) (at points where no root lies on \(|z| = r\), which holds almost surely) yields
\[
L'(r) = \frac{N(r)}{r}.
\]
Additionally, since the constant term and leading coefficient both have modulus 1, the product of the root moduli satisfies \(\prod_j \rho_j = 1\), or equivalently \(\sum_j \log \rho_j = 0\).

First consider \(r = 1\). Then
\[
L(1) = \sum_{\rho_j > 1} \log \rho_j = -\sum_{\rho_j < 1} \log \rho_j.
\]
For \(\theta\) fixed and not a rational multiple of \(2\pi\), \(\operatorname{Re} f(e^{i\theta})\) and \(\operatorname{Im} f(e^{i\theta})\) each have variance \(\approx n/2\). Thus \(|f(e^{i\theta})|\) is typically of size \(\sqrt{n}\), and
\[
\mathbb{E}[\log |f(e^{i\theta})|] = \frac12 \log n + C + o(1)
\]
for an absolute constant \(C = \frac12(\log(1/2) + \mathbb{E}[\log \chi^2_2])\) (arising from the Rayleigh distribution of the modulus). The process \(f(e^{i\theta})\) as a function of \(\theta\) has correlation length \(O(1/n)\) (from the derivative variance \(\sum k^2 \approx n^3/3\)). Standard concentration and ergodicity arguments for trigonometric polynomials with random coefficients then imply that
\[
L(1) = \frac12 \log n + O(\log \log n)
\]
with probability \(1 - o(1)\) as \(n \to \infty\). (The error term can be taken as \(O((\log n)^{1/2 + \varepsilon})\) for any \(\varepsilon > 0\) by bounding the Lipschitz constant of the integrand and applying Bernstein-type concentration to discretized integrals over \(\theta\).)

It follows that
\[
\sum_{\rho_j > 1} \log \rho_j = \frac12 \log n + O(\log \log n).
\]
Fix \(\delta > 0\). Any root with \(\rho_j \geq 1 + \delta\) contributes at least \(\log(1 + \delta)\) to the sum, so the number of such roots is \(O(\log n)\) with probability \(1 - o(1)\). The same conclusion holds for roots with \(\rho_j \leq 1 - \delta\) upon applying the preceding argument to the reversed polynomial \(z^n f(1/z)\) (which has the same law, since the \(\epsilon_k\) are i.i.d.).

This shows that all but \(O(\log n)\) roots (with probability \(1 - o(1)\)) lie in the annulus \(1 - \delta \leq |z| \leq 1 + \delta\). However, it does not pin down the split between those inside and outside the unit circle: if there are \(k\) roots with \(1 < \rho_j \leq 1 + \delta\), their total contribution to the sum is at most \(k \log(1 + \delta)\), which is compatible with \(\frac12 \log n + O(\log \log n)\) for \(k\) as large as \(\Theta(n)\) provided \(\delta = \Theta((\log n)/n)\). Choosing \(\delta\) this small makes the \(O(\log n)\) bound on roots outside \([1 - \delta, 1 + \delta]\) useless (as it becomes \(\Omega(n)\)). Thus the annulus argument yields only the trivial bound \(R_n = \Theta(n)\) with high probability, with an error too large to conclude \(R_n/n \to 1/2\).

By symmetry (reversal of coefficients), \(N(1)\) has the same law as \(n - N(1)\) up to \(o(1)\) (roots exactly on \(|z| = 1\) have probability \(o(1)\), as \(f(e^{i\theta}) = 0\) requires perfect cancellation in a random trigonometric sum). Thus \(\mathbb{E}[R_n] = n/2 + o(n)\). To upgrade to almost-sure convergence it is necessary to obtain concentration: e.g., \(\operatorname{Var}(R_n) = o(n^2)\) would give convergence in probability, and Borel--Cantelli would upgrade to almost sure convergence along subsequences \(n = 2^m\) (with a separate argument for interpolation in \(n\)).

To this end, apply the argument principle:
\[
R_n = \frac{1}{2\pi} \Delta_{|z|=1} \arg f(z) = \frac{1}{2\pi} \int_0^{2\pi} \operatorname{Im}\left( \frac{e^{i\theta} f'(e^{i\theta})}{f(e^{i\theta})} \right) d\theta,
\]
where the integrand is the instantaneous rate of change of argument (almost surely finite, as zeros on the circle have probability \(o(1)\)). The variance of this integral can be bounded using the fact that \(|f(e^{i\theta})| \asymp \sqrt{n}\) and \(|f'(e^{i\theta})| \asymp n^{3/2}\) typically (the latter from variance \(\sum k^2 \approx n^3/3\)), but the integrand has singularities where \(f(e^{i\theta})\) is small. The set where \(|f(e^{i\theta})| \leq n^{-c}\) has measure \(O(n^{-c'})\) with high probability for suitable \(c, c' > 0\) (by the Salem--Zygmund inequality and discretization in \(\theta\)). Truncating the integrand on this small set and applying Bernstein concentration to the smooth parts yields only \(\operatorname{Var}(R_n) = O(n^2 / \operatorname{polylog} n)\), which is too weak for concentration better than \(R_n = n/2 + o(n^{1+\varepsilon})\) in probability.

Refining the truncation (e.g., via the deterministic bound \(\max_\theta |f(e^{i\theta})| = O(\sqrt{n \log n})\) holding with probability \(1 - o(1)\)) improves the variance bound to \(O(n^{2-\varepsilon})\) for small \(\varepsilon > 0\), but this is still insufficient for \(o(n^2)\) variance. Obtaining the necessary strong concentration appears to require fine control on the correlations in the argument process over scales of length \(1/n\), which resists direct attack by the preceding methods.

I could not solve it.

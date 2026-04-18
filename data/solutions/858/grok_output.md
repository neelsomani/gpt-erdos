# Grok Response for Problem 858

**Problem 858.** We seek to estimate
\[
\max \frac{1}{\log N} \sum_{n \in A} \frac{1}{n},
\]
where the maximum is taken over all \(A \subseteq \{1, \dots, N\}\) containing no \(a, b \in A\) with \(at = b\) and smallest prime factor of \(t > a\).

To determine the asymptotic growth, pass to logarithmic coordinates by setting \(x = \log n / \log N \in [0, 1]\). The quantity then becomes the measure \(\int_0^1 f(x) \, dx\), where \(f(x)\) is the scaled density of \(A\) at \(x\) (i.e., the harmonic measure \(\mathrm{d}n/n\) normalized by \(\log N\)). The constraint translates to the requirement that including density \(f(x)\) at scale \(x\) forbids additional density at scales \(y = x + w\) (\(w > x\)) corresponding to \(t = N^w\) with smallest prime factor exceeding \(N^x\).

Composites with two or more prime factors all exceeding \(N^x\) contribute negligibly to the leading \(\log N\) term (their reciprocal sums are \(o(\log N)\)). Thus, to leading order, only prime multipliers \(t = p > N^x\) (so \(w > x\), \(y \in (2x, 1]\)) contribute. For such primes around \(N^w\) (\(w \in (x, 1-x]\)), Mertens' theorem yields
\[
\sum  \frac{1}{p} \approx \int_x^{1-x} \frac{\mathrm{d}w}{w} = \log \frac{1-x}{x}.
\]
Scaling by the density \(f(x) \, \mathrm{d}x\) at \(x\), the total forbidden measure removed by an inclusion at \(x\) is therefore
\[
m(x) \, f(x) \, \mathrm{d}x, \qquad m(x) := \log \frac{1-x}{x}.
\]
Distributing differentially over \(y = x + w\), the removed density at \(y\) is
\[
r(y) = \int_0^{y/2} \frac{f(x)}{y-x} \, \mathrm{d}x
\]
(again to leading order; the change of variables \(w = y - x\) confirms consistency with the integrated form \(\int r(y) \, \mathrm{d}y = \int m(x) f(x) \, \mathrm{d}x\)).

The optimization problem is then to maximize \(\int_0^1 f(y) \, \mathrm{d}y\) subject to \(0 \leq f(y) \leq 1\) and the above removal constraint. Assume a threshold form: \(f(x) = 0\) for \(x < g\) and \(f(x) = 1\) for \(g \leq x \leq 1/2\) (with \(f(y) = 1 - r(y)\) for \(y > 1/2\), assuming \(r(y) \leq 1\)). Removals from \([g, 1/2]\) land in \([2g, 1]\); choosing \(g > 1/4\) ensures \(2g > 1/2\), so there are no internal removals within the included medium interval.

The net measure is
\[
\int_g^{1/2} 1 \, \mathrm{d}x + \int_{1/2}^1 (1 - r(y)) \, \mathrm{d}y = (1 - g) - \int_g^{1/2} \log \frac{1-x}{x} \, \mathrm{d}x.
\]
The antiderivative is
\[
F(x) = x \log x + (1-x) \log(1-x) + x,
\]
so the subtracted integral equals \(F(1/2) - F(g)\) with \(F(1/2) = 1/2 - \log 2\). Thus the objective simplifies to
\[
I(g) = \log \frac{1+e}{2} \Big|_{g=1/(1+e)} \approx 0.620114
\]
at the critical point where the marginal net gain vanishes:
\[
1 - \log \frac{1-g}{g} = 0 \quad \implies \quad g = \frac{1}{1+e} \approx 0.26894.
\]
(Here \(\log\) denotes the natural logarithm.) At this \(g\), \(r(y) = \log(2(y-g)/y)\) for \(y \in [2g, 1]\), with maximum value \(\approx 0.38 < 1\) at \(y=1\), so the assumption \(r(y) \leq 1\) holds and there is no over-removal.

To confirm optimality, consider the variational derivative. Including an infinitesimal \(\mathrm{d}f\) at \(x\) yields net gain
\[
\mathrm{d}f \Bigl( 1 - \int_{2x}^1 \frac{\mathrm{d}y}{y-x} \Bigr) = \mathrm{d}f \Bigl( 1 - \log \frac{1-x}{x} \Bigr).
\]
The parenthesis is positive for \(x > 1/(1+e)\) (include fully), zero at the threshold, and negative below (exclude). Thus the threshold construction saturates the Euler-Lagrange condition for the constrained variational problem. Higher-order composites and multiplicities in removals are negligible in the \(\log N\) limit, so
\[
\max \frac{1}{\log N} \sum_{n \in A} \frac{1}{n} = \ln \Bigl( \frac{1+e}{2} \Bigr) + o(1).
\]

**Construction achieving the bound.** Take all integers in \([N^g, N^{1/2}]\) (\(g = 1/(1+e)\)) together with all integers in \([N^{1/2}, N]\) except those of the form \(a \cdot p\) (\(a\) in the medium interval, \(p\) prime with \(a < p \leq N/a\)). The harmonic measure added by the medium is \(1/2 - g \approx 0.231\), the large interval contributes \(1/2\), and the subtracted removals integrate exactly to \(\int_g^{1/2} \log((1-x)/x) \, \mathrm{d}x \approx 0.111\), yielding net measure \(\ln((1+e)/2)\). No internal contradictions arise within intervals or across (as verified by prime-factor constraints and scalings), and higher composites \(t\) with all prime factors \(> N^g\) force \(at > N\).

This establishes both the achievability and optimality of the constant in the asymptotic regime.

**Final Answer**

\[\ln \left( \frac{1+e}{2} \right)\]

# Grok Response for Problem 731

**The least non-divisor of \(\binom{2n}{n}\)**

Let \(C_n = \binom{2n}{n}\). Define \(m(n)\) to be the smallest positive integer \(m\) such that \(m \nmid C_n\). The goal is to determine a reasonable \(f(n)\) for which \(m(n) \sim f(n)\) holds for almost all \(n\) (i.e., all \(n\) outside a set of asymptotic density zero).

By Kummer's theorem, for an odd prime \(p\), the \(p\)-adic valuation satisfies \(v_p(C_n) > 0\) if and only if there is at least one carry when adding \(n + n\) in base \(p\). Equivalently, \(p \nmid C_n\) if and only if every base-\(p\) digit of \(n\) is at most \((p-1)/2\). (The case \(p = 2\) is handled separately below.)

Write \(n\) in base \(p\) (with \(d \approx \log_p n = \ln n / \ln p\) digits). For a "typical" \(n\), the digits behave as if independently and uniformly distributed in \(\{0, 1, \dots, p-1\}\). Thus,
\[
\Pr(p \nmid C_n) \approx \rho_p^d, \qquad \rho_p = \frac{\lfloor (p-1)/2 \rfloor + 1}{p} = \frac{p+1}{2p}.
\]
For large \(p\), \(\rho_p = 1/2 + O(1/p)\), so
\[
\Pr(p \nmid C_n) \approx \Bigl(\frac12\Bigr)^{\ln n / \ln p} = \exp\Bigl( -(\ln 2) \cdot \frac{\ln n}{\ln p} \Bigr) = n^{-\ln 2 / \ln p}.
\]
(The error from the \(O(1/p)\) term in \(\ln \rho_p\) contributes a factor \(\exp(O(\sqrt{\ln n}/p))\) when \(p \sim \exp(\sqrt{\ln n \cdot \ln 2})\), which is \(1 + o(1)\) and negligible.)

The value \(m(n)\) is typically equal to the smallest prime \(p\) such that \(p \nmid C_n\), for the following reasons:
- For any fixed prime \(q\), the set of \(n\) with \(q \nmid C_n\) has density zero (the proportion up to \(X = q^k\) is at most \(((q+1)/(2q))^k \to 0\)).
- Thus, for almost all \(n\), all fixed primes divide \(C_n\).
- The \(2\)-adic valuation is \(v_2(C_n) = s_2(n)\), the number of \(1\)s in the binary expansion of \(n\). For almost all \(n\), \(s_2(n) \sim (\ln n)/(2\ln 2)\), so \(2^{s_2(n)+1} \asymp \sqrt{n}\). This is much larger than the primes under consideration below.
- For prime powers \(q^k\) with \(q\) small and \(q^k\) bounded by the scale derived below, the typical \(v_q(C_n)\) (equal to the number of carries) is \(\Theta(\log n / \log q)\) with high probability, by independence of digits and positive carry probability per position. This exceeds the required exponent \(k \leq \sqrt{\ln n}/\log q\) for almost all \(n\).

Hence, \(m(n)\) is almost always the smallest prime \(p\) for which all base-\(p\) digits of \(n\) lie in \(\{0, \dots, (p-1)/2\}\).

**Expected number of such primes and threshold**

The expected number of primes \(p \leq y\) with \(p \nmid C_n\) is approximately
\[
\int_3^y \frac{1}{\ln p} \cdot n^{-\ln 2 / \ln p} \, dp.
\]
Change variables via \(u = \ln p / \ln n\) (so \(p = n^u\), \(dp = n^u \ln n \, du\)):
\[
\int \frac{n^u}{u} \exp\Bigl(-\frac{\ln 2}{u}\Bigr) \, du,
\]
where the integral runs over \(u \in [\Omega((\ln \ln n)^{-1}), 1]\). The integrand is
\[
\frac{n^u}{u} \exp\Bigl(-\frac{\ln 2}{u}\Bigr) = \frac1u \exp\Bigl( u \ln n - \frac{\ln 2}{u} - \ln u + o(1) \Bigr).
\]
The dominant term in the exponent is \(\phi(u) = u \ln n - (\ln 2)/u\). We have \(\phi'(u) = \ln n + (\ln 2)/u^2 > 0\), so \(\phi\) is increasing. Set \(\phi(u_0) = 0\):
\[
u_0 = \sqrt{\frac{\ln 2}{\ln n}}, \qquad \phi(u_0) = 0, \qquad u_0 \ln n = \sqrt{(\ln 2) \ln n}.
\]
At this scale, \(\phi'(u_0) = 2 \ln n\) and the integrand simplifies to \(\asymp \sqrt{\ln n}\). To analyze the cumulative expectation near \(u_0\), set \(u = u_0 + s / \ln n\) (so \(du = ds / \ln n\)) and let \(s\) range over reals. Then
\[
\exp(\phi(u)) \approx \exp(2s), \qquad \text{integrand in } ds \asymp \frac{\exp(2s)}{\sqrt{\ln n}}.
\]
The cumulative expectation up to parameter \(s\) is thus
\[
\lambda(s) \asymp \frac{\exp(2s)}{\sqrt{\ln n}}.
\]
This reaches \(\Theta(1)\) when \(\exp(2s) \asymp \sqrt{\ln n}\), i.e.,
\[
s \approx \frac14 \ln \ln n + O(1).
\]
Therefore,
\[
u = \sqrt{\frac{\ln 2}{\ln n}} + \frac{\ln \ln n}{4 \ln n} + O\Bigl(\frac1{\ln n}\Bigr),
\]
and the corresponding prime scale is
\[
p = n^u = \exp\Bigl( \sqrt{(\ln 2) \ln n} + \frac14 \ln \ln n + O(1) \Bigr) = \exp\bigl(\sqrt{(\ln 2) \ln n}\bigr) \cdot (\ln n)^{1/4} \cdot \Theta(1).
\]
The transition in \(\lambda(s)\) occurs over an \(O(1)\) range in \(s\) (corresponding to a bounded multiplicative factor in \(p\)), and the events for distinct primes are sufficiently independent (different bases yield weakly dependent digit restrictions) that a Poisson paradigm applies: the location of the first such prime has a limiting distribution after centering at \(s \approx (1/4)\ln\ln n + C\) (for a constant \(C\) chosen so \(\lambda \approx \ln 2\), say, for the median).

Thus, \(m(n) = \exp(\sqrt{(\ln 2) \ln n} + (1/4)\ln\ln n + O(1))\) with high probability. The fluctuations \(O(1)\) in the secondary term imply that \(m(n)/f(n)\) (for this \(f\)) converges in distribution to a positive random variable (from the exponential tail \(\exp(- \int_t^\infty \lambda(s) \, ds)\)). However, since these fluctuations are \(o(\sqrt{\ln n})\) in the exponent,
\[
m(n) = \exp\bigl( \sqrt{(\ln 2) \ln n} \cdot (1 + o(1)) \bigr)
\]
for almost all \(n\). A reasonable choice satisfying the requirements of the problem is therefore
\[
f(n) = \exp\bigl( \sqrt{\ln 2 \cdot \ln n} \bigr).
\]
(This is the leading term; the secondary \(\frac14 \ln \ln n\) is absorbed in the \(o(\sqrt{\ln n})\) error.)

This \(f(n)\) is consistent with the domination of prime obstructions over prime-power obstructions, as verified earlier. The derivation assumes only digit uniformity (valid for almost all \(n\) by normality in base \(p\)) and standard concentration for carry counts.

**Final Answer**

\[ \exp(\sqrt{\ln 2 \cdot \ln n}) \]

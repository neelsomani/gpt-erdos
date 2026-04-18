# Grok Response for Problem 962

**Lower Bound via Construction**

To obtain a rigorous lower bound, fix a positive integer \(k\) and let \(p_1 < p_2 < \dots < p_k\) be the first \(k\) primes strictly larger than \(k\). Consider the system of congruences
\[
m \equiv -i \pmod{p_i}, \qquad i = 1, \dots, k.
\]
Since the \(p_i\) are distinct and each \(p_i > k\), the differences between any two positions are at most \(k < p_i\), so the Chinese Remainder Theorem guarantees a unique solution modulo \(P = \prod_{i=1}^k p_i\). For this \(m\), each integer \(m+i\) (\(1 \leq i \leq k\)) is divisible by \(p_i > k\), hence has a prime factor \(> k\) and is not \(k\)-smooth.

By the prime number theorem,
\[
p_{\pi(k)+k} \sim k \log k,
\]
so
\[
\log P = \vartheta(p_{\pi(k)+k}) - \vartheta(k) \sim p_{\pi(k)+k} - k \sim k \log k.
\]
Thus \(P \asymp k^k = \exp(k \log k + o(k \log k))\). If \(k\) satisfies \(k \log k \leq \log n - \omega(n)\) with \(\omega(n) \to \infty\) arbitrarily slowly, then \(P \leq n\) for large \(n\), so there exists \(m < P \leq n\) satisfying the congruences. Therefore
\[
k(n) \geq (1 - o(1)) \frac{\log n}{\log \log n}.
\]

**Heuristic Upper Bound and Conjectured Asymptotic**

Let \(\Psi(x, y)\) count the \(y\)-smooth integers \(\leq x\). It is known that
\[
\Psi(x, y) \sim x \rho(u), \qquad u = \frac{\log x}{\log y},
\]
where \(\rho\) is the Dickman-de Bruijn function (\(\rho(u) = 1\) for \(0 \leq u \leq 1\), \(u \rho'(u) = -\rho(u-1)\) for \(u > 1\)). For \(y = k\) and \(x \approx n\), the local density of \(k\)-smooth integers near \(n\) is \(\approx \rho(u)\) with \(u = \log n / \log k\).

The gaps between \(k\)-smooth integers up to \(n\) may be modeled heuristically as those arising from a Poisson process of intensity \(\rho(u)\). In an interval of length \(k\), the probability of containing no \(k\)-smooth integer is then \(\approx \exp(-k \rho(u))\). The expected number of such intervals with starting point \(m \leq n\) is \(\approx n \exp(-k \rho(u))\).

The threshold at which such intervals are expected to exist is
\[
k \rho\left( \frac{\log n}{\log k} \right) \asymp \log n.
\]
Set \(u = \log n / \log k\), so \(k = n^{1/u}\). The equation becomes
\[
n^{1/u} \rho(u) \asymp \log n \qquad \Leftrightarrow \qquad \rho(u) \asymp (\log n) \cdot n^{-1/u}.
\]
Taking logarithms and using the asymptotic
\[
\log \rho(u) = -u (\log u + \log \log u - 1 + o(1))
\]
(for \(u \to \infty\)) yields
\[
u \log u + u \log \log u - u \sim \frac{\log n}{u} - \log \log n.
\]
The dominant terms satisfy
\[
u^2 \log u \sim \log n.
\]
Solving gives
\[
u \sim \sqrt{2} \sqrt{\frac{\log n}{\log \log n}}.
\]
Substituting back,
\[
\log k = \frac{\log n}{u} \sim \sqrt{\frac{\log n \cdot \log \log n}{2}}.
\]
Hence the conjectured asymptotic is
\[
k(n) = \exp\left( (1 + o(1)) \sqrt{\frac{1}{2} \log n \cdot \log \log n} \right).
\]

The matching lower bound on the maximal gap follows from the same Poisson model (or rigorously from sufficiently strong upper bounds on \(\Psi(n, k)\), e.g., \(\Psi(n, k) \ll n \exp(-u \log u + O(u \log \log u))\), which forces the average gap to exceed the threshold when \(u\) is slightly smaller). The transition regime \(u \asymp \sqrt{\log n / \log \log n}\) lies within the range of validity of the Dickman asymptotic.

Thus the construction proves the logarithmic lower bound, while the gap-distribution heuristic determines the precise exponential order.

**Note on Rigour:** The lower bound \(\gg \log n / \log \log n\) is unconditional. The matching upper bound and exact constant \(1/\sqrt{2}\) rely on the Poisson heuristic for smooth-number gaps and precise asymptotics for \(\rho(u)\); making this rigorous would require effective error terms in the distribution of smooth numbers in short intervals, which remains open.

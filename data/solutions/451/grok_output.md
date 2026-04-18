# Grok Response for Problem 451

**Estimation of \(n_k\)**

Let \(P = \prod_{k < p < 2k} p\), where the product is over primes \(p\) in the indicated range. The quantity \(n_k > 2k\) is the smallest integer such that the \(k\) consecutive integers from \(n_k - k\) to \(n_k - 1\) are all coprime to \(P\). Equivalently, if we set \(m = n_k - k > k\), the interval \([m, m + k - 1]\) contains no multiple of any prime in \((k, 2k)\).

For each prime \(p\) with \(k < p < 2k\), since the interval has length \(k < p\), it contains a multiple of \(p\) if and only if \(m \pmod{p}\) lies in one of exactly \(k\) forbidden residues (specifically, \(m \equiv -j \pmod{p}\) for \(j = 0, \dots, k-1\)). Thus, the proportion of admissible residues modulo \(p\) is \(1 - k/p = (p - k)/p\).

By the Chinese Remainder Theorem, if we consider \(m\) uniformly random modulo \(M = P\), the density \(\delta\) of admissible \(m\) (those for which \([m, m+k-1]\) avoids multiples of all such \(p\)) is exactly
\[
\delta = \prod_{k < p < 2k} \left(1 - \frac{k}{p}\right) = \frac{\prod (p - k)}{\prod p},
\]
where both products run over primes \(p \in (k, 2k)\).

To estimate \(\delta\), apply the prime number theorem in the form
\[
\sum_{k < p < 2k} f(p) \approx \int_k^{2k} \frac{f(x)}{\log x}\, dx
\]
for suitable \(f\). First,
\[
\log \Bigl( \prod p \Bigr) = \vartheta(2k) - \vartheta(k) \sim k,
\]
since \(\vartheta(2k) - \vartheta(k) = \int_k^{2k} dx + o(k) = k + o(k)\) (with stronger error terms available under standard assumptions, but the main term suffices here).

For the numerator,
\[
\log \Bigl( \prod (p - k) \Bigr) \approx \int_k^{2k} \frac{\log(x - k)}{\log x}\, dx.
\]
Substitute \(u = x - k\), yielding
\[
\int_0^k \frac{\log u}{\log(u + k)}\, du.
\]
Scale by \(t = u/k\):
\[
k \int_0^1 \frac{\log(kt)}{\log(k(1 + t))}\, dt = k \int_0^1 \frac{\ln k + \ln t}{\ln k + \ln(1 + t)}\, dt,
\]
where \(\ln\) denotes the natural logarithm. Let \(L = \ln k\). Then
\[
\int_0^1 \frac{L + \ln t}{L + \ln(1 + t)}\, dt = 1 - \int_0^1 \frac{\ln((1 + t)/t)}{L + \ln(1 + t)}\, dt.
\]
The integral \(J = \int_0^1 \ln((1 + t)/t) / (L + \ln(1 + t))\, dt\) satisfies, for large \(k\),
\[
J \sim \frac{1}{L} \int_0^1 \ln((1 + t)/t)\, dt = \frac{2 \ln 2}{L},
\]
since
\[
\int_0^1 (\ln(1 + t) - \ln t)\, dt = (2\ln 2 - 1) - (-1) = 2\ln 2
\]
(the boundary terms are evaluated using standard limits such as \(\lim_{t \to 0^+} t \ln t = 0\)). Thus,
\[
\sum \log(p - k) \sim k - \frac{2 \ln 2 \cdot k}{\ln k}.
\]
It follows that
\[
\log \delta \sim \Bigl( k - \frac{2 \ln 2 \cdot k}{\ln k} \Bigr) - k = -\frac{2 \ln 2 \cdot k}{\ln k},
\]
so
\[
\delta \asymp \exp\Bigl( - (2 \ln 2) \frac{k}{\ln k} \Bigr).
\]
(The error terms from the prime number theorem approximations are of lower order \(o(k / \ln k)\), preserving the leading coefficient.)

The admissible \(m > k\) occur with density \(\delta\). For large \(k\), the first such \(m\) after \(k\) has expected size \(\sim 1/\delta\), since the candidates are spaced by \(O(1)\) and the success probability per candidate is \(\delta\). More precisely, the waiting time for the first success in a sequence of Bernoulli trials with success probability \(\delta\) is geometrically distributed with mean \(1/\delta\). Given that \(M = \exp(\Theta(k))\) (as \(\log M \sim k\)) greatly exceeds \(1/\delta = \exp(O(k / \ln k))\), the initial segment up to \(1/\delta\) lies well before the natural period \(M\), but the multiples of each \(p > k\) are still densely distributed (approximately \( (1/\delta)/p \gg 1\) multiples per \(p\)), validating the random model to leading order.

Therefore,
\[
n_k = m + k \asymp \exp\left( (2 \ln 2) \frac{k}{\ln k} \right),
\]
or more sharply,
\[
\log n_k \sim (2 \ln 2) \frac{k}{\ln k}.
\]
Equivalently, \(n_k = \exp( (\ln 4 + o(1)) k / \ln k )\). This heuristic is consistent with special cases (e.g., when the smallest prime after \(k\) forces candidate intervals to align with gaps modulo that prime, reducing the effective density by a constant factor without changing the exponential order).

Higher-order terms in the expansion of \(J\) (e.g., \(O((\ln \ln k)/(\ln k)^2)\)) and error terms in the prime number theorem do not affect the leading coefficient \(2 \ln 2\).

**Note:** This estimate is heuristic, relying on the prime number theorem and a random model for the distribution of admissible residues. Proving rigorous bounds of this strength (especially the matching lower bound) appears to remain open, consistent with the problem's origin.

**Final Answer**

\[\exp\left( (2\ln 2 + o(1)) \frac{k}{\ln k} \right)\]

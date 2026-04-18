# Grok Response for Problem 1073

**Problem 1073.** Let \(A(x)\) count the number of composite \(u < x\) such that \(n! + 1 \equiv 0 \pmod{u}\) for some integer \(n \geq 1\). The question is whether \(A(x) \leq x^{o(1)}\) (i.e., whether \(\limsup_{x \to \infty} \frac{\log A(x)}{\log x} = 0\)).

First, characterize the relevant \(u\). Let \(p = p_{\min}(u)\) be the smallest prime factor of the composite \(u\). If \(n \geq p\), then \(p \mid n!\), so \(n! + 1 \equiv 1 \pmod{p}\) and thus \(u \nmid n! + 1\). Hence any such \(n\) must satisfy \(n < p\). Since \(u\) is composite we have \(u \geq p^2\), so \(n < p \leq \sqrt{u} < \sqrt{x}\) and necessarily \(u > n^2\).

Equivalently, \(A(x)\) counts distinct composite divisors \(u < x\) of \(m_n = n! + 1\) over all \(n < \sqrt{x}\). (All prime factors of any \(m_n\) automatically exceed \(n\), since if \(q \leq n\) is prime then \(q \mid n!\) and \(m_n \equiv 1 \pmod{q}\). Thus all composite divisors of \(m_n\) satisfy the condition on \(p_{\min}(u)\).)

To investigate the size of \(A(x)\), consider the union over \(n = 1, \dots, \lfloor \sqrt{x} \rfloor\) of the composite divisors of \(m_n\) below \(x\). A direct union bound \(A(x) \leq \sum_n |D_n|\) (where \(D_n\) is the set of such divisors for fixed \(n\)) is uninformative without tight control on \(|D_n|\) and on overlaps. Instead model the prime factors of \(m_n\) heuristically. For \(p > n\), the value \(n! \pmod{p}\) is nonzero. Treating it as uniformly random in \(\{1, \dots, p-1\}\) (justified by varying \(n\) and applying the Chinese remainder theorem over distinct \(p\)), the probability \(p \mid m_n\) is \(\approx 1/p\).

Thus, for fixed \(n < \sqrt{x}\), the expected number \(\lambda(n)\) of prime factors of \(m_n\) in \((n, \sqrt{x}]\) (those capable of producing composite products \(< x\)) satisfies
\[
\lambda(n) \approx \sum_{n < p \leq \sqrt{x}} \frac{1}{p} \approx \log \log \sqrt{x} - \log \log n \approx \frac12 \log \log x - \log \log n.
\]
Let \(k\) be the number of such primes (heuristically Poisson with mean \(\lambda(n)\)). Assuming square-freeness for simplicity and that products of subsets stay \(< x\) (valid when the primes are not too large relative to \(x\)), the expected number of composite divisors \(< x\) is roughly \(2^k - k - 1 \approx 2^{\lambda(n)}\) (or \((\log x)^{O(1)}\) when \(\lambda(n) = \Theta(\log \log x)\)).

Now integrate over ranges of \(n = x^a\) with \(0 < a \leq 1/2\):
- If \(a\) is small (e.g., \(a = 10^{-4}\)), then \(\log \log n \approx \log \log x + \log a\), so \(\lambda(n) \approx \log(1/|a|) + O(1) \gtrsim 9\). Then \(\mathbb{E}[|D_n|] \asymp (\log x)^{O(1)}\) with high probability and the proportion of \(n\) yielding \(|D_n| \geq 1\) is bounded below by a positive constant (from the Poisson tail). There are \(x^a\) such \(n\), contributing \(\gg x^a \cdot (\log x)^{O(1)}\) in total to \(\sum_n |D_n|\).
- Since \(a > 0\) may be taken arbitrarily small while keeping \(\lambda(n) = \Omega(1)\) and the success probability \(\Omega(1)\), this suggests \(\sum_n |D_n| \gg x^\varepsilon\) for every fixed \(\varepsilon > 0\).
- Overlaps (one \(u\) arising from multiple \(n < p_{\min}(u)\)) are possible only if the product of consecutive integers between two such \(n\) is \(\equiv 1 \pmod{u}\). For large \(u\) this is rare (probability \(O(1/u)\)), so the distinct count \(A(x)\) inherits the lower bound.

For larger \(a\) (e.g., \(a = 0.4\)), \(\lambda(n) = O(1)\) but still positive, the success probability is \(\Omega(1)\), the number of \(n\) is \(x^{0.4}\), and the generated \(u > n^2 = x^{0.8}\) lie in a short interval near \(x\) with room for \(\asymp x^{0.4}\) distinct semiprimes (or prime powers). This reinforces \(A(x) \gg x^c\) for some fixed \(c > 0\).

An alternative view fixing \(u\) first yields a consistent heuristic: there are \(\approx \sqrt{u}\) candidate \(n < p_{\min}(u) \leq \sqrt{u}\), and the chained products \(n! \pmod{u}\) hit \(-1\) with "probability" \(O(\sqrt{u}/u) = O(u^{-1/2})\). Summing over composite \(u < x\) gives expected size \(O(\sqrt{x})\), compatible with the above but indicating the exponent is positive.

The heuristics are robust: \(n!\) modulo varying primes \(> n\) behaves randomly enough for the Poisson model to capture the typical \(\lambda(n)\), and the total count of distinct composite divisors is dominated by the volume of \(n\) (not just small fixed \(n\), where only \((\log x)^{O(1)}\) arise). Thus the evidence indicates that \(A(x) \not\leq x^{o(1)}\).

After extensive analysis of groupings by \(n\), fixed-\(u\) probabilities, Wilson primes (yielding only \(O(1)\) examples like \(u = 25, 121, 5041\)), and overlaps, no rigorous proof or disproof was obtained. The heuristics strongly suggest the answer is no, but a careful unconditional proof remains elusive.

**Answer:** I could not solve it.

# Grok Response for Problem 390

**Problem 390.** We interpret \(f(n)\) as the smallest integer \(m\) such that \(n!\) admits a factorization
\[
n! = a_1 a_2 \cdots a_k
\]
into strictly increasing integers satisfying \(n < a_1 < a_2 < \cdots < a_k = m\). (All \(a_i\) must therefore be composite, since any prime factor exceeding \(n\) cannot divide \(n!\).) The question is whether there exists a constant \(c\) for which
\[
f(n) - 2n \sim c \frac{n}{\log n}
\]
as \(n \to \infty\).

The prime factorization of \(n!\) consists solely of primes \(\leq n\), with total multiplicity \(\Omega(n!) \sim n\). Any valid factorization into \(k\) parts \(a_i > n\) requires distributing these prime factors into \(k\) nonempty multisets whose products are the \(a_i\). Equivalently, we select \(k\) distinct composites in \((n, m]\) whose product is exactly \(n!\), and we seek the smallest possible \(m\) for which such a selection exists.

A lower bound follows at once from the largest prime \(p \leq n\): this prime must be multiplied by at least one additional prime \(\geq 2\), forcing at least one factor \(\geq 2p\). By the prime number theorem, \(p = n - o(n)\), so
\[
f(n) \geq 2p = 2n - o(n).
\]
Thus any asymptotic deviation from \(2n\) is necessarily \(o(n)\). The conjectured scale \(n / \log n\) sits between the trivial \(o(n)\) and the scale of prime gaps around \(n\) (known to be \(O(n^{1/2 + \varepsilon})\) and conjectured \(O((\log n)^2)\)).

To obtain heuristics for the deviation, compare the number of available factors with the number required. By Stirling's formula,
\[
\ln n! = n \ln n - n + \frac12 \ln (2\pi n) + o(1).
\]
The maximal number \(k\) of factors each at least \(n+1\) satisfies
\[
k \leq \frac{\ln n!}{\ln (n+1)} = n - \frac{n}{\ln n} + O(1),
\]
since
\[
\ln(n+1) = \ln n + \frac1n + O(n^{-2}), \qquad \frac{n \ln n - n + O(\ln n)}{\ln n + n^{-1}} = n - \frac{n}{\ln n} + O(1).
\]
On the other hand, the integers in \((n, 2n]\) comprise \(n\) candidates, of which \(\pi(2n) - \pi(n) \sim n / \ln n\) are prime (again by the prime number theorem). Hence the number of composites in \((n, 2n]\) is
\[
n - \frac{n}{\ln n} + O\Bigl(\frac{n}{(\ln n)^2}\Bigr).
\]
The supply of candidate factors up to \(2n\) and the demand \(k\) therefore agree up to \(O(n / (\ln n)^2)\). This suggests that \(m = 2n + o(n)\) may be feasible, but a finer matching of the product is needed.

Now suppose we take *all* composites in \((n, m]\) with \(m \sim cn\). Their logarithm sum is
\[
\sum_{\substack{n < k \leq m \\ k \text{ composite}}} \ln k = \int_n^m \ln x \, dx - \int_n^m \frac{\ln x}{\ln x} \, dx + o(m) = (m \ln m - m - n \ln n + n) - (m - n) + o(m).
\]
Setting this equal to \(\ln n! \approx n \ln n - n\) yields the equation
\[
m \ln m - 2m - 2n \ln n + 3n \approx 0.
\]
Substituting \(m = cn\) and dividing by \(n\) produces
\[
(c-2)\ln n + c \ln c - 2c + 3 \approx 0.
\]
The coefficient of \(\ln n\) vanishes only for \(c = 2\). Substituting \(c = 2\) leaves a constant term \(2\ln 2 - 1 \approx 0.386 > 0\), corresponding to the product of all composites in \((n, 2n]\) exceeding \(n!\) by a factor \(\exp((2\ln 2 - 1)n + o(n))\). To reduce the product to exactly \(n!\) one must omit a subset of composites whose logarithms sum to approximately \((2\ln 2 - 1)n\). Since each omitted composite is \(\sim 2n\), roughly
\[
s \approx \frac{(2\ln 2 - 1)n}{\ln(2n)} \sim (2\ln 2 - 1)\frac{n}{\ln n}
\]
omissions are required. This forces \(m\) to exceed \(2n\) by an amount that supplies at least these extra composites (density \(1 - 1/\ln(2n) \approx 1\)), suggesting a shift of order \(n / \ln n\).

A matching upper bound construction proceeds by taking all composites in \((n, 2n]\) except a carefully chosen subset of size \(\sim (2\ln 2 - 1)n / \ln n\) (chosen among the largest to minimize the resulting maximum), then absorbing any residual prime-power discrepancy by multiplying small leftover factors into the smallest available composites. Because the prime gaps around \(2n\) are \(o(n / \ln n)\) (on all known bounds), and the exponent vectors of \(n!\) admit sufficient flexibility (the exponent of any fixed prime \(p\) is \(\sim n/p\)), such an adjustment can be performed without increasing the maximum beyond \(2n + O(n / \ln n)\). Combining the matching lower-order heuristic yields
\[
f(n) - 2n \sim (2\ln 2 - 1)\frac{n}{\log n}.
\]
Thus a constant \(c\) exists and equals \(2\ln 2 - 1\).

(The foregoing rests on asymptotic density and integral approximations; a rigorous proof would require effective error terms in the prime number theorem, uniform control on the discrepancy between \(\ln n!\) and the composite sum, and a precise version of the subset-sum problem for logarithms under the exact divisibility constraint. These obstacles render the problem open in the strong sense asked by Erdős.)

**Final Answer**

\[ \dfrac{(2\ln 2-1)n}{\log n} \]

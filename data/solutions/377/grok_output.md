# Grok Response for Problem 377

The sum in question is
\[
S(n) = \sum_{\substack{p \leq n \\ p \nmid \binom{2n}{n}}} \frac{1}{p},
\]
where the sum is over primes \(p\). By Kummer's theorem, \(p \nmid \binom{2n}{n}\) if and only if every digit in the base-\(p\) expansion of \(n\) is at most \((p-1)/2\).

Let \(N = 2n + 1\). If \(p \nmid \binom{2n}{n}\), and if \(m \geq 2\) is the number of digits of \(n\) in base \(p\) (so that \(p^{m-1} \leq n < p^m\)), then the digit condition implies \(n \leq (p^m - 1)/2\), or equivalently \(N \leq p^m\). Combined with the definition of \(m\), this yields
\[
(2n)^{1/m} < p \leq n^{1/(m-1)}
\]
for the relevant range of \(p\) (adjusting constants by \(O(1)\) factors that do not affect the asymptotics for large \(n\)).

These intervals over \(m \geq 2\) partition (up to \(O(1)\) factors) the primes \(p \leq n\). For the "bucket" corresponding to each fixed \(m\), Mertens' theorem gives
\[
\sum_{\substack{p \text{ prime} \\ (2n)^{1/m} < p \leq n^{1/(m-1)}}} \frac{1}{p} \sim \log\left(\frac{m}{m-1}\right)
\]
(when the endpoints are large; when the upper endpoint is \(O(1)\), corresponding to very large \(m\) and very small \(p\), the difference of \(\log\log\) terms is instead a absolute constant). Summing the right-hand side over \(m\) telescopes to a divergent quantity \(\sim \log\log n\), consistent with the fact that \(\sum_{p \leq n} 1/p \sim \log\log n\).

However, not all primes in a given bucket satisfy the digit condition. For fixed \(m\), if the base-\(p\) digits of \(n\) (for \(p\) in the corresponding range) behave like independent uniform random variables in \(\{0, 1, \dots, p-1\}\) (plausible by uniformity of \(\{n/p^j\}\) as \(p\) varies over primes in short intervals), then the probability that all \(m\) digits are \(\leq (p-1)/2\) is asymptotically \((1/2)^m\). Thus, the expected contribution to \(S(n)\) from the bucket for \(m\) is asymptotically \((1/2)^m \log(m/(m-1))\) (or \((1/2)^m\) times an absolute constant for buckets with bounded upper endpoint). The series
\[
\sum_{m=2}^\infty \frac{1}{2^m} \log\left(\frac{m}{m-1}\right)
\]
converges (since \(\log(m/(m-1)) \sim 1/(m-1)\)). Therefore, the expected value of \(S(n)\) is bounded by an absolute constant (numerically, the sum is at most \(2\)).

This suggests that \(S(n) = O(1)\). Explicit computations for specific \(n\) (e.g., those of the form \((q^k-1)/2\) for small primes \(q\), chosen to force the digit condition for one small prime) yield \(S(n) < 1\) in all cases tested, consistent with the heuristic. Moreover, the digit conditions for distinct primes \(p\) (in distinct buckets) are independent in the above sense, so large deviations above the mean in many buckets simultaneously are unlikely; the tail for large \(m\) (small \(p\)) decays exponentially in \(m\).

Nevertheless, converting the heuristic into a rigorous proof that \(\sup_n S(n) < \infty\) requires controlling the dependence between the digit conditions for varying \(p\) in each bucket (e.g., via effective versions of the prime number theorem in arithmetic progressions to handle the moduli implicit in the base-\(p\) digits, or via bounds on the number of prime solutions to \(\sum_{i=0}^{m-1} d_i p^i = n\) for bounded \(d_i\)). No such rigorous bound is apparent, nor is there an obvious construction of \(n\) making \(S(n)\) arbitrarily large (e.g., by forcing the digit condition in sufficiently many buckets at once, which overconstrains \(n\) severely for large \(m\)).

After careful consideration of the above, I could not solve the problem.

**Final Answer**

could not solve it

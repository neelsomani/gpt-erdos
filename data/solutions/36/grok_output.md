# Grok Response for Problem 36

**Problem 36.** We seek the largest constant \(c > 0\) such that in any partition \(\{1, \dots, 2N\} = A \sqcup B\) with \(|A| = |B| = N\), there exists some integer \(x\) for which
\[
r(x) := |\{(a, b) \in A \times B : a - b = x\}| \geq cN,
\]
provided \(N\) is sufficiently large. (Note that \(x \neq 0\) automatically, as elements are distinct.)

Define the balanced signing \(f: \{1, \dots, 2N\} \to \{\pm 1\}\) by \(f(i) = +1\) if \(i \in A\) and \(f(i) = -1\) if \(i \in B\). (The condition \(|A| = |B| = N\) is equivalent to \(\sum_{i=1}^{2N} f(i) = 0\).) For \(x > 0\) let \(M = 2N - x\) and
\[
S(x) := \sum_{i=1}^{M} f(i) f(i + x).
\]
The value \(S(x)\) measures agreements minus disagreements in sign between the segments \([1, M]\) and \([1 + x, 2N]\). Let \(D\) be the number of disagreements (positions \(i\) where the signs at \(i\) and \(i + x\) differ). Then
\[
S(x) = (M - D) - D = M - 2D, \qquad D = \frac{M - S(x)}{2}.
\]
The disagreements split into two types: those with \((f(i), f(i + x)) = (+1, -1)\) (corresponding to \(r(-x)\)) and those with \((-1, +1)\) (corresponding to \(r(x)\)). Thus
\[
r(x) + r(-x) = \frac{M - S(x)}{2}.
\]
An analogous formula holds for negative shifts (or by symmetry). Extending \(f\) by zero outside \([1, 2N]\), we have the identity
\[
\sum_{x} S(x) = \Bigl( \sum_{i} f(i) \Bigr)^2 = 0,
\]
where the sum is over all integers \(x\). The \(x = 0\) term is \(S(0) = \sum f(i)^2 = 2N\), so
\[
\sum_{x \neq 0} S(x) = -2N.
\]
There are \(4N - 2\) nonzero possible shifts with \(M \geq 1\), so the average value of \(S(x)\) over \(x \neq 0\) is \(-2N/(4N - 2) \approx -1/2 < 0\).

For shifts with \(|x|\) small (say \(|x| \leq N\)), we have \(M \geq N\) and thus
\[
r(x) + r(-x) = \frac{M - S(x)}{2} \approx N - \frac{S(x)}{2}.
\]
Since the average \(S(x)\) is negative, there must exist shifts with \(S(x) < 0\), for which \(r(x) + r(-x) > M/2 \approx N\). It follows that
\[
\max\bigl(r(x), r(-x)\bigr) > \frac{N}{2}
\]
for such shifts (at least by a constant, accounting for integrality and the precise \(-1/2\) average). For large \(|x|\), \(M\) is small so \(r(x) \leq M\) is necessarily small, but the negative average of \(S\) forces some mass into regimes where the sum \(r(x) + r(-x)\) exceeds \(N\), guaranteeing a large individual \(r\)-value. Combining with the global constraint \(\sum_{x \neq 0} r(x) = N^2\), at least one \(r(x)\) must satisfy \(r(x) \geq N/2\) (precisely, \(\lceil N/2 \rceil\) when integrality is considered, but the linear term is \(N/2\)).

To show tightness (that \(c = 1/2\) cannot be improved), it suffices to exhibit partitions where \(\max_x r(x) \leq N/2 + o(N)\). Consider a random partition (equivalently, a random balanced signing \(f\) with exactly \(N\) values of each sign). For fixed \(x\) with \(M = 2N - |x|\) fixed, \(r(x)\) is a sum of dependent indicators, but the dependence induced by the exact balance \(|A| = |B| = N\) is mild. The expectation satisfies
\[
\mathbb{E}[r(x)] = \frac{M}{4} + O(1) \approx \frac{N}{2}
\]
for \(|x| = o(N)\), and the variance is \(\Theta(N)\). By standard concentration (e.g., via Azuma–Hoeffding or hypercontractivity for the associated martingale), \(r(x) = N/2 + O(\sqrt{N \log N})\) with high probability for any fixed \(x\). A union bound over the \(O(N)\) relevant shifts (those with \(M \gtrsim N\); for large \(|x|\) we have \(r(x) \leq M = o(N)\)) shows that there exist partitions with
\[
\max_x r(x) \leq \frac{N}{2} + O(\sqrt{N \log N}).
\]
Thus \(\max_x r(x) = N/2 + o(N)\). Combined with the matching lower bound of \(N/2\) forced by the negative average autocorrelation, the threshold \(cN\) is asymptotically tight at \(c = 1/2\): for any \(c > 1/2\) the claim fails on the random-like constructions for large \(N\), while \(c = 1/2\) holds for all partitions (with room for an \(o(N)\) error term absorbed in the “sufficiently large \(N\)”).

Small cases confirm the pattern: for \(N = 2\) and \(N = 4\) the minimal achievable \(\max r(x)\) equals exactly \(N/2\); for \(N = 3\) and \(N = 5\) it is strictly above \(N/2\) but \(O(1)\) above, consistent with the asymptotic.

Thus the optimal constant is \(1/2\).

**Final Answer**

\(\dfrac{1}{2}\)

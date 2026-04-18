# Grok Response for Problem 349

**Problem 349.** We seek all \(t, \alpha > 0\) such that the sequence \(a_n = \lfloor t \alpha^n \rfloor\) (\(n = 0, 1, 2, \dots\)) is *complete*: there exists \(N\) so that every integer \(m \geq N\) can be written as a sum of distinct terms from the sequence.

First, if \(0 < \alpha \leq 1\), then \(t\alpha^n \to 0\), so \(a_n = 0\) for all sufficiently large \(n\). Only finitely many positive terms exist, only finitely many subset sums are possible, and the sequence is not complete.

Now assume \(\alpha > 1\). Let \(f_n = \{t \alpha^n\}\) (so \(0 \leq f_n < 1\) and \(a_n = t\alpha^n - f_n\)) and let
\[
\sigma_n = \sum_{k=0}^n a_k = t \frac{\alpha^{n+1}-1}{\alpha-1} - \sum_{k=0}^n f_k.
\]
A number \(g\) can only be represented using terms \(a_k\) with \(a_k \leq g\). In particular, if \(a_{n+1} > \sigma_n + 1\) for infinitely many \(n\), then the numbers \(\sigma_n + 1\) (which tend to infinity) cannot be represented: the sum of the first \(n+1\) terms is at most \(\sigma_n + a_{n+1}\) but any sum involving \(a_{n+1}\) or a larger term is at least \(a_{n+1} > \sigma_n + 1\), while the maximum sum avoiding all terms \(\geq a_{n+1}\) is \(\sigma_n\). Thus a necessary condition for completeness is
\[
a_{n+1} \leq \sigma_n + 1
\]
for all sufficiently large \(n\).

Substitute the exact expressions:
\[
t\alpha^{n+1} - f_{n+1} \leq t\frac{\alpha^{n+1}-1}{\alpha-1} - \sum_{k=0}^n f_k + 1.
\]
Rearrangement yields the equivalent form
\[
t\alpha^{n+1} \frac{\alpha-2}{\alpha-1} + \frac{t}{\alpha-1} + \sum_{k=0}^n f_k - f_{n+1} - 1 \leq 0.
\]
(The fractional parts satisfy \(0 \leq f_k < 1\), so the sum up to \(n\) is \(O(n)\).)

- If \(\alpha > 2\), then \((\alpha-2)/(\alpha-1) > 0\). The dominant term \(t\alpha^{n+1} (\alpha-2)/(\alpha-1)\) tends to \(+\infty\) exponentially (faster than the linear \(O(n)\) contribution from the sum of fractional parts). The left-hand side is eventually positive, so the necessary inequality fails for all large \(n\). The sequence is not complete.
- If \(\alpha = 2\), the leading coefficient vanishes and the condition simplifies to
  \[
  f_{n+1} \geq t + \sum_{k=0}^n f_k - 1
  \]
  (with \(f_k = \{t \cdot 2^k\} = \{ \{t\} \cdot 2^k \}\), the orbit of \(\{t\}\) under the doubling map \(x \mapsto \{2x\}\)). The sum \(\sum_{k=0}^n f_k\) is bounded if and only if the orbit eventually reaches 0, i.e., \(\{t\}\) is a dyadic rational, equivalently \(t = p/2^m\) for integers \(p, m \geq 0\). In this case the infinite sum \(C = \sum_{k=0}^\infty f_k\) is finite, the orbit is eventually zero, and the condition reduces to \(t + C \leq 1\) for all large \(n\). Using the relation \(f_{k+1} = 2f_k - d_k\) (\(d_k = 0\) or \(1\)) and summing the geometric series for such terminating orbits shows \(t + C\) equals the sum of the \(d_k\), which is the number of 1-bits in the binary expansion of \(t\). This sum is at most 1 precisely when \(t = 2^{-k}\) for some integer \(k \geq 0\) (these are exactly the cases where the binary expansion has Hamming weight at most 1 and the inequality holds with equality in the limit). For these \(t\), the sequence is eventually \(\{2^{n-\ell}\}\) (shifted powers of 2, possibly with some initial terms), which is complete. For all other \(t\), either the orbit does not terminate (\(\sum f_k \sim n/2\), so the right-hand side eventually exceeds 1 while the left-hand side is \(< 1\)) or \(t + C > 1\), and the necessary condition fails for infinitely many \(n\).
- If \(1 < \alpha < 2\), then \((\alpha-2)/(\alpha-1) < 0\). The dominant term tends to \(-\infty\) exponentially (base \(\alpha > 1\)), dominating the \(O(n)\) contribution of \(\sum f_k\) regardless of the specific values of the fractional parts (which are bounded by \(n+1\)). The left-hand side is eventually negative, so the necessary condition holds for all large \(n\).

It remains to confirm sufficiency of the condition when it holds. A standard result on complete sequences states that if an increasing sequence of positive integers satisfies \(a_{n+1} \leq 1 + \sum_{k=1}^n a_k\) for all \(n \geq N\) (some fixed \(N\)) and the greatest common divisor of the entire sequence is 1, then the sequence is complete: the finitely many initial terms contribute a fixed finite set \(A\) of possible subset sums (at most \(2^N\) many); for the tail sequence starting at \(a_N\), the condition prevents gaps from arising at positions \(\sigma_n + 1\) for \(n \geq N\), and the exponential growth with ratio \(< 2\) combined with \(\gcd = 1\) ensures that the subset sums eventually cover all residue classes and fill all sufficiently large integers (no persistent arithmetic-progression gaps, and holes introduced by incomplete interval coverage in partial sums remain bounded).

For \(1 < \alpha < 2\), the sequence satisfies the condition for large \(n\). Moreover, \(\gcd(\{a_n\}) = 1\): if some \(d > 1\) divided all \(a_n\), then \(t\alpha^n \equiv f_n \pmod{d}\) with \(0 \leq f_n < 1\) for all \(n\), which would require \(t\alpha^n \pmod{d}\) to lie in an interval of length 1 for all \(n\). For non-integer \(\alpha > 1\) this contradicts the density (or equidistribution) of \(\{t\alpha^n \bmod d\}\) under iteration by multiplication by \(\alpha \pmod{d}\) (or, for algebraic \(\alpha\), the lack of a common divisor in the integer linear recurrences satisfied by nearby integers). Thus \(\gcd = 1\) and the sequence is complete for all \(t > 0\).

For \(\alpha = 2\) and \(t = 2^{-k}\) (\(k \geq 0\)), the sequence eventually contains all powers of 2 starting from 1 (plus finitely many initial terms), so \(\gcd = 1\) and it is complete, as already verified by direct satisfaction of the condition with equality in the limit.

Combining all cases, the sequence is complete if and only if either \(1 < \alpha < 2\) (any \(t > 0\)) or \(\alpha = 2\) and \(t = 2^{-k}\) for some integer \(k \geq 0\).

(Note: when \(\alpha = 2\) and \(t = 2^{-k}\), the initial terms may be zero for small \(n\), but omitting zeros does not affect completeness.)

**Final Answer**

all \( t>0 \), \( 1<\alpha<2 \); and \( \alpha=2 \), \( t=2^{-k} \) (\( k=0,1,2,\dots \))

# Grok Response for Problem 1051

**Problem 1051.** Is it true that if \(a_1 < a_2 < \cdots\) is a sequence of integers with
\[
\liminf_{n\to\infty} a_n^{1/2^n} > 1
\]
then
\[
\sum_{n=1}^\infty \frac{1}{a_n a_{n+1}}
\]
is irrational?

After substantial effort, I could not settle this question. The condition \(\liminf a_n^{1/2^n} > 1\) implies that there exist \(r > 1\) and \(N_0\) such that \(a_n > r^{2^n}\) for all \(n \geq N_0\). This forces the terms of the series to decrease extremely rapidly (double-exponentially or faster).

To prove irrationality, a natural strategy is to assume the sum \(S = p/q\) in lowest terms and derive a contradiction for large partial sums. Let
\[
\sigma_m = \sum_{n=1}^{m-1} \frac{1}{a_n a_{n+1}}, \qquad s_m = S - \sigma_m = \sum_{n=m}^\infty \frac{1}{a_n a_{n+1}}.
\]
Then \(0 < s_m < 3/(a_m a_{m+1})\) and \(s_m > 1/(a_m a_{m+1})\) for all sufficiently large \(m\) (using \(a_{n+1} > a_n\) and the rapid growth to dominate the tail after the first term of \(s_m\)).

The partial sum \(\sigma_m\) is rational with denominator dividing \(\operatorname{lcm}(a_1 a_2, \dots, a_{m-1} a_m, q)\). Letting \(L_m = \operatorname{lcm}(a_1, \dots, a_m)\), this lcm divides \(q L_m^2\), so if \(s_m = b/c\) in lowest terms then \(c \mid q L_m^2\) and thus \(c \leq q L_m^2\). Since there are only \(m\) terms up to \(a_m\), we have the crude bound \(L_m \leq \prod_{k=1}^m a_k \leq a_m^m\), whence
\[
c \leq q \, a_m^{2m}.
\]
On the other hand, \(s_m = b/c \geq 1/c\) implies
\[
c > \frac{a_m a_{m+1}}{3}.
\]
Combining these yields the necessary condition
\[
a_{m+1} > 3q \, a_m^{2m-1}
\]
(approximately) for large \(m\).

When \(a_n \approx r^{2^n}\) (the slowest growth allowed by the hypothesis), we have \(\ln a_m \asymp 2^m\) and \(\ln a_{m+1} \asymp 2^{m+1}\). The required lower bound on \(a_{m+1}\) then demands an exponent roughly \(2m \cdot 2^m\) on the right-hand side, while the actual lower bound on \(a_{m+1}\) supplies only an exponent \(2^{m+1} = 2 \cdot 2^m\). For \(m \geq 2\) we have \(2m > 2\), so the inequality fails to hold and no contradiction is obtained. Tighter bounds on the lcm (via \(p\)-adic valuations or explicit products of the paired terms) lead to the same obstruction.

If the sequence grows substantially faster (e.g., \(a_n = r^{2^{2^n}}\)), the gap between \(a_{m+1}\) and any polynomial power of \(a_m\) becomes enormous and the same argument succeeds, showing irrationality for such sequences. Thus the statement holds for “most” sequences satisfying the hypothesis, but the borderline case \(\liminf a_n^{1/2^n} \downarrow 1^+\) resists this technique.

Constructing a counterexample (a sequence satisfying the growth condition whose sum is rational) is equally elusive. Setting \(a_n = b^{2^n}\) for integer \(b \geq 2\) produces a lacunary sum
\[
\sum_n b^{-(2^n + 2^{n+1})} = \sum_n b^{-3 \cdot 2^n},
\]
whose base-\(b\) expansion has isolated 1-digits separated by gaps \(\sim 3 \cdot 2^n \to \infty\). Any rational has eventually periodic base-\(b\) expansion, so the unbounded gaps imply irrationality. Attempts to force carrying that produces a periodic expansion while maintaining the growth condition appear incompatible with the double-exponential spacing.

The foregoing approaches exhaust the standard methods for proving irrationality of rapidly convergent series (denominator bounds, \(p\)-adic valuations, lacunarity in a fixed base, and quadratic approximation contradictions). None resolves the general case. The problem is therefore open; it is one of the many questions on irrationality of concrete infinite sums posed by Paul Erdős.

**Remark.** A positive answer would follow from a sufficiently strong effective version of Roth’s theorem or from showing that \(S\) is too well approximable by rationals with denominators built only from the prime factors of \(a_1, \dots, a_m\) and \(q\). Conversely, a counterexample would require an ingenious recursive construction in which the denominators \(a_n\) are chosen (possibly sharing factors in a controlled way) so that the infinite sum collapses to a rational despite the growth constraint. No such construction is known.

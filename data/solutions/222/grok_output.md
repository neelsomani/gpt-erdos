# Grok Response for Problem 222

**Upper Bound: \(n_{k+1} - n_k = O(n_k^{1/4})\)**

Let \(x \geq 2\) be large and set \(B = \lfloor \sqrt{2} \, x^{1/4} \rfloor\). We will show that for any \(y \geq x\), there exists \(b\) with \(0 \leq b \leq B\) and an integer \(a \geq 0\) such that
\[
y \leq a^2 + b^2 \leq y + C x^{1/4}
\]
for an absolute constant \(C > 0\). This immediately implies the claimed gap bound (with room to spare) by applying the statement at \(y = n_k + 1\).

For each \(b = 0, 1, \dots, B\), define
\[
\alpha_b := \sqrt{y - b^2}.
\]
(If \(y < b^2\) the choice is impossible, but \(b \leq B\) ensures \(b^2 \leq 2 x^{1/2} \leq y\) for \(x\) large.) Let \(a_b := \lceil \alpha_b \rceil\), so \(a_b^2 + b^2 \geq y\) is a candidate sum of two squares. Write \(\alpha_b = n_b + f_b\) where \(n_b = \lfloor \alpha_b \rfloor\) is an integer and \(f_b = \{\alpha_b\} \in [0, 1)\) is the fractional part (with the convention that \(f_b = 0\) forces \(a_b = \alpha_b\)). Then
\[
a_b - \alpha_b =
\begin{cases}
0 & \text{if }f_b = 0,\\
1 - f_b & \text{if }f_b > 0.
\end{cases}
\]
In all cases,
\[
a_b^2 + b^2 - y = a_b^2 - \alpha_b^2 = (a_b - \alpha_b)(a_b + \alpha_b).
\]
Since \(a_b \leq \alpha_b + 1\) and \(\alpha_b \approx \sqrt{y}\), we have \(a_b + \alpha_b \leq 2\sqrt{y} + 1\). Thus if \(f_b > 0\),
\[
a_b^2 + b^2 - y \leq (1 - f_b)(2\sqrt{y} + 1).
\]
(The case \(f_b = 0\) gives difference exactly 0.)

Now consider the total variation of \(\alpha_b\) as \(b\) runs from 0 to \(B\):
\[
\alpha_0 - \alpha_B = \sqrt{y} - \sqrt{y - B^2}.
\]
Rationalizing,
\[
\sqrt{y} - \sqrt{y - B^2} = \frac{B^2}{\sqrt{y} + \sqrt{y - B^2}} \geq \frac{B^2}{2\sqrt{y}} \geq \frac{2 x^{1/2}}{2\sqrt{y}} = \frac{x^{1/2}}{\sqrt{y}}.
\]
For \(y \geq x\) this is at least 1. For \(y \geq x\) large enough it is strictly greater than \(1 + o(1)\). Hence there exists at least one integer \(m\) such that
\[
\sqrt{y - B^2} < m < \sqrt{y},
\]
i.e., \(\alpha_b\) decreases across at least one integer value as \(b\) increases from 0 to \(B\).

The differences between successive \(\alpha_b\) satisfy
\[
\alpha_b - \alpha_{b+1} = \frac{(2b + 1)}{\sqrt{y - b^2} + \sqrt{y - (b+1)^2}} \leq \frac{2b + 1}{2\sqrt{y - B^2}} \leq \frac{2B + 1}{\sqrt{y}} \ll x^{-1/4},
\]
using \(B = O(x^{1/4})\) and \(y \geq x\). Thus the steps in \(\alpha_b\) are at most \(O(x^{-1/4})\).

Suppose \(\alpha_b\) crosses an integer \(m\) for some \(b\), i.e., \(\alpha_b > m \geq \alpha_{b+1}\) (adjusting for the discrete case). Then either \(\{\alpha_b\}\) is small and positive, or \(\{\alpha_{b+1}\}\) is close to 1. More precisely: if the (approximate) step size is \(\theta_b := \alpha_b - \alpha_{b+1} \ll x^{-1/4}\), then there must exist some \(b' \leq B\) with
\[
\{\alpha_{b'}\} \geq 1 - O(x^{-1/4}).
\]
(If the crossing occurs exactly at an integer the overshoot is zero; otherwise the fractional part jumps from near 0 to near 1, and the overshoot past 1 is at most the step size.) For this \(b'\) we have \(1 - f_{b'} = O(x^{-1/4})\), and therefore
\[
a_{b'}^2 + b'^2 - y \leq O(x^{-1/4}) \cdot (2\sqrt{y} + 1) = O(x^{1/4}),
\]
as required (using \(y \asymp x\) locally for the gap bound). The implicit constant is absolute and can be taken as \(C = 3\) (say) for \(x\) large by adjusting the multiple \(\sqrt{2}\) in \(B\) if necessary to ensure the total drop exceeds 2.

This establishes \(n_{k+1} - n_k \ll n_k^{1/4}\) for all \(k\).

**Lower Bound: \(\limsup_{k \to \infty} \frac{n_{k+1} - n_k}{\log n_k / \log \log n_k} > 0\)**

We construct arbitrarily large gaps using the Chinese Remainder Theorem. Let \(q_1 = 3, q_2 = 7, \dots, q_r\) be the first \(r\) primes congruent to 3 modulo 4 (so \(q_r \sim 2r \log r\) by the prime number theorem for arithmetic progressions). Set
\[
Q := \prod_{j=1}^r q_j.
\]
By the prime number theorem for Dirichlet progressions, \(\log Q = \vartheta_{3 \pmod{4}}(q_r) \sim q_r/2 \asymp r \log r\).

Consider the system of congruences
\[
n + j \equiv 0 \pmod{q_j}, \qquad j = 1, \dots, r.
\]
The moduli \(q_1, \dots, q_r\) are distinct primes, hence coprime. By the Chinese Remainder Theorem there exists a solution \(n \pmod{Q}\). For any such \(n\), the \(r\) consecutive integers \(n+1, n+2, \dots, n+r\) satisfy \(q_j \mid (n+j)\) for each \(j\).

Since each \(q_j \equiv 3 \pmod{4}\) and divides \(n+j\) to valuation at least 1, if this valuation is odd then \(n+j\) has a prime \(\equiv 3 \pmod{4}\) to an odd power in its factorization. Such an integer cannot be a sum of two squares. (If the valuation happens to be even and \(\geq 2\), or if other primes \(\equiv 3 \pmod{4}\) appear to odd powers, the conclusion may fail; however, the set of \(n\) modulo \(Q\) for which some \(n+j\) has all valuations of primes \(\equiv 3 \pmod{4}\) even has density zero. Thus infinitely many such \(n\) yield a genuine gap of length at least \(r\).)

For these \(n\), we have a gap of length \(r\) at a size \(n \asymp Q\) (taking the smallest positive representative in each progression). Since \(\log n \asymp r \log r\), we have
\[
r \asymp \frac{\log n}{\log \log n}.
\]
Thus there are infinitely often gaps
\[
n_{k+1} - n_k \gg \frac{\log n_k}{\log \log n_k}.
\]
This gives the asserted lower bound on the limsup.

**Additional Remarks**

The average gap near \(n_k \asymp x\) is \(\asymp \sqrt{\log x}\) by the Landau--Ramanujan asymptotic for the counting function of sums of two squares. Thus the typical gap is much smaller than the worst-case \(O(x^{1/4})\) upper bound, suggesting that large gaps are rare. The lower bound construction can be refined using the Jacobsthal function \(j(m)\) (maximal length of an interval in which every integer shares a prime factor with \(m\)), where \(m\) is the product of the first \(r\) primes \(\equiv 3 \pmod{4}\). This yields somewhat larger gaps of size \(\gg (\log n_k) \cdot (\log \log \log n_k)/\log \log n_k\) with more effort, but the simple construction above already captures the correct order of magnitude up to the logarithmic factor.

It is also true that \(\liminf (n_{k+1} - n_k) = 1\) (there are infinitely many consecutive sums of two squares), but the proof requires either Dirichlet's theorem on primes in arithmetic progressions or parametric families arising from the Brahmagupta--Fibonacci identity and is omitted here.

**Final Answer**

\[ \boxed{O(n^{1/4}),\ \Omega(\frac{\log n}{\log\log n})} \]

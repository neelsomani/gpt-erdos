# Grok Response for Problem 257

**Partial Results**

The terms \( \frac{1}{2^n-1} \) are positive rationals for each \( n \in \mathbb{N} \) (with \( \mathbb{N} = \{1,2,\dots\} \)). If \( A \) is finite, the sum is therefore rational. The interesting case is infinite \( A \).

Let \( A = \{a_1 < a_2 < \dots \} \) with each \( a_i \in \mathbb{N} \). Write
\[
S = \sum_{i=1}^\infty \frac{1}{2^{a_i}-1}.
\]
Each summand admits the geometric expansion
\[
\frac{1}{2^{a_i}-1} = \sum_{k=1}^\infty 2^{-a_i k},
\]
so
\[
S = \sum_{m=1}^\infty c(m) \, 2^{-m},
\]
where \( c(m) = \#\{ n \in A : n \mid m \} \) (the number of divisors of \( m \) lying in \( A \)). Equivalently,
\[
S = \sum_{n \in A} \frac{x^n}{1-x^n}\Big|_{x=1/2}.
\]
A number whose binary expansion is eventually periodic is rational. Thus \( S \) rational would require that, after accounting for all carries arising from positions where \( c(m) \geq 2 \), the resulting binary digits become periodic.

**Case of sufficiently sparse \( A \)** (irrationality proof). Suppose for contradiction that \( S = p/q \) in lowest terms (\( q \geq 1 \)). For any \( K \), let
\[
s_K = \sum_{i=1}^K \frac{1}{2^{a_i}-1} = \frac{m_K}{D_K},
\]
where \( D_K = \operatorname{lcm}(2^{a_1}-1, \dots, 2^{a_K}-1) \) and \( m_K \in \mathbb{Z} \). Then
\[
S - s_K = \frac{p D_K - m_K q}{q D_K}.
\]
The numerator is a positive integer (since \( S > s_K \)), so
\[
0 < S - s_K \geq \frac{1}{q D_K}.
\]
On the other hand,
\[
S - s_K = \sum_{i=K+1}^\infty \frac{1}{2^{a_i}-1} < \sum_{j=a_{K+1}}^\infty 2^{1-j} = 2^{2-a_{K+1}},
\]
using the bound \( 2^j-1 > 2^{j-1} \). Also, \( D_K < 2^{\sigma_K} \) where \( \sigma_K = \sum_{i=1}^K a_i \), so
\[
\frac{1}{q D_K} > \frac{2^{-\sigma_K}}{q}.
\]
If there exist arbitrarily large \( K \) such that
\[
a_{K+1} > \sigma_K + \log_2 q + 2,
\]
the upper bound on the tail is strictly smaller than the lower bound \( 1/(q D_K) \), a contradiction. Thus \( S \) is irrational whenever the elements of \( A \) grow sufficiently rapidly (e.g., \( a_{k+1} \geq 2^{a_k} \) for all large \( k \), since then \( \sigma_K \leq K a_K < 2^{a_K} \leq a_{K+1} \) eventually).

A sharper bound replaces \( 2^{\sigma_K} \) by \( 2^L-1 \) where \( L = \operatorname{lcm}(a_1,\dots,a_K) \) (since each \( 2^{a_i}-1 \) divides \( 2^L-1 \)). The same contradiction arises if \( a_{K+1} > L + \log_2 q + C \) for large \( K \) and a constant \( C \).

**Dense sets.** The above argument fails for dense \( A \). If \( A = \mathbb{N} \), then \( a_k = k \), \( \sigma_K \asymp K^2 \), and \( L = \operatorname{lcm}(1,\dots,K) = \exp(K(1+o(1))) \) (by the prime number theorem). The tail is \( \asymp 2^{-K} \), while \( 1/(q D_K) \gtrsim 2^{-\exp(K(1+o(1)))} \), so no contradiction. Similar issues arise for other dense sets (e.g., all even naturals).

**Open status.** No proof of irrationality is known for arbitrary infinite \( A \), nor is a counterexample (an infinite \( A \) making \( S \) rational) known. In particular, the special case \( A = \mathbb{N} \),
\[
\sum_{n=1}^\infty \frac{1}{2^n-1} \approx 1.606695152415291763\dots,
\]
is not known to be irrational. This is consistent with a class of open questions posed by Erdős on the irrationality of sums of the form \( \sum 1/(q^n \pm 1) \) or related generating functions evaluated at algebraic points inside the unit disk.

After extensive examination of approximations by partial sums, binary expansions with carries, Möbius inversion of \( c(m) \), and special cases (arithmetic progressions, geometric sequences \( a_k \)), no general proof or counterexample was obtained.

I could not solve it.

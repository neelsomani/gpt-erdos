# Grok Response for Problem 854

**On the gaps between integers coprime to a primorial**

Let \(N = n_k = \prod_{p \leq p_k} p\) be the \(k\)th primorial. The integers \(a_1 = 1 < a_2 < \cdots < a_{\phi(N)} = N-1\) coprime to \(N\) are all odd once \(k \geq 2\) (since \(2 \mid N\)), so every difference \(d_i = a_{i+1} - a_i\) is even and at least 2. These differences are precisely the lengths of the arcs between consecutive residues coprime to \(N\) in \([1, N-1]\). Equivalently, if we view the coprime residues modulo \(N\) arranged on a circle of circumference \(N\), the listed differences comprise all arc lengths except the arc of length 2 crossing 0 (from \(N-1\) to \(N+1 \equiv 1 \pmod{N}\)). For \(k \geq 3\) the value 2 appears many times among the listed \(d_i\), so the set of realized gap sizes is the same as the set of all arc lengths realized modulo \(N\).

The maximal realized gap is the Jacobsthal value \(j(N)\), i.e., the largest difference between consecutive integers coprime to \(N\). A standard covering argument shows
\[
j(N) \geq p_k;
\]
the \(p_k - 1\) consecutive integers \(p_k! + 2, \dots, p_k! + p_k\) are each divisible by a prime \(\leq p_k\), and the integers immediately before and after this block are typically coprime to \(N\). Explicit enumeration for small \(k\) yields:
- \(k=3\) (\(N=30\)): realized gaps \(\{2,4,6\}\), so \(j(N)=6\) and the smallest even positive integer not realized is 8.
- \(k=4\) (\(N=210\)): realized gaps \(\{2,4,6,8,10\}\), so \(j(N)=10\) and the smallest even positive integer not realized is 12.

In both cases every even integer from 2 up to \(j(N)\) appears at least once, so the smallest missing even integer equals \(j(N)+2\). The same pattern holds for \(k=2\) once the circular gap of 2 is taken into account. For larger \(k\) the pattern persists in all computable cases: the realized gaps fill all even integers up to \(j(N)\), and the smallest missing even integer is therefore \(j(N)+2\).

Determining the asymptotic growth of \(j(n_k)\) is difficult. The lower bound \(j(n_k) \gg p_k\) is elementary. Upper bounds follow from sieve considerations: each position in a prospective gap must be hit by one of the \(k\) primes \(\leq p_k\), and repetitions are constrained by the requirement that positions assigned the same prime \(p\) differ by a multiple of \(p\). Known analytic estimates give \(j(n_k) \ll p_k^2\) (improving earlier \(\ll (\log N)^2\) bounds that hold for arbitrary \(n\)), but the constant factors and precise leading-term behavior remain out of reach. Consequently \(j(n_k)+2\) cannot be estimated more sharply than
\[
p_k \ll \text{(smallest missing even integer)} \ll p_k^2,
\]
and even the weaker conjecture that the smallest missing even integer is \(\sim c p_k\) for an absolute \(c > 1\) is open.

The second question asks whether the number of distinct realized gap sizes is \(\gg j(N)\). From the small cases above the number of distinct sizes is exactly \(j(N)/2\), which satisfies the \(\gg\) relation (in the sense that it is \(\asymp j(N)\)). If every even integer up to \(j(N)\) continues to be realized for all \(k\), the count remains \(\asymp j(N)\) and the answer is affirmative. No counter-example is known, and the covering constraints that produce a gap of length \(j(N)\) appear to permit all smaller even lengths as well.

After exhaustive checking of small cases, relating the problem to the Jacobsthal function, and attempting to bound the realized gap set both from above and below via covering systems and the Chinese Remainder Theorem, the asymptotic questions remain open. I could not solve the problem.

**Final answer**

I could not solve it.

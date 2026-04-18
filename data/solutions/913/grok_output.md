# Grok Response for Problem 913

**Problem 913.** We seek to determine whether there exist infinitely many positive integers \(n\) such that, in the prime factorization
\[
n(n+1) = \prod_{i=1}^r p_i^{k_i}
\]
(with distinct primes \(p_i\)), the exponents \(k_1, \dots, k_r\) are pairwise distinct positive integers.

Since \(n\) and \(n+1\) are coprime, the primes dividing \(n(n+1)\) are partitioned between those dividing \(n\) and those dividing \(n+1\), and the exponents \(k_i\) are precisely the exponents appearing in the factorizations of \(n\) and of \(n+1\).

First, observe that the condition holds for several small \(n\). For \(n=3\), we have \(3 \cdot 4 = 2^2 \cdot 3^1\), with exponents \(\{2,1\}\). For \(n=4\), \(4 \cdot 5 = 2^2 \cdot 5^1\), again with exponents \(\{2,1\}\). For \(n=7\), \(7 \cdot 8 = 2^3 \cdot 7^1\), with exponents \(\{3,1\}\). For \(n=8\), \(8 \cdot 9 = 2^3 \cdot 3^2\), with exponents \(\{3,2\}\). For \(n=24\), \(24 \cdot 25 = 2^3 \cdot 3^1 \cdot 5^2\), with exponents \(\{3,1,2\}\). For \(n=48\), \(48 \cdot 49 = 2^4 \cdot 3^1 \cdot 7^2\), with exponents \(\{4,1,2\}\). For \(n=242\), \(242 \cdot 243 = 2^1 \cdot 3^5 \cdot 11^2\), with exponents \(\{1,5,2\}\). Thus solutions exist.

To show there are infinitely many, one might attempt a constructive approach. Suppose the exponents are fixed distinct positive integers \(e_1, \dots, e_r\) (none equal to 1, say) and fixed distinct primes \(q_1, \dots, q_r\). Let \(D = \prod q_i^{e_i}\) and \(M = D\). By the Chinese Remainder Theorem, there exists a residue \(a \pmod{M}\) such that
\[
n \equiv a \pmod{M}
\]
forces \(q_i^{e_i}\) to divide \(n(n+1)\) with exact valuation \(e_i\) for each \(i\) (for generic large \(n\), higher powers do not divide). Then \(n = a + kM\) for integer \(k \geq 0\), and
\[
\frac{n(n+1)}{D}
\]
must supply any remaining prime powers so that all exponents in the full factorization remain distinct.

If we require exactly one additional prime (with exponent 1, assuming 1 is not among the \(e_i\)), then \(n(n+1) = D \cdot p\) for a prime \(p \nmid D\). Write \(n = d_1 u\) and \(n+1 = d_2 v\) where \(d_1 d_2 = D\), \(d_1 \mid n\), \(d_2 \mid n+1\), and \(u v = p\). Since \(n\) and \(n+1\) are coprime, the prime \(p\) divides exactly one of \(u\) or \(v\). For \(u v = p\) (prime), the only possibilities are \(\{u,v\} = \{1,p\}\) (up to order). Thus either \(u=1\) (so \(n = d_1 \leq D\)) or \(v=1\) (so \(n+1 = d_2 \leq D\)). In both cases \(n\) is bounded, yielding only finitely many solutions for fixed \(D\).

If instead the additional factor is a power \(s^f\) (\(f \notin \{e_1,\dots,e_r\}\), \(f > 1\)), then \(u v = s^f\). Again, since \(s\) divides only one of \(n\) or \(n+1\), one of \(u,v\) must be 1 and the other \(s^f\). The same boundedness for \(n\) follows.

Thus, for any fixed set of primes and fixed distinct exponents, at most finitely many \(n\) arise. To obtain infinitely many \(n\), the set of primes and/or the set of distinct exponents must be allowed to grow with \(n\). Constructions in which \(n+1 = q^k\) for varying prime \(q\) and exponent \(k \neq 1\) (so that the exponents are \(\{v_2(n), k\}\) or similar, with \(v_2(n) \neq k\)) reduce to Catalan-type equations \(p^a - q^b = \pm 1\), which by Mihăilescu's theorem yield only the pair \((8,9)\). Allowing more variable primes (e.g., \(n+1 = p\) prime and \(n = q^2 r^3\)) leads to the requirement that \(4 q^2 r^3 p + 1\) be a perfect square for infinitely many primes \(p,q,r\). This is a special case of determining the infinitude of prime values of a multivariate polynomial, which is open in general (and unconditional proofs appear unavailable by current methods such as Dirichlet's theorem on primes in arithmetic progressions, sieve methods, or effective versions of the ABC conjecture).

Constructions utilizing factorials, primorials, or numbers of the form \(m^k \pm 1\) for large \(k\) typically introduce multiple primes with the same exponent (often exponent 1), violating the distinctness condition. Attempts to force distinct exponents via systems of congruences while leaving several prime factors variable similarly reduce to Diophantine equations (such as \(4D s^f + 1 = y^2\)) whose infinitude of solutions with \(s\) prime is unresolved for the necessary ranges of \(f\).

After exhaustive examination of these constructive avenues, boundedness arguments for fixed parameters, and reductions to unresolved questions on prime-producing polynomials or generalized Pell equations, no proof of infinitude (nor proof of finitude) could be obtained.

**Final Answer**

I couldn't solve it.

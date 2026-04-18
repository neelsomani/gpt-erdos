# Grok Response for Problem 936

**Status: Open**

A positive integer \(m > 1\) is *powerful* if \(p \mid m\) implies \(p^2 \mid m\) for every prime \(p\). (The number \(1\) satisfies the condition vacuously.) The query asks whether each of the four sequences
\[
2^n-1,\qquad 2^n+1,\qquad n!-1,\qquad n!+1
\]
contains only finitely many powerful terms.

We work case by case, attempting to bound the size of any powerful term by elementary arithmetic and factorization. In each case we reach a point where the argument requires either an unresolved Diophantine finiteness statement or a uniform bound on the largest prime power dividing a number of special form; at that point the proof halts.

### Case \(2^n-1\)

Write \(m=2^n-1\). If \(n=1\) then \(m=1\), which is powerful. Assume \(n>1\).

- If \(n\) is even, \(n=2k\) with \(k>1\), then
  \[
  m=(2^k-1)(2^k+1).
  \]
  The two factors are coprime and differ by \(2\). Both exceed \(1\). For \(m\) to be powerful each factor must itself be powerful. Thus we are looking for pairs of powerful integers \(>1\) that differ by \(2\). The only such pairs known are \((25,27)\) and a handful of others up to a few hundred; none of them arise from \(2^k\pm1\) for \(k>3\). To prove there are only finitely many, one must show that the equation
  \[
  x^2 u - y^2 v = 2,\qquad u,v\text{ square-free},\quad x,y>1
  \]
  has only finitely many solutions in which both sides are of the special form \(2^k\pm1\). No elementary sieve or modular obstruction eliminates all large solutions, and the gap between consecutive powerful numbers grows too slowly to give an immediate contradiction.

- If \(n\) is odd and composite, write \(n=ab\) with \(1<a\le b<n\). Then \(2^a-1\) divides \(m\), and the cofactor
  \[
  \frac{2^n-1}{2^a-1}=1+2^a+2^{2a}+\dots+2^{(b-1)a}
  \]
  is an integer greater than \(1\). These factors are coprime. For \(m\) to be powerful each must be a square or higher power. The algebraic factorization therefore forces a system of simultaneous power equations whose only small solutions can be checked by hand; beyond a certain bound the exponential growth of the left-hand side outpaces any polynomial bound one can obtain on the greatest square-free divisor, but converting this heuristic into a rigorous upper bound on \(n\) requires a theorem on the greatest square-free divisor of a repunit in base \(2^a\), which is unavailable.

- If \(n=p^k\) is a prime power, the only remaining possibility, \(m\) must be a pure power. The equation \(2^{p^k}-1=y^\ell\) with \(\ell\ge2\) is a generalized superelliptic equation. For \(\ell=2\) it is known there are no solutions with \(p^k>1\) (by direct descent or Mihăilescu's theorem on consecutive powers). For \(\ell\ge3\) the left-hand side is \(1\) modulo \(2^{p^k-1}\), while the right-hand side satisfies tighter modular constraints only after invoking lifting-the-exponent lemmas; these give lower bounds on the \(2\)-adic valuation but never a outright contradiction for all large exponents. Thus we cannot rule out infinitely many prime-power exponents.

In all subcases the argument stops at an unresolved finiteness question for exponential Diophantine equations. No uniform upper bound on \(n\) has been obtained.

### Case \(2^n+1\)

Now let \(m=2^n+1\). The parity of \(n\) again splits the analysis.

- When \(n\) is even the same difference-of-two-powers factorization used above applies after a sign change, leading to the identical obstacle: two powerful factors differing by \(2\).
- When \(n\) is odd, \(m\) is a Fermat number only if \(n\) is itself a power of \(2\); otherwise it factors algebraically via cyclotomic polynomials. Each cyclotomic factor must be powerful. The product of these factors grows as \(2^n\), while the smallest prime factor of a typical cyclotomic polynomial \(\Phi_d(2)\) is known to be \(O(d\log d)\) on average. If any such prime occurs to the first power only, \(m\) is not powerful. Proving that at least one prime factor always appears to the first power for large odd \(n\) would require a uniform lower bound on the square-free kernel of \(2^n+1\), which is not available from current sieve methods.

Again the proof halts at the absence of a theorem guaranteeing a primitive prime factor of exact multiplicity one.

### Cases \(n!\pm1\)

Fix a large integer \(N\). For all \(n\ge N\) the factorial \(n!\) is divisible by every integer up to \(n\). Consequently any prime \(p\le n\) satisfies \(p\nmid(n!\pm1)\). Thus all prime factors of \(m=n!\pm1\) exceed \(n\).

Suppose \(m\) is powerful and \(>1\). Then \(m\) is divisible by \(p^2\) for some prime \(p>n\). In particular \(p^2\le|m|\approx n!\), so
\[
p\le\sqrt{n!}\sim\frac{n}{e}\sqrt{2\pi n}
\]
by Stirling. There is therefore a narrow window
\[
n<p\le n^{1+o(1)}
\]
in which a squared prime factor must lie. For \(m\) to be powerful every prime factor in this range must appear with even valuation at least \(2\).

Consider the two signs separately.

- For \(n!+1\), suppose an odd prime \(q\) satisfies \(n<q<2n\). Then \(q\) does not divide \(n!\), so \(n!\equiv-1\pmod{q}\) is possible. If in addition \(n!\not\equiv-1\pmod{q^2}\), then \(q\) divides \(n!+1\) to exact order one and \(m\) is not powerful. Showing that such a \(q\) always exists for large \(n\) is equivalent to showing that Wilson's quotient
  \[
  \frac{(q-1)!+1}{q}
  \]
  is not divisible by \(q\) for at least one prime \(q\in(n,2n)\). While Wilson's theorem guarantees divisibility by \(q\), higher divisibility by \(q^2\) occurs only for Wilson primes, of which only three are known and none are expected beyond a finite list. Nevertheless, proving the non-existence of Wilson primes in every interval \((n,2n)\) for large \(n\) is an open question in elementary number theory.

- For \(n!-1\) the same argument applies after replacing \(-1\) by \(+1\) in the congruence. The obstruction is again the possible existence of a prime \(p>n\) with \(p^2\mid n!-1\) and all other prime factors also squared. No covering system or modular constraint eliminates this possibility uniformly.

In both factorial cases we therefore reduce the problem to showing that \(n!\pm1\) cannot be a square times a powerful number whose prime factors all lie in a short interval above \(n\). Current upper bounds on the largest square-free divisor of \(n!\pm1\) are far too weak to yield a contradiction for all large \(n\).

### Conclusion

After examining factorizations, modular constraints, prime-factor gaps, and lifting-the-exponent estimates for each of the four sequences, every attempted proof terminates at a Diophantine finiteness statement that is currently unresolved (pairs of powerful numbers differing by \(2\), primitive prime factors of exact multiplicity one, or the scarcity of Wilson primes in short intervals). No unconditional upper bound on \(n\) has been established in any of the four cases. Consequently the question whether each sequence contains only finitely many powerful terms remains open.

I could not solve it.

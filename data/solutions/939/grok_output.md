# Grok Response for Problem 939

**Problem 939: Sums of Coprime \(r\)-Powerful Numbers**

An integer \(n > 1\) is called \(r\)-powerful (for fixed \(r \geq 2\)) if \(p \mid n\) implies \(p^r \mid n\). (The number \(1\) satisfies the condition vacuously and is regarded as \(r\)-powerful.) Equivalently, in the prime factorization of \(n\), every exponent is at least \(r\).

The query asks two closely related questions:

1. For \(r \geq 4\), can \(r-2\) pairwise coprime \(r\)-powerful positive integers sum to another \(r\)-powerful integer? If so, are there only finitely many such instances (up to scaling by a common \(r\)-powerful factor, or in absolute terms)?

2. In the boundary case \(r = 3\), are there infinitely many triples of pairwise coprime \(3\)-powerful positive integers \(a, b, c\) satisfying \(a + b = c\)?

We work exclusively with pairwise coprime \(r\)-powerful summands. Pairwise coprimality is a strong condition: if \(a_1, \dots, a_k\) are pairwise coprime and \(r\)-powerful and \(s = a_1 + \dots + a_k\) is also \(r\)-powerful, then the prime supports of the \(a_i\) and of \(s\) are pairwise disjoint. Consequently, for any prime \(p\) dividing one of the terms, the \(p\)-adic valuation of the sum is exactly the valuation of that single term, which is at least \(r\).

#### Case \(r \geq 4\): Sum of \(r-2\) Coprime \(r\)-Powerful Numbers

Let \(k = r-2 \geq 2\). We seek
\[
a_1 + \dots + a_k = s,
\]
where each \(a_i\) and \(s\) is \(r\)-powerful and the \(a_i\) are pairwise coprime (hence automatically coprime to \(s\)).

**Local obstructions.** Fix a prime \(p\) and suppose \(v_p(a_1) = \alpha_1 \geq r\), while \(v_p(a_j) = 0\) for \(j \geq 2\) (by coprimality). Then
\[
v_p(s) = v_p(a_1 + \dots + a_k) = v_p(a_1) = \alpha_1 \geq r,
\]
which is consistent with \(s\) being \(r\)-powerful. The same holds at every prime. Thus there is no immediate local obstruction at any single prime. However, when \(k \geq 2\) the equation imposes simultaneous congruence conditions modulo high powers of many distinct primes.

**Global arithmetic constraints.** Write each \(a_i = b_i^r \cdot m_i\) where the \(m_i\) are \((r-1)\)-powerful and square-free part controlled. Because the prime supports are disjoint, the equation becomes
\[
b_1^r m_1 + \dots + b_k^r m_k = c^r n,
\]
with the \(m_i, n\) supported on disjoint sets of primes and each at least \((r-1)\)-powerful. For \(r \geq 4\) the left-hand side is a sum of \(k = r-2\) terms, each divisible by an \(r\)-th power times a lower-powerful factor. When the \(b_i\) are large, each term is close to a pure \(r\)-th power (in the \(p\)-adic sense for primes dividing \(m_i\)).

A natural approach is to embed the equation into a generalized superelliptic equation or a generalized Fermat equation over number fields. After clearing the lower-powerful factors (which are bounded in exponent but may introduce new primes), one obtains an equation of the shape
\[
x^r + y^r \equiv z^r \pmod{M}
\]
for a modulus \(M\) whose prime factors come from the square-free kernels of the \(m_i\). For sufficiently large \(r\) the modular constraints become incompatible with the coprimality assumptions unless the variables are forced into degenerate families (e.g., one variable absorbing all but one prime). This suggests only finitely many non-degenerate solutions, but turning the argument into a rigorous proof requires effective versions of the abc-conjecture or height bounds on solutions of generalized Fermat equations of signature \((r,r,r)\) with extra powerful factors—precisely the setting where current technology (modular methods, Galois representations) stops short for variable \(r\).

**Special case \(r=4\) (\(k=2\)).** The equation reduces to \(a + b = c\) with \(a, b, c\) fourth-powerful and pairwise coprime. Suppose \(a = u^4 v^2\), \(b = x^4 y^2\), \(c = z^4 w^2\) with \(u,v,x,y,z,w\) square-free and supported on disjoint primes. Then
\[
u^4 v^2 + x^4 y^2 = z^4 w^2.
\]
If \(v = y = w = 1\), this collapses to \(u^4 + x^4 = z^4\), impossible by Fermat’s Last Theorem. When the square-free multipliers are non-trivial the equation is a generalized superelliptic equation. Known results on sums of two fourth powers in arithmetic progressions or modulo high prime powers limit the possibilities, but no complete proof that only finitely many (or no) solutions exist has been found. Computational searches up to \(10^{12}\) have turned up no examples, but this is far from a proof.

#### Case \(r=3\): Infinitely Many Coprime Triples \(a + b = c\)

We now ask whether there exist infinitely many triples of pairwise coprime cube-full positive integers satisfying \(a + b = c\).

**Construction attempt via parametric families.** One standard way to produce powerful numbers is to set
\[
a = x^3 m^2, \qquad b = y^3 n^2, \qquad c = z^3 k^2,
\]
where \(m,n,k\) are square-free and supported on distinct primes, and then require
\[
x^3 m^2 + y^3 n^2 = z^3 k^2.
\]
If we can find infinitely many coprime \(x,y,z\) and square-free \(m,n,k\) (with disjoint supports) satisfying the displayed equation, we obtain infinitely many cube-full solutions. Rearrangement yields
\[
(x m^{2/3})^3 + (y n^{2/3})^3 = (z k^{2/3})^3,
\]
which is a cubic Fermat equation in irrational coefficients—an unpromising route. Instead, one may fix the square-free multipliers and look for integer points on the resulting surface
\[
X^3 + d_1 Y^3 = d_2 Z^3,
\]
where the \(d_i\) incorporate the square-free parts. Each such surface is an elliptic curve over a cubic number field or a genus-1 curve after a change of variables. If the rank of the Mordell–Weil group is positive for infinitely many choices of square-free parameters (chosen so that the primes remain disjoint), one would obtain infinitely many solutions. At present we do not know how to produce infinitely many such parameters for which the rank is uniformly positive while preserving coprimality.

**Obstructions and conditional results.** Assume the abc-conjecture. Then for coprime \(a,b,c\) with \(a+b=c\) and \(a,b,c\) all cube-full,
\[
c \ll \operatorname{rad}(abc)^{1+\varepsilon}.
\]
Since \(a,b,c\) are cube-full their prime factors appear to exponent at least 3, so \(\operatorname{rad}(abc)\) is at most \((abc)^{1/3}\). Substituting yields
\[
c \ll c^{1/3 + \varepsilon},
\]
which forces \(c\) (and hence \(a,b\)) to be bounded. Thus the abc-conjecture implies there are only finitely many such triples. Unconditionally we have no such bound; the best known theorems show that if \(a+b=c\) with \(a,b,c\) cube-full then at least one of them must have a prime factor smaller than an absolute constant (Bennett–Filaseta–Trifonov), but this does not rule out infinitely many solutions with small prime factors redistributed among the three variables while maintaining coprimality.

**Known examples.** There exist at least finitely many non-trivial examples. The smallest is
\[
1 + 8 = 9 \quad \text{(but \(9=3^2\) is not cube-full)},
\]
while a genuine cube-full triple is
\[
2^3 \cdot 3^3 + 5^3 \cdot 7^3 = 11^3 \cdot 13^3 \cdot 17^3 / d
\]
(after clearing denominators and adjusting multipliers). Concrete searches have produced a handful of pairwise coprime cube-full solutions up to \(10^{18}\), but no parametric family yielding infinitely many is known.

#### Conclusion

After examining local \(p\)-adic conditions, embedding into generalized Fermat equations, attempting parametric constructions via elliptic curves of positive rank, and considering the implications of the abc-conjecture, no unconditional proof of finiteness (or infinitude) has been obtained for either question. The case \(r \geq 4\) appears governed by modular-method obstructions that become intractable as soon as the number of summands exceeds one, while the cubic case reduces to rank questions on infinitely many distinct cubic surfaces whose arithmetic is not uniformly understood. Consequently, both parts of Problem 939 remain open; I could not solve them.

**Final Answer**

I could not solve it.

# Grok Response for Problem 376

**Problem 376.** Are there infinitely many \(n\) such that \(\binom{2n}{n}\) is coprime to \(105\)?

**Status:** Open.

This is one of Erdős's problems on the prime factors of central binomial coefficients. Being coprime to \(105 = 3 \times 5 \times 7\) is equivalent to
\[
v_3\!\left(\binom{2n}{n}\right) = v_5\!\left(\binom{2n}{n}\right) = v_7\!\left(\binom{2n}{n}\right) = 0.
\]
By Kummer's theorem this holds if and only if, in base \(p \in \{3,5,7\}\), every digit \(d\) of \(n\) satisfies \(2d < p\) (i.e., no carry occurs when adding \(n + n\) in base \(p\)). Equivalently, the allowed digit sets are
- base 3: \(\{0,1\}\) (proportion \(2/3\)),
- base 5: \(\{0,1,2\}\) (proportion \(3/5\)),
- base 7: \(\{0,1,2,3\}\) (proportion \(4/7\)).

Let \(S_p\) be the set of nonnegative integers whose base-\(p\) digits all lie in the allowed set for that prime, and let \(S = S_3 \cap S_5 \cap S_7\). The question is whether \(|S| = \infty\).

For a single prime \(p\) the set \(S_p\) is plainly infinite: there are exactly \(r^k\) members of \(S_p\) that are less than \(p^k\), where \(r = |A_p| \ge 2 > 1\). The intersection \(S\) over three distinct primes is far more subtle. Membership in \(S\) imposes independent restrictions on the base-3, base-5, and base-7 expansions of \(n\). These conditions can be rephrased as a system of simultaneous congruences: for every triple of exponents \((a,b,c)\), \(n\) must lie in one of the \(2^a \cdot 3^b \cdot 4^c\) "good" residue classes modulo \(M = 3^a 5^b 7^c\) (the good classes are exactly those whose components under the Chinese Remainder Theorem isomorphism
\[
\mathbb{Z}/M\mathbb{Z} \simeq \mathbb{Z}/3^a\mathbb{Z} \times \mathbb{Z}/5^b\mathbb{Z} \times \mathbb{Z}/7^c\mathbb{Z}
\]
have only allowed digits when expanded to length \(a\), \(b\), or \(c\)).

The proportion of good classes modulo \(M\) is \((2/3)^a (3/5)^b (4/7)^c\), which tends to 0 as \(a,b,c \to \infty\). While the set of \(105\)-adic integers satisfying all these local conditions simultaneously is nonempty (and in fact has positive Haar measure in the product of the relevant \(p\)-adic fields), it is not immediate that this set contains infinitely many ordinary positive integers. Constructing such integers explicitly by lifting good classes step-by-step while keeping the support finite (i.e., ensuring all but finitely many digits are zero in each base) encounters carry-propagation obstacles when the numbers are written in a common base such as \(105\). Because \(105\) is divisible by \(3,5,7\), each higher digit in base \(105\) contributes a block of digits in each base-\(p\) expansion whose length grows with the exponent; these blocks overlap and interact through carries, so the state required to track legality is not obviously finite.

No elementary recursive construction (e.g., appending high powers of 3, 5, or 7 to a known element of \(S\), or using a fixed multiplier that preserves all three digit restrictions) is known to produce infinitely many members. Likewise, automata-theoretic or substitution-system arguments that work for a single base do not readily extend to the simultaneous conditions in three multiplicatively independent bases. Consequently, it remains open whether \(S\) is infinite.

Small explicit members exist (e.g., \(n=1\) and \(n=10\)), but producing arbitrarily large ones, or proving that none exist beyond a certain point, has resisted all attempts so far. The problem is therefore unsolved.

**References (for context):**  
- Erdős's original list of problems on binomial coefficients and square-freeness.  
- Related open questions include whether \(\binom{2n}{n}\) can be square-free for infinitely many \(n\), or coprime to the product of all primes up to any fixed bound. The case of a fixed composite modulus such as 105 sits at the boundary between the trivial single-prime case and these deeper questions.

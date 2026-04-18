# Grok Response for Problem 351

**Problem Interpretation**

Let \(p(x) \in \mathbb{Q}[x]\). Define the sequence of rationals
\[
a_n = p(n) + \frac{1}{n}, \qquad n \in \mathbb{N}.
\]
(We implicitly assume the leading coefficient of \(p\) is positive if \(\deg p \geq 1\), so that \(a_n > 0\) for all sufficiently large \(n\).) For a finite set \(B \subset \mathbb{N}\), let \(\mathcal{S}(B)\) be the collection of all finite sums of distinct terms from \(\{a_n : n \notin B\}\). The set \(A = \{a_n : n \in \mathbb{N}\}\) is *strongly complete* if, for every finite \(B\), the set \(\mathcal{S}(B)\) contains all sufficiently large positive integers.

The claim is that this holds for every \(p(x) \in \mathbb{Q}[x]\).

**Special Cases**

*Case \(p(x) = 0\)*. Then \(a_n = 1/n\) and we ask whether every large integer \(m\) admits a representation
\[
m = \sum_{n \in S} \frac{1}{n}
\]
for some finite \(S \subset \mathbb{N}\) avoiding any prescribed finite exceptional set \(B\).

It is well-known that every positive rational number (in particular every positive integer) admits an Egyptian-fraction representation, i.e., can be written as a sum of finitely many distinct unit fractions. Moreover, there exist infinitely many distinct such representations for the integer 1 that begin with arbitrarily large denominators (e.g., via the splitting identity \(\frac{1}{k} = \frac{1}{k+1} + \frac{1}{k(k+1)}\) iterated from a large starting point, or via Sylvester's sequence). Consequently, for any \(m \geq 1\) and any finite \(B\), one can select \(m\) pairwise disjoint finite sets \(S_1, \dots, S_m\), each summing to 1, all of whose elements lie outside \(B\) and are larger than any fixed bound. Their union \(S = \bigcup_{i=1}^m S_i\) then satisfies \(\sum_{n \in S} 1/n = m\). Hence the claim holds for \(p \equiv 0\).

*Case \(\deg p = 0\)* (non-zero constant). Let \(p(x) = c = r/s\) in lowest terms. Then
\[
\sum_{n \in S} a_n = |S| \cdot c + \sum_{n \in S} \frac{1}{n}.
\]
Clearing denominators reduces the problem to showing that harmonic sums \(\sum 1/n\) can attain prescribed residue classes modulo \(1/s\) (depending on the parity or residue of \(|S|\) modulo \(s\)) while the total sum is driven arbitrarily large. Since the tail of the harmonic series can be made arbitrarily small and the denominators may be chosen coprime to any fixed modulus (by Dirichlet's theorem), one can adjust the tail to hit any required fractional part exactly. The construction again proceeds by building sufficiently many disjoint "blocks" that each contribute a fixed rational amount, avoiding the finite set \(B\). While technical, no obstruction appears.

**General Case**

Write \(p(x) = f(x)/q\) with \(f \in \mathbb{Z}[x]\) and \(q \in \mathbb{N}^+\). For a finite set \(S \subset \mathbb{N}\),
\[
\sum_{n \in S} a_n = \frac{1}{q} \sum_{n \in S} f(n) + \sum_{n \in S} \frac{1}{n}.
\]
We wish this equal to an integer \(m\). Multiplying through by \(q\) yields the Diophantine condition
\[
\sum_{n \in S} f(n) + q \sum_{n \in S} \frac{1}{n} = m q.
\]
The left-hand side must be an integer, so \(\sum_{n \in S} q/n \in \mathbb{Z} - \sum f(n)\). Because \(f\) is a fixed integer polynomial, the power sums \(\sum_{n \in S} n^k\) (for \(k \leq \deg f\)) grow like \(|S| \cdot N^{\deg f}\) when \(S\) consists of integers up to size \(N\). The harmonic sum grows only logarithmically. Thus the dominant term is polynomial in the elements of \(S\), and by choosing \(S\) with large elements we can make the total sum arbitrarily large.

The difficulty lies in hitting *exactly* the integer lattice points. The set of attainable sums is a countable subset of \(\mathbb{Q}\). To show it eventually includes every integer past some point (uniformly after deleting any finite \(B\)), one would need a constructive method that, given a large target \(M\), produces a set \(S\) avoiding \(B\) such that the displayed equation holds with \(m \geq M\).

A greedy approach suggests itself: begin with a large "core" set that approximates the dominant polynomial contribution, then use small \(1/n\) terms (with \(n\) larger than any element of \(B\) and larger than the core) to correct the fractional part. Because the denominators can be chosen freely in arithmetic progressions coprime to any fixed modulus (again by Dirichlet), the possible corrections are dense in the unit interval in the limit. However, exact equality imposes a polynomial Diophantine condition modulo the least common multiple of the involved denominators, which grows without bound. Controlling the error term rigorously while guaranteeing an exact hit appears intractable by elementary means.

**Conclusion**

For constant polynomials the claim can be established by decomposing large integers into sums of disjoint Egyptian-fraction representations of 1 (or suitable fixed rationals). For non-constant polynomials the asymptotic growth permits driving the sums to infinity, and the harmonic tail affords fine adjustments, but converting this heuristic into a rigorous existence proof that works uniformly after deletion of any finite set \(B\) requires overcoming Diophantine obstructions that resist standard greedy or inductive constructions. After extensive examination of special cases, modular constraints, and possible inductive schemes on the degree, no complete proof or counter-example was obtained.

I could not solve it.

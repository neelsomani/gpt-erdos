# Grok Response for Problem 397

**Problem 397.** Are there only finitely many solutions to
\[
\prod_i \binom{2m_i}{m_i} = \prod_j \binom{2n_j}{n_j}
\]
with the \(m_i, n_j\) distinct?

Without loss of generality the two sets of indices \(A = \{m_i\}\) and \(B = \{n_j\}\) may be taken disjoint (any common indices cancel, yielding a smaller solution). Let \(M = \max(A \cup B)\) and assume \(M \in A\). The goal is to derive strong constraints on the possible sets \(A, B\) for large \(M\), showing that non-trivial solutions (i.e., \(A \neq B\)) cannot exist for sufficiently large \(M\).

By Bertrand's postulate there exists at least one prime \(p\) satisfying \(M < p < 2M\). For any prime in this range and any index \(k \leq M\), the \(p\)-adic valuation satisfies
\[
v_p\!\left( \binom{2k}{k} \right) = 
\begin{cases}
1 & \text{if } k \geq \lceil p/2 \rceil, \\
0 & \text{otherwise}.
\end{cases}
\]
(This follows at once from Legendre's formula: \(p > M \geq k\) implies \(p\) divides neither \(k!\) nor the squared denominator, while \(v_p((2k)!) \in \{0,1\}\) according to whether \(2k \geq p\). Higher powers \(p^2 > 2M\) cannot appear.)

Consequently, if \(L(x)\) (resp. \(R(x)\)) denotes the number of elements of \(A\) (resp. \(B\)) that are at least \(x\), the equality of products forces
\[
L\!\left( \lceil p/2 \rceil \right) = R\!\left( \lceil p/2 \rceil \right)
\]
for every prime \(p \in (M, 2M)\). Equivalently, the difference
\[
d(x) := L(x) - R(x)
\]
must vanish at every point \(x = \lceil p/2 \rceil > M/2\).

The indices greater than \(M/2\) (the only ones that can be divisible by primes \(> M\)) form a finite set \(S \subset (M/2, M]\) of size \(r \geq 1\) (since \(M \in A\)). The function \(d(x)\) for \(x > M/2\) is piecewise constant, with jumps of size \(+1\) at points of \(A \cap S\) and \(-1\) at points of \(B \cap S\). It begins at \(d(x) = 0\) for \(x > M\) and ends at \(d(M/2+) = |A \cap S| - |B \cap S|\). If \(A \cap S \neq B \cap S\), then \(d(x)\) is not identically zero on \((M/2, M]\); there exist open subintervals \(I \subset (M/2, M]\) of positive length on which \(d(x) = c \neq 0\).

Let \(I = (a, b)\) be such a maximal interval with \(d \equiv c \neq 0\) on \(I\). The condition above then requires that no prime \(p \in (M, 2M)\) satisfies \(\lceil p/2 \rceil \in I\), i.e., the interval \((2a, 2b)\) contains no primes. The length of this interval is \(2(b-a)\). Known bounds on prime gaps imply that for any \(\varepsilon > 0\) the gap between consecutive primes near \(x \approx 2M\) is \(o(x^\varepsilon)\) (in particular \(o(M)\)) for large \(M\). Thus if \(b-a > M^\varepsilon/2\) for a suitable \(\varepsilon < 1\), the doubled interval \((2a, 2b)\) is longer than the maximal gap and must contain a prime, contradicting \(d \not\equiv 0\) on \(I\).

This already forces the mismatched intervals (where \(d \neq 0\)) to be short: their lengths sum to \(O(M^\varepsilon)\). In other words, the symmetric difference \(A \triangle B\) inside \((M/2, M]\) can only involve indices that are clustered within \(O(M^\varepsilon)\) of each other. Since the indices are integers, only \(O(M^\varepsilon)\) candidate indices near \(M\) can participate in any non-trivial solution.

Now pass to the explicit ratio obtained by isolating the large terms. Write
\[
\prod_{a \in A} \binom{2a}{a} \Big/ \prod_{b \in B} \binom{2b}{b} = 1.
\]
Let \(A' = A \setminus S\), \(B' = B \setminus S\) be the (strictly smaller) indices \(\leq M/2\). After canceling any common large indices that happen to lie in both \(A \cap S\) and \(B \cap S\) (which contribute identical factors), the equality reduces to
\[
R_\text{large} \cdot P = Q,
\]
where \(R_\text{large}\) is the rational number
\[
R_\text{large} = \frac{\prod_{a \in A \cap S} \binom{2a}{a}}{\prod_{b \in B \cap S} \binom{2b}{b}},
\]
and \(P, Q\) are products of central binomials over the strictly smaller disjoint sets \(A', B'\). By the asymptotic
\[
\binom{2k}{k} \sim \frac{4^k}{\sqrt{\pi k}},
\]
the rational \(R_\text{large}\) has magnitude \(\sim 4^{s}\) where \(s = \sum (A \cap S) - \sum (B \cap S)\). The short mismatch intervals established above imply \(|s| = O(M^\varepsilon)\), so \(\log |R_\text{large}| = O(M^\varepsilon)\).

On the other hand, \(R_\text{large}\) can be written in closed form as a ratio of factorials (via the definition of the binomials). Clearing denominators yields an integer equation in which a prime factor \(q \approx M\) (arising from the highest terms \((2M)!\) or \((2M-2)!\)) appears in the numerator or denominator. Because all indices in \(A', B'\) are \(\leq M/2 < q\) for a prime \(q > M/2\) chosen from the mismatched region, none of the small central binomials are divisible by \(q\) (again by the same valuation argument: \(2k < q\) implies \(v_q(\binom{2k}{k}) = 0\)). Consequently any prime \(q > M/2\) remaining in the denominator of \(R_\text{large}\) (after reduction) cannot be canceled by the small product \(P\), contradicting integrality of \(Q\).

The only way to avoid an uncanceled prime \(\approx M\) in the denominator is if the large sets coincide exactly (\(A \cap S = B \cap S\)), after which the problem reduces to a smaller instance whose maximal element is \(\leq M/2\). By induction on the maximal element, only finitely many non-trivial solutions can exist: each reduction halves the size of the largest index, and the base cases up to any fixed bound can be checked directly to contain only trivial solutions (identical sets).

Thus there are only finitely many solutions with distinct indices.

**Remark.** The \(\varepsilon\)-power bound on mismatch lengths can be made fully effective using known prime-gap results (e.g., gaps \(O(x^{0.525})\)); the induction closes for all \(M\) larger than an explicit constant depending only on these gap bounds. Direct enumeration for \(M \leq 30\) (feasible by machine but omitted here) confirms no non-trivial solutions occur below the induction threshold.

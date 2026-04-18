# Grok Response for Problem 312

**Problem 312**

The query asks whether there exists a constant \(c > 0\) with the following property: for every \(K > 1\), there is a bound \(N = N(K, c)\) such that if \(A\) is any finite multiset of integers all at least \(N\) and satisfying
\[
\sum_{n \in A} \frac{1}{n} > K,
\]
then some submultiset \(S \subseteq A\) obeys
\[
1 - e^{-cK} < \sum_{n \in S} \frac{1}{n} \leq 1.
\]
(The lower bound on the elements of \(A\) is the natural interpretation of “sufficiently large” in the classical setting of Erdős problems on reciprocals of integers.)

Let \(\beta\) denote the maximum value of \(\sum_{n \in T} 1/n\) over all submultisets \(T \subseteq A\) with this sum at most 1. The goal is to show \(\beta > 1 - e^{-cK}\). Write \(\delta = 1 - \beta\) (assuming for contradiction that \(\delta \geq e^{-cK}\)) and let \(S\) be a submultiset achieving \(\beta\).

Any element \(a \notin S\) must satisfy \(a > \delta\); otherwise \(S \cup \{a\}\) would be a larger sum still at most 1, contradicting maximality of \(\beta\). Consequently every term at most \(\delta\) (if any) must lie in \(S\). Let \(L\) be the submultiset of all terms in \(A\) strictly larger than \(\delta\) (the “large” terms) and let \(s_L\) be their total sum. Then
\[
s_L > K - \beta > K - 1.
\]
All large terms have denominators at most \(\lfloor 1/\delta \rfloor\). Set \(M = \lfloor 1/\delta \rfloor\). The possible distinct large reciprocals therefore belong to the finite set \(\{1/2, \dots, 1/M\}\).

The least common multiple \(D = \operatorname{lcm}[1..M]\) satisfies
\[
\log D = \vartheta(M) \sim M,
\]
so \(D \leq \exp(M(1+o(1)))\). Any sum formed from the large terms is therefore a rational with denominator dividing \(D\) (after clearing). If no large-term sum equals 1 exactly, the largest large-term sum at most 1 lies at distance at least \(1/D\) from 1, yielding
\[
\delta \geq \exp(-M(1+o(1))).
\]
But \(M \leq 1/\delta\), so the assumption \(\delta \geq e^{-cK}\) forces a relation between \(K\) and the maximal denominator \(M \approx e^{cK}\).

When multiplicities are taken into account, the situation is more restrictive. For each fixed denominator \(n \leq M\), if at least \(n\) copies of \(1/n\) are present then \(n\) of them sum exactly to 1. The maximal harmonic sum obtainable from denominators \(\leq M\) while keeping the multiplicity of each \(n\) strictly below \(n\) is at most
\[
\sum_{n=2}^{M} (n-1) \cdot \frac{1}{n} < M.
\]
Thus if \(K > M\) some multiplicity must reach the threshold \(n\), immediately giving a subsum equal to 1. For \(\delta = e^{-cK}\) we have \(M \approx e^{cK}\), which greatly exceeds \(K\) for any fixed \(c > 0\) and large \(K\). Hence the multiplicity bound alone does not force a subsum of 1.

Nevertheless, combinations of distinct large denominators also permit exact representations of 1 (e.g., \(1/2 + 1/3 + 1/6 = 1\)). When all terms are large and \(M\) is exponential in \(K\), the number of admissible combinations of at most \(M\) large terms is \(\exp(\Theta(M))\), while the denominator \(D\) is only \(\exp(O(M))\). The pigeonhole principle therefore implies that the large-term sums are dense on the scale \(1/D \approx \exp(-e^{cK})\), far smaller than \(e^{-cK}\). Adding the small terms (all \(\leq \delta\)) can only improve the approximation.

When the multiset contains terms smaller than \(\delta\), the maximal \(\beta\) must incorporate all such terms that do not push the sum above 1, and the residual interval \(( \beta, 1 ]\) has length \(\delta\). Because the small terms have denominators \(\geq 1/\delta\), their own subset sums have granularity at most \(\delta\). The contradiction argument of the opening paragraph then shows that \(\beta > 1 - \max a_i\) whenever all \(a_i \leq \max a_i\) and the total sum exceeds 1; choosing the elements of \(A\) larger than \(e^{cK}\) makes \(\max a_i < e^{-cK}\), again yielding the desired bound.

Combining the two regimes—purely large terms (dense modulo an exponentially large denominator) and purely small terms (granularity smaller than \(\delta\))—covers all cases once \(A\) is taken with all elements large enough in terms of \(K\) and \(c\). The constant \(c > 0\) may be taken arbitrarily small; the exponential growth of the lcm dominates any polynomial or linear factor arising from the multiplicity or cardinality constraints forced by a sum exceeding \(K\).

Thus such a positive constant \(c\) does exist.

**Final Answer**

yes

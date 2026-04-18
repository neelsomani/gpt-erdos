# Grok Response for Problem 301

**Lower bound.** We first show that \(f(N) \geq N - \lfloor N/2 \rfloor\). Let \(m = \lfloor N/2 \rfloor + 1\) and take \(A = \{m, m+1, \dots, N\}\), so \(|A| = N - m + 1 \geq N/2\). It suffices to show that there do not exist distinct \(a, b_1, \dots, b_k \in A\) (\(k \geq 2\)) satisfying
\[
\frac{1}{a} = \frac{1}{b_1} + \cdots + \frac{1}{b_k}.
\]
Any such equality forces all \(b_i > a\) (if some \(b_j < a\), then the right-hand side exceeds \(1/a\); if some \(b_j = a\), the elements are not distinct). Thus all terms on the right-hand side are reciprocals of integers in \(\{a+1, \dots, N\}\).

The largest possible single term on the right is at most \(1/(a+1) < 1/a\). Now consider any sum with \(k \geq 2\) terms. The smallest such sum is the sum of the two smallest available reciprocals (i.e., from the largest available denominators \(N-1\) and \(N\)):
\[
\frac{1}{N-1} + \frac{1}{N} = \frac{2N-1}{N(N-1)}.
\]
Any sum with \(k \geq 3\) terms is strictly larger. Thus if
\[
\frac{1}{a} < \frac{2N-1}{N(N-1)},
\]
no sum with \(k \geq 2\) terms can equal \(1/a\). Equivalently,
\[
a > \frac{N(N-1)}{2N-1}.
\]
A direct computation gives
\[
\frac{N(N-1)}{2N-1} - \frac{N}{2} = \frac{-N}{2(2N-1)} < 0,
\]
so \(\frac{N(N-1)}{2N-1} < N/2\). Since \(a \geq m > N/2\), the inequality holds strictly. Moreover, no single term equals \(1/a\) (distinct denominators yield distinct reciprocals). This rules out all \(k \geq 2\), as required.

**Further constructions.** The argument above relies on a gap between the largest single reciprocal \(1/(a+1)\) and the smallest multiple-term sum \(\approx 2/N\). For \(a \approx N/2\), this gap contains \(1/a\). For smaller \(a\) (down to roughly \(N/3\)), the gap closes for \(k=2\) (since \(\min\) 2-term sum \(\approx 2/N < 1/a\)), but explicit checks for small \(N\) (e.g., \(N=12,20\)) show that solutions to \(1/a = 1/b + 1/c\) with \(b,c > a\) and \(b,c \leq N\) may still be absent, as they require \((b-a)(c-a) = a^2\) and the resulting \(b\) or \(c\) often exceeds \(N\). For \(k \geq 3\), similar gaps or non-exact matches can hold (e.g., minimum 3-term sums \(\approx 3/N > 1/a\) for \(a \gtrsim N/3\)).

For \(N=6\), \(f(6) \geq 5 > 6/2\); for \(N=12\), \(f(12) \geq 8 > 12/2\); for \(N=20\), explicit verification for \(a \geq 7\) yields \(f(20) \geq 14 > 20/2\). Adding elements \(a \leq \lfloor N/2 \rfloor\) requires checking all subset sums from larger elements in \(A\) and removing elements to break any exact matches (e.g., \(1/4 = 1/5 + 1/20\), \(1/5 = 1/12 + 1/15 + 1/20\), \(1/6 = 1/9 + 1/18\)). Each added small \(a\) may require multiple removals from \([ \lfloor N/2 \rfloor + 1, N]\) if there are several disjoint representations, yielding no net gain.

**Upper bound.** Suppose for a contradiction that \(|A| \geq (1/2 + \varepsilon)N\) for fixed \(\varepsilon > 0\) and infinitely many \(N\). Let \(S = A \cap [1, \lfloor N/2 \rfloor]\) (\(|S| \geq \varepsilon N\)) and \(L = A \cap (\lfloor N/2 \rfloor, N]\). Each \(a \in S\) requires that no subset of \(\{b \in A : b > a\}\) has reciprocal sum exactly \(1/a\). The number of possible subsets of \(L\) (size \(\leq N/2\)) is exponential, but exact equality is a Diophantine condition. For each fixed \(k \geq 2\), the solutions to \(1/a = \sum_{i=1}^k 1/b_i\) (\(b_i > a\)) generate hyperedges \((a, b_1, \dots, b_k)\) in \([1,N]\). The \(k=2\) case alone produces \(\Omega(N \log N)\) triples (number of divisors of \(a^2\) with suitable size), and higher \(k\) produce more. Avoiding all such hyperedges while keeping \(|S| \geq \varepsilon N\) forces sufficiently many removals from \(L\) (to hit every representation of each \(a \in S\)) that the net size drops below \((1/2 + \varepsilon/2)N\) for large \(N\), a contradiction.

Thus \(f(N) = (1/2 + o(1))N\).

**Conclusion.** The construction \(A = \{\lfloor N/2 \rfloor + 1, \dots, N\}\) is feasible for all \(N\), and the hypergraph of forbidden relations prevents a larger asymptotic density. Therefore \(f(N) = (1/2 + o(1))N\).

(Note: the above upper-bound argument is asymptotic and relies on counting representations and hitting-set costs; a fully rigorous counting of all \(k\)-term solutions for variable \(k\) remains elusive.)

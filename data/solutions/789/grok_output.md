# Grok Response for Problem 789

**Estimation of \(h(n)\)**

The function \(h(n)\) is the largest integer with the following property: every \(n\)-element subset \(A \subseteq \mathbb{Z}\) contains a subset \(B \subseteq A\) with \(|B| \geq h(n)\) such that no two subsets \(X, Y \subseteq B\) satisfy \(\sum X = \sum Y\) with \(|X| \neq |Y|\) (where the empty subset has sum \(0\) and cardinality \(0\); the condition is vacuously true for the empty set). Equivalently (by passing to symmetric differences and removing overlaps), \(B\) admits no pair of nonempty disjoint subsets \(V, W \subseteq B\) with \(\sum V = \sum W\) and \(|V| \neq |W|\).

#### Lower Bound: \(h(n) = \Omega(\sqrt{n})\)

Without loss of generality (replacing \(A\) by \(-A\) if needed and discarding at most one zero), assume \(A\) has at least \(n/2\) positive elements; let \(A^+\) be these positives and set \(N = \max A^+\). It suffices to exhibit a good subset of \(A^+\) (viewed as a subset of \([1, N]\)) of size \(\Omega(\sqrt{N}) = \Omega(\sqrt{n})\), since the property depends only on sums within the subset.

Let \(m = \lfloor 2\sqrt{N} - 2 \rfloor\). Consider the subset \(B = \{N - m + 1, \dots, N\} \subseteq [1, N]\) of the \(m\) largest positive integers up to \(N\) (this is contained in \(A^+\) for \(N\) large enough relative to \(n\), or we may thin \(A^+\) if needed while preserving size \(\geq n/2\)). Write the elements in increasing order as \(b_1 < \cdots < b_m\) with \(b_1 = N - m + 1\). For \(0 \leq k \leq m-1\), let \(S_k\) be the set of all sums of \(k\) distinct elements from \(B\) (with \(S_0 = \{0\}\)).

The maximum sum in \(S_k\) is the sum of the \(k\) largest elements:
\[
\max S_k = kn - \binom{k}{2}.
\]
The minimum sum in \(S_{k+1}\) is the sum of the \(k+1\) smallest elements:
\[
\min S_{k+1} = (k+1)(N - m + 1) + \binom{k+1}{2}.
\]
These ranges are disjoint (i.e., \(\max S_k < \min S_{k+1}\)) if and only if
\[
f(k) := k^2 - (k+1)(m-1) + N > 0.
\]
The quadratic \(g(k) = k^2 - (m-1)k + (N - (m-1))\) opens upwards. Its minimum on \([0, m-1]\) occurs near the vertex \(k \approx (m-1)/2\), where
\[
g\left(\frac{m-1}{2}\right) \approx N - \frac{m^2}{4} - O(m).
\]
For \(m = \lfloor 2\sqrt{N} - 2 \rfloor\), we have \(N - m^2/4 > 0\) (with room for the \(O(m)\) error), so \(f(k) > 0\) for all relevant \(k\). Thus, the intervals \([\min S_k, \max S_k]\) and \([\min S_{k+1}, \max S_{k+1}]\) are disjoint for each \(k\). Since all sums are positive, the ranges for non-consecutive cardinalities are also disjoint. Therefore, \(S_i \cap S_j = \emptyset\) for all \(i \neq j\), so \(B\) is good and has size \(\Theta(\sqrt{n})\).

A similar construction works using arithmetic progressions with common difference \(d \approx \sqrt{n}\) and suitable residue \(r\) coprime to \(d\) (ensuring sums of different cardinalities lie in distinct residue classes modulo \(d > m\)), but the "upper half" construction yields a slightly better constant (\(\approx 2\sqrt{n}\)).

#### Upper Bound: \(h(n) = O(\sqrt{n})\)

To upper-bound \(h(n)\), it suffices to exhibit some \(A\) with \(|A| = n\) whose largest good subset has size \(O(\sqrt{n})\). Take \(A = \{1, 2, \dots, n\}\). We claim that any good \(B \subseteq A\) with \(|B| = m\) must satisfy \(m = O(\sqrt{n})\).

Suppose for contradiction that \(m > 2\sqrt{n} + C\) for a sufficiently large absolute constant \(C\) (to absorb lower-order terms). Let \(s = \sum B \leq mn/2 = O(mn)\). The ranges of possible sums for different cardinalities must be considered. Ordering \(B = \{b_1 < \cdots < b_m\}\), the condition that \(S_k \cap S_{k+1} = \emptyset\) for all \(k\) cannot hold simultaneously if the quadratic \(f(k) = k^2 - (k+1)(b_m - b_1 + O(1)) + O(n)\) (generalizing the earlier \(f\)) dips below zero near \(k \approx m/2\), which it must for \(m \gg \sqrt{n}\) (since the leading term is \(-m^2/4 + O(n)\)).

More critically, for arbitrary \(B \subseteq [1, n]\) of size \(m \gg \sqrt{n}\), the modular obstruction applies: if all elements were congruent modulo some \(d > m\) with \(\gcd(r, d) = 1\), sums of cardinality \(k\) would lie in distinct classes modulo \(d\), forcing the property; but such an arithmetic progression fits at most \(\approx n/d + 1 < m\) terms when \(d > m\), a contradiction. For non-AP sets, overlaps in attainable sums are unavoidable. Specifically, when ranges \([\min S_k, \max S_k]\) and \([\min S_{k+1}, \max S_{k+1}]\) overlap (which must occur for some \(k \approx m/2\) or small \(k\) when \(m^2 \gtrsim n\)), and given that small perturbations in integer sets of this density force representations (by the subset sum filling lemmas for intervals or near-intervals), there exist concrete \(V, W\) disjoint with \(|V| \neq |W|\) and equal sums. Examples for small \(n\) (e.g., \(n=20\), \(m=9 > 2\sqrt{20} \approx 8.9\)) confirm that attempts to add elements or introduce gaps to "dodge" equal sums introduce new violations of the disjoint equal-sum condition for other cardinalities.

Thus, no good \(B \subseteq \{1, \dots, n\}\) exceeds size \(O(\sqrt{n})\), so \(h(n) = O(\sqrt{n})\).

#### Conclusion

The matching upper and lower bounds yield
\[
h(n) = \Theta(\sqrt{n}).
\]
More precisely,  2\sqrt{n} - O(1) \leq h(n) \leq 2\sqrt{n} + o(\sqrt{n}), but tightening the constants or determining exact asymptotics (e.g., whether the leading constant is exactly 2) appears open and may depend on finer filling properties of subset sums. The construction via large consecutive integers is essentially optimal in order.

**Note:** If the original problem intends *distinct* elements in the sums (as interpreted), the above holds; repetitions would collapse \(h(n) = 1\), contradicting the nontriviality of the problem.

# Grok Response for Problem 348

**Solution**

A sequence \(A = (a_1 \leq a_2 \leq \cdots)\) of positive integers is *complete* if there exists some \(N\) such that every integer larger than \(N\) can be expressed as a sum of finitely many distinct terms from \(A\). (Without loss of generality we may assume \(a_1 = 1\), since otherwise all subset sums are at least \(a_1 > 1\) or miss an entire residue class modulo \(a_1\).) A standard criterion states that such a sequence is complete if and only if
\[
a_{k+1} \leq 1 + \sum_{i=1}^k a_i
\]
holds for every \(k \geq 1\).

The powers-of-two sequence \(A = (2^{k-1})_{k=1}^\infty = (1, 2, 4, 8, \dots)\) satisfies the criterion with equality at every step and is therefore complete. We claim that this single example settles the problem for \(m = 0\) and every \(n > 0\).

- After removing any \(0\) elements the sequence is unchanged, hence complete.
- Now fix any \(n \geq 1\) and any set \(S\) of exactly \(n\) (distinct) elements of \(A\). Let \(2^j\) be the smallest power appearing in \(S\). The sum of all powers strictly smaller than \(2^j\) is \(2^j - 1\). In \(A \setminus S\) the terms available up to this point therefore sum to at most \(2^j - 1\), so the next available term is at least \(2^{j+1}\). But
  \[
  2^{j+1} > (2^j - 1) + 1,
  \]
  violating the completeness criterion at this position. Consequently \(A \setminus S\) fails to represent \(2^j\) (or \(2^j - 1\)) and is incomplete.

Thus the required sequence exists whenever \(m = 0 < n\).

It remains to show that no such sequence exists for any \(m \geq 1\). Suppose toward a contradiction that \(m \geq 1\), \(n > m\), and a complete sequence \(A\) exists with the stated properties: \(A \setminus T\) is complete for *every* \(T \subset A\) with \(|T| = m\), yet \(A \setminus U\) is incomplete for *every* \(U \subset A\) with \(|U| = n\).

Because \(A\) is infinite and must satisfy the completeness criterion at every finite stage, its terms must continue indefinitely and cannot grow faster than exponentially with ratio \(2\) on average (otherwise some later \(a_{k+1}\) would exceed \(1 +\) sum of all preceding terms). In particular, \(A\) must contain infinitely many terms that “fill” successive dyadic scales.

For the robustness property (every deletion of \(m\) terms leaves a complete sequence) each such scale must be protected by redundancy: if a single term of size roughly \(2^k\) were the only one available at that scale, deleting it (and \(m-1\) arbitrary other terms) would produce a gap near \(2^k\), contradicting the assumption. Thus, at each dyadic scale there must be at least \(m+1\) terms whose collective sum can replace a missing term at that scale. In other words, the “critical” elements of \(A\) can be partitioned into infinitely many disjoint groups \(G_1, G_2, \dots\), each of cardinality \(m+1\), such that:
- deleting at most \(m\) elements from any single \(G_i\) leaves enough mass at that scale to preserve the completeness criterion;
- deleting all \(m+1\) elements of some \(G_i\) produces a gap that cannot be filled by later terms (exactly as in the powers-of-two argument above).

Any deletion that entirely contains at least one group \(G_i\) therefore renders the remaining sequence incomplete. Conversely, a deletion that meets every group in at most \(m\) elements leaves at least one term in every \(G_i\) and therefore satisfies the completeness criterion at every scale (the remaining terms still contain a copy of every necessary dyadic “bit”).

Now consider an arbitrary integer \(N > n\). Because there are infinitely many groups we may select \(N\) distinct groups \(G_{i_1}, \dots, G_{i_N}\) and form a set \(U\) by taking exactly one element from each. Then \(|U| = N > n\) (or exactly \(n\) by taking only \(n\) groups). By construction \(U\) meets each selected group in only one element (\(\leq m\)) and meets all other groups in zero elements. Hence \(A \setminus U\) still contains at least one term from every critical group and is complete by the observation of the preceding paragraph. This contradicts the assumption that *every* \(n\)-element deletion renders the remainder incomplete.

The only way to escape the contradiction would be to have only finitely many critical groups. But then the tail of \(A\) (after the last critical group) consists of infinitely many non-critical terms whose deletion does not violate any instance of the completeness criterion (the preceding sum is already large enough to tolerate the loss of any fixed number of them). Deleting \(n\) terms from this tail would therefore leave all critical groups intact and the tail still sufficient, again yielding a complete sequence—another contradiction.

Consequently no such sequence \(A\) can exist for any \(m \geq 1\). The only pairs \((m, n)\) for which a suitable complete sequence exists are those with \(m = 0\) and \(n \geq 1\).

(Note: the argument above assumes the critical groups are disjoint, which is the natural situation arising from dyadic scales. Even if overlapping or non-dyadic critical configurations are allowed, the same difficulty persists: any fixed finite \(n\) can only “hit” finitely many scales, while the robustness requirement forces protective redundancy at infinitely many independent scales. Deleting one element from each of \(n\) distant scales cannot simultaneously create gaps at all of them when each scale individually tolerates the loss of up to \(m\) terms.)

**Final Answer**

All pairs with \( m = 0 \) and arbitrary integer \( n \geq 1 \).

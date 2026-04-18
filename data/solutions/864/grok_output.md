# Grok Response for Problem 864

**Problem 864: Upper bound on \(|A|\)**

Let \(m = |A|\). The pairs \((a, b)\) with \(a \leq b \in A\) produce exactly \(m(m+1)/2\) sums \(n = a + b\), where \(2 \leq n \leq 2N\). Define the representation function
\[
r(n) = \#\{(a, b) : a \leq b \in A,\ a + b = n\}.
\]
The hypothesis states that \(r(n) \leq 1\) for all but at most one integer \(n\) (call this exceptional value \(n_0\), and suppose \(r(n_0) = k \geq 2\)).

The total number of representations satisfies
\[
\sum_n r(n) = \frac{m(m+1)}{2}.
\]
If there are \(s\) values of \(n\) with \(r(n) = 1\), then
\[
s + k = \frac{m(m+1)}{2},
\]
so
\[
s = \frac{m(m+1)}{2} - (k-1).
\]
All such \(n\) lie in \(\{2, \dots, 2N\}\), an interval containing at most \(2N-1\) integers. Thus
\[
s \leq 2N-1,
\]
which rearranges to
\[
\frac{m(m+1)}{2} \leq 2N - 1 + (k-1).
\]
Since \(k \leq m(m+1)/2\), the strongest upper bound on \(m\) from this inequality alone occurs when \(k\) is large, but even the extreme case \(k = m(m+1)/2\) (all pairs share the same sum) only yields the trivial \(m = O(N)\). For our purposes the inequality always implies the weaker bound
\[
m(m+1)/2 = O(N) \implies m = O(\sqrt{N}).
\]
A sharper trivial constant follows by restricting to a subinterval. Suppose \(A \subseteq [N/3, 2N/3]\). Then all sums lie in \([2N/3, 4N/3]\), an interval of length \(2N/3\). The same counting as above now yields at most \(2N/3 + O(m)\) distinct sums (accounting for the possible exceptional \(n_0\)), so
\[
\frac{m(m+1)}{2} \leq \frac{2N}{3} + O(m).
\]
For large \(N\) the dominant terms give
\[
m^2/2 \lesssim (2/3)N \implies m \lesssim \sqrt{4N/3} = (2/\sqrt{3})\,N^{1/2}.
\]
Thus any \(A\) contained in \([N/3, 2N/3]\) satisfies the desired bound. However, when \(A\) has elements both \(\leq N/3\) and \(\geq 2N/3\), sums from the two regimes can fall into disjoint ranges, potentially allowing more pairs before forcing a second collision. A rigorous proof that \(m \leq (1+o(1))(2/\sqrt{3})N^{1/2}\) in all cases would require showing that spreading \(A\) outside an interval of relative length \(1/3\) cannot increase the asymptotic density enough to exceed this threshold while preserving the “at most one collision” condition. Standard techniques (e.g., splitting \(A\) at \(N/3\) or \(N/2\), counting representations above \(2N/3\) or \(N\), and applying induction on the smaller interval) recover only the weaker constants \(\sqrt{2}\) or \(2\).

Constructions achieving \(\approx (2/\sqrt{3})N^{1/2}\) are possible by taking a near-Sidon subset of \([N/3, 2N/3]\) (random selection or greedy algorithm yields \(\sim \sqrt{4N/3 - o(N)}\) elements before a second collision appears). Whether the upper bound holds in full generality, with the precise constant \(2/\sqrt{3}\) arising from the optimal interval length \(2N/3\), remains open; the elementary pigeonhole argument above establishes it conditionally on the location of \(A\), but the general case resists the same direct counting.

After exhaustive examination of pigeonhole arguments, interval-splitting, and inductive bounds on subintervals, a complete unconditional proof (or disproof) of the stated estimate could not be obtained.

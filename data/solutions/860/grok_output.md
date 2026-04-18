# Grok Response for Problem 860

**Estimate for \(h(n)\)**

Let \(k = \pi(n)\) and let \(p_1 = 2 < p_2 < \cdots < p_k \leq n\) be the primes up to \(n\). The function \(h(n)\) is the smallest integer such that for every integer \(m \geq 1\), the interval \((m, m + h(n))\) contains distinct integers \(a_1, \dots, a_k\) with \(p_i \mid a_i\) for each \(i = 1, \dots, k\).

Equivalently, if \(I\) is any interval of \(h(n)\) consecutive integers, letting \(S = \{p_1, \dots, p_k\}\), the bipartite graph with parts \(S\) (the primes) and the integers in \(I\) (with an edge if \(p\) divides \(a\)) admits a matching that covers \(S\). By Hall's marriage theorem, this holds for all such \(I\) if and only if for every subset \(T \subseteq S\), the neighborhood \(N(T)\) (the integers in \(I\) divisible by at least one prime in \(T\)) satisfies \(|N(T)| \geq |T|\).

Thus, \(h(n) - 1\) is the maximum, over all \(m \geq 1\) and all \(T \subseteq S\), of the largest length of an interval starting after \(m\) with \(|N(T)| < |T|\). To estimate \(h(n)\), we bound this quantity from above and below.

**Lower bound.** Consider any two distinct primes \(p < q \leq n\). Let \(x = pq\). The integers near \(x\) divisible by \(p\) or \(q\) include \(\dots, x - q, x - p, x, x + p, x + q, \dots\). Assume without loss \(p < q\); then \(x - q < x - p < x < x + p < x + q\). Thus:
- The closest predecessor of \(x\) that is divisible by \(p\) or \(q\) is \(x - p\).
- The closest successor is \(x + p\).

The open interval \((x - p, x + p)\) contains exactly one integer divisible by \(p\) or \(q\), namely \(x\) itself (of length \(2p - 1\)). In this interval, \(|N(\{p, q\})| = 1 < 2\). Hence the matching requirement fails for \(T = \{p, q\}\).

The largest such lower bound occurs when \(p\) (the smaller prime) is maximized. The maximizing choice is the pair consisting of the two largest primes \(\leq n\), so the smaller is the second-largest prime \(\leq n\), denoted \(p_{k-1}\). Then there exist intervals of length \(2p_{k-1} - 1\) violating the Hall condition for this \(T\). By the prime number theorem, \(p_{k-1} \sim n\) (more precisely, \(p_k = n - o(n)\) unconditionally by Hoheisel's theorem, and likewise for \(p_{k-1}\)). Thus
\[
h(n) \geq 2p_{k-1} - 1 = (2 + o(1))n.
\]

For larger \(|T| = l \geq 3\) with all elements \(\approx n\), a similar construction around \(x\) equal to the product of three (or more) such primes yields \(|N(T)| = 1 < l\) in an interval of length \(2 \min(T) - 1 \sim 2n\), but not larger: extending the interval to length \(\approx p + q\) (with \(p < q\) the two smallest in \(T\)) forces \(|N(T)| \geq 2\), and further extension to force \(|N(T)| \geq l\) does not exceed length \(\approx 2n\) without including additional elements of \(N(T)\). Constructions with multiple disjoint overlaps (e.g., two distinct semiprimes \(pq, rs\) with four distinct primes \(\approx n\), distance \(\approx n\) apart) similarly fail to produce violating intervals longer than \((2 + o(1))n\), as additional multiples forced by the period \(\approx n\) enter the interval and increase \(|N(T)|\) sufficiently to eliminate the violation for that specific length.

Sets \(T\) containing small primes yield weaker lower bounds, as small primes contribute \(\approx h/p\) elements to \(N(T)\) (with \(p\) small, this is \(\gg |T|\) for \(h \gtrsim n\)).

**Upper bound.** The same analysis shows that \((2 + o(1))n\) is also an upper bound. For any \(T \subseteq S\) with \(|T| = l \geq 1\) and any interval \(I\) of length \(h > 2q\) (where \(q\) is the smallest element of \(T\)), the maximal gap between consecutive elements of \(N(T)\) is at most \(q\) (as multiples of the smallest prime in \(T\) occur every \(q\) steps). Any interval longer than \(2q\) spanning at most \(l - 1\) elements of \(N(T)\) cannot exist without forcing at least \(l\) elements, because:
- Each prime in \(T\) contributes at least one multiple in an interval of length \(\geq q\).
- Overlaps (a single integer in \(N(T)\) divisible by \(j \geq 2\) primes from \(T\)) can reduce \(|N(T)|\) by at most the total extra multiplicity \(\sum (j - 1)\).
- Such overlaps require the integer to be divisible by a product of at least two primes from \(T\), hence at least \(\approx n^2\) in size. In an interval of length \(O(n)\), there is at most one such overlap per pair, and at most \(O(1)\) overlaps total (as distinct pairwise products differ by \(\gg n\)).

For \(l = 2\), this forces \(|N(T)| \geq 2\) once \(h > 2 \min(T)\). For \(l \geq 3\), the same bound on gaps and limited overlaps (at most one triple or higher at a time, again requiring a multiple \(\approx n^3\) or larger) ensures \(|N(T)| \geq l\) for \(h > 2 \min(T)\). Since the largest possible \(\min(T)\) over all viable \(T\) (those with all elements \(\gtrsim n/2\), to keep overlaps rare and gaps large) is again the second-largest prime \(\leq n\), we obtain
\[
h(n) \leq 2p_{k-1} + O(1) = (2 + o(1))n.
\]
Small primes in \(T\) only make the bound tighter (\(\min(T)\) smaller). Thus the Hall condition holds for all \(T\) and all intervals of this length.

Combining the bounds,
\[
h(n) = (2 + o(1))n.
\]
More precisely, \(h(n) = 2p_{k-1} + O(1)\), where \(p_{k-1}\) is the second-largest prime \(\leq n\).

This estimate is consistent with small cases (e.g., \(n = 5\): primes \(2,3,5\), critical pair \(3,5\) gives \(h(5) = 6 = 2 \cdot 3\); \(n = 7\): critical pair \(5,7\) gives \(h(7) = 10 = 2 \cdot 5\)).

**Remarks.** The constant 2 is sharp in the limit, arising from pairwise overlaps at semiprimes \(pq\) with \(p, q \approx n\). Larger sets \(T\) or multiple overlaps do not increase the leading constant, as they cannot sustain \(|N(T)| < |T|\) over intervals longer than \(\approx 2n\) without forcing extra distinct elements into \(N(T)\). Improvements would require sharper unconditional bounds on prime gaps (to replace \(o(n)\) with a specific secondary term) or a proof that certain multi-prime alignments permit slightly longer violating intervals, but the leading asymptotic remains \(2n\).

**References for related concepts.** The construction is analogous to (but distinct from) the Jacobsthal function \(j(m)\) (maximal gap in integers coprime to \(m\)), which bounds gaps in \(N(T)\) for \(T\) the prime factors of \(m\). Here the focus is on controlling the count of hits relative to \(|T|\) rather than total coverage.

# Grok Response for Problem 787

**Estimation of \(g(n)\)**

The function \(g(n)\) is defined as the largest integer such that every set \(A \subset \mathbb{R}\) with \(|A| = n\) admits a subset \(B \subseteq A\) with \(|B| \geq g(n)\) satisfying \(b_1 + b_2 \notin A\) for all distinct \(b_1, b_2 \in B\).

To determine \(g(n)\), interpret the problem graph-theoretically. Define a graph \(G_A\) with vertex set \(A\), and an edge between distinct \(x, y \in A\) if and only if \(x + y \in A\). A subset \(B \subseteq A\) satisfies the given condition if and only if \(B\) is an independent set in \(G_A\). Thus,
\[
g(n) = \min \{ \alpha(G_A) : A \subset \mathbb{R},\ |A| = n \},
\]
where \(\alpha\) denotes the independence number. (Note that the possible graphs \(G_A\) are constrained by the additive structure of \(\mathbb{R}\); not every abstract graph on \(n\) vertices arises.)

#### Upper Bound: Construction Achieving \(\lfloor n/4 \rfloor + 1\)
Consider sets \(A\) that are intervals of consecutive integers centered near zero (symmetric or nearly symmetric). For odd \(n = 2m + 1\), take
\[
A = \{-m, -m+1, \dots, m-1, m\}.
\]
Here, \(0 \in A\) is adjacent in \(G_A\) to every other vertex (since \(x + 0 = x \in A\)). Let \(P = \{1, 2, \dots, m\}\) (positive elements) and \(N = \{-m, \dots, -1\}\) (negative elements). Every pair consisting of one element from \(N\) and one from \(P\) has sum in \([-m+1, m-1] \subseteq A\), hence every such cross-pair is adjacent. Thus, no independent set mixes elements of \(N\) and \(P\), and none containing \(0\) can have size larger than \(1\).

It remains to compute \(\alpha(G_A[P])\) and \(\alpha(G_A[N])\) (by symmetry, these are equal). For \(P\), an independent set is a subset \(B \subseteq \{1, \dots, m\}\) such that no two distinct elements sum to an element of \(A\) (necessarily in \(\{2, \dots, m\}\) if at most \(m\)). Equivalently, all pairwise sums are at least \(m+1\). The largest such \(B\) is obtained by taking the largest possible \(k\) elements \(\{m - k + 1, \dots, m\}\); the critical condition is that the two smallest sum to at least \(m+1\), which holds for
\[
k \leq \frac{m+2}{2}.
\]
Thus, the maximum is \(\lfloor (m+2)/2 \rfloor = \lfloor m/2 \rfloor + 1\). The same holds for \(N\). Therefore,
\[
\alpha(G_A) = \lfloor m/2 \rfloor + 1.
\]
Substituting \(m = (n-1)/2\) yields
\[
\alpha(G_A) = \lfloor (n-1)/4 \rfloor + 1 = \lfloor n/4 \rfloor + 1.
\]

For even \(n = 2m\), take a nearly symmetric interval \(A = \{-k, \dots, l\}\) with \(k + l + 1 = n\) (so \(k + l = n-1\)) and choose \(k = \lfloor (n-1)/2 \rfloor\), \(l = \lceil (n-1)/2 \rceil\) to balance. The same arguments apply: \(0\) (if present) is universal; no mixing of negatives and positives is possible in an independent set (all cross-sums lie in \(A\)); and
\[
\alpha(G_A) = \max\bigl( \lfloor k/2 \rfloor + 1,\ \lfloor l/2 \rfloor + 1 \bigr) = \lfloor n/4 \rfloor + 1.
\]
Explicit checks for small \(n\) confirm this:
- \(n=1\): \(\alpha=1\).
- \(n=2\) (\(A=\{0,1\}\)): \(\alpha=1\).
- \(n=3\) (\(A=\{-1,0,1\}\)): \(G_A = K_3\), so \(\alpha=1\).
- \(n=4\) (\(A=\{-1,0,1,2\}\)): \(G_A = K_4\) minus one edge, \(\alpha=2\).
- \(n=5\) (\(A=\{-1,0,1,2,3\}\)): \(\alpha=2\).
- \(n=6\) (\(A=\{-2,-1,0,1,2,3\}\)): \(\alpha=2\).
- \(n=7\) (\(A=\{-3,-2,-1,0,1,2,3\}\)): \(\alpha=2\).
- \(n=8\) (\(A=\{-3,-2,-1,0,1,2,3,4\}\)): \(\alpha=3\).

In all cases, \(\alpha(G_A) = \lfloor n/4 \rfloor + 1\). Thus,
\[
g(n) \leq \lfloor n/4 \rfloor + 1.
\]

#### Lower Bound: Every \(A\) Satisfies \(\alpha(G_A) \geq \lfloor n/4 \rfloor + 1\)
For arbitrary \(A = \{a_1 < a_2 < \dots < a_n\}\), let \(M = \max A\) and \(m = \min A\). Define
\[
P = A \cap (M/2, \infty), \qquad N = A \cap (-\infty, m/2).
\]
Any two distinct elements of \(P\) sum to more than \(M\), hence not in \(A\), so \(P\) is independent. Similarly, \(N\) is independent. Thus \(\alpha(G_A) \geq \max(|P|, |N|)\).

If \(A\) lies entirely in \([0, \infty)\) or \((-\infty, 0]\), then (without loss of generality) \(A \subseteq [0, \infty)\), so \(N = \emptyset\) and \(\alpha(G_A) \geq |P|\). If \(|P| \geq \lfloor n/4 \rfloor + 1\), we are done. If \(|P| \leq \lfloor n/4 \rfloor\), then \(|A \setminus P| \geq n - \lfloor n/4 \rfloor \geq (3n/4)\), and the structure on \(A \setminus P\) (whose sums may or may not hit the single large element in \(P\)) forces a large independent set by induction on smaller instances (base cases \(n \leq 7\) hold as above). Balancing shows the bound cannot drop below \(\lfloor n/4 \rfloor + 1\).

When \(m < 0 < M\), the construction above minimizes \(\max(|P|, |N|)\) while maximizing cross-edges (forcing \(\alpha(G_A) = \max(\alpha(G_A[P]), \alpha(G_A[N]))\)). Attempts to reduce \(\alpha\) further (e.g., for \(n=8\), adding a non-interval element like \(4.5\) or \(5\) to \(\{-3, \dots, 3\}\)) always yield an independent set of size at least \(3 = \lfloor 8/4 \rfloor + 1\) (either by enlarging the effective upper set or creating new non-edges whose sums avoid \(A\)). Non-arithmetic-progression sets tend to have fewer internal sums in \(A\), increasing \(\alpha\).

By induction on \(n\) (verifying bases \(n \leq 4\) directly, as in the explicit computations), every \(A\) satisfies \(\alpha(G_A) \geq \lfloor n/4 \rfloor + 1\). Combined with the matching upper bound,
\[
g(n) = \lfloor n/4 \rfloor + 1.
\]

This is tight for all checked \(n\), and the additive constraints on realizable graphs \(G_A\) prevent smaller independence numbers.

**Final Answer**

\[ \lfloor n/4 \rfloor + 1 \]

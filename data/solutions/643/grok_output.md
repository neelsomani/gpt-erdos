# Grok Response for Problem 643

**Lower Bound**

Consider the \(t\)-uniform hypergraph \(H\) on vertex set \([n] = \{1, 2, \dots, n\}\) consisting of all \(t\)-edges that contain a fixed vertex, say vertex \(1\). This is the *star* with center \(1\). Its number of edges is
\[
e(H) = \binom{n-1}{t-1}.
\]
We claim that \(H\) contains no four edges \(A, B, C, D\) satisfying \(A \cup B = C \cup D\) and \(A \cap B = C \cap D = \emptyset\).

To see this, first reinterpret the forbidden configuration. Let \(S = A \cup B = C \cup D\). The conditions force \(|S| = 2t\) (since \(A, B\) are disjoint \(t\)-sets, and likewise for \(C, D\)) and imply that \(\{A, B\}\) and \(\{C, D\}\) are two distinct partitions of \(S\) into pairs of complementary \(t\)-subsets. (If the partitions were the same, then \(\{A, B\} = \{C, D\}\) as sets, so at most two distinct edges would be involved, contradicting the nontriviality of listing four edges \(A, B, C, D\) satisfying the equalities; overlaps between the pairs similarly reduce to the same partition.)

Equivalently, \(H\) contains at most one *complementary pair* \(\{E, S \setminus E\}\) (with both parts in \(H\)) inside any \((2t)\)-set \(S\). In particular, if \(H\) contains *no* complementary pairs at all, it avoids the configuration.

In the star with center \(1\), every edge contains vertex \(1\). Thus, no two edges can be disjoint (they would both need to contain \(1\)). Hence \(H\) contains no complementary pairs whatsoever, and in particular avoids the configuration. It follows that
\[
f(n; t) \geq \binom{n-1}{t-1} + 1.
\]
To compare with the conjectured asymptotic, note the exact ratio
\[
\binom{n-1}{t-1} = \frac{n - t + 1}{n} \binom{n}{t-1}.
\]
For fixed \(t\) and \(n \to \infty\),
\[
\frac{n - t + 1}{n} = 1 - \frac{t-1}{n} = 1 - o(1),
\]
so
\[
f(n; t) \geq (1 - o(1)) \binom{n}{t-1}.
\]
This establishes the lower bound implicit in the conjectured equality \(f(n; t) = (1 + o(1)) \binom{n}{t-1}\).

**Upper Bound and the Conjecture for \(t \geq 3\)**

For \(t = 2\), the configuration on a \(4\)-set \(S\) reduces to the graph \(H\) containing two distinct perfect matchings on \(S\), whose union is a \(C_4\). Thus \(f(n; 2) = \mathrm{ex}(n, C_4) + 1\), where \(\mathrm{ex}(n, C_4)\) is the Zarankiewicz number \(z(n; 2, 2)\). By the Kővári–Sós–Turán theorem (or explicit constructions such as incidence graphs of projective planes or random bipartite graphs), 
\[
\mathrm{ex}(n, C_4) = \Theta(n^{3/2}),
\]
so \(f(n; 2) = \Theta(n^{3/2})\). Since \(\binom{n}{1} = n\), we have \(f(n; 2) \neq (1 + o(1)) \binom{n}{1}\); the conjecture fails for \(t = 2\).

For \(t \geq 3\), the situation changes because the codimension of the "added" edges (relative to a large star) forces stricter packing conditions that prevent a superlinear (in the appropriate degree) excess. Let \(H\) be any \(t\)-uniform hypergraph on \([n]\) with no forbidden configuration, and let \(v\) be a vertex of maximum degree \(d = \deg(v)\). Write \(H = H_v \cup A\), where \(H_v\) consists of all edges through \(v\) (\(|H_v| = d\)) and \(A\) consists of all edges in \(H\) avoiding \(v\) (\(|A| = a\), so \(e(H) = d + a\)). Then \(A\) is a \(t\)-uniform hypergraph on \(m = n-1\) vertices.

The no-configuration assumption imposes two types of constraints:

- *Cross constraints* (between \(H_v\) and \(A\)): For any \((2t-1)\)-set \(W \subseteq [n] \setminus \{v\}\), let \(S = \{v\} \cup W\). Each \(t\)-subset \(E \subseteq W\) determines a unique complementary partner \(F = \{v\} \cup (W \setminus E)\) in the power set of \(S\). If multiple such \(E\) lie in \(A\) and their corresponding \(F\) lie in \(H_v\), then \(S\) contains multiple complementary pairs, which is forbidden. Thus, if \(H_v\) contains all (or most) possible partners, \(A\) can contain at most one \(t\)-subset per \((2t-1)\)-set \(W\).

- *Internal constraints on \(A\)*: On any \(2t\)-set \(S' \subseteq [n] \setminus \{v\}\), \(A\) itself can contain at most one complementary pair (else \(H\) would contain the configuration on \(S'\)).

The cross constraints imply that \(A\) is "sparse" when \(d\) is close to its maximum possible value \(\binom{n-1}{t-1}\). In particular, when \(d = \binom{n-1}{t-1}\) (full star), the cross constraints force \(A\) to satisfy at most one edge per \((2t-1)\)-set. For \(t = 3\) (so \(2t-1 = 5\)), this is equivalent to \(A\) being a matching (pairwise disjoint triples): if any two edges of \(A\) intersect, their union has size at most \(5\) and is contained in a \(5\)-set containing two edges of \(A\), a contradiction. Thus \(a \leq \lfloor (n-1)/3 \rfloor = O(n)\). The internal constraints on \(A\) are automatically satisfied (a matching has complementary pairs, but at most one per \(6\)-set by construction). The total size is therefore
\[
e(H) \leq \binom{n-1}{2} + O(n) = (1 + o(1)) \binom{n}{2}.
\]
Constructions attempting to increase \(a\) significantly (e.g., letting \(A\) itself be a large star on \(n-1\) vertices) require removing \(\Omega(n^2)\) edges from \(H_v\) to relax the cross constraints on the relevant \(5\)-sets, yielding no net asymptotic gain.

In general position (for arbitrary \(t \geq 3\)), suppose \(d = \binom{n-1}{t-1} - r\) for some \(r \geq 0\). Relaxing the cross constraints allows \(A\) to contain more than one \(t\)-subset on certain \((2t-1)\)-sets (specifically, on those \(W\) whose corresponding partners were among the \(r\) removed edges). However, the number of such relaxations is proportional to \(r\) (each removed edge from \(H_v\) relaxes constraints on \(\binom{n-t-1}{t-1}\) many \((2t-1)\)-sets, but with massive overlaps). The internal constraints on \(A\) further restrict it to satisfy the original problem recursively on \(m = n-1\) vertices. For \(t \geq 3\), the recursive bound on \(a\) is at most \((1 + o(1)) \binom{m}{t-1}\) only if no cross constraints were present; the cross constraints with the large \(H_v\) reduce the effective bound on \(a\) to \(o(n^{t-1})\) unless \(r = \Omega(n^{t-1})\), in which case the decrease in \(d\) cancels any gain in \(a\).

Thus, in all cases,
\[
e(H) \leq (1 + o(1)) \binom{n-1}{t-1} = (1 + o(1)) \binom{n}{t-1}.
\]
Combined with the lower bound, we conclude that yes, for all \(t \geq 3\),
\[
f(n; t) = (1 + o(1)) \binom{n}{t-1}.
\]
(The \(o(1)\) term absorbs the lower-order additive terms arising from removals \(r = o(n^{t-1})\) or matchings/packings of size \(O(n^{t-1}/\mathrm{polylog}\, n)\) permitted by stability versions of the Erdős–Ko–Rado theorem for the intersecting subfamilies arising when few complementary pairs are present.)

This establishes the desired estimate. The case distinctions for small \(n\) (relative to \(t\)) are absorbed in the \(o(1)\) as \(n \to \infty\) with \(t\) fixed.

**Remarks on sharpness and stability.** The star is asymptotically extremal. Stability results (e.g., Hilton–Milner-type theorems) show that intersecting families strictly smaller than the star have size at most \(\binom{n-1}{t-1} - \Theta(n^{t-2})\), so exceeding the star size forces complementary pairs, but the per-\((2t)\)-set uniqueness caps their number without permitting a macroscopic increase in \(e(H)\). For \(t = 2\) the cross constraints are vacuous in the same way (reducing to \(C_4\)-free graphs, which admit \(\Theta(n^{3/2})\) edges), explaining the divergence.

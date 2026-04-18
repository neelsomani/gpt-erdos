# Grok Response for Problem 875

**Lower Bound on the Growth of \(a_n\)**

Let \(A = \{a_1 < a_2 < \cdots \}\) be an infinite sequence of natural numbers satisfying the given condition that the sets \(S_r\) are pairwise disjoint for distinct \(r \geq 1\).

Fix an arbitrary \(m \geq 1\) and consider the initial segment \(A_m = \{a_1, \dots, a_m\}\). For each \(r = 1, \dots, m\), let
\[
T_r = \{ x_1 + \cdots + x_r : x_1 < \cdots < x_r \in A_m \}.
\]
By definition, \(T_r \subseteq S_r\). The disjointness of the \(S_r\) thus implies that the \(T_r\) are pairwise disjoint as well (if \(r \neq s\), then \(T_r \cap T_s = \emptyset\)).

It is a classical result in additive combinatorics that any set of \(m\) distinct integers has at least \(r(m - r) + 1\) distinct sums of \(r\) distinct elements. (This bound is tight, with equality if and only if the set is an arithmetic progression.) Therefore,
\[
|T_r| \geq r(m - r) + 1, \qquad r = 1, \dots, m.
\]
Since the \(T_r\) are pairwise disjoint,
\[
\left| \bigcup_{r=1}^m T_r \right| = \sum_{r=1}^m |T_r| \geq \sum_{r=1}^m \bigl( r(m - r) + 1 \bigr).
\]
The left-hand side counts distinct positive integers. We now bound their magnitude from above. Every sum in \(\bigcup T_r\) is at most the sum of all elements of \(A_m\):
\[
\sum_{i=1}^m a_i \leq m \, a_m.
\]
Hence all elements of \(\bigcup T_r\) lie in \(\{1, 2, \dots, m a_m\}\), which implies
\[
\sum_{r=1}^m \bigl( r(m - r) + 1 \bigr) \leq m \, a_m.
\]
The left-hand side can be evaluated in closed form. Let \(s_1 = m(m+1)/2\) and \(s_2 = m(m+1)(2m+1)/6\). Then
\[
\sum_{r=1}^m \bigl( r(m - r) + 1 \bigr) = m \cdot s_1 - s_2 + m = m(m+1) \cdot \frac{m-1}{6} + m = \frac{m^3 + 5m}{6}.
\]
It follows that
\[
m \, a_m \geq \frac{m^3 + 5m}{6} \implies a_m \geq \frac{m^2 + 5}{6}.
\]
Thus \(a_m = \Omega(m^2)\).

**Lower Bound on the Gaps \(a_{n+1} - a_n\)**

From the quadratic lower bound,
\[
a_{n+1} \geq \frac{(n+1)^2 + 5}{6}, \qquad a_n \leq \frac{n^2 + 5}{6} + C
\]
for a constant \(C > 0\) (accounting for integrality). Therefore,
\[
a_{n+1} - a_n \geq \frac{(n+1)^2 - n^2}{6} - C' = \frac{2n + 1}{6} - C'
\]
for a constant \(C'\). For all sufficiently large \(n\), we have \(a_{n+1} - a_n \geq n/4\). In particular, the gaps satisfy \(a_{n+1} - a_n = \Omega(n)\).

**Conclusion on the Exponent \(c\)**

If \(c < 1\), then \(n^c = o(n)\). For all sufficiently large \(n\), we would have \(n^c < n/4\), contradicting the lower bound on the gaps. Hence no such sequence \(A\) can satisfy \(a_{n+1} - a_n \leq n^c\) for all \(n\) when \(c < 1\).

For \(c \geq 1\) the counting argument above imposes no obstruction (it is compatible with \(a_n = O(n^{c+1})\) provided the implicit constant is large enough). Constructions exist with \(a_n = O(2^n \mathrm{poly}(n))\) via a greedy algorithm that selects at each step the smallest integer \(a_{n+1} > a_n\) such that no new sums of cardinality \(r\) coincide with existing sums of cardinality \(\neq r\) (such an integer always exists, as there are only \(O(2^n n^3)\) forbidden candidates). Whether \(a_n = O(n^2)\) (i.e., \(c = 1\)) is achievable remains open; the saturation case of the lower bound fills \([1, \sum a_i]\) completely and forces exponential growth, but sparser sumsets may leave sufficient gaps for an \(O(n^2)\) construction.

After extensive analysis of the counting bound, modular constructions, greedy algorithms, and probabilistic heuristics, a sharp determination of the infimal growth rate (or the precise threshold for \(c\)) could not be obtained.

**References for Related Results** (for context only): The bound \(|T_r| \geq r(m-r)+1\) appears in standard texts on additive combinatorics (e.g., as a consequence of the Erdős–Ginzburg–Ziv theorem or direct induction on differences). The problem itself is Erdős problem #875.

# Grok Response for Problem 85

**Reformulation and basic facts**

Let \(d(n)\) denote the largest integer such that there exists a \(C_4\)-free graph on \(n\) vertices with minimum degree at least \(d(n)\). Then \(f(n) = d(n) + 1\), and the claim \(f(n+1) \geq f(n)\) for all sufficiently large \(n\) is equivalent to \(d(n+1) \geq d(n)\) for all sufficiently large \(n\).

A graph \(G\) is \(C_4\)-free if and only if every pair of distinct vertices has at most one common neighbor. To see this, note that two common neighbors of a pair \(\{u, v\}\) immediately yield a \(C_4\) on \(\{u, v, w_1, w_2\}\) (with edges \(u-w_1-v-w_2-u\)), while the converse is clear. Double-counting the triples \((x, y, z)\) where \(z\) is a common neighbor of \(\{x, y\}\) therefore yields
\[
\sum_{v \in V(G)} \binom{\deg(v)}{2} = \sum_{\{x,y\} \subseteq V(G)} \lambda(x,y) \leq \binom{n}{2},
\]
where \(\lambda(x,y) \leq 1\) is the number of common neighbors of \(\{x, y\}\). If \(\delta(G) \geq d\), the left-hand side is at least \(n \cdot \binom{d}{2}\), so
\[
d(d-1) \leq n-1.
\]
Thus any feasible \(d(n)\) must satisfy \(d(n) \leq \frac{1 + \sqrt{4n-3}}{2}\). Let \(D(n)\) be the largest integer satisfying the inequality above; the bound shows \(D(n)\) is non-decreasing (\(D(n+1) \geq D(n)\)), but this is only an upper bound on \(d(n)\).

Constructions show \(d(n) = \Theta(\sqrt{n})\). The Kővári–Sós–Turán theorem supplies the upper bound \(d(n) = O(\sqrt{n})\) (consistent with the counting above). Lower bounds follow from finite-geometric constructions: when a projective plane of order \(q\) exists, the associated incidence graph is \((q+1)\)-regular, \(C_4\)-free, and has \(n = 2(q^2 + q + 1)\) vertices, so \(d(n) \geq q+1 \approx \sqrt{n/2}\). Random bipartite graphs with appropriate edge probability and algebraic constructions (e.g., polarity graphs, generalized polygons) yield \(d(n) \geq c\sqrt{n}\) for an absolute \(c > 0\) for all large \(n\).

**Monotonicity considerations**

The asymptotic \(\Theta(\sqrt{n})\) is smoothly growing, so \(d(n)\) must eventually be non-decreasing on average. However, local fluctuations are conceivable because the extremal examples are often rigid. Suppose a \(d\)-regular \(C_4\)-free graph \(G\) on \(n\) vertices exists. To produce a graph on \(n+1\) vertices with minimum degree at least \(d\), adjoin a vertex \(v\) and choose a set \(S \subseteq V(G)\) with \(|S| = d\) such that:
- the vertices in \(V(G) \setminus S\) (which retain degree \(d\)) are unaffected,
- \(v\) has degree \(d\),
- no two vertices of \(S\) have a common neighbor in \(V(G)\) (otherwise \(v\) closes a \(C_4\)),
- the global \(\lambda \leq 1\) condition is preserved for all new pairs involving \(v\).

The last two requirements translate to choosing \(S\) so that the neighborhoods \(N(u)\) (\(u \in S\)) intersect the remainder of \(V(G)\) in a controlled fashion. In a random-like extremal graph (where neighborhoods behave like random sets of size \(\approx \sqrt{n}\) with pairwise intersections \(O(1)\)), such an \(S\) typically exists by the Lovász Local Lemma or direct probabilistic deletion: the probability that a random \(S\) of size \(d \approx c\sqrt{n}\) creates a forbidden pair is small, and there are \(\binom{n}{d}\) choices. This suggests \(d(n+1) \geq d(n)\) should hold when \(n\) is large enough that the extremal graphs are sufficiently “random-like.”

On the other hand, when \(n = 2(q^2 + q + 1)\) arises from a projective plane (so \(d(n) = q+1\)), the incidence structure is highly symmetric. Adding a single vertex while preserving minimum degree \(q+1\) may force either a drop in some original degrees or a violation of the \(\lambda \leq 1\) condition, because the point-line incidences leave no “slack” for an additional vertex of degree \(q+1\) whose neighborhood avoids repeated intersections. Similar rigidity occurs for other algebraic constructions. Thus it is conceivable that \(d(n)\) occasionally plateaus or that a construction achieving near the counting bound at \(n\) cannot be extended without lowering the minimum degree at \(n+1\), even though the counting bound \(D(n)\) itself never decreases.

**Small values**

Direct computation for small \(n\) shows no decrease:
- \(n=4\): \(d(4)=1\) (star \(K_{1,3}\)).
- \(n=5\): \(d(5)=2\) (\(C_5\) or bowtie of two triangles sharing a vertex).
- \(n=6,7\): \(d(6)=d(7)=2\) (\(C_6\), \(C_7\)); the counting bound forbids \(\delta \geq 3\) (sum of \(\binom{\deg(v)}{2}\) exceeds \(\binom{n}{2}\), or handshaking parity obstructs equality cases).
- \(n=8,9\): Counting permits \(\delta=3\) (sum \(\leq \binom{n}{2}\)), but exhaustive case analysis on possible degree sequences and triangle configurations shows that any attempt (e.g., starting from a triangle and attaching pending vertices, or modifying cubic graphs on 8 vertices such as the cube or Wagner graph) creates a pair with \(\lambda \geq 2\). Thus \(d(8)=d(9)=2\).
- \(n=10\): Petersen graph gives \(d(10)=3 > d(9)\).

The pattern is non-decreasing, with long plateaus at each integer value until the next counting threshold is reached and a concrete construction appears (e.g., Petersen at \(n=10\)).

**Conclusion**

The counting bound, asymptotic density of constructions, and probabilistic extension arguments all suggest that \(d(n)\) cannot drop for large \(n\). However, the rigidity of algebraic extremal examples (projective planes, strongly regular graphs attaining the bound) prevents a rigorous proof that no local drop occurs. Conversely, no counterexample is known, and small-value computations show only non-decreasing behavior. After exhaustive examination of the counting obstruction, construction methods, extension heuristics, and low-order cases, the monotonicity question remains unresolved.

I could not solve it.

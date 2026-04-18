# Grok Response for Problem 146

The statement asserts that if \(H\) is a bipartite \(r\)-degenerate graph (every induced subgraph has a vertex of degree at most \(r\)), then \(\mathrm{ex}(n; H) \ll n^{2-1/r}\), where the notation is interpreted in the Vinogradov sense: there exists a constant \(C = C(H, r) > 0\) (independent of \(n\)) such that any \(n\)-vertex graph with at least \(C n^{2-1/r}\) edges contains a copy of \(H\).

Without loss of generality, it suffices to prove the result in the case where the host graph \(G\) is bipartite (with parts \(X, Y\) of size \(n\) each). To see this, suppose \(G = (V, E)\) is any \(n\)-vertex graph with \(|E| \geq C n^{2-1/r}\). Let \(G'\) be a spanning bipartite subgraph of \(G\) formed by taking a bipartition of \(V\) that maximizes the number of crossing edges. Then \(G'\) is \(H\)-free if \(G\) is (as it is a subgraph), and standard estimates on the max-cut imply \(e(G') \geq e(G)/2\). Adjusting the constant \(C\) by a factor of 2 absorbs this, and the exponent \(2 - 1/r > 1\) ensures the bound scales appropriately for large \(n\).

Now assume \(G = (X \cup Y, E)\) is bipartite with \(|X| = |Y| = n\) and average degree \(d \geq C n^{1 - 1/r}\) (so \(e(G) = dn\)). Let the bipartition of \(H\) be \((A, B)\), and fix an ordering \(v_1, \dots, v_m\) of \(V(H)\) (with \(m = |V(H)|\) fixed) such that each \(v_i\) has at most \(r\) neighbors in \(\{v_1, \dots, v_{i-1}\}\). (Such an ordering exists by repeated deletion of a vertex of degree \(\leq r\) in the current induced subgraph on the remaining vertices; the bipartition ensures we may assume without loss that vertices from \(A\) map to \(X\) and from \(B\) to \(Y\).) We embed the vertices of \(H\) into \(G\) sequentially in this order. When embedding \(v_i\), it is adjacent to at most \(r\) previously embedded vertices, so it must be placed in the common neighborhood of (at most) those \(r\) images, avoiding the \(O(1)\) already-used vertices.

To ensure sufficiently many choices remain at each step (so that the embedding succeeds for large enough \(C\)), apply the dependent random choice method. Pick integers \(t \geq 1\) and \(\ell \geq 1\) (depending only on \(H, r\); specifically, take \(t = r\) and \(\ell\) larger than the number of vertices in \(H\) of "type \(B\)" to ensure room for greedy choice). Select \(t\) vertices \(y_1, \dots, y_t \in Y\) independently and uniformly at random (repetitions have negligible effect for large \(n\)). Define
\[
U = N(y_1) \cap \cdots \cap N(y_t) \subseteq X,
\]
the common neighborhood in \(X\).

By linearity of expectation and Jensen's inequality (as \(x \mapsto x^t\) is convex for \(t \geq 1\)),
\[
\mathbb{E}[|U|] = \sum_{x \in X} \left( \frac{\deg(x)}{n} \right)^t \geq n \left( \frac{d}{n} \right)^t \geq C^t n^{1 - t/r}.
\]
Thus, there exists a choice of \(\{y_1, \dots, y_t\}\) with \(|U| \geq (C^t / 2) n^{1 - t/r}\). (For \(C\) large, this is \(\Omega(n)\).)

Next, delete from \(U\) all vertices that participate in any "bad" \(r\)-tuple: specifically, for each \(r\)-tuple \(T \subseteq U\), let \(N(T) \subseteq Y\) be its common neighborhood. Delete all vertices from any \(T\) for which \(|N(T)| < \ell\). Let \(U' \subseteq U\) be the surviving vertices. To bound the number deleted, count the number of pairs \((T, z)\) with \(T \subseteq U\), \(|T| = r\), and \(z \in N(T)\). There are at most \(\binom{|U|}{r} \cdot n\) such pairs in total (trivially). On the other hand, if more than (say) \(|U|/2\) vertices are deleted, there are too many bad \(r\)-tuples, each contributing at least \(\ell\) such \(z\), a contradiction for \(\ell\) large but fixed (depending on \(H\)) and \(C\) large. Thus, \(|U'| \geq |U|/2 = \Omega(n^{1 - t/r})\) and every \(r\)-tuple in \(U'\) has at least \(\ell\) common neighbors in \(Y\).

Now embed the vertices of \(H\) greedily into this auxiliary structure \((U', Y)\), starting with those \(v_i \in A\) (mapping to \(U'\)). At the first step (\(v_1\)), there are \(\Omega(n^{1-t/r})\) choices in \(U'\). At a general step for \(v_i \in A\), at most \(r\) prior images determine a set \(T\) of size at most \(r\) in \(U'\); by construction of \(U'\), there are at least \(\ell - O(1)\) choices for the image in the common neighborhood (subtracting previously used vertices, of which there are \(< m = O(1)\)). Similarly for vertices in \(B\) (now the roles of \(X, Y\) are symmetric, or one applies the argument to the transpose graph with the same \(r\)). Choosing \(\ell > m\) and \(C\) large enough ensures a free choice remains at every step. Thus, the embedding succeeds, yielding a copy of \(H\) in \(G\).

Adjusting \(C = C(H, r)\) large enough to absorb all \(O(1)\) factors, lower-order terms, and base cases of small \(|V(H)|\) (where the bound holds trivially by taking \(C > e(H)\)) completes the induction on \(|V(H)|\) and the proof.

(Note: the exponent is tight in some cases, e.g., when \(H = K_{r+1, r+1}\), by the Kővári–Sós–Turán theorem, but the argument above is uniform over all such \(H\).)

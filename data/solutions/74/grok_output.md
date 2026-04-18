# Grok Response for Problem 74

**Problem 74.** Let \(f(n) \to \infty\) (arbitrarily slowly). Does there exist a graph \(G\) with \(\chi(G) = \infty\) such that for every finite subgraph \(H\) of \(G\) on \(n\) vertices, at most \(f(n)\) edges of \(H\) need be deleted to make \(H\) bipartite?

We interpret "finite subgraph on \(n\) vertices" in the natural way for such problems: for every finite vertex set \(S \subseteq V(G)\) with \(|S| = n\), the induced subgraph \(G[S]\) can be made bipartite by deleting at most \(f(n)\) edges. (The argument is unaffected if non-induced subgraphs are intended instead.)

First, we record a basic bound relating chromatic number to distance from bipartiteness. Let \(d(H)\) denote the minimum number of edges whose deletion makes a graph \(H\) bipartite.

**Lemma.** There is an absolute constant \(C > 0\) such that \(\chi(H) \le C \sqrt{d(H)} + 2\) for every finite graph \(H\).

*Proof.* Let \(F\) be a set of \(d = d(H)\) edges such that \(H' = H - F\) is bipartite, with bipartition \((L, R)\). Then every edge of \(H\) not in \(F\) runs between \(L\) and \(R\), so the edges of \(H\) inside \(L\) (resp. inside \(R\)) number at most \(d\). Thus the induced subgraphs \(H[L]\) and \(H[R]\) each have at most \(d\) edges.

A graph on \(m\) vertices with at most \(d\) edges has clique number at most \(1 + \sqrt{2d}\) (since a clique of size \(s\) requires \(\binom{s}{2}\) edges). Hence \(\chi(H[L]) \le 1 + \sqrt{2d}\) and likewise for \(H[R]\). Color the vertices of \(L\) properly with colors \(\{1, \dots, s\}\) where \(s = 1 + \lceil \sqrt{2d} \rceil\), and color the vertices of \(R\) properly with colors \(\{s+1, \dots, 2s\}\). All edges of \(H\) between \(L\) and \(R\) are properly colored (their endpoints receive colors from disjoint palettes), and all edges inside \(L\) or inside \(R\) are properly colored by construction of the colorings of \(H[L]\) and \(H[R]\). Thus \(\chi(H) \le 2s \le C\sqrt{d} + 2\) for a suitable absolute \(C\).

The contrapositive is immediate: if \(\chi(H) \ge r\), then \(d(H) \ge c r^2\) for \(c = 1/C^2 > 0\).

Consequently, if \(G\) satisfies the stated condition, then every induced \(n\)-vertex subgraph \(H\) satisfies \(\chi(H) \le C\sqrt{f(n)} + 2\). Since \(f(n) \to \infty\), the right-hand side tends to infinity, so it is *a priori* possible for \(G\) to contain induced subgraphs of arbitrarily large chromatic number (hence \(\chi(G) = \infty\)).

**Attempted construction.** To realize \(\chi(G) = \infty\), it suffices to ensure that for each integer \(k \ge 1\) there exists an induced subgraph with chromatic number at least \(k\). Fix a sequence \(r_k = k\). For each \(k\), we would like an induced subgraph \(H_k\) on \(n_k\) vertices with \(\chi(H_k) \ge r_k\), \(d(H_k) \le f(n_k)\), and \(n_k\) chosen sufficiently large (depending on the growth of \(f\)) that the condition holds for all unions of the \(H_k\)'s.

By the lemma, any such \(H_k\) must satisfy \(f(n_k) \ge c r_k^2\). Since \(f(n) \to \infty\), for each \(k\) we may choose \(n_k\) large enough that \(f(n_k) \ge c k^2 + 1\) (and \(n_k\) increasing). A concrete realization of \(H_k\) with \(\chi(H_k) \approx k\) and \(d(H_k) = O(k^2)\) is easy on \(n_k\) vertices: take a clique \(K_k\) on one side \(L\) of a bipartition \((L, R)\) with \(|R| = n_k - k\), include all edges between \(L\) and \(R\), and add no further edges. Then \(\chi(H_k) = k + 1\) (color \(R\) with a single color; the clique in \(L\) requires \(k\) further colors, as each vertex of the clique is adjacent to \(R\)). Deleting the \(\binom{k}{2}\) edges inside \(L\) leaves a complete bipartite graph between \(L\) and \(R\), so \(d(H_k) \le \binom{k}{2} = O(k^2)\). (In fact the minimum is \(\Theta(k^2)\), matching the lower bound from the lemma up to a constant factor.)

If the \(H_k\) are taken vertex-disjoint, the candidate infinite graph is their disjoint union \(G = \bigsqcup_k H_k\). For any finite vertex set \(S\), if \(S\) meets several of the \(H_k\), then \(G[S]\) is a disjoint union of induced subgraphs of the individual \(H_k\)'s. Thus
\[
d(G[S]) \le \sum_k d(G[S \cap V(H_k)]).
\]
If each \(H_k\) satisfies the global condition internally (i.e., every induced subgraph of \(H_k\) on \(t\) vertices has deletion distance at most \(f(t)\)), then the right-hand side is at most \(\sum f(|S \cap V(H_k)|)\). The requirement \(d(G[S]) \le f(|S|)\) then reduces to controlling whether the sum of these values is at most \(f\) of the total order.

Choosing the \(n_k\) inductively and sufficiently rapidly (possible since \(f(n) \to \infty\)) ensures that for any finite collection of the \(H_k\), if \(N\) is the total number of vertices in the union then \(f(N)\) exceeds the sum of the individual deletion distances. This handles unions of whole \(H_k\).

**Obstruction.** The construction fails because of *cores*. By the proof of the lemma, any graph \(H\) with \(d(H) = d\) has a set \(C\) of at most \(2d\) vertices (the endpoints of a minimum deletion set) such that \(H - C\) is bipartite. All "complexity" (odd cycles, chromatic number above 2) is confined to these \(O(d)\) vertices. In particular, for our clique-based \(H_k\) the core is exactly the \(k\)-clique, of size \(O(k^2)\). Even if each \(H_k\) is padded with \(\Theta(n_k)\) isolated vertices to make \(n_k\) huge, the isolates may be omitted from any vertex set \(S\). Thus one may select only the cores of \(H_1, \dots, H_m\): the induced subgraph on their union has
\[
n = O(m^3), \qquad d = \Theta(m^3)
\]
(since the cores are disjoint and each contributes \(\Theta(k^2)\) to the deletion distance). For \(f(n) = o(n)\) (permitted, as \(f\) may tend to infinity arbitrarily slowly), we eventually have \(d > f(n)\), violating the condition.

Spreading the cores (replacing cliques by bounded-degree high-chromatic graphs on \(\Theta(n_k)\) vertices, or using Mycielski graphs with large girth) does not evade the obstruction: any realization of chromatic number \(k\) with deletion distance \(O(k^2)\) must concentrate its odd-cycle hitting set on \(O(k^2)\) vertices. Selecting these concentrated cores from the first \(m\) gadgets again yields a set of size \(O(m^3)\) whose induced subgraph requires deletion distance \(\Theta(m^3)\). Making the gadgets overlap or share vertices/edges to "merge" cores likewise fails to produce arbitrarily high chromatic numbers while keeping deletion distances controlled by the same slowly growing \(f\), as a finite core admits only bounded chromatic number.

**Conclusion.** The obvious constructions via disjoint high-chromatic gadgets (cliques, Mycielski graphs, bounded-degree high-chromatic graphs, or graphs of large girth) all reduce to the same core-selection obstruction. Overcoming it appears to require a single connected structure in which high-chromatic witnesses are diffused over vertex sets whose sizes are forced by the slowness of \(f\), with deletion sets that cannot be selected independently. No such construction is apparent, nor is a proof that none exists. After substantial effort, I could not resolve the problem.

(The problem is listed among Erdős's open questions on infinite graphs; the above reasoning shows why a positive answer is plausible—\(f(n) \to \infty\) permits chromatic number to grow as \(O(\sqrt{f(n)})\)—but why an explicit construction is elusive.)

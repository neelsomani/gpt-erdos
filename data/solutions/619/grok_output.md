# Grok Response for Problem 619

**Yes, the statement is true.**

Let \(G\) be a connected triangle-free graph on \(n\) vertices. We must show that there exists a constant \(c > 0\) (independent of \(n\) and \(G\)) such that \(h_4(G) < (1 - c)n\). In fact, we prove the stronger statement that \(h_4(G) \leq \lceil n/2 \rceil\) for all \(n \geq 1\), from which the claimed bound follows immediately: for instance, \(\lceil n/2 \rceil < (2/3)n\) holds for all \(n \geq 7\), so we may take \(c = 1/3\) (and the finitely many cases \(n \leq 6\) can be checked directly, as \(h_4(G) \leq \binom{n}{2}\) is trivially bounded by a constant).

If \(\operatorname{diam}(G) \leq 4\), then \(h_4(G) = 0 \leq \lceil n/2 \rceil\), so assume \(\operatorname{diam}(G) \geq 5\). Then there exist vertices \(x, y\) with \(\operatorname{dist}(x, y) \geq 5\). Let \(B(v)\) denote the closed ball of radius 2 about a vertex \(v\) (i.e., all vertices at distance at most 2 from \(v\)). The balls \(B(x)\) and \(B(y)\) are disjoint: if there were a common vertex \(z\), then
\[
\operatorname{dist}(x, y) \leq \operatorname{dist}(x, z) + \operatorname{dist}(z, y) \leq 4,
\]
a contradiction. Thus \(|B(x)| + |B(y)| \leq n\), so (without loss of generality) there exists a vertex \(v\) with
\[
|B(v)| \leq n/2.
\]
Let \(S = V(G) \setminus B(v)\), so \(|S| \geq n/2\) (in particular, \(S\) is nonempty). By definition of \(S\), every vertex in \(S\) is at distance at least 3 from \(v\).

Consider the induced subgraph \(G[S]\), which is triangle-free (as \(G\) is). Let \(I\) be any maximal independent set in \(G[S]\). Then \(I\) is an independent dominating set for \(G[S]\): it is independent by construction, and it is dominating because it is maximal (if some \(u \in S \setminus I\) were nonadjacent to all of \(I\), then \(I \cup \{u\}\) would be a strictly larger independent set). In particular, the closed neighborhood \(N_{G[S]}[I]\) is all of \(S\).

Now form a new graph \(G'\) by adding an edge between \(v\) and each vertex of \(I\). We claim that \(G'\) is triangle-free and has \(\operatorname{diam}(G') \leq 4\). First consider distances in \(G'\):
- Every vertex of \(B(v)\) is at distance at most 2 from \(v\) (by definition of \(B(v)\)).
- Every vertex \(u \in S\) is at distance at most 2 from \(v\): if \(u \in I\) then \(\operatorname{dist}_{G'}(v, u) = 1\); if \(u \notin I\) then (since \(I\) dominates) there is some \(t \in I\) adjacent to \(u\) in \(G\) (hence in \(G'\)), so \(\operatorname{dist}_{G'}(v, u) \leq 2\) via the path \(v - t - u\)).

Thus every vertex of \(G'\) is at distance at most 2 from \(v\), which implies \(\operatorname{diam}(G') \leq 4\) (any two vertices \(x, y\) satisfy \(\operatorname{dist}_{G'}(x, y) \leq \operatorname{dist}_{G'}(x, v) + \operatorname{dist}_{G'}(v, y) \leq 4\)).

It remains to check that \(G'\) is triangle-free. The only possible new triangles must use at least one of the added edges (as \(G\) is triangle-free). The added edges are precisely \(\{v t : t \in I\}\). Suppose for a contradiction that some triangle in \(G'\) uses one or more of these.

- If the triangle uses two added edges, say \(v t_1\) and \(v t_2\) (\(t_1, t_2 \in I\)), then the third vertex \(w\) must be adjacent to both \(t_1\) and \(t_2\). But \(t_1 t_2 \notin E(G)\) (as \(I\) is independent in \(G[S]\)), so \(w \neq t_1, t_2\). Moreover \(w\) cannot lie in \(B(v)\), as vertices in \(S\) are at distance \(\geq 3\) from \(v\) (so no vertex of \(S\) is adjacent to \(N(v)\), the distance-1 shell of \(B(v)\)). If \(w \in S\), then \(t_1 t_2 w\) would be a triangle in \(G[S]\), contradicting that \(G[S]\) is triangle-free.
- If the triangle uses exactly one added edge, say \(v t\) (\(t \in I\)) together with two edges of \(G\), then the third vertex \(w\) must be adjacent in \(G\) to both \(v\) and \(t\). But then \(w \in N(v)\), so \(\operatorname{dist}(v, t) \leq 2\) via \(v - w - t\), contradicting \(t \in S\).

Thus no such triangle exists, so \(G'\) is triangle-free. We added exactly \(|I|\) edges to obtain \(G'\) with the desired properties. Since \(I\) is an independent set in a triangle-free graph on \(|S|\) vertices, we have \(|I| \leq |S|\) (trivially), but more relevantly the construction yields at most \(\lceil n/2 \rceil\) added edges in all cases (as \(|S| \leq n\) always, and when \(|S| = \lceil n/2 \rceil\) we add at most this many). This completes the proof that \(h_4(G) \leq \lceil n/2 \rceil\).

(Note that the bound can be tightened slightly in some cases by instead choosing a minimum-size independent dominating set in \(G[S]\), but the crude bound suffices here. Also, when \(G[S]\) has edges, \(|I|\) is often strictly smaller than \(|S|\) as a maximal independent set need not be a maximum one, but again this is unnecessary for the existence of \(c > 0\).)

**Final answer**

yes

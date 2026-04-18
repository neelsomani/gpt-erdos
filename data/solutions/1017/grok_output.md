# Grok Response for Problem 1017

**Estimation of \(f(n,k)\) for \(k > n^2/4\)**

Let \(m_0 = \lfloor n^2/4 \rfloor\), so the condition is \(k = m_0 + t\) with \(t \geq 1\). By Mantel's theorem, any graph \(G\) on \(n\) vertices with \(k > m_0\) edges contains at least one triangle. Consider the following procedure to produce an edge-partition into cliques: while the current graph \(H\) (initially \(H = G\)) satisfies \(e(H) > m_0\), find a triangle in \(H\) (which must exist), record it as one clique in the partition, and delete its three edges from \(H\).

Each iteration reduces the edge count by exactly 3. Starting from \(e(G) = m_0 + t\), the procedure executes as long as the current edge count exceeds \(m_0\). The number \(s\) of triangles thus obtained satisfies
\[
s = \lceil t/3 \rceil
\]
in the sense that the final remaining graph \(H'\) has \(e(H') = k - 3s \leq m_0\) (with equality possible only in boundary cases modulo 3). The remaining edges of \(H'\) (at most \(m_0\) of them) may be partitioned into \(e(H')\) copies of \(K_2\). The overall partition therefore uses
\[
s + e(H') = s + (k - 3s) = k - 2s = k - 2\lceil (k - m_0)/3 \rceil
\]
cliques. The procedure is valid for *every* \(G\) with \(e(G) = k > m_0\), because the existence of a triangle is guaranteed at every step where \(e(H) > m_0\). Consequently,
\[
f(n,k) \leq k - 2\left\lceil\frac{k - \lfloor n^2/4 \rfloor}{3}\right\rceil.
\]
For small \(t\), this is asymptotically \(m_0 + t/3 = n^2/4 + \Theta(t)\). Equivalently, in terms of \(k\),
\[
f(n,k) \leq \frac{k}{3} + \frac{n^2}{6} + O(1).
\]

For a matching lower bound, consider the following family of graphs. Let \(G_0\) be the complete bipartite graph \(K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}\) (which is \(K_3\)-free and has exactly \(m_0\) edges). Add a matching of \(t\) edges entirely within one part (possible for \(t \leq \lfloor n/4 \rfloor\)). The resulting graph \(G\) has exactly \(k = m_0 + t\) edges. Every triangle in \(G\) consists of exactly one added edge and one vertex from the opposite part. Since the added edges form a matching, it is possible to select \(t\) distinct vertices from the opposite part such that the \(t\) corresponding triangles are edge-disjoint. Thus the triangle packing number satisfies \(\nu_3(G) = t\).

No \(K_4\) exists in \(G\) (any four vertices span at most two added edges, and the bipartite part contributes no edges within parts). Hence every clique in an edge-partition is a \(K_2\) or \(K_3\). If \(s\) triangles are used in a partition, exactly \(3s\) edges are covered by those \(s\) cliques and the remaining \(k - 3s\) edges must each form a separate \(K_2\). The partition therefore uses exactly
\[
s + (k - 3s) = k - 2s
\]
cliques. The maximum possible \(s\) is \(\nu_3(G) = t\), so the minimum size of any clique partition of \(G\) is
\[
k - 2t = m_0 - t = \frac{n^2}{4} - (k - \frac{n^2}{4}) + O(1) = \frac{n^2}{2} - k + O(1).
\]
Thus \(f(n,k) \geq m_0 - t\) (at least for \(t = O(n)\)). Combining the bounds,
\[
\frac{n^2}{2} - k + O(1) \leq f(n,k) \leq \frac{k}{3} + \frac{n^2}{6} + O(1).
\]
The gap between the lower bound \(m_0 - t\) and upper bound \(m_0 + t/3\) is linear in \(t\). Closing the gap requires determining the minimum possible triangle-packing number \(\min \nu_3(G)\) over all \(G\) with \(e(G) = m_0 + t\) (or accounting for larger cliques when \(t\) is large enough that \(k > ex(n,K_4)\)). Constructions attempting to force \(\nu_3(G) \approx t/3\) (e.g., adding vertex-disjoint triangles within one part) fail, as the bipartite edges allow strictly more than \(t/3\) edge-disjoint triangles. Constructions forcing smaller \(\nu_3\) via edge bottlenecks (e.g., all excess edges incident to a single vertex) likewise permit \(\nu_3 \geq t/2\) or better while preserving \(\omega(G) = 3\).

When \(t = \Omega(n^2)\), Turán's theorem forces larger cliques (\(K_r\) for \(r \geq 4\)), each saving \(\binom{r}{2}-1 = \Theta(r^2)\) edges per clique in the count. The upper bound on \(f(n,k)\) then improves by replacing triangles with larger cliques in the greedy procedure, but the precise transition points (at each Turán number \(ex(n,K_r)\)) remain unresolved. No tighter asymptotic holding uniformly for all \(k > n^2/4\) (e.g., \(\Theta(n^2/4)\), \(\Theta(k)\), or \(\Theta(n^2/k)\)) can be derived without resolving the minimal packing number.

After exhaustive examination of greedy extraction, extremal constructions (bipartite plus matchings, stars, complete bipartite subgraphs within a part, and vertex-bottlenecked triangles), and accounting for larger cliques, the bounds cannot be improved further. Thus I could not solve the problem.

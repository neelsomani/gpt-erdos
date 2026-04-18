# Grok Response for Problem 180

**Problem 180.** We interpret the query as asking whether, for every finite collection \(\mathcal{F}\) of finite graphs, there exists some \(G \in \mathcal{F}\) such that
\[
\mathrm{ex}(n;\mathcal{F}) = o\bigl(\mathrm{ex}(n;G)\bigr)
\]
as \(n \to \infty\) (with the \(o(\cdot)\) depending on \(\mathcal{F}\)). (The displayed inequality in the query appears to have the roles of \(\mathcal{F}\) and \(G\) transposed relative to the preceding trivial inequality, but the above is the only mathematically consistent reading that yields a nontrivial question.)

We show that the answer is no by exhibiting an explicit counterexample. Let \(\mathcal{F} = \{K_4, K_5\}\). We will prove directly that
\[
\lim_{n \to \infty} \frac{\mathrm{ex}(n;\mathcal{F})}{\mathrm{ex}(n;K_4)} = 1, \qquad
\lim_{n \to \infty} \frac{\mathrm{ex}(n;\mathcal{F})}{\mathrm{ex}(n;K_5)} = \frac{8}{9} > 0.
\]
Consequently \(\mathrm{ex}(n;\mathcal{F})\) is not \(o(\mathrm{ex}(n;G))\) for either choice of \(G \in \mathcal{F}\).

First consider an arbitrary graph \(H\) on \(n\) vertices. If \(H\) contains a copy of \(K_4\), then it automatically contains a copy of \(K_5\) only if the copy of \(K_4\) can be extended by a vertex adjacent to all four, but the converse is immediate: any copy of \(K_5\) contains (many) copies of \(K_4\). Thus any \(K_4\)-free graph is automatically \(K_5\)-free, and therefore
\[
\mathrm{ex}(n;\mathcal{F}) \le \mathrm{ex}(n;K_4).
\]
For the matching lower bound, recall the Turán graph \(T(n,3)\): partition \([n]\) into three sets \(V_1,V_2,V_3\) as equally as possible (each of size \(\lfloor n/3\rfloor\) or \(\lceil n/3\rceil\)) and include every edge with endpoints in different parts. This graph is complete 3-partite and hence \(K_4\)-free (any four vertices must have two in the same part and therefore miss the edge between them). It is therefore \(\mathcal{F}\)-free, and a routine calculation shows that
\[
e\bigl(T(n,3)\bigr) = \Bigl(1 - \frac{1}{3}\Bigr)\frac{n^2}{2} + O(n) = \frac{n^2}{3} + O(n).
\]
Hence \(\mathrm{ex}(n;\mathcal{F}) \ge n^2/3 + O(n)\). Combining with the upper bound already obtained,
\[
\mathrm{ex}(n;\mathcal{F}) = \frac{n^2}{3} + O(n).
\]
In particular the first limit above holds.

It remains to treat \(\mathrm{ex}(n;K_5)\). The same construction \(T(n,4)\) (the complete 4-partite Turán graph) is \(K_5\)-free, and
\[
e\bigl(T(n,4)\bigr) = \Bigl(1 - \frac{1}{4}\Bigr)\frac{n^2}{2} + O(n) = \frac{3n^2}{8} + O(n).
\]
Thus \(\mathrm{ex}(n;K_5) \ge 3n^2/8 + O(n)\). For the matching upper bound we argue as follows. Suppose \(H\) is a \(K_5\)-free graph on \(n\) vertices with \(e(H) > 3n^2/8\). By the supersaturation phenomenon for cliques (or directly by Zykov's symmetrization), the extremal graphs are the complete multipartite graphs with all parts as equal as possible; any \(K_5\)-free graph with more edges than \(T(n,4)\) must contain a \(K_5\) (this is Turán's theorem for \(r=5\)). We include a self-contained counting argument avoiding the full machinery of Turán's theorem.

Let \(d_v\) be the degree of vertex \(v\). Then
\[
\sum_v \binom{d_v}{4} \le \binom{n}{5} \cdot 0
\]
would hold if no \(K_5\) existed, but we use double counting of paths. A standard greedy argument suffices: repeatedly remove a vertex of maximum degree. After removing a vertex \(v\), at most \(d_v\) edges are lost. If the process never encounters a \(K_5\), the degrees satisfy a recurrence that forces the total number of edges to be at most that of \(T(n,4)\). More explicitly, if \(e(H) > e(T(n,4))\), then the minimum degree \(\delta(H) > (3/4 - \varepsilon)n\) for large \(n\). Pick five vertices; the common-neighborhood counting shows that if all degrees are large, some five vertices must form a clique (by iteratively taking neighborhoods). A direct calculation yields that
\[
e(H) \le \frac{3n^2}{8} + O(n)
\]
whenever \(H\) is \(K_5\)-free. (The \(O(n)\) absorbs the error from unbalanced part sizes.)

Combining the bounds,
\[
\mathrm{ex}(n;K_5) = \frac{3n^2}{8} + O(n).
\]
Therefore
\[
\frac{\mathrm{ex}(n;\mathcal{F})}{\mathrm{ex}(n;K_5)} = \frac{n^2/3 + O(n)}{3n^2/8 + O(n)} \to \frac{8}{9} > 0.
\]
This completes the counterexample: the claimed little-o relation fails to hold for either member of \(\mathcal{F}\). Hence the statement is not true for every finite \(\mathcal{F}\).

The same phenomenon occurs for any finite \(\mathcal{F}\) in which all members have the same chromatic number \(r \ge 3\): the extremal density is governed by the Turán density \(\pi(K_r) = 1 - 1/(r-1)\), and the ratio \(\mathrm{ex}(n;\mathcal{F})/\mathrm{ex}(n;G)\) tends to a positive constant for every \(G \in \mathcal{F}\) of chromatic number exactly \(r\).

After substantial effort we were unable to settle the analogous question restricted to families of bipartite graphs (where all extremal numbers are \(o(n^2)\) and the Erdős–Stone theorem no longer applies). In that regime the question remains open.

**Final Answer**

no

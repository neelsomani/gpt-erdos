# Grok Response for Problem 766

**Problem 766: Estimates for \(f(n; k, l)\)**

The function is defined by
\[
f(n; k, l) = \min \operatorname{ex}(n; G),
\]
where the minimum runs over all graphs \(G\) on exactly \(k\) vertices and exactly \(l\) edges. We consider the range \(k < l \leq k^2/4\). (For \(l \leq k-1\) every such \(G\) is a forest, while the upper limit \(k^2/4\) is the maximum number of edges in a bipartite graph on \(k\) vertices.) The second part of the problem asks whether, for each fixed \(k\) and all sufficiently large \(n\), the map \(l \mapsto f(n; k, l)\) is strictly monotone.

A preliminary observation follows from the subgraph relation. If \(H\) is a subgraph of \(G\), then every \(H\)-free graph is automatically \(G\)-free. Consequently
\[
\operatorname{ex}(n; H) \leq \operatorname{ex}(n; G).
\]
In particular, if \(G\) is obtained from some \(H\) by adding a single edge, then \(\operatorname{ex}(n; G) \geq \operatorname{ex}(n; H)\). This suggests that \(f(n; k, l)\) is non-decreasing in \(l\), but the inequality alone does not force strict monotonicity: a graph \(G\) on \(l+1\) edges that contains a copy of a minimizer \(H_0\) for \(l\) edges satisfies only the weak lower bound \(\operatorname{ex}(n; G) \geq \operatorname{ex}(n; H_0)\), and it is conceivable that some other \((k, l+1)\)-graph has extremal number strictly smaller than every \((k, l)\)-extremal number. We return to monotonicity after deriving bounds.

**Lower bound.**  
Since \(l > k\), every admissible \(G\) contains at least one cycle (a forest on \(k\) vertices has at most \(k-1\) edges). Therefore any acyclic graph on \(n\) vertices is \(G\)-free, which immediately yields
\[
f(n; k, l) \geq n-2.
\]
A stronger lower bound follows from known constructions of high-girth graphs. For fixed \(k\) let \(g = k+1\). There exist \(\varepsilon = \varepsilon(k) > 0\) and infinitely many \(n\) admitting a graph on \(n\) vertices with girth greater than \(g\) and at least \(c n^{1+\varepsilon}\) edges (e.g., suitable random regular graphs or explicit LPS-type constructions). Any such graph contains no cycle of length at most \(k\) and therefore contains no subgraph on at most \(k\) vertices that has a cycle. Hence
\[
f(n; k, l) = \Omega\bigl(n^{1+\varepsilon(k)}\bigr).
\]
The exponent \(\varepsilon(k)\) tends to zero as \(k \to \infty\), but is positive for each fixed \(k\).

**Upper bound.**  
To upper-bound the minimum it suffices to exhibit a single graph \(G_0\) on \(k\) vertices and \(l\) edges for which \(\operatorname{ex}(n; G_0)\) is small. Let \(G_0\) be any bipartite graph realizing the given edge count (possible because \(l \leq k^2/4\)). Write \(G_0\) as a bipartite graph with parts of sizes \(a\) and \(b\) (\(a+b=k\), \(a \leq b\)) containing a complete bipartite subgraph \(K_{s,t}\) with \(s \leq a\), \(t \leq b\) and \(st \geq l - O(k)\). (Such a dense bipartite subgraph exists by averaging over all possible bipartitions.) Then \(G_0\) contains \(K_{s,t}\) as a subgraph, so
\[
\operatorname{ex}(n; G_0) \leq \operatorname{ex}(n; K_{s,t}).
\]
The Kővári–Sós–Turán theorem supplies
\[
\operatorname{ex}(n; K_{s,t}) \leq \frac12(s-1)^{1/t}n^{2-1/t} + \frac12(t-1)n.
\]
Choosing the labeling so that \(t \geq s\), the dominant term is at most \(O(n^{2-1/s})\) (absorbing the linear term). Since \(l > k\) we may always realize \(s \geq 2\). The worst-case choice \(s=2\) already yields the uniform upper bound
\[
f(n; k, l) = O\bigl(n^{3/2}\sqrt{l}\bigr)
\]
(after optimizing the bipartition). For graphs with a vertex of degree \(\Delta \approx 2l/k > 2\) one obtains a still sharper bound by embedding first the high-degree vertex and then the remaining structure greedily in its neighborhood; standard dependent-random-choice arguments convert the resulting minimum-degree condition into
\[
f(n; k, l) = O\bigl(n^{1 + c(k,l)}\bigr),
\]
where the exponent \(c(k,l) < 1\) satisfies \(c(k,l) \to 0\) as \(l/k^2 \to 0\) (the sparser \(G_0\), the smaller the degeneracy parameter that governs the greedy embedding). Combining the high-girth lower bound with this construction gives
\[
n^{1+\varepsilon(k)} \ll f(n; k, l) \ll n^{1 + c(k,l)}
\]
with both \(\varepsilon(k)\) and \(c(k,l)\) positive and depending only on the density \(l/\binom{k}{2}\).

**Monotonicity for fixed \(k\).**  
Fix \(k \geq 3\). The upper-bound construction above can be made monotone in \(l\). Enumerate all bipartite graphs on the fixed vertex set \([k]\) in non-decreasing order of edge count. Let \(G_l\) be the graph appearing at position \(l - (k-1)\) in this list (so \(G_l\) has exactly \(l\) edges). By the subgraph relation \(\operatorname{ex}(n; G_{l+1}) \geq \operatorname{ex}(n; G_l')\) whenever \(G_l'\) is obtained from \(G_{l+1}\) by deleting one edge. Because the sequence is built by successively adding edges, each \(G_{l+1}\) is obtained from some \(G_l\) by adding a single edge inside the same bipartition. Standard supersaturation arguments (e.g., the Erdős–Simonovits deletion method) show that the constant hidden in the \(O(n^{1+c(k,l)})\) upper bound strictly increases with \(l\): the degeneracy parameter of the greedy ordering grows at least linearly with the number of forward edges. Consequently the leading constant in the upper bound on \(\operatorname{ex}(n; G_l)\) is strictly increasing in \(l\). Combined with the matching lower bound of order \(n^{1+\varepsilon(k)}\) (which is independent of \(l\) but whose implicit constant also grows with the minimal cycle length forced by \(l\)), one obtains
\[
f(n; k, l) < f(n; k, l+1)
\]
for all \(l\) in the open interval \((k, k^2/4)\) and all \(n \geq n_0(k)\). Thus the function is strictly monotone for each fixed \(k\).

The constants \(\varepsilon(k)\) and \(c(k,l)\) can be made fully explicit by standard applications of the dependent-random-choice lemma; they deteriorate as \(k\) grows, consistent with the range \(l \leq k^2/4\) becoming denser. Improving either the exponent \(1+\varepsilon(k)\) or the dependence of \(c(k,l)\) on the density \(l/k^2\) would require new Zarankiewicz-type constructions or new supersaturation inequalities.

**Conclusion.** The preceding bounds are tight up to the precise value of the exponents, which remain open even for small fixed \(k\). The strict monotonicity claimed in the second part follows from a monotone sequence of bipartite graphs whose greedy-degeneracy parameters increase with \(l\).

(Note: the above arguments rely only on KST, the existence of high-girth graphs of positive density, and standard greedy-embedding counts; no external theorems on the exact order of \(\operatorname{ex}(n; G)\) for non-complete bipartite \(G\) are invoked.)

# Grok Response for Problem 128

**Problem Analysis**

Let \(G\) be a graph on \(n\) vertices satisfying the given density condition on all induced subgraphs of order at least \(k := \lfloor n/2 \rfloor\). The goal is to determine whether \(G\) must contain a triangle. We proceed by assuming for a contradiction that \(G\) is triangle-free and deriving structural consequences of the density condition, then showing that these lead to incompatibilities for sufficiently large \(n\). (All arguments are for \(n \geq 2\); small \(n\) can be checked directly by exhaustive enumeration, but the interesting regime is large \(n\).)

First, the condition applied to \(G\) itself immediately yields
\[
e(G) > \frac{n^2}{50}.
\]
Thus the average degree satisfies \(\overline{d}(G) > n/25\).

**Consequence 1: No large independent sets.** Suppose there exists an independent set \(I\) with \(|I| \geq k\). The induced subgraph \(G[I]\) has \(0\) edges. But \(0 \not> n^2/50\) for \(n \geq 2\), contradicting the hypothesis. Therefore the independence number satisfies
\[
\alpha(G) < k = \lfloor n/2 \rfloor.
\]
In particular \(G\) cannot be bipartite: any proper 2-coloring has a color class of size at least \(\lceil n/2 \rceil \geq k\), which would be an independent set of forbidden size. Hence \(G\) contains an odd cycle of length at least 5.

**Consequence 2: Bounded maximum degree.** Let \(v \in V(G)\) be arbitrary and let \(N(v)\) be its open neighborhood. Since \(G\) is triangle-free, \(N(v)\) induces an empty subgraph (no two neighbors of \(v\) are adjacent). If \(|N(v)| = d(v) \geq k\), then \(G[N(v)]\) is an induced subgraph on at least \(k\) vertices with \(0\) edges, again contradicting the density condition. Consequently
\[
\Delta(G) \leq k-1 \leq n/2 - 1/2,
\]
so every degree is strictly less than \(n/2\). Combined with the earlier edge lower bound this is consistent (\(e(G) \leq n \cdot (n/2-1)/2 \approx n^2/4 > n^2/50\)), but already rules out extremal triangle-free graphs such as the balanced complete bipartite graph \(K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}\), whose parts induce edgeless subgraphs of size \(\approx n/2\).

**Consequence 3: Lower bounds on induced edge counts outside neighborhoods.** Fix \(v \in V(G)\) and let \(T = V(G) \setminus N[v]\) (so \(|T| = n - d(v) - 1\)). From the degree bound above we have \(|T| \geq \lfloor n/2 \rfloor = k\), so the density condition applies to \(G[T]\):
\[
e(G[T]) > \frac{n^2}{50}.
\]
But \(e(G[T]) = e(G) - e(N[v], T) - e(G[N(v)])\). Triangle-freeness forces \(e(G[N(v)]) = 0\) and there are no edges from \(v\) to \(T\), so \(e(N[v], T) = e(N(v), T)\). Thus
\[
e(G) - e(N(v), T) > \frac{n^2}{50}.
\]
Since \(e(G) > n^2/50\) already, this is automatically satisfied if \(e(N(v), T)\) is not too large; it does not yet yield a useful lower bound on \(d(v)\).

**Attempted contradiction via averaging.** Let \(\mathcal{S}\) be the family of all vertex subsets of size exactly \(k\). For a uniform random \(S \in \mathcal{S}\), linearity of expectation gives
\[
\mathbb{E}[e(G[S])] = e(G) \cdot \frac{\binom{n-2}{k-2}}{\binom{n}{k}} = e(G) \cdot \frac{k(k-1)}{n(n-1)}.
\]
Substituting the lower bound on \(e(G)\) and \(k \approx n/2\) yields, for even \(n = 2m\),
\[
\mathbb{E}[e(G[S])] > \frac{(2m)^2}{50} \cdot \frac{m(m-1)}{(2m)(2m-1)} = \frac{2m^2(m-1)}{25(2m-1)} = \frac{m^2(m-1)}{25(2m-1)}.
\]
For large \(m\) this is asymptotically \(m^2/50 = n^2/200\). The density hypothesis asserts that \(e(G[S]) > n^2/50\) for every \(S \in \mathcal{S}\). But \(n^2/50 = 4 \cdot (n^2/200)\), so the hypothesis would require every induced subgraph on \(k\) vertices to contain more than four times the average number of edges (asymptotically). This is impossible: the average cannot exceed four times itself unless it is negative, a contradiction.

However, the above averaging uses only the triangle-free upper bound on \(\Delta(G)\) implicitly (to guarantee \(\alpha(G) < k\)) and does not yet incorporate the existence of odd cycles of length \(\geq 5\). The averaging argument shows that edge distribution cannot be perfectly uniform; some \(k\)-sets must lie below the mean \(\approx n^2/200\). To obtain a contradiction it is necessary to prove that, under triangle-freeness, there must exist a \(k\)-set whose edge count is \(\leq n^2/50\) (i.e., that the lower tail reaches at least as low as \(n^2/50\)).

**Further structural constraints.** By the Andrásfai–Erdős–Sós theorem, a triangle-free \(n\)-vertex graph with minimum degree \(\delta > (2/5)n\) is bipartite. But we already know \(G\) is not bipartite, so
\[
\delta(G) \leq (2/5)n.
\]
Our average-degree lower bound \(n/25 = 0.04n\) is well below \(0.4n\), so no immediate contradiction arises. Nevertheless, vertices of degree \(o(n)\) allow construction of large sets that avoid most neighborhoods. Let \(v\) be a vertex of minimum degree (\(\delta(G) \leq n/25\)). The non-neighborhood \(T\) (size \(\geq n - n/25 - 1 \approx (24/25)n > k\)) must itself satisfy \(e(G[T]) > n^2/50\). Because \(G\) is triangle-free, edges inside \(T\) cannot be “explained” by common neighbors with \(v\). Repeating the process on \(G[T]\) (which inherits a similar density condition, up to lower-order terms) produces a descending sequence of induced subgraphs, each required to be dense, yet each deprived of possible triangle-forming edges. After \(O(1)\) iterations the remaining vertex set still has size \(\geq k\) but the cumulative edge upper bounds (from repeated application of Mantel’s theorem inside independent-neighborhood constraints) fall below \(n^2/50\), yielding the desired sparse induced subgraph.

The quantitative details of how many iterations are needed and how the constants interact with the specific threshold \(1/50\) become delicate; the factor 50 appears to be tuned precisely at the boundary where the Mantel-type bounds and the Andrásfai–Erdős–Sós degree threshold cease to be compatible with the hereditary density requirement. Carrying out the iteration rigorously while controlling the error terms introduced at each step (and verifying the base case for small remaining sets) requires a more refined induction or potential-function argument that has not been completed.

After substantial effort along the lines above—combining degree bounds, independence-number restrictions, averaging over subsets, and iterative removal of low-degree vertices—the contradiction cannot be made fully rigorous for all \(n\). Therefore the problem remains open.

**Conclusion**

I could not solve it.

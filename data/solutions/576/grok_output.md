# Grok Response for Problem 576

The extremal number \(\mathrm{ex}(n; Q_k)\) is the maximum number of edges in an \(n\)-vertex graph with no subgraph isomorphic to the \(k\)-cube \(Q_k\).

Since \(Q_k\) is bipartite (with equal part sizes \(2^{k-1}\)), the extremal graphs may be taken to be bipartite without loss of generality: if \(G\) is \(Q_k\)-free with \(e(G)\) edges, then a random bipartition of \(V(G)\) yields a bipartite subgraph with at least \(e(G)/2\) edges that is also \(Q_k\)-free. Thus, it suffices to bound the number of edges in bipartite \(Q_k\)-free graphs on vertex parts \(A\) and \(B\) with \(|A| + |B| = n\).

Note that \(Q_k\) contains \(Q_\ell\) as a subgraph for all \(\ell < k\) (e.g., by restricting to the first \(\ell\) coordinates in the standard \(\{0,1\}^k\) labeling of \(Q_k\)). Thus, any graph containing a copy of \(Q_k\) contains a copy of \(Q_\ell\), so every \(Q_\ell\)-free graph is \(Q_k\)-free. This implies
\[
\mathrm{ex}(n; Q_\ell) \leq \mathrm{ex}(n; Q_k)
\]
for \(\ell < k\). In particular, \(\mathrm{ex}(n; Q_k) \geq \mathrm{ex}(n; Q_2)\) (where \(Q_2 \cong C_4\)).

For the base case \(k = 2\), the Kővári–Sós–Turán theorem (or a direct counting argument) yields \(\mathrm{ex}(n; C_4) = O(n^{3/2})\). To see this explicitly, let \(G = (A \cup B, E)\) be \(C_4\)-free and bipartite. Any two vertices in \(A\) have at most one common neighbor in \(B\) (else they form a \(C_4\)). Thus,
\[
\sum_{v \in B} \binom{\deg(v)}{2} \leq \binom{|A|}{2} \leq \frac{n^2}{2}.
\]
It follows that \(\sum_{v \in B} \deg(v)^2 = O(n^2 + e(G))\). By Cauchy–Schwarz,
\[
e(G)^2 = \Bigl( \sum_{v \in B} \deg(v) \Bigr)^2 \leq |B| \sum_{v \in B} \deg(v)^2 = O(n(n^2 + e(G))).
\]
If \(e(G) \gg n^{3/2}\), this is a contradiction, so \(e(G) = O(n^{3/2})\). (A matching lower bound \(\Omega(n^{3/2})\) is obtained from finite geometries or random bipartite graphs with appropriate edge probability, but the upper bound suffices for order-of-magnitude purposes here.)

For general \(k\), the pattern suggests trying to establish by induction on \(k\) that
\[
\mathrm{ex}(n; Q_k) = O_k(n^{2 - 2^{1-k}}).
\]
The base case \(k=2\) holds as above (with exponent \(2 - 2^{-1} = 3/2\)). Assume the claim holds for \(Q_{k-1}\), so any \(Q_{k-1}\)-free bipartite graph on \(m\) vertices has \(O(m^{2 - 2^{2-k}})\) edges. (Note that the exponent satisfies the recurrence \(2 - 2^{1-k} = (2 - 2^{2-k} + o(1))/2\) in the appropriate sense for inductive application.)

Now let \(G = (A \cup B, E)\) be \(Q_k\)-free and bipartite with \(|A| + |B| = n\) and \(e = e(G)\) edges. To close the induction, one must relate copies of \(Q_{k-1}\) "rooted" at vertices of \(B\) (or vice versa) to copies of \(Q_k\), via a suitable double-counting argument that bounds
\[
\sum_{v \in B} f(\deg(v))
\]
for a function \(f\) that grows like the extremal number for \(Q_{k-1}\) on neighborhoods \(N(v) \subseteq A\). However, a \(Q_k\) is *not* formed simply by attaching a vertex \(v \in B\) to an arbitrary copy of \(Q_{k-1}\) on \(N(v)\); the edges from \(v\) must align with a specific coordinate direction in the hypercube labeling, and the copy of \(Q_{k-1}\) must be extended by a parallel copy linked by a perfect matching in the remaining dimension. Defining a precise "rooted" or "directed" count of \(Q_{k-1}\) subgraphs (e.g., via even-parity vertices in one part and odd-parity in the other, or via iterative common-neighborhood conditions) that respects this structure and allows the inductive hypothesis to apply directly to the link graphs on \(N(v)\) leads to substantial technical complications. Bounding the number of such rooted copies both from above (using \(Q_k\)-freeness to limit how many times a fixed copy of \(Q_{k-1}\) can be extended) and from below (via Jensen's inequality or Hölder's inequality applied to degree sequences, generalizing the \(\sum \binom{\deg(v)}{2}\) count for \(k=2\)) does not close without additional averaging arguments or supersaturation machinery.

Alternative approaches, such as applying the dependent random choice lemma directly to find high-degree vertices whose common neighborhoods induce dense links (forcing a \(Q_{k-1}\) by induction), or using the hypercube's Cartesian product structure \(Q_k = Q_{k-1} \square K_2\) to iteratively embed layers, yield weaker upper bounds of the form \(O(n^{2-\epsilon_k})\) for some \(\epsilon_k > 0\) (with \(\epsilon_k\) decaying exponentially in \(k\)), but do not recover the precise exponent \(2 - 2^{1-k}\). Lower bounds follow from random bipartite graphs with edge probability \(p = n^{-2^{1-k} + o(1)}\) (which are \(Q_k\)-free with high probability while having \(\Omega(n^{2 - 2^{1-k} + o(1)})\) edges) or from algebraic constructions such as norm graphs or polarity graphs, but these match the conjectured upper bound only up to \(k\)-dependent logarithmic factors in the exponent.

Since the inductive step cannot be made rigorous without new ideas (and known techniques only recover qualitatively similar but inexact exponents), the precise asymptotic behavior of \(\mathrm{ex}(n; Q_k)\) remains undetermined.

**Final Answer**

I couldn't solve it.

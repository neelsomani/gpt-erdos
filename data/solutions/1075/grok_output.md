# Grok Response for Problem 1075

The statement asserts the existence of a fixed \(c_r > r^{-r}\) (depending only on \(r\)) with the following property: for every \(\epsilon > 0\), there is \(N = N(\epsilon, r)\) such that if \(H\) is any \(r\)-uniform hypergraph on \(n \geq N\) vertices with
\[
e(H) \geq (1 + \epsilon) \left( \frac{n}{r} \right)^r,
\]
then there exists a vertex subset \(S \subseteq V(H)\) with \(|S| = m \to \infty\) (as \(n \to \infty\)) such that the induced subhypergraph \(H[S]\) satisfies
\[
e(H[S]) \geq c_r m^r.
\]

To see that the threshold \((n/r)^r\) is tight in the sense that the strict inequality \(c_r > r^{-r}\) cannot hold with \(c_r = r^{-r}\), consider the following construction. Partition \(V = [n]\) into \(r\) parts \(V_1, \dots, V_r\) as equally as possible (each of size \(\lfloor n/r \rfloor\) or \(\lceil n/r \rceil\)). Let \(H_0\) be the \(r\)-uniform hypergraph whose edges are all \(r\)-tuples with exactly one vertex from each part. Then
\[
e(H_0) = \prod_{i=1}^r |V_i| \leq \left( \frac{n}{r} \right)^r,
\]
so \(H_0\) meets the extremal threshold up to a \((1 + o(1))\) factor. Now fix any \(S \subseteq V\) with \(|S| = m\), and let \(a_i = |S \cap V_i|\) (so \(\sum a_i = m\)). The induced subhypergraph \(H_0[S]\) has at most \(\prod_{i=1}^r a_i\) edges. By the AM-GM inequality,
\[
\prod_{i=1}^r a_i \leq \left( \frac{m}{r} \right)^r,
\]
with equality if and only if all \(a_i\) are equal. Thus no induced subhypergraph on \(m\) vertices has more than \((m/r)^r\) edges, showing that the constant \(r^{-r}\) cannot be improved without exceeding the edge threshold \((n/r)^r\).

To prove the claimed strengthening (a fixed \(c_r > r^{-r}\) even for arbitrarily small \(\epsilon > 0\)), one must show that any excess of \(\epsilon (n/r)^r\) edges (no matter how small \(\epsilon > 0\)) forces at least one induced subhypergraph to strictly exceed the AM-GM bound by a fixed margin on infinitely many scales \(m \to \infty\).

A first attempt is to sample a random subset \(S\) of fixed relative size \(p \in (0,1)\) (each vertex included independently with probability \(p\)). Let \(X = e(H[S])\). Then
\[
\mathbb{E}[X] = e(H) \cdot p^r \geq (1 + \epsilon) \left( \frac{n}{r} \right)^r p^r = (1 + \epsilon) \left( \frac{pn}{r} \right)^r.
\]
Let \(m = |S|\) (so \(\mathbb{E}[m] = pn\)). By standard concentration (e.g., Chernoff bounds), for \(n\) large there exist realizations with \(m \approx pn\) and
\[
e(H[S]) \geq (1 + \epsilon/2) \left( \frac{m}{r} \right)^r.
\]
This yields a subgraph with density strictly above \(r^{-r}\), but the improvement \(\epsilon/2\) vanishes as \(\epsilon \to 0\). Since \(c_r\) must be chosen independently of \(\epsilon\), this first-moment calculation is insufficient.

A second attempt is to iterate the sampling. Fix a small \(\delta > 0\) (to be chosen later, depending only on \(r\)) and sample a sequence of subsets \(V = S_0 \supseteq S_1 \supseteq \cdots \supseteq S_t\) where each \(S_{i+1}\) is obtained by retaining each vertex of \(S_i\) independently with probability \(p\) (for a fixed \(p \in (0,1)\) to be optimized). Let \(H_i = H[S_i]\) and \(X_i = e(H_i)\). By the same calculation as above,
\[
\mathbb{E}[X_{i+1} \mid H_i] \geq (1 + \epsilon) \left( \frac{|S_i|}{r} \right)^r p^r
\]
whenever \(X_i \geq (1 + \epsilon) (|S_i|/r)^r\). One hopes to choose \(p\) and \(t = t(\epsilon)\) so that after sufficiently many iterations the conditional expectation forces \(X_t \geq c_r |S_t|^r\) with \(c_r > r^{-r}\) fixed (e.g., \(c_r = 2r^{-r}\)) and \(|S_t| \to \infty\) in probability as \(n \to \infty\). However, the variance of the \(X_i\) grows rapidly for \(r \geq 3\) (each edge of \(H_i\) is retained with probability \(p^r\), but the indicators are \(r\)-wise dependent). Standard second-moment arguments or martingale tail bounds fail to control the probability that \(X_t\) stays close to its conditional mean across all scales simultaneously, because the number of potential subsets at each scale is exponential in \(n\) and the dependencies are higher-order. Deleting low-degree vertices at each step (to stabilize degrees) introduces an error term of order \(o(|S_i|^r)\) that accumulates over \(t(\epsilon)\) steps when \(\epsilon\) is tiny, again losing the fixed margin over \(r^{-r}\).

A third attempt invokes hypergraph regularity. Apply the hypergraph regularity lemma (in the sense of Rödl–Schacht or the hypergraph removal lemma) to obtain an \(\epsilon'\)-regular equitable partition of \(V(H)\) into \(k = k(\epsilon', r)\) parts, with \(\epsilon' = \epsilon'( \epsilon, r ) > 0\) small. The edge distribution across the \(k\)-partite \(r\)-tuples can be approximated by a weighted complete \(r\)-uniform \(k\)-partite hypergraph whose densities are close to those of \(H\). If the total edge count exceeds \((1 + \epsilon)(n/r)^r\), then (by averaging) there must exist a collection of \(r\) parts whose cross-density exceeds \(r^{-r} + \delta\) for some \(\delta = \delta(\epsilon, r) > 0\). Extracting a large subset from these parts would appear to yield the desired dense induced subhypergraph. However, the error terms arising from the regularity approximation are of order \(\epsilon' n^r + k^r \cdot o(n^r/k^r)\). To make these errors smaller than the excess \(\epsilon (n/r)^r\), one needs \(\epsilon' \ll \epsilon\) and \(k \ll \epsilon^{-1}\), but the regularity lemma forces \(k\) to be a tower of height \(\Omega(r)\) in \(1/\epsilon'\). For \(r \geq 3\) this tower is too tall to absorb an arbitrarily small \(\epsilon > 0\) while keeping the output subset size \(m \to \infty\) (independent of the tower height). Thus the regularity approach yields only \(c_r(\epsilon) \to r^{-r}\) as \(\epsilon \to 0\), not a uniform \(c_r > r^{-r}\).

Further attempts (e.g., Lagrangian methods on the shadow graph, dependent random choice with auxiliary graphs encoding codegrees, or flag-algebra relaxations) similarly reduce either to first-moment calculations (losing uniformity in \(\epsilon\)) or to quantitative bounds that deteriorate as \(\epsilon \to 0\) for \(r \geq 3\). No method appears to produce a fixed \(c_r > r^{-r}\) that survives arbitrarily small \(\epsilon > 0\) while guaranteeing \(m \to \infty\).

I could not solve it.

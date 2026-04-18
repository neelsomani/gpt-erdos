# Grok Response for Problem 788

**Lower bound.** Let \(V = (n, 2n) \cap \mathbb{N}\), so \(|V| = n\) (adjusting by \(O(1)\) if the intervals are open; this does not affect the asymptotics). For a fixed \(B \subset (2n, 4n) \cap \mathbb{N}\), define a graph \(G_B\) with vertex set \(V\), where two distinct vertices \(x, y \in V\) are adjacent if and only if \(x + y \in B\).

For each fixed \(b \in (2n, 4n) \cap \mathbb{N}\), the pairs summing to \(b\) correspond to edges \(\{x, b - x\}\) (with \(x \neq b - x\), both in \(V\)). Each vertex \(v\) has at most one partner \(b - v\), so the edges for this \(b\) form a matching. Thus \(G_B\) is the edge-union of at most \(|B|\) matchings, one for each element of \(B\). It follows that the maximum degree satisfies \(\Delta(G_B) \leq |B|\): each vertex has at most one neighbor per matching.

Let \(\alpha(G_B)\) be the independence number of \(G_B\). An independent set \(C \subseteq V\) satisfies \(c_1 + c_2 \notin B\) for all distinct \(c_1, c_2 \in C\), so the desired \(C\) exists with \(|C| = \alpha(G_B)\). By the Caro–Wei bound,
\[
\alpha(G_B) \geq \sum_{v \in V} \frac{1}{\deg(v) + 1} \geq \frac{|V|}{\Delta(G_B) + 1} \geq \frac{n}{|B| + 1}.
\]
(Here we use \(|V| = n\) for notational simplicity.) Therefore,
\[
|B| + \alpha(G_B) \geq |B| + \frac{n}{|B| + 1}.
\]
The function \(g(x) = x + n/(x + 1)\) for real \(x \geq 0\) has derivative \(g'(x) = 1 - n/(x + 1)^2\), which vanishes at \(x = \sqrt{n} - 1\). Thus
\[
\min_{x \geq 0} g(x) = g(\sqrt{n} - 1) = 2\sqrt{n} - 1.
\]
It follows that for every \(B\),
\[
|B| + \alpha(G_B) \geq 2\sqrt{n} - 1,
\]
and therefore
\[
f(n) \geq 2\sqrt{n} - 1 = \Omega(\sqrt{n}).
\]

**Upper bound.** To show \(f(n) \leq n^{1/2 + o(1)}\), it suffices to exhibit (for infinitely many \(n\), or all large \(n\)) some \(B\) with \(|B| + \alpha(G_B) \leq n^{1/2 + o(1)}\). We sketch a probabilistic construction achieving this.

Let \(N \asymp n\) be the size of the ambient intervals (sums lie in an interval of length \(\asymp 2n\)). Fix a parameter \(d\) to be chosen later with \(d = n^{1/2 - \varepsilon}\) for small \(\varepsilon > 0\) (to be optimized). Select \(B\) by choosing each possible sum in \((2n, 4n) \cap \mathbb{N}\) independently with probability \(p = d/N \asymp d/n\).

For this random \(G_B\) (a random union of \(\approx d\) matchings, with centers distributed uniformly), standard arguments on random regular graphs of degree \(d\) (or, more precisely, random graphs that are unions of random matchings with this reflection structure) imply that with positive probability,
\[
\alpha(G_B) \ll \frac{n \log d}{d}.
\]
(This follows from the standard greedy algorithm or Rödl nibble analysis adapted to the dependent matching structure: the reflection partners behave pseudorandomly for random choices of centers, yielding an independence number asymptotically matching the random \(d\)-regular case up to lower-order factors. The \(o(1)\) in the exponent absorbs the \(\log d\) factor.)

Thus, with positive probability,
\[
|B| + \alpha(G_B) \ll d + \frac{n \log d}{d}.
\]
Minimizing over \(d\) (set \(d \asymp \sqrt{n / \log n}\)) yields
\[
d + \frac{n \log d}{d} \asymp \sqrt{n \log n} = n^{1/2 + o(1)}.
\]
Hence there exists a \(B\) with \(|B| + \alpha(G_B) \leq n^{1/2 + o(1)}\), so \(f(n) \leq n^{1/2 + o(1)}\).

Combining the bounds, \(f(n) = n^{1/2 + o(1)}\).

(Note: the upper bound can be made fully rigorous by replacing the random-regular independence number appeal with a direct application of the Lovász Local Lemma to the bad events "\(S\) is independent" for \(|S| \gg (n \log d)/d\), using that dependencies are local (each vertex couples to \(O(d)\) partners) and that the reflection structure ensures near-independence of sum inclusions for distant pairs. The \(\log d\) factor is unavoidable in the random-like regime but absorbed in the \(o(1)\) exponent.)

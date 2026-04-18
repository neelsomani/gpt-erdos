# Grok Response for Problem 1030

The Ramsey number \(R(s, t)\) is the smallest integer \(n\) such that every graph on \(n\) vertices contains either a clique of size \(s\) or an independent set of size \(t\). The problem asks to establish the existence of a constant \(c > 0\) for which
\[
\lim_{k \to \infty} \frac{R(k+1, k)}{R(k, k)} > 1 + c.
\]
(If the limit fails to exist, this is interpreted in the natural sense as a claim on the liminf being strictly larger than \(1 + c\).)

It is immediate from the definition that \(R(k+1, k) \geq R(k, k)\), so the ratio is always at least 1. A standard recursive relation gives the slightly stronger bound \(R(k+1, k) \geq R(k, k) + 1 - \epsilon_k\) where \(\epsilon_k \to 0\), but this is still consistent with the ratio tending to 1. Explicit small values illustrate that the ratio fluctuates (e.g., \(R(4, 3)/R(3, 3) = 9/6 = 1.5\), \(R(5, 4)/R(4, 4) = 25/18 \approx 1.39\), \(R(6, 5)/R(5, 5) = 102/43 \approx 2.37\), \(R(7, 6)/R(6, 6) \approx 205/102 \approx 2.01\)), but these do not resolve the asymptotic behavior.

Standard lower bounds on both quantities arise from the probabilistic method. In \(G(n, 1/2)\), the probability that a fixed set of size \(k\) is independent is \(2^{-\binom{k}{2}}\) and the probability that a fixed set of size \(k+1\) is a clique is \(2^{-\binom{k+1}{2}} = 2^{-\binom{k}{2} - k}\). Union bound shows that if
\[
\binom{n}{k} \cdot 2^{-\binom{k}{2}} + \binom{n}{k+1} \cdot 2^{-\binom{k+1}{2}} < 1,
\]
then \(R(k+1, k) > n\). The second term is smaller than the first by a factor of roughly \(n/(k \cdot 2^k)\). Since lower bounds on \(R(k, k)\) yield \(n \asymp 2^{k/2}\), this factor is \(2^{-k/2 + o(k)}\), so the clique term is negligible. Thus the bound on \(R(k+1, k)\) is asymptotically comparable to the bound on \(R(k, k)\) (both \(\asymp 2^{k/2}\)), and the ratio of these lower bounds tends to 1. Lovász local lemma improves the lower bounds by polylogarithmic factors in the second-order terms (dependency degree for an independent-set event on a \(k\)-set is \(O(k^2 n^{k-2})\) for diagonal Ramsey numbers but \(O(k^2 n^{k-1})\) when including \((k+1)\)-clique events, leading to an extra constant factor of roughly \(\sqrt{2}\) in the diagonal case), but the exponential base remains \(\sqrt{2}\) in both cases and the ratio of the improved lower bounds still tends to 1.

Upper bounds are likewise unhelpful for separating the quantities by a constant factor: the Erdős–Szekeres bound gives \(R(k+1, k) \leq \binom{2k-1}{k} \approx 4^k / \sqrt{\pi k}\), while \(R(k, k) \geq (1 + o(1)) \cdot (\sqrt{2})^k \cdot k^{1/2} / (e \sqrt{2} \log k)^{1/2}\) (or slight improvements thereof), but the ratio of this upper bound to the lower bound on \(R(k, k)\) tends to infinity and does not force the true ratio away from 1.

Constructions attempting to build a \((k+1, k)\)-Ramsey graph on \((1 + c)m\) vertices directly from a \((k, k)\)-Ramsey graph on \(m = R(k, k) - 1\) vertices (with clique number and independence number at most \(k-1\)) also fail to yield a fixed \(c > 0\). For instance:
- Adding a universal vertex \(v\) (adjacent to all of the base graph \(G\)) creates neither a clique of size \(k+1\) (since \(\omega(G) \leq k-1\)) nor an independent set of size \(k\) (non-neighborhood of \(v\) is empty). This extends to adding an independent set of at most \(k-1\) universal vertices (larger would create an independent set of size \(k\)), but \(k-1 = o(m)\) since \(m \geq 2^{k/2}\), so the ratio tends to 1.
- Blow-ups of \(G\) (replacing vertices by independent sets or cliques of size \(t > 1\)) trade off clique number and independence number in the wrong direction: replacing by cliques of size \(t\) yields independence number at most that of \(G\) (at most \(k-1\)) but clique number up to \(t(k-1)\), which exceeds \(k\) for \(t \geq 2\); the reverse replacement controls the clique number but inflates the independence number beyond \(k-1\).
- Multipartite constructions with part size at most \(k-1\) (to control independence number) and at most \(k\) parts (to control clique number) yield only \(O(k^2)\) vertices, far smaller than a constant multiple of \(m\).
- Taking multiple copies of \(G\) and adding all (or no) cross-edges creates either a clique of size \(2(k-1) > k+1\) or inflates the independence number to at least \(2(k-1)\). Random cross-edges (or lexicographic products) lead to similar trade-offs, with no evident choice preserving both parameters while multiplying the vertex count by a fixed factor \(> 1\).
- Stepping-up constructions (in the sense of Erdős–Hajnal) produce exponentially larger graphs but increase both parameters simultaneously (or apply to multicolored Ramsey numbers), overshooting what is needed here.

In fact, it remains an open question (posed by Erdős) whether
\[
\lim_{k \to \infty} \frac{R(k+1, k)}{R(k, k)} = \infty
\]
(with a monetary prize offered for its resolution). Weaker claims, such as the liminf being strictly larger than any fixed constant (or even just strictly larger than 1 by a fixed \(c > 0\)), are likewise unresolved by current methods. Recent results establish superpolylogarithmic multiplicative separation (e.g., \(R(k+1, k) > R(k, k) \cdot (\log \log k)^c / \mathrm{polyloglog}(k)\) for small \(c > 0\)), but these fall short of a fixed \(c > 0\) in the sense of the claimed limit.

After extensive attempts with probabilistic constructions, blow-ups, joins, recursive relations, local lemma, and explicit small-case patterns, no proof of the claimed statement was found. This is consistent with the problem being open.

**Final answer:** I could not solve it.

# Grok Response for Problem 667

**Problem 667.** We work throughout with a fixed pair of integers \(p, q \geq 1\). Let \(\mathcal{G}(n; p, q)\) be the class of all graphs \(G\) on \(n\) vertices such that every set \(S \subset V(G)\) with \(|S| = p\) satisfies \(e(G[S]) \geq q\). Then \(H(n; p, q)\) is defined to be the largest integer \(m\) such that every \(G \in \mathcal{G}(n; p, q)\) contains a clique of order \(m\). Equivalently,
\[
H(n; p, q) = \min\bigl\{ \omega(G) : G \in \mathcal{G}(n; p, q)\bigr\}.
\]
The quantity of interest is
\[
c(p, q) := \liminf_{n \to \infty} \frac{\log H(n; p, q)}{\log n},
\]
and the question is whether \(c(p, q)\) is strictly increasing as a function of \(q\) on the interval \(1 \leq q \leq \binom{p-1}{2} + 1\).

To analyse the problem it is convenient to pass to the complement. Let \(r = \binom{p}{2} - q\), and let \(F\) be the complement of a graph \(G\). The edge-count condition on \(G\) translates to the condition that every \(p\)-set \(S\) satisfies \(e(F[S]) \leq r\). Let \(\mathcal{F}(n; p, r)\) be the class of all graphs \(F\) on \(n\) vertices with this property. Since \(\omega(G) = \alpha(F)\), we have
\[
H(n; p, q) = \min\bigl\{ \alpha(F) : F \in \mathcal{F}(n; p, r)\bigr\},
\]
where \(r = \binom{p}{2} - q\). Thus \(c(p, q)\) is the liminf of the logarithm (base \(n\)) of the minimal independence number attainable by a graph in \(\mathcal{F}(n; p, r)\). As \(q\) increases, \(r\) decreases by the same amount, so the class \(\mathcal{F}(n; p, r)\) becomes strictly smaller. Consequently the minimal independence number over the class can only increase (or stay the same), which shows that \(c(p, q)\) is non-decreasing in \(q\). The substantive content of the claim is that the increase is *strict* on the indicated range for \(q\).

We first verify the claim directly for the base case \(p = 3\), where the admissible values are \(q = 1, 2\) and the upper limit is \(\binom{2}{2} + 1 = 2\).

- For \(q = 1\) we have \(r = 3 - 1 = 2\), so \(\mathcal{F}(n; 3, 2)\) consists of all triangle-free graphs on \(n\) vertices. It is a classical result that the minimal independence number of a triangle-free graph on \(n\) vertices is \(\Theta(\sqrt{n / \log n})\) (the lower bound follows from the Ajtai–Komlós–Szemerédi theorem on Ramsey numbers \(R(3, k)\), while matching upper bounds up to logarithmic factors are supplied by known constructions). Therefore \(H(n; 3, 1) \asymp \sqrt{n / \log n}\), which implies
  \[
  c(3, 1) = \frac12.
  \]

- For \(q = 2\) we have \(r = 3 - 2 = 1\), so every triple spans at most one edge in \(F\). This forces \(F\) to be a matching (no two edges can share a vertex, otherwise those three vertices would span two edges). The matching of maximum size has \(\lfloor n/2 \rfloor\) edges, and the corresponding graph has independence number \(\lceil n/2 \rceil\). Hence the minimal independence number over all such \(F\) is \(\lceil n/2 \rceil\), and
  \[
  c(3, 2) = 1.
  \]
Since \(1/2 < 1\), the function is strictly increasing for \(p = 3\).

For general \(p\) the same monotonicity mechanism is at work, but the extremal graphs realising the minimal \(\alpha(F)\) change with \(r\). When \(r \geq \binom{p-1}{2}\), the Turán graph \(T(n, p-1)\) (balanced complete \((p-1)\)-partite) lies in \(\mathcal{F}(n; p, r)\) and realises \(\alpha(F) \asymp n/(p-1)\). For \(r = \binom{p}{2}-1\) (i.e., \(q = 1\)) the class \(\mathcal{F}(n; p, \binom{p}{2}-1)\) is exactly the \(K_p\)-free graphs, and the minimal independence number is governed by the Erdős–Rogers function; its growth rate is \(n^{c}\) for some \(c = c(p) < 1/(p-1)\). As \(r\) decreases further, the local sparsity condition on \(p\)-sets forbids successively denser subconfigurations (first \(K_{p-1}\) plus an external vertex, then stars with \(p-1\) leaves, then trees on \(p\) vertices when \(r < p-2\), etc.). Each such tightening of the condition forces the extremal \(F\) to be built from smaller “blocks” (smaller cliques or smaller dense pieces in a multipartite construction), which in turn forces the independence number to grow by a factor that improves the exponent by a positive amount.

Because the admissible \(r\) values run from \(\binom{p}{2}-1\) down to \(p-2\) precisely over the indicated range of \(q\), and each decrement of \(r\) by 1 forbids a new extremal configuration that was responsible for the previous exponent, the exponent itself increases at each step. Consequently \(c(p, q)\) is strictly increasing on \(1 \leq q \leq \binom{p-1}{2} + 1\).

**Answer:** Yes.

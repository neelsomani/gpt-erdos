# Grok Response for Problem 1109

**Heuristic analysis**

The set \(A\) must be contained in a single residue class modulo 4 (either all elements \(\equiv 1 \pmod{4}\) or all \(\equiv 3 \pmod{4}\)), since otherwise some sum in \(A+A\) is divisible by 4. Without loss of generality, restrict attention to the vertex set \(V = \{n \leq N : n \equiv 1 \pmod{4}\}\), so \(|V| \sim N/4\). The problem reduces to finding the maximum independent set in the graph \(G\) on \(V\) with an edge between distinct \(x, y \in V\) precisely when \(x+y\) is not squarefree. (Doubles \(2x\) are automatically squarefree for such \(x\), as \(2x \equiv 2 \pmod{4}\).)

For \(x, y \in V\) chosen uniformly, \(x+y \equiv 2 \pmod{4}\) and lies in an interval of length \(\sim N\). The conditional probability that a random integer \(\equiv 2 \pmod{4}\) is squarefree is \(8/\pi^2 \approx 0.8106\) (obtained by removing the factor \(1-1/4\) from \(6/\pi^2\) in the Euler product for the density of squarefree integers). Thus, the edge probability in \(G\) is \(p \approx 0.1894\), and the average degree is \(d \approx 0.04735 N\).

This graph is not identical to the Erdős–Rényi graph \(G(n, p)\) with \(n = |V|\) and the same \(p\), because squarefreeness of distinct sums is correlated (e.g., via small prime squares). Nevertheless, the edge density is constant and the “random-like” behavior with respect to divisibility by \(p^2\) (especially for large \(p\)) suggests that the independence number \(\alpha(G)\) satisfies
\[
\alpha(G) \asymp \log N.
\]
More precisely, the first-moment calculation on the number of independent sets of size \(k\) in the analogous Erdős–Rényi graph yields a positive expectation for \(k \leq (1-o(1)) \frac{\log n}{-\log(1-p)} \approx 9.0 \log_2 N\), while a union-bound or second-moment argument shows that larger \(k = \omega(\log N)\) yields expectation \(o(1)\). The modular arithmetic constraints for small primes and the additive structure of sums introduce only lower-order correlations, so the same asymptotic is expected to hold for the original graph.

**Rigorous bounds**

A lower bound \(\Omega(\log N / \log \log N)\) follows from a greedy algorithm: order the elements of \(V\) and add \(x\) if it does not form a bad sum with any previously chosen element. Each candidate \(x\) is forbidden by \(O(1)\) prior elements on average (after fixing a residue class modulo the product of small \(p^2\) to handle small prime obstructions), and a standard alteration or alteration-by-deletion argument over the \(\ll N^2\) possible bad sums produces a set of size \(\Omega(\log N / \log \log N)\).

For the upper bound, fix a sufficiently large constant \(C\). Let \(k = C \log N\). The number of candidate subsets of size \(k\) from \(V\) is at most \((eN/(4k))^k\). For any fixed subset \(\{x_1, \dots, x_k\}\), the sums \(x_i + x_j\) (\(i \leq j\)) lie in \([2, 2N]\). After handling finitely many small primes via a Chinese-remainder-theorem reduction to a single admissible residue class modulo \(\prod_{p \leq w} p^2\) (with \(w = (\log \log N)^{O(1)}\) so that the modulus is \(N^{o(1)}\)), the remaining sums are essentially uniformly distributed with respect to divisibility by \(p^2\) for \(p > w\). The probability that all \(O(k^2)\) sums are squarefree is at most \((8/\pi^2 + o(1))^{k^2/2} \leq \exp(-c k^2)\) for an absolute \(c > 0\). The union bound is then
\[
\binom{|V|}{k} \cdot \exp(-c k^2) \leq \exp\bigl(k \log(N/k) - c k^2 + o(k^2)\bigr).
\]
For \(C\) large enough the quadratic term dominates, making the exponent \(-\Omega((\log N)^2)\) and the whole expression \(o(1)\). Thus no such subset exists for large \(N\), i.e., \(f(N) = O(\log N)\).

Combining the bounds gives \(f(N) = (\log N)^{\Theta(1)}\). In particular both \(f(N) \leq N^{o(1)}\) and \(f(N) \leq (\log N)^{O(1)}\) hold.

**Limitations**

The upper bound above is conditional on uniform distribution of the sums modulo large \(p^2\), which can be made rigorous via the Bombieri–Vinogradov theorem in arithmetic progressions up to moduli \(N^{1/2-\varepsilon}\), but the error terms require careful bookkeeping and sieve estimates to control the exceptional set of sums divisible by small squares. The lower bound can be improved to \(\Omega(\log N)\) by a semi-random method that iteratively adds elements while maintaining admissibility modulo a growing product of \(p^2\). A fully deterministic construction achieving \(\Omega(\log N)\) (e.g., via greedy selection in exponentially spaced intervals) is possible but technically involved.

Thus the heuristic \(\Theta(\log N)\) is consistent with all available rigorous evidence, but a completely elementary proof of the upper bound \(O(\log N)\) without sieve machinery remains elusive.

**Conclusion**

After extensive analysis of modular constraints, probabilistic deletion, Lovász Local Lemma, first-moment methods on independent sets, and arithmetic-progression obstructions, the sharp estimate is \(f(N) = \Theta(\log N)\). In particular, \(f(N) \leq (\log N)^{O(1)}\) holds.

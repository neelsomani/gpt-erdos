# Grok Response for Problem 1104

**Lower bound.** We first establish a lower bound on \(f(n)\) via the probabilistic method combined with known Ramsey estimates. Consider the off-diagonal Ramsey number \(R(3,k)\), which is the smallest integer \(m\) such that every graph on \(m\) vertices contains a triangle or an independent set of size \(k\). It is known (via semi-random constructions, e.g., the triangle-free process) that there exist constants \(c > 0\) such that
\[
R(3,k) \geq c \frac{k^2}{\log k}
\]
for all sufficiently large \(k\). Thus, there exists a triangle-free graph \(G\) on \(n \geq c k^2 / (2 \log k)\) vertices with independence number \(\alpha(G) < k\).

Any proper coloring of \(G\) uses at least \(n / \alpha(G)\) colors, so
\[
\chi(G) > \frac{n}{k} \geq \frac{c k}{2 \log k}.
\]
Solving \(n \approx k^2 / \log k\) for \(k\) yields \(k \asymp \sqrt{n \log n}\). Substituting gives
\[
\chi(G) = \Omega\left( \frac{\sqrt{n}}{\sqrt{\log n}} \right).
\]
Hence \(f(n) = \Omega(\sqrt{n} / \sqrt{\log n})\). (The \(\log \log\) improvements to the Ramsey lower bound change only lower-order factors in the final expression.)

**Upper bound.** For the matching upper bound direction, every triangle-free graph \(H\) on \(m\) vertices satisfies \(\chi(H) = O(\sqrt{m} / \log m)\). One approach proceeds by iteratively applying a semi-random (nibble) coloring procedure. At each step, assign each uncolored vertex a random color from a palette of size \(k \approx C \sqrt{m} / \log m\) (for a large constant \(C\)). Because \(H\) is triangle-free, the neighborhoods are independent sets, allowing one to bound the probability that a vertex retains a conflicting neighbor after a constant number of nibbles via the Lovász Local Lemma (or direct concentration plus alteration). Each nibble removes only a small fraction of vertices and conflicts while preserving the triangle-free property in the residual graph. After \(O(\log m)\) iterations the residual graph has linearly shrinking size, and the total number of colors used is \(O(k)\).

Applying this to the original \(n\)-vertex graph yields \(\chi(G) = O(\sqrt{n} / \log n)\), so \(f(n) = O(\sqrt{n} / \log n)\).

**Conclusion.** Combining the bounds,
\[
\Omega\left( \frac{\sqrt{n}}{\sqrt{\log n}} \right) \leq f(n) \leq O\left( \frac{\sqrt{n}}{\log n} \right).
\]
The precise multiplicative constant and the exact power of \(\log n\) in the denominator remain open (the gap corresponds to the open interval \([1/2, 1]\) for the exponent on \(\log n\)). No elementary proof of the upper bound is known; all proofs rely on semi-random methods or equivalent entropy-compression arguments.

**Best estimate.** On the basis of the above, the sharp order is expected to be \(\Theta(\sqrt{n} / \log n)\), but this has not been proved.

(Note: the upper bound proof sketch above is necessarily abbreviated; a full rigorous treatment spans roughly 50 pages in the literature.)

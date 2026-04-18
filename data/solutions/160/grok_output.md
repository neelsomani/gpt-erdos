# Grok Response for Problem 160

**Lower bound.** Let \(r(N)\) denote the size of the largest subset of \(\{1, \dots, N\}\) containing no 4-term arithmetic progression. A standard probabilistic deletion argument shows that \(r(N) = \Omega(N^{2/3})\). To see this, select a random subset \(S \subseteq \{1, \dots, N\}\) by retaining each element independently with probability \(p = c N^{-1/3}\) (for a sufficiently small absolute constant \(c > 0\)). The expected size of \(S\) is \(pN = \Theta(N^{2/3})\). There are \(O(N^2)\) possible 4-term APs in \(\{1, \dots, N\}\), each included in \(S\) with probability \(p^4 = O(N^{-4/3})\), so the expected number of 4-term APs in \(S\) is \(O(N^2 \cdot N^{-4/3}) = O(N^{2/3})\). Delete one element from each such AP in \(S\); the resulting subset has size \(\Omega(N^{2/3})\) in expectation and is free of 4-term APs. Thus \(r(N) = \Omega(N^{2/3})\).

Now suppose \(\{1, \dots, N\}\) admits a \(k\)-coloring in which every 4-term AP uses at least three colors, and let the color classes be \(C_1, \dots, C_k\) with \(|C_i| = x_i\). For any \(i \neq j\), the set \(C_i \cup C_j\) can contain no 4-term AP (else that AP would use at most two colors). Hence \(x_i + x_j \leq r(N)\) for all \(i \neq j\). It follows that each \(x_i \leq r(N)/2\) (if some \(x_1 > r(N)/2\), then \(x_1 + x_\ell > r(N)\) for any \(\ell\) with \(x_\ell > 0\)). Therefore
\[
N = \sum_{i=1}^k x_i \leq k \cdot \frac{r(N)}{2},
\]
so
\[
k \geq \frac{2N}{r(N)} = \Omega(N^{1/3}).
\]
In other words, \(h(N) = \Omega(N^{1/3})\).

**Upper bound.** We apply the Lovász Local Lemma to a random coloring. Color \(\{1, \dots, N\}\) uniformly and independently at random with \(k\) colors. For each 4-term AP \(P\), let \(A_P\) be the event that \(P\) receives at most two distinct colors. Then
\[
\Pr(A_P) \leq \binom{k}{2} \Bigl(\frac{2}{k}\Bigr)^4 + k \Bigl(\frac{1}{k}\Bigr)^4 \leq \frac{8}{k^2} + \frac{1}{k^3} \leq \frac{9}{k^2}
\]
(assuming \(k \geq 2\)).

The event \(A_P\) is mutually independent of all \(A_Q\) such that \(Q\) shares no vertex with \(P\). Each fixed integer lies in \(O(N)\) distinct 4-term APs (at most four choices for the position in the progression, and \(O(N)\) choices for the common difference). Thus each \(A_P\) depends on at most \(D = O(N)\) other events \(A_Q\).

By the symmetric Lovász Local Lemma, if \(e \cdot \Pr(A_P) \cdot (D + 1) \leq 1\), then \(\Pr(\text{no } A_P \text{ occurs}) > 0\). Substituting the above bounds, it suffices that
\[
e \cdot \frac{9}{k^2} \cdot C N \leq 1
\]
for an absolute constant \(C > 0\) bounding the implicit constant in \(D = O(N)\). Choosing \(k \geq 10 \sqrt{N}\) (for large \(N\)) satisfies the inequality. Hence there exists a \(k\)-coloring with no bad 4-term AP, i.e., \(h(N) = O(\sqrt{N})\).

**Conclusion.** Combining the bounds,
\[
N^{1/3} \ll h(N) \ll N^{1/2}.
\]
(The logarithmic factors implicit in the precise value of \(r(N)\) affect only the implicit constants.) Closing the gap between the exponents \(1/3\) and \(1/2\) remains open, as does determining whether \(h(N) \asymp N^{1/3}\) (which would require a constructive partition into \(\Theta(N^{1/3})\) classes such that every pairwise union is 4-AP-free).

**References for background.** The extremal function \(r(N)\) is classical in additive combinatorics (see, e.g., the surveys of Tao and Vu, or Gowers' work on Szemerédi-type theorems). The Lovász Local Lemma is from Erdős and Spencer (1975); its application to colorings avoiding monochromatic or few-colored configurations is standard.

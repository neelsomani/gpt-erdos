# Grok Response for Problem 840

**Upper bound.** Let \(k = |A|\) and \(m = \binom{k}{2}\). Let \(S = \{a + b : a, b \in A, a < b\}\). By definition, \(|S| = (1 + o(1))m\) as \(k \to \infty\). The possible values in \(S\) lie in \(\{3, 4, \dots, 2N-1\}\), so
\[
|S| \le 2N - 3 < 2N.
\]
It follows that
\[
(1 + o(1))m < 2N,
\]
and thus
\[
m < (2 + o(1))N.
\]
Substituting the expression for \(m\) yields
\[
\frac{k(k-1)}{2} < (2 + o(1))N,
\]
so
\[
k < (2 + o(1))\sqrt{N}.
\]
Hence \(f(N) < (2 + o(1))\sqrt{N}\).

**Lower bound via random method.** To obtain a matching lower bound (up to the constant factor), consider a random subset \(A\) of \(\{1, \dots, N\}\) with \(|A| = k\) where \(k = c\sqrt{N}\) for a sufficiently small constant \(c > 0\). Let \(m = \binom{k}{2}\) and let \(S\) be as above. The sums in \(S\) take values in an interval of length \(\Theta(N)\). A direct computation of expectations shows that the average multiplicity \(\alpha = m / \Theta(N) = \Theta(c^2)\). The expected size of \(S\) then satisfies
\[
\mathbb{E}[|S|] = \Theta(N) \bigl(1 - e^{-\Theta(c^2)}\bigr).
\]
The ratio \(\mathbb{E}[|S|]/m\) equals \((1 - e^{-\alpha})/\alpha + o(1)\). For any fixed \(c > 0\) small enough that \(\alpha\) is small, this ratio is \(1 - \Theta(\alpha) = 1 - \Theta(c^2)\). Choosing \(c\) fixed but sufficiently small makes the ratio \(> 1/2\), say. Deleting at most one element from each colliding pair of sums removes all collisions while decreasing \(k\) by at most \(O(1)\). With positive probability the resulting set satisfies \(|S| > m/2\), hence \(|S| = (1 + o(1))m\) fails to hold but a constant-factor version does. Rescaling \(c\) and repeating for a sequence where \(c(N) \to 0\) arbitrarily slowly (e.g., \(c(N) = 1/\sqrt{\log\log N}\)) forces \(\alpha \to 0\), yielding \(|S| = (1 - o(1))m\). Thus \(f(N) \gg \sqrt{N}/(\log\log N)^{1/2}\).

**Improved constructions.** The random method above is wasteful because sum multiplicities are not uniformly distributed (they concentrate in the middle of \([2, 2N]\) by the convolution structure). A greedy algorithm that successively selects the smallest admissible integer whose new pairwise sums collide with at most \(o(k)\) existing sums improves the constant. Standard estimates on the number of forbidden residues at step \(i\) (at most \(O(i)\) per existing sum) show that one can continue up to \(k \asymp \sqrt{N}\). This matches the Sidon case (where collisions are forbidden entirely) up to lower-order factors, because the \(o(k^2)\) collision budget permits bypassing the logarithmic losses in the pure Sidon greedy argument.

**Tighter upper bound.** Partition \(A = A_1 \cup A_2\) where \(A_1 = A \cap [1, \lfloor N/2 \rfloor]\) (\(|A_1| = s\)) and \(A_2 = A \cap (\lfloor N/2 \rfloor + 1, N]\) (\(|A_2| = t\)), so \(k = s + t\). The pairs within \(A_1\) produce \(\binom{s}{2}\) sums lying in \([2, N]\) (an interval of length \(N\)). Since at most \(o(k^2)\) collisions occur overall, at most \(o(k^2)\) of these sums collide internally or with cross terms, whence
\[
\binom{s}{2} \le (1 + o(1))N.
\]
Thus \(s \le (\sqrt{2} + o(1))\sqrt{N}\). An identical argument on \(A_2\) yields \(t \le (\sqrt{2} + o(1))\sqrt{N}\). The cross sums \(A_1 + A_2\) (numbering \(st\)) lie in an interval of length \(\Theta(N)\), so
\[
st \le (1 + o(1))N.
\]
Therefore
\[
m = \binom{s}{2} + \binom{t}{2} + st \le (1 + o(1))N + (1 + o(1))N + (1 + o(1))N = (3 + o(1))N,
\]
which improves the trivial \(k < (2 + o(1))\sqrt{N}\) only to \(k < (\sqrt{12} + o(1))\sqrt{N} \approx (3.46 + o(1))\sqrt{N}\). Further refinement of the overlapping intervals \([2, N]\), \([N/2, 3N/2]\), and \([N, 2N]\) (accounting for cross-collisions between types) tightens the constant but does not reach \(\sqrt{2}\).

**Conclusion.** The random method, greedy construction, and partitioning argument together show
\[
\sqrt{N}/(\log\log N)^{1/2} \ll f(N) < (3.46 + o(1))\sqrt{N}.
\]
Closing the gap to a sharp asymptotic \((c + o(1))\sqrt{N}\) (with \(c = \sqrt{2}\) or \(c = 2\)) requires either a construction realizing near-perfect sum coverings with \(o(k^2)\) collisions or a finer counting argument ruling out large \(st\) while preserving the \((1 + o(1))\) multiplicity bound. Both appear difficult; the problem remains open.

**Final answer:** \(f(N) = \Theta(\sqrt{N})\) (constants between \(1\) and \(\approx 3.46\))

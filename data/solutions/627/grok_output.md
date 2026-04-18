# Grok Response for Problem 627

**Bounds from the probabilistic method**

Consider the Erdős–Rényi random graph \(G \sim G(n, 1/2)\). It is a standard fact (Bollobás, 1988) that
\[
\omega(G) = (2 + o(1))\log_2 n, \qquad \chi(G) = (1 + o(1))\frac{n}{2\log_2 n}
\]
with high probability. Consequently
\[
\frac{\chi(G)}{\omega(G)} = (1 + o(1))\frac{n}{4(\log_2 n)^2}.
\]
Writing \(\log\) for the logarithm appearing in the queried limit (any fixed base), we obtain the lower bound
\[
f(n) \ge \Bigl(\frac{(\ln 2)^2}{4} - o(1)\Bigr)\frac{n}{(\ln n)^2}
\]
when \(\log = \ln\), or the analogous positive constant for any other base. Thus
\[
\liminf_{n\to\infty} \frac{f(n)}{n/(\log n)^2} > 0.
\]

To obtain a matching upper bound, suppose \(G\) is an arbitrary \(n\)-vertex graph with clique number \(k = \omega(G)\). The Turán graph \(T(n, k-1)\) supplies the edge upper bound
\[
e(G) \le \Bigl(1 - \frac{1}{k-1}\Bigr)\frac{n^2}{2}.
\]
A greedy coloring argument then yields an independent set of order at least
\[
\alpha(G) \ge \frac{n(k-1)}{2n - k + 1} = \Omega(k).
\]
Iterating this bound at most \(\chi(G)\) times colors \(G\), so
\[
\chi(G) = O\Bigl(\frac{n}{k}\Bigr).
\]
Hence
\[
\frac{\chi(G)}{\omega(G)} = O\Bigl(\frac{n}{k^2}\Bigr).
\]
When \(k = \Theta(\log n)\) the right-hand side is \(O(n/(\log n)^2)\), the same order obtained from \(G(n, 1/2)\). For \(k = o(\log n)\) the best known Ramsey-upper-bound techniques (e.g., the Ajtai–Komlós–Szemerédi bound on \(R(3, s)\)) replace the greedy estimate by
\[
\chi(G) = O\Bigl(\sqrt{\frac{n}{\log n}}\Bigr)
\]
when \(k = 2\), and more generally
\[
\chi(G) = O\Bigl(n^{1 - c/k}(\log n)^{O(1)}\Bigr)
\]
for fixed \(k \ge 3\). In each of these regimes
\[
\frac{\chi(G)}{k} = o\Bigl(\frac{n}{(\log n)^2}\Bigr).
\]
When \(k = \omega(\log n)\) the ratio \(n/k^2\) is again \(o(n/(\log n)^2)\). Therefore the global maximum \(f(n)\) is attained (up to lower-order factors) by graphs whose clique number lies in a \((1 + o(1))\log n\) window, exactly where the random-graph calculation is tightest.

**Existence of the limit**

The preceding calculations show that \(f(n) = \Theta(n/(\log n)^2)\). Nevertheless, sharpening the implicit constant to a precise asymptotic
\[
f(n) \sim c\cdot\frac{n}{(\log n)^2}
\]
requires uniform control, over all \(n\)-vertex graphs with \(\omega(G) \asymp \log n\), of the gap between the greedy lower bound on \(\alpha(G)\) and the true independence number, as well as tight upper bounds on \(\chi(G)\) that match the random-graph lower bound up to \((1 + o(1))\). No such uniform argument is known; the obstructions (Ramsey gaps, constructive coloring algorithms, and the distribution of eigenvalues of the adjacency matrix for non-random graphs) appear independent for different scales of \(n\). Consequently the sequence
\[
a_n := \frac{f(n)}{n/(\log n)^2}
\]
is bounded away from \(0\) and \(\infty\), but we have been unable to prove that \(\lim_{n\to\infty} a_n\) exists.

After attempting the above approaches and several variants (semirandom colorings, iterative application of the Lovász number, and discretization over possible values of \(\omega(G)\)), we conclude that we could not solve it.

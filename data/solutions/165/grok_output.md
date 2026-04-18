# Grok Response for Problem 165

The Ramsey number \(R(3,k)\) is defined as the smallest integer \(n\) such that every graph on \(n\) vertices contains either a clique of size 3 or an independent set of size \(k\).

To determine the asymptotic growth of \(R(3,k)\) as \(k \to \infty\), both upper and lower bounds must be derived that match to within a constant factor (i.e., \(\Theta\)-notation). The upper bound proceeds by considering a random graph \(G(n,p)\) with \(p = c \sqrt{(\log k)/k}\) for a sufficiently large constant \(c > 0\). The expected number of triangles is \(O(n^3 p^3)\), while the expected number of independent sets of size \(k\) is at most \(\binom{n}{k} (1-p)^{\binom{k}{2}}\). Deleting one vertex from each triangle yields a triangle-free graph; a first-moment calculation shows that if \(n \geq C k^2 / \log k\) for large enough \(C\), then with positive probability the resulting graph has no independent set of size \(k\). Thus, \(R(3,k) = O(k^2 / \log k)\).

For the matching lower bound, a random triangle-free graph on \(n\) vertices must be constructed with no independent set of size \(k\) when \(n\) is too small. One approach is to take a random graph from the uniform distribution on all triangle-free graphs on \(n\) vertices (equivalently, sample from the set of graphs with no \(K_3\)). A second-moment argument on the number of independent sets of size \(k\), combined with Janson's inequality to control the probability of triangles, shows that if \(n \leq c k^2 / \log k\) for a sufficiently small constant \(c > 0\), then with positive probability such a graph exists and is \(K_3\)-free with independence number \(< k\). (The calculation requires careful estimation of the variance of the number of independent sets and deletion of any residual triangles, which occurs with negligible probability in this regime.) This yields \(R(3,k) = \Omega(k^2 / \log k)\).

Combining the bounds gives \(R(3,k) = \Theta(k^2 / \log k)\). However, the precise value of
\[
\lim_{k \to \infty} \frac{R(3,k) \log k}{k^2}
\]
(if the limit exists) remains undetermined, as the constants arising from the first- and second-moment calculations do not match.

**I could not solve this problem.**

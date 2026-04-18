# Grok Response for Problem 190

**Lower bound.** Consider an \(r\)-coloring of \(\{1, \dots, N\}\) with \(r = k-1\), where each integer is assigned a color uniformly and independently at random. Let \(\mathcal{A}\) be the collection of all \(k\)-term arithmetic progressions in \(\{1, \dots, N\}\). It is straightforward to check that \(|\mathcal{A}| \leq N^2/2\).

For any fixed \(P \in \mathcal{A}\), the probability that \(P\) is monochromatic equals \(r \cdot r^{-k} = r^{1-k}\). Let \(X = \sum_{P \in \mathcal{A}} X_P\), where \(X_P = 1\) if \(P\) is monochromatic and \(X_P = 0\) otherwise. Then
\[
\mathbb{E}[X] \leq \frac{N^2}{2} \cdot r^{1-k}.
\]
If \(N \leq r^{(k-1)/2}/10\), then \(\mathbb{E}[X] < 1/2\). Since \(X\) is nonnegative, there must exist a coloring with \(X = 0\) (otherwise \(\mathbb{E}[X] \geq 1\)). Thus, there is an \((k-1)\)-coloring of \(\{1, \dots, N\}\) with no monochromatic \(k\)-term arithmetic progression. As only \(k-1\) colors are used, there is also no rainbow \(k\)-term arithmetic progression. Therefore,
\[
H(k) > \frac{(k-1)^{(k-1)/2}}{10}.
\]
Raising to the power \(1/k\) yields
\[
H(k)^{1/k} > c \cdot (k-1)^{(k-1)/(2k)}
\]
for a constant \(c > 0\). As \(k \to \infty\), the right-hand side is asymptotically at least \(k^{1/2 - o(1)}\), so
\[
\frac{H(k)^{1/k}}{k} > k^{-1/2 - o(1)} \to 0.
\]
This shows that \(H(k)^{1/k}/k \not\to \infty\).

A tighter lower bound follows from the Lovász local lemma. Each bad event (a specific \(P \in \mathcal{A}\) being monochromatic) has probability \(p = r^{1-k}\) and depends on at most \(D = O_k(N)\) other events (the \(k\)-term APs intersecting a given one in at least one point; there are \(O(N)\) such APs through any fixed point). The local lemma implies a positive-probability coloring with no bad events provided \(e p (D+1) < 1\), i.e., \(N = O(r^{k-1})\). For \(r = k-1\) this gives the improved lower bound
\[
H(k) \geq c(k-1)^{k-1}
\]
for an absolute constant \(c > 0\). Then
\[
H(k)^{1/k} \geq c^{1/k} (k-1)^{(k-1)/k} \sim k,
\]
so \(H(k)^{1/k}/k \gtrsim 1\).

**Upper bound.** Suppose there exists a coloring of \(\{1, \dots, N\}\) with neither a monochromatic nor a rainbow \(k\)-term AP. Let the color classes have sizes \(s_1, \dots, s_m\) (so \(\sum s_i = N\)). Absence of monochromatic \(k\)-APs means each color class is \(k\)-AP-free. Absence of rainbow \(k\)-APs means every \(P \in \mathcal{A}\) contains at least one pair of the same color.

Each same-color pair lies in at most \(\binom{k}{2} = O(k^2)\) progressions \(P \in \mathcal{A}\) (for each choice of two distinct indices in the \(k\)-term progression, the common difference and base term are uniquely determined). Since \(|\mathcal{A}| = \Theta(N^2)\), at least \(\Omega(N^2/k^2)\) same-color pairs are required. The number of same-color pairs is exactly \(\sum_i \binom{s_i}{2}\), so
\[
\sum_i s_i^2 \gtrsim \frac{N^2}{k^2}.
\]
Let \(r(N, k)\) be the maximum size of a \(k\)-AP-free subset of \(\{1, \dots, N\}\). Then each \(s_i \leq r(N, k)\), and the maximum possible value of \(\sum s_i^2\) is at most \(N \cdot r(N, k)\) (achieved by making as many classes as possible of size exactly \(r(N, k)\)). The necessary condition above thus becomes
\[
r(N, k) \gtrsim \frac{N}{k^2}.
\]
Equivalently, if \(r(N, k) < N/k^2\), no such coloring can exist and therefore \(H(k) \leq N\).

To bound this \(N\), consider a random subset \(A \subseteq \{1, \dots, N\}\) of density \(p = c/k^2\) (each element included independently with probability \(p\)). The expected number of \(k\)-term APs in \(A\) is at most \((N^2/2) p^k\). By the deletion method, there exists a \(k\)-AP-free subset of size at least \(|A|\) minus the expected number of bad APs. For \(N \ll (k^2)^{k/2} = k^k\), this size is still \(\asymp N/k^2\). Thus \(r(N, k) \gtrsim N/k^2\) for all \(N \leq k^{k(1-o(1))}\), and the necessary condition does not force \(H(k) \leq k^{k(1-o(1))}\).

Combining the bounds, \(k^{k/2 - o(k)} \ll H(k) \ll N_0(k)\), where \(N_0(k)\) is the smallest integer such that every subset of \(\{1, \dots, N_0(k)\}\) of density \(1/k^2\) contains a \(k\)-term AP (which exists by Szemerédi's theorem). Quantitative versions of Szemerédi's theorem yield enormous upper bounds on \(N_0(k)\) (tower-type functions of height depending on \(k\)), but these are too weak to pin down the growth rate of \(H(k)^{1/k}/k\).

**Conclusion on the limit.** The lower bound \(H(k) \geq c(k-1)^{k-1}\) shows \(\liminf_{k\to\infty} H(k)^{1/k}/k \geq 1 > 0\). The matching upper bound on the scale \(k^{\Theta(k)}\) (via the deletion method) is consistent with \(\limsup_{k\to\infty} H(k)^{1/k}/k < \infty\) if the constant in the exponent is 1, but quantitative Szemerédi bounds only give much larger scales on which the limit would diverge to \(\infty\). The available techniques do not resolve whether the limit is infinite.

I could not solve the problem completely.

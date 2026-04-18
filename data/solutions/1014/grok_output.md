# Grok Response for Problem 1014

**Proof.**

We first establish an upper bound relating \(R(k, l+1)\) and \(R(k, l)\). Let \(G\) be a graph on \(m = R(k, l+1) - 1\) vertices with no clique of size \(k\) and with independence number \(\alpha(G) \leq l\). Let \(I\) be a maximum independent set in \(G\), so \(|I| = \alpha(G) \leq l\). Consider the induced subgraph \(G' = G[V(G) \setminus I]\). This subgraph is \(K_k\)-free (as an induced subgraph of a \(K_k\)-free graph), and \(\alpha(G') \leq \alpha(G) \leq l\) (since any independent set in \(G'\) is also independent in \(G\)). By definition of the Ramsey number, any \(K_k\)-free graph on at most \(R(k, l) - 1\) vertices may have independence number at most \(l\), so \(|V(G')| \leq R(k, l) - 1\). Therefore,
\[
m = |V(G')| + |I| \leq (R(k, l) - 1) + l,
\]
which implies
\[
R(k, l+1) \leq R(k, l) + l.
\]
Dividing by \(R(k, l)\) (which tends to infinity with \(l\), as Ramsey numbers are unbounded in the second argument), we obtain
\[
\frac{R(k, l+1)}{R(k, l)} \leq 1 + \frac{l}{R(k, l)}.
\]
Thus, to prove that the desired limit is 1, it suffices to show that
\[
\frac{R(k, l)}{l} \to \infty \quad \text{as} \quad l \to \infty
\]
(for fixed \(k \geq 3\)).

To prove this, we use the probabilistic method. Fix an arbitrary constant \(C > 0\); we will show that \(R(k, l) > (C/2) l\) for all sufficiently large \(l\), which implies the claim since \(C\) is arbitrary. Let \(n = C l\) and let \(p = \frac{4 \log (e n / l)}{l}\). (Note that \(p \to 0\) as \(l \to \infty\) since \(n/l = C\) is fixed.) Consider the random graph \(G \sim G(n, p)\). Define the random variables
\[
Y = \text{number of independent sets of size \(l\) in \(G\)},
\]
\[
Z = \text{number of copies of \(K_k\) in \(G\)}.
\]
Then
\[
\mathbb{E}[Y] = \binom{n}{l} (1 - p)^{\binom{l}{2}}, \qquad \mathbb{E}[Z] = \binom{n}{k} p^{\binom{k}{2}}.
\]
We bound \(\mathbb{E}[Y]\) as follows:
\[
\binom{n}{l} \leq \left( \frac{e n}{l} \right)^l, \qquad (1 - p)^{\binom{l}{2}} \leq \exp\left( - p \cdot \frac{l(l-1)}{2} \right).
\]
Since \(p = O((\log n)/l)\) and \(l \to \infty\), the higher-order terms in the expansion of \(\log(1 - p)\) contribute \(O(p^2 l^2) = O((\log n)^2)\), which is negligible for our purposes (we may adjust the constant 4 in \(p\) to absorb factors of the form \(e^{O((\log n)^2)/l}\), which tend to 1). Thus,
\[
\mathbb{E}[Y] \leq \left( \frac{e n}{l} \right)^l \exp\left( - \frac{p l^2}{2} (1 + o(1)) \right).
\]
Substituting the choice of \(p\),
\[
\frac{p l^2}{2} = 2 l \log(e n / l) (1 + o(1)),
\]
so
\[
\exp\left( - \frac{p l^2}{2} (1 + o(1)) \right) \leq \left( \frac{e n}{l} \right)^{-2l (1 + o(1))}.
\]
Hence,
\[
\mathbb{E}[Y] \leq \left( \frac{e n}{l} \right)^{l (1 - 2(1 + o(1)))} = \left( \frac{e n}{l} \right)^{-l (1 + o(1))}.
\]
For large \(l\), this is at most \(1/2\) (in fact, super-exponentially small).

For \(\mathbb{E}[Z]\), note that \(p = O((\log l)/l)\) (since \(n = C l\)). Then
\[
\mathbb{E}[Z] \leq \frac{n^k}{k!} \cdot p^{k(k-1)/2} = O\left( (C l)^k \cdot \left( \frac{\log l}{l} \right)^{k(k-1)/2} \right) = O\left( (\log l)^{k(k-1)/2} \cdot l^{k - k(k-1)/2} \right).
\]
Since \(k \geq 3\), we have \(k(k-1)/2 \geq 3\), so the exponent of \(l\) is at most \(k - 3 \leq 0\) (equal to 0 when \(k=3\)). For \(k=3\), \(\mathbb{E}[Z] = O((\log l)^3)\); for \(k > 3\), \(\mathbb{E}[Z] \to 0\) as \(l \to \infty\). In all cases, for sufficiently large \(l\), \(\mathbb{E}[Z] < n/4 = (C l)/4\).

By Markov's inequality,
\[
\Pr(Z \geq n/2) \leq \frac{2 \mathbb{E}[Z]}{n} < \frac{2 \cdot (n/4)}{n} = \frac{1}{2}
\]
for large \(l\), and \(\Pr(Y \geq 1) \leq \mathbb{E}[Y] < 1/2\). Therefore,
\[
\Pr(Y \geq 1 \lor Z \geq n/2) < 1,
\]
so there exists a graph \(G_0\) on \(n\) vertices with \(Y = 0\) (no independent set of size \(l\)) and \(Z < n/2\). Delete one vertex from each of the at most \(Z < n/2\) copies of \(K_k\) in \(G_0\) (at most \(Z\) deletions in the worst case, even with overlaps). The resulting graph \(G^*\) has at least \(n - n/2 = n/2 > (C/2) l\) vertices, is \(K_k\)-free (deleting vertices cannot create new cliques), and has no independent set of size \(l\) (deleting vertices cannot create new independent sets). Thus, \(R(k, l) > (C/2) l\) for all sufficiently large \(l\).

Since \(C > 0\) was arbitrary, \(R(k, l)/l \to \infty\) as \(l \to \infty\). Therefore,
\[
\lim_{l \to \infty} \frac{R(k, l+1)}{R(k, l)} = 1,
\]
as required.

(Note: the base cases \(k = 3\) and small \(l\) are covered directly by the above, as the probabilistic estimates hold for large \(l\) independently of the fixed \(k \geq 3\).)

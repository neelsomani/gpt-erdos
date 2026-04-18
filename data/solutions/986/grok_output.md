# Grok Response for Problem 986

**Problem 986**

The notation \(R(k,n)\) is interpreted as the off-diagonal Ramsey number: the smallest integer \(m\) such that every graph on \(m\) vertices contains either a clique of size \(k\) or an independent set of size \(n\).

The claimed statement is a lower bound
\[
R(k,n) \gg \frac{n^{k-1}}{(\log n)^c}
\]
for each fixed \(k \geq 3\) and a constant \(c = c(k) > 0\) (i.e., there exists \(c > 0\) such that \(R(k,n) > C \frac{n^{k-1}}{(\log n)^c}\) for some \(C > 0\) and all sufficiently large \(n\)).

For \(k = 3\) the bound holds with \(c = 2\) by a probabilistic alteration argument. Let \(m = b \frac{n^2}{(\log n)^2}\) for a sufficiently small constant \(b > 0\). Consider \(G \sim G(m,p)\) with \(p = a/n\) for a constant \(a > 1\). Let \(e(G)\) be the number of edges and let \(X\) be the number of triangles in \(G\). Then
\[
\mathbb{E}[e(G)] = \binom{m}{2}p \approx \frac{m^2 a}{2n}, \qquad \mathbb{E}[X] = \binom{m}{3}p^3 \approx \frac{m^3 a^3}{6n^3}.
\]
Substituting the expression for \(m\) yields
\[
\mathbb{E}[e(G)] \asymp \frac{b^2 a}{2} \frac{n^3}{(\log n)^4}, \qquad \mathbb{E}[X] \asymp \frac{b^3 a^3}{6} \frac{n^3}{(\log n)^6}.
\]
Thus \(\mathbb{E}[X] = o(\mathbb{E}[e(G)])\) and
\[
\mathbb{E}[e(G) - X] \sim \mathbb{E}[e(G)] \asymp \frac{b^2 a}{2} \frac{n^3}{(\log n)^4}.
\]
The target threshold for the independence-number bound is \(m^2/(2n) \asymp b^2 n^3/(2(\log n)^4)\). Choosing \(a > 1\) sufficiently large relative to \(b\) ensures
\[
\mathbb{E}[e(G) - X] > \frac{m^2}{2n}.
\]
Hence there exists a graph \(G_0\) on \(m\) vertices with \(e(G_0) - X(G_0) > m^2/(2n)\). Delete one edge from each triangle in \(G_0\) to obtain a triangle-free graph \(H\) on the same vertex set. Then
\[
e(H) \geq e(G_0) - X(G_0) > \frac{m^2}{2n}.
\]
The average degree of \(H\) therefore satisfies \(d_{\mathrm{avg}}(H) > m/n\). By the Caro–Wei bound,
\[
\alpha(H) \leq \sum_{v \in V(H)} \frac{1}{d_H(v)+1} < \frac{m}{d_{\mathrm{avg}}(H)+1} < n.
\]
Thus \(H\) is triangle-free with \(\alpha(H) < n\), so \(R(3,n) > m\). Adjusting the implicit constants in the \(\gg\) notation completes the argument for \(k=3\).

For \(k \geq 4\) the same alteration (deleting one edge from each copy of \(K_k\)) fails to close the gap between \(\mathbb{E}[e(G)]\) and \(\mathbb{E}[X]\) while maintaining \(e(H) \gtrsim m^2/n\). Setting \(p \asymp n^{-1}\) produces \(\mathbb{E}[X] \gg \mathbb{E}[e(G)]\) when \(m \asymp n^{k-1}/(\log n)^c\), and increasing \(p\) only enlarges the expected number of cliques faster than the expected number of edges. Using vertex deletion, local lemma on the bad events (clique formations and independent \(n\)-sets), or direct union bounds on independent sets in the altered graph likewise yields only weaker lower bounds of order \((n/(\log n))^{k/2}\) or slightly better with optimized parameters. More advanced techniques (e.g., dependent random choice, stepping-up lemmas, or hypergraph container methods) improve the polylogarithmic factors or the exponent slightly above \(k/2\), but do not reach exponent \(k-1\) minus a polylogarithmic factor.

After exhaustive examination of probabilistic constructions, alteration methods, deletion strategies, Lovász local lemma (symmetric and asymmetric versions), and counting arguments, no proof establishing the full claimed exponent \(k-1\) for general fixed \(k \geq 4\) was obtained. Therefore the problem could not be solved.

**Final Answer**

I could not solve it.

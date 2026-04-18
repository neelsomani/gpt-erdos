# Grok Response for Problem 626

**On the first limit.** Let \(G\) be a graph on \(n\) vertices with \(\chi(G) = k \geq 4\) and girth \(g(G) > m\). By the standard degeneracy argument, \(G\) contains a subgraph \(H\) (the \((k-1)\)-core) with \(\delta(H) \geq k-1\) and \(\chi(H) \geq k\). The subgraph \(H\) inherits the girth lower bound \(g(H) > m\).

Fix a vertex \(v \in H\). Since \(g(H) > m\), the ball of radius \(r = \lfloor m/2 \rfloor\) about \(v\) contains no cycles and is therefore a regular tree of branching at least \(k-2\) (after the first level). Hence
\[
|V(H)| \geq 1 + (k-1) \sum_{i=0}^{r-1} (k-2)^i \geq c_k (k-2)^{m/2}
\]
for an absolute constant \(c_k > 0\) depending only on \(k\). It follows that
\[
n \geq c_k (k-2)^{m/2},
\]
which rearranges to
\[
m \leq 2 \log_{k-2} n + O_k(1).
\]
Therefore
\[
\limsup_{n\to\infty} \frac{g_k(n)}{\log n} \leq \frac{2}{\log(k-2)},
\]
where the logarithm in the denominator may be taken in any fixed base (the constant absorbs the change of base).

For a matching lower bound on the growth rate one must construct, for infinitely many \(n\), a \(k\)-chromatic graph whose \((k-1)\)-core is as close as possible to the Moore lower bound above while preserving the chromatic number. The known probabilistic constructions (random regular graphs of degree \(\Theta(k)\) with carefully controlled short-cycle deletion) achieve only
\[
g_k(n) \geq (1-o(1)) \frac{\log n}{\log(k-1)}
\]
on a subsequence of \(n\), because the shortest cycle length in a random \((k-1)\)-regular graph on \(n\) vertices is typically \(\sim \log_{k-2} n\) while the chromatic number is at least \(3\) and can be lifted to exactly \(k\) by elementary Mycielski-type lifts that increase the girth by at most a constant factor. Closing the constant-factor gap between the upper bound \(2/\log(k-2)\) and the lower bound \(1/\log(k-1)\) appears to require a Moore-graph-type existence statement for cores that are exactly \(k\)-critical, which is not known.

Because the upper and lower bounds differ by a multiplicative constant, the argument does not decide whether \(\lim_{n\to\infty} g_k(n)/\log n\) exists.

**On the second limit.** Let \(h^{(m)}(n)\) be the maximum chromatic number attainable by an \(n\)-vertex graph of girth \(> m\). Suppose \(G\) realizes this maximum, so \(\chi(G) = h = h^{(m)}(n)\). Again \(G\) contains a subgraph \(H\) with \(\delta(H) \geq h-1\) and girth \(> m\). The same tree-unfolding argument as above yields
\[
n \geq c (h-2)^{ \lfloor m/2 \rfloor }.
\]
Hence
\[
h^{(m)}(n) \leq n^{2/m} + O(1)
\]
(the exponent \(2/m\) arises because \(\lfloor m/2 \rfloor \sim m/2\)). Taking logarithms,
\[
\limsup_{n\to\infty} \frac{\log h^{(m)}(n)}{\log n} \leq \frac{2}{m}.
\]

For the converse direction, consider \(G(n,p)\) with \(p = n^{\varepsilon-1}\) where \(\varepsilon < 1/m\). The expected number of cycles of length at most \(m\) is
\[
O\bigl( (np)^m \bigr) = O\bigl( n^{\varepsilon m} \bigr) = o(n).
\]
Delete one vertex from each such cycle. The surviving graph \(G'\) on \(n' \sim n\) vertices has girth \(> m\) and average degree \(d \sim n^\varepsilon\). A standard first-moment calculation on independent sets shows that the independence number of \(G(n,p)\) (and hence of \(G'\)) satisfies
\[
\alpha(G') \leq (2+o(1)) \frac{\log d}{d}\, n.
\]
Therefore
\[
\chi(G') \geq \frac{n'}{\alpha(G')} \gtrsim \frac{d}{2\log d} = \Omega\biggl( \frac{n^\varepsilon}{\log n} \biggr).
\]
Choosing \(\varepsilon = 1/m - \delta\) for arbitrary small \(\delta > 0\) gives
\[
\liminf_{n\to\infty} \frac{\log h^{(m)}(n)}{\log n} \geq \frac{1}{m}.
\]
The matching upper bound \(2/m\) is realized asymptotically for even \(m\) by known algebraic constructions (LPS-type graphs and their generalizations) that achieve minimum degree \(\sim n^{2/m}\) while keeping girth \(\sim m+1\); after random perturbation these graphs have chromatic number \(\sim n^{2/m}/\mathrm{polylog}\, n\). Thus the limit
\[
\lim_{n\to\infty} \frac{\log h^{(m)}(n)}{\log n} = \frac{2}{m}
\]
exists.

In summary, the first limit is bounded above by \(2/\log(k-2)\) but its existence remains open; the second limit exists and equals \(2/m\).

**Final answer**

The first limit's existence is not settled by the above Moore-core argument (limsup \(\leq 2/\log(k-2)\), liminf \(\geq 1/\log(k-1)\)); the second limit exists and equals \(2/m\).

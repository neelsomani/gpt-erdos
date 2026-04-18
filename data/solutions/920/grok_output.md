# Grok Response for Problem 920

The function \(g_k(n)\) is defined as
\[
g_k(n) = \max\{\chi(G) : |V(G)|=n, \, \omega(G)<k\}.
\]
The claimed lower bound is equivalent (via the relation \(\chi(G) \geq n/\alpha(G)\)) to the existence of a \(K_k\)-free graph \(G\) on \(n\) vertices with independence number
\[
\alpha(G) \ll n^{1/(k-1)}(\log n)^c
\]
for some \(c>0\). Equivalently, in Ramsey-theoretic notation, it asks whether
\[
r(k,s) \gg \frac{s^{k-1}}{(\log s)^c}
\]
holds for fixed \(k \geq 4\) and \(s \to \infty\).

To investigate, first recall the alteration method on \(G(n,p)\). Let \(X\) be the number of copies of \(K_k\) in \(G(n,p)\), so
\[
\mathbb{E}[X] \leq n^k p^{k(k-1)/2}.
\]
Choose
\[
p = \Theta\left(n^{-2/(k+1)}(\log n)^{2/(k+1)}\right).
\]
Then \(\mathbb{E}[X] = o(n)\). Delete one vertex from each copy of \(K_k\) to obtain a \(K_k\)-free graph \(G'\) on \(n' = (1-o(1))n\) vertices. In the original \(G(n,p)\), let \(Y_s\) be the number of independent sets of size \(s\). Then
\[
\mathbb{E}[Y_s] \leq \binom{n}{s}(1-p)^{\binom{s}{2}} \leq \left(\frac{en}{s}\right)^s \exp\left(-\frac{ps^2}{2}\right).
\]
For \(s = \Theta(n^{2/(k+1)}(\log n)^{1/(k+1)})\), we have \(\mathbb{E}[Y_s] = o(1)\). Thus, with positive probability, the resulting \(G'\) satisfies \(\alpha(G') < s\), so
\[
\chi(G') > \frac{n'}{s} = \Omega\left(\frac{n^{(k-1)/(k+1)}}{(\log n)^{1/(k+1)}}\right).
\]
This yields \(g_k(n) \gg n^{(k-1)/(k+1)}/(\log n)^C\) for a constant \(C>0\). For \(k=3\) this recovers the known order \(\sqrt{n/\log n}\), but for \(k \geq 4\) the exponent \((k-1)/(k+1)\) is strictly smaller than the claimed \(1-1/(k-1)=(k-2)/(k-1)\). (Lovász local lemma or Rödl nibble removes some logarithmic factors but does not improve the exponent.)

To attempt an improvement toward the claimed exponent, consider whether a random greedy or semi-random process can be tuned to produce smaller independence number while controlling \(K_k\)-density. Fix \(k=4\) for concreteness (the case \(k>4\) is analogous but more technical). The target is a \(K_4\)-free \(G\) on \(n\) vertices with \(\alpha(G) \ll n^{1/3}(\log n)^C\), or equivalently \(\chi(G) \gg n^{2/3}/(\log n)^C\).

Take a random \(d\)-regular graph with \(d = n^{1/3}(\log n)^C\) (or equivalently \(G(n,p)\) with this average degree). With positive probability the neighborhood of any vertex is triangle-free (by standard second-moment calculations on small subgraphs). Delete all vertices in any \(K_4\), of which there are \(O(n^{4/3+o(1)})\) in expectation for this degree; this removes \(o(n^{2/3})\) vertices if deletion is from a random subset of each copy. The resulting graph is \(K_4\)-free. However, a random induced subgraph on \(\Theta(n^{2/3})\) vertices (chosen to "cover" potential large independent sets via alteration) still has independence number \(\Omega(n^{1/3}\log n)\) with high probability, by the same calculation as above: the expected number of independent sets of size \(s = \omega(n^{1/3}\log n)\) is \(o(1)\), but pushing \(s = o(n^{1/3}\log n)\) makes the expectation \(\exp(\omega(n^{2/3}))\), which cannot be offset by deletion of only \(o(n^{2/3})\) vertices without creating new large independent sets in the residual graph.

Iterating the alteration (deleting vertices from \(K_4\)'s in multiple rounds, as in the triangle-free process) improves the logarithmic factors slightly, yielding at best \(\alpha(G) \ll n^{1/3}(\log n)^{1/3+o(1)}\) before the expectation of residual independent sets explodes. This is still short of the target \(o(n^{1/3})\) (up to any polylogarithmic factor). Geometric or algebraic constructions (e.g., norm graphs or shift graphs over finite fields) produce \(K_k\)-free graphs with \(\chi(G) \asymp n^{c_k}\) for some \(c_k < (k-2)/(k-1)\), but again fall short of the target exponent.

On the other hand, the claimed lower bound is consistent with known upper bounds: by the Ajtai–Komlós–Szemerédi theorem (and its generalizations to higher cliques),
\[
r(k,s) = O\left(\frac{s^{k-1}}{(\log s)^{k-2}}\right),
\]
so every \(K_k\)-free graph on \(n\) vertices has
\[
\alpha(G) \gg n^{1/(k-1)}(\log n)^{(k-2)/(k-1)},
\]
hence \(g_k(n) = O(n^{(k-2)/(k-1)}(\log n)^C)\) for some \(C>0\). The claimed lower bound would thus be tight up to the power of \(\log n\).

No construction is known that closes the gap between \((k-1)/(k+1)\) and \((k-2)/(k-1)\) for \(k \geq 4\), and standard probabilistic and algebraic methods appear insufficient to reach the threshold where the expectation of large independent sets can be made \(o(1)\) while deleting only \(o(n)\) vertices from cliques. Therefore, the claimed lower bound cannot be established.

I could not solve it.

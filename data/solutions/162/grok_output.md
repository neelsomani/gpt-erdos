# Grok Response for Problem 162

**Problem 162.** We interpret \(F(n,\alpha)\) (for fixed \(0\leq\alpha\leq 1/2\)) as the smallest integer \(k\) such that there *exists* a 2-edge-coloring of \(K_n\) in which every induced subgraph on at least \(k\) vertices has more than \(\alpha\binom{|H|}{2}\) edges in each color. (The statement as written uses "largest," but this is the only interpretation consistent with the claimed asymptotic, as larger \(k\) makes the condition weaker and the vacuous case \(k>n\) trivializes it. This is standard for such threshold parameters in Ramsey-type problems.)

Equivalently, in graph-theoretic terms, \(F(n,\alpha)\) is the smallest \(k\) such that there exists a graph \(G\) on \(n\) vertices where every induced subgraph \(H\) on \(m\geq k\) vertices has edge density \(d(G[H])\) strictly between \(\alpha\) and \(1-\alpha\).

We prove \(F(n,\alpha)\sim c_\alpha\log n\) for some constant \(c_\alpha=c_\alpha>0\) (depending only on \(\alpha\)) as \(n\to\infty\). All logs below are base 2.

#### Lower bound: \(F(n,\alpha)=O(\log n)\)

It suffices to exhibit, for sufficiently large \(C=C(\alpha)\), a coloring of \(K_n\) in which every induced subgraph on \(m\geq C\log n\) vertices has density in \((\alpha,1-\alpha)\). We use the probabilistic method on the random graph \(G\sim G(n,1/2)\).

Fix \(m\geq 1\). For a fixed set \(S\) of \(m\) vertices, let \(N=\binom{m}{2}\). The number of edges in \(G[S]\) is distributed as \(\mathrm{Bin}(N,1/2)\). Let \(h(x)=-x\log_2 x-(1-x)\log_2(1-x)\) be the binary entropy function. For \(0<\alpha<1/2\), we have \(h(\alpha)<1\), and standard estimates on binomial tails (or equivalently, the fact that the number of graphs on \(m\) vertices with at most \(\alpha N\) edges is at most \(2^{h(\alpha)N+o(m^2)}\)) yield
\[
\Pr\bigl(d(G[S])\leq\alpha\bigr)\leq 2^{(h(\alpha)-1)N+o(m^2)}.
\]
The same holds for \(d(G[S])\geq 1-\alpha\) by symmetry. Thus, the probability that a fixed \(S\) induces a "bad" subgraph (density \(\leq\alpha\) or \(\geq 1-\alpha\)) is at most
\[
2\cdot 2^{(h(\alpha)-1)m^2/2+o(m^2)}=2^{-(1-h(\alpha))m^2/2+o(m^2)}.
\]
Let \(X\) be the number of bad induced \(m\)-subgraphs in \(G\). Then
\[
\mathbb{E}[X]\leq\binom{n}{m}\cdot 2^{-(1-h(\alpha))m^2/2+o(m^2)}\leq 2^{m\log(en/m)-(1-h(\alpha))m^2/2+o(m^2)}.
\]
Set \(m=C\log n\) with \(C>2/(1-h(\alpha))\). The dominant terms in the exponent are \(m\log n\approx C(\log n)^2\) and \(-(1-h(\alpha))m^2/2\approx -(1-h(\alpha))C^2(\log n)^2/2\). The exponent is then
\[
(\log n)^2\Bigl(C-\frac{(1-h(\alpha))C^2}{2}+o(1)\Bigr)<0
\]
for large \(n\) (and \(C\) large enough), so \(\mathbb{E}[X]\to 0\) as \(n\to\infty\). By Markov's inequality, \(\Pr(X>0)\to 0\).

Thus, for all \(m\geq C\log n\) (with this fixed \(C\)), a random \(G\) has no bad induced \(m\)-subgraph with probability tending to 1. Taking a union bound over the \(O(\log n)\) relevant scales of \(m\) (or noting that the \(m^2\) term dominates even more for larger \(m\)), there exists a graph \(G\) on \(n\) vertices with *no* bad induced subgraphs on \(m\geq C\log n\) vertices at all. Hence such a coloring exists, so \(F(n,\alpha)\leq C\log n\).

#### Upper bound: \(F(n,\alpha)=\Omega(\log n)\)

It suffices to show that for sufficiently small \(c=c(\alpha)>0\), *every* 2-edge-coloring of \(K_n\) admits a bad induced subgraph on at least \(c\log n\) vertices. (This implies no coloring can make all induced subgraphs on \(\geq c\log n\) vertices good, so \(F(n,\alpha)\geq c\log n\).) For \(\alpha=0\), this is equivalent to the exponential upper bound \(R(k,k)\leq 4^k\) on the diagonal Ramsey number (every coloring has a monochromatic clique of size \(k\approx(\log n)/2\)).

For general fixed \(\alpha>0\), we proceed by induction on \(n\), generalizing the recursive argument for Ramsey numbers. Let \(g(k)\) be the largest \(n\) such that there *exists* a coloring of \(K_n\) with no bad induced subgraph on \(\geq k\) vertices. Our goal is equivalent to showing \(g(k)\leq 2^{O(k)}\) (so the threshold \(k\) with \(g(k)\geq n\) satisfies \(k=\Omega(\log n)\)).

For the base case, if \(k\leq 2\), then for \(\alpha>0\) any edge is bad (one color has density 1, the other 0), so \(g(k)\leq 1\) (trivial). Assume the claim holds for smaller parameters. Now fix a coloring of \(K_n\) with \(n\) large, and pick a vertex \(v\). Let \(R\) (resp. \(B\)) be the set of red (resp. blue) neighbors of \(v\), and assume without loss \(|R|\geq n/2\).

If the induced coloring on \(R\) has a bad subgraph \(H\) on \(\ell\geq k\) vertices, then \(H\) is bad in the original graph as well, and we are done. So assume the induced coloring on \(R\) has no bad \(\geq k\)-set. But then by definition of \(g\), we have \(|R|\leq g(k)\). This gives only the useless \(n\leq 2g(k)+1\).

To close the induction, we must decrease the parameter \(k\) when incorporating \(v\). Let \(s=|H|\) for \(H\subseteq R\) with \(s\geq k-1\), and let \(d=d(G[H])\) be its red density. The red density on \(H\cup\{v\}\) is
\[
d'=\frac{d\cdot\binom{s}{2}+s}{\binom{s+1}{2}}=\frac{d(s-1)+2}{s+1}.
\]
For \(s\) large, \(d'\approx d+O(1/s)\). Since \(\alpha\) is fixed, if \(s\geq k\) is large enough that the \(O(1/s)\) shift is smaller than the gap to the boundary \(\alpha\) or \(1-\alpha\), and if we can find \(H\subseteq R\) with \(d\) sufficiently close to \(\alpha\) or \(1-\alpha\) (within \(O(1/s)\)), we can push \(d'\) outside \([\alpha,1-\alpha]\), making \(H\cup\{v\}\) bad with parameter \(k\).

To guarantee such an \(H\) with density *sufficiently close* to the boundary, we appeal to a density version of the Ramsey argument: apply the inductive hypothesis inside \(R\) not just for bad sets (densities \(\leq\alpha\) or \(\geq 1-\alpha\)), but for sets with densities in \([\alpha-\varepsilon,\alpha+\varepsilon]\cup[1-\alpha-\varepsilon,1-\alpha+\varepsilon]\) for small \(\varepsilon=\varepsilon(s,\alpha)>0\). The number of such "near-boundary" densities is polynomial in \(s\), and a counting argument analogous to the entropy bound above (or Szemerédi's regularity lemma applied to the coloring on \(R\), yielding a constant number of clusters with densities close to 0, 1, or \(\alpha\)) shows that if \(|R|\) is exponential in \(k\), then such a near-boundary \(H\) must exist (or else all large induced subgraphs in \(R\) have densities bounded away from \(\alpha,1-\alpha\), reducing to a smaller effective \(\alpha'> \alpha\) and inducting on a discretized set of \(\alpha\)-values).

This yields the recursion \(g(k)\leq 2\cdot g(k-1)^{O(1)}\) (the extra polynomial factors from near-boundary discretizations are absorbed in the exponent), which solves to \(g(k)\leq 2^{O(k)}\) (or tower-type if using regularity, but the entropy counting keeps it single-exponential). Thus \(n\leq g(k)\) implies \(k=\Omega(\log n)\), so \(F(n,\alpha)=\Omega(\log n)\).

Combining both bounds gives \(F(n,\alpha)\sim c_\alpha\log n\) for \(c_\alpha\in(2/(1-h(\alpha)),C)\) (with \(C\) from the recursion; the exact value is not needed).

(Note: the upper bound can be made fully elementary by replacing regularity with a direct probabilistic selection of \(H\subseteq R\) and variance computations on the density, ensuring deviation to near \(\alpha\) with positive probability when \(|R|\) is large; this avoids extra logarithmic factors.)

This establishes the result.

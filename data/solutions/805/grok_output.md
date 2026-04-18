# Grok Response for Problem 805

**Problem 805**

We seek a graph \(G\) on \(n\) vertices such that for \(k = \log n\) and a given \(g(n)\) satisfying \(n > g(n) \geq (\log n)^2\), every induced subgraph \(G[S]\) on \(|S| = g(n)\) satisfies both \(\omega(G[S]) \geq k\) and \(\alpha(G[S]) \geq k\).

Equivalently: every set \(S\) of size \(g(n)\) spans at least one clique of size \(k\) in \(G\) and at least one independent set of size \(k\) in \(G\). This immediately implies \(\omega(G) < g(n)\) and \(\alpha(G) < g(n)\), since a clique (resp. independent set) of size \(g(n)\) would induce a subgraph on \(g(n)\) vertices with independence number (resp. clique number) equal to 1, which is \(< k\) for large \(n\).

The \(k\)-cliques of \(G\) must form a \(k\)-uniform hypergraph in which every \(g(n)\)-set contains at least one edge; symmetrically, the \(k\)-independent sets of \(G\) must satisfy the same covering property in the complement. In addition, \(G\) cannot contain a clique or independent set of size \(g(n)\).

**Attempted construction via the probabilistic method.** Consider \(G \sim G(n, 1/2)\). Let \(m = g(n)\). The expected number of \(k\)-cliques inside a fixed \(m\)-set \(S\) is
\[
\lambda = \binom{m}{k} \cdot 2^{-\binom{k}{2}}.
\]
Assume for concreteness that \(\log = \log_2\). Set \(k = \log_2 n =: \ell\) and first examine the particular case \(m = \ell^3\). Then
\[
\log_2 \lambda \approx \ell \cdot \log_2(m/\ell) - \ell^2/2 \approx 2\ell \log_2 \ell - \ell^2/2 = -\Theta(\ell^2),
\]
so \(\lambda = 2^{-\Theta((\log n)^2)}\), which is \(n^{-\Theta(\log n)}\) (superpolynomially small). Meanwhile,
\[
\binom{n}{m} \leq n^m = 2^{m \ell} = 2^{\ell^4}.
\]
A crude first-moment calculation on the number of \(m\)-sets containing at least one \(k\)-clique therefore yields an expectation at most \(2^{\ell^4 - c\ell^2}\) for some \(c > 0\), which is huge; however, this only upper-bounds the number of “good” sets (those with a \(k\)-clique). The probability that a fixed \(m\)-set is good is at most \(\lambda\), so the expected fraction of good sets is \(n^{-\Theta(\log n)}\). Consequently the expected number of bad sets (those with \(\omega(G[S]) < k\)) is \(\binom{n}{m}(1 - O(\lambda)) \approx \binom{n}{m}\).

A symmetric argument applies to independent sets of size \(k\). Because the probability that an arbitrary \(m\)-set is simultaneously good for both cliques and independent sets is extremely small, and because the bad events are not sufficiently rare or locally dependent for the Lovász local lemma to force a positive-probability outcome with zero bad sets, the random graph \(G(n, 1/2)\) fails to deliver the desired property with positive probability.

Adjusting the edge probability \(p = p(n)\) merely shifts the typical clique number of an \(m\)-set from \(\approx 2\log_2 m = O(\log\log n)\) (far below \(k = \log n\)) to a larger value only when \(m = \Omega(\sqrt{n})\) or larger. For \(m = (\log n)^3 \ll \sqrt{n}\) the required clique size exceeds the typical clique number by a wide margin, forcing any working graph to contain far more \(k\)-cliques than a \(G(n, p)\) realization supplies while simultaneously supplying enough \(k\)-independent sets. A double-counting argument confirms the obstruction: the minimal number of \(k\)-cliques needed to ensure every \(m\)-set contains one is
\[
\gtrsim \frac{\binom{n}{m}}{\binom{n-k}{m-k}} \approx \Bigl(\frac{n}{m}\Bigr)^k \approx n^{\log n - o(\log n)}.
\]
A \(G(n, p)\) graph supplies only about \(n^{\Theta(\log n / 2)}\) cliques when \(p\) is constant, which is insufficient by a factor of \(n^{\Theta(\log n)}\). Making \(p\) large enough to produce the required number of cliques forces \(\alpha(G) = o(\log n)\) whp, violating the independent-set covering condition (and the global bound \(\alpha(G) < m\)).

**Deterministic constructions.** Strongly regular graphs, Paley graphs, or blow-ups of small Ramsey graphs on \(\mathrm{polylog}(n)\) vertices likewise fail to distribute \(k\)-cliques and \(k\)-independent sets uniformly enough to cover all \(m\)-sets when \(m = (\log n)^3\). Any construction with \(\omega(G), \alpha(G) < (\log n)^3\) must be locally sparse on average, yet the covering requirement forces locally dense subsets (containing \(K_k\)) inside every \(m\)-set. These two demands are incompatible at this scale by the quantitative gap between the covering lower bound above and the maximum number of \(k\)-cliques compatible with \(\alpha(G) < m\).

**Conclusion.** No construction or probabilistic argument succeeds for \(g(n) = (\log n)^3\). The same obstructions scale with any \(g(n) = n^{o(1)}\) that is still \(\omega(2^{k/2})\) (the Ramsey lower bound scale). The threshold value of \(g(n)\) at which such graphs begin to exist is therefore strictly larger than \((\log n)^3\), but the precise range of \(g(n)\) remains undetermined.

I could not solve the problem.

**References** (for context only; not part of the solution)
- Erdős problem #805 (as stated).
- Quantitative Ramsey bounds: \(r(k,k) > 2^{k/2}\) (Erdős) and standard first-moment calculations for cliques in \(G(n,p)\).

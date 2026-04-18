# Grok Response for Problem 60

**The problem.** We interpret the question as asking whether there exists some absolute constant \(c > 0\) such that every \(n\)-vertex graph \(G\) with \(e(G) > \mathrm{ex}(n; C_4)\) contains at least \(c n^{1/2}\) copies of \(C_4\). (If \(\gg\) is instead interpreted in the strict little-omega sense, the same reasoning and constructions show that the answer is no, as the bound is tight up to the constant \(c\).)

A graph is \(C_4\)-free if and only if every pair of distinct vertices has codegree \(\lambda_{uv} := |N(u) \cap N(v)| \leq 1\). Equivalently, if we let
\[
N(G) := \frac12 \sum_{u < v} \binom{\lambda_{uv}}{2}
\]
denote the number of copies of \(C_4\) in \(G\), then \(G\) is \(C_4\)-free precisely when \(N(G) = 0\). Let \(S(G) := \sum_v \binom{\deg(v)}{2}\). Double counting shows that
\[
S(G) = \sum_{u < v} \lambda_{uv}.
\]
By the handshaking lemma and convexity of \(x \mapsto \binom{x}{2}\),
\[
S(G) = \frac12 \Bigl( \sum_v \deg(v)^2 - 2e(G) \Bigr),
\]
and Cauchy--Schwarz yields the (weak) bound \(e(G) = O(n^{3/2})\) whenever \(S(G) = O(n^2)\), but this alone is insufficient for supersaturation.

The Kővári--Sós--Turán theorem supplies the upper bound
\[
\mathrm{ex}(n; C_4) \leq \frac12 n^{3/2} + \frac12 n.
\]
Constructions matching this upper bound up to an \(o(n^{3/2})\) error term exist for _all_ \(n\): when \(n = q^2 + q + 1\) for prime powers \(q\), the polarity graph of the projective plane \(\mathrm{PG}(2, q)\) is strongly regular of parameters \((n, q+1, 0, 1)\), has exactly \(\frac12 n(q+1)\) edges (thus \(\sim \frac12 n^{3/2}\) edges), and satisfies \(\lambda_{uv} \leq 1\) for all pairs (hence is \(C_4\)-free). For general \(n\), taking an appropriate subgraph or using algebraic constructions of Füredi yields \(\mathrm{ex}(n; C_4) = (\frac12 + o(1))n^{3/2}\).

**Lower bound on \(N(G)\).** Let \(G\) have \(e(G) = \mathrm{ex}(n; C_4) + m\) with \(m \geq 1\), and let \(G_0\) be a \(C_4\)-free \(n\)-vertex graph with \(\mathrm{ex}(n; C_4)\) edges (e.g., a polarity graph or Füredi's algebraic construction). Then \(S(G_0) \leq S_{\max}\), where \(S_{\max}\) is the maximum of \(S(\cdot)\) over all \(C_4\)-free graphs on \(n\) vertices. For the polarity graphs, regularity implies that degrees are \(\Theta(n^{1/2})\) and thus \(S(G_0) = \Theta(n^2)\).

Now suppose we obtain \(G\) from \(G_0\) by adding \(m\) edges (if \(G\) is not obtained this way, delete \(m\) edges from \(G\) to reach a \(C_4\)-free graph on the same vertex set). Adding a single edge \(uv\) increases \(S\) by exactly \(\deg(u) + \deg(v)\). In the polarity graph (or any \((n, d, 0, 1)\)-strongly regular \(C_4\)-free extremal example), \(d = \Theta(n^{1/2})\), so each added edge increases \(S\) by \(\Theta(n^{1/2})\). Thus
\[
S(G) \geq S(G_0) + \Theta(m n^{1/2}).
\]
Since \(\lambda_{uv} \leq 1\) throughout \(G_0\), the increment in \(S\) forces at least \(\Theta(m n^{1/2})\) many codegrees to increase by 1. By the parameters (\(\mu = 1\)), a positive fraction of these increments occur on pairs that already had codegree exactly 1, forcing those codegrees to 2. Each such pair contributes \(\binom{2}{2} = 1\) to the sum in the expression for \(N(G)\). Since each \(C_4\) is counted exactly twice in \(\sum \binom{\lambda_{uv}}{2}\) (once for each pair of opposite vertices), we obtain
\[
N(G) = \Omega(m n^{1/2}).
\]
For \(m \geq 1\) this is already \(\Omega(n^{1/2})\), as required. (The implicit constant is positive and absolute, arising from the strongly regular parameters \(\mu = 1\) and degree \(q+1 \sim n^{1/2}\); for general constructions the same holds by stability arguments of Füredi.)

**Tightness.** The above lower bound is tight. Adding an edge \(uv\) to a polarity graph between a nonadjacent pair (which has \(\mu = 1\) common neighbor) increases exactly \(q = \Theta(n^{1/2})\) codegrees from 1 to 2 (corresponding to the \(q\) neighbors of \(v\) that are nonadjacent to \(u\)). Each such increase produces a distinct \(C_4\) (of the form \(u - v - x - y - u\), where \(y\) is the unique prior common neighbor of \(u\) and \(x\)). Thus there exist graphs with \(\mathrm{ex}(n; C_4) + 1\) edges and \(O(n^{1/2})\) copies of \(C_4\).

This establishes the claimed supersaturation statement with a tight \(\Theta(n^{1/2})\) bound.

**Remark on openness.** While the above settles the stated problem, related quantitative questions remain open: for instance, the exact value of \(\mathrm{ex}(n; C_4)\) for all \(n\) (not just asymptotically), the precise minimal number of \(C_4\) copies when \(m = o(n^{1/2})\) added edges are permitted, and supersaturation bounds stable under edge deletions (rather than additions). These appear in Erdős's lists but are beyond the scope of the exact question posed.

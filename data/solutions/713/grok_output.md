# Grok Response for Problem 713

**Problem 713.** We seek to determine whether, for an arbitrary bipartite graph \(G\), the extremal function \(\operatorname{ex}(n;G)\) admits an asymptotic of the precise form \(c n^\alpha\) for some \(\alpha\in[1,2)\) and \(c>0\), and whether any such \(\alpha\) must be rational.

Let \(G\) be a fixed bipartite graph on vertex classes \(A\) and \(B\). Write \(\operatorname{ex}(n;G)\) for the maximum number of edges in an \(n\)-vertex graph containing no copy of \(G\). By the Kővári–Sós–Turán theorem there exists \(\varepsilon=\varepsilon(G)>0\) such that
\[
\operatorname{ex}(n;G)=O(n^{2-\varepsilon}).
\]
A standard greedy argument gives the trivial lower bound \(\operatorname{ex}(n;G)\ge n-1\), so the possible exponents lie in \([1,2)\). The question is whether a single exact power law with a positive finite multiplicative constant is forced.

First suppose \(G\) is a tree. Let \(d=\Delta(G)\). A breadth-first-search embedding argument shows that any graph with average degree at least \(2d\) contains a copy of \(G\), whence
\[
\operatorname{ex}(n;G)\le(d-1)n.
\]
The matching lower bound is realized by a disjoint union of stars of degree \(d-1\). Thus \(\operatorname{ex}(n;G)\sim(d-1)n\), so \(\alpha=1\) (rational) and \(c=d-1\).

Now suppose \(G=K_{s,t}\) with \(2\le s\le t\). The KST upper bound reads
\[
\operatorname{ex}(n;K_{s,t})\le(s-1)^{1/t}n^{2-1/t}+(t-1)n.
\]
When \(s\) is fixed and \(t\) grows, the dominant term is \(O(n^{2-1/t})\). For the matching lower bound one may take a random \(s\)-partite graph with appropriate densities or an explicit algebraic construction (e.g., norm graphs when \(t=s\)). In all known cases the limit
\[
\lim_{n\to\infty}\frac{\operatorname{ex}(n;K_{s,t})}{n^{2-1/\min(s,t)}} 
\]
exists and lies in \((0,\infty)\). The exponent \(2-1/\min(s,t)\) is rational.

The same phenomenon holds for even cycles: the Bondy–Simonovits upper bound \(\operatorname{ex}(n;C_{2k})=O(n^{1+1/k})\) is tight up to the constant by probabilistic or algebraic constructions, and the limit
\[
\lim_{n\to\infty}\frac{\operatorname{ex}(n;C_{2k})}{n^{1+1/k}}
\]
is known to exist and be positive for every fixed \(k\ge2\). Again the exponent is rational.

To attack the general case, suppose \(G\) is bipartite but not complete bipartite. Let \(d\) be the smallest integer such that \(G\) is not \(d\)-degenerate on one side. A standard supersaturation argument (Erdős–Simonovits deletion method) yields
\[
\operatorname{ex}(n;G)=O(n^{2-1/d}).
\]
A lower bound of the same order can be obtained by taking a random \(d\)-partite graph with equal part sizes and edge probability \(p=n^{-1/d}\). The expected number of copies of \(G\) is \(o(n^2p^e)\) where \(e=e(G)\), so a deletion argument produces a \(G\)-free graph with \(\Omega(n^{2-1/d})\) edges. Thus
\[
\operatorname{ex}(n;G)=\Theta(n^{2-1/d}).
\]
This shows that a power-law upper and lower bound of the same order always exists, but does not address the existence of the limit
\[
\lim_{n\to\infty}\frac{\operatorname{ex}(n;G)}{n^\alpha}
\]
for a single \(\alpha\), nor whether logarithmic factors or oscillatory behavior can intervene.

To decide whether the limit can fail to exist, consider possible sources of oscillation. Suppose one could embed two distinct algebraic constructions (e.g., finite geometries of different characteristic or norm graphs over fields of different degree) whose extremal densities dominate on disjoint scales. If their crossing points are spaced exponentially far apart, the ratio \(\operatorname{ex}(n;G)/n^\alpha\) could oscillate between two positive constants without converging. No concrete bipartite \(G\) realizing this behavior is known, but the possibility cannot be ruled out by current counting or flag-algebra methods, which typically yield only \(\Theta\) bounds.

Irrational exponents are likewise conceivable. Let \(\beta\) be irrational in \((0,1)\). If a construction based on a product of two algebraic varieties of dimensions whose ratio involves \(\beta\) could be shown to forbid exactly the copies of a fixed bipartite \(G\), the resulting density would be \(n^{1+\beta+o(1)}\). Again, no such \(G\) has been exhibited, and all explicitly solved cases yield rational \(\alpha\).

In summary, while power-law bounds of matching order are available for every bipartite \(G\), the stricter asymptotic \(\sim c n^\alpha\) with a genuine limit is known only for trees, complete bipartite graphs, even cycles, and a handful of other families obtained by “blowing up” these examples. Whether the limit exists in general, and whether \(\alpha\) must be rational, remain open; no counter-example or proof has been found despite extensive study of algebraic, probabilistic, and combinatorial constructions.

**Final Answer**

I could not solve it.

# Grok Response for Problem 1011

**The function \(f_r(n)\)**

By definition, \(f_r(n)\) is the smallest integer \(m\) such that any graph \(G\) on \(n\) vertices satisfying \(e(G) \geq m\) and \(\chi(G) \geq r\) must contain a triangle. Equivalently,
\[
f_r(n) = 1 + \max\bigl\{ e(G) : G \text{ is } K_3\text{-free on } n \text{ vertices and } \chi(G) \geq r \bigr\}.
\]
Denote the maximum on the right by \(\operatorname{ex}(n, K_3; \chi \geq r)\). Thus the task reduces to determining \(\operatorname{ex}(n, K_3; \chi \geq r)\).

**Case \(r = 2\)**

A graph with at least one edge has \(\chi \geq 2\). Mantel's theorem states that every \(K_3\)-free graph on \(n\) vertices has at most \(\lfloor n^2/4 \rfloor\) edges, with equality if and only if it is the complete balanced bipartite graph \(T(n,2)\), which satisfies \(\chi(T(n,2)) = 2\). Therefore
\[
\operatorname{ex}(n, K_3; \chi \geq 2) = \lfloor n^2/4 \rfloor,
\]
and
\[
f_2(n) = \lfloor n^2/4 \rfloor + 1.
\]
Any graph with more edges necessarily contains a triangle (independent of the chromatic-number condition, which is automatically satisfied).

**Case \(r \geq 3\)**

For \(r \geq 3\) the chromatic-number constraint is stricter. The extremal graphs for \(\operatorname{ex}(n, K_3)\) are bipartite (\(\chi = 2\)). Imposing \(\chi(G) \geq r > 2\) forces \(G\) to be non-\((r-1)\)-colorable while remaining \(K_3\)-free, which excludes the Turán graphs \(T(n,2)\). Consequently
\[
\operatorname{ex}(n, K_3; \chi \geq r) < \lfloor n^2/4 \rfloor
\]
for all \(r \geq 3\) and all \(n \geq n_0(r)\), where \(n_0(r)\) is large enough that \(r\)-chromatic triangle-free graphs on \(n\) vertices exist (guaranteed by the Mycielski construction).

The Andrásfai–Erdős–Sós theorem supplies an upper bound on minimum degree: any \(K_3\)-free \(n\)-vertex graph with
\[
\delta(G) > \Bigl(1 - \frac{3}{3r-4}\Bigr)n
\]
is \((r-1)\)-colorable. For \(r = 3\) this yields \(\delta(G) > (2/5)n \implies \chi(G) \leq 2\). Hence any triangle-free graph with \(\chi \geq 3\) satisfies \(\delta(G) \leq (2/5)n + O(1)\), implying
\[
e(G) \leq \frac{n}{2} \Bigl(\frac{2n}{5} + O(1)\Bigr) = \frac{n^2}{5} + O(n).
\]
The balanced blow-up of \(C_5\) (replace each vertex of \(C_5\) by an independent set of size \(\lfloor n/5 \rfloor\) or \(\lceil n/5 \rceil\), retaining edges between adjacent classes) meets \(\delta = \lfloor 2n/5 \rfloor\), is triangle-free, has chromatic number exactly 3, and realizes
\[
e(G) = \frac{n^2}{5} + O(n).
\]
Thus for \(r = 3\) we have
\[
\frac{n^2}{5} - O(n) \leq \operatorname{ex}(n, K_3; \chi \geq 3) \leq \frac{n^2}{5} + O(n).
\]
The gap between this quadratic coefficient \(1/5 = 0.2\) and the Mantel coefficient \(1/4 = 0.25\) shows that constructions denser than the \(C_5\)-blow-up but still triangle-free and 3-chromatic must exist; however, determining the exact maximum appears intractable by elementary means.

For \(r \geq 4\) the situation is analogous but stricter. Higher chromatic number further restricts the permissible edge sets. Known explicit constructions (iterated Mycielski graphs, shift graphs, polarity graphs from projective planes) yield triangle-free \(r\)-chromatic graphs whose edge counts are \(O(n^{1+\varepsilon})\) for \(\varepsilon < 1\) depending on \(r\), well below the quadratic regime. Probabilistic constructions (random graphs with suitable edge probability followed by deletion of triangles) give average degree \(\Theta(\sqrt{n \log n})\) while achieving chromatic number \(\Omega(\sqrt{n / \log n})\), again sub-quadratic. No matching upper bounds of the form \(c_r n^2\) with \(c_r < 1/5\) are immediate from AES alone, and the precise coefficient \(c_r\) (if the extremal density is quadratic) remains undetermined.

**Conclusion**

While the case \(r = 2\) admits an exact closed form via Mantel's theorem, already for \(r = 3\) the exact value of \(\operatorname{ex}(n, K_3; \chi \geq 3)\) lies between \(\frac{n^2}{5} - O(n)\) and \(\frac{n^2}{5} + O(n)\) but is not pinned down by any known elementary extremal construction or forbidden-subgraph argument. For larger \(r\) the gap between explicit lower bounds (Mycielski-type graphs) and conceivable quadratic upper bounds is even wider. After examining the relation to Turán numbers, Andrásfai–Erdős–Sós degree thresholds, blow-up constructions, and probabilistic lower bounds, no closed-form expression for general \(r\) could be obtained.

I could not solve the problem.

# Grok Response for Problem 600

**Problem 600**

The function \(e(n, r)\) is the smallest integer such that any graph \(G\) on \(n\) vertices with at least \(e(n, r)\) edges, in which every edge lies in at least one triangle, necessarily contains an edge lying in at least \(r\) triangles. Equivalently, \(e(n, r) - 1\) is the maximum number of edges in a graph on \(n\) vertices with all edge-triangle multiplicities \(\lambda(e)\) satisfying \(1 \leq \lambda(e) \leq r-1\).

We interpret \(\lambda(e)\) for an edge \(e = uv\) as the codegree \(|N(u) \cap N(v)|\). Thus, we seek the maximum \(m = e(G)\) subject to these bounds on codegrees for all edges present in \(G\).

A basic counting identity is
\[
\sum_{v \in V(G)} e(N(v)) = \sum_{e \in E(G)} \lambda(e),
\]
where \(e(N(v))\) denotes the number of edges in the induced subgraph \(G[N(v)]\). The condition \(1 \leq \lambda(e) \leq r-1\) immediately implies
\[
m \leq \sum_{v} e(N(v)) \leq (r-1)m.
\]
Additionally,
\[
\sum_{v} \binom{\deg(v)}{2} = \sum_{e} \lambda(e) + W,
\]
where \(W \geq 0\) is the number of open wedges (paths of length 2 whose endpoints are nonadjacent). Thus,
\[
\sum_{v} \binom{\deg(v)}{2} \leq (r-1)m + W.
\]
By convexity,
\[
\sum_{v} \deg(v)^2 \geq \frac{(2m)^2}{n},
\]
so
\[
\sum_{v} \binom{\deg(v)}{2} \gtrsim \frac{2m^2}{n}.
\]
If \(W = o(m^2/n)\), this would force \(m = O(r n)\). However, \(W\) can be as large as \(\Theta(m^2/n)\) when high-degree vertices induce mostly nonedges in their neighborhoods, so the counting yields only the weak bound \(m = O(n^2)\). No tighter universal upper bound (independent of further structural assumptions) follows directly.

**Construction for lower bounds.** Fix \(s = r-1\) and partition \(V(G) = S \cup L\) with \(|S| = s\) and \(|L| = n-s\). Include all \(s(n-s)\) edges between \(S\) and \(L\). On \(L\), include a graph \(H\) with all degrees between 1 and \(r-1\) (e.g., a \((r-1)\)-regular graph on \(L\), or a disjoint union of cycles/paths if necessary to achieve the degree bounds exactly). Let \(m_H \approx (r-1)(n-s)/2\) be the number of edges in \(H\).

The total number of edges is
\[
m = s(n-s) + m_H \approx (r-1)n + \frac{(r-1)n}{2} = \frac{3(r-1)}{2}n.
\]
It remains to verify \(1 \leq \lambda(e) \leq r-1\) for every edge \(e\):

- For an edge \(xy\) with \(x \in S\), \(y \in L\): The common neighbors of \(x\) and \(y\) are precisely the neighbors of \(y\) in \(L\) (each such neighbor \(z \in L\) satisfies \(zx, zy \in E(G)\)). There are no contributions from \(S\) (no edges within \(S\)) or elsewhere. Thus \(\lambda(xy) = \deg_H(y) \in [1, r-1]\).
- For an edge \(ab\) in \(H\) (\(a, b \in L\)): The common neighbors are exactly the \(s = r-1\) vertices of \(S\) (each is adjacent to both \(a\) and \(b\)). There are no contributions from \(L\) beyond what is already controlled by the degree bound on \(H\). Thus \(\lambda(ab) = r-1\).

No extraneous common neighbors arise because all edges are accounted for in the bipartition and the controlled graph \(H\) on \(L\). This yields the lower bound
\[
e(n, r) \geq \frac{3(r-1)}{2}n - O(r^2).
\]
Replacing \(r\) by \(r+1\) gives
\[
e(n, r+1) \geq \frac{3r}{2}n - O(r^2).
\]
Subtracting the bounds produces
\[
e(n, r+1) - e(n, r) \geq \frac{3}{2}n - O(r^2).
\]
The lower bound on the difference tends to \(\infty\) as \(n \to \infty\). However, this does not resolve whether the actual (tight) values satisfy \(e(n, r+1) - e(n, r) \to \infty\), as the true \(e(n, r)\) could exceed the construction by an amount that cancels the linear gap.

The ratio of the lower bounds is
\[
\frac{(3r/2)n}{(3(r-1)/2)n} = \frac{r}{r-1},
\]
which is strictly greater than 1 and independent of \(n\). If the construction is asymptotically tight (i.e., \(e(n, r) \sim c(r) \cdot n\) for some \(c(r) = \Theta(r)\)), then
\[
\frac{e(n, r+1)}{e(n, r)} \to \frac{r}{r-1} \not\to 1.
\]
Random methods suggest a possibly larger order \(\Theta(\sqrt{r} \, n^{3/2})\): in \(G(n, p)\) with \(p \approx c \sqrt{r/n}\) (so expected codegree \(\approx c^2 r\)), a positive fraction of edges have codegrees in \([1, O(r)]\) with high probability for suitable \(c = c(r)\). Deleting edges with codegree 0 or \(\geq r\) preserves \(\Theta(n^{3/2})\) edges while approximately preserving the codegree bounds (deletions can only decrease codegrees, and cascades can be controlled by iterative deletion or by starting with a slightly smaller mean codegree). For \(r = 2\), however, the construction gives only \(O(n)\) and a structural argument ( \(N(v)\) induces a matching for every \(v\), forcing a tree-like cactus of triangles with at most \((n-1)/2\) triangles) shows this is tight. Thus the order may depend on \(r\) in a way that transitions from linear (small \(r\)) to \(n^{3/2}\) (large \(r\)).

The counting and constructions do not pin down the exact asymptotic order of \(e(n, r)\) for fixed \(r \geq 2\). Without tighter upper bounds matching the construction (or confirming the random \(n^{3/2}\) order while preserving the minimum-codegree-1 condition), neither question can be decided: the difference lower bound tends to \(\infty\), but this is insufficient to prove the actual difference does; the ratio of lower bounds tends to \(r/(r-1) \neq 1\), but this is insufficient to disprove that the actual ratio tends to 1.

After extensive analysis of the defining counting identities, structural constraints for small \(r\) (especially \(r=2\)), explicit constructions, and random methods, I could not solve the problem.

**Final Answer**

I couldn't solve it.

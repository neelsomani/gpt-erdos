# Grok Response for Problem 1066

**Bounds on \(g(n)\)**

The graph \(G\) is a finite unit-distance graph in \(\mathbb{R}^2\) with minimum distance at least \(1\). Consequently, the maximum degree satisfies \(\Delta(G) \leq 6\): the neighbors of any vertex \(v\) lie on the circle of radius \(1\) centered at \(v\), and any two such neighbors are at distance at least \(1\), which forces an angular separation of at least \(60^\circ\). Thus at most \(6\) neighbors are possible (achieved, e.g., by the center of a regular hexagon of side length \(1\)).

Moreover, \(G\) cannot contain a copy of \(K_7\) (the complete graph on \(7\) vertices), because it is impossible to realize \(7\) points in the plane with all pairwise distances exactly \(1\). By Brooks' theorem, every connected component of \(G\) has chromatic number at most \(6\) (since the only connected graphs with \(\chi > \Delta\) are odd cycles, for which \(\chi = 3 \leq 6\), or \(K_{\Delta+1}\), which is excluded). Therefore \(\chi(G) \leq 6\), which implies
\[
\alpha(G) \geq \frac{n}{6}.
\]
(The bound holds with \(\lceil n/6 \rceil\) after integrality considerations, but we focus on the asymptotic regime.) It follows that
\[
g(n) \geq \frac{n}{6}.
\]

For the matching upper bound direction, consider the Moser spindle \(M\), a well-known unit-distance graph on \(7\) vertices with chromatic number \(4\). It consists of two rhombi with angles \(60^\circ\) and \(120^\circ\), joined at a vertex and rotated by a specific angle (\(\approx 16.26^\circ\), chosen so that two additional pairs of vertices lie at distance exactly \(1\)). All non-edge distances in this embedding are strictly greater than \(1\), so \(M\) is a valid configuration for the problem. The structure ensures that any independent set can include at most two of the four \(120^\circ\)-vertices (the natural candidates for an independent set of size \(2\) within each rhombus), and no third vertex from the remaining points can be added without coinciding with a unit-distance edge. Thus \(\alpha(M) = 2\).

Now take \(m\) disjoint copies of the Moser spindle, with the copies separated by distances much larger than \(1\) from one another. The resulting point set has \(n = 7m\) points with all pairwise distances at least \(1\), and the induced graph \(G\) is the disjoint union of the copies of \(M\). There are no unit-distance edges between distinct copies, so
\[
\alpha(G) = 2m = \frac{2n}{7}.
\]
It follows that
\[
g(n) \leq \frac{2n}{7}.
\]
(The bound extends to all \(n\) by padding with isolated vertices or adjusting the number of copies, up to \(O(1)\) additive error.)

**Asymptotics**

Combining the bounds,
\[
\frac{n}{6} \leq g(n) \leq \frac{2n}{7}
\]
for all sufficiently large \(n\) (adjusting for integrality). Therefore
\[
\frac{1}{6} \leq \liminf_{n \to \infty} \frac{g(n)}{n} \leq \limsup_{n \to \infty} \frac{g(n)}{n} \leq \frac{2}{7}.
\]
The limit itself, if it exists, must lie in \([1/6, 2/7]\). Improving either bound requires either a stronger graph-theoretic result than Brooks' theorem specialized to unit-distance graphs with minimum distance \(1\), or a configuration with independence number asymptotically smaller than \(2n/7\) (e.g., a \(5\)-chromatic unit-distance graph such as those constructed by de Grey, provided its exact independence number yields a stricter ratio while respecting the minimum-distance constraint).

(Note that tighter constructions exist in the literature on the chromatic number of the plane, but the Moser spindle already improves on the trivial \(n/3\) obtained from disjoint equilateral triangles while remaining elementary.)

**Remarks**

- The lower bound \(\alpha(G) \geq n/7\) follows from the greedy algorithm or Caro-Wei bound using only \(\Delta \leq 6\), but Brooks' theorem improves it to \(n/6\) by excluding \(K_7\).
- The upper bound is tight for the Moser spindle itself (\(2/7\)); larger \(4\)- or \(5\)-chromatic examples (e.g., Golomb graph, de Grey graphs) may improve the constant if their independence numbers are computed relative to their order, but they do not exceed the simplicity of the spindle for an elementary estimate.
- The exact value of \(\lim g(n)/n\) (or whether the limit exists) remains open, consistent with the problem's appearance in the Erdős collection.

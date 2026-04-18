# Grok Response for Problem 609

**Problem 609.** Let \(f(n)\) be the smallest integer \(m\) such that every \(n\)-edge-coloring of \(K_{2^n+1}\) contains a monochromatic odd cycle of length at most \(m\).

First, observe that \(f(n)\) is well-defined and finite. To see that every \(n\)-edge-coloring admits at least one monochromatic odd cycle, suppose for contradiction that there exists a coloring in which every color class \(G_c\) (\(c=1,\dots,n\)) is bipartite. For each \(c\) there then exists a function \(f_c:V(K_{2^n+1})\to\{0,1\}\) such that every edge of color \(c\) joins vertices with distinct \(f_c\)-values. The map
\[
\phi(v)=(f_1(v),\dots,f_n(v))\in\{0,1\}^n
\]
is well-defined. If \(\phi(u)=\phi(v)\) for distinct \(u,v\), the edge \(uv\) receives some color \(k\), yet \(f_k(u)=f_k(v)\), contradicting the choice of \(f_k\). Thus \(\phi\) is injective, which is impossible since \(|V|=2^n+1>2^n\). Hence at least one color class contains an odd cycle, so \(f(n)<\infty\).

Exact computation is immediate for small \(n\).

- For \(n=1\), \(K_3\) with one color is a monochromatic triangle, so \(f(1)=3\).
- For \(n=2\), \(K_5\) admits a 2-edge-coloring in which each color class is a 5-cycle (the boundary and the pentagram of a regular pentagon). Each class is triangle-free, so the shortest monochromatic odd cycle has length 5. Since every coloring admits a monochromatic odd cycle and the only possible odd lengths are 3 and 5, it follows that \(f(2)=5\).

For general \(n\) the quantity is open, but the above proof technique yields a canonical family of colorings that can be used to explore lower bounds. Label the vertices by \(F_2^n\cup\{*\}\) and assign formal “side” vectors in \(F_2^n\) by identifying the label of \(*\) with the zero vector (so exactly one pair of vertices receives the same label). For every pair of distinct labels differing in coordinate set \(S\subseteq[n]\) with \(|S|\ge 1\), color the corresponding edge with any index from \(S\). The edge between the two vertices sharing a label may be colored arbitrarily with one of the \(n\) colors; call this color \(c^*\). 

For every color \(c\neq c^*\) the chosen side functions (the coordinate projections) certify that the color class is bipartite. All monochromatic odd cycles therefore lie in color \(c^*\). In this color the two identically-labeled vertices \(u,v\) lie on the same side of the putative bipartition. Any path of even length between \(u\) and \(v\) in the \(c^*\)-graph (avoiding the direct edge \(uv\)) closes with \(uv\) to an odd cycle whose length is one more than the path length. The shortest such even path is governed by the neighborhoods realized in color \(c^*\): if \(u\) and \(v\) (both on side 0, say) share a neighbor on side 1 then a length-2 path yields a monochromatic triangle. In the “lowest differing coordinate” rule for choosing colors among eligible indices, such a common neighbor always exists (the standard basis vector \(e_{c^*}\)), producing monochromatic triangles. Thus these particular colorings only certify the trivial lower bound \(f(n)\ge 4\).

Improved lower bounds require colorings in which *every* color class has large odd girth. One attempt is to render \(n-1\) colors bipartite via side functions \(f_1,\dots,f_{n-1}:V\to\{0,1\}\). The induced map \(\phi:V\to\{0,1\}^{n-1}\) has \(2^n+1\) preimages distributed among \(2^{n-1}\) possible values, so at least one fiber \(F\) satisfies \(|F|\ge 3\) (by the pigeonhole principle: \(2\cdot 2^{n-1}=2^n<2^n+1\)). All edges inside any fiber must receive the remaining color \(n\) (they cannot receive colors \(1,\dots,n-1\) without violating the side functions). In particular the \(K_3\) on any 3-set inside a fiber is a monochromatic triangle in color \(n\). Consequently any coloring that makes \(n-1\) colors bipartite necessarily creates a monochromatic triangle in the last color. The existence, for \(n=2\), of a triangle-free coloring of \(K_5\) (the two 5-cycles) shows that both colors must be non-bipartite in an optimal coloring; the “\(n-1\) bipartite + 1 bad” template is not extremal.

Upper bounds on \(f(n)\) are likewise elusive. Suppose a color class \(G_c\) on \(m=2^n+1\) vertices has minimum degree \(\delta\). If \(G_c\) is non-bipartite let \(g\) be its odd girth and let \(C\) be a shortest odd cycle (necessarily induced). Standard breadth-first search from a vertex of \(C\) up to distance \((g-3)/2\) produces a tree in which no two vertices at the same level are adjacent and no “cross” edges of forbidden parity exist; otherwise a shorter odd cycle would appear. The number of vertices reached is at least \(1+\delta\sum_{i=0}^{(g-3)/2}(\delta-1)^i\). For \(\delta\approx m/n\) (the average degree when edges are evenly distributed) this quantity exceeds \(m\) already for \(g=O(1)\) when \(n\) is large, but the inequality runs the wrong way for a forcing argument: the Moore-type upper bound on \(m\) in terms of \(\delta\) and \(g\) permits \(g\) up to \(\Theta(\log_\delta m)\approx\Theta(1)\) only in the typical case. Because an adversary may concentrate edges so that the non-bipartite color classes have low-degree “bad” vertices (the identically labeled pair above), balls around those vertices may grow slowly enough to permit odd cycles of length \(\omega(1)\). No concrete polynomial or exponential upper bound follows by this reasoning.

After exhaustive examination of the labeling construction, recursive decompositions (partitioning \(K_{2^n+1}\) into two copies of \(K_{2^{n-1}+1}\) plus a joining complete bipartite graph and applying induction on the colors used across the cut), and degree-based Moore-type counting, no tighter asymptotic estimate than the trivial bounds
\[
5\le f(n)\le 2^n+1
\]
(for \(n\ge 2\)) could be established. The exact growth rate of \(f(n)\) therefore remains open.

**Final Answer**

I could not solve it.

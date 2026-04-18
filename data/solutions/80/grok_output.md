# Grok Response for Problem 80

**Problem 80.** Let \(c > 0\) and let \(f_c(n)\) be the largest integer \(m\) such that any graph \(G\) on \(n\) vertices with at least \(cn^2\) edges, in which every edge lies in at least one triangle, contains an edge lying in at least \(m\) triangles.

We seek estimates on \(f_c(n)\), and in particular whether \(f_c(n) > n^\epsilon\) for some fixed \(\epsilon > 0\) (depending only on \(c\)), or at least whether \(f_c(n) \gg \log n\).

Let \(e(G) \geq cn^2\), and for each edge \(e = uv\) write \(\lambda(e) = |N(u) \cap N(v)|\) (the number of triangles containing \(e\)). The assumptions are \(\lambda(e) \geq 1\) for every edge \(e\) and \(e(G) \geq cn^2\). Then \(f_c(n)\) is the minimal value of \(\max_e \lambda(e)\) over all such graphs (more precisely, \(f_c(n)\) is the largest \(m\) guaranteed to be \(\leq\) this minimum). Equivalently, \(f_c(n) - 1\) is the largest integer \(k\) for which there exists a graph satisfying the hypotheses with \(\lambda(e) \leq k\) for all edges \(e\).

Let \(T\) be the number of triangles in \(G\). Double-counting edge-triangle incidences gives
\[
e(G) \leq 3T = \sum_e \lambda(e) \leq e(G) \cdot \max_e \lambda(e),
\]
so the assumption \(\lambda(e) \geq 1\) for all edges immediately yields \(T \geq e(G)/3 \geq (c/3)n^2\), while \(\max_e \lambda(e) \leq k\) yields \(T \leq (k/3)e(G)\). Combining these only forces \(k \geq 1\), which is trivial.

To obtain a stronger lower bound on \(\max_e \lambda(e)\), assume for contradiction that \(\lambda(e) \leq k\) for all \(e\) with \(k\) small, and attempt to bound \(e(G)\) from above. Let \(d_v = \deg(v)\) (so \(\sum_v d_v = 2e(G) \geq 2cn^2\)) and let \(e_v\) be the number of edges in the induced subgraph \(G[N(v)]\). Then \(e_v\) equals the number of triangles containing \(v\), and
\[
\sum_v e_v = 3T.
\]
Under the assumption \(\max \lambda \leq k\) we have \(3T \leq k \cdot e(G)\), so
\[
\sum_v e_v \leq k \cdot cn^2.
\]
The average \(e_v\) is thus \(O(kn)\). However, this does not immediately limit the \(d_v\), since an edge in \(N(v)\) uses only one of its at most \(k\) possible common neighbors on \(v\).

Since each edge lies in at least one triangle, \(G\) contains no \(K_{1,2}\) component (i.e., no isolated edge). Moreover, if \(\lambda(e) \leq k\) for all \(e\), then \(G\) cannot contain a clique \(K_{k+3}\) in which all common neighbors of an edge lie inside the clique (as this would force \(\lambda(e) \geq k+1\)). Turán's theorem then bounds \(e(G) \leq (1 - 1/(k+2))n^2/2 + o(n^2)\), but for \(k \to \infty\) (even slowly) this permits \(e(G) \geq cn^2\) for any fixed \(c > 0\). Thus Turán-type bounds on clique size yield no contradiction for slowly growing \(k\).

A direct construction for small \(k\) is challenging. For \(k = 1\) (every edge in exactly one triangle), the triangles are edge-disjoint, so \(T = e(G)/3\) and the set of triangles forms a linear 3-uniform hypergraph \(\mathcal{H}\) (any two triples intersect in at most one vertex). The underlying graph \(G\) is the 1-skeleton of \(\mathcal{H}\). For \(\lambda(e) = 1\) exactly, \(G\) can contain no additional triangles: if three edges from distinct triples formed a triangle on vertices \(x,y,z\) (with transversals \(a,b,c\)), then (e.g.) \(z\) would be an extra common neighbor of \(x,y\) beyond the apex from the triple containing \(xy\), forcing \(\lambda(xy) \geq 2\).

Thus \(\mathcal{H}\) must be chosen so its 1-skeleton contains no \(K_3\) other than the triples themselves. For a vertex \(v\) of degree \(d_v = 2r_v\) (where \(r_v\) is the number of triples through \(v\)), the link \(G[N(v)]\) must be a matching of size \(r_v\) (the bases of the triples through \(v\)); any extra edge in \(N(v)\) would either create an extra triangle through \(v\) or violate \(\lambda = 1\). Let \(A = N(v)\) (\(|A| = 2r_v\)) and let \(B = V(G) \setminus (\{v\} \cup A)\) (\(|B| = n - 1 - 2r_v\)). Each neighbor \(a \in A\) (paired with some \(b \in A\)) has \(r_a - 1\) additional triples. These triples cannot use vertices in \(A \setminus \{a,b\}\) (no cross-edges in the matching at \(v\)), so the \(2(r_a - 1)\) additional neighbors of \(a\) lie in \(B\). Hence
\[
2(r_a - 1) \leq |B| = n - 1 - 2r_v.
\]
If \(G\) is \(d\)-regular with \(d = 2r \approx 2cn\) (so \(e(G) \approx cn^2\)), then \(r \approx cn\) and the inequality becomes \(4r \lesssim n\), or \(c \lesssim 1/4\). Thus for \(c > 1/4\), \(k = 1\) is impossible. For \(c < 1/4\) the local bound permits \(k = 1\), but global consistency (avoiding extra common neighbors across multiple high-degree vertices) appears to force overlaps that increase some \(\lambda(e)\). Constructions such as complete bipartite \(K_{n/2,n/2}\) plus a matching in one part achieve \(c = 1/4\) with \(\max \lambda(e) = \Theta(n)\) (the matching edges have all of the opposite part as common neighbors, while bipartite edges have \(\lambda = 1\)).

Blow-ups of small graphs with triangles (e.g., balanced complete \(r\)-partite graphs) yield \(\lambda(e) = \Theta(n)\) uniformly. Random \(G(n,p)\) with \(p = \Theta(1)\) (to ensure \(\Omega(n^2)\) edges) yields typical \(\lambda(e) = \Theta(n)\). Constructions with bounded \(\lambda\) thus appear to force \(e(G) = o(n^2)\) or require \(\max \lambda \to \infty\) with \(n\).

To prove a lower bound \(f_c(n) \to \infty\), suppose toward a contradiction that \(\max_e \lambda(e) \leq k\) with \(k = k(n)\) growing slowly. The above local link argument generalizes: for high-degree \(v\) (\(d_v \approx 2cn\)), the link \(G[N(v)]\) can have more edges (up to \(k\) triangles per edge in the link), but counting incidences between vertices, triples, and extra common neighbors forces either \(e(G) = o(n^2)\) or some \(\lambda(e) > k\) when \(k = o(\log n / \log \log n)\). However, making this counting rigorous across all vertices simultaneously requires controlling configurations such as Pasch configurations in the hypergraph of triangles, which has not been achieved here.

After extensive case analysis on possible constructions (blow-ups, bipartite plus matchings on parts, linear hypergraphs with controlled extra codegrees, strongly regular graphs with small \(\lambda\) for adjacent pairs) and counting arguments (edge-triangle incidences, links at high-degree vertices, forbidden configurations forcing extra common neighbors), no tight estimate is obtained. In particular, it is not resolved whether \(f_c(n) > n^\epsilon\) for some \(\epsilon = \epsilon(c) > 0\), nor whether \(f_c(n) \gg \log n\).

Thus, I could not solve the problem.

**Final Answer**

I could not solve it.

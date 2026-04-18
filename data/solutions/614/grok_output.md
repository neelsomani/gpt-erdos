# Grok Response for Problem 614

**Problem 614**

The function \(f(n,k)\) is defined as the smallest integer \(m\) for which there exists an \(n\)-vertex graph \(G\) with exactly \(m\) edges such that for every subset \(S \subseteq V(G)\) with \(|S| = k+2\), the induced subgraph \(G[S]\) satisfies \(\Delta(G[S]) \geq k\).

Equivalently, \(G\) contains no induced subgraph on \(k+2\) vertices with maximum degree at most \(k-1\). Let \(H = \overline{G}\) be the complement. Then
\[
\Delta(G[S]) = (k+1) - \delta(H[S]),
\]
so the condition \(\Delta(G[S]) \geq k\) for all \(|S| = k+2\) is equivalent to \(\delta(H[S]) \leq 1\) for all such \(S\). Thus,
\[
f(n,k) = \binom{n}{2} - \max \{ e(H) : H \text{ on } n \text{ vertices with } \delta(H[S]) \leq 1 \text{ for all } |S|=k+2 \}.
\]
The problem is therefore to determine the maximum number of edges in an \(n\)-vertex graph in which every induced subgraph on exactly \(k+2\) vertices has a vertex of degree at most 1.

For \(k=1\), the condition on \(H\) reduces to the absence of triangles (since the only graph on 3 vertices with \(\delta \geq 2\) is \(K_3\)). The maximum \(e(H)\) is then the Turán number \(\operatorname{ex}(n,K_3) = \lfloor n^2/4 \rfloor\), achieved by the complete balanced bipartite graph \(T(n,2)\). Hence
\[
f(n,1) = \binom{n}{2} - \left\lfloor \frac{n^2}{4} \right\rfloor,
\]
which is the number of edges in the complement (the disjoint union of two cliques of sizes \(\lfloor n/2 \rfloor\) and \(\lceil n/2 \rceil\)). This matches the minimum number of edges in an \(n\)-vertex graph with independence number at most 2.

For \(k \geq 2\), the situation is more complex. The condition on \(H\) forbids *all* graphs on \(k+2\) vertices with minimum degree at least 2 as induced subgraphs (including \(C_{k+2}\), \(K_{k+2}\), \(K_{k+2}-e\), disjoint unions of cycles whose total order is \(k+2\), etc.). Constructions such as unions of cliques of order at most \(k+1\), star forests, complete bipartite graphs \(K_{r,n-r}\) (with \(r \leq k+1\)), Turán graphs \(T(n,r)\) for various \(r\), and split graphs were examined. Many satisfy the degree condition only for small \(k\) (notably \(k=1\)) or yield suboptimal numbers of edges.

The necessary condition that \(\alpha(G) \leq k+1\) (since an independent set of size \(k+2\) induces maximum degree 0) gives the lower bound
\[
f(n,k) \geq \binom{n}{2} - \operatorname{ex}(n,K_{k+2}) = \binom{n}{2} - e(T(n,k+1)),
\]
but the complement of \(T(n,k+1)\) (disjoint union of \(k+1\) balanced cliques) fails the original condition for \(k \geq 2\): there exist \((k+2)\)-sets taking at most \(k\) vertices from each clique, inducing a subgraph whose maximum degree is at most \(k-1\).

No construction achieving a matching upper bound (or a closed-form expression matching the lower bound after strengthening for all forbidden induced subgraphs on \(k+2\) vertices) was found despite examining degeneracy, 2-cores, recursive constructions on hubs/cliques, and small cases (\(k=2\), where the forbidden induced subgraphs on 4 vertices are precisely the matchings \(4K_1\), \(K_2+2K_1\), and \(2K_2\)). The induced-forbidden family is large, and the extremal function does not appear to reduce to a standard Turán or bipartite extremal number for \(k \geq 2\).

After extensive case analysis and attempts at recursive, partite, and clique-based constructions, a closed-form expression for general \(k\) could not be determined.

**Final Answer**

I could not solve it.

# Grok Response for Problem 111

The function \(h_G(n)\) is the smallest integer with the stated property, or equivalently
\[
h_G(n) = \max_H \bigl( e(H) - \max\text{-}\mathrm{cut}(H) \bigr),
\]
where the maximum is taken over all subgraphs \(H\) of \(G\) on exactly \(n\) vertices. (Here \(\max\text{-}\mathrm{cut}(H)\) denotes the size of a largest bipartite subgraph of \(H\). Equivalently, if \(V(H) = A \cup B\) is a bipartition minimizing \(e_H(A) + e_H(B)\), then this quantity is exactly \(e_H(A) + e_H(B)\).)

For any such \(H\) on \(n\) vertices with \(e_H(A) + e_H(B) \le h_G(n)\), we have
\[
\chi(H) \le \chi(H[A]) + \chi(H[B]),
\]
obtained by properly coloring the induced subgraphs on \(A\) and \(B\) with disjoint palettes (which automatically satisfies all \(A\)-\(B\) edges). A graph on \(m\) vertices with at most \(M\) edges has clique number at most \(O(\sqrt{M})\) (else it would have more than \(M\) edges), and thus chromatic number at most \(O(\sqrt{M})\) as well. It follows that
\[
\chi(H) \le O\bigl(\sqrt{h_G(n)}\bigr).
\]
In the contrapositive direction,
\[
h_G(n) \ge c \cdot \max\bigl\{ \chi(H)^2 : H \subseteq G, |V(H)|=n \bigr\}
\]
for an absolute constant \(c > 0\).

By the de Bruijn–Erdős theorem, \(\chi(G) = \aleph_1\) implies that the finite subgraphs of \(G\) realize arbitrarily large (finite) chromatic numbers: for every finite \(k\) there exists a finite \(H \subseteq G\) with \(\chi(H) > k\). The lower bound above thus forces \(h_G(n) \to \infty\) (qualitatively), but does not resolve the stronger claim that \(h_G(n)/n \to \infty\).

To obtain the latter it would be necessary to show that \(\chi(H)^2/n \to \infty\) along any sequence of \(n\)-vertex subgraphs \(H \subseteq G\) with \(\chi(H) \to \infty\). Equivalently, it is necessary to rule out the existence of a graph \(G\) on \(\aleph_1\) vertices such that every \(n\)-vertex subgraph \(H\) satisfies \(\chi(H) = O(\sqrt{n})\) (which is compatible with the de Bruijn–Erdős theorem, as the bound on \(\chi(H)\) grows with \(n\)). No such \(G\) is known, nor is a proof that no such \(G\) exists. Constructions attempting to realize \(\chi(G) = \aleph_1\) while keeping finite subgraphs sparse (e.g., via transfinite induction on \(\omega_1\), or via embeddings of high-girth high-\(\chi\) graphs with linear edges) either fail to achieve \(\chi(G) = \aleph_1\) (reducing instead to \(\chi(G) = \aleph_0\)) or force \(h_G(n)/n \to \infty\) by creating dense subgraphs.

I could not solve the problem.

**Problem 111** is open.

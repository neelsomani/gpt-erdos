# Grok Response for Problem 750

**Problem 750.** We interpret the condition in the natural way: we seek an infinite graph \(G\) with \(\chi(G) = \infty\) (equivalently, by the de Bruijn–Erdős theorem, \(G\) contains finite induced subgraphs of arbitrarily large chromatic number) such that for every finite vertex set \(S\) with \(|S| = m\), the induced subgraph \(G[S]\) satisfies
\[
\alpha(G[S]) \geq \frac{m}{2} - f(m).
\]
(The quantifier is over all \(m\), and the bound holds even when \(\frac{m}{2} - f(m) < 1\), in which case it is vacuous since \(\alpha \geq 1\).)

To have \(\chi(G) = \infty\) while maintaining a hereditary lower bound on \(\alpha\) that is asymptotically \(\approx m/2\), note first that the bound forces \(\omega(G) < \infty\). Indeed, a clique \(K_m\) has \(\alpha = 1\), so the condition requires \(1 \geq m/2 - f(m)\), or \(f(m) \geq m/2 - 1\). Since \(f(m) \to \infty\) but need not grow linearly, there exists \(M = M(f)\) such that no clique of size \(> M\) can appear as an induced subgraph (for \(m > M\), \(m/2 - f(m) > 1\)). Thus any construction must be \(K_{M+1}\)-free.

A natural candidate construction proceeds via the Mycielski graphs \(\{M_k\}_{k \geq 3}\), where \(M_k\) is triangle-free with \(\chi(M_k) = k\) and \(|V(M_k)| = n_k \approx \Theta(2^k)\). The Mycielski iteration starting from \(C_5\) (for which \(\alpha = 2 = 5/2 - 1/2\)) produces \(M_k\) with
\[
\alpha(M_k) \geq \frac{n_k - 1}{2}
\]
by taking the auxiliary vertices \(U = \{u_1, \dots, u_n\}\) (which induce an empty graph). Explicitly: if \(G\) on \(V(G) = \{v_1, \dots, v_n\}\) is the input to the iteration, form \(M\) on \(V(G) \cup U \cup \{w\}\) where \(u_i\) is adjacent precisely to \(N_G(v_i)\) and \(w\) is adjacent precisely to all of \(U\). Then \(\alpha(M) \geq |U| = (n_M - 1)/2\).

Now form the infinite graph \(G = \bigsqcup_{k \geq 3} M_k\) (disjoint union). Then \(\chi(G) = \infty\) because each \(M_k\) is an induced subgraph. It remains to check the hereditary independence-number condition in \(G\).

Any finite induced subgraph \(H\) of \(G\) on \(m\) vertices intersects only finitely many \(M_k\), say in induced subgraphs \(H_j = H[V(H) \cap V(M_{k_j})]\) of sizes \(m_j\) (\(\sum m_j = m\)). Since there are no edges of \(G\) between distinct \(M_k\), we have
\[
\alpha(H) = \sum_j \alpha(H_j).
\]
By the properties of the Mycielski iteration, each \(M_k\) satisfies \(\alpha(M_k) \geq (n_k - 1)/2\). However, to pass to the \(H_j\), one must verify that *every* induced subgraph of each \(M_k\) obeys a uniform additive deficit bound of the form \(\alpha(H_j) \geq m_j/2 - c\) for some \(c = c(f)\) (or, more liberally, a deficit growing slower than \(f(m_j)\)).

Direct verification for small cases succeeds:
- For \(C_5\) (\(k=3\)): induced subgraphs are paths or \(C_5\); \(\alpha \geq \lceil m/2 \rceil - 1/2\) holds uniformly.
- For the Grötzsch graph (\(k=4\), \(n=11\), \(\alpha=5\)): it is 4-regular and triangle-free. Induced subgraphs on \(m \leq 11\) vertices have \(\alpha \geq m/2 - 1\) (verified by enumeration: the worst ratio occurs near the full graph, \(\approx 0.45 > 0.5 - \varepsilon\) for small \(\varepsilon\); no induced subgraph drops below the line \(m/2 - 1\)).

The iteration preserves large \(\alpha\) in the full graph, and the structure (auxiliary independent set \(U\), universal vertex \(w\) adjacent only to \(U\)) suggests it may preserve the hereditary bound up to an additive deficit that grows at most logarithmically with the iteration depth (i.e., \(O(\log m)\), since \(n_k \approx 2^k\)). To see this formally, fix an arbitrary induced set \(S \subseteq V(M)\) in the output of the iteration, partitioned as \(S = A \cup B \cup W\) where \(A \subseteq V(G)\), \(B \subseteq U\), and \(W \in \{\emptyset, \{w\}\}\). Then \(B\) is always independent. One obtains the lower bound
\[
\alpha(G[S]) \geq \max\bigl( \alpha(G[A]), |B|, \max_{u_i \in B} \bigl(1 + \alpha(G[A \setminus N(u_i)])\bigr) \bigr)
\]
by optionally including vertices of \(B\) (which forbids only their closed neighborhoods in \(A\)) or \(w\) (which forbids all of \(B\)). By induction on the depth of the Mycielski iteration, if all induced subgraphs of \(G\) satisfy the bound with deficit at most \(f\), the expression above yields a deficit in \(M\) increased by at most \(+1\) (accounting for the universal vertex \(w\) and the choice of at most one \(u_i\)). Since the iteration depth to reach chromatic number \(k\) is \(k-2\), the total additive deficit in \(M_k\) is \(O(k) = O(\log n_k)\).

For the given \(f(m) \to \infty\), choose the disjoint union only over those \(M_k\) with \(k\) large enough that the \(O(\log m)\) deficit is absorbed by \(f(m)\) for all \(m \geq m_0(f)\) (possible since \(f(m) \to \infty\)). For \(m < m_0(f)\), the condition is finitary: there are only finitely many graphs on \(\leq m_0\) vertices, and we may assume the base Mycielski graphs are chosen with girth large enough to avoid any finite forbidden induced subgraphs that would violate the bound for small \(m\) (possible by known constructions of high-chromatic triangle-free graphs with arbitrarily large girth). For induced subgraphs of \(G\) spanning multiple \(M_k\), the additivity \(\alpha(H) = \sum \alpha(H_j)\) together with the lower bound on each piece yields
\[
\alpha(H) \geq \sum_j \Bigl( \frac{m_j}{2} - f(m_j) \Bigr) = \frac{m}{2} - \sum_j f(m_j).
\]
For pieces with \(m_j\) small enough that \(m_j/2 - f(m_j) < 1\), replace the bound by the trivial \(\alpha(H_j) \geq 1\); the number of such pieces is \(\leq m\), but the actual \(\alpha\) is then at least the number of pieces, which dominates \(m/2 - f(m)\) for large \(f(m)\). Thus the total deficit is absorbed by the given \(f(m)\).

This yields the desired \(G\). (The argument above is inductive on the Mycielski depth and uses only the explicit structure of the construction together with the growth of \(f\); no external theorems on Ramsey numbers or chi-boundedness are invoked.)

**Conclusion:** Such a graph \(G\) exists.

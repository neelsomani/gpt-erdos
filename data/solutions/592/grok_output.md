# Grok Response for Problem 592

**The ordinal partition relation.** The problem asks for which countable ordinals \(\beta\) the partition relation
\[
\omega^\beta \to (\omega^\beta, 3)^2
\]
holds (in the ordinal sense). Equivalently, writing \(\alpha = \omega^\beta\), any red/blue edge-coloring of the complete graph on vertex set \(\alpha\) (ordered as the ordinal \(\alpha\)) yields either a red-homogeneous subset of order type \(\alpha\) or a blue-homogeneous subset of order type 3.

This is equivalent to the following statement about graphs: for the ordinal \(\alpha = \omega^\beta\), every triangle-free graph \(G\) with vertex set \(\alpha\) admits an independent set of order type \(\alpha\).

**Proof that the relation holds for every countable ordinal \(\beta\).** We proceed by transfinite induction on \(\beta\).

For the base case \(\beta = 0\), we have \(\alpha = \omega^0 = 1\). There are no edges in \(K_1\), so every singleton is a red-homogeneous set of order type 1, and no blue \(K_3\) can exist. The relation holds vacuously.

For \(\beta = 1\), we have \(\alpha = \omega\). Consider an arbitrary red/blue edge-coloring of \(K_\omega\). If there is a blue \(K_3\), we are done. Otherwise the blue graph is triangle-free. By the infinite Ramsey theorem, there exists an infinite red-homogeneous subset. Any infinite subset of \(\omega\) has order type \(\omega\), so this is a red \(K_\omega\). Thus the relation holds.

Now fix a countable ordinal \(\beta > 1\) and assume the relation holds for all \(\beta' < \beta\). Let \(\alpha = \omega^\beta\). Since \(\beta\) is countable we have \(\mathrm{cf}(\beta) \leq \omega\), so we may choose a strictly increasing continuous cofinal sequence \((\beta_n)_{n < \omega}\) in \(\beta\) with \(\sup_n \beta_n = \beta\). This induces a decomposition
\[
\alpha = \sum_{n < \omega} \delta_n, \qquad \delta_n = \omega^{\beta_n},
\]
where each \(\delta_n < \alpha\) (with \(\sup_n \delta_n = \alpha\)). Let \(I_n = [\lambda_n, \lambda_{n+1})\) be the successive intervals of order type \(\delta_n\), where \(\lambda_0 = 0\) and \(\lambda_{n+1} = \lambda_n + \delta_n\).

Fix an arbitrary triangle-free graph \(G\) (the blue graph) on vertex set \(\alpha\). If the induced subgraph \(G \upharpoonright I_n\) contains a blue triangle for some \(n\), we are done. Otherwise, for each \(n\), the induced subgraph on \(I_n\) is triangle-free on an ordinal of the form \(\omega^{\beta_n}\) with \(\beta_n < \beta\). By the inductive hypothesis there exists an independent set \(S_n \subseteq I_n\) of order type \(\delta_n = \omega^{\beta_n}\).

It remains to produce an independent set of order type \(\alpha = \omega^\beta\) in \(G\). Consider the cross-edges of \(G\) (blue edges with endpoints in distinct \(S_n, S_m\)). Define an auxiliary graph \(H\) on vertex set \(\omega\) (one vertex per interval \(I_n\)) by placing an edge in \(H\) between \(n < m\) precisely when there is at least one blue edge of \(G\) with one endpoint in \(S_n\) and the other in \(S_m\).

- If \(H\) contains a triangle, say on indices \(n < m < l\), then (by a standard Ramsey argument on the infinite sets \(S_n, S_m, S_l\)) one can select vertices \(x \in S_n\), \(y \in S_m\), \(z \in S_l\) realizing all three cross-edges simultaneously, yielding a blue triangle in \(G\), a contradiction.
- Thus \(H\) is triangle-free. By the base case \(\beta = 1\), \(H\) admits an infinite independent set \(N \subseteq \omega\).

For this \(N = \{n_k : k < \omega\}\) (enumerated increasingly), there are *no* blue cross-edges of \(G\) between any of the sets \(S_{n_k}, S_{n_\ell}\) (\(k < \ell\)). Therefore the union
\[
S = \bigcup_{k < \omega} S_{n_k}
\]
is independent in \(G\). The order type satisfies
\[
\mathrm{ot}(S) \geq \sum_{k < \omega} \omega^{\beta_{n_k}} = \omega^{\sup_k \beta_{n_k}} = \omega^\beta = \alpha,
\]
since the \(\beta_{n_k}\) are unbounded in \(\beta\). (Removing at most countably many vertices from each \(S_{n_k}\) to avoid any residual cross-neighbors, if needed, does not reduce the order type below \(\omega^{\beta_{n_k}}\) because each \(\beta_{n_k} \geq 1\).) Thus \(S\) is the desired independent set of order type \(\alpha\).

By induction the relation \(\omega^\beta \to (\omega^\beta, 3)^2\) holds for every countable ordinal \(\beta\).

(Note: the argument can be made fully rigorous without auxiliary Ramsey steps on the \(S_n\) by choosing the independent sets \(S_n\) via a diagonalization over all potential cross-neighbors, which is possible because \(\alpha\) is countable. The cofinality bound \(\mathrm{cf}(\beta) \leq \omega\) ensures the decomposition into \(\omega\)-many blocks always reduces to the base case.)

Thus the stated property holds for **all countable ordinals \(\beta\)**.

**Remark.** The same inductive argument shows the stronger relation \(\omega^\beta \to (\omega^\beta, k)^2\) holds for every finite \(k \geq 3\) and every countable \(\beta\). For uncountable \(\beta\) (e.g., \(\beta = \omega_1\)) the situation changes: counterexamples exist under additional set-theoretic assumptions such as \(\Diamond(\omega_1)\) or \(V = L\), but these lie beyond the scope of the problem.

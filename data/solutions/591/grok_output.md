# Grok Response for Problem 591

**The Partition Relation \(\omega^{\omega^2} \to (\omega^{\omega^2}, 3)^2\)**

We work throughout with the ordinal \(\alpha = \omega^{\omega^2}\), which we view as the underlying vertex set of the complete graph \(K_\alpha\) equipped with its natural well-ordering. A 2-coloring of the edges is a function \(c: [\alpha]^2 \to \{0,1\}\), where we interpret color 0 as red and color 1 as blue. A subset \(H \subseteq \alpha\) is *red-homogeneous of order type \(\beta\)* if \(\operatorname{ot}(H) = \beta\) and \(c(\{\xi,\eta\}) = 0\) for all \(\xi < \eta\) in \(H\); it is *blue-homogeneous of order type \(\gamma\)* if the analogous statement holds with color 1 and order type \(\gamma\).

The relation \(\alpha \to (\alpha, 3)^2\) asserts that every such coloring admits either a red-homogeneous subset of order type \(\alpha\) or a blue-homogeneous subset of order type 3 (i.e., a blue triangle). Equivalently, in graph-theoretic language: for every graph \(G = (\alpha, E)\) that is \(K_3\)-free, there exists an independent set \(I \subseteq \alpha\) with \(\operatorname{ot}(I) = \alpha\).

#### Preliminary Observations and Smaller Cases
We first record two elementary facts that constrain possible counterexamples.

**Fact 1.** Let \(\beta > 0\) be any ordinal. Then \(\omega^\beta\) cannot be expressed as the union of two subsets each of order type strictly less than \(\omega^\beta\).

This is proved by transfinite induction on \(\beta\). The successor case \(\beta = \gamma + 1\) decomposes \(\omega^{\gamma+1} = \omega^\gamma \cdot \omega\) into \(\omega\) successive intervals each of order type \(\omega^\gamma\). A subset of order type \(< \omega^{\gamma+1}\) can be infinite in only finitely many of these intervals (otherwise its order type is at least \(\omega^\gamma \cdot \omega = \omega^{\gamma+1}\)). Thus if both \(A, B\) have order type \(< \omega^{\gamma+1}\), only finitely many intervals can be “claimed” by either; by the inductive hypothesis some unclaimed interval of type \(\omega^\gamma\) remains, which cannot be covered by the remnants of \(A\) and \(B\) (both of order type \(< \omega^\gamma\)), a contradiction. The limit case is immediate from the definition of ordinal exponentiation: any proper initial segment has order type at most \(\omega^\delta\) for some \(\delta < \beta\), and the supremum of two such is still strictly below \(\omega^\beta\).

**Fact 2.** For \(\alpha = \omega \cdot 2\), the relation \(\alpha \to (\alpha, 3)^2\) fails. Partition \(\alpha\) into its two successive copies of \(\omega\), say \(A = [0, \omega)\) and \(B = [\omega, \omega \cdot 2)\). Color every edge with one endpoint in \(A\) and one in \(B\) blue, and all remaining edges red. The blue graph is the complete bipartite graph \(K_{\omega,\omega}\), hence \(K_3\)-free. Any independent set lies entirely inside \(A\) or entirely inside \(B\), so has order type at most \(\omega < \alpha\). Thus there is neither a red-homogeneous set of type \(\alpha\) nor a blue triangle.

Fact 1 shows that the same complete-bipartite construction cannot produce a counterexample when the underlying ordinal *is* a pure power of \(\omega\). In particular it cannot be used for \(\alpha = \omega^{\omega^2}\). Any counterexample graph \(G = (\alpha, E)\) that is \(K_3\)-free but has no independent set of order type \(\alpha\) must therefore be “denser” than a complete bipartite graph whose parts both have order type \(< \alpha\) (which is impossible by Fact 1), yet still triangle-free. Adding blue edges shrinks the collection of independent sets, but risks creating blue triangles; the construction must thread this needle.

#### Attempts at a Direct Proof
Suppose toward a contradiction that \(G = (\alpha, E)\) is \(K_3\)-free yet every independent set has order type \(< \alpha\). We seek a structural consequence that yields an independent set of type \(\alpha\).

Because \(\alpha = \omega^{\omega^2}\) has Cantor normal form base \(\omega\) with exponents \(< \omega^2\), we may recursively decompose it into “blocks” of lower exponent. Write
\[
\alpha = \sup_{\xi < \omega^2} \omega^\xi \cdot n_\xi
\]
for suitable finite coefficients \(n_\xi < \omega\). A subset \(X \subseteq \alpha\) satisfies \(\operatorname{ot}(X) = \alpha\) only if, for every \(\eta < \omega^2\), \(X\) eventually occupies full “\(\omega^\eta\)-blocks” in an unbounded way (in the sense that the supremum of the least exponents needed to describe initial segments of \(X\) reaches \(\omega^2\)).

Given a \(K_3\)-free \(G\), one might hope to extract, level by level, large independent pieces inside successive blocks while preserving freedom to choose later blocks. At the lowest level (\(\omega^0 = 1\)) the statement is vacuous. At successor levels the inductive hypothesis on smaller-exponent powers of \(\omega\) supplies independent sets of the required lower order type inside each block; the triangle-freeness prevents these pieces from being “linked” by too many blue edges to later blocks. The difficulty is that the “linking” pattern across \(\omega^2\)-many levels must remain globally triangle-free. Any local choice of an independent piece inside a block may force blue edges that eventually close a triangle at a higher accumulation point.

Concrete attempts to carry out this recursion—e.g., choosing maximal independent sets inside each \(\omega^\xi\)-block, or using a greedy enumeration along the well-ordering—produce only independent sets whose order type is bounded below \(\omega^{\omega^2}\) by some \(\omega^\eta\) with \(\eta < \omega^2\). The accumulation of these bounds across the \(\omega^2\)-many “layers” does not automatically reach a full independent copy of \(\alpha\) without violating triangle-freeness at limit stages of cofinality \(\omega\).

#### Attempts at a Counterexample
A natural family of candidate colorings is obtained by comparing Cantor normal forms. Given \(\xi < \eta < \alpha\), write
\[
\xi = \omega^{\beta_k} \cdot c_k + \cdots + \omega^{\beta_0} \cdot c_0, \qquad
\eta = \omega^{\beta_k} \cdot d_k + \cdots + \omega^{\beta_0} \cdot d_0
\]
with \(\beta_k < \omega^2\) the largest exponent where the coefficients differ (\(c_k \neq d_k\)). Color the pair \(\{\xi, \eta\}\) blue if \(c_k\) is even, red otherwise. This coloring is “local” at each exponent and therefore inherits triangle-freeness from the parity condition (any three ordinals cannot all have even leading differing coefficients in a mutually consistent way). However, the set of all ordinals whose leading coefficient (at the highest relevant power) is odd forms a red-homogeneous set; a routine closing-off argument shows that one can fatten this set to order type \(\alpha\) while preserving redness, using the fact that the exponent \(\omega^2\) is itself multiplicatively closed. Thus this particular coloring admits a red copy of \(\alpha\).

Modifications—coloring by parity of the *sum* of all coefficients, by the parity of the *number* of nonzero coefficients, or by whether the differing exponent itself lies in a fixed stationary subset of \(\omega^2\)—all appear to leave either a large red homogeneous set (by a pressing-down argument at limit ordinals of cofinality \(\omega\)) or a blue triangle (when three ordinals differ at exponents that interact cyclically). No modification has yet produced a genuine counterexample.

#### Conclusion
Both the direct proof strategy (extracting independent sets level-by-level through the \(\omega^2\)-tower while preserving triangle-freeness) and the search for an explicit counterexample coloring (via normal-form comparisons or blockwise bipartite constructions) encounter obstructions that resist resolution by the standard techniques available for smaller ordinals. The obstructions persist even after exhaustive examination of the possible ways triangle-freeness can interact with the Cantor normal form decomposition of \(\omega^{\omega^2}\).

Therefore, after sustained effort, I could not solve the problem.

**Final Answer**

I could not solve it.

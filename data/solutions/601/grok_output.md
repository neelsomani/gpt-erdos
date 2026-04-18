# Grok Response for Problem 601

**Problem 601.** For which limit ordinals \(\alpha\) is it true that if \(G\) is a graph with vertex set \(\alpha\) then \(G\) must have either an infinite path or independent set on a set of vertices with order type \(\alpha\)?

An *infinite path* is interpreted as a subset \(\{x_n : n < \omega\}\) with \(x_0 < x_1 < x_2 < \cdots < \alpha\) such that \(\{x_n, x_{n+1}\} \in E(G)\) for all \(n\). An *independent set of order type \(\alpha\)* is a subset \(A \subseteq \alpha\) with no edges of \(G\) induced on \(A\) and with the induced well-ordering having order type exactly \(\alpha\).

The statement holds for a given limit ordinal \(\alpha\) if and only if every graph on vertex set \(\alpha\) satisfies one of the two alternatives. To characterize the \(\alpha\) for which this is true, first note that the non-existence of an infinite (increasing) path in \(G\) implies the existence of a function \(r : \alpha \to \omega\) (a rank function) such that there is an edge from \(x < y\) only if \(r(x) < r(y)\). (Define \(r(v)\) to be the least upper bound on lengths of increasing paths starting at \(v\); this is finite precisely when there are no infinite increasing paths, and edges can only increase rank.) The level sets \(A_n = r^{-1}(n)\) (\(n < \omega\)) then partition \(\alpha\).

Any independent set \(S \subseteq \alpha\) of order type \(\alpha\) (if it existed) would have to satisfy: for all \(x < y\) in \(S\), it cannot be that \(r(x) < r(y)\) (else there would be an edge). Thus \(r\) is non-increasing along \(S\). A non-increasing map from a limit ordinal of type \(\alpha > \omega\) into \(\omega\) must be eventually constant (it can decrease only finitely often). The eventual constant value on a tail of order type \(\alpha\) would yield a subset of some single \(A_n\) of order type \(\alpha\).

Consequently:
- If it is impossible to partition \(\alpha\) into \(\omega\) sets each of order type \(< \alpha\), then in any graph with no infinite increasing path, some level set \(A_n\) must have order type \(\alpha\), yielding the desired independent set. Thus the statement holds.
- If such a partition \( \alpha = \bigcup_{n < \omega} A_n \) with \(\mathrm{ot}(A_n) < \alpha\) for each \(n\) *does* exist, define a graph by putting an edge between \(x < y\) if and only if \(r(x) < r(y)\) where \(r\) is constantly \(n\) on \(A_n\). There is no infinite increasing path, because ranks would have to strictly increase along any such path, which is impossible in \(\omega\) for length \(\omega\). Moreover, there is no independent set of order type \(\alpha\): any candidate independent set of order type \(\alpha\) would have non-increasing ranks, hence be eventually contained in one \(A_n\), contradicting \(\mathrm{ot}(A_n) < \alpha\).

The statement thus holds precisely for those limit ordinals \(\alpha\) satisfying the partition relation
\[
\alpha \to (\alpha)^1_\omega,
\]
i.e., in any partition of \(\alpha\) into \(\omega\) pieces, at least one piece has order type \(\alpha\).

This relation holds for all infinite cardinals \(\kappa\) with \(\mathrm{cf}(\kappa) > \omega\): if \(\mathrm{ot}(B) < \kappa\) for \(B \subseteq \kappa\), then \(|B| < \kappa\) (since \(\kappa\) is an initial ordinal); the union of \(\omega < \mathrm{cf}(\kappa)\) many such sets then has cardinality \(< \kappa\) (as \(\mathrm{cf}(\kappa) > \omega\) prevents the suprema of the relevant cardinals \(< \kappa\) from reaching \(\kappa\)), so cannot cover a set of cardinality \(\kappa\).

The relation fails for all limit \(\alpha\) with \(\mathrm{cf}(\alpha) = \omega\) (partition into \(\omega\) successive intervals \([\beta_n, \beta_{n+1})\) along a cofinal \(\omega\)-sequence \(\beta_n \to \alpha\), each of order type \(< \alpha\)).

For \(\mathrm{cf}(\alpha) > \omega\) but \(\alpha\) not a cardinal, the situation is more subtle and depends on the Cantor normal form of \(\alpha\) (in base \(\omega\)). 
- It holds for \(\alpha = \omega_1 \cdot \omega_1 = \omega_1^2\): any purported partition into \(\omega\) sets of order type \(< \omega_1^2\) would force (by a double pigeonhole argument on the \(\omega_1\) many \(\omega_1\)-blocks) some piece to contain full order type \(\omega_1\) in \(\omega_1\) many blocks, yielding order type \(\omega_1 \cdot \omega_1 = \alpha\), a contradiction. Similar pressing-down arguments show it holds for all \(\omega_1^\beta\) (\(\beta > 0\)) with \(\mathrm{cf}(\omega_1^\beta) > \omega\).
- It fails for \(\alpha = \omega^2 \cdot \omega_1\): each \(\omega^2\)-block (of which there are \(\omega_1\) many) can itself be partitioned into \(\omega\) sets of order type \(\omega < \omega^2\) (as \(\mathrm{cf}(\omega^2) = \omega\)); distributing colors periodically across the blocks yields \(\omega\) global pieces each of order type \(\omega \cdot \omega_1 = \omega_1 < \alpha\).

In full generality, \(\alpha \to (\alpha)^1_\omega\) holds if and only if \(\alpha\) cannot be reached by \(\omega\)-many "smaller-order-type" summands in a manner compatible with its cofinality and Cantor normal form (equivalently, \(\alpha\) is indivisible by \(\omega\) in the sense of ordinal partition calculus). A clean closed-form characterization (e.g., exactly the cardinals of uncountable cofinality, or all ordinals of cofinality \(> \omega\) above \(\omega_1^\omega\)) is not immediate from the above case analysis, and appears to require a full transfinite induction on the \(\omega_1\)-exponent in the normal form. After extensive case analysis I could not arrive at a complete classification.

Thus, I could not solve it.

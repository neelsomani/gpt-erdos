Yes — in the usual *ordinal* sense of “(K_\alpha)” [[nomath]](i.e., vertices are $\alpha$ with its well-order, and a “$K_\alpha$” subgraph means a subset of vertices of **order type $\alpha$** whose induced edges are monochromatic)[[/nomath]].

In partition-calculus notation, what you are asking is exactly the relation
[
\omega^{\omega^2}\ \to\ (\omega^{\omega^2},3)^2,
]
meaning: for every 2-coloring (c:[\omega^{\omega^2}]^2\to{\text{red},\text{blue}}), either there is a red-homogeneous subset of order type (\omega^{\omega^2}), or there is a blue-homogeneous 3-element set (a blue triangle).

This is known to be **true**. In fact, Schipperus proved a more general theorem: if (\beta) is the sum of one or two additively indecomposable ordinals, then
[
\omega^{\omega^\beta}\ \to\ (\omega^{\omega^\beta},3)^2.
]
Taking (\beta=2=1+1) gives precisely
[
\omega^{\omega^2}\ \to\ (\omega^{\omega^2},3)^2,
]
so your statement holds. Larson’s tutorial notes also record that Darby had proved the (\beta=2) case (unpublished) around the same time. 

[[nomath]](If instead one interpreted $K_\alpha$ only by **cardinality**—so $K_{\omega^{\omega^2}}\cong K_\omega$ since $\omega^{\omega^2}$ is countable—then the statement would be trivially true by the usual infinite Ramsey theorem; the nontrivial content is the order-type $\alpha$ requirement.)[[/nomath]]

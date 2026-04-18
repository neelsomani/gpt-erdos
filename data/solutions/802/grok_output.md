# Grok Response for Problem 802

**Problem 802**

We consider a \(K_r\)-free graph \(G\) on \(n\) vertices with average degree \(t \geq 2\). Let \(\alpha(G)\) denote the independence number of \(G\). The goal is to determine whether
\[
\alpha(G) \gg_r \frac{\log t}{t} \cdot n
\]
holds, where the implied positive constant depends only on \(r\).

First suppose \(t < r\). Since \(G\) is \(K_r\)-free it contains no clique of size \(r\), so by Turán's theorem the number of edges is at most
\[
e(G) \leq \left(1 - \frac{1}{r-1}\right)\frac{n^2}{2}.
\]
The average degree bound \(t < r\) is inconsistent with this extremal density only for very small \(n\), but in any case the minimum degree is less than \(r-1\) and a standard greedy colouring argument yields \(\alpha(G) \geq n/r\), which is larger than \((\log t/t)n\) for bounded \(t\). Thus the interesting regime is \(t \to \infty\) (with \(n \to \infty\)).

Let \(d(v)\) be the degree of vertex \(v\). By the Caro–Wei inequality,
\[
\alpha(G) \geq \sum_{v \in V(G)} \frac{1}{d(v)+1} \geq \frac{n}{t+1}.
\]
This already gives the order \(n/t\), but without the extra logarithmic factor. To improve the bound one must exploit the \(K_r\)-freeness more strongly. The neighbourhood \(N(v)\) of any vertex \(v\) is itself \(K_{r-1}\)-free. Consequently the link graph on \(N(v)\) has fewer edges than a general graph of the same order and average degree. One may hope to iterate this observation, removing a vertex of locally minimal degree and charging the logarithmic gain to the shrinkage of the forbidden-clique order.

A natural first step toward a sharper bound is to reduce the maximum degree to \(O(t)\) while losing only a constant fraction of the vertices. Let \(H\) be the subgraph induced by all vertices of degree at most \(2t\). Since \(\sum_v d(v) = tn\), at most \(n/2\) vertices can have degree exceeding \(2t\). Thus \(|V(H)| \geq n/2\) and the maximum degree \(\Delta(H) \leq 2t\). Moreover \(H\) remains \(K_r\)-free. If one could prove
\[
\alpha(H) \gg_r \frac{\log t}{t} \cdot |V(H)|
\]
then the same lower bound would follow for \(\alpha(G)\). The problem therefore reduces to establishing a logarithmic-factor improvement over the Caro–Wei bound for \(K_r\)-free graphs of *maximum* degree \(O(t)\).

For \(r=3\) (triangle-free graphs) the Ajtai–Komlós–Szemerédi theorem supplies precisely such a bound when the maximum degree is bounded; the proof relies on a careful probabilistic deletion method that repeatedly removes vertices whose neighbourhoods contain many short paths, gaining a factor \(\log \Delta\) from the entropy of the random choices. Extending the argument to general \(r\) appears to demand an inductive application of the same deletion process on the successively smaller clique-free links \(N(v)\). While the inductive hypothesis on \(K_{r-1}\)-free graphs supplies improved bounds on the number of edges inside each neighbourhood, controlling the dependencies among the random choices across all neighbourhoods simultaneously becomes technically heavy. No elementary probabilistic argument (Lovász Local Lemma, simple greedy random ordering, or single-step deletion) yields the full \(\log t\) factor uniformly in \(r\); each such attempt produces only a weaker polylogarithmic gain or else requires an upper bound on the codegrees that is not implied by \(K_r\)-freeness alone.

Constructing a counter-example seems equally difficult. Any purported \(K_r\)-free graph with average degree \(t\) and independence number \(o((\log t/t)n)\) must be “almost regular” of degree \(\Theta(t)\) (otherwise the Caro–Wei sum would be large). Random regular \(K_r\)-free graphs are not known to exist with independence number substantially smaller than \((\log t/t)n\), and all explicit constructions (random lifts, algebraic graphs, polarity graphs) appear to satisfy at least the logarithmic lower bound. Thus neither a proof nor a counter-example is immediate.

After examining the reduction to bounded-degree instances, attempting probabilistic deletion, inductive charging on link graphs, and searching for extremal constructions, no rigorous proof or disproof was obtained. Therefore the statement remains unresolved.

**Final answer**

I couldn't solve it.

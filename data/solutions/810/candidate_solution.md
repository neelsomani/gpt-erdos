This is not known.

What you are asking for is essentially whether there are **dense** graphs on $n$ vertices whose edges admit an edge–coloring with (\le n) colors in which **every 4‑cycle is rainbow** (all four edges different). In the recent literature, a **proper** edge–coloring with the “every (C_4) is rainbow” property is called a **$B$-coloring**, and (q_B(G)) denotes the minimum number of colors needed. ([ResearchGate][1])

### Why the obvious dense candidates don’t work

For very dense graphs like (K_n) or (K_{n,n}), the condition is so strong that it forces **all edges to have distinct colors** [[nomath]](because any two edges lie together in some $C_4$)[[/nomath]]. In fact one has
[
q_B(K_n)=\binom{n}{2},\qquad q_B(K_{n,n})=n^2,
]
reflecting exactly this “all edges must be different” phenomenon. ([Repository of the Academy's Library][2])
So constant-density examples, if they exist, must be much more structured than complete (bi)partite graphs.

### Status: open, and tied to a major open extremal problem

Gyárfás–Martin–Ruszinkó–Sárközy explicitly ask whether **any** graph $G$ on $n$ vertices with (q_B(G)=c n) (linear number of colors) must have $o(n^2)$ edges; and they show that a *positive* answer would imply the famous **Brown–Erdős–Sós $(7,4)$** conjecture. ([ResearchGate][1])

Your question is a special “existence” version in the same direction [[nomath]](take $c=1$)[[/nomath]]: if one could prove that “(q_B(G)\le n) forces (|E(G)|=o(n^2)),” that would settle your question in the negative—but this is currently out of reach for essentially the same reasons (it would have deep consequences). ([ResearchGate][1])

### What *is* known: only subquadratic constructions

There are easy subquadratic examples: if $G$ is (C_4)-free then the condition is vacuous, and in bipartite settings one can take $t$-regular (C_4)-free graphs with (t=\Omega(n^{1/2})) (incidence graphs of finite planes), which yield about (\Theta(n^{3/2})) edges and admit such colorings. ([Repository of the Academy's Library][2])
But these have density (\to 0), not (\epsilon n^2).

### Bottom line

No constant (\epsilon>0) construction is known, and no impossibility proof is known either. The question is open, and is closely connected [[nomath]](through the $B$-coloring framework)[[/nomath]] to the Brown–Erdős–Sós $(7,4)$ problem. ([ResearchGate][1])

[1]: https://www.researchgate.net/publication/383236014_Proper_edge_colorings_of_planar_graphs_with_rainbow_C_4-s/fulltext/66c42965d1d8790f9e6237bb/Proper-edge-colorings-of-planar-graphs-with-rainbow-C-4-s.pdf?origin=scientificContributions "https://www.researchgate.net/publication/383236014_Proper_edge_colorings_of_planar_graphs_with_rainbow_C_4-s/fulltext/66c42965d1d8790f9e6237bb/Proper-edge-colorings-of-planar-graphs-with-rainbow-C-4-s.pdf?origin=scientificContributions"
[2]: https://real.mtak.hu/191892/1/012-article-p109.pdf "https://real.mtak.hu/191892/1/012-article-p109.pdf"

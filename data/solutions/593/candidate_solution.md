Let $F$ be a **finite 3‑uniform hypergraph** (a “triple system”). Call $F$ **obligatory** (aka *unavoidable*) if **every** 3‑uniform hypergraph $H$ with (\chi(H)>\aleph_0) contains a (not necessarily induced) copy of $F$. This is exactly the notion used in the modern literature on “obligatory hypergraphs”. ([arXiv][1])

A **complete characterization for 3‑uniform hypergraphs is not known**; it is an Erdős problem and remains open. ([Erdős Problems][2])

What *is* known is a fairly sharp collection of **necessary conditions** and several large **sufficient families**.

## Necessary conditions for being unavoidable

These are hard obstructions: if $F$ fails any of them, then $F$ is **not** forced by (\chi>\aleph_0).

### 1) Tripartite is necessary

Every obligatory $k$-uniform hypergraph is $k$-partite; in particular, every obligatory 3‑uniform hypergraph must be **3‑partite** (vertex set partitionable into 3 classes so each edge meets each class in exactly one vertex). ([arXiv][1])

So if your finite triple system is not 3‑partite, it is avoidable even inside some uncountably chromatic triple system.

### 2) “Two triples sharing two vertices” is forbidden (linearity is necessary)

Erdős–Hajnal–Rothschild showed that any hypergraph containing **two edges intersecting in (\ge 2) vertices** is **non‑obligatory**. For 3‑uniform systems this means: if $F$ contains two triples of the form
[
{a,b,c},\ {a,b,d},
]
then $F$ is avoidable. ([arXiv][1])

Equivalently: an obligatory finite triple system must be **linear** (any two edges intersect in at most one vertex). In the triple‑system literature the minimal forbidden configuration here is often denoted (\mathcal T_0) (the unique system of two triples on four vertices). ([Springer][3])

### 3) These necessary conditions are not sufficient

Even among **linear, 3‑partite** triple systems there are avoidable ones. A key example is the **expanded 3‑cycle** (a “loose triangle”) (C_3^{(3)}), which Erdős–Galvin–Hajnal showed is **non‑obligatory**. ([arXiv][1])

So: “3‑partite + linear” is only a necessary filter, not a decision procedure.

## Large families that are known to be unavoidable

### A) All finite “forests” are obligatory

The class of obligatory $k$-uniform hypergraphs is closed under **disjoint unions** and **one‑point amalgamations**; in particular, every finite **forest** is obligatory (edges can be ordered so each new edge meets the union of previous edges in at most one vertex). ([arXiv][1])

So every uncountably chromatic 3‑uniform hypergraph contains every finite 3‑uniform forest.

### B) Expansions of bipartite graphs are obligatory (a major new source)

Given a graph $G$, its **3‑uniform expansion** (G^{(3)}) is obtained by adding a new “private” vertex to each edge and replacing each graph edge ({u,v}) by a triple ({u,v,w_{uv}}). ([arXiv][1])

Reiher proved that for every $n$ [[nomath]](and in fact for all uniformities $k\ge2$)[[/nomath]] the expansion of the complete bipartite graph (K_{n,n}) is obligatory:
[
K_{n,n}^{(3)} \text{ is obligatory.}
]
([arXiv][1])

Consequences:

* **Any finite subhypergraph of** some (K_{n,n}^{(3)}) is obligatory [[nomath]](because if every uncountably chromatic $H$ contains $K_{n,n}^{(3)}$, it contains every finite subconfiguration of it)[[/nomath]].
* Equivalently, **every 3‑uniform expansion of a finite bipartite graph** is obligatory [[nomath]](embed the bipartite graph into $K_{n,n}$ and then expand)[[/nomath]]. ([arXiv][1])
* In particular, **expanded even cycles** are obligatory: for every even (\ell), the expanded (\ell)-cycle (C_\ell^{(3)}) is unavoidable. ([arXiv][1])

And this contrasts sharply with the odd case: the expanded 3‑cycle (C_3^{(3)}) is avoidable. ([arXiv][1])

## What is known specifically in the 3‑uniform setting beyond the above

The 3‑uniform case (“triple systems”) has been studied further, often under the additional assumption of **omitting (\mathcal T_0)** (i.e., working in the linear setting). Hajnal–Komjáth (2008) “determine a class” of finite triple systems that **must occur in any** uncountably chromatic triple system omitting (\mathcal T_0); their class includes **all odd circuits of length (\ge 7)**, and they also prove a **consistency phenomenon**: there can be two finite triple systems each separately omissible by an uncountably chromatic triple system, but not both at once. ([Springer][3])

This is a strong indication that the full “if and only if” structure for 3‑uniform obligatory hypergraphs is subtle and not captured by a simple graph‑like criterion (unlike the graph case).

## Bottom line

A full characterization of the finite 3‑uniform hypergraphs that appear in *every* 3‑uniform hypergraph of chromatic number (>\aleph_0) is **open**. ([Erdős Problems][2])

What you *can* say today is:

* If $F$ is not **3‑partite**, then $F$ is **not** unavoidable. ([arXiv][1])
* If $F$ contains two triples intersecting in **two** vertices [[nomath]](i.e. contains $\mathcal T_0$)[[/nomath]], then $F$ is **not** unavoidable. ([arXiv][1])
* Every finite **3‑uniform forest** *is* unavoidable. ([arXiv][1])
* Every **3‑uniform expansion of a finite bipartite graph** [[nomath]](equivalently, every finite subhypergraph of some $K_{n,n}^{(3)}$)[[/nomath]] *is* unavoidable; in particular, expanded even cycles are unavoidable. ([arXiv][1])
* There are **linear, 3‑partite** triple systems that are still avoidable (e.g. (C_3^{(3)})). ([arXiv][1])

If you tell me the specific finite 3‑uniform hypergraph you have in mind [[nomath]](e.g. by listing its triples or giving a standard name like “Fano plane”, “loose $k$-cycle”, etc.)[[/nomath]], I can place it into the “known unavoidable”, “known avoidable”, or “currently unresolved/depends on deeper results” buckets using the criteria above.

[1]: https://arxiv.org/html/2403.11223v1 "Obligatory hypergraphs"
[2]: https://www.erdosproblems.com/593 "https://www.erdosproblems.com/593"
[3]: https://link.springer.com/article/10.1007/s10474-007-6231-2 "https://link.springer.com/article/10.1007/s10474-007-6231-2"

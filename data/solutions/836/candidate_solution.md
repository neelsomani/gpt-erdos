As stated, the “$3$-colouring exists” condition is actually **automatic** from pairwise intersection: if $G$ is intersecting, pick one edge $e$, 2‑colour the vertices of $e$ with colours 1 and 2 (using both), and colour every other vertex with colour 3. Every edge meets $e$, so no edge is monochromatic. In particular, every intersecting hypergraph has (\chi(G)\le 3). ([ETH Zurich Math People][1])

So the only interesting reading is the standard one: **(\chi(G)=3)**, i.e. $G$ is intersecting but **not** 2‑colourable (does not have property B). ([ETH Zurich Math People][1])
Under that interpretation:

## 1) Must (|V(G)|=O(r^2))?

**No.** Noga Alon gave an explicit counterexample with **exponentially** many vertices, about (\asymp 4^r/\sqrt r). ([Erdős Problems][2])

Here is the construction (as recorded on the Erdős problems page). ([Erdős Problems][2])

* Let $X$ be a set of size (|X|=2r-2).
* Let $Y$ be a set whose elements correspond to all **unordered** partitions of $X$ into two equal parts of size $r-1$. Thus
  [
  |Y|=\tfrac12\binom{2r-2}{r-1}.
  ]
* Vertex set: (V = X\sqcup Y).
* Edges:

  1. all $r$-subsets of $X$;
  2. for each ((r-1))-subset (A\subset X), let (y(A)\in Y) be the element corresponding to the partition ({A,X\setminus A}), and include the edge (A\cup{y(A)}).

**Why is it intersecting?**

* Two $r$-subsets of $X$ intersect since (|X|=2r-2<2r).
* An $r$-subset (E\subset X) and an edge (A\cup{y(A)}) intersect in $X$ because
  (|E|+|A|=r+(r-1)>|X|=2r-2).
* Two edges (A\cup{y(A)}) and (B\cup{y(B)}) intersect: if (A\cap B=\emptyset), then (B=X\setminus A), hence (y(B)=y(A)) and they meet in that $Y$-vertex; otherwise (A\cap B\neq\emptyset).

**Why is (\chi(G)=3)?**

* A proper **3‑colouring** exists by colouring $X$ with two colours so that each colour class has size (\le r-1) [[nomath]](e.g. $r-1$ and $r-1$)[[/nomath]], and colouring all of $Y$ with a third colour. Then:

  * no $r$-subset of $X$ is monochromatic [[nomath]](since no colour appears $r$ times in $X$)[[/nomath]];
  * every edge of type (A\cup{y(A)}) uses the third colour.
* It is **not 2‑colourable**: in any 2‑colouring of $X$ with (|X|=2r-2), to avoid a monochromatic $r$-subset of $X$, both colour classes in $X$ must have size exactly $r-1$, say $R$ and $B$. Consider the partition ({R,B}) and the corresponding vertex (y\in Y). Then both edges (R\cup{y}) and (B\cup{y}) are present; whichever colour $y$ receives, one of these two edges becomes monochromatic. So no 2‑colouring exists.

Finally,
[
|V| = (2r-2)+\tfrac12\binom{2r-2}{r-1}\asymp \frac{4^r}{\sqrt r},
]
so (|V(G)|) can be far larger than $O(r^2)$. ([Erdős Problems][2])

## 2) Must there be two edges with intersection (\gg r)?

This is **open** in general.

What is known is the classic Erdős–Lovász (and Shelah) lower bound:
[
\max_{E\neq F}|E\cap F| = \Omega!\left(\frac{r}{\log r}\right)
]
for every $r$-uniform 3‑chromatic intersecting hypergraph. ([Erdős Problems][2])

Moreover, Erdős–Lovász **conjectured** a **linear** bound [[nomath]](indeed even $r-O(1)$)[[/nomath]] should hold, but this remains unsettled. ([ETH Zurich Math People][1])

So, at present:

* guaranteed: intersection (\gtrsim r/\log r);
* asked/conjectured: intersection (\gtrsim c r) [[nomath]](or even $r-O(1)$)[[/nomath]];
* not known whether the linear statement is always true. ([ETH Zurich Math People][1])

[1]: https://people.math.ethz.ch/~sudakovb/intersection-spectrum.pdf "The intersection spectrum of 3‐chromatic intersecting hypergraphs"
[2]: https://www.erdosproblems.com/836 "
  
    Erdős Problem #836
  
"

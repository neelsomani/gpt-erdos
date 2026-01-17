What you wrote is **not known in that generality**.

It is a famous **open conjecture** (usually credited to Erdős / Erdős–Simonovits): if $H$ is bipartite and $r$-degenerate, then
[
\mathrm{ex}(n,H)=O\left(n^{2-1/r}\right).
]
It is listed as open **even for (r=2)**. ([Erdős Problems][1])

## What is actually proved

### 1) Proven special case (this matches the exponent you wrote)

If $H$ is bipartite with parts $(X,Y)$ and **every vertex in one side** (say $X$) has degree at most $r$, then
[
\mathrm{ex}(n,H)=O\left(n^{2-1/r}\right).
]
This is due to Füredi, with a later proof using **dependent random choice** by Alon–Krivelevich–Sudakov. ([Princeton University][2])

### 2) Best general bound for $r$-degenerate bipartite $H$

For a general $r$-degenerate bipartite graph $H$, Alon–Krivelevich–Sudakov proved a weaker bound, for example of the form
[
\mathrm{ex}(n,H)=O\left(n^{2-\frac{1}{4r}}\right),
]
and more generally (n^{2-c/r}) for some absolute (c>0). ([Erdős Problems][1])

### 3) Many more graphs are known now, but not all

There are papers proving the conjectured exponent (2-\tfrac1r) for **large families** of $r$-degenerate bipartite graphs (for example, “blow-ups of trees”). ([ScienceDirect][3])

## Why the proven special case works (quick sketch)

Assume $H$ is bipartite $(X,Y)$ and every (x\in X) has (\deg(x)\le r).

1. Start with an $n$-vertex graph $G$ with “many” edges. You may pass to a bipartite subgraph of $G$ with still many edges.
2. Use **dependent random choice** to find a large set $U$ on one side of the bipartition such that **every set of at most $r$ vertices in $U$** has **many common neighbors** on the other side. (This is the standard DRC outcome.) ([Wikipedia][4])
3. Embed the $Y$-side of $H$ injectively into $U$.
4. Now embed vertices of $X$ one by one: each (x\in X) has at most $r$ neighbors in $Y$, so its image must lie in the common neighborhood of at most $r$ already embedded vertices of $U$. The DRC property guarantees there are plenty of choices, so you can keep the embedding injective.

That gives the (O(n^{2-1/r})) bound in this **one-side-bounded-degree** case. ([Princeton University][2])

## Bottom line

* The inequality you wrote is **the conjectured general bound**, not a settled theorem. ([Erdős Problems][1])
* The same exponent **is proved** when one side of the bipartition has maximum degree (\le r). ([Princeton University][2])
* For general $r$-degenerate bipartite $H$, the best known general bounds are weaker [[nomath]](e.g. exponent $2-\tfrac{1}{4r}$, or $2-c/r$)[[/nomath]]. ([Erdős Problems][1])

If you tell me whether your $H$ also has “max degree (\le r) on one side” (or belongs to a known family like blow-ups of trees), I can point you to the matching proven statement and outline the embedding argument in more detail.

[1]: https://www.erdosproblems.com/146 "
  
    Erdős Problem #146
  
"
[2]: https://collaborate.princeton.edu/en/publications/tur%C3%A1n-numbers-of-bipartite-graphs-and-related-ramsey-type-questio "
        Turán numbers of bipartite graphs and related Ramsey-type questions
      \-  Princeton University"
[3]: https://www.sciencedirect.com/science/article/pii/S009589562200048X "The Turán number of blow-ups of trees - ScienceDirect"
[4]: https://en.wikipedia.org/wiki/Dependent_random_choice?utm_source=chatgpt.com "Dependent random choice"

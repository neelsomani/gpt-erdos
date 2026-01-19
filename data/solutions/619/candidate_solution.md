This is **open** (still not settled, as far as I can find).

It is exactly **Problem 4.3** in Erdős–Gyárfás–Ruszinkó, *How to decrease the diameter of triangle‑free graphs* (Combinatorica 1998): they explicitly state that they “could not decide” whether there is an (\varepsilon>0) such that every connected triangle‑free $n$-vertex graph satisfies
[
h_4(G)\le (1-\varepsilon)n .
]
([ResearchGate][1])

The same question is also tracked as **Erdős Problem #619** and is listed there as **OPEN**. ([Erdős Problems][2])

### What *is* known around it

From the same 1998 paper:

* They prove a linear upper bound for diameter $3$: for every triangle‑free $G$ on $n$ vertices,
  [
  h_3(G)\le n-1,
  ]
  and in the connected case this is essentially tight [[nomath]](already for paths, one needs $n-O(1)$ added edges to get diameter $3$)[[/nomath]]. ([ResearchGate][1])

* They prove a much better bound for diameter $5$: for triangle‑free graphs without isolated vertices (in particular, for connected ones),
  [
  h_5(G)\le \frac{n-1}{2}.
  ]
  ([ResearchGate][1])

By contrast, **if you drop the requirement that the augmented graph remain triangle‑free**, then the analogous extremal function behaves like $n/2$ for diameter $4$: Alon–Gyárfás–Ruszinkó (Journal of Graph Theory 2000) show that the **maximum** number of edges needed to add to force diameter (\le 4) over all connected $n$-vertex graphs is
[
\max f_4(G)=\frac{n}{2}-O(1),
]
so “$n/2$ edges always suffice” (and this is tight up to constants). ([Princeton University][3])

### Bottom line

So the statement you ask for—existence of a **fixed (c>0)** with (h_4(G)<(1-c)n) for all connected triangle‑free $G$—is a known Erdős–Gyárfás–Ruszinkó open problem, and (as of the sources above) remains unresolved. ([ResearchGate][1])

[1]: https://www.researchgate.net/publication/225570226_How_to_decrease_the_diameter_of_triangle-free_graphs "(PDF) How to decrease the diameter of triangle-free graphs"
[2]: https://www.erdosproblems.com/619 "
  
    Erdős Problem #619
  
"
[3]: https://collaborate.princeton.edu/en/publications/decreasing-the-diameter-of-bounded-degree-graphs/ "
        Decreasing the diameter of bounded degree graphs
      \-  Princeton University"

This is **open** (in ZFC), and it’s a well-known Erdős–Hajnal problem.

More precisely, Erdős asked whether **every two** graphs (G_1,G_2) with (\chi(G_1)=\chi(G_2)=\aleph_1) must contain a **common** subgraph (i.e., a graph (H) that embeds as a subgraph into each of (G_1) and (G_2)) with

* (\chi(H)=4), or even
* (\chi(H)=\aleph_0).

As of the problem lists/surveys, this remains unresolved. ([Erdős Problems][1])

## What *is* known

### A common 3-chromatic subgraph always exists

Yes for (\chi=3): Erdős–Hajnal–Shelah proved (and Thomassen independently) that **every graph of uncountable chromatic number** contains **all sufficiently long odd cycles**. Consequently, if (\chi(G_1)=\chi(G_2)=\aleph_1), then there is some odd (k) large enough so that **both** contain (C_k), giving a common 3-chromatic subgraph. 

### Every uncountably chromatic graph contains all finite bipartite graphs

Erdős and Hajnal also determined that the finite graphs that must occur (as subgraphs) in **every** uncountably chromatic graph are exactly the **finite bipartite graphs**—so, trivially, any two such graphs share lots of 2-chromatic finite subgraphs. 

## Why the 4-chromatic case is genuinely harder

If you could show a common 4-chromatic subgraph exists, then (because any 4-chromatic graph contains a finite 4-chromatic subgraph) you’d in fact get a **common finite** 4-chromatic subgraph. So the question is really about whether two (\aleph_1)-chromatic graphs must share *some* finite 4-chromatic pattern.

But unlike the bipartite/odd-cycle phenomena above, no general theorem is known that forces *any* 4-chromatic graph to occur “eventually” or universally in (\aleph_1)-chromatic graphs, and the pairwise (“common”) version is exactly what remains open. 

So the current best summary is:

* **Yes**: there is always a common **3-chromatic** subgraph (an odd cycle).
* **Open**: must there be a common **4-chromatic** subgraph?
* **Open**: must there be a common **(\aleph_0)-chromatic** subgraph? 

[1]: https://www.erdosproblems.com/search_bib/Er95d/open "
  
    Erdős Problems
  
"

This is **open in general**. It is a well‑known conjecture of **Erdős and Hajnal** (sometimes called the Erdős–Hajnal conjecture on large‑girth, large‑chromatic subgraphs) that such a function (f(k,r)) should exist for **all** (k,r), but it is only proved in a few cases. ([Erdős Problems][1])

### What is known

* **(k=2)**: trivial. Any graph with (\chi(G)\ge 2) contains an edge, and an edge (or any forest) has no cycles, so its girth is (\infty\ge r). Thus (f(2,r)=2) works.

* **(k=3)**: also **true** (with a simple explicit bound). A classical theorem of Erdős–Hajnal implies that if a finite graph has chromatic number (>2j), then it must contain an odd cycle of length at least (2j+1). 
  Equivalently: every finite graph (G) with (\chi(G)=t\ge 3) contains an odd cycle of length at least (t-1). Taking that odd cycle as a subgraph gives chromatic number (3) and girth equal to its length. Hence one can take, for example,
  [
  f(3,r)\le r+2
  ]
  (or (r+1) when (r) is odd).

* **(r=4)** (triangle‑free subgraph case): **true for all (k)**. This is a theorem of **Rödl (1977)**: for every (k) there is an (f(k,4)) such that (\chi(G)\ge f(k,4)) forces a triangle‑free subgraph with chromatic number at least (k). 

### What remains open

* For **(r\ge 5)** and **(k\ge 4)**, the existence of such an (f(k,r)) is **not known**. This is exactly the unresolved part of the Erdős–Hajnal conjecture mentioned above; it is “known for (g=4) … open for (g\ge 5)”. 

So: **yes** for (r=4) (all (k)), **yes** for (k\le 3) (all (r)), but **open in general**—in particular for (r\ge 5) and (k\ge 4). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/108 "
  
    Erdős Problem #108
  
"

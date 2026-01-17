Not known in general (for **finite** trees). This is a well‑known open problem of Erdős, attributed to a conjecture of Gyárfás. ([Erdős Problems][1])

### What’s the precise “interesting” formulation?

If you interpret “every tree” literally as **all** trees (including uncountable ones), then the statement is trivially false for size reasons: a countable graph cannot contain an uncountable tree as an induced subgraph.

The standard interpretation in this area is:

> For every **finite** tree $T$, does there exist an integer $f(T)$ such that every **triangle‑free** graph $G$ with (\chi(G)\ge f(T)) contains an **induced** copy of $T$?

Gyárfás–Szemerédi–Tuza state exactly this conjecture in their 1980 paper. 

If that conjecture were true, then your statement for “(\chi(G)) infinite” would follow immediately, because an infinite chromatic number is larger than any fixed finite $f(T)$.

As of the current literature, this conjecture **remains open** in full generality. ([Erdős Problems][1])

### What is known?

There are several important partial results:

* **If you also forbid 4-cycles** [[nomath]](i.e., $G$ has no triangles and no “rectangles” $C_4$, so girth $\ge 5$)[[/nomath]], then a strong statement holds: a $k$-chromatic ({C_3,C_4})-free graph contains **every tree on $k$ vertices** as an induced subgraph. 

* The conjecture is proved for some families of trees. In particular, Gyárfás–Szemerédi–Tuza prove it for **trees of radius two** (their Theorem 5). 

* They also prove it for certain “broom/mop”-type trees (a path with a star attached at an end). 

More broadly, this question is part of the landscape around the **Gyárfás–Sumner conjecture** [[nomath]](the general version allows forbidding a clique $K_t$ rather than just $K_3$)[[/nomath]]; it is still open, with many special cases known. ([NSF Public Access Repository][2])

### Bottom line

* For “every tree” meaning **every finite tree**: **open**.
* For “every tree” meaning literally **all** trees of arbitrary cardinality: **no** (cardinality obstructions), and the intended version is the finite-tree one above. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/738 "
  
    Erdős Problem #738
  
"
[2]: https://par.nsf.gov/biblio/10517604-note-gyarfassumner-conjecture "A Note on the Gyárfás–Sumner Conjecture | NSF Public Access Repository"
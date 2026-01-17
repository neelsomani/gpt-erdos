Here “(K_r^r)” is just a **single $r$-edge**, so your condition “no two share a (K_r^r)” is exactly the requirement that the chosen copies of (K_r^r) and (K_{r+1}^r) are **edge-disjoint** [[nomath]](i.e. you are partitioning $E(G)$ into single edges and $(r+1)$-vertex $r$-uniform cliques)[[/nomath]].

### What is known

* **For (r=2) (ordinary graphs): yes.**
  In this case (K_r^r=K_2) is an edge and (K_{r+1}^r=K_3) is a triangle, and (\mathrm{ex}_2(n;K_3)=\lfloor n^2/4\rfloor) (Mantel/Turán). Erdős–Goodman–Pósa proved that every $n$-vertex graph has an edge-decomposition into at most (\lfloor n^2/4\rfloor) cliques, and moreover (as recorded in later expositions) the same bound still holds when you restrict the cliques to have size **2 or 3**, i.e. **edges and triangles**. ([arXiv][1])

* **For (r\ge 3): open (as far as the standard references indicate).**
  This is stated as an open conjecture of Erdős and Sauer (it appears explicitly as Erdős Problem #719). ([Erdős Problems][2])

So the current best concise answer is:

* **Yes for (r=2)** (classical theorem).
* **Open for (r\ge 3)** (Erdős–Sauer conjecture / Erdős Problem #719). ([Erdős Problems][2])

[1]: https://arxiv.org/pdf/1909.11371 "https://arxiv.org/pdf/1909.11371"
[2]: https://www.erdosproblems.com/719 "
  
    Erdős Problem #719
  
"
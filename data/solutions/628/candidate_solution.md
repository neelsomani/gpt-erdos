This is **exactly the Erdős–Lovász Tihany conjecture** [[nomath]](sometimes phrased as “$(a,b)$-splittable”)[[/nomath]]. ([Erdős Problems][1])

To see the match: your hypotheses say (\chi(G)=k=a+b-1) and “no (K_k)” is the same as (\omega(G)<\chi(G)). The Tihany conjecture asserts that for every graph with (\omega(G)<\chi(G)=a+b-1), the vertex set can be split into two (vertex-)disjoint parts whose induced subgraphs have chromatic numbers at least $a$ and $b$. 
(Your formulation only asks for **two disjoint subgraphs**; since adding edges/vertices cannot *decrease* chromatic number, one can always replace “subgraph” by the induced subgraph on its vertex set, and any leftover vertices can be assigned to either side without lowering the chromatic numbers. So it is essentially the same splitting problem.)

### Status (as of early 2026)

**Open in general.** There is no known counterexample, but there is also no general proof. The conjecture is known in full generality only for a handful of small parameter pairs. 

Concretely, for **arbitrary graphs**, the only pairs $(a,b)$ for which the conjecture is known to hold are:
[
(a,b)\in {(2,2),(2,3),(2,4),(3,3),(3,4),(3,5)},
]
with proofs due to Brown–Jung (1969), Mozhan (1987), and Stiebitz (1987). 
In particular, Erdős’s original case (a=b=3) [[nomath]](so $k=5$)[[/nomath]] is true; Brown and Jung actually show the graph contains two vertex-disjoint odd cycles. ([Erdős Problems][1])

### Partial positive results for special graph classes

While the general conjecture is open, it **is proved for some important classes** of graphs. For example:

* **Quasi-line graphs** and **graphs with independence number (\alpha(G)=2)** satisfy the full conjecture [[nomath]](all $(a,b)$)[[/nomath]]. ([Erdős Problems][1])
* There is continuing progress for **claw-free graphs** and other structured families; e.g. a 2026 Discrete Mathematics paper proves additional $(s,t)$ ranges under claw-free / clique-containing hypotheses, and also emphasizes that for general graphs the exact-known pairs remain the small list above. ([ScienceDirect][2])

So the answer to “must there exist?” is:

* **In full generality: not known (open).** ([Erdős Problems][1])
* **Yes** for the specific small $(a,b)$ pairs above, and **yes** for several special graph classes [[nomath]](e.g. quasi-line graphs, $\alpha(G)=2$)[[/nomath]]. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/628 "
  
    Erdős Problems
  
"
[2]: https://www.sciencedirect.com/science/article/abs/pii/S0012365X25003784 "Some cases of the Erdős-Lovász Tihany conjecture for claw-free graphs - ScienceDirect"

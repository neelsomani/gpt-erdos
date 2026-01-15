This is **not known in general**.

It is exactly the **Erdős–Gyárfás conjecture** (posed in 1995): every *finite* graph with minimum degree at least 3 should contain a simple cycle whose length is a power of 2 [[nomath]](so, in your phrasing, some $2^k$ with $k\ge 2$)[[/nomath]]. ([Wikipedia][1])

What *is* known:

* **No counterexample is known**, but computer searches show any counterexample would have to be fairly large: at least **17 vertices**, and if one exists that is **cubic (3-regular)** then it must have at least **30 vertices**; bipartite counterexamples (if any) must have at least **32 vertices**. ([Wikipedia][1])
* There are “near misses”: e.g. Markström found 24-vertex cubic graphs with **no 4- or 8-cycles**, but they still have a **16-cycle**, so they are *not* counterexamples. ([Wikipedia][1])

And the conjecture **has been proved for several special classes**, for example:

* **3-connected cubic planar graphs** satisfy the conjecture. ([Combinatorics][2])
* Graphs with **no induced path on 10 vertices** [[nomath]]($P_{10}$-free graphs)[[/nomath]] satisfy it—in fact they must contain a **4-cycle or an 8-cycle**. ([ScienceDirect][3])
* More recently, it has been pushed further (with computer aid) to **(P_{13})-free graphs**. 
* If the graph has **diameter 2** [[nomath]](still with minimum degree $\ge 3$)[[/nomath]], then it contains a **4-cycle or 8-cycle**. ([arXiv][4])
* If the **average degree/minimum degree is sufficiently large** (above some absolute constant), then the conjecture holds (indeed, much stronger “many even lengths” results hold). ([Erdős Problems][5])

So the current state is: **the statement is a famous open problem**, verified in many important special cases and for small graphs by computation, but **still unproved (and un-disproved) for general finite graphs of minimum degree 3**. ([Wikipedia][1])

[1]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture "Erdős–Gyárfás conjecture - Wikipedia"
[2]: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v20i2p7 "
		Erdös-Gyárfás Conjecture for Cubic Planar Graphs
							\| The Electronic Journal of Combinatorics
			"
[3]: https://www.sciencedirect.com/science/article/abs/pii/S0012365X24003066 "The Erdős-Gyárfás conjecture holds for P10-free graphs - ScienceDirect"
[4]: https://arxiv.org/abs/2508.19302 "[2508.19302] Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum Degree at Least 3"
[5]: https://www.erdosproblems.com/forum/thread/64 "

    Erdős Problem #64 - Discussion thread

"

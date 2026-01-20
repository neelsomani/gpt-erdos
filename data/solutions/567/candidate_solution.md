This is exactly the (still-famous) question of whether these graphs are **Ramsey size-linear**.

### What “(R(G,H)\ll m)” means here

A graph $G$ is called **Ramsey size-linear** if there is a constant (C_G) such that for every graph $H$ with **no isolated vertices**,
[
R(G,H)\le C_G,e(H),
]
i.e. linear in the number of edges of $H$. [[nomath]](Equivalently, since no isolated vertices implies $v(H)\le 2e(H)$, this is linear in $m=e(H)$.)[[/nomath]] ([memphis.edu][1])

### Status for (G\in{Q_3,;K_{3,3},;H_5})

These three graphs were explicitly singled out by Erdős–Faudree–Rousseau–Schelp as “test cases” for size-linearity, asking exactly whether
[
R(G,H)\le c,m
]
for all $m$-edge graphs $H$ with no isolated vertices. 

**As of the end of 2025 / January 2026, this is still open in full generality** for all three of (Q_3), (K_{3,3}), and (H_5). ([Erdős Problems][2])

### What *is* known [[nomath]](notably for $H_5$)[[/nomath]]

The graph (H_5) is also known as (K_4^*): the graph obtained from (K_4) by subdividing one edge once. ([Erdős Problems][2])

Recent progress (Bradač–Gishboliner–Sudakov, published 2024) gives two important partial results:

* **Bipartite $H$:** for every **bipartite** graph $F$ with no isolated vertices,
  [
  R(K_4^*,F)=O(e(F)).
  ]
  So the desired linear-in-$m$ bound holds for (H_5) against all bipartite $H$. ([ETH Zurich Math Homepages][3])

* **All other subdivisions of (K_4):** every subdivision of (K_4) on at least 6 vertices is Ramsey size-linear. ([ETH Zurich Math Homepages][3])

But **for (H_5) against general (not necessarily bipartite) $H$**, the full statement (R(H_5,H)\ll e(H)) remains open. ([Erdős Problems][2])

### Useful general facts around the boundary

From the classical work on size-linear graphs (summarized in Balister–Schelp–Simonovits’s note):

* If $G$ is connected and (e(G)\le v(G)+1), then $G$ is Ramsey size-linear.
* If (e(G)\ge 2v(G)-2), then $G$ is **not** Ramsey size-linear.
* Also, certain bipartite graphs with extremal number $ex(n,G)=O(n^{3/2})$ are Ramsey size-linear. ([memphis.edu][1])

Your three graphs all lie in the “hard middle range” between these easy sufficient/necessary criteria, which is why they’ve persisted as benchmark open cases.

### Bottom line

* **For (Q_3): open.**
* **For (K_{3,3}): open** (Erdős even emphasized this case). ([Erdős Problems][2])
* **For (H_5): open in general**, but **known true when $H$ is bipartite**. ([ETH Zurich Math Homepages][3])

If you tell me what class of graphs $H$ you care about (e.g. bipartite, bounded degeneracy, bounded max degree, etc.), I can summarize the strongest known linear (or near-linear) bounds in that regime.

[1]: https://www.memphis.edu/msci/people/pbalistr/ramsl.pdf "https://www.memphis.edu/msci/people/pbalistr/ramsl.pdf"
[2]: https://www.erdosproblems.com/forum/thread/567 "

    Erdős Problem #567 - Discussion thread

"
[3]: https://people.math.ethz.ch/~sudakovb/ramsey-size-linear-graphs.pdf "On Ramsey Size-Linear Graphs and Related Questions | SIAM Journal on Discrete Mathematics | Vol. 38, No. 1 | Society for Industrial and Applied Mathematics"

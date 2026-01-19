As stated [[nomath]](with **no further closure assumptions on** $S$)[[/nomath]], the answer is **no**.

### A simple counterexample

Let $R(3;n)$ be the usual $n$-colour Ramsey number for a monochromatic triangle, and let
[
S={,K_{R(3;n)} : n\in\mathbb N,}.
]
Then for each $n$, take (G_n=K_{R(3;n)}\in S). By definition of $R(3;n)$, **every** $n$-edge-colouring of (G_n) contains a monochromatic triangle.

But now suppose there were a graph $G$ such that **every finite subgraph** of $G$ lies in $S$. If $G$ has even a single edge, then it has (K_2) as a finite subgraph. However (K_2\notin S) [[nomath]](every graph in $S$ is a complete graph on at least $3$ vertices)[[/nomath]]. Hence $G$ must be **edgeless**, so it has **no** triangle at all—therefore it certainly does **not** have the property that every (\aleph)-colouring of its edges yields a monochromatic triangle.

So the statement is **false in general**.

---

### The “intended” hereditary version is (apparently) open

If one adds a natural extra condition such as “$S$ is **hereditary** (closed under taking subgraphs)”, then the above trivial counterexample disappears. In that strengthened form, this question is recorded as an Erdős problem and is listed as **open** in the Erdős Problems database. ([Erdős Problems][1])

---

### Context: for complete graphs the infinite-colour threshold is known

For comparison, if you drop the $S$-restriction and just ask for a complete graph that forces a monochromatic triangle under (\kappa) colours [[nomath]](infinite $\kappa$)[[/nomath]], there is a clean answer:

* There is a standard (\kappa)-colouring of (K_{2^\kappa}) with **no** monochromatic triangle [[nomath]](e.g. for $\kappa=\aleph_0$ a concrete “first differing binary digit” colouring of $\mathbb R$ is described on MathOverflow)[[/nomath]]. ([MathOverflow][2])
* On the other hand, Erdős–Rado implies ((2^\kappa)^+\rightarrow(\kappa^+)^{2}*{\kappa}), which in particular gives
  [
  K*{(2^\kappa)^+}\rightarrow (K_3)_\kappa.
  ]
  ([Wikipedia][3])

So **for complete graphs**, ((2^\kappa)^+) vertices suffice [[nomath]](and $2^\kappa$ vertices do not)[[/nomath]].

A corresponding immediate **positive** special case for your question is: if $S$ contains **all** finite cliques (K_m) [[nomath]](so that $K_{(2^\kappa)^+}$ has all finite subgraphs in $S$)[[/nomath]], then taking (G=K_{(2^\kappa)^+}) works by Erdős–Rado. ([Wikipedia][3])

---

If you tell me whether you intended $S$ to be hereditary / closed under subgraphs (as is common in “age”/Fraïssé-style formulations), I can focus on what is known in that stronger setting and what kinds of additional hypotheses on $S$ make the statement provable.

[1]: https://www.erdosproblems.com/forum/thread/638 "https://www.erdosproblems.com/forum/thread/638"
[2]: https://mathoverflow.net/questions/35838/monochromatic-cycle-free-colouring-of-the-complete-graph-on-r?utm_source=chatgpt.com "monochromatic cycle-free colouring of the complete graph ..."
[3]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Rado_theorem "https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Rado_theorem"

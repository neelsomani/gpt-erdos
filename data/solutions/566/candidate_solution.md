If the implied constant in (R(G,H)\ll m) is meant to be **absolute** [[nomath]](independent of $G$)[[/nomath]], then **no**: take (H=K_2) [[nomath]](so $m=1$)[[/nomath]]. Then (R(G,K_2)=|V(G)|), which can be arbitrarily large even for graphs $G$ satisfying your sparsity condition (e.g. long paths/cycles).

The interesting interpretation (and the standard one in this area) is:

> For each fixed $G$, does there exist a constant (C_G) such that for every graph $H$ with no isolated vertices,
> $R(G,H)\le C_G e(H)=C_Gm ?$
> (This is exactly the definition of “Ramsey size-linear”.) ([memphis.edu][1])

Under that interpretation, your hypothesis on $G$ is exactly the natural “$2$-density (\le 2)” condition, since
[
e(J)\le 2|V(J)|-3\quad\text{for all subgraphs }J
]
is equivalent to (m_2(G)\le 2), where (m_2) is the usual $2$-density parameter. 
This condition is also essentially **necessary** for size-linearity, because Spencer’s lower bound (R(G,K_n)=\tilde\Omega(n^{m_2(G)})) would otherwise give (R(G,K_n)=\omega(e(K_n))) when (m_2(G)>2). 

### Status: open in general

Erdős–Faudree–Rousseau–Schelp explicitly asked whether **every** graph $G$ with (m_2(G)\le 2) is Ramsey size-linear, and (as of the more recent literature) this is **still open**. 

So: **your statement is not known in general**.

### What is known (partial landscape)

Some foundational facts (again from Erdős–Faudree–Rousseau–Schelp and follow-ups):

* If $G$ is connected and (e(G)\le v(G)+1), then $G$ **is** Ramsey size-linear. ([memphis.edu][1])
* If (e(G)\ge 2v(G)-2), then $G$ **is not** Ramsey size-linear. ([memphis.edu][1])
  Your condition forces (e(G)\le 2v(G)-3), so it lives in the “intermediate” regime where the full characterization is genuinely hard. ([arXiv][2])

There are also substantial positive results inside your class (m_2(G)\le 2), but not a full theorem.

* **Cycles:** very strong “size-linear with constant $2$” type bounds are known. A January 2026 paper settles the remaining odd-cycle cases in the classic Erdős–Faudree–Rousseau–Schelp question, proving [[nomath]](for odd $k\ge 7$)[[/nomath]] that
  [
  R(C_k,H)\le 2e(H)+\left\lfloor\frac{k-1}{2}\right\rfloor
  ]
  for all $H$ with no isolated vertices, provided $e(H)$ is large enough compared to $k$. ([arXiv][2])

* **Subdivisions of (K_4):** a key stubborn example is (K_4^*), the graph obtained from (K_4) by subdividing **one** edge once. It satisfies your sparsity condition, but whether it is Ramsey size-linear against *all* $H$ is still open; however it *is* known to be size-linear against all **bipartite** $H$, and every (K_4)-subdivision on at least $6$ vertices is Ramsey size-linear. 

* **The general picture is complicated:** e.g. Wigderson (2025) showed there are infinitely many graphs that are not Ramsey size-linear but all proper subgraphs are, illustrating how subtle “borderline” behavior can be. ([research-collection.ethz.ch][3])

### Bottom line

* **Absolute (\ll) independent of $G$:** false [[nomath]](already fails with $H=K_2$)[[/nomath]].
* **(\ll) with constant depending on $G$:** this is exactly the “Ramsey size-linear” property, and **for your class (m_2(G)\le 2) it remains an open problem** in full generality. 

[1]: https://www.memphis.edu/msci/people/pbalistr/ramsl.pdf "https://www.memphis.edu/msci/people/pbalistr/ramsl.pdf"
[2]: https://arxiv.org/pdf/2601.10238 "https://arxiv.org/pdf/2601.10238"
[3]: https://www.research-collection.ethz.ch/bitstreams/b099bc2d-c85e-4328-8b8e-e55af2f54269/download "Infinitely many minimally non-Ramsey size-linear graphs"

Write (\vec\chi(D)) for the usual **dichromatic number of a digraph** $D$: the minimum number of colours needed so that each colour class induces an **acyclic** digraph. Your (\delta(G)) for an undirected graph $G$ is exactly
[
\delta(G)=\max{\vec\chi(D): D \text{ is an orientation of }G},
]
i.e. the **maximum** dichromatic number among all orientations of $G$. ([Cambridge Core][1])

## 1) Does large (\chi(G)) force large (\delta(G))?

This is a well-known open problem (Erdős–Neumann-Lara, 1979):

> For every integer $k$, does there exist (f_k) such that (\chi(G)>f_k \implies \delta(G)>k)? ([Cambridge Core][1])

It’s immediate that (f_1=1) and (f_2=3), but **it is still open whether (f_3) exists**, i.e. whether graphs can have arbitrarily large chromatic number while (\delta(G)\le 2). ([Cambridge Core][1])
This is also recorded as Erdős problem #761. ([Erdős Problems][2])

### What is known in support (but not a full answer)?

* **Complete graphs** already show (\delta) can be much smaller than (\chi), but still unbounded: Erdős and Neumann-Lara proved
  [
  c_1\frac{n}{\log n}\ \le\ \delta(K_n)\ \le\ c_2\frac{n}{\log n}
  ]
  for constants (c_1,c_2>0) [[nomath]](with $c_1\sim \tfrac12$, $c_2\sim 1$ for large $n$)[[/nomath]]. ([Cambridge Core][1])

* Mohar and Wu proved a **fractional** analogue: if the **fractional chromatic number** (\chi_f(G)>t), then the **fractional dichromatic number** (\delta_f(G)) satisfies
  [
  \delta_f(G)>\frac{t}{4\log(2et^2)}.
  ]
  Since (\delta(G)\ge \delta_f(G)), this gives lower bounds on (\delta(G)) for graphs with large (\chi_f(G)). ([Cambridge Core][1])
  [[nomath]](This does not settle the original conjecture because $\chi_f$ can stay bounded while $\chi$ grows.)[[/nomath]]

So at present: **no proof and no counterexample** is known for “large (\chi) forces large (\delta)” in general [[nomath]](beyond the trivial $k=2$ case)[[/nomath]].

## 2) Does large (\zeta(G)) force a subgraph with large (\delta)?

This is another open question, attributed to Erdős and Gimbel (and listed together with #761). ([Erdős Problems][2])

A key reason it’s of interest is that a positive answer here would imply a positive answer to $1$, via a theorem of Alon–Krivelevich–Sudakov:

* If (\chi(G)=n), then $G$ contains a (not necessarily induced) subgraph $H$ with **large cochromatic number**, in fact (\zeta(H)=\Omega\left(\frac{n}{\ln n}\right)), and more precisely (\zeta(H)\ge (1/4+o(1)),\frac{n}{\log_2 n}). ([ETH Zurich Mathematics People][3])

So if one could show “(\zeta) large (\Rightarrow \delta) large (in some subgraph)”, then combining with the Alon–Krivelevich–Sudakov result would yield “(\chi) large (\Rightarrow \delta) large”. ([ETH Zurich Mathematics People][3])

## Bottom line

* **Must** large chromatic number force large (\delta(G))? **Open** [[nomath]](Erdős–Neumann-Lara; unknown already for forcing $\delta(G)\ge 3$)[[/nomath]]. ([Cambridge Core][1])
* **Must** large cochromatic number force (some subgraph with) large (\delta)? **Also open**, and a positive resolution would imply a positive resolution of the first question using the Alon–Krivelevich–Sudakov theorem on finding large-cochromatic subgraphs in high-chromatic graphs. ([ETH Zurich Mathematics People][3])

[1]: https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/78CBB88EC47B8F258F4B0F05B626552F/S2050509416000281a.pdf/dichromatic_number_and_fractional_chromatic_number.pdf "https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/78CBB88EC47B8F258F4B0F05B626552F/S2050509416000281a.pdf/dichromatic_number_and_fractional_chromatic_number.pdf"
[2]: https://www.erdosproblems.com/761 "https://www.erdosproblems.com/761"
[3]: https://people.math.ethz.ch/~sudakovb/cochrom.pdf "https://people.math.ethz.ch/~sudakovb/cochrom.pdf"

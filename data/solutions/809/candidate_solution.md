What you are calling (F_k(n)) is exactly the “strong chromatic number” extremal function studied by Burr–Erdős–Graham–Sós in their 1989 paper: they define
[
xs(n,e,L)=\min_{G:|V(G)|=n,\ |E(G)|=e}\ xs(G,L),
]
where $xs(G,L)$ is the minimum number of edge‐colours needed so that **every** copy of $L$ in $G$ is *totally multicoloured* (i.e. rainbow). ([users.renyi.hu][1])
Your (F_k(n)) is $xs(n,\lfloor n^2/4\rfloor+1,C_{2k+1})$.

A key point is that for any fixed odd cycle (C_{2k+1}), for $n$ large enough one has
[
\mathrm{ex}(n,C_{2k+1})=t_2(n)=\\\lfloor\frac{n^2}{4}\\\rfloor,
]
so your edge count (t_2(n)+1) is exactly “one over extremal”, hence (C_{2k+1}) is forced and the condition is not vacuous. ([users.renyi.hu][1])

## Status of the asymptotic (F_k(n)\sim n^2/8)

As far as the standard references indicate, this is **open**.

* Burr–Erdős–Graham–Sós prove that for **odd cycles other than (C_3) and (C_5)** [[nomath]](in particular for all odd $C_{2k+1}$ with $2k+1\ge 7$)[[/nomath]], the function is **quadratic**: there is a constant (c=c(k)>0) with
  [
  F_k(n)\ge cn^2
  ]
  for all sufficiently large $n$. This is also recorded in the ErdosProblems entry for this question. ([Erdős Problems][2])

* In the same 1989 paper they **explicitly ask** whether one can take the sharp constant $1/8$, and they go further and state the precise asymptotic you wrote [[nomath]](in their notation for odd cycle length $k\ge 7$)[[/nomath]]:

  > “It may in fact be true that … if (e=t_2(n)+1), then [[nomath]](xs$n,e,C_k$=$1+o(1)$$n^2/8$)[[/nomath]].” ([Semantic Scholar][3])
  > Translating their $k$ (cycle length) to your $2k+1$, this is exactly your conjecture for (k\ge 3).

So: **the conjecture (F_k(n)\sim n^2/8) is (to the best of what these sources record) not proved nor disproved**; what is proved is only that (F_k(n)) has order of growth (\Theta(n^2)) for (2k+1\ge 7), with the leading constant unknown. ([Erdős Problems][2])

## Context: why $1/8$ is the “right” constant to hope for

The same paper emphasizes a trichotomy: (C_3) is easy/small, (C_5) behaves very differently, and **all other odd cycles force very large (quadratic) strong chromatic numbers**. ([users.renyi.hu][1])
Their comment that $1/8$ would be “best possible” is pointing at a plausible extremal constant in this quadratic regime. ([Semantic Scholar][3])

If you want, I can also restate the problem in the hypergraph language they use [[nomath]](edges of $G$ are “vertices” of a hypergraph whose hyperedges are the copies of $C_{2k+1}$)[[/nomath]], which often clarifies why it is hard: you are asking for the chromatic number of that hypergraph minimized over all $G$ with (t_2(n)+1) edges. ([users.renyi.hu][1])

[1]: https://users.renyi.hu/~sos/1989_Maximal_Antiramsey_Graphs_And_the_Strong_Chromatic_Number.pdf "Maximal antiramsey graphs and the strong chromatic number"
[2]: https://www.erdosproblems.com/latex/809 "https://www.erdosproblems.com/latex/809"
[3]: https://pdfs.semanticscholar.org/7f9d/4eb8362dd5d2a8c3f16c95d53f70426382be.pdf "https://pdfs.semanticscholar.org/7f9d/4eb8362dd5d2a8c3f16c95d53f70426382be.pdf"

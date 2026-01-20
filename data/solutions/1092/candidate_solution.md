No.

It’s convenient to rephrase your condition in “edge‐deletion distance to $r$-colorable.”
For a graph $H$, let
[
\tau_r(H):=\min{|F|:\ \chi(H-F)\le r},
]
i.e. the minimum number of edges you must delete from $H$ to make it $r$-colorable.
Then your hypothesis for $G$ is exactly: for every subgraph $H$ on $m$ vertices,
[
\tau_r(H)\le f_r(m).
]

## The case $r=2$

Rödl (1982) constructed graphs with arbitrarily large chromatic number that are *locally* “almost bipartite” in precisely this sense: for every (\varepsilon>0) and every $k$, for all sufficiently large $n$ there is a graph $G$ with
[
\chi(G)=k+2,
\qquad\text{and}\qquad
\text{every subgraph }H\text{ becomes bipartite after deleting }\le \varepsilon |V(H)|\text{ edges.}
]
This is stated explicitly in the discussion of Erdős problem #1092 (citing Rödl’s Theorem 1.5). ([Erdős Problems][1])
It also matches the formulation in the Springer abstract: Rödl’s note gives a negative answer to the question of whether some fixed (\varepsilon>0) would force (\chi(G)\le 3). ([Springer][2])

Now suppose (for contradiction) that (f_2(n)\gg n), i.e. there is a constant (c>0) such that [[nomath]](f_2$m$\ge cm)[[/nomath]] for all large $m$. Take (\varepsilon=c/2) and pick Rödl’s $G$ with (\chi(G)\ge 4). Then every subgraph $H$ satisfies (\tau_2(H)\le \varepsilon|V(H)|\le f_2(|V(H)|)), so $G$ meets the hypothesis defining (f_2), but $G$ is not $3$-colorable. Contradiction. This is exactly the argument recorded on the Erdős Problems page. ([Erdős Problems][1])

So (f_2(n)\not\gg n); in fact Rödl’s construction shows you cannot have any positive linear lower bound.

## General (r\ge 2)

The same Rödl examples also kill the $r$-statement [[nomath]](for every fixed $r\ge2$)[[/nomath]].

Indeed, if a subgraph $H$ can be made **bipartite** after deleting (\le \varepsilon|V(H)|) edges, then it can certainly be made **$r$-colorable** after deleting the same number of edges, because bipartite (\Rightarrow r)-colorable for all (r\ge2).

So for any fixed (r\ge2) and any candidate constant (c_r>0), choose (\varepsilon=c_r/2) and choose Rödl’s $G$ with (\chi(G)\ge r+2) [[nomath]](possible since he gets $\chi(G)=k+2$ for arbitrary $k$)[[/nomath]]. Then every subgraph $H$ satisfies
[
\tau_r(H)\le \tau_2(H)\le \varepsilon|V(H)|\le c_r|V(H)|,
]
yet (\chi(G)>r+1). Hence no linear lower bound (f_r(n)\gg_r n) can hold. ([Erdős Problems][1])

---

So:

* (f_2(n)\gg n) is false (Rödl 1982, also noted on Erdős Problems). ([Erdős Problems][3])
* More generally, for every fixed (r\ge2), (f_r(n)\gg_r n) is also false [[nomath]](by the same construction, since “almost bipartite” is stronger than “almost $r$-colorable”)[[/nomath]]. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/1092 "https://www.erdosproblems.com/forum/thread/1092"
[2]: https://link.springer.com/article/10.1007/BF02579434 "https://link.springer.com/article/10.1007/BF02579434"
[3]: https://www.erdosproblems.com/latex/1092 "
  
    Erdős Problems
  
"

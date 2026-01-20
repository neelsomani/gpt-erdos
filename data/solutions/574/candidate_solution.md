No one currently knows this in general, and it is **open already for $k=2$**.

### Why $k=2$ already blocks a “yes”

For $k=2$ your statement becomes
[
\mathrm{ex}(n;{C_3,C_4})=(1+o(1))(n/2)^{3/2},
]
i.e. the extremal number of graphs with **no triangle and no 4‑cycle** (girth at least 5). This is a long–standing open problem: recent work explicitly notes that the conjectured asymptotic ((n/2)^{3/2}+o(n^{3/2})) is still “widely open.” ([Cambridge University Press & Assessment][1])

What *is* known for $k=2$ is only a range of possible leading constants:
[
\frac{1}{2\sqrt2}\ \le\ \liminf_{n\to\infty}\frac{\mathrm{ex}(n;{C_3,C_4})}{n^{3/2}}
\ \le\
\limsup_{n\to\infty}\frac{\mathrm{ex}(n;{C_3,C_4})}{n^{3/2}}
\ \le\ \frac12,
]
and the exact asymptotic constant is unknown. 

There has also been recent progress showing (\mathrm{ex}(n;{C_3,C_4})) can exceed the “balanced bipartite” benchmark by a **superlinear** additive term [[nomath]](still lower order than $n^{3/2}$)[[/nomath]], which shows the problem is subtler than just “it’s asymptotically bipartite.” ([Cambridge University Press & Assessment][1])

### For $k=3$ and beyond, it’s also open

For $k=3$ the question is about (\mathrm{ex}(n;{C_5,C_6})). Verstraëte’s survey explicitly flags determining the asymptotics of (\mathrm{ex}(n,{C_5,C_6})) as an open problem. ([mathweb.ucsd.edu][2])

### A deeper reason: it would imply major open results about even cycles

Your proposed asymptotic would in particular give a matching-order lower bound for (\mathrm{ex}(n,C_{2k})), since
[
\mathrm{ex}(n,C_{2k}) \ \ge\ \mathrm{ex}(n;{C_{2k-1},C_{2k}}).
]
But the classical “even cycle” Turán problem [[nomath]](understanding $\mathrm{ex}(n,C_{2k})$)[[/nomath]] is itself only well understood in a few cases: Conlon notes that after decades, it is “only reasonably well understood” for cycle lengths $4,6,10$, and he even discusses conjectural reasons to suspect the standard upper-bound exponent might not be tight already for (C_8). 

### What bounds *are* known in general?

* **Upper bound:** forbidding (C_{2k}) alone already forces (\mathrm{ex}(n,C_{2k}) \le O_k(n^{1+1/k})) (Bondy–Simonovits “even circuit” type bounds), hence
  [
  \mathrm{ex}(n;{C_{2k-1},C_{2k}}) \le O_k(n^{1+1/k}). 
  ]
* **Lower bounds:** your ((n/2)^{1+1/k}) matches what one gets from very dense **balanced bipartite** constructions when they exist. For (k=2,3,5), Wenger-type bipartite constructions give (C_{2k})-free graphs with about ((n/2)^{1+1/k}) edges [[nomath]](after translating Conlon’s “two parts of size $n$” notation to total vertex count $2n$)[[/nomath]]. 
  For general $k$, comparable lower bounds are not known at that level of precision.

### Bottom line

As of now, the statement
[
\mathrm{ex}(n;{C_{2k-1},C_{2k}})=(1+o(1))(n/2)^{1+1/k}
]
is **not proved**, and it is **open already for $k=2$** [[nomath]](the ${C_3,C_4}$ case)[[/nomath]]. ([Cambridge University Press & Assessment][1])

[1]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/ED3AF154970DCE68C1EF742401F0A919/S205050942510100Xa.pdf/on_extremal_numbers_of_the_triangle_plus_the_fourcycle.pdf "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/ED3AF154970DCE68C1EF742401F0A919/S205050942510100Xa.pdf/on_extremal_numbers_of_the_triangle_plus_the_fourcycle.pdf"
[2]: https://mathweb.ucsd.edu/~jverstra/cycles-survey-final-revision.pdf?utm_source=chatgpt.com "Extremal problems for cycles in graphs"

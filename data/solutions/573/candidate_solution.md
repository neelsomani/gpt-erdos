It’s **not known**. The statement
[
\mathrm{ex}(n;{C_3,C_4})\sim\left(\frac n2\right)^{3/2}
]
is essentially **Erdős’s conjecture** and remains **wide open**.

### What is known

Let $z(n,C_4)$ be the **Zarankiewicz number**: the maximum number of edges in an $n$-vertex **bipartite** (C_4)-free graph. Since bipartite graphs are automatically triangle-free,
[
\mathrm{ex}(n;{C_3,C_4})\ \ge\ z(n,C_4).
]
Moreover,
[
z(n,C_4)=\left(\frac n2\right)^{3/2}+o(n^{3/2}),
]
and in fact explicit two-sided estimates of the form
[
\left(\frac n2\right)^{3/2}-cn^{4/3}\ \le\ z(n,C_4)\ \le\ \left(\frac n2\right)^{3/2}+\frac14 n
]
are known. 

So we get the lower bound
[
\mathrm{ex}(n;{C_3,C_4})\ \ge\ \left(\frac n2\right)^{3/2}+o(n^{3/2}). 
]

On the other hand, the best general **upper bound** currently available is still the “trivial” one coming from forbidding only (C_4):
[
\mathrm{ex}(n;{C_3,C_4})\ \le\ \mathrm{ex}(n,C_4)\ =\ \frac12n^{3/2}+O(n). 
]

So the leading constant is only known to lie in the range
[
\frac{1}{2\sqrt2}\ \le\ \liminf_{n\to\infty}\frac{\mathrm{ex}(n;{C_3,C_4})}{n^{3/2}}
\ \le\
\limsup_{n\to\infty}\frac{\mathrm{ex}(n;{C_3,C_4})}{n^{3/2}}
\ \le\ \frac12.
]

### The conjecture, and why your formula is “the” famous one

Erdős conjectured that the bipartite construction is asymptotically optimal, i.e.
[
\mathrm{ex}(n;{C_3,C_4})=\left(\frac{1}{2\sqrt2}+o(1)\right)n^{3/2},
]
which is exactly the same as (\mathrm{ex}(n;{C_3,C_4})\sim (n/2)^{3/2}). 

Equivalently, in the modern formulation:
[
\lim_{n\to\infty}\frac{\mathrm{ex}(n;{C_3,C_4})}{z(n,C_4)}=1,
]
and this is stated as “still widely open” in a 2025 paper of Ma–Yang. 

### Recent progress (doesn’t settle the asymptotic, but is important)

Even though the leading-term conjecture is open, we now know that (\mathrm{ex}(n;{C_3,C_4})) can be **strictly larger** than $z(n,C_4)$ by a **superlinear** amount:

* Ma–Yang (2025) prove that for every (n\ge 7),
  [
  \mathrm{ex}(n;{C_3,C_4}) \ge z(n,C_4) + cn^{1.25}.
  ]

* In particular, for infinitely many $n$ [[nomath]](e.g. $n=2(q^2+q+1)$ with $q$ a prime power)[[/nomath]],
  [
  \mathrm{ex}(n;{C_3,C_4})=\left(\frac n2\right)^{3/2}+\Omega(n^{1.25}),
  ]
  showing the error term can be **much larger than $O(n)$**. 

This **does not contradict** (\mathrm{ex}(n;{C_3,C_4})\sim (n/2)^{3/2}), because (n^{1.25}=o(n^{1.5})). It just says the second-order behavior is subtler than previously hoped.

### Competing conjecture

Interestingly, Allen–Keevash–Sudakov–Verstraëte have conjectured the **opposite direction** in a ratio sense:
[
\liminf_{n\to\infty}\frac{\mathrm{ex}(n;{C_3,C_4})}{z(n,C_4)} > 1,
]
i.e. that triangle-free + (C_4)-free graphs are asymptotically denser than the best bipartite (C_4)-free graphs. 

### Bottom line

* Your asymptotic (\mathrm{ex}(n;{C_3,C_4})\sim (n/2)^{3/2}) is a **major open conjecture** (Erdős’s).
* The best general bounds currently are
  [
  \left(\frac n2\right)^{3/2}+o(n^{3/2})
  \ \le\
  \mathrm{ex}(n;{C_3,C_4})
  \ \le\
  \frac12,n^{3/2}+O(n).
  ]

* Recent work shows (\mathrm{ex}(n;{C_3,C_4})) can exceed ((n/2)^{3/2}) by (\Omega(n^{5/4})) for infinitely many $n$, but this still leaves the leading constant unresolved. 

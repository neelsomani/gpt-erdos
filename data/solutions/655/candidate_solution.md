No.

Let $D$ be the number of distinct distances among the (\binom n2) pairs.

### 1) A universal lower bound is only (\approx n/2)

Fix a distance value $d$. Make a graph (G_d) on vertex set ({1,\dots,n}) where $ij$ is an edge iff (|x_i-x_j|=d).

Your condition says: for each $i$, there are **not** three points (x_j,x_k,x_\ell) all at the same distance from (x_i). Equivalently, for each fixed $d$,
[
\deg_{G_d}(i)\le 2 \quad \text{for every vertex } i.
]
Hence
[
2|E(G_d)|=\sum_i \deg_{G_d}(i)\le 2n \quad\Rightarrow\quad |E(G_d)|\le n.
]
Now sum over all distinct distances $d$:
[
\binom n2 = \sum_{d} |E(G_d)| \le D\cdot n,
]
so
[
D \ge \frac{\binom n2}{n}=\frac{n-1}{2}.
]
Since $D$ is an integer, this gives (D\ge \left\lceil\frac{n-1}{2}\right\rceil=\left\lfloor\frac n2\right\rfloor).

So the condition forces at least (\sim n/2) distances, but this argument alone cannot give ((1+c)\frac n2).

### 2) A configuration achieving only (\left\lfloor\frac n2\right\rfloor) distances exists

Take the $n$ points to be the vertices of a regular $n$-gon.

* **Condition holds:** From any vertex (x_i), for each (k=1,2,\dots,\lfloor n/2\rfloor), there are at most two vertices at “step” $k$ $clockwise/counterclockwise$ and they are at the same distance from (x_i). Thus every distance from (x_i) occurs at most twice [[nomath]](except when $n$ is even, the opposite vertex occurs once)[[/nomath]]. So no circle centered at (x_i) passes through three other vertices.

* **Number of distinct distances:** The distance between two vertices depends only on the step $k$, and equals the chord length
  [
  d_k = 2R\sin\left(\frac{k\pi}{n}\right),\qquad k=1,\dots,\left\lfloor\frac n2\right\rfloor,
  ]
  which are all distinct. Hence the whole set determines exactly (\left\lfloor\frac n2\right\rfloor) distinct distances.

Therefore for every (c>0) and all sufficiently large $n$,
[
\left\lfloor\frac n2\right\rfloor < (1+c)\frac n2,
]
so the proposed bound fails.

In fact, combining the counting lower bound with the regular $n$-gon construction shows the minimum possible number of distinct distances under your condition is exactly (\left\lfloor \frac n2\right\rfloor).

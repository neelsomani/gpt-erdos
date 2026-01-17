Write the **Lebesgue function**
$
\Lambda_X(x):=\sum_{k=1}^n |l_k(x)|,\qquad X={x_1<\cdots<x_n}\subset(-1,1),
$
and extend the partition points by (x_0=-1,\ x_{n+1}=1).
A basic (and very useful) fact is that (\Lambda_X) is *piecewise polynomial* and, on each subinterval $(x_i,x_{i+1})$, it has **exactly one** local maximum; if (\pm1) are not interpolation points, there are also local maxima “at the endpoints” (\pm1). ([DNB Portal][1])
So if we set
[
\lambda_i(X):=\max_{x\in[x_i,x_{i+1}]}\Lambda_X(x)\qquad (i=0,1,\dots,n),
]
then your quantity is simply the **smallest local maximum**
[
\Upsilon(X)=\min_{0\le i\le n}\lambda_i(X).
]

## 1) Is (\Upsilon(X)\ll \log n) for all $X$?

Yes — and the right “reason” is that the **max–min** problem you wrote down is already a classical extremal problem in interpolation theory (Bernstein–Erdős). One formulation (in modern notation) is:

* Let (M(X):=\max_i \lambda_i(X)=\max_{x\in[-1,1]}\Lambda_X(x)) be the usual **Lebesgue constant**.
* Let (m(X):=\min_i \lambda_i(X)=\Upsilon(X)) be the **smallest local maximum**.

Then there exists a distinguished point set (X^\*) (“Lebesgue–optimal nodes”) for which the local maxima are all equal (equioscillation), and for **every** node set $X$ one has the sandwich inequality
[
m(X)\ \le\ m(X^*)\ =\ M(X^*)\ \le\ M(X),
]
i.e. the same set (X^*) **maximizes the smallest** local maximum and **minimizes the largest** one. ([DNB Portal][1])
Equivalently,
[
\Upsilon(X)\le \Upsilon(X^*) = M(X^*).
]

Now $M(X^*)$ is the **optimal Lebesgue constant**, and it is known to have logarithmic growth:
[
M(X^*) = \frac{2}{\pi}\Big(\log(n+1)+\gamma+\log\frac{4}{\pi}\Big)+o(1)
\qquad (n\to\infty),
]
in the standard indexing conventions [[nomath]](shifting $n\mapsto n-1$ just changes $\log(n+1)$ to $\log n$ at this level)[[/nomath]]. ([DNB Portal][1])
Therefore,
[
\Upsilon(X)\ \le\ C\log n
]
for an absolute constant $C$, uniformly over all $X$.

Moreover, this is sharp in order: at the extremal set (X^\*), (\Upsilon(X^*)\sim \tfrac{2}{\pi}\log n).

## 2) Which (x_i) maximize (\Upsilon)?

They are exactly the **Lebesgue–optimal interpolation nodes** (X^*), characterized by an **equioscillation/equal–peak** property:

> The maximizer (X^\*={x_1^\*<\cdots<x_n^\*}) is the (unique) node set for which
> $\lambda_0(X^*)=\lambda_1(X^*)=\cdots=\lambda_n(X^*)$
> i.e. the $n+1$ “relative maxima” of (\Lambda_{X^*}) on the $n+1$ subintervals $[x_i^*,x_{i+1}^*]$ all have the **same height**. ([DNB Portal][1])

This is precisely the Bernstein–Erdős characterization: the optimal set is **unique**, **symmetric** (about 0), and its Lebesgue function must equioscillate. ([DNB Portal][1])  In general the points (x_i^*) do **not** have a simple closed form; explicit formulas are only known for very small degrees, and otherwise they are computed numerically (e.g. via a Remez-type exchange algorithm). ([DNB Portal][1])

### What do these maximizing nodes look like?

While not closed-form, their *shape* is well understood:

* They are **symmetric**: (x_{n+1-k}^\*=-x_k^\*). ([DNB Portal][1])
* They cluster toward (\pm1) with an asymptotic **arcsine/Chebyshev density**, i.e. heuristically
  [
  x_k^*\approx \cos\Big(\frac{(2k-1)\pi}{2n}\Big),
  ]
  (Chebyshev–Gauss nodes), with small $n$-dependent corrections. ([DNB Portal][1])
  There are also explicit *near-optimal* “modified Chebyshev” node families in the literature that achieve the same asymptotic (\frac{2}{\pi}\log n) growth. ([DNB Portal][1])

## Summary

* **Yes:** for every choice of nodes, (\Upsilon(x_1,\dots,x_n)=O(\log n)). In fact (\Upsilon(X)\le M(X^*)\sim \frac{2}{\pi}\log n). ([DNB Portal][1])
* The node set that **maximizes** (\Upsilon) is the unique **Lebesgue–optimal** set (X^*), characterized by **equal local maxima** (equioscillation) of the Lebesgue function on all $n+1$ subintervals. ([DNB Portal][1])
* Asymptotically, those points are distributed like **Chebyshev points** (arcsine law), so (x_k^*) are very close to (\cos((2k-1)\pi/(2n))) for large $n$. ([DNB Portal][1])

[1]: https://d-nb.info/1090940718/34 "https://d-nb.info/1090940718/34"

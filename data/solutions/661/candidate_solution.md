Interpreting the question in the usual nontrivial way [[nomath]](the $x_i$’s are $n$ **distinct** points and the $y_j$’s are $n$ **distinct** points; if repetitions are allowed then you can make the answer trivially “yes” by collapsing all $x_i$’s and all $y_j$’s)[[/nomath]], this is **open**.

A standard way to formalize it is to define
[
D(m,n)=\min_{|\mathcal P|=m,,|\mathcal Q|=n} \bigl|{,|p-q|: (p,q)\in \mathcal P\times \mathcal Q,}\bigr|
]
[[nomath]](the minimum number of distinct “bipartite” distances between an $m$-point set and an $n$-point set)[[/nomath]].

Your question is exactly asking whether
[
D(n,n)=o\left(\frac{n}{\sqrt{\log n}}\right)
]
can happen.

### What is known (best general bounds)

* **Upper bound:** One always has
  [
  D(n,n)\le D(2n)=O\left(\frac{n}{\sqrt{\log n}}\right),
  ]
  by taking a (\sqrt{2n}\times \sqrt{2n}) integer lattice patch (Erdős’ classic construction for the usual distinct distances problem) and then splitting the (2n) points into two sets of size $n$; the set of cross-distances is a subset of all distances in the (2n)-point configuration. 

* **Lower bound:** For the bipartite problem in the plane, the best general lower bound known for the “balanced” case $m=n$ is
  [
  D(n,n)=\Omega!\left(\frac{n}{\log n}\right).
  ]
  This follows from the more general bound (D(m,n)=\Omega(\sqrt{mn}/\log n)) in the range (n^{1/3}\le m\le n). ([arXiv][1])

So at present, for $m=n$,
[
\boxed{\ \Omega\left(\frac{n}{\log n}\right)\ \le\ D(n,n)\ \le\ O\left(\frac{n}{\sqrt{\log n}}\right)\ }
]
and there is a remaining gap of a factor (\sqrt{\log n}).

### Status of the specific little‑$o$ question

Whether one can improve the upper bound to **little‑$o$** of (n/\sqrt{\log n}) [[nomath]](even by a slowly vanishing factor, e.g. dividing by $\log\log n$, etc.)[[/nomath]] is currently regarded as **open**. ([erdosproblems.com][2])

[1]: https://arxiv.org/abs/1912.01883 "[1912.01883] On Bipartite Distinct Distances in the Plane"
[2]: https://www.erdosproblems.com/forum/thread/661 "

    Erdős Problem #661 - Discussion thread

"

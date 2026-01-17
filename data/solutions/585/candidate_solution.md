Let $f(n)$ be the maximum number of edges in an $n$-vertex (simple) graph that **does not** contain two **edge-disjoint** cycles with the **same vertex set**.

This is a classical question of **Erdős (1975)**, and the exact value of $f(n)$ is **not known** in general. ([arXiv][1])

What *is* known (best current bounds):

* **Lower bound:**
  There exist $n$-vertex graphs with
  [
  f(n)\ \ge\ c, n\log\log n
  ]
  edges [[nomath]](for some absolute constant $c>0$)[[/nomath]] that still avoid having two edge-disjoint cycles on the same vertex set. This comes from a construction of Pyber–Rödl–Szemerédi [[nomath]](via graphs with no $4$-regular subgraphs)[[/nomath]], and it implies the growth cannot be purely linear in $n$. ([arXiv][1])

* **Upper bound (2024/2025 breakthrough):**
  Chakraborti–Janzer–Methuku–Montgomery proved that there is a constant $t$ such that any $n$-vertex graph with at least
  [
  C, n(\log n)^t = n\cdot \mathrm{polylog}(n)
  ]
  edges must contain (in fact) $k$ edge-disjoint cycles with the same vertex set for any fixed (k\ge2); in particular for $k=2$, this gives
  [
  f(n)\ \le\ C, n(\log n)^t.
  ]
  ([arXiv][1])

So, in asymptotic terms, the currently best-known answer is:
[
\boxed{;c,n\log\log n\ \le\ f(n)\ \le\ C,n(\log n)^t;}
]
for some absolute constants (c,C,t>0). ([arXiv][1])

[[nomath]](Previously, only “Turán-type” arguments gave an upper bound around $n^{3/2+o(1)}$, and the new result brings this down to “almost linear” up to polylogarithmic factors.)[[/nomath]] ([arXiv][1])

[1]: https://arxiv.org/abs/2404.07190 "[2404.07190] Edge-disjoint cycles with the same vertex set"

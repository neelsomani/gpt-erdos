Your graphs are exactly the **minimum‑distance graphs** in the plane (equivalently, **penny graphs**): put a circle of diameter $1$ around each point; two vertices are adjacent iff the circles are tangent. In this model one gets two key structural facts:

* **Planarity:** every such graph is planar.
* **Degree bound:** every vertex has degree (\le 6) (the planar “kissing number” for equal circles). ([Springer][1])

Let $g(n)$ be the minimum possible independence number over all $n$-vertex graphs of this type [[nomath]](this is the same function denoted $F(n)$ or $\alpha_m(n,\mathbb E^2)$ in the literature)[[/nomath]]. Then:

## Linear growth and existence of the limit

Because you can take two extremal configurations on $n$ and $m$ points and place them far apart, you get
[
g(n+m)\ \le\ g(n)+g(m),
]
i.e. $g$ is **subadditive**. By Fekete’s lemma, the limit
[
\lim_{n\to\infty}\frac{g(n)}{n}
]
**exists** and equals (\inf_n g(n)/n). (So you don’t need to worry about limsup/liminf.)

## Best known bounds (as of 2025)

A basic bound comes from 4-colorability: any planar graph has an independent set of size at least $n/4$. For these graphs, Swanepoel notes you can even avoid the full Four Color Theorem because one can always find a vertex of degree (\le 3) and color greedily. ([Springer][1])

The record improvements are:

* **Lower bound:**
  [
  g(n)\ \ge\ \frac{8}{31},n \approx 0.258064,n.
  ]
  This is Swanepoel’s Theorem 1 for the Euclidean plane. ([Springer][1])
  [[nomath]](Earlier: Pollack $n/4$, Csizmadia $9n/35$. $[Springer][1]$)[[/nomath]]

* **Upper bound (construction):**
  [
  g(n)\ \le\ \left\lceil \frac{5}{16},n \right\rceil = 0.3125,n \quad\text{for large }n,
  ]
  due to Pach–Tóth, improving an earlier $6n/19$ construction. ([Springer][1])

These remain the **current record bounds** in the standard references and compilations through at least Oct 2, 2025. ([Erdős Problems][2])

## Therefore, for the limit

Let
[
c^* = \lim_{n\to\infty}\frac{g(n)}{n}.
]
Then the best known interval is
[
\frac{8}{31}\ \le\ c^*\ \le\ \frac{5}{16},
]
i.e.
[
0.258064\ldots \ \le\ c^*\ \le\ 0.3125.
]
Determining the exact constant (c^*) (or substantially tightening the interval) is open. ([Erdős Problems][2])

If you want, I can also summarize (at a high level) what goes into Swanepoel’s $8/31$ discharging-style argument and what Pach–Tóth’s $5/16$ construction looks like geometrically.

[1]: https://link.springer.com/content/pdf/10.1007/s00454-002-2897-y.pdf "/c/1997c/tops/dvips"
[2]: https://www.erdosproblems.com/1066 "
  
    Erdős Problem #1066
  
"

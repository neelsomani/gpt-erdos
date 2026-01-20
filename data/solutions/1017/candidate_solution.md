Write (\operatorname{cp}(G)) for the **clique partition number** of $G$: the minimum $t$ such that $E(G)$ can be partitioned into $t$ edge-disjoint complete graphs. Then
[
f(n,k)=\max{\operatorname{cp}(G): |V(G)|=n,\ |E(G)|=k}.
]

### Universal bound [[nomath]](works for all $k$)[[/nomath]]

Erdős–Goodman–Pósa proved that every $n$-vertex graph admits an edge-partition into **at most (\lfloor n^2/4\rfloor)** cliques (in fact, edges and triangles suffice), and this is tight at (k\approx n^2/4) [[nomath]](balanced $K_{\lfloor n/2\rfloor,\lceil n/2\rceil}$)[[/nomath]]. ([Erdős Problems][1])
So for all $k$,
[
f(n,k)\le \left\lfloor \frac{n^2}{4}\right\rfloor .
]

The point of your question is: once (k>n^2/4) (so triangles are forced), how much smaller can the *worst-case* (\operatorname{cp}(G)) be?

---

## Translating “extra edges” into “triangles” [[nomath]](the $k>n^2/4$ regime)[[/nomath]]

Let
[
k=\left\lfloor \frac{n^2}{4}\right\rfloor+m,\qquad m>0.
]

If $G$ is (K_4)-free, then every clique in a partition is either an edge ((K_2)) or a triangle ((K_3)). In that case, if you can find $t$ **edge-disjoint triangles**, you get a clique partition with
[
(\text{edges not in triangles})+(\text{triangles})
= (k-3t)+t = k-2t
]
cliques. So bounding how many edge-disjoint triangles are forced gives a bound on (\operatorname{cp}(G)).

### Exact answer in the (K_4)-free case

Győri–Keszegh proved the sharp statement:

> Every (K_4)-free graph with $n$ vertices and (\lfloor n^2/4\rfloor+m) edges contains $m$ pairwise edge-disjoint triangles. ([Springer][2])

Therefore every such (K_4)-free graph has a clique partition into at most
[
k-2m=\left\lfloor \frac{n^2}{4}\right\rfloor-m
]
cliques, and this is the “right” linear improvement in that setting.

So:
[
f_{K_4\text{-free}}!\left(n,\left\lfloor \frac{n^2}{4}\right\rfloor+m\right)
= \left\lfloor \frac{n^2}{4}\right\rfloor-m .
]

---

## Best unconditional “sharpening” known for general graphs

For *arbitrary* graphs [[nomath]](not assuming $K_4$-free)[[/nomath]], the best general quantitative improvement I can point to from the literature is via guaranteed triangle packings above Mantel’s threshold. In particular, Král’, Lidický, Pfender, and Volec prove (as a corollary of their optimal edge/triangle decomposition results) that an $n$-vertex graph with (\lfloor n^2/4\rfloor+m) edges contains
[
\left(\frac{2}{3}m-o(n^2)\right)
]
edge-disjoint triangles. 

Plugging (t\ge \frac{2}{3}m-o(n^2)) into (\operatorname{cp}(G)\le k-2t) gives an unconditional bound:
[
\operatorname{cp}(G)\ \le\ \left\lfloor \frac{n^2}{4}\right\rfloor+m\ -\ 2\left(\frac{2}{3}m-o(n^2)\right)
\ =\ \left\lfloor \frac{n^2}{4}\right\rfloor\ -\ \frac{1}{3}m\ +\ o(n^2).
]
Equivalently, for fixed edge density (k=(\tfrac14+\varepsilon)n^2) [[nomath]](constant $\varepsilon>0$)[[/nomath]],
[
f(n,k)\ \le\ \\(\tfrac14-\tfrac{\varepsilon}{3}+o(1)\\)n^2.
]

---

## What you can safely say as an “estimate”

Let (k=\lfloor n^2/4\rfloor+m) with (m>0).

* Always:
  [
  f(n,k)\le \left\lfloor \frac{n^2}{4}\right\rfloor
  ]
  (Erdős–Goodman–Pósa). ([Erdős Problems][1])

* In the (K_4)-free extremal setting (where cliques are only edges/triangles):
  [
  f_{K_4\text{-free}}(n,k)=\left\lfloor \frac{n^2}{4}\right\rfloor-m
  ]
  (Győri–Keszegh). ([Springer][2])

* For general graphs, the best asymptotic *guaranteed* sharpening I can cite is
  [
  f(n,k)\ \le\ \left\lfloor \frac{n^2}{4}\right\rfloor-\frac13\bigl(k-\lfloor n^2/4\rfloor\bigr)+o(n^2).
  ]


Determining the true asymptotics of $f(n,k)$ for general graphs in the whole range (k>n^2/4) is (in Erdős’s formulation) an open-ended “sharpening” problem; this is explicitly recorded as open in the problem literature. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/1017 "

    Erdős Problem #1017 - Discussion thread

"
[2]: https://link.springer.com/article/10.1007/s00493-016-3500-0 "On the Number of Edge-Disjoint Triangles in K4-Free Graphs | Combinatorica | Springer Nature Link"

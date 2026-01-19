No — not as stated [[nomath]](with $f(t)$ coming from the triangular/hexagonal lattice)[[/nomath]].

I’ll interpret your $f(t)$ the way your examples suggest: for the triangular lattice (\Lambda_{\triangle}) with nearest–neighbor distance $1$, $f(t)$ is the number of *other* lattice points within Euclidean distance (\le t) of a given lattice point. [[nomath]](So for $1\le t<\sqrt3$, one has $f(t)=6$; at $t=\sqrt3$, it jumps to $12$, etc.)[[/nomath]]

## A concrete counterexample for (t<\sqrt3)

Take instead the **square lattice**
[
\Lambda_{\square}=\mathbb{Z}^2
]
with spacing $1$. It also satisfies (d(x,y)\ge 1) for distinct lattice points.

Now fix any $t$ with
[
\sqrt2 < t < \sqrt3.
]

* In the **triangular lattice**, since (t<\sqrt3), you only see the 6 nearest neighbors at distance $1$. Thus
  [
  f_{\triangle}(t)=6.
  ]

* In the **square lattice**, each lattice point has

  * 4 neighbors at distance $1$: ((\pm1,0),(0,\pm1)),
  * 4 neighbors at distance (\sqrt2): $(\pm1,\pm1)$.

  Since (\sqrt2 < t), all 8 of these lie within distance $t$. Hence
  [
  f_{\square}(t)\ge 8.
  ]

So for every (t\in(\sqrt2,\sqrt3)), there exists a unit-separated set [[nomath]](a big patch of $\mathbb{Z}^2$, or the whole lattice)[[/nomath]] in which a typical interior point has **8** other points within distance (\le t), which is **strictly larger** than the triangular lattice’s **6** for the same $t$.

This already disproves the proposed universal upper bound “(\le f(t))” with $f(t)$ taken from the triangular lattice.

## If you meant the *total number of pairs* with distance (\le t)

If your intended quantity is the number of pairs
[
|\\{,{i,j}: i<j,\ d(x_i,x_j)\le t,\\}|,
]
then the same square-lattice construction beats the triangular lattice [[nomath]](for $t\in(\sqrt2,\sqrt3)$)[[/nomath]] by a linear factor.

Take an (m\times m) grid
[
{(i,j): 1\le i,j\le m},
\qquad n=m^2.
]
For any $t$ with (\sqrt2 < t < 2) [[nomath]](hence also for $\sqrt2 < t < \sqrt3$)[[/nomath]] the only pairs at distance (\le t) are exactly the horizontal/vertical adjacencies [[nomath]](distance $1$)[[/nomath]] and the diagonals of unit squares [[nomath]](distance $\sqrt2$)[[/nomath]]. Count them:

* horizontal edges: $m(m-1)$,
* vertical edges: $m(m-1)$,
* diagonals in each of ((m-1)^2) unit squares: (2(m-1)^2).

Total:
[
2m(m-1)+2(m-1)^2
=4m^2-6m+2
=4n-6\sqrt n+2.
]
So asymptotically you get (\sim 4n) pairs with distance (\le t).

But for (t<\sqrt3), the triangular lattice only contributes “nearest-neighbor” type short pairs [[nomath]](length $1$)[[/nomath]], giving asymptotically (\sim 3n) such pairs in large patches. So for (\sqrt2<t<\sqrt3), the square grid has **strictly more** close pairs than the triangular lattice.

## Your “in particular” question

> “In particular, is it true that the number of distances (\le \sqrt3-\varepsilon) is less than $1$?”

Interpreting this in the natural “count pairs” or “count neighbors” sense, this is **definitely false**.

Choose any
[
0<\varepsilon<\sqrt3-\sqrt2 \approx 0.3178,
]
so that
[
\sqrt2 < \sqrt3-\varepsilon < \sqrt3.
]
Then in the square lattice (\mathbb{Z}^2),

* every interior point has **8** neighbors within distance (\le \sqrt3-\varepsilon),
* and an (m\times m) grid has about (4n) such close pairs.

So there are *many* distances (\le \sqrt3-\varepsilon), not “less than $1$”.

---

If you tell me which exact quantity you want to extremize (per-point neighbor count? total number of pairs? average degree? and whether points are constrained to lie in a bounded region), I can also say what *is* known or plausible in that precise formulation. But with the usual meanings, the triangular lattice is **not** extremal for all $t$, and (t\in(\sqrt2,\sqrt3)) already gives clean counterexamples.

It depends what you mean by “(\gg)”, but in either standard interpretation the situation is basically “known for (r=2,3), open for (r\ge 4)”.

### 1) If you mean “(\gg)” = **(\Omega(\cdot))** (a constant-factor lower bound)

Then you’re asking whether the Kővári–Sós–Turán upper bound is tight in the *balanced* case (K_{r,r}), i.e. whether
[
\mathrm{ex}(n,K_{r,r}) \ge c_r n^{2-1/r}
\quad\text{for some }c_r>0.
]
This is a special case of the classical Zarankiewicz problem / conjecture (balanced case), and:

* **True for (r=2)**: (\mathrm{ex}(n,K_{2,2})=\mathrm{ex}(n,C_4)=\Theta(n^{3/2})). ([TAU Math][1])
* **True for (r=3)**: (\mathrm{ex}(n,K_{3,3})=\Theta(n^{5/3})); a matching lower bound was proved by Brown (1966). ([VU Web][2])
* **Open for (r\ge 4)**: even (r=4) is wide open; e.g. it has been explicitly noted that the “fundamental question” of (\mathrm{ex}(n,K_{t,t})) is wide open even for (t=4). ([UserPages][3])

What *is* known in general is a weaker probabilistic lower bound: for (s\le t),
[
\mathrm{ex}(n,K_{s,t}) \ge c, n^{,2-\frac{s+t-2}{st-1}},
]
so in particular for (s=t=r),
[
\mathrm{ex}(n,K_{r,r}) \ge c, n^{,2-\frac{2}{r+1}},
]
which is strictly smaller than (n^{2-1/r}) for every (r\ge 2). ([TAU Math][1])

There *are* constructions matching the KST exponent $2-1/r$ for many **unbalanced** graphs (K_{r,s}) when $s$ is sufficiently large compared to (r) (notably via (projective) norm graphs), but that does **not** settle the balanced case (s=r). ([UserPages][3])

### 2) If you mean “(\gg)” = **(\omega(\cdot))** (“grows faster than”)

Then the answer is **no for fixed $r$**, because the Kővári–Sós–Turán theorem gives
[
\mathrm{ex}(n,K_{r,r}) = O\left(n^{2-1/r}\right),
]
so it cannot be asymptotically larger than (n^{2-1/r}) by more than a constant factor. ([TAU Math][1])

---

So, in the most common extremal-graph-theory reading [[nomath]](“$\gg$” = $\Omega$)[[/nomath]]: **yes for (r=2,3), unknown for (r\ge 4)**; and in the “much larger” reading [[nomath]](“$\gg$” = $\omega$)[[/nomath]]: **definitely false** [[nomath]](for fixed $r$)[[/nomath]].

[1]: https://www.math.tau.ac.il/~asafico/ext-graph-theory/notes.pdf "https://www.math.tau.ac.il/~asafico/ext-graph-theory/notes.pdf"
[2]: https://web.vu.lt/mif/s.jukna/Knizka/Brown.pdf "https://web.vu.lt/mif/s.jukna/Knizka/Brown.pdf"
[3]: https://page.mi.fu-berlin.de/szabo/PDF/SubgraphsPNG.pdf "https://page.mi.fu-berlin.de/szabo/PDF/SubgraphsPNG.pdf"

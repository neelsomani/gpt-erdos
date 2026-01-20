Write $E(X)$ for the number of pairs ({x_i,x_j}) at distance exactly $1$ in a set (X\subset \mathbb{R}^d) with (|x_i-x_j|\ge 1) for all (i\ne j). Then your (f_d(n)) is
[
f_d(n)=\max{E(X): |X|=n,\ |x_i-x_j|\ge 1}.
]

A convenient reformulation is: put closed balls of radius $1/2$ around the points. The condition “all distances (\ge 1)” means these balls have disjoint interiors, and a pair of points at distance $1$ is exactly a *touching pair* of balls. So (f_d(n)) is the classical **contact number** of a packing of $n$ congruent balls (up to scaling). ([arXiv][1])

## Universal (and essentially sharp) linear bound via kissing numbers

Let $k(d)$ be the **kissing number** in (\mathbb{R}^d): the maximum number of non-overlapping congruent balls that can touch one given ball. ([arXiv][1])

Fix a point (p\in X). All points (q\in X) with (|p-q|=1) correspond to balls of radius $1/2$ touching the ball around $p$, and they cannot overlap each other [[nomath]](because all inter-point distances are $\ge 1$)[[/nomath]]. Hence
[
\deg(p)\le k(d).
]
Summing degrees and using the handshake lemma,
[
E(X)=\frac12\sum_{p\in X}\deg(p)\le \frac12,k(d),n.
]
So
[
\boxed{f_d(n)\le \frac{k(d)}{2},n.}
]
In particular (f_d(n)=O_d(n)).

## A simple matching lower bound: (f_d(n)=\Omega_d(n))

Take the (m\times\cdots\times m) integer grid
[
X={0,1,\dots,m-1}^d,\qquad n=m^d.
]
All distances are (\ge 1). The unit-distance pairs are exactly the grid edges: in each of the $d$ coordinate directions there are ((m-1)m^{d-1}) unit edges, so
[
E(X)=d(m-1)m^{d-1}=d,n-d,m^{d-1}=d,n-O(n^{(d-1)/d}).
]
Thus
[
\boxed{f_d(n)\ge d,n-O!\left(n^{(d-1)/d}\right).}
]
Combining with the kissing-number upper bound gives the clean growth rate
[
\boxed{f_d(n)=\Theta_d(n)\quad\text{for every fixed }d.}
]

## Sharper known estimates (best-known general bounds)

Let (\delta_d) be the maximal (infinite) packing density of congruent balls in (\mathbb{R}^d). Bezdek–Khan survey a general upper bound [[nomath]](for $d\ge 3$)[[/nomath]] of the form
[
\boxed{f_d(n)=c(n,d);<;\frac12,k(d),n-\frac12,d,\delta_d^{-(d-1)/d},n^{(d-1)/d}.}
]
So the leading term is (\tfrac12k(d)n), with a *boundary loss* of order (n^{(d-1)/d}). ([arXiv][1])

### Dimension 2 (exact)

Harborth proved the exact formula
[
\boxed{f_2(n)=\left\lfloor 3n-\sqrt{12n-3}\right\rfloor,}
]
so (f_2(n)=3n-\Theta(\sqrt n)). ([arXiv][1])

### Dimension 3 (best known general bounds)

One has
[
\boxed{f_3(n)=c(n,3)<6n-0.926n^{2/3}}
]
and there are matching lattice-based constructions (fcc clusters) giving (6n-O(n^{2/3})), so the correct second-order term is (\Theta(n^{2/3})) (constant not pinned down). ([arXiv][1])

## Dependence on $d$ [[nomath]](if you care about varying $d$)[[/nomath]]

The constant $k(d)$ grows exponentially in $d$. For example, Kabatiansky–Levenshtein give (k(d)\le 2^{0.401d(1+o(1))}) [[nomath]](and also $\delta_d\le 2^{-0.599d(1+o(1))}$)[[/nomath]], which plugged into the bound above yields an exponential-in-$d$ upper bound on the coefficient of $n$. ([arXiv][1])

---

### Bottom line

For each fixed dimension $d$,
[
\boxed{f_d(n)=\Theta(n).}
]
More precisely, it’s bounded above by (\frac12k(d)n) (kissing-number bound) and in fact admits general upper bounds of the form (\frac12k(d)n-\Theta(n^{(d-1)/d})), while simple grid/lattice constructions give (\Omega(n)) unit-distance pairs [[nomath]](indeed $d,n-O(n^{(d-1)/d})$)[[/nomath]].

[1]: https://arxiv.org/pdf/1601.00145 "arXiv:1601.00145v2  [math.MG]  22 Jan 2016"

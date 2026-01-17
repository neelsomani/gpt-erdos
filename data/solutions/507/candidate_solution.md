Let (D={(x,y):x^{2}+y^{2}\le 1}). For a given $n$-point set (P\subset D), write
[
m(P):=\min_{{p,q,r}\subset P}\operatorname{Area}(\triangle pqr).
]
Your (\alpha(n)) is exactly the extremal quantity
[
\alpha(n)=\sup_{|P|=n,P\subset D} m(P),
]
i.e. the **largest possible value of the smallest triangle area** forced among $n$ points. This is the classical **Heilbronn triangle problem** (the choice of disk vs square only affects constants).

### What is known (best current estimates)

Up to absolute constant factors (depending only on the region, here the unit disk), the best known bounds are
[
\boxed{\frac{\log n}{n^{2}}\ \lesssim\ \alpha(n)\ \lesssim\ n^{-7/6+o(1)}}
]
as (n\to\infty).

* **Lower bound (constructions):** Komlós–Pintz–Szemerédi showed there exist configurations of $n$ points for which *every* triangle has area at least on the order of (\frac{\log n}{n^{2}}). A standard summary statement appears, for instance, in Lefmann’s 2003 survey paper, explicitly citing KPS. ([Springer Link][1])
  [[nomath]](Earlier constructions of Erdős already give $\alpha(n)\gtrsim 1/n^{2}$, but KPS adds the $\log n$ factor.)[[/nomath]]

* **Upper bound (guarantee in every configuration):** The current best general upper bound is due to Cohen–Pohoata–Zakharov: any $n$ points in the unit square contain a triangle of area at most (n^{-7/6+o(1)}). ([arXiv][2])
  Since the unit disk is contained in (and contains) a constant-factor comparable square [[nomath]](e.g. disk $\subset$ square of side $2$, and disk $\supset$ square of side $\sqrt2$)[[/nomath]], and scaling multiplies all triangle areas by a constant factor, the same asymptotic upper bound applies to the disk up to constants.

### A simple benchmark bound (easy, but weaker)

Without deep work one can show
[
\alpha(n)\ \lesssim\ \frac{1}{n}
]
by a pigeonhole/strip or triangulation argument [[nomath]](average triangle area in a triangulation of the convex hull is $\asymp 1/n$)[[/nomath]]. This is far from the best known (n^{-7/6+o(1)}), but it’s a useful sanity check.

### Status

The true asymptotic order of (\alpha(n)) is **still unknown**: there is a large gap between the best lower bound (\sim (\log n)/n^{2}) and best upper bound (\sim n^{-7/6}). The (\alpha(n)=\Theta(1/n^{2})) behavior originally conjectured by Heilbronn is false [[nomath]](because of the $\log n$ lower-bound construction)[[/nomath]]. ([Springer Link][1])

So the best current “estimate” is the two-sided bound
[
\boxed{;\alpha(n)=\Omega!\left(\frac{\log n}{n^{2}}\right)\ \text{ and }\ \alpha(n)=O!\left(n^{-7/6+o(1)}\right).;}
]

[1]: https://link.springer.com/article/10.1007/s00493-003-0040-1 "On Heilbronn’s Problem in Higher Dimension | Combinatorica | Springer Nature Link"
[2]: https://arxiv.org/abs/2409.07658 "[2409.07658] Lower bounds for incidences"

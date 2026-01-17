Let
[
\ell(f):=\inf{\text{(Euclidean) length}(\gamma):\ \gamma\subset E,\ \gamma\text{ joins }0\text{ to some point with }|z|=1}.
]

### What you can say unconditionally

* Any path from $0$ to the unit circle must have length (\ge 1), simply because the Euclidean distance from $0$ to ({|z|=1}) is $1$.
* This lower bound is sharp: for (f(z)=z^n) we have (E={ |z^n|\le 1}={|z|\le 1}), and the straight segment ([0,1]\subset E) has length $1$.
  So **the smallest possible value of (\ell(f)) over all such polynomials is $1$**.

### If you meant the “worst case” over all such polynomials of degree $n$

This is the version that appears as an Erdős/Hayman-type research problem: define
[
L_n := \sup{\ell(f): f \text{ monic of degree }n,\ \text{all zeros of }f\text{ in }|z|\le 1}.
]
It is known (Clunie–Netanyahu) that for every such $f$, **some** path in $E$ from $0$ to (|z|=1) exists, so (\ell(f)<\infty) always; but **the growth and sharp determination of (L_n) is open**. Erdős explicitly suggested that the extremal (“worst-case”) length should grow with $n$, but this remains unresolved. ([Erdős Problems][1])

Related work has studied other geometric quantities of polynomial lemniscates [[nomath]](e.g. the *boundary* length of ${|p(z)|=1}$ for monic $p$)[[/nomath]], with recent progress showing near-sharp linear-in-$n$ bounds for that boundary-length extremal problem. ([arXiv][2]) But this does **not** by itself settle the **inner shortest-path** question above.

**Bottom line:**

* If the question is “what is the minimum possible shortest-path length [[nomath]](over all such $f$)[[/nomath]]?” the answer is **(\boxed{1})** (sharp).
* If the question is “how large can that shortest-path length be in the worst case for degree $n$?” then the exact answer (and even the correct growth rate) is **an open problem**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/1120 "https://www.erdosproblems.com/1120"
[2]: https://arxiv.org/html/2512.12455v1 "https://arxiv.org/html/2512.12455v1"

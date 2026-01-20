Write
[
\mu(F)=\inf\\{\mathrm{area}\bigl({z\in\mathbb C:\ |p(z)|<1}\bigr):p(z)=\prod_{j=1}^n (z-z_j),\ z_j\in F,\ n\ge 1\\},
]
(where “area” is planar Lebesgue measure). For compact $F$, the transfinite diameter $d(F)$ agrees with the logarithmic capacity (\mathrm{cap}(F)).

### 1) If $F$ is unbounded, then (\mu(F)=0) [[nomath]](so $d(F)=\infty$ implies $\mu(F)=0$)[[/nomath]]

This is easy and does **not** require potential theory: if $F$ contains points (\pm R) with (R\to\infty), take
[
p_R(z)=(z-R)(z+R)=z^2-R^2.
]
Then ({|p_R|<1}) consists of two tiny components near (\pm R), each of radius (\asymp 1/R), hence total area (\asymp 1/R^2\to 0). So (\mu(F)=0) for any unbounded closed infinite $F$.

The real issue is the **bounded/compact** case.

### 2) What is known when (d(F)<1)

A classical theorem of Erdős–Netanyahu (building on Erdős–Herzog–Piranian) says:

> If $D$ is bounded, closed, **connected** and (d(D)=1-c) with (0<c<1), then for every monic polynomial (f(z)=\prod_{v=1}^n (z-z_v)) with (z_v\in D), the lemniscate ({|f|<1}) contains a disk of radius (p(c)>0) depending only on $c$. 

In particular, for such connected $D$ with (d(D)<1), one gets a **uniform positive lower bound** on area, hence (\mu(D)>0).

They also emphasize connectedness matters for such uniform “disk inside” statements (they explicitly remark their disk theorem fails without it). 

### 3) The “capacity (\ge 1)” direction and your (\mu(F)=0) question

Already in 1973, Erdős–Netanyahu wrote (paraphrasing): if $D$ has transfinite diameter $1$, it is plausible that the area of ({|f|<1}) can be made (<\varepsilon) by taking $n$ large; it was known for $D$ equal to the unit circle or $(-2,2)$, but “the general case is open.” 

There has been recent progress. In a 2025 preprint, Krishnapur–Lundberg–Ramachandran introduce
(\kappa_n(K,1)) = the **minimum** area of ({|p|<1}) among monic degree-$n$ polynomials with zeros in $K$, and prove:

> **Theorem 6 (KLR, 2025).** If $K$ is the closure of a bounded open set with (C^2)-smooth boundary and (\mathrm{cap}(K)=1), then (\inf_n \kappa_n(K,1)=0). ([arXiv][1])

Since your (\mu(K)) is exactly (\inf_n \kappa_n(K,1)), this gives
[
\mu(K)=0
]
for every such “smooth enough” compact $K$ of transfinite diameter $1$. By a simple scaling/renormalization trick [[nomath]](and the fact that ${|p|<t}\subseteq {|p|<1}$ for $t<1$)[[/nomath]], the same conclusion extends to (\mathrm{cap}(K)>1) within the same regularity class. The same paper also recalls that when (\mathrm{cap}(K)<1) one has a positive lower bound [[nomath]](depending on $K$)[[/nomath]], and discusses faster decay for some (\mathrm{cap}(K)>1) cases. ([arXiv][1])

**But:** KLR explicitly note their theorem proves the “(\inf_n=0)” conclusion only for *smooth enough* $K$ (they highlight this limitation). ([arXiv][1])
So, as far as I can find in the literature available, the fully general statement

> “(\mu(F)=0) for **every** compact (or closed) $F$ with (d(F)\ge 1)”

is **not** completely settled without additional regularity hypotheses on $F$.

### 4) Is (\mu(F)) determined by $d(F)$?

In full generality, this is **not known**.

What we can say from the results above:

* In the regime (d(F)\ge 1), we now know (\mu(F)=0) for a large class of sets [[nomath]](e.g. closures of bounded $C^2$ domains)[[/nomath]]. ([arXiv][1])
  If someday one proves (\mu(F)=0) for *all* $F$ with (d(F)\ge 1), then in that regime (\mu) would indeed be determined by the transfinite diameter [[nomath]](it would just be identically $0$)[[/nomath]].

* In the regime (d(F)<1), one has general positive lower bounds, and for **connected** sets those lower bounds can be made to depend only on $d(F)$ (Erdős–Netanyahu). 
  But outside such hypotheses, the best available lower bounds are typically stated as depending on finer features of $F$ (and uniform “disk inside” statements fail without connectedness). 

So at present:

* **Your “in particular” question:** proven **yes** for many “regular” compact sets with (d(F)\ge 1), but the completely general case (no regularity assumptions) appears still open. ([arXiv][1])
* **The stronger “(\mu) is determined by transfinite diameter” question:** also open in general; current results give strong evidence of a capacity threshold at $1$ in wide classes, but do not yield a complete “(\mu=\Phi(d(F)))” classification. ([arXiv][1])

[1]: https://arxiv.org/pdf/2503.18270 "https://arxiv.org/pdf/2503.18270"

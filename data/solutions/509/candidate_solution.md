Interpreting “circles” in the usual way in this context [[nomath]](closed discs in $\mathbb C$)[[/nomath]], the statement with **total radius (\le 2)** is **not known in general**: it is a classical open problem of Erdős [[nomath]](often presented as an “improve Cartan’s constant to $2$” question)[[/nomath]]. ([Erdős Problems][1])

What is known is:

* **Cartan (1928):** one can always cover ({,|f(z)|\le 1,}) by discs whose radii sum to (\le 2e). 
* **Pommerenke:** improved the constant (2e) to about **(2.59)** [[nomath]](still $>2$)[[/nomath]]. ([Erdős Problems][1])
* **Connected case:** if ({,|f(z)|\le 1,}) is **connected**, then the desired bound **(\le 2)** is achievable (Pommerenke). ([Erdős Problems][1])

So the best current status is: **open in general; true in special cases; true with a larger constant.** ([Erdős Problems][1])

---

## Why (2e) always works [[nomath]](Cartan’s lemma $\Rightarrow$ a $2e$-cover)[[/nomath]]

Let (\deg f=n\ge 1) and write (counting multiplicity)
[
f(z)=\prod_{j=1}^n (z-z_j),
]
so
[
E:={z:|f(z)|\le 1}=\\{z:\prod_{j=1}^n |z-z_j|\le 1\\}.
]

A geometric lemma of H. Cartan (one standard formulation) says:

> **Cartan’s covering lemma (one form).**
> Given points (z_1,\dots,z_n\in\mathbb C) and (H>0), there exist closed discs (\Delta_1,\dots,\Delta_m) with (m\le n) such that
> [
> \sum_{k=1}^m \operatorname{rad}(\Delta_k)\le 2H,
> ]
> and for every (z\notin\bigcup_{k=1}^m\Delta_k),
> [
> \prod_{j=1}^n |z-z_j|>(\frac{H}{e})^n.
> ]
>

Now choose $H=e$. Then outside the discs,
[
\prod_{j=1}^n |z-z_j|>\left(\frac{e}{e}\right)^n=1,
]
so (|f(z)|>1). Equivalently,
[
{,|f(z)|\le 1,}\subset \bigcup_{k=1}^m \Delta_k,
\qquad \sum \operatorname{rad}(\Delta_k)\le 2e.
]

That proves the universal $2e$ bound. 

---

## What remains open

Your exact question asks whether the same conclusion holds with **$2$** in place of $2e$:

[
\text{Is }E={|f|\le 1}\text{ always coverable by discs with }\sum r_i\le 2\ ?
]

This is listed as an **open** Erdős problem; the best published constants cited there are $2e$ (Cartan) and $2.59$ (Pommerenke), and $2$ is known when $E$ is connected. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/509 "

    Erdős Problem #509 - Discussion thread

"

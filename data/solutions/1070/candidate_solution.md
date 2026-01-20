Given a set $P$ of $n$ points in (\mathbb R^2), form the **unit–distance graph**
[
G(P):\quad V(G)=P,\qquad {x,y}\in E(G)\iff |x-y|=1.
]
Then your $f(n)$ is exactly
[
f(n)=\min_{|P|=n}\ \alpha(G(P)),
]
the smallest possible independence number among all unit–distance graphs on $n$ vertices.

## What is known asymptotically

### Upper bound: (f(n)\le \frac{2}{7}n)

The **Moser spindle** is a unit–distance graph on $7$ vertices with independence number $2$. Hence for $n=7k$, taking $k$ disjoint copies (placed far apart so there are no unit edges between copies) gives an $n$-point set whose largest unit-distance-free subset has size (2k=\frac{2}{7}n). Therefore
[
f(n)\le \frac{2}{7}n\quad\text{(up to rounding)}.
]
This example is explicitly cited by Erdős as giving (f(n)\le 2n/7). ([Rényi Institute][1])

### Lower bounds: linear in $n$

1. **Székely’s bound:** Erdős notes that Székely proved (f(n) > n/5) (and “somewhat sharper”). ([Rényi Institute][1])

2. **A better constant via “dense 1‑avoiding sets”:**
   Let (A\subset\mathbb R^2) be a measurable set with **no pair of points at distance 1** (“1‑avoiding”), and let (\delta(A)) denote its upper density. A standard averaging/translation argument gives:

> For any finite set $P$ of $n$ points and any such $A$, there exists a translate $t$ so that (|P\cap (A+t)|\ge \delta(A),n).
> Since $A+t$ has no unit-distance pairs, (P\cap(A+t)) is an independent set in $G(P)$.

So
[
f(n)\ \ge\ m_1(\mathbb R^2),n,
]
where (m_1(\mathbb R^2)) is the supremum of upper densities of measurable 1‑avoiding sets.

The best-known **explicit construction** (Croft’s “tortoise”) gives
[
m_1(\mathbb R^2)>0.22936,
]
and the 2023 paper by Ambrus–Csiszárik–Matolcsi–Varga–Zsámboki states that this remains the best known construction to date. ([math.bme.hu][2])
Thus,
[
f(n)\ \ge\ 0.22936,n.
]

Putting the best published constants together (as of the sources above):
[
0.22936n\ \le\ f(n)\ \le\ \frac{2}{7}n\approx 0.2857n.
]
(Up to integer rounding.)

So, in particular, **(f(n)=\Theta(n))**, but the optimal constant is unknown.

## Is (f(n)\ge n/4) true?

As stated (with **no extra assumptions** on the point set), this remains **open** in the classical Erdős formulation: Erdős explicitly asks “is it true that (f(n)>n/4)?” after recording the bounds above. ([Rényi Institute][1])

One important nuance: the **measurable-density method** cannot prove $n/4$, because the same 2023 work proves an **upper bound** on the best possible density of measurable 1‑avoiding sets:
[
m_1(\mathbb R^2)\le 0.2470 < \tfrac14,
]
so any argument that only works by translating a fixed 1‑avoiding measurable set is capped below $n/4$. ([math.bme.hu][2])

## A related variant where $n/4$ *is* true

If you additionally assume the point configuration has **minimum pairwise distance (\ge 1)** (so the unit-distance graph is a “minimum-distance graph” in that literature), then there are results giving an independent set (> n/4). But that is a **different** problem than the one you stated. ([Erdős Problems][3])

---

If you want, I can also sketch the translation/averaging proof of (f(n)\ge m_1 n) cleanly in a few lines, and/or explain why the Moser spindle gives exactly the $2/7$ obstruction.

[1]: https://www.renyi.hu/~p_erdos/1987-27.pdf "https://www.renyi.hu/~p_erdos/1987-27.pdf"
[2]: https://math.bme.hu/~matolcsi/57_unit_avoding_solution.pdf "https://math.bme.hu/~matolcsi/57_unit_avoding_solution.pdf"
[3]: https://www.erdosproblems.com/forum/thread/1070 "https://www.erdosproblems.com/forum/thread/1070"

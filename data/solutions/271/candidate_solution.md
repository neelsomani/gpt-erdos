What you’ve defined is exactly the **Stanley sequence** generated from the 3‑free seed set $\\{0,n\\}$.  In the usual notation it’s (S(0,n)={a_k}_{k\ge0}), built by the greedy rule “take the smallest integer (>a_k) that keeps the set 3‑term‑AP‑free.” ([MIT Mathematics][1])

## 1) Can (a_k) be written explicitly?

### Fully explicit (in terms of ternary digits) for the “regular” $n$

Odlyzko–Stanley found that when
[
n=3^m\quad\text{or}\quad n=2\cdot 3^m\qquad(m\ge 0),
]
membership in the set has a clean description in terms of the **ternary expansion** of an integer (t=\sum_{i\ge0} t_i 3^i). ([MIT Mathematics][1])

#### Case A: (n=3^m)

An integer (t\ge0) lies in (S(0,3^m)) iff its ternary digits satisfy: ([MIT Mathematics][1])

* (t_i\in{0,1}) for every (i\neq m);
* if (t_m=0), then all lower digits vanish: (t_{m-1}=t_{m-2}=\cdots=t_0=0);
* if (t_m=2), then the lower digits are **not** all zero: (\sum_{i=0}^{m-1} t_i>0).

Example (m=1) (so (n=3)): this produces
[
0,3,4,7,9,12,13,16,27,30,31,34,\dots
]
[[nomath]](see OEIS entry for $S(0,3)$)[[/nomath]]. ([oeis.org][2])

#### Case B: (n=2\cdot 3^m)

Similarly, (t\in S(0,2\cdot 3^m)) iff [[nomath]](again writing $t=\sum t_i 3^i$)[[/nomath]] the digits satisfy: ([MIT Mathematics][1])

* (t_i\in{0,1}) for every (i\notin{m,m+1});
* (t_m\in{0,2});
* if (t_{m+1}=2), then (t_m=0) and (\sum_{i=0}^{m-1} t_i>0).

These digit rules give an **explicit membership test**, hence an explicit description of the set and (in principle) an explicit way to compute the ordered terms (a_k). ([MIT Mathematics][1])

### The simplest explicit closed form: (n=1)

When (n=1), the description collapses to a very clean formula:

* (t\in S(0,1)) iff the ternary expansion of (t) contains **no digit 2**.
* Equivalently, to get (a_k): write (k) in binary and interpret the same digit string as a ternary number. ([MIT Mathematics][1])

So if (k=\sum b_i 2^i) with bits (b_i\in{0,1}), then
[
a_k=\sum b_i 3^i.
]
This is the classic “binary–ternary” Stanley sequence. ([MIT Mathematics][1])

### For general $n$: no known explicit description

For $n$ not of the form (3^m) or (2\cdot 3^m), Odlyzko–Stanley observed that the greedy sequences appear **erratic** and “have no simple description” (their term), and they conjectured that the only “regular” cases among $S(0,n)$ are exactly (n=3^m) and (n=2\cdot 3^m). ([MIT Mathematics][1])

So: **explicit digit formulas are known only in those regular cases**; beyond that, there is not currently a general closed form.

## 2) How fast do they grow?

It’s useful to separate “regular” vs “irregular” behavior.

### Regular (n=3^m) or (2\cdot 3^m): power-law growth (k^{\log_2 3})

Let
[
\alpha=\frac{\log 3}{\log 2}=\log_2 3\approx 1.585.
]
Odlyzko–Stanley show that for these regular values the growth satisfies
[
a_k = \Theta!\left(k^{\alpha}\right),
]
and more precisely they give bounds on (\liminf) and (\limsup) of (a_k/k^\alpha) [[nomath]](between $1/2$ and $1$ in their normalization)[[/nomath]]. ([MIT Mathematics][1])

Equivalently, the **counting function**
[
A(x):=|\\{a_k\le x\\}|
]
grows like (x^{\log_3 2}\approx x^{0.631}) [[nomath]](this is just inversion of the $k^{\log_2 3}$ law)[[/nomath]]. ([Wikipedia][3])

### Irregular $n$: conjecturally much faster, but still open

Odlyzko–Stanley gave a probabilistic heuristic suggesting that “irregular” cases should behave like
[
a_k \approx c\frac{k^2}{\log k}
]
for some constant $c$ (this is what later papers call “Type 2” growth). ([MIT Mathematics][1])

However, and this is important:

* **No specific $n$** has been proved to have this precise (\Theta(k^2/\log k)) asymptotic.
* And there is **new (Dec 2025) numerical evidence** that the flagship irregular case (n=4) may *not* actually have (\Theta(k^2/\log k)) growth as a two-sided bound; the preprint suggests the upper bound may still be (O(k^2/\log k)), but the lower growth might be closer to (\Omega(k^{2-\delta})) for some (\delta>0). ([arXiv][4])

So the honest current picture is: **irregular growth is not settled**, even heuristically, though the (k^2/\log k) law is historically the main guess.

### What *is* proved for every $n$: a universal quadratic upper bound

A rigorous theorem of Moy (2010/2011) gives a general lower bound on the counting function of *any* Stanley sequence $S(A)$:
[
S(A,x)\ \ge\ (\sqrt2-\varepsilon)\sqrt{x}\quad\text{for all large }x,
]
which implies for the $k$-th term (a_k) (invert this relation) that
[
a_k \le \left(\frac{k}{\sqrt2-\varepsilon}\right)^2
]
for all sufficiently large $k$. In short: **every Stanley sequence satisfies (a_k=O(k^2))**. ([arXiv][5])

## 3) Takeaway

* Your $A(n)$ is the Stanley sequence $S(0,n)$. ([MIT Mathematics][1])
* **Explicit digit descriptions** exist for the “regular” parameters (n=3^m) and (n=2\cdot 3^m), and in the special case (n=1) there’s an especially clean “binary → ternary” formula. ([MIT Mathematics][1])
* For those regular $n$, (a_k) grows like (k^{\log_2 3}\approx k^{1.585}). ([MIT Mathematics][1])
* For other $n$, no closed form is known; growth is conjecturally “Type 2,” historically (\Theta(k^2/\log k)), but this is unproved and (as of late 2025) there is credible numerical evidence it may be more subtle at least for (n=4). ([MIT Mathematics][1])
* Universally, (a_k=O(k^2)) is proved. ([arXiv][5])

If you tell me a specific $n$ you care about [[nomath]](say $n=4,5,7,\dots$)[[/nomath]], I can also generate the first several hundred/thousand terms and compare empirically to the candidate growth laws.

[1]: https://math.mit.edu/~rstan/papers/od.pdf "od.dvi"
[2]: https://oeis.org/A185256 "A185256 - OEIS"
[3]: https://en.wikipedia.org/wiki/Stanley_sequence?utm_source=chatgpt.com "Stanley sequence"
[4]: https://arxiv.org/abs/2512.11983 "https://arxiv.org/abs/2512.11983"
[5]: https://arxiv.org/abs/1101.0022 "https://arxiv.org/abs/1101.0022"

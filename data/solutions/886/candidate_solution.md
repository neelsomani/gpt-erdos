This is a known open problem in general.

Let
$
D_n(X,Y):=|\\{d\mid n:\ X<d\le X+Y\\}|.
$
Your question is exactly the assertion that for each fixed (\epsilon>0),
$
D_n(n^{1/2},n^{1/2-\epsilon})=O_\epsilon(1)\quad\text{as }n\to\infty.
$
It appears explicitly as **Conjecture 1** in a 2025 preprint of Letendre (in essentially the same notation). ([arXiv][1])

## What is known

### 1) If (\epsilon> \tfrac14), then **yes**

Write (\epsilon=\tfrac14+\delta) with (\delta>0). Then
[
n^{1/2-\epsilon}=n^{1/2-(1/4+\delta)}=n^{1/4-\delta}.
]
Letendre proves the following uniform bound: for (0<\theta<1) and (0<\varepsilon<\theta^2),
[
D_n\bigl(n^\theta,\ n^{\theta^2-\varepsilon}\bigr)\ \ll\ \frac{\theta(1-\theta)}{\varepsilon}+\frac1{\theta(1-\theta)}.
]
([arXiv][1])

Plugging in (\theta=\tfrac12) and (\varepsilon=\delta) gives
[
D_n\bigl(n^{1/2},n^{1/4-\delta}\bigr)\ \ll\ \frac{1}{\delta},
]
so in your notation:
[
D_n\bigl(n^{1/2},n^{1/2-\epsilon}\bigr)=O\\(\frac{1}{\epsilon-1/4}\\)\qquad(\epsilon>1/4).
]
In particular, it is (O_\epsilon(1)) for every (\epsilon>1/4).

[[nomath]](As a side note: if $\epsilon\ge 1/2$, then the interval length $n^{1/2-\epsilon}\le 1$, so the count is trivially $\le 1$ for large $n$.)[[/nomath]]

### 2) If (\epsilon\le \tfrac14), then it is **open** in general

Even at the “borderline” (\epsilon=\tfrac14) [[nomath]](interval length $n^{1/4}$)[[/nomath]], Erdős–Rosenfeld exhibited infinitely many $n$ with **four** divisors in $(n^{1/2},n^{1/2}+n^{1/4})$, and asked whether 4 is best possible; the general boundedness question is still regarded as open. ([Erdős Problems][2])

So:

* **Proved:** the (O_\epsilon(1)) bound holds for all $\epsilon>1/4$. ([arXiv][1])
* **Open:** whether such a bound holds for $\epsilon\in(0,1/4]$, including (\epsilon=1/4). ([arXiv][1])

If you want, I can also summarize the best currently-known *non-uniform* upper bounds in the open range [[nomath]](they typically depend on $\tau(n)$, the prime-exponent structure of $n$, etc.)[[/nomath]], but the clean “bounded by a constant depending only on (\epsilon)” statement is exactly what remains unresolved for (\epsilon\le 1/4).

[1]: https://arxiv.org/pdf/2503.12146 "https://arxiv.org/pdf/2503.12146"
[2]: https://www.erdosproblems.com/887 "https://www.erdosproblems.com/887"

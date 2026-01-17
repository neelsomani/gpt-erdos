Let
[
P_{(a_1,\dots,a_n)}(z):=\prod_{j=1}^n(1-z^{a_j}),\qquad |z|=1,
]
and
[
M(a_1,\dots,a_n):=\max_{|z|=1}|P_{(a_1,\dots,a_n)}(z)|.
]
Your “maximal” $f(n)$ is exactly
[
f(n)=\inf_{1\le a_1\le\cdots\le a_n} M(a_1,\dots,a_n),
]
the classical Erdős–Szekeres “pure power product” extremal function. 

## What is known asymptotically

### Subexponential growth

Erdős–Szekeres proved
[
\lim_{n\to\infty} f(n)^{1/n}=1,
]
so (f(n)=\exp(o(n))). 

### Best general lower bound (as of 2025)

The classical bound was (f(n)\ge \sqrt{2n}) (with later fixes/repairs of the original gap). 
A 2025 preprint of Quanyu Tang gives the first general improvement since 1959:
[
f(n)\ \ge\ 2\sqrt{n}\qquad \text{for all }n\in\mathbb N.
]
([arXiv][1])

So at minimum,
[
\log f(n)\ \ge\ \tfrac12\log n + O(1).
]

### Best general upper bound (construction of “small” products)

The strongest general upper bound quoted in modern surveys is still the 1996 Belov–Konyagin estimate (via nonnegative trigonometric polynomials), which yields
[
f(n)=\exp\bigl(O((\log n)^4)\bigr),
]
i.e.
[
\log f(n)\ \ll\ (\log n)^4.
]
This is presented as the best currently known general upper bound, with no improvement reported in later surveys. 

Putting the two together, the current general state is
[
2\sqrt{n}\ \le\ f(n)\ \le\ \exp\bigl(C(\log n)^4\bigr)
]
for some absolute constant (C>0). ([arXiv][1])

## Answer to your “(\log f(n)\gg n^c)?” question

No. The upper bound (\log f(n)\ll (\log n)^4) rules it out: for every fixed (c>0),
[
(\log n)^4=o(n^c)\quad(n\to\infty),
]
so (\log f(n)) cannot dominate (n^c). 

## What remains open

There is still a huge gap between the polynomial lower bound (f(n)\gtrsim \sqrt n) and the polylogarithmic-exponent upper bound (f(n)\le \exp(O((\log n)^4))). Erdős conjectured that $f(n)$ should grow faster than any power of $n$ [[nomath]](i.e. $f(n)=n^{\omega(1)}$)[[/nomath]], but this is far from proved: even with Tang’s improvement, the best general lower bound is still only (\asymp \sqrt n). 

[1]: https://arxiv.org/pdf/2509.14182 "An improved lower bound for Erd\H{o}s--Szekeres products"

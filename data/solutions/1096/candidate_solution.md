Assuming [[nomath]](as your notation $0=x_1<x_2<\cdots$ forces)[[/nomath]] that the exponents are **nonnegative integers**—i.e. you are looking at
[
X(q):=\\{\sum_{i\in S} q^i:\ S\subset{0,1,2,\dots}\ \text{finite}\\},
]
and ((x_k)) is the increasing enumeration of $X(q)$,

then **yes**: for $q$ sufficiently close to $1$ one has (x_{k+1}-x_k\to 0).

In fact, Akiyama–Komornik study exactly this “spectrum” (X_1(q)=X(q)) and define
[
L_1(q):=\limsup_{k\to\infty}\bigl(x_{k+1}-x_k\bigr).
]
They prove [[nomath]](Theorem 1.4$i$)[[/nomath]] that if (1<q<2) is **not** a Pisot number and
[
1<q\le 2^{1/3}\approx 1.2599,
]
then
[
L_1(q)=0.
]
That is, (\limsup_{k\to\infty}(x_{k+1}-x_k)=0). ([arXiv][1])

Since each gap (x_{k+1}-x_k\ge 0), having (\limsup=0) forces the actual limit to be $0$, i.e.
[
x_{k+1}-x_k \longrightarrow 0.
]

Moreover, the **smallest Pisot number** is (P_1\approx 1.32). ([arXiv][1])
Because (2^{1/3}\approx 1.2599 < P_1), *every* $q\in(1,2^{1/3}]$ is automatically non‑Pisot, so the hypothesis “non‑Pisot” is vacuous in that range.

So you can take an explicit “sufficiently small”
[
\varepsilon_0 = 2^{1/3}-1 \approx 0.259921\ldots
]
and conclude:

> For every $q\in(1,1+\varepsilon_0]$, the consecutive gaps (x_{k+1}-x_k) tend to $0$.

If you’re wondering how far beyond (2^{1/3}) this should remain true: the same paper records that the full characterization of when (L_1(q)=0) holds on larger intervals is still subtle; e.g. they explicitly list as an open question whether (L_1(q)=0) for *all* non‑Pisot $q$ below the golden ratio. ([arXiv][1])

[1]: https://arxiv.org/pdf/1103.4508 "https://arxiv.org/pdf/1103.4508"

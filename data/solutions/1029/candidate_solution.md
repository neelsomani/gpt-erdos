Let (R(k)=r(k,k)) be the usual *diagonal* Ramsey number [[nomath]](the least $n$ such that every red/blue colouring of $E(K_n)$ contains a monochromatic $K_k$)[[/nomath]].

### What we know

The best general **lower bound** (Spencer, via the Lovász local lemma) is
[
R(k)\ge (1-o(1))\frac{\sqrt2}{e}k2^{k/2}\qquad (k\to\infty),
]
so
[
\frac{R(k)}{k2^{k/2}} \ge (1-o(1))\frac{\sqrt2}{e},
]
i.e. the ratio is bounded below by a positive constant. 

On the **upper bound** side, the classical Erdős–Szekeres (4^k) bound has been improved: Conlon proved
[
R(k)\le k^{-c\log k/\log\log k}4^k
]
for some absolute (c>0),  and more recently Campos–Griffiths–Morris–Sahasrabudhe proved an *exponential* improvement
[
R(k)\le (4-\varepsilon)^k
]
for some (\varepsilon>0). ([arXiv][1])

### Status of your limit claim

Your statement
[
\frac{R(k)}{k2^{k/2}}\to\infty
]
is **not currently known**.

In fact, it is open even to beat Spencer’s lower bound by any *fixed constant factor*: Conlon–Fox–Sudakov explicitly pose the problem of whether there exists (\varepsilon>0) such that, for all large $k$,
[
R(k)\ge (1+\varepsilon)\frac{\sqrt2}{e}k2^{k/2}.
]


Since (\frac{R(k)}{k2^{k/2}}\to\infty) would imply such a constant-factor improvement (and much more), it is far beyond what is proved at present.

So, as of the current state of the art: **the limit claim is an open problem**.

[1]: https://arxiv.org/abs/2303.09521?utm_source=chatgpt.com "An exponential improvement for diagonal Ramsey"

Let $f(N)$ denote the maximum possible $r$.

This is a classical Erdős problem (“non‑intersecting arithmetic progressions”), and the exact order of growth of $f(N)$ is still **open**. What is known is that $f(N)$ is **sublinear** but only by a *very slowly growing* factor.

## What is known (best current bounds)

Erdős and Stein conjectured that (f(N)=o(N)); this was proved by Erdős–Szemerédi. In particular, they showed that for every (\varepsilon>0),
[
\frac{N}{\exp\big((\log N)^{1/2+\varepsilon}\big)} \ll_{\varepsilon} f(N)
<
\frac{N}{(\log N)^c}
]
for some absolute constant (c>0). ([Erdős Problems][1])

Much sharper bounds are now known. Write
[
L(N) := \exp\Big(\sqrt{\log N\log\log N}\Big).
]
De la Bretèche–Ford–Vandehey proved (as (N\to\infty)) the two‑sided estimate
[
\frac{N}{L(N)^{1+o(1)}} \le f(N) \le \frac{N}{L(N)^{\sqrt3/2+o(1)}}.
]
Equivalently,
[
N\exp\big(-(1+o(1))\sqrt{\log N,\log\log N}\big)
\le
f(N)
\le
N\exp\big(-(\tfrac{\sqrt3}{2}+o(1))\sqrt{\log N\log\log N}\big).
]
([Kevin Ford's Home Page][2])

They further **conjecture** that the lower bound is the right order of magnitude, i.e.
[
f(N)=\frac{N}{L(N)^{1+o(1)}}.
]
([Kevin Ford's Home Page][2])

## Interpretation

So (f(N)) is “almost linear,” but divided by a factor
[
\exp\big(\Theta(\sqrt{\log N\log\log N})\big),
]
which grows faster than any power of (\log N) but slower than (N^\delta) for any fixed (\delta>0). In short:

[
f(N)=N\cdot \exp!\big(-\Theta(\sqrt{\log N\log\log N})\big),
]
with the constant in the (\Theta(\cdot)) currently known to lie between (\sqrt3/2\approx 0.866) and $1$. ([Kevin Ford's Home Page][2])

[1]: https://www.erdosproblems.com/forum/thread/202 "

    Erdős Problem #202 - Discussion thread

"
[2]: https://www.ford126.web.illinois.edu/wwwpapers/NAP.pdf "NAP8.dvi"

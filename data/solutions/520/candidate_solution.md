This is **open** as of January 2026. In fact, the question in exactly this form is recorded as **Erdős Problem #520** (from Erdős 1961) and is listed as open in current compilations. ([Erdős Problems][1])

If the values $f(n)$ behaved like *independent* mean-zero variables with the “right” variance, then one would expect a Khintchine–Kolmogorov law of the iterated logarithm (LIL)–type constant. Here
[
\mathbb E,f(n)=0 \ (n>1),\qquad \mathbb E,f(n)^2=\mathbf 1_{\text{(n) squarefree}},
]
so
[
\mathbb E\Big(\sum_{m\le N} f(m)\Big)^2=|\\{m\le N:\ m\ \text{squarefree}\\}|\sim \frac{6}{\pi^2}N.
]
If an LIL for *independent* variables with this variance profile applied, it would suggest a normalization like
(\sqrt{(12/\pi^2)N\log\log N}), i.e. your ratio would have a deterministic constant $c$ [[nomath]](namely $\sqrt{12}/\pi$)[[/nomath]].

However, the core difficulty is that $\\{f(n)\\}$ are **not independent** [[nomath]](even though they are pairwise orthogonal in $L^2$)[[/nomath]], and the best results to date are still far from pinning down the “correct” iterated-logarithm scale.

### What is known (bounds)

Write (M_f(x):=\sum_{n\le x} f(n)).

**Almost sure upper bounds.**

* Lau–Tenenbaum–Wu proved that for every (\varepsilon>0),
  [
  M_f(x)\ll \sqrt{x},(\log\log x)^{2+\varepsilon}\qquad\text{a.s.}
  ]

* Caich (2024) improved this to
  [
  M_f(x)\ll \sqrt{x},(\log\log x)^{3/4+\varepsilon}\qquad\text{a.s.}
  ]


These bounds are *compatible* with (\sqrt{x\log\log x}) fluctuations, but they do not imply such a scale, nor do they control your normalized limsup tightly enough to yield a constant.

**Almost sure lower bounds (“large fluctuations occur”).**
Harper (2023) proved that for any function (V(x)\to\infty), almost surely there are arbitrarily large $x$ with
[
|M_f(x)| \ge \frac{\sqrt{x}(\log\log x)^{1/4}}{V(x)}.
]


This is the first lower bound that forces (|M_f(x)|) to exceed (\sqrt{x}) by a power of (\log\log x), and Harper notes it is **plausible the exponent $1/4$ is sharp**. 

### Why many people *don’t* expect a positive LIL constant at the (\sqrt{N\log\log N}) scale

A key piece of evidence is that the “typical” size at a fixed point $x$ seems **smaller than (\sqrt{x})**: Harper notes (citing low-moment results) that
[
\mathbb E\Big|\sum_{n\le x} f(n)\Big|\asymp \frac{\sqrt{x}}{(\log\log x)^{1/4}}.
]


Heuristically, if the typical size is (\sqrt{x}/(\log\log x)^{1/4}), then a random-walk-style “maximal over many $x$” effect might only multiply by (\sqrt{\log\log x}), leading to a conjectural maximal order around
[
\sqrt{x},(\log\log x)^{1/4+o(1)},
]
which is exactly the scale Harper conjectures. ([Erdős Problems][1])
If that conjecture is correct, then your normalization (\sqrt{N\log\log N}=\sqrt{N}(\log\log N)^{1/2}) is **too large**, and the limsup in your question would be $0$, not a positive constant.

### Bottom line

No constant (c>0) is currently known, and the existence of such a positive constant is an **open problem**. Moreover, the best current heuristic/conjectural picture (based on work of Harper and others) suggests the true maximal scale may be closer to (\sqrt{N}(\log\log N)^{1/4+o(1)}), which would make your limsup equal to $0$ rather than (c>0). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/520 "
  
    Erdős Problem #520
  
"

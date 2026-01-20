Not in general (at least, not with current techniques).

* **What is known for arbitrary irreducible $f$:** one has the *right order of magnitude*
  [
  \sum_{n\le X}\tau(f(n)) \asymp_f X\log X,
  ]
  with a lower bound due to **van der Corput** and an upper bound due to **Erdős**. ([Erdős Problems][1])

* **Where the full asymptotic is known:** the asymptotic
  [
  \sum_{n\le X}\tau(f(n))\sim c(f),X\log X
  ]
  is proved when $f$ has **degree $1$** or is an **irreducible quadratic** [[nomath]](degree $2$)[[/nomath]], in particular by **Hooley** for irreducible quadratics; the constant $c(f)$ is explicit but can be quite intricate (and is worked out in various cases by McKee and others). ([Erdős Problems][1])
  For example,
  [
  \sum_{n\le x}\tau(n^2+1)=\frac{3}{\pi}x\log x+O(x).
  ]
  ([Erdős Problems][1])

* **What happens for (\deg f\ge 3):** even for a fixed irreducible polynomial $f$ of degree (>2), the existence of such a constant $c(f)$ (i.e. a genuine asymptotic with a limiting ratio) is **still unknown** and is considered difficult. ([arXiv][2])

### What one expects $c(f)$ to be (heuristics)

A standard heuristic writes
[
\sum_{n\le X}\tau(f(n))=\sum_{n\le X}\sum_{d\mid f(n)}1
=\sum_{d\ge1}|\\{n\le X:\ f(n)\equiv0\pmod d\\}|,
]
and models
[
|\\{n\le X:\ f(n)\equiv0\pmod d\\}|\approx \frac{\rho_f(d)}{d},X,
\quad
\rho_f(d):=|\\{a\bmod d:\ f(a)\equiv0\pmod d\\}|.
]
This suggests a main term coming from (\sum_{d\le X^{\deg f}}\rho_f(d)/d), hence an (X\log X) asymptotic with a “singular series” constant built from the local root densities (\rho_f(p^k)). (Such Euler-product constants do appear in proven divisor-average results once one averages over *many variables*; the one-variable case is exactly the hard one.) ([arXiv][3])

So the best current answer is:

* **Yes** for (\deg f=1) and for **irreducible quadratics**.
* **Open** for general irreducible $f$ of degree (\ge 3), although (\asymp_f X\log X) is known. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/975 "https://www.erdosproblems.com/latex/975"
[2]: https://arxiv.org/pdf/1806.01404 "https://arxiv.org/pdf/1806.01404"
[3]: https://www.arxiv.org/pdf/2409.18116 "https://www.arxiv.org/pdf/2409.18116"

This is **not known** in general: the existence of
[
\lim_{n\to\infty}\frac{f(n)}{n/(\log n)^2}
]
is an **open Erdős problem** (often listed as Erdős Problem #627). ([Erdős Problems][1])

A few relevant facts [[nomath]](using $\log$ base $2$, as is standard in much of the literature; changing the log base only rescales the expression by a fixed constant, so **existence/nonexistence of the limit is base-independent**)[[/nomath]]:

* Erdős (1967) proved the correct **order of growth**
  [
  f(n)=\Theta\left(\frac{n}{(\log n)^2}\right),
  ]
  and in particular established [[nomath]](with $\log=\log_2$)[[/nomath]]
  [
  \left(\frac14+o(1)\right)\frac{n}{(\log n)^2}\ \le\ f(n)\ \le\ \left(4+o(1)\right)\frac{n}{(\log n)^2}.
  ]
  ([arXiv][2])

* Very recently, Araujo–Filipe–Miyazaki (Dec 2025) improved the **upper constant**:
  [
  f(n)\le \left(3.71943+o(1)\right)\frac{n}{(\log n)^2},
  ]
  and even slightly better under an additional conjecture (their Conjecture 1.1). ([arXiv][2])

* The same paper makes explicit why the limit is hard: if you define
  [
  g(n):=\frac{(\log n)^2}{n}f(n),
  ]
  then they relate (\liminf g(n)) and (\limsup g(n)) to **Ramsey-number asymptotics** [[nomath]](via quantities $L$ and $M$ defined from $R(s,t)$)[[/nomath]]. In particular, they show (\limsup g(n)=M^2) and (\liminf g(n)\ge L^2). ([arXiv][2])

* Moreover, **conditionally** (assuming their Conjecture 1.1), if the famous diagonal Ramsey limit (\lim_{k\to\infty}\frac{\log R(k,k)}{k}) exists and equals $L$, then
  [
  f(n)=\left(L^2+o(1)\right)\frac{n}{(\log n)^2},
  ]
  which would in particular imply that your limit **does** exist [[nomath]](and equals $L^2$, with logs base $2$)[[/nomath]]. ([arXiv][2])

So: **unconditionally, the limit is still open**; we only know it is trapped between explicit constants [[nomath]](currently $\tfrac14$ and $3.71943$ for base-2 logs, up to lower-order terms)[[/nomath]]. ([arXiv][2])

[1]: https://www.erdosproblems.com/627?utm_source=chatgpt.com "Erdős Problem #627"
[2]: https://arxiv.org/pdf/2512.16062 "On the maximum ratio between chromatic number and clique number"

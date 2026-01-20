This is **not known** in general.

It is an Erdős problem (often listed as **Erdős Problem #933**) asking exactly whether
[
\limsup_{n\to\infty}\frac{2^k3^l}{n\log n}=\infty
]
when $n(n+1)=2^k3^lm$ with ((m,6)=1); and it is currently recorded as **open**. ([Erdős Problems][1])

### What is known

* **There are infinitely many $n$** for which the ratio is already (>1) (so the limsup is at least a positive constant). In fact, a clean explicit construction is to take
  [
  n = 2^{3^r}.
  ]
  Then (v_2(n)=3^r), so (2^k=2^{3^r}=n). Also (n+1=2^{3^r}+1) has a large 3-adic valuation: by LTE [[nomath]](since $3\mid 2+1$ and $3^r$ is odd)[[/nomath]],
  [
  v_3(2^{3^r}+1)=v_3(2+1)+v_3(3^r)=1+r,
  ]
  so (3^l \ge 3^{r+1}). Therefore
  [
  \frac{2^k3^l}{n\log n} \ge \frac{n\cdot 3^{r+1}}{n\log(2^{3^r})}
  =\frac{3^{r+1}}{3^r\log 2}
  =\frac{3}{\log 2},
  ]
  a fixed constant (\approx 4.33), for all $r$. This is the “simple proof” noted in the literature around the problem. ([Erdős Problems][1])

  In particular,
  [
  \limsup_{n\to\infty}\frac{2^k3^l}{n\log n}\ge \frac{3}{\log 2} > 1.
  ]

* **An upper-bound type result (too weak to settle the limsup)**: Mahler proved that in this setup one has
  [
  2^k3^l < n^{1+o(1)}.
  ]
  This says the ({2,3})-part of $n(n+1)$ is at most “slightly superlinear” in $n$, but it still leaves open whether the ratio divided by (n\log n) can become arbitrarily large. ([Erdős Problems][1])

### Bottom line

* We **can** show the ratio is (>1) infinitely often [[nomath]](indeed $\ge 3/\log 2$ along an explicit sequence)[[/nomath]].
* But whether the ratio’s **limsup is infinite** is, as far as currently recorded, an **open problem**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/search_bib/Er76d?sources_only=1 "
  
    Erdős Problems
  
"

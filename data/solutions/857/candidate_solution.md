Write ([n]={1,\dots,n}), and let

[
F_k(n):=\max{|\mathcal F|:\ \mathcal F\subseteq 2^{[n]}\text{ contains no (k)-sunflower}}.
]

Then your $m(n,k)$ is simply
[
m(n,k)=F_k(n)+1,
]
since $m(n,k)$ is “one more than the largest $k$-sunflower–free family”. [[nomath]](One usually assumes the $A_i$ are distinct; repeats only make it easier to find a sunflower.)[[/nomath]] ([arXiv][1])

A convenient way to package the asymptotics is via the **$k$-sunflower-free capacity**
[
\mu_k^{\mathrm S}:=\lim_{n\to\infty} F_k(n)^{1/n},
]
which exists (tensor-power argument). In terms of this,
[
F_k(n)=(\mu_k^{\mathrm S}+o(1))^n,\qquad m(n,k)=(\mu_k^{\mathrm S}+o(1))^n.
]
Determining (\mu_k^{\mathrm S}) [[nomath]](or even showing $\mu_k^{\mathrm S}<2$)[[/nomath]] is the heart of the problem. ([arXiv][1])

## General lower bound [[nomath]](all $k\ge 3$)[[/nomath]]

A standard Erdős–Szemerédi construction gives an explicit exponential lower bound.

Assume (n=m(k-1)) and partition ([n]=R_1\sqcup\cdots\sqcup R_m) into blocks of size $k-1$. Let (t=\lceil (k-1)/2\rceil), and take (\mathcal F) to be all sets (S\subseteq[n]) with (|S\cap R_j|=t) for every block (R_j). Then (\mathcal F) is $k$-sunflower-free and has size
[
|\mathcal F|=\binom{k-1}{t}^{n/(k-1)}.
]
Hence, for all $n$,
[
F_k(n)\ \ge\ \binom{k-1}{\lceil (k-1)/2\rceil}^{\lfloor n/(k-1)\rfloor}.
]
The proof that this construction is $k$-sunflower-free is simple: inside any fixed block (R_j) [[nomath]](size $k-1$)[[/nomath]], $k$ distinct sets cannot have pairwise intersections all equal unless they are all identical on that block; forcing this on every block would make the $k$ sets identical overall, contradicting distinctness. 

Asymptotically [[nomath]](using $\binom{k-1}{\lfloor (k-1)/2\rfloor}\sim 2^{k-1}/\sqrt{k}$)[[/nomath]],
[
F_k(n)\ \ge\ 2^{\left(1-\Theta!\left(\frac{\log k}{k}\right)\right)n},
]
so for large $k$ you can have a $k$-sunflower-free family that is a (2^{-\Theta(n\log k/k)}) fraction of the whole cube (2^{[n]}). 

## Best results for $k=3$

This is the one case where we have a genuine “(c^n) with (c<2)” upper bound.

* **Upper bound (Naslund–Sawin):**
  [
  F_3(n)\ \le\ 3n\sum_{j\le n/3}\binom{n}{j}\ \le\ \left(\frac{3}{2^{2/3}}\right)^{n(1+o(1))}
  ]
  so
  [
  \mu_3^{\mathrm S}\le \frac{3}{2^{2/3}} \approx 1.889881574\ldots
  ]
  ([arXiv][2])

* **Lower bound (Deuber–Erdős–Gunderson–Kostochka–Meyer):**
  [
  \mu_3^{\mathrm S}>1.551,
  ]
  i.e. (F_3(n)\ge (1.551-o(1))^n). ([arXiv][1])

So, currently,
[
(1.551-o(1))^n \ \le\ F_3(n)\ \le\ (1.8898816+o(1))^n,
]
and therefore
[
(1.551-o(1))^n \ \le\ m(n,3)-1\ \le\ (1.8898816+o(1))^n.
]
([arXiv][1])

The exact base (\mu_3^{\mathrm S}) [[nomath]](hence a true asymptotic for $m(n,3)$)[[/nomath]] is not known.

## Upper bounds for (k\ge 4) (and what is open)

The classical **Erdős–Szemerédi sunflower conjecture** says that for every fixed (k\ge 3),
[
\mu_k^{\mathrm S}<2 \quad\text{equivalently}\quad F_k(n)\le 2^{(1-\varepsilon_k)n}=(2-\delta_k)^n
]
for some (\varepsilon_k>0). This is proved for $k=3$ but open for (k\ge 4). 

The best general upper bounds known for (k\ge 4) are only **subexponential savings** over (2^n). One form (coming from the improved uniform sunflower lemma plus the original Erdős–Szemerédi reduction) is:

> For each fixed (k\ge 3) there is (c=c(k)>0) such that if (|\mathcal F|\ge 2^{n(1-c(\log n)^{-(1+o(1))})}) then (\mathcal F\subseteq 2^{[n]}) contains a $k$-sunflower. ([ECCC][3])

Equivalently,
[
F_k(n)\ \le\ 2^{n(1-c(\log n)^{-(1+o(1))})}\qquad (k\ \text{fixed}),
]
which still allows (\mu_k^{\mathrm S}=2) and therefore does not resolve the conjecture for (k\ge 4). ([ECCC][3])

## Summary as estimates for $m(n,k)$

Let (m(n,k)=F_k(n)+1). Then:

* **General lower bound [[nomath]](all $k\ge 3$)[[/nomath]]:**
  [
  m(n,k)\ \ge\ \binom{k-1}{\lceil (k-1)/2\rceil}^{\lfloor n/(k-1)\rfloor}+1
  \ =\ 2^{(1-\Theta(\log k/k))n}\ \text{(for large (k))}.
  ]


* **$k=3$:**
  [
  (1.551-o(1))^n \ \le\ m(n,3)-1\ \le\ (1.8898816+o(1))^n.
  ]
  ([arXiv][1])

* **Fixed (k\ge 4):** conjecturally (m(n,k)=(2-\delta_k+o(1))^n), but currently the best upper bounds are only
  [
  m(n,k)\ \le\ 2^{n(1-c(\log n)^{-(1+o(1))})}+1.
  ]
  ([ECCC][3])

If you tell me whether you care most about **fixed $k$** (classic setting) or about regimes where **(k=k(n)) grows**, I can tailor the estimates to that regime; the behavior changes a lot as $k$ increases.

[1]: https://arxiv.org/pdf/2512.20055 "https://arxiv.org/pdf/2512.20055"
[2]: https://arxiv.org/abs/1606.09575 "[1606.09575] Upper bounds for sunflower-free sets"
[3]: https://eccc.weizmann.ac.il/report/2019/110/download "https://eccc.weizmann.ac.il/report/2019/110/download"

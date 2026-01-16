Let (R(3,k)) be the least (n) such that every red/blue colouring of (E(K_n)) contains either a red triangle or a blue (K_k) (equivalently: every triangle‑free graph on (n) vertices has an independent set of size (k)). ([arXiv][1])

As (k\to\infty) (with (\log) denoting the natural logarithm), the known asymptotics are
[
R(3,k)=\Theta!\left(\frac{k^2}{\log k}\right),
]
and more precisely the best current bounds are
[
\left(\frac12+o(1)\right)\frac{k^2}{\log k}\ \le\ R(3,k)\ \le\ (1+o(1))\frac{k^2}{\log k},.
]
([arXiv][1])

* The **upper bound** (R(3,k)\le (1+o(1)),k^2/\log k) is due to **Shearer (1983)** (building on Ajtai–Komlós–Szemerédi), via lower bounds on the independence number of triangle‑free graphs. ([arXiv][2])
* The **lower bound** (R(3,k)\ge (\tfrac12+o(1)),k^2/\log k) was proved very recently by **Hefty–Horn–King–Pfender (2025)** by constructing triangle‑free graphs with unusually small independence number. ([arXiv][1])

So the growth rate is settled up to a factor (2+o(1)), and it is now conjectured that the true constant is (1/2) (i.e. (R(3,k)\sim \frac12,k^2/\log k)), but the matching upper bound is still open. ([arXiv][1])

[1]: https://arxiv.org/pdf/2510.19718 "Improving $R(3,k)$ in just two bites"
[2]: https://arxiv.org/pdf/2601.05221 "Some recent results in Ramsey theory"

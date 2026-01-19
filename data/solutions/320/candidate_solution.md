Write
[
S(N)=|\\{\sum_{n\in A}\frac1n:;A\subseteq{1,2,\dots,N}\\}|.
]
This is exactly the number of *distinct* Egyptian-fraction values whose denominators are (\le N) (each denominator used at most once), i.e. the size of the set (E_N) in the Egyptian-fraction literature. ([arXiv][1])

## Easy bounds (to calibrate)

* Trivially (S(N)\le 2^N), since there are (2^N) subsets.
* A simple (but weak) lower bound comes from restricting to primes: if (A,B) are distinct subsets of primes (\le N), then (\sum_{p\in A}1/p\ne \sum_{p\in B}1/p) [[nomath]](multiply by $\prod_{p\in A\cup B}p$ and reduce mod a prime in the symmetric difference)[[/nomath]]. Hence
  [
  S(N)\ge 2^{\pi(N)}=\exp!\Big((\log 2+o(1))\frac{N}{\log N}\Big).
  ]
  This already shows $S(N)$ grows faster than any power of $N$, but it’s far from best known results.

## Best-known general bounds (iterated logarithms)

Let (\log_1 N=\log N) and (\log_{j+1}N=\log(\log_j N)) denote iterated natural logarithms.

### Upper bounds (Bleicher–Erdős, 1976)

Bleicher and Erdős proved strong subexponential upper bounds. In particular they show (Lemma 8) that for (\log_2 N\ge 1),
[
S(N)<\exp\Big(\frac{N}{\log_2 N}\Big),
]
and for (\log N\ge 1),
[
S(N)<\exp\Big(\frac{N\log_2 N}{\log N}\Big).
]


More generally (Theorem 3), for any integer (r\ge 1) with (\log_{2r}N\ge 1),
[
\log S(N)<\frac{N,\log_r N}{\log N}\prod_{j=3}^{r}\log_j N.
]


A key takeaway is already visible from the $r=2$ inequality:
[
\log S(N)\ \ll\ \frac{N\log\log N}{\log N}=o(N),
]
so (S(N)=\exp(o(N))): **the number of distinct subsums is subexponential in $N$**. 

### Lower bounds (Bettin–Grenié–Molteni–Sanna, 2025)

The best current lower bound (improving earlier work of Bleicher–Erdős) is: for every integer (k\ge 4) such that (\ln_k N\ge 3/2),
[
\frac{\ln S(N)}{\ln 2}\ge\Big(2-\frac{3}{\ln_k N}\Big)\frac{N}{\ln N}\prod_{j=3}^{k}\ln_j N.
]
([arXiv][1])

Equivalently,
[
\ln S(N)\ \ge\ \Big(2\ln 2+o(1)\Big)\frac{N}{\ln N}\prod_{j=3}^{k}\ln_j N
\qquad(\text{for any fixed }k\ge 4\text{ as }N\to\infty),
]
which is much stronger than the elementary (2^{\pi(N)}) bound. ([arXiv][1])

## What “estimate” we can currently give

Putting the best-known results together:

* For suitable (k\ge 4),
  [
  \ln S(N)\ \ge\ \Big(2\ln 2+o(1)\Big)\frac{N}{\ln N}\prod_{j=3}^{k}\ln_j N;
  ]
* For suitable (r\ge 1),
  [
  \ln S(N)\ \le\ \frac{N,\ln_r N}{\ln N}\prod_{j=3}^{r}\ln_j N,
  ]
  and in particular the clean unconditional-looking form
  [
  \ln S(N)\ \ll\ \frac{N\ln\ln N}{\ln N}
  ]
  holds for large $N$. ([arXiv][1])

So $S(N)$ is known to satisfy
[
\exp\Big(\Omega\Big(\frac{N}{\ln N}\cdot \ln_3 N\cdot \ln_4 N\cdots\Big)\Big)
\ \le\
S(N)
\ \le\
\exp!\Big(O\Big(\frac{N\ln\ln N}{\ln N}\Big)\Big),
]
with more refined iterated-log factors available on both sides as above.

The true order of growth is still not pinned down; closing the gap between these iterated-log bounds is part of an open Erdős-type problem. ([erdosproblems.com][2])

[1]: https://arxiv.org/abs/2509.10030 "https://arxiv.org/abs/2509.10030"
[2]: https://www.erdosproblems.com/tags/number%20theory "https://www.erdosproblems.com/tags/number%20theory"

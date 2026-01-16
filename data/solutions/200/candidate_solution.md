Let $L(N)$ be the maximum $k$ for which there exist primes
[
p_0<p_1<\cdots<p_{k-1}\le N,\qquad p_i=a+id
]
in arithmetic progression. Your question is whether
[
L(N)=o(\log N)\quad\text{as }N\to\infty,
]
i.e. (L(N)/\log N\to 0).

This is **open** (it’s an Erdős–Graham question and is listed as open as “Erdős Problem #200”). ([Erdős Problems][1])

### What *is* known unconditionally

A standard necessary local condition for a $k$-term prime progression forces the common difference to be divisible by many small primes, which yields the best general upper bound we currently have:
[
L(N)\le (1+o(1))\log N.
]
This is exactly the bound noted on the Erdős problem page. ([Erdős Problems][1])

One way to see the mechanism is:

* Suppose (a,a+d,\dots,a+(k-1)d) are all primes and (as is typical for large $N$) all exceed $k$.
* Fix a prime (q\le k). If (q\nmid d), then the residues (a, a+d, \dots, a+(k-1)d) are all distinct mod $q$, so among (k\ge q) consecutive residues one is (0\bmod q). That term would be divisible by $q$, hence not prime [[nomath]](since it’s $>q$)[[/nomath]]. Contradiction.
* Therefore (q\mid d) for every prime (q\le k), so $d$ is a multiple of the primorial (k#:=\prod_{q\le k}q).
* Since (a+(k-1)d\le N), we have ((k-1)d\le N), hence (k#\le d\le N).
* Taking logs and using (\log(k#)=\sum_{q\le k}\log q\sim k) (equivalent to the prime number theorem in this form) gives (k\lesssim \log N).

That yields the ((1+o(1))\log N) upper bound, but it does **not** improve to $o(\log N)$.

### What is known on the lower-bound side

We do know (L(N)\to\infty) as (N\to\infty), because Green–Tao proved that the primes contain arbitrarily long arithmetic progressions. ([Annals of Mathematics][2])
However, the known quantitative bounds are extremely weak [[nomath]](they don’t come close to pinning down $L(N)$ at the $\log N$ or $\log N/\log\log N$ scale)[[/nomath]], so they don’t resolve your (o(\log N)) question either.

### Heuristics (what people expect)

A common heuristic (Cramér/Hardy–Littlewood style) treats “being prime near $N$” as happening with probability (\approx 1/\log N), and counts the number of possible $k$-term progressions $(a,d)$ with (a+(k-1)d\le N), which is (\asymp N^2). This suggests an expected count roughly like
[
\text{(# candidates)}\times \text{(probability all (k) are prime)}
;\approx;
N^2 \cdot \frac{1}{(\log N)^k}.
]
Setting this (\approx 1) suggests the “threshold” $k$ is around
[
k \approx \frac{2\log N}{\log\log N},
]
which **is** (o(\log N)). But this remains heuristic; proving anything close to this is far beyond current methods.

**Bottom line:** nobody currently knows whether (L(N)=o(\log N)); it’s an open Erdős–Graham problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/200 "
  
    Erdős Problem #200
  
"
[2]: https://annals.math.princeton.edu/2008/167-2/p03 "The primes contain arbitrarily long arithmetic progressions | Annals of Mathematics"

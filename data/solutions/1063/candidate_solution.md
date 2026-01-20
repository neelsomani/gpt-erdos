Write
[
\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k!}.
]
For (m=n-i) [[nomath]](with $0\le i<k$)[[/nomath]] we have
$
\frac{\binom nk}{m}=\frac{\prod_{0\le j<k,\ j\ne i}(n-j)}{k!}.
$
Hence
$
m\mid \binom nk \quad\Longleftrightarrow\quad k!\mid \prod_{0\le j<k,\ j\ne i}(n-j).
$
Equivalently, in $p$-adic valuations,
$
m\mid \binom nk\quad\Longleftrightarrow\quad v_p(m)\le v_p\\(\binom nk\\)\ \text{ for every prime }p\le k
$
[[nomath]](primes $>k$ never appear in $k!$, so they are never cancelled and cause no obstruction)[[/nomath]].

The growth of (n_k) is dictated by the “large” primes $p$ with (p>\sqrt{k}). For such primes, (p^2>k), so in $k!$ the exponent is just
[
v_p(k!)=\\\lfloor\frac{k}{p}\\\rfloor=:j.
]
Among any $k$ consecutive integers, the count of multiples of $p$ is either $j$ or $j+1$ [[nomath]](because $k<(j+2)p$)[[/nomath]]. Ignoring the very rare event that one of these multiples is divisible by (p^2) (which does not affect the main asymptotics), we get
[
v_p\\(\binom nk\\)\in{0,1},
]
and [[nomath]](v_p$\binom nk$=1)[[/nomath]] occurs exactly when the block
[
n-k+1,\dots,n
]
contains $j+1$ multiples of $p$.

Now connect this to the “all but one divisor” condition:

* If (p\le k/2), then (j=\lfloor k/p\rfloor\ge 2), so there are **at least two** multiples of $p$ among (n-k+1,\dots,n). If [[nomath]](v_p$\binom nk$=0)[[/nomath]], then every number in that block that is divisible by $p$ fails to divide (\binom nk), giving at least two failures—impossible.
  Hence for every prime $p\in(\sqrt{k},k/2]$ we must have $v_p(\binom nk)\ge 1$.

* For primes (p\in(k/2,k]) [[nomath]](where $j=1$)[[/nomath]], there is typically one multiple of $p$ in the block. Only one index $i$ is allowed to fail, so aside from a negligible number of primes that can all divide the single “exceptional” number, we also need $v_p(\binom nk)\ge 1$ for essentially all these primes as well. This does not change the main exponential scale.

So, up to a negligible loss, a necessary condition is:
[
v_p\\(\binom nk\\)\ge 1 \quad \text{for almost all primes }p\le k \text{ with }p>\sqrt{k}.
]

For a prime $p$ with (j=\lfloor k/p\rfloor), the condition “$j+1$ multiples of $p$ lie in (n-k+1,\dots,n)” is a simple congruence restriction. Write (n\equiv r\pmod p) with (0\le r<p). Then the multiples of $p$ in the block are
[
n-r,\ n-r-p,\dots
]
and there are $j+1$ of them iff
[
r\le k-jp.
]
Thus, modulo $p$, the allowed residues form an interval of size
[
(k-jp)+1.
]
The allowed **proportion** is therefore
[
\frac{k-jp+1}{p}\sim \frac{k-jp}{p}=\frac{k}{p}-j=\\{\frac{k}{p}\\}\in(0,1],
]
the fractional part of $k/p$.

### Counting and the asymptotic scale

Take a set of primes $p$ [[nomath]](say $\sqrt{k}<p\le k$, which dominates asymptotically)[[/nomath]]. By the Chinese remainder theorem, the set of $n$ satisfying all these congruence restrictions has density approximately the product of the allowed proportions:
[
\prod_{p} \frac{k-\lfloor k/p\rfloor p}{p}.
]
Taking logs and using the prime number theorem to turn the sum over primes into an integral over (x=p/k), one obtains
[
\sum_{p\le k}\log\\(\frac{k-\lfloor k/p\rfloor p}{p}\\)
=-(C+o(1))\frac{k}{\log k},
]
where the constant $C$ can be computed explicitly:
[
C=\sum_{j=1}^\infty \frac{\log(1+1/j)}{j}\approx 1.2577468869.
]

Heuristically (and one can make this rigorous with CRT counting bounds), the number of admissible (n\le N) is about
[
N\exp\left(-(C+o(1))\frac{k}{\log k}\right).
]
Therefore the **first** such $n$ should occur when this quantity is (\approx 1), i.e.
[
\log n_k \sim C\frac{k}{\log k}.
]

### Conclusion

[
\boxed{\ \log n_k = \left(C+o(1)\right)\frac{k}{\log k}\quad\text{as }k\to\infty\ }
]
equivalently,
[
\boxed{\ n_k=\exp\left(\left(C+o(1)\right)\frac{k}{\log k}\right)\ },
\qquad
C=\sum_{j=1}^\infty \frac{\log(1+1/j)}{j}\approx 1.2577468869.
]

So (n_k) is **subexponential** in $k$: it grows faster than any fixed power of $k$, but slower than (e^{\varepsilon k}) for every fixed (\varepsilon>0).

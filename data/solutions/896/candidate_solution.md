Let
[
r_{A,B}(m):=|\\{(a,b)\in A\times B:\ ab=m\\}|,
\qquad
F(A,B):=|\\{m:\ r_{A,B}(m)=1\\}|,
]
and
[
M(N):=\max_{A,B\subseteq{1,\dots,N}} F(A,B).
]

## Lower bound: (M(N)\ge (1+o(1))\dfrac{N^2}{\log N})

Take
[
A:={p\ \text{prime}:\ N/\log N \le p\le N},
]
and let (B\subseteq{1,\dots,N}) be the set of integers **not divisible by any** (p\in A).

* By the prime number theorem, (|A|=(1+o(1))\dfrac{N}{\log N}).
* The set excluded from $B$ is (\bigcup_{p\in A}{n\le N:\ p\mid n}), whose size is at most
  [
  \sum_{p\in A}\frac{N}{p}
  =N\sum_{p\in A}\frac1p
  =o(N),
  ]
  since (\sum_{p\in [N/\log N,N]} \frac1p = \log\log N-\log\log(N/\log N)+o(1)=o(1)).
  Hence (|B|=(1+o(1))N).

Now if (p\in A) and (b\in B), the product $m=pb$ has a **unique** representation in (A\times B): if (pb=p'b') with (p,p'\in A) primes, then either (p=p') and (b=b'), or [[nomath]](if $p\neq p'$)[[/nomath]] we’d have (p\mid b'), contradicting (b'\in B). Therefore every element of (AB) is counted, i.e. $F(A,B)=|A||B|$, and
[
F(A,B)=(1+o(1))\frac{N}{\log N}\cdot (1+o(1))N=(1+o(1))\frac{N^2}{\log N}.
]
This construction (and the bound) is recorded explicitly in the discussion of Erdős Problem #896. ([Erdős Problems][1])

So
[
M(N)\ge (1+o(1))\frac{N^2}{\log N}.
]

## Upper bound: (M(N)\ll \dfrac{N^2}{(\log N)^{\delta}(\log\log N)^{3/2}})

For any (A,B\subseteq{1,\dots,N}), every $m$ counted by $F(A,B)$ is certainly a product of two integers (\le N). Also, the counted $m$’s are **distinct**. Hence
[
F(A,B)\le |\\{ab:\ 1\le a,b\le N\\}|,
]
i.e. $F(A,B)$ is bounded by the number of **distinct entries in the (N\times N) multiplication table**.

Kevin Ford proved that the number of distinct products in the multiplication table has order
[
\asymp \frac{N^2}{(\log N)^{\delta}(\log\log N)^{3/2}},
\qquad
\delta = 1-\frac{1+\log\log 2}{\log 2}\approx 0.08607,
]
via results on integers with a divisor in an interval (this is the resolution of the classic Erdős “multiplication table problem”). ([Annals of Mathematics][2])

Therefore,
[
M(N)\ll \frac{N^2}{(\log N)^{\delta}(\log\log N)^{3/2}}.
]
This is exactly the upper bound quoted on the Erdős Problem #896 page. ([Erdős Problems][1])

## Summary of the best-known estimate

Putting the two bounds together,
[
(1+o(1))\frac{N^2}{\log N}
\le
\max_{A,B\subseteq{1,\dots,N}}F(A,B)
;\ll;
\frac{N^2}{(\log N)^{\delta}(\log\log N)^{3/2}},
\quad
\delta\approx 0.08607.
]
([Erdős Problems][1])

Closing the (large) gap between these bounds is the substance of the problem as currently understood.

[1]: https://www.erdosproblems.com/forum/thread/896 "https://www.erdosproblems.com/forum/thread/896"
[2]: https://annals.math.princeton.edu/wp-content/uploads/annals-v168-n2-p01.pdf "https://annals.math.princeton.edu/wp-content/uploads/annals-v168-n2-p01.pdf"

Let (k=\lfloor \sqrt N\rfloor).  For any (A\subseteq{1,\dots,N}) with (|A|=k),

[
(A+A)\cap[1,N]={a+a':a,a'\in A,\ a+a'\le N}.
]

### Upper bound

Each distinct sum in ((A+A)\cap[1,N]) comes from at least one unordered pair ({a,a'}) with (a,a'\in A) [[nomath]](allowing $a=a'$)[[/nomath]]. The number of such pairs is
[
\binom{k+1}{2}=\frac{k(k+1)}2=\frac{N}{2}+O(\sqrt N),
]
so
[
f(N)\le \frac{N}{2}+O(\sqrt N)=\\(\frac12+o(1)\\)N.
]
[[nomath]](This is the $(\tfrac12+o(1))N$ upper bound quoted by Erdős–Freud as well. $[Erdős Problems][1]$)[[/nomath]]

### Lower bound [[nomath]](construction giving $3N/8$)[[/nomath]]

Erdős–Freud proved a construction giving
[
f(N)\ge \\(\frac38-o(1)\\)N. \quad \text{([Erdős Problems][1])}
]

Here is a standard way to see the constant (\tfrac38) using a *cyclic Sidon set* (Bose–Chowla type construction):

* For a prime power $q$, there exists a Sidon set $B$ in the cyclic group (\mathbb Z_{q^2-1}) with (|B|=q) (Bose–Chowla). 
  Take representatives (B\subseteq{0,1,\dots,M-1}) with (M=q^2-1).

* Define
  [
  A := B \ \cup\ (B+M)\subseteq {0,1,\dots,2M-1}.
  ]
  Then (|A|=2q), while $N$ can be taken (\asymp 4M) [[nomath]](and for general $N$, pick $q$ so that $4M\le N$ and use monotonicity; the loss is $o(N)$)[[/nomath]].

* Because $B$ is Sidon mod $M$, the sums in $B+B$ are all distinct **and** no two sums in $B+B$ differ by $M$ [[nomath]](otherwise they’d be equal mod $M$)[[/nomath]]. Hence the three translates
  [
  (B+B),\quad (B+B)+M,\quad (B+B)+2M
  ]
  are pairwise disjoint as sets of integers inside $[0,4M]$.

* Therefore
  [
  |A+A|=3|B+B|=3\binom{q+1}{2}=\frac{3}{2}q(q+1)
  =\\(\frac38+o(1)\\)\cdot 4q^2
  =\\(\frac38+o(1)\\)N.
  ]

So (f(N)\ge (\tfrac38-o(1))N).

### Conclusion / best-known asymptotic estimate

Putting the bounds together,
[
\boxed{\\(\frac38-o(1)\\)N \ \le\ f(N)\ \le\ \\(\frac12+o(1)\\)N.}
]
These asymptotics [[nomath]](linear growth with constants between $3/8$ and $1/2$)[[/nomath]] are exactly the bounds recorded for this Erdős problem by Erdős–Freud. ([Erdős Problems][1])

If you want, I can also write the lower-bound construction in “fully integer” form for arbitrary $N$ [[nomath]](choosing an appropriate prime power $q$ and embedding the set into ${1,\dots,N}$ cleanly)[[/nomath]], but asymptotically it won’t change the (\tfrac38) constant.

[1]: https://www.erdosproblems.com/latex/819 "https://www.erdosproblems.com/latex/819"

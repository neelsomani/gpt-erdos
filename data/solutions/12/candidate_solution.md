Call such a set (A\subset\mathbb N) a **$P$-set** (this is standard terminology): no element (a\in A) divides $b+c$ for two *larger* distinct (b,c\in A).

As of the current literature, all three questions you wrote down are still unresolved in full generality, but there are some fairly sharp partial results.

## What is known about how large (A\cap[1,N]) can be

Erdős and Sárközy proved that every infinite $P$-set has **asymptotic density (0)**, i.e.
[
\frac{|A\cap[1,N]|}{N}\to 0,
]
but they also showed this is “essentially best possible” in the sense that for **any** function (f(N)\to\infty) one can build a $P$-set $A$ with
[
|A\cap[1,N]|>\frac{N}{f(N)}
]
for infinitely many $N$.
So you cannot hope for a strong upper bound that holds for *all* (N).

On the **lower-bound** side for “square-root sized” growth:

* A classical example (already noted by Erdős–Sárközy) is
  [
  A={p^2:\ p\ \text{prime},\ p\equiv 3!!\pmod 4},
  ]
  which satisfies $P$ and has
  [
  \liminf_{N\to\infty}\frac{|A\cap[1,N]|}{\sqrt N},\log N>0,
  ]
  i.e. $|A\cap[1,N]|$ is on the order of (\sqrt N/\log N).

* Elsholtz and Planitzer improved this by constructing a $P$-set with
  [
  |A\cap[1,N]|\gg \frac{\sqrt N}{(\log N)^{1/2}(\log\log N)^2(\log\log\log N)^2}.
  ]

### Your first question

> Is there such an $A$ with (\displaystyle \liminf_{N\to\infty}\frac{|A\cap[1,N]|}{N^{1/2}}>0)?

**Still open.** The best constructions known fall short of a positive constant by logarithmic factors (as above), and no impossibility result is known that rules out (\asymp \sqrt N) for *all* large $N$.

## Power-saving upper bounds along infinitely many $N$

### Your second question

> Does there exist an absolute (c>0) such that every infinite $P$-set $A$ has infinitely many $N$ with (|A\cap[1,N]|<N^{1-c})?

**Open in general**, but there is a strong partial result under an extra hypothesis:

* If the elements of $A$ are **pairwise coprime**, Schoen proved that
  [
  |A\cap[1,N]|\ll N^{2/3}
  ]
  for infinitely many $N$, and Baier improved this to
  [
  |A\cap[1,N]|\ll \frac{N^{2/3}}{\log N}
  ]
  for infinitely many $N$.
  So for pairwise coprime $P$-sets, you can take (c=1/3).

Also, any *universal* $c$ (even if it exists) must satisfy (c\le 1/2): the prime-squares example above has (|A\cap[1,N]|) around (\sqrt N/\log N), which is eventually **larger** than (N^{1/2-\varepsilon}) for any fixed (\varepsilon>0).

## Convergence of (\sum_{n\in A}1/n)

### Your third question

> Is it true that (\sum_{n\in A}\frac1n<\infty)?

This is also **open** in general (it’s posed as part of the same Erdős–Sárközy problem).

What we can say:

* Many **known constructions** of large $P$-sets (including the prime-squares example and the Elsholtz–Planitzer construction) lie very close to “square-like” sets, and for those examples the reciprocal sum **does** converge [[nomath]](heuristically because the $n$-th element grows roughly like $n^2$ up to logs)[[/nomath]].
* But density $0$ alone doesn’t decide this [[nomath]](e.g. primes have density $0$ but $\sum 1/p$ diverges)[[/nomath]], so proving convergence would require a genuinely stronger global structural/size theorem for $P$-sets than is currently known.

## Extra context: the finite version is now settled

Unrelated to your three asymptotic questions but often mentioned alongside them: the **finite extremal problem** [[nomath]](“how large can $A\subset[1,n]$ be with property $P$?”)[[/nomath]] was recently resolved by Bedert, showing (|A|\le \lfloor n/3\rfloor+1) for all sufficiently large $$n$$.

---

If you want, I can also sketch why the “(p^2) with (p\equiv3!!\pmod4)” construction satisfies the divisibility condition [[nomath]](it’s a clean one-line use of “$-1$ is a nonresidue mod $p\equiv3\pmod4$”)[[/nomath]].

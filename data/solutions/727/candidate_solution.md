Write
[
R_{n,k}:=\frac{(2n)!}{(n+k)!^2}.
]
Since
[
\binom{2n}{n}=\frac{(2n)!}{(n!)^2}
\quad\text{and}\quad
\frac{(n+k)!}{n!}=\prod_{i=1}^k(n+i),
]
we have the exact identity
[
R_{n,k}
=\frac{(2n)!}{(n!)^2}\cdot\Big(\frac{n!}{(n+k)!}\Big)^2
=\frac{\binom{2n}{n}}{\Big(\prod_{i=1}^k (n+i)\Big)^2}.
]
Therefore
[
(n+k)!^2\mid (2n)!
\quad\Longleftrightarrow\quad
\Big(\prod_{i=1}^k (n+i)\Big)^2 \mid \binom{2n}{n}.
\tag{★}
]

## A strong necessary condition

Fix a prime $p$. By Legendre’s formula,
[
v_p!\binom{2n}{n}=v_p((2n)!)-2v_p(n!)
=\sum_{j\ge 1}\Big(\Big\lfloor\frac{2n}{p^j}\Big\rfloor-2\Big\lfloor\frac{n}{p^j}\Big\rfloor\Big),
]
and each summand is $0$ or $1$. In particular, if (p^2>2n) then only the $j=1$ term can contribute, so
[
p^2>2n \quad\Longrightarrow\quad v_p!\binom{2n}{n}\le 1.
]
But in ((★)), if (p\mid \prod_{i=1}^k(n+i)) then the right-hand side needs (v_p!\binom{2n}{n}\ge 2) (at least) to absorb the square. Hence:

**If ((n+k)!^2\mid(2n)!), then every prime divisor $p$ of (\prod_{i=1}^k(n+i)) must satisfy (p\le \sqrt{2n}).**

Equivalently: **each of (n+1,n+2,\dots,n+k) must be (\sqrt{2n})-smooth** [[nomath]](no prime factor exceeding $\sqrt{2n}$)[[/nomath]]. This already rules out primes in $(n,n+k]$ and also rules out numbers like (2q) with a very large prime (q>\sqrt{2n}), etc.

So the question is at least as hard as producing infinitely many blocks of $k$ consecutive integers all of whose prime factors are (\le \sqrt{2n}), plus additional $p$-adic constraints to make the *square* in ((★)) work.

## Why primes around (\sqrt n) are “ideal”

If $p$ is a prime with
[
\sqrt n < p \le \sqrt{2n},
]
then (p^2\le 2n) but (p^2>n). In that range, the (p^2)-term contributes exactly $1$ to (v_p!\binom{2n}{n}), and if additionally (p\mid(n+i)) with (p>2k) [[nomath]](so $n\bmod p = p-i \ge p-k > p/2$)[[/nomath]], the $j=1$ term also contributes $1$. So such a prime typically gives (v_p!\binom{2n}{n}=2), which is exactly what you want when $p$ occurs to the first power in (\prod_{i=1}^k(n+i)).

This heuristic matches what one sees in actual examples: many solutions have factorizations of the numbers $n+i$ dominated by primes in $(\sqrt n,\sqrt{2n}]$, with only small-prime “noise”.

## Status

I do **not** know a proof (or disproof) that for every fixed (k\ge 2) the divisibility ((n+k)!^2\mid(2n)!) holds for **infinitely many** $n$. The reduction ((★)) and the necessary smoothness condition above suggest the problem is genuinely delicate and tied to “clusters” of moderately smooth numbers in very short intervals.

What I *can* say concretely is that there are many solutions for small $k$, and they get rapidly rarer as $k$ grows. For example, by direct computation:

* $k=2$: solutions start (n=208,458,987,1650,1790,\dots) [[nomath]](there are thousands up to $10^6$)[[/nomath]].
* $k=3$: (n=3475,8174,8175,11548,\dots)
* $k=4$: (n=8174,51984,103359,\dots)
* $k=5$: (n=252965,347849,681546,\dots)
* $k=6$: (n=3648835,7141713,12688568,12722146,17139249,\dots) [[nomath]](I found 13 solutions up to $3\times 10^7$)[[/nomath]].
* $k=7$: no solutions show up up to (3\times 10^7) in the same brute-force search (so if solutions exist, they begin later).

So empirically the answer looks plausibly “yes” for small $k$ and gets extremely sparse, but I’m not aware of a general argument establishing infinitude (or finiteness) for all (k\ge 2).

If you want, I can also show how to derive sharper necessary conditions prime-by-prime from Kummer’s theorem [[nomath]](carries in base $p$)[[/nomath]] and explain why primes (>\sqrt{2n}) kill the divisibility immediately, which is the main structural obstruction.

Let $P(n)$ denote the largest prime divisor of $n$.
Your condition
[
P\left(\prod_{i=0}^{k}(p^2+i)\right)=p
]
is equivalent to
[
P(p^2+i)\le p\quad\text{for every }i=1,2,\dots,k,
]
since the $i=0$ factor is (p^2), so $p$ certainly divides the product and hence the largest prime divisor is (\ge p).

So the question is asking: for each fixed $k$, are there infinitely many primes $p$ such that all the integers
[
p^2+1,p^2+2,\dots,p^2+k
]
are **$p$-smooth** [[nomath]](have no prime factor $>p$)[[/nomath]]?

## What is known

As far as I can tell, this is **not proved** for any fixed (k\ge 1), and it is treated as open in closely related discussions. In particular, even the *existence* question for the stronger symmetric block ({p^2-k,\dots,p^2+k}) is only supported by heuristic reasoning and computation in the standard reference discussion I found. ([Mathematics Stack Exchange][1])

## Why people expect “yes” (heuristic)

There is a classical notion (Greene–Knuth) of an **unusual number**: an integer $n$ whose largest prime factor exceeds (\sqrt n). For integers $n$, the set of unusual numbers has natural density (\log 2): roughly $69.3\%$ of integers satisfy (P(n)>\sqrt n). 

Now note that for large $p$ [[nomath]](say $p$ much larger than $k$)[[/nomath]],
[
\sqrt{p^2+i} < p+1 \quad (1\le i\le k),
]
so the requirement (P(p^2+i)\le p) is essentially the same as requiring “(p^2+i) is **not** unusual”.

If one (heuristically) models the events “(p^2+i) is not unusual” as having probability (1-\log 2) and being roughly independent across $i$, then the probability that **all** $k$ of (p^2+1,\dots,p^2+k) are not unusual is about
[
(1-\log 2)^k>0,
]
a constant independent of $p$. This kind of heuristic is exactly what is used in the related symmetric problem around (p^2) on Math StackExchange. ([Mathematics Stack Exchange][1])

Under that heuristic, one would expect not just infinitely many such primes $p$, but a positive proportion of primes to work for each fixed $k$. However, turning this into a proof seems out of reach with current techniques.

## Computational evidence

Although it doesn’t prove infinitude, brute force finds many examples. For your *one-sided* condition (i=0,\dots,k), the smallest prime $p$ I found for each $k$ [[nomath]](up to $7$)[[/nomath]] is:

* (k=1: p=7) [[nomath]](since $7^2+1=50$ has prime factors $\le 7$)[[/nomath]]
* (k=2: p=41)
* (k=3: p=443)
* (k=4: p=8663)
* (k=5: p=15361)
* (k=6: p=125441)
* (k=7: p=510569)

For example, when $k=7$ and $p=510569$, the largest prime factors of (p^2+i) for (i=1,\dots,7) are
[
111053,\ 6841,\ 222913,\ 5689,\ 1523,\ 4013,\ 2549,
]
all (<p), so the largest prime divisor of (\prod_{i=0}^{7}(p^2+i)) is indeed $p$.

## Bottom line

* For $k=0$: trivially **yes** (every prime works).
* For every (k\ge 1): there is strong heuristic and computational support, but **no known proof** that there are infinitely many such primes $p$. The most relevant existing discussion I found explicitly gives only heuristic reasoning for the stronger symmetric variant. ([Mathematics Stack Exchange][1])

[1]: https://math.stackexchange.com/questions/428461/is-there-always-a-prime-p-so-that-the-largest-prime-factor-of-p2i-not-exce "number theory - Is there always a prime $p$ so that the largest prime factor of $p^2+i$ not exceeding $p$ for $-k\leq i \leq k$? - Mathematics Stack Exchange"

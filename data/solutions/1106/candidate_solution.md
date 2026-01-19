Write
[
F(n)=\omega\Big(\prod_{k=1}^n p(k)\Big),
]
where (\omega(\cdot)) is the number of **distinct** prime divisors. Equivalently, $F(n)$ is the size of the union of the prime-divisor sets of (p(1),p(2),\dots,p(n)). In particular $F(n)$ is **nondecreasing** in $n$.

## 1) Does (F(n)\to\infty) as (n\to\infty)?

Yes.

Ken Ono proved Erdős’s conjecture that **for every prime $m$** there exists at least one $n$ with
[
p(n)\equiv 0 \pmod m,
]
i.e. (m\mid p(n)). ([arXiv][1])

Now fix any integer $M$. Take any $M$ distinct primes (q_1,\dots,q_M). For each (q_i), choose (n_i) such that (q_i\mid p(n_i)) (possible by Ono’s result). Let (N=\max_i n_i). Then every (q_i) divides (\prod_{k\le N}p(k)), so (F(N)\ge M). Since $F$ is nondecreasing, this implies (F(n)\to\infty).

[[nomath]](Actually, Ono’s work gives far more: for each prime $m\ge 5$ there are infinitely many $n$ with $p(n)\equiv 0\pmod m$; the corollary above already suffices for the divergence of $F(n)$. $[arXiv][1]$)[[/nomath]]

## 2) Is (F(n)>n) for all sufficiently large $n$?

As far as the literature I can locate, this is **not proved**.

What is known is much weaker growth. Schinzel–Wirsing proved that $F(n)$ grows at least logarithmically [[nomath]](more precisely, $F(n) > C\log n$ for any fixed $C<1/\log 2$, for all large $n$)[[/nomath]]. ([OEIS][2])

Computationally, however, it seems very plausible that $F(n)$ eventually dominates $n$: OEIS reports that **it appears** (F(n)>n) for all (n>115) [[nomath]](equivalently $F(n)-n>0$ for $n>115$)[[/nomath]]. ([OEIS][2])
For example, a direct check gives (F(115)=115) and (F(116)=117), so the inequality does start holding very early; but turning this into a proof for all sufficiently large $n$ seems open with current methods. ([OEIS][3])

[1]: https://arxiv.org/pdf/math/0008140 "https://arxiv.org/pdf/math/0008140"
[2]: https://oeis.org/A194259 "https://oeis.org/A194259"
[3]: https://oeis.org/A194260 "https://oeis.org/A194260"

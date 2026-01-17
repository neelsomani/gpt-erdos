Let
[
S(n):=\sum_{p\le n}\frac1p\mathbf 1_{{n\bmod p\in(p/2,p)}}.
]
[[nomath]](So the indicator is $1$ exactly when the residue $r=n\bmod p$ lies in the “upper half” ${(p+1)/2,\dots,p-1}$ for odd $p$; for $p=2$ it is always $0$.)[[/nomath]]

A clean way to make sense of the asymptotic is: **for a set of integers $n$ of natural density $1$** [[nomath]](equivalently: if you pick $n$ uniformly at random from $\\{1,\dots,N\\}$ and let $N\to\infty$, the statement holds with probability $\to1$)[[/nomath]]. Under that interpretation one indeed has
[
S(n)\sim \frac12\log\log n.
]

Here is a proof.

---

## 1) Fix the prime cutoff and compute the mean

For a parameter (y\ge 3), define the truncated sum
[
S_y(n):=\sum_{p\le y}\frac1p\mathbf 1_{{n\bmod p\in(p/2,p)}}.
]

For an odd prime $p$, exactly $(p-1)/2$ residue classes mod $p$ lie in $(p/2,p)$, so
[
\mathbb E\Big[\mathbf 1_{{n\bmod p\in(p/2,p)}}\Big]=\frac{p-1}{2p}
\qquad (p\text{ odd}),
]
and for (p=2) the expectation is $0$.

Thus
[
\mu_y:=\mathbb E[S_y(n)]
=\sum_{p\le y}\frac1p\mathbb E\Big[\mathbf 1_{{n\bmod p\in(p/2,p)}}\Big]
=\sum_{\substack{p\le y\ p>2}}\frac{p-1}{2p^2}.
]
Rewrite
[
\frac{p-1}{2p^2}=\frac1{2p}-\frac1{2p^2},
]
so
[
\mu_y
=\frac12\sum_{p\le y}\frac1p +O(1),
]
because (\sum_p 1/p^2) converges.

By Mertens’ theorem,
$
\sum_{p\le y}\frac1p=\log\log y+O(1),
$
hence
$
\mu_y=\frac12\log\log y+O(1).
$

---

## 2) Concentration: fluctuations are tiny compared to (\log\log y)

Now we use independence across primes.

For fixed $y$, let
[
P_y:=\prod_{p\le y}p.
]
The quantity (S_y(n)) depends only on (n\bmod P_y). As $n$ runs through a complete residue system mod (P_y), the CRT implies the residues ((n\bmod p)*{p\le y}) are jointly uniform and independent. Therefore the random variables
[
X_p(n):=\mathbf 1*{{n\bmod p\in(p/2,p),}}\qquad (p\le y)
]
are independent [[nomath]](for $n$ uniform mod $P_y$)[[/nomath]].

Each summand (X_p(n)/p) lies in $[0,1/p]$. Apply Hoeffding’s inequality to the weighted sum (S_y(n)=\sum_{p\le y} X_p(n)/p):
[
\mathbb P\big(|S_y-\mu_y|>t\big)
\le
2\exp\left(
-\frac{2t^2}{\sum_{p\le y}(1/p)^2}
\right).
]
But (\sum_p 1/p^2<\infty), so (\sum_{p\le y}(1/p)^2\le C) for an absolute constant $C$. Hence
[
\mathbb P\big(|S_y-\mu_y|>t\big)\le 2e^{-c t^2}
]
for some absolute (c>0).

Take (y=2^k) and (t=(\log\log y)^{2/3}). Then (\log\log(2^k)=\log k+O(1)), so
[
\sum_{k\ge 3}\mathbb P\Big(|S_{2^k}-\mu_{2^k}|>(\log\log 2^k)^{2/3}\Big)
\ll\sum_{k\ge 3}\exp!\big(-c(\log k)^{4/3}\big)
<\infty.
]
Since the “bad sets” here are unions of residue classes mod (P_{2^k}), their probabilities equal their natural densities. A standard Borel–Cantelli/union-bound argument then shows:

> For a set of integers $n$ of density $1$,
> $S_{2^k}(n)=\mu_{2^k}+O\big((\log\log 2^k)^{2/3}\big) \quad\text{for all sufficiently large }k$
> In particular, for such $n$,
> $S_{2^k}(n)=\mu_{2^k}+o(\log\log 2^k).$

---

## 3) Replace the dyadic cutoff by the moving cutoff (p\le n)

Now take one of those “good” integers $n$, and choose $k$ so that
$2^k\le n<2^{k+1}.$
Then
$$
S(n)=\sum_{p\le n}\frac{X_p(n)}p = S_{2^{k+1}}(n)-\sum_{n<p\le 2^{k+1}}\frac{X_p(n)}p.
$$

The tail is nonnegative and bounded by

$
0\le \sum_{n<p\le 2^{k+1}}\frac{X_p(n)}p\le \sum_{n<p\le 2^{k+1}}\frac1p
\log\log(2^{k+1})-\log\log n+o(1)
=O(\frac1k)
=o(1),
$

since (n\in[2^k,2^{k+1})) implies (\log n\asymp k) and (\log\log) changes by (O(1/k)) across a factor of 2.

So for density-1 many $n$,
[
S(n)=S_{2^{k+1}}(n)+o(1)

\mu_{2^{k+1}}+o(\log\log 2^{k+1}).
]
Using (\mu_{2^{k+1}}=\tfrac12\log\log(2^{k+1})+O(1)) and (\log\log(2^{k+1})=\log\log n+o(\log\log n)), we get
[
S(n)=\frac12\log\log n+o(\log\log n).
]

That is exactly
[
\sum_{p\le n}1_{n\in (p/2,p)\pmod{p}}\frac{1}{p}\sim \frac{\log\log n}{2}
]
**for almost all integers $n$** [[nomath]](density $1$)[[/nomath]].

---

### Remark

This method actually shows much more: the fluctuations around (\frac12\log\log n) are very tight (subgaussian tails) because the coefficients $1/p$ are square-summable. So, heuristically, the sum is (\frac12\log\log n + O(1)) “most of the time”.

If you meant the asymptotic to hold **for every integer $n$** (not just almost all), that’s a stronger deterministic claim and is not what the above probabilistic/CRT argument proves.
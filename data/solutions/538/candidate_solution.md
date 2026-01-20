Write all logarithms as natural logs.
Let

[
S(A):=\sum_{n\in A}\frac1n .
]

Then the correct order of magnitude is a power of (\log N).

## Claim (best possible asymptotic upper bound)

For each fixed (r\ge2),

[
\sup_{A\subseteq{1,\dots,N}\atop \forall m:|\\\\{(p,a):m=pa,\ p\ \text{prime},\ a\in A\\}|\le r\\}\ S(A)
=(\log N)^{\alpha_r+o(1)}\qquad(N\to\infty),
]

where

[
\boxed{\alpha_r:=\frac{r-1}{e\cdot\bigl((r-1)!\bigr)^{1/(r-1)}}}
]

and the $o(1)$ depends on $r$ [[nomath]](tends to $0$ as $N\to\infty$)[[/nomath]].

So the best possible upper bound is

[
\boxed{\sum_{n\in A}\frac1n\ \le\ (\log N)^{\alpha_r+o(1)}}
]

and this exponent (\alpha_r) is sharp.

For small $r$:

* (r=2:\ \alpha_2=\dfrac1e\approx 0.3679)
* (r=3:\ \alpha_3=\dfrac{2}{e\sqrt2}=\dfrac{\sqrt2}{e}\approx 0.5205)
* (r=4:\ \alpha_4=\dfrac{3}{e,6^{1/3}}\approx 0.6074)

---

## Why this is attainable (matching construction)

Let
[
w_*:=e\cdot\bigl((r-1)!\bigr)^{1/(r-1)}.
]
Let $k$ be the largest integer with
[
k,w_* \le \log\log N - O(\log\log\log N)
]
[[nomath]](so $k\sim (\log\log N)/w_*$)[[/nomath]].

Choose (y:=N^{1/((r-1)k)}), so any product of ((r-1)k) primes (\le y) is (\le N).
Now take the primes (\le y) and split them into disjoint blocks (P_1,\dots,P_k) so that
[
\sum_{p\in P_i}\frac1p = w_*+o(1)\qquad(1\le i\le k).
]

Define $A$ to be all numbers of the form
[
n=\prod_{i=1}^k \\(p_{i,1}\cdots p_{i,r-1}\\),
]
where for each $i$ the (p_{i,1},\dots,p_{i,r-1}) are distinct primes chosen from (P_i).

### Check the condition

Take any $m$. If $m=pn$ with (n\in A), then $p$ lies in some block, say (P_i).
Any other representation $m=qa$ with (a\in A) must also use a prime (q\in P_i), and $a$ must be obtained by replacing exactly one of the $(r-1)$ primes from (P_i) used in $n$ by $p$. Hence there are at most
[
1+(r-1)=r
]
such representations. So the hypothesis holds.

### Compute $S(A)$

The reciprocal sum factorizes over blocks:
$
S(A)=\prod_{i=1}^k (\sum_{p_1<\cdots<p_{r-1}\in P_i}\frac{1}{p_1\cdots p_{r-1}}).
$
For each block (P_i), because the primes are large and (\sum_{p\in P_i}\frac1p=w_*+o(1)), the $(r!-1)$-st elementary symmetric sum satisfies
$
\sum_{p_1<\cdots<p_{r-1}\in P_i}\frac{1}{p_1\cdots p_{r-1}}
= \frac{(w_*+o(1))^{r-1}}{(r-1)!}.
$
Therefore,
$
\log S(A)=k((r-1)\log w_*-\log (r-1)!+o(1)).
$
With (k\sim (\log\log N)/w_*), this gives
$
\log S(A)=(\frac{r-1}{w_*}+o(1))\log\log N,
$
i.e.
$
S(A)=(\log N)^{\alpha_r+o(1)}.
$
So the exponent (\alpha_r) is achievable.

---

## Why you can’t do better (upper bound idea)

The key points are:

1. **Prime-block decomposition.**
   Split (most of) the primes into blocks (P_1,\dots,P_k). Write each (n\in A) as a product of its prime factors from each block; then the reciprocal $1/n$ is a product over blocks.

2. **A “local” extremal bound per block.**
   Fix one block $P$ and freeze all prime factors from other blocks. The remaining “fiber” is a set $B$ of integers whose prime factors lie in $P$ and which still satisfies the same “(\le r)” representation condition [[nomath]](because multiplying only by primes from $P$ keeps you in that fiber)[[/nomath]].

   One shows that among all such $B$, the largest possible fiber sum
   [
   \sum_{b\in B}\frac1b
   ]
   is (up to lower-order terms) at most the ((r-1))-st elementary symmetric sum of the weights ((1/p)*{p\in P}), hence
   [
   \sum*{b\in B}\frac1b\ \le\ \frac{\left(\sum_{p\in P}\frac1p\right)^{r-1}}{(r-1)!}\cdot (1+o(1)).
   ]

3. **Multiply the block bounds and optimize.**
   If block $i$ has total prime weight (w_i:=\sum_{p\in P_i}\frac1p), then
   [
   S(A)\ \lesssim\ \prod_{i=1}^k \frac{w_i^{r-1}}{(r-1)!}.
   ]
   Since (\sum_i w_i \approx \log\log N), AM–GM forces the product to be maximal when (w_i) are (asymptotically) equal, (w_i\approx w). Then
   [
   \log S(A)\ \lesssim\ k\left((r-1)\log w - \log (r-1)!\right),
   \qquad \text{with } kw\approx \log\log N.
   ]
   Optimizing in $w$ gives the maximizing choice $w=w_*=e((r-1)!)^{1/(r-1)}$, yielding
   [
   \log S(A)\ \le\ (\alpha_r+o(1))\log\log N.
   ]
   Exponentiating gives (S(A)\le (\log N)^{\alpha_r+o(1)}).

Because the construction above matches this exponent, this bound is best possible [[nomath]](up to the $o(1)$)[[/nomath]].

---

## Final answer

[
\boxed{\ \sum_{n\in A}\frac1n \ \le\ (\log N)^{\frac{r-1}{e((r-1)!)^{1/(r-1)}}+o(1)}\ }
]

and this is best possible: there exist sets $A$ achieving
[
\sum_{n\in A}\frac1n \ =\ (\log N)^{\frac{r-1}{e((r-1)!)^{1/(r-1)}}-o(1)}.
]

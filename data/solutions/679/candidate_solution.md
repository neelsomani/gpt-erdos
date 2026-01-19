As far as I can tell, your first question [[nomath]](the $(1+\varepsilon)$-version)[[/nomath]] is **currently open**. It is recorded as Erdős Problems #679 and is listed there as unsolved. ([Erdős Problems][1])

For the second question: **yes, the stronger bound**
[
\omega(n-k) < \frac{\log k}{\log\log k}+O(1)
]
is **false**, and in fact it fails in a quantitatively stronger way.

## Why the ( \frac{\log k}{\log\log k}+O(1)) version is false

Let (p_m) be the $m$-th prime and let
[
P_m := \prod_{j\le m} p_j
]
be the $m$-th primorial.  For a given $n$, choose $m$ so that
[
P_{m-1}< n \le P_m.
]
Now set
[
k := n - P_{m-1}.
]
Then (1\le k < P_m) and
[
n-k = P_{m-1}\quad\Longrightarrow\quad \omega(n-k)=\omega(P_{m-1})=m-1.
]

So the problem becomes: compare $m-1$ to (\frac{\log k}{\log\log k}).

Since (k<P_m), we have
[
\log k \le \log P_m = \vartheta(p_m),
]
where (\vartheta(x)=\sum_{p\le x}\log p) is Chebyshev’s (\vartheta)-function [[nomath]](so $\vartheta(p_m)=\log P_m$)[[/nomath]]. ([nntdm.net][2])

A standard explicit estimate (one convenient form is Lemma 2.1 in Ghosh) gives, for large $m$,
[
\frac{\vartheta(p_m)}{m} \le \log m+\log\log m -1 + O!\left(\frac{\log\log m}{\log m}\right).
([nntdm.net][2])
Equivalently,
[
\log P_m = \vartheta(p_m) \le m\Big(\log m+\log\log m -1 + o(1)\Big).
]

Also,
[
\log\log k \le \log\log P_m = \log\vartheta(p_m) = \log m + \log\log m + o(1).
]

Putting these together,
[
\frac{\log k}{\log\log k}
\le
\frac{\log P_m}{\log\log P_m}
\le
m\cdot\frac{\log m+\log\log m -1 + o(1)}{\log m+\log\log m + o(1)}
==================================================================

m - (1+o(1))\frac{m}{\log m+\log\log m}.
]
Therefore,
[
\omega(n-k) - \frac{\log k}{\log\log k}
\ge
(m-1) - \left(m - (1+o(1))\frac{m}{\log m+\log\log m}\right)
============================================================

(1+o(1))\frac{m}{\log m+\log\log m} - 1,
]
which (\to\infty) as (m\to\infty). In particular, for any fixed constant $C$, for all sufficiently large $n$ this construction produces some (k<n) with
[
\omega(n-k) \ge \frac{\log k}{\log\log k} + C.
]
So an additive $O(1)$ cannot be correct.

Moreover, since (m\sim \frac{\log k}{\log\log k}), one gets the more precise growth
[
\omega(n-k)
\ge
\frac{\log k}{\log\log k} + c,\frac{\log k}{(\log\log k)^2}
]
for some absolute (c>0) (as noted in the discussion of the same problem). ([Erdős Problems][1])
This is exactly the sense in which the (+O(1)) strengthening fails.

## What this says about the ((1+\varepsilon)) question

The primorial obstruction above only forces an *additive* gap of size (\asymp \frac{\log k}{(\log\log k)^2}), i.e. a *relative* gap of order (1+O(1/\log\log k)). That does **not** contradict the possibility that, for each fixed (\varepsilon>0), one can find infinitely many $n$ for which
[
\omega(n-k) < (1+\varepsilon)\frac{\log k}{\log\log k}
]
holds for all sufficiently large (k<n). And indeed, that ((1+\varepsilon))-version is exactly the part currently listed as open. ([Erdős Problems][1])

If you want, I can also rephrase the primorial argument as: “for every large $n$ there is a *forced* $k$ (coming from the preceding primorial) where (\omega(n-k)) is slightly larger than (\frac{\log k}{\log\log k}) by about (\frac{\log k}{(\log\log k)^2}), so any improvement beyond a ((1+o(1))) factor can’t be hoped for in that direction.”

[1]: https://www.erdosproblems.com/forum/thread/679 "https://www.erdosproblems.com/forum/thread/679"
[2]: https://nntdm.net/papers/nntdm-25/NNTDM-25-4-001-007.pdf "An asymptotic formula for the Chebyshev theta function"

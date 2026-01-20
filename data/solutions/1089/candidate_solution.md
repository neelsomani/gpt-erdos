Write
[
m_k(d):=\max\\{|X|:\ X\subset\mathbb R^d,\ \bigl|{|x-y|:\ x\neq y\in X}\bigr|\le k\\},
]
the largest size of a $k$-distance set in (\mathbb R^d). Then by definition
[
g_d(n)=m_{n-1}(d)+1.
]

## General bounds (sharp in the leading term)

### Upper bound (Bannai–Bannai–Stanton; also Blokhuis)

A classical result of Bannai–Bannai–Stanton shows that any $k$-distance set (X\subset\mathbb R^d) satisfies
[
|X|\le \binom{d+k}{k}. \tag{UB}
]
([Springer][1])

So
[
g_d(n)=m_{n-1}(d)+1\ \le\ \binom{d+n-1}{n-1}+1.
]
([Springer][2])

### Lower bound (explicit construction)

For (k\le d+1), take all vectors in ({0,1}^{d+1}) with exactly $k$ ones. They lie in the $d$-dimensional affine hyperplane (\sum x_i=k) and determine exactly $k$ distances [[nomath]](equivalently $k+1$ possible inner products)[[/nomath]], giving a $k$-distance set of size (\binom{d+1}{k}). ([Springer][2])

Hence
[
m_k(d)\ge \binom{d+1}{k}\quad\Longrightarrow\quad
g_d(n)=m_{n-1}(d)+1\ \ge\ \binom{d+1}{n-1}+1
]
[[nomath]](for all sufficiently large $d$, and in particular for every fixed $n$ once $d\ge n-2$)[[/nomath]]. ([Springer][2])

Putting the two together:
[
\boxed{\ \binom{d+1}{n-1}+1\ \le\ g_d(n)\ \le\ \binom{d+n-1}{n-1}+1\ }. \tag{*}
]

## Asymptotics for fixed $n$ and (d\to\infty)

Let (k=n-1) be fixed. Both binomial coefficients in ((*)) have the same leading term:
[
\binom{d+1}{k}=\frac{d^k}{k!}+O(d^{k-1}),\qquad
\binom{d+k}{k}=\frac{d^k}{k!}+O(d^{k-1}).
]
Therefore
[
g_d(n)=\frac{d^{,n-1}}{(n-1)!}+O!\left(d^{,n-2}\right).
]

In particular, dividing ((*)) by (d^{n-1}) and letting (d\to\infty) gives a squeeze:
[
\frac{\binom{d+1}{n-1}}{d^{n-1}}
\ \le\ \frac{g_d(n)}{d^{n-1}}\ \le
\frac{\binom{d+n-1}{n-1}}{d^{n-1}},
]
and both endpoints tend to (\frac1{(n-1)!}). Hence the limit exists and
[
\boxed{\ \lim_{d\to\infty}\frac{g_d(n)}{d^{n-1}}=\frac1{(n-1)!}\ }.
]

## Small $n$ sanity checks

* $n=2$: (g_d(2)=d+2) [[nomath]](since the largest equidistant set in $\mathbb R^d$ has $d+1$ points)[[/nomath]], so (g_d(2)/d\to 1=1/1!).
* $n=3$: $(*)$ gives (\binom{d+1}{2}+1\le g_d(3)\le\binom{d+2}{2}+1), so (g_d(3)\sim \tfrac12 d^2), matching the limit $1/2!$.

If you want, I can also summarize what’s known (and not known) about the *exact* values of (m_k(d)) for small $k$ (e.g. (k=2,3)), where classification results exist in low dimensions, versus the general case where only bounds like $(*)$ are available.

[1]: https://link.springer.com/article/10.1007/BF02579288 "An upper bound for the cardinality of ans-distance subset in real euclidean space, II | Combinatorica | Springer Nature Link"
[2]: https://link.springer.com/article/10.1007/s00454-023-00489-x "https://link.springer.com/article/10.1007/s00454-023-00489-x"

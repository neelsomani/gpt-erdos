Let

[
M(N):=\max\\{|A|:\ A\subseteq{1,\dots,N}\ \text{and}\ \exists,\delta:A\to{\pm1}\ \text{with}\
\sum_{n\in A}\frac{\delta_n}{n}=0,
\ \sum_{n\in A'}\frac{\delta_n}{n}\neq 0\ \forall,\varnothing\neq A'\subsetneq A\\}.
]

At present, the exact growth of $M(N)$ is **not known**; this is Erdős problem #319. ([Erdős Problems][1])

## Best known lower bound [[nomath]](linear in $N$)[[/nomath]]

A result of Croot implies that for large $N$ there exists a set
[
B\subseteq \bigl[(1/e-o(1))N,\ N\bigr]
\quad\text{with}\quad
\sum_{b\in B}\frac1b=1,
]
and necessarily (|B|\ge (1-1/e+o(1))N) because the interval has ((1-1/e)N+o(N)) integers and all terms are (\asymp 1/N). ([Erdős Problems][1])

From such a $B$, define
[
A := B\cup{1},\qquad \delta_1=-1,\ \delta_b=+1\ (b\in B).
]
Then
[
\sum_{n\in A}\frac{\delta_n}{n}=-1+\sum_{b\in B}\frac1b=-1+1=0.
]
And it is automatically **minimal** in your sense:

* If (A') does **not** contain $1$, then (\sum_{n\in A'}\delta_n/n>0).
* If (A') **does** contain $1$ but is a *proper* subset of $A$, then it omits at least one (b\in B), so
  [
  \sum_{n\in A'}\frac{\delta_n}{n}=-1+\sum_{b\in A'\cap B}\frac1b
  <-1+\sum_{b\in B}\frac1b=0.
  ]

So no nonempty proper subcollection can sum to $0$.

This gives
[
M(N)\ \ge\ |A|=|B|+1\ =\ (1-1/e+o(1)),N.
]
([Erdős Problems][1])

## A simple general upper bound

For every (N\ge 2), one always has
[
M(N)\le N-1.
]

Reason: let (2^k) be the largest power of $2$ with (2^k\le N). I claim **no** valid $A$ can contain (2^k). Indeed, suppose (2^k\in A) and let (L=\mathrm{lcm}(A)). Multiplying the zero-sum identity by $L$ gives an integer relation
[
\sum_{n\in A}\delta_n,\frac{L}{n}=0.
]
Now (L/2^k) is **odd** [[nomath]](because $2^k$ contributes the full 2-adic factor to $L$)[[/nomath]], while for every other (n\in A) we have $L/n$ **even** [[nomath]](since no other $n\le N$ is divisible by $2^k$)[[/nomath]]. Reducing mod $2$ leaves
[
\delta_{2^k}\cdot 1 \equiv 0 \pmod 2,
]
impossible because (\delta_{2^k}\in{\pm1}\equiv 1\pmod 2). Hence (2^k\notin A), so (|A|\le N-1).

## What’s actually known overall

Putting the two together, the best currently available general bounds are

[
(1-1/e+o(1)),N \ \le\ M(N)\ \le\ N-1\qquad (N\to\infty).
]

Determining the true asymptotic behaviour [[nomath]](in particular, whether the constant $1-1/e$ is optimal, or whether $M(N)$ can be much closer to $N$)[[/nomath]] is **open**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/319 "https://www.erdosproblems.com/319"

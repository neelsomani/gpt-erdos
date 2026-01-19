Let
[
a_k(t):=(-1)^{\epsilon_k(t)}\in{\pm1},\qquad P_n(x):=\sum_{k=1}^n a_k(t),x^k,
\qquad M_n(t)=\sup_{x\in[-1,1]}|P_n(x)|.
]
For Lebesgue-a.e. (t\in(0,1)), the bits (\epsilon_k(t)) are i.i.d. Bernoulli($1/2$), hence ((a_k(t))) are i.i.d. Rademacher [[nomath]]($\pm1$ with prob. $1/2$)[[/nomath]]. (We ignore the dyadic rationals, a null set, where the binary expansion is not unique.)

## Step 1: Reduce the supremum over $x$ to random-walk partial sums

Define the partial sums
[
A_m:=\sum_{k=1}^m a_k(t),\qquad m\le n.
]

**Abel/partial summation** gives, for (x\in[0,1]),
[
\sum_{k=1}^n a_k x^k
= A_n x^n+\sum_{m=1}^{n-1} A_m,(x^m-x^{m+1}).
]
Since (x^m-x^{m+1}=x^m(1-x)\ge 0) on $[0,1]$,
[
\Big|\sum_{k=1}^n a_k x^k\Big|
\le \Big(\max_{1\le m\le n}|A_m|\Big)\Big(x^n+\sum_{m=1}^{n-1}(x^m-x^{m+1})\Big)
= x\max_{m\le n}|A_m|
\le \max_{m\le n}|A_m|.
]
So for (x\in[0,1]),
[
\sup_{x\in[0,1]}|P_n(x)|\le \max_{m\le n}|A_m|.
]

For (x\in[-1,0]), write (x=-y) with (y\in[0,1]) and set (b_k:=a_k(-1)^k) and
[
B_m:=\sum_{k=1}^m b_k=\sum_{k=1}^m a_k(-1)^k.
]
Then
[
P_n(x)=\sum_{k=1}^n a_k(-y)^k=\sum_{k=1}^n b_k,y^k,
]
and the same Abel argument yields
[
\sup_{x\in[-1,0]}|P_n(x)|\le \max_{m\le n}|B_m|.
]

Putting both halves together,
[
M_n(t)\le \max\\{\max_{m\le n}|A_m|,\ \max_{m\le n}|B_m|\\}.
]

On the other hand, evaluating at the endpoints gives the lower bound
[
M_n(t)\ge \max{|P_n(1)|,\ |P_n(-1)|}
=\max{|A_n|,\ |B_n|}.
]

So we have the clean sandwich:
[
\boxed{\ \max{|A_n|,|B_n|}\ \le\ M_n(t)\ \le\ \max\\{\max_{m\le n}|A_m|,\ \max_{m\le n}|B_m|\\}\ } \tag{★}
]

## Step 2: Apply the law of the iterated logarithm

For a.e. $t$, ((a_k)) are i.i.d. Rademacher, so (A_m) is a simple symmetric random walk. Also ((b_k)=(a_k(-1)^k)) is again i.i.d. Rademacher [[nomath]](multiplying by $(-1)^k$ is deterministic)[[/nomath]], hence (B_m) is another simple symmetric random walk.

Kolmogorov’s law of the iterated logarithm (LIL) says
[
\limsup_{n\to\infty}\frac{|A_n|}{\sqrt{2n\log\log n}}=1
\quad\text{a.s.},
\qquad
\limsup_{n\to\infty}\frac{|B_n|}{\sqrt{2n\log\log n}}=1
\quad\text{a.s.}
]
Moreover, since (m\mapsto m\log\log m) is eventually increasing, the same envelope controls the running maxima:
[
\limsup_{n\to\infty}\frac{\max_{m\le n}|A_m|}{\sqrt{2n\log\log n}}=1,
\qquad
\limsup_{n\to\infty}\frac{\max_{m\le n}|B_m|}{\sqrt{2n\log\log n}}=1
\quad\text{a.s.}
]
Taking the max of the two does not change the limsup constant [[nomath]](still $1$)[[/nomath]].

Now combine with the sandwich (★): the lower bound gives limsup (\ge 1) [[nomath]](already from $x=1$)[[/nomath]], and the upper bound gives limsup (\le 1). Hence:

[
\boxed{\ \text{For Lebesgue-a.e. }t,\quad
\limsup_{n\to\infty}\frac{M_n(t)}{\sqrt{2n\log\log n}}=1.\ }
]

## Final “order of magnitude” statement

So the correct almost-sure growth scale is
[
\boxed{\ M_n(t)\ \text{is of order}\ \sqrt{n\log\log n}\ \text{(a.s., in the LIL/limsup sense)}. }
]

Equivalently: for a.e. $t$,

* (M_n(t)=O\big(\sqrt{n\log\log n}\big)) as (n\to\infty), and
* (M_n(t)\ge (1-o(1))\sqrt{2n\log\log n}) infinitely often.

[[nomath]](If you care about “typical size for a fixed $n$” rather than limsup along $n$, then $M_n(t)$ is usually $\asymp \sqrt n$; the $\sqrt{\log\log n}$ factor reflects the rare peaks along the sequence $n$, exactly as for a simple random walk.)[[/nomath]]

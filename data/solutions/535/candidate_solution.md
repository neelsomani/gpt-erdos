Write (A\subseteq{1,\dots,N}).
A set of $r$ distinct integers ({a_1,\dots,a_r}\subset A) has **all pairwise gcd’s equal** iff there is some (d\ge1) such that
[
\gcd(a_i,a_j)=d\quad(\forall i\ne j).
]
Equivalently,
[
a_i=d,b_i\quad\text{and}\quad \gcd(b_i,b_j)=1\ \ (\forall i\ne j),
]
i.e. after factoring out the common gcd $d$, the quotients are pairwise coprime.

So (f_r(N)) is the maximum (|A|) such that **for every $d$**, among the multiples of $d$ in $A$, you cannot find $r$ elements whose quotients are pairwise coprime.

## Known upper bounds

Erdős showed
[
f_r(N)\le N^{3/4+o(1)},
]
and Abbott–Hanson improved the exponent to $1/2$: for each fixed (r\ge3),
[
f_r(N)\le N^{1/2+o(1)}.
]
([Erdős Problems][1])

(These bounds are the best general published ones recorded in the standard references for this problem.)

## A general lower bound (explicit construction)

There is a simple construction giving a “subpower” lower bound for every fixed (r\ge3).

Let $m$ be a parameter (to be chosen), and take $m(r-1)$ distinct primes, grouped into $m$ blocks of size $r-1$:
[
B_i={q_{i,1},q_{i,2},\dots,q_{i,r-1}}\qquad (i=1,\dots,m).
]
Now form the family
[
A=\\{\ \prod_{i=1}^m q_{i,\sigma(i)}\ :\ \sigma:{1,\dots,m}\to{1,\dots,r-1}\\}.
]
So each element of $A$ picks **exactly one prime from each block**, and (|A|=(r-1)^m).

**Claim:** no $r$ distinct elements of $A$ have all pairwise gcd equal.

*Proof sketch.* Take $r$ distinct products (x_1,\dots,x_r\in A). Fix a block (B_i). Among the $r$ chosen primes from (B_i) [[nomath]](one per $x_j$)[[/nomath]], by pigeonhole two of the (x_j)’s chose the same prime [[nomath]](since there are only $r-1$ primes in the block)[[/nomath]]. Hence that prime divides (\gcd(x_j,x_{j'})) for some pair (j\ne j').
If all pairwise gcd’s were equal to some $d$, then that prime would have to divide **every** pairwise gcd, hence it would have to appear in **every** (x_t), forcing all $r$ choices in block (B_i) to be identical. Doing this for every block forces (x_1=\cdots=x_r), contradiction. (\square)

Now choose $m$ as large as possible while keeping all these products (\le N). If we take the primes in increasing order, standard prime-number estimates imply the largest product behaves like
[
\exp!\bigl((1+o(1)),m\log m\bigr),
]
so we can take
[
m=(1+o(1))\frac{\log N}{\log\log N}.
]
Then
[
|A|=(r-1)^m
=\exp!\left(m\log(r-1)\right)
= N^{\frac{\log(r-1)+o(1)}{\log\log N}}.
]
So for each fixed (r\ge3),
[
f_r(N)\ \ge\ N^{\frac{\log(r-1)+o(1)}{\log\log N}}.
]

In particular for $r=3$, this gives (f_3(N)\ge N^{(\log 2+o(1))/\log\log N}), which is of the same *shape* as Erdős’s classical lower bound (f_3(N) > N^{c/\log\log N}) for some (c>0). ([Erdős Problems][1])

## Summary of the best general “estimate” currently known

For each fixed (r\ge3),
[
N^{\frac{\log(r-1)+o(1)}{\log\log N}}
\ \le\
f_r(N)
\ \le\
N^{1/2+o(1)}.
]

For $r=3$, Erdős conjectured that the true order of growth is **subpower**, of the form (N^{C/\log\log N}) (matching the lower bound up to the constant in the numerator). ([Erdős Problems][1])

The gap between the known upper bound (N^{1/2+o(1)}) and the conjectured subpower growth is open, and is closely related (in Erdős’s formulation) to sunflower/(\Delta)-system phenomena. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/535 "https://www.erdosproblems.com/forum/thread/535"

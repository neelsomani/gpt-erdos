Take an $n$-point set (P\subset\mathbb R^2) in **general position** (no three collinear). A “convex subset” here means a subset (Q\subseteq P) whose points are in **convex position** [[nomath]](equivalently: $Q$ is convexly independent; every point of $Q$ is a vertex of $\operatorname{conv}(Q)$)[[/nomath]]. This is the same as counting convex $k$-gons with vertices in $P$, over all (k\ge 3) (plus the trivial small subsets, which are negligible asymptotically). This is the Erdős–Hammer question. ([Erdős Problems][1])

Let
[
F(P):=|\\{Q\subseteq P:\ Q\text{ is in convex position}\\}|,
\qquad
f(n):=\min_{|P|=n}F(P).
]

## What is known about $f(n)$

Erdős proved that $f(n)$ is **quasi-polynomial**, more precisely
[
f(n)=\exp(\Theta((\log n)^2)),
]
and this order of magnitude is **best possible**. ([Pure][2])

Equivalently, there exist constants (c_1,c_2>0) such that
[
n^{c_1\log n} < f(n) < n^{c_2\log n}.
]
([Erdős Problems][1])

So (\log f(n)) really is (\Theta((\log n)^2)).

## Quantitative bounds on the constant in the ((\log n)^2) exponent

Most of the literature (and the sources above) use base‑2 logarithms; I’ll do the same. (Changing the log base just multiplies the constant by a fixed factor.)

### Upper bound (construction)

From the Erdős–Szekeres lower bound $ES(k)\ge 2^{k-2}+1$, there are $n$-point sets with **no** convex subset larger than (\approx \log_2 n). ([Pure][2])
For such a set, every convex subset has size (\le t) with (t=\log_2 n+O(1)), hence
[
f(n)\ \le\ \sum_{i\le t}\binom ni\ =\ 2^{(1+o(1))(\log_2 n)^2}.
]
So
[
\limsup_{n\to\infty}\frac{\log_2 f(n)}{(\log_2 n)^2}\ \le\ 1.
]

### Lower bound (Erdős’s counting + modern Erdős–Szekeres)

A standard “supersaturation via double counting” argument used by Erdős gives a general lower bound in terms of how large a convex subset is forced inside medium-size subconfigurations.

Using the current best asymptotic Erdős–Szekeres upper bound (Suk), every set of $m$ points in general position contains ((1-o(1))\log_2 m) points in convex position. ([Pure][2])
Let (m=\lfloor\sqrt n\rfloor), and let
[
k=(1-o(1))\log_2 m=(\tfrac12-o(1))\log_2 n.
]
Every $m$-subset of $P$ contains a convex $k$-subset [[nomath]](take any $k$ points from a larger convexly independent subset if needed)[[/nomath]]. Now count:

* there are (\binom{n}{m}) $m$-subsets;
* each fixed $k$-subset is contained in at most (\binom{n-k}{m-k}) $m$-subsets.

So the number of **distinct** convex $k$-subsets is at least
[
\frac{\binom{n}{m}}{\binom{n-k}{m-k}}
=\prod_{i=0}^{k-1}\frac{n-i}{m-i}
\ \ge\ \left(\frac{n}{m}\right)^k
\ =\ (\sqrt n)^{,k}.
]
Taking (\log_2) gives
[
\log_2 f(n)\ \ge\ \left(\tfrac14-o(1)\right)(\log_2 n)^2,
]
i.e.
[
f(n)\ \ge\ 2^{(\frac14-o(1))(\log_2 n)^2}.
]

### Summary of current explicit asymptotics

Putting both together, one gets
[
2^{(\frac14-o(1))(\log_2 n)^2}
\ \le\
f(n)
\ \le\
2^{(1+o(1))(\log_2 n)^2}.
]
Equivalently,
[
\frac14\ \le\ \liminf_{n\to\infty}\frac{\log_2 f(n)}{(\log_2 n)^2}
\ \le\
\limsup_{n\to\infty}\frac{\log_2 f(n)}{(\log_2 n)^2}
\ \le\ 1.
]

## Does the limit constant $c$ exist?

This is **open**. Erdős already explicitly speculated about existence of
(\lim \frac{\log f(n)}{(\log n)^2}), and the Erdős Problems site lists it as open. ([Department of Applied Mathematics][3])

So the best current picture is:

* growth rate is pinned down to (\exp(\Theta((\log n)^2))), but
* the **leading constant** in front of ((\log n)^2) (and even whether it converges) is unknown.

[1]: https://www.erdosproblems.com/latex/838 "https://www.erdosproblems.com/latex/838"
[2]: https://pure.tue.nl/ws/files/290869770/morin_decarufel_numbered.pdf "https://pure.tue.nl/ws/files/290869770/morin_decarufel_numbered.pdf"
[3]: https://kam.mff.cuni.cz/~chvatal/MorSol00.pdf "https://kam.mff.cuni.cz/~chvatal/MorSol00.pdf"

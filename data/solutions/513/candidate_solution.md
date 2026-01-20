This is **not known exactly**: it’s an open problem of Erdős (Erdős Problem **#513**). ([Erdős Problems][1])

If we write
[
\mu(r):=\max_n |a_n|r^n,\qquad M(r):=\max_{|z|=r}|f(z)|,
]
the question asks for the supremum [[nomath]](over all transcendental entire $f$)[[/nomath]] of
[
\liminf_{r\to\infty}\frac{\mu(r)}{M(r)}.
]

## What is known

From the current literature summary (as of Dec 28, 2025), the exact supremum is unknown, but it is known that ([Erdős Problems][1])

* it is **at least $1/2$** (a “trivial” lower bound),
* in fact it is **strictly greater than $1/2$** (Kővári, unpublished),
* and Clunie–Hayman proved an **upper bound**
  [
  \sup \le \frac{2}{\pi}-c
  \quad\text{for some absolute }c>0,
  ]
  so in particular the supremum is **strictly less than** (2/\pi\approx 0.63662). ([Erdős Problems][1])

So, letting $S$ denote the “greatest possible value” asked for,
[
\boxed{;\frac12 < S \le \frac{2}{\pi}-c < \frac{2}{\pi}\approx 0.63662;}
]
with the exact value of $S$ still open. ([Erdős Problems][1])

## Why $1/2$ is a (constructible) lower bound

Here is a concrete construction giving (\liminf = \tfrac12), which shows (S\ge \tfrac12).

Take a very lacunary entire series with positive coefficients, e.g.
[
f(z)=\sum_{k=0}^\infty e^{-4^k}z^{2^k}
\qquad(\text{so }a_{2^k}=e^{-4^k}\ a_n=0\text{ otherwise}).
]
This is entire because for each fixed $r$,
[
|a_{2^k}|r^{2^k}=\exp(-4^k+2^k\log r)\to 0\quad(k\to\infty).
]

Let (n_k=2^k) and choose radii (r_k) so that the $k$-th and ((k+1))-st terms have equal size:
[
e^{-n_k^2}r_k^{n_k}=e^{-n_{k+1}^2}r_k^{n_{k+1}}
\quad\Longrightarrow\quad
\log r_k=n_k+n_{k+1},
]
so (r_k=\exp(n_k+n_{k+1})=\exp(3\cdot 2^k)).

At (r=r_k),

* the $k$-th and ((k+1))-st terms are equal and dominate the rest [[nomath]](because the exponents $2^k$ grow so fast)[[/nomath]], hence
  [
  \mu(r_k)=|a_{n_k}|r_k^{n_k}=|a_{n_{k+1}}|r_k^{n_{k+1}},
  ]
  and all other terms are (o(\mu(r_k))).
* Since all coefficients are nonnegative, the maximum modulus on (|z|=r_k) is attained at (z=r_k>0), so
  [
  M(r_k)=f(r_k)=2\mu(r_k)+o(\mu(r_k)).
  ]

Therefore
[
\frac{\mu(r_k)}{M(r_k)}\to \frac12,
]
and between these transition radii the series is essentially dominated by a single term, so the ratio stays (\ge \tfrac12-o(1)). Thus this $f$ has
[
\liminf_{r\to\infty}\frac{\mu(r)}{M(r)}=\frac12.
]

This yields the “trivial” lower bound (S\ge \tfrac12) mentioned on the problem page. ([Erdős Problems][1])

## A simple (not best-known) universal upper bound: (S\le 1/\sqrt2)

Here’s an elementary upper bound that holds for every transcendental entire $f$:

Using Parseval on the circle (|z|=r),
[
\frac{1}{2\pi}\int_0^{2\pi}\bigl|f(re^{i\theta})\bigr|^2,d\theta
=\sum_{n=0}^\infty |a_n|^2r^{2n}.
]
Hence (M(r)^2\ge \sum |a_n|^2r^{2n}).

Now, for transcendental $f$, the index $n$ achieving (\mu(r)=\max_n |a_n|r^n) must change infinitely often as (r\to\infty); at each change radius there are at least two indices (n\neq m) with (|a_n|r^n=|a_m|r^m=\mu(r)). For such radii,
[
\sum |a_k|^2r^{2k}\ge |a_n|^2r^{2n}+|a_m|^2r^{2m}=2\mu(r)^2,
]
so (M(r)\ge \sqrt2,\mu(r)) along an unbounded sequence of $r$. This forces
[
\liminf_{r\to\infty}\frac{\mu(r)}{M(r)}\le \frac1{\sqrt2}.
]
So (S\le 1/\sqrt2\approx 0.707). [[nomath]](This is weaker than the best known $<2/\pi$ bound.)[[/nomath]]

## Bottom line

The **exact** “greatest possible value” is **unknown** (open Erdős problem #513). The best succinct summary currently is: ([Erdős Problems][1])

[
\boxed{;\frac12 < \sup_f \liminf_{r\to\infty}\frac{\max_n|a_nr^n|}{\max_{|z|=r}|f(z)|}
\ \le\ \frac{2}{\pi}-c
\ <\ \frac{2}{\pi}\approx 0.63662;}
]
for some absolute (c>0). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/513 "

    Erdős Problem #513 - Discussion thread

"

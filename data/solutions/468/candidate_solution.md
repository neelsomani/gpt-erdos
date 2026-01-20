Let
$
1<d_1<d_2<\cdots<d_{k_n}
$
be the divisors of $n$ larger than $1$, and
$
D_n={d_1,\ d_1+d_2,\ \ldots,\ d_1+\cdots+d_{k_n}}.
$

## 1) (\bigl|D_n\setminus\bigcup_{m<n}D_m\bigr|)

If you define
$
a(n)\ :=\ |D_n\setminus\bigcup_{m<n}D_m|,
$
then this is exactly the “number of debut sums” sequence **OEIS A387502**. ([OEIS][1])

The OEIS entry gives:

* the definition in exactly your language ([OEIS][1])
* initial values
  [
  a(1),a(2),a(3),\ldots = 0,1,1,1,1,1,1,1,1,1,0,3,1,1,1,1,0,2,\ldots
  ]
  ([OEIS][1])
* examples [[nomath]](e.g. $a(12)=3$ because $D_{12}={2,5,9,15,27}$ and $9,15,27$ are new)[[/nomath]] ([OEIS][1])
* computational/observational facts like record indices (2,12,36,144,336,1320,1980,5040,8400,25200,75600,\dots) ([OEIS][1])
* the observed average of the first (100000) terms: about (0.8349). ([OEIS][1])

So at present the “best answer” is: **this size is the value of A387502 at $n$**, and the deeper asymptotic understanding of this sequence is part of an Erdős–Graham problem. ([OEIS][1])

[[nomath]](Conceptually: $a(n)$ counts how many integers $N$ have *minimal* witness $n$; i.e. how many $N$ satisfy $f(N)=n$.)[[/nomath]]

## 2) The minimal witness $f(N)$ and whether (f(N)=o(N))

Let $f(N)$ be the least $n$ with (N\in D_n).

### Relation to an OEIS “minimal $m$” sequence

A closely related “minimal $m$” function is **OEIS A167485**, defined as the smallest $m$ such that $n$ is a partial sum of the (increasing) divisor list of $m$ [[nomath]](that OEIS version includes the divisor $1$)[[/nomath]]. ([OEIS][2])

Because your (D_n) excludes $1$, you can translate between them by a shift:

* if (A167485(n)=) least $m$ such that $n$ is a partial sum including $1$,
* then your $f(N)$ corresponds to that quantity at (n=N+1) (the OEIS entry for A387502 explicitly notes an index shift relationship). ([OEIS][1])

### A basic unconditional fact: (\liminf f(N)/N=0)

From A167485’s comments: (a(\sigma(n))\le n) [[nomath]](here $\sigma=A000203$)[[/nomath]], and (\sigma(n)/n) is unbounded, so (\liminf a(n)/n=0). Translated to your normalization, this gives (\liminf f(N)/N=0) along a subsequence. ([OEIS][2])

### But the key point: (f(N)=o(N)) is **false**, even “for almost all $N$”

This has been addressed quite recently in the Erdős Problems forum. In particular:

* Erdős Problem #1054 [[nomath]](which is exactly the “is $f(n)=o(n)$?” question in Guy’s book)[[/nomath]] states that **Tao disproved the strong claim (f(n)=o(n))** and that he proved an **upper density bound**
  [
  \overline{d}\bigl({n: f(n)\le \delta n}\bigr)\ \ll\ \delta^2.
  ]
  ([Erdős Problems][3])

* The detailed argument is in Tao’s comment on the discussion thread for the closely related Erdős Problem #468. ([Erdős Problems][4])

What this means in plain terms:

* Fix a small (\delta>0). Then **only $O(\delta^2)$** of the integers $N$ (in upper density) satisfy (f(N)\le \delta N). ([Erdős Problems][3])
* In particular, (f(N)/N\to 0) **cannot** hold on a density‑$1$ set [[nomath]](“almost all $N$”)[[/nomath]], because the set where (f(N)/N\le\delta) actually has density (\ll \delta^2), which is small when (\delta) is small. ([Erdős Problems][3])

Very briefly, the mechanism of Tao’s proof is:

* encode “partial sums of divisors” using (\sigma_k(n)), the sum of divisors of $n$ with the $k$ largest divisors removed [[nomath]](partial sums correspond to $\sigma_k(n)$ for various $k$)[[/nomath]]; ([Erdős Problems][4])
* prove a uniform averaged bound (\sum_{n\le x}\sigma_k(n)\ll x^2/k^{1.1}); ([Erdős Problems][4])
* sum over $k$ [[nomath]](since $k$ is not fixed in the definition of $f$)[[/nomath]] to get strong control on how many large targets can be hit by small $n$, leading to the (\ll \delta^2) density bound. ([Erdős Problems][4])

## What remains open

Even after this, there are still interesting open directions (and the Erdős Problems pages are still marked open): e.g. the size/growth behavior of the debut-count sequence $a(n)$, and questions about how large (\limsup f(N)/N) can be. ([OEIS][1])

[1]: https://oeis.org/A387502 "A387502 - OEIS"
[2]: https://oeis.org/A167485 "A167485 - OEIS"
[3]: https://www.erdosproblems.com/1054 "
  
    Erdős Problem #1054
  
"
[4]: https://www.erdosproblems.com/forum/thread/468 "

    Erdős Problem #468 - Discussion thread

"

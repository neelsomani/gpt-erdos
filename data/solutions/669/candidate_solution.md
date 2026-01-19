Let (P\subset \mathbb R^2) with (|P|=n).  Write
[
t_j(P):=|\\{\text{lines }\ell:\ |\ell\cap P|=j\\}|,\qquad
T_k(P):=|\\{\text{lines }\ell:\ |\ell\cap P|\ge k\\}|=\sum_{j\ge k} t_j(P).
]
Then your extremal functions are
[
f_k(n)=\max_{|P|=n} t_k(P),\qquad F_k(n)=\max_{|P|=n} T_k(P)=\max_{|P|=n}\sum_{j\ge k} t_j(P).
]

## 1) A universal “pair-counting” upper bound

Every unordered pair of points determines a unique line, so
[
\sum_{j\ge 2} t_j(P)\binom{j}{2}=\binom{n}{2}.
]
In particular, for (k\ge 2),
[
T_k(P)\binom{k}{2}\ \le\ \sum_{j\ge k} t_j(P)\binom{j}{2}\ \le\ \binom{n}{2},
]
hence
[
F_k(n)\le \frac{\binom{n}{2}}{\binom{k}{2}}=\frac{n(n-1)}{k(k-1)}.
]
The same inequality holds for (f_k(n)) since (f_k(n)\le F_k(n)).

So, for every fixed $k$,
[
\limsup_{n\to\infty}\frac{F_k(n)}{n^2}\le \frac{1}{k(k-1)},\qquad
\limsup_{n\to\infty}\frac{f_k(n)}{n^2}\le \frac{1}{k(k-1)}.
]

## 2) Szemerédi–Trotter gives the correct order (n^2/k^3) (up to constants)

A much stronger bound for “$k$-rich” lines comes from the Szemerédi–Trotter incidence theorem. A standard corollary (often stated as “Theorem 3” in expositions) is:

> For $n$ points in the plane and (2\le k\le \sqrt n), the number of lines containing at least $k$ points is (\ll n^2/k^3) (absolute implied constant). 

So
[
F_k(n)\ \ll\ \frac{n^2}{k^3}\qquad (2\le k\le \sqrt n),
]
and also (via the same derivation) one has the more uniform form
[
F_k(n)\ \ll\ \frac{n^2}{k^3}+\frac{n}{k}.
]
[[nomath]](And trivially $f_k(n)\le F_k(n)$.)[[/nomath]]

Moreover, this (n^2/k^3) order is *tight up to constants* for (2\le k\le \sqrt n) using grid-type constructions [[nomath]](“$\sqrt n\times \sqrt n$” lattice)[[/nomath]], as explicitly noted in the same source. 

So for a wide range of parameters one has the *right scale*
[
F_k(n)=\Theta\left(\frac{n^2}{k^3}+\frac{n}{k}\right)\quad\text{(up to absolute constants),}
]
and similarly [[nomath]](allowing extra lines with $\ge k$ points does not hurt)[[/nomath]] there are also constructions giving
[
f_k(n)\ \gg\ \frac{n^2}{k^3}
]
for fixed $k$ (Croft–Erdős-type constructions; see below). ([Wikipedia][1])

## 3) Exact asymptotics for $k=2$ and $k=3$

### $k=2$

If no three points are collinear, every pair gives a distinct line with exactly 2 points. Thus
[
f_2(n)=F_2(n)=\binom{n}{2},
]
so
[
\lim_{n\to\infty}\frac{F_2(n)}{n^2}=\lim_{n\to\infty}\frac{f_2(n)}{n^2}=\frac12.
]

### $k=3$  (the Orchard-planting problem)

For $k=3$, the extremal problem is the classic orchard-planting problem. Green–Tao proved that for all sufficiently large $n$, the maximum number of 3-point lines is
[
f_3(n)=\frac{n(n-3)}{6}+1\quad\text{(for (n) large enough).} ([Wikipedia][1])
]
In extremal configurations there are no 4 collinear points, so “(\ge3)” and “(=3)” coincide asymptotically, hence also
[
F_3(n)\sim f_3(n)\sim \frac{n^2}{6}.
]
Therefore,
[
\boxed{\ \lim_{n\to\infty}\frac{F_3(n)}{n^2}=\lim_{n\to\infty}\frac{f_3(n)}{n^2}=\frac16\ }.
]

## 4) What is known (and unknown) for (k\ge 4)

### Order of magnitude

For every fixed (k\ge 4), combining:

* the Szemerédi–Trotter upper bound (F_k(n)\ll n^2/k^3), 
* and standard grid/lattice constructions showing tightness up to constants, 
  one gets
  [
  F_k(n)=\Theta\left(\frac{n^2}{k^3}\right)\quad\text{(for fixed (k), up to constants),}
  ]
  and similarly
  [
  f_k(n)=\Theta\left(\frac{n^2}{k^3}\right)\quad\text{(for fixed (k), up to constants),}
  ]
  because the known constructions can be arranged to produce (\gg n^2/k^3) lines containing **exactly** $k$ points [[nomath]](Croft–Erdős style; the construction may include some longer lines with $>k$ points)[[/nomath]]. ([Wikipedia][1])

### The constants (your requested limits)

Define (if the limits exist)
[
c_k:=\lim_{n\to\infty}\frac{f_k(n)}{n^2},\qquad C_k:=\lim_{n\to\infty}\frac{F_k(n)}{n^2}.
]
Erdős explicitly formulated (c_k) in this way [[nomath]](for the “exactly $k$” problem)[[/nomath]] and noted that:

* (c_2=\tfrac12), (c_3=\tfrac16),
* beyond that, the exact values were not determined; Szemerédi–Trotter gives a bound on the scale (1/k^3) [[nomath]](up to polylog factors in $k$ in some formulations)[[/nomath]]. 

As far as standard references indicate, for (k\ge 4) the **exact constants are not known**. What *is* known unconditionally is that there are positive absolute constants (0<a\le b<\infty) such that for all fixed $k$ and large $n$,
[
\frac{a}{k^3}\ \lesssim\ \frac{f_k(n)}{n^2}\ \le\ \frac{F_k(n)}{n^2}\ \lesssim\ \frac{b}{k^3},
]
together with the always-valid “pair counting” ceiling
[
\frac{F_k(n)}{n^2},\frac{f_k(n)}{n^2}\ \le\ \frac{1}{k(k-1)}.
]
The (n^2/k^3) upper bound and its tightness on grids are explicitly stated in Székely’s exposition. 

So, for (k\ge 4), the best honest answer to your “determine the limits” request is:

* (\displaystyle \lim_{n\to\infty} \frac{F_k(n)}{n^2}) and (\displaystyle \lim_{n\to\infty}\frac{f_k(n)}{n^2}) are **known exactly only for (k=2,3)**.
* For (k\ge 4), the **precise limiting constants are not known**; one has matching (up to absolute multiplicative constants) bounds of order (1/k^3) coming from Szemerédi–Trotter plus grid-type constructions, and the trivial ceiling (1/(k(k-1))). 

## Final “limit” summary

[
\boxed{\lim_{n\to\infty}\frac{F_2(n)}{n^2}=\lim_{n\to\infty}\frac{f_2(n)}{n^2}=\frac12.}
]

[
\boxed{\lim_{n\to\infty}\frac{F_3(n)}{n^2}=\lim_{n\to\infty}\frac{f_3(n)}{n^2}=\frac16.}
]

For each fixed (k\ge 4),
[
\boxed{\ \frac{f_k(n)}{n^2},\frac{F_k(n)}{n^2}\ \text{stay between positive constants }\asymp \frac{1}{k^3}\ \text{(and }\le \frac1{k(k-1)}\text{), but the exact limits are not currently determined.}\ }
]
[[nomath]](And the $n^2/k^3$ scale is the one dictated by Szemerédi–Trotter and known to be tight up to constants via grid constructions.)[[/nomath]] 

If you want, I can also spell out a concrete grid-based lower-bound count that yields an explicit absolute constant (a>0) in (f_k(n),F_k(n)\ge a,n^2/k^3), and the standard Szemerédi–Trotter derivation of (F_k(n)\ll n^2/k^3+n/k).

[1]: https://en.wikipedia.org/wiki/Orchard-planting_problem "Orchard-planting problem - Wikipedia"

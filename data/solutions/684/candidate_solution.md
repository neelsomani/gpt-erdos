Let
[
\binom{n}{k}=u(n,k),v(n,k),
]
where every prime factor of $u(n,k)$ is (\le k) and every prime factor of $v(n,k)$ is (>k). Equivalently, $u(n,k)$ is the “$k$-smooth part” of (\binom{n}{k}).

Define
[
f(n)=\min{k: u(n,k)>n^2},
]
[[nomath]](with the convention “no such $k$” for very small $n$; OEIS records this as $0$ for those $n$)[[/nomath]]. ([OEIS][1])

---

## A general explicit upper bound: (f(n)\le \lfloor n/2\rfloor) for all sufficiently large $n$

Take (k=\lfloor n/2\rfloor). Then all primes counted in $v(n,k)$ lie in $(k,n]\subset (n/2,n]$. In particular, if $p\in (n/2,n]$, then $2p>n$, so $p$ appears in $n!$ with exponent $1$, and does not appear in $k!$ or ((n-k)!). Hence each such prime can occur in (\binom{n}{k}) with exponent at most $1$, and
$
v(n,k)\ \Big|\ \prod_{n/2<p\le n} p.
$
Introduce Chebyshev’s function (\vartheta(x)=\sum_{p\le x}\log p); then
$
\prod_{n/2<p\le n} p=\exp(\vartheta(n)-\vartheta(n/2)),
$
so
$
\log v(n,k)\le \vartheta(n)-\vartheta(n/2).
$

On the other hand, the central binomial coefficient is the largest term in (\sum_{j=0}^n \binom{n}{j}=2^n), so
[
\binom{n}{\lfloor n/2\rfloor}\ge \frac{2^n}{n+1}.
]
Therefore
[
\log u(n,k)=\log \binom{n}{k}-\log v(n,k)
\ge
n\log 2-\log(n+1)-\big(\vartheta(n)-\vartheta(n/2)\big).
]

Using the Prime Number Theorem ((\vartheta(x)=x+o(x))), we have (\vartheta(n)-\vartheta(n/2)=\tfrac12n+o(n)), so
[
\log u(n,\lfloor n/2\rfloor)\ge \Big(\log 2-\tfrac12\Big)n+o(n).
]
Since (\log 2-\tfrac12\approx 0.193>0), the right-hand side grows linearly, hence eventually exceeds (2\log n). Thus, for all sufficiently large $n$,
[
u\bigl(n,\lfloor n/2\rfloor\bigr)>n^2,
]
so
[
f(n)\le \lfloor n/2\rfloor\qquad(n\ \text{large}).
]

If you want this made fully explicit [[nomath]](with a concrete “for all $n\ge N_0$”)[[/nomath]], you can combine an explicit estimate for (\vartheta(x)) [[nomath]](e.g. Dusart gives explicit error terms of the form $\vartheta(x)=x+O\left(\tfrac{x}{\log^4 x}\right)$)[[/nomath]] with the inequality above. ([Data Science][2])

So, one unconditional upper bound is:
[
f(n)=O(n)\quad\text{(indeed, }f(n)\le n/2\text{ for all large }n\text{)}.
]

## A nontrivial lower bound in the “eventual” sense: (f(n)\to\infty), but no effective growth rate is known

A theorem of Mahler on the “smooth part” of products of consecutive integers implies:

> For any fixed $k$ (and appropriate smoothness parameter), the $k$-smooth part of a product of $k$ consecutive integers is (< n^{1+\varepsilon}) for all sufficiently large $n$.

Applied in this setting, it implies that for every fixed $K$, once $n$ is large enough, **no** (k\le K) can make (u(n,k)>n^2). Equivalently,
[
f(n)\to\infty\qquad(n\to\infty),
]
but Mahler’s result is *ineffective* here, so it does **not** give an explicit function (g(n)\uparrow\infty) with (f(n)\ge g(n)), nor an explicit “(n\ge N(K))” in terms of $K$. ([Erdős Problems][3])

In fact, determining any meaningful effective lower bound [[nomath]](e.g. proving $f(n)\ge c\log n$ or even $f(n)\ge c\log\log n$ for all large $n$)[[/nomath]] is part of an Erdős problem that is currently open in general. ([Erdős Problems][3])

So the best unconditional “lower bound” currently known in general form is:
[
\forall K\ \exists N(K)\ \text{such that}\ n\ge N(K)\implies f(n)>K,
]
i.e. $f(n)$ is unbounded.

---

## Small-$n$ behavior and data

For small $n$, there may be no $k$ at all with (u>n^2) [[nomath]](OEIS records $a(n)=0$ in that case)[[/nomath]]. The same OEIS entry gives, for example, (f(21)=8) because
[
\binom{21}{8}=203490 = 630\cdot 323,\qquad 630=2\cdot 3^2\cdot 5\cdot 7>21^2.
]
([OEIS][1])

---

## Summary of what you can say unconditionally today

* **Upper bound (effective):** (f(n)\le \lfloor n/2\rfloor) for all sufficiently large $n$ [[nomath]](hence $f(n)=O(n)$)[[/nomath]]. [[nomath]](Argument via central binomial coefficient and bounding the “large-prime part” $v$ with $\vartheta(n)-\vartheta(n/2)$.)[[/nomath]] ([Data Science][2])
* **Lower bound (ineffective but asymptotic):** (f(n)\to\infty) as (n\to\infty), by Mahler’s theorem on smooth parts of products of consecutive integers; **no effective growth rate** is currently known in general. ([Erdős Problems][3])
* **Status:** Improving these to something like (f(n)\ll (\log n)^C) or giving any explicit (f(n)\gg g(n)\to\infty) is (as far as current references indicate) an open Erdős problem. ([Erdős Problems][3])

If you tell me what kind of bounds you’re aiming for [[nomath]](effective vs. asymptotic, “for all $n$” vs. “infinitely many $n$”, etc.)[[/nomath]], I can tailor the discussion—e.g., show how far the (k=\lfloor n/2\rfloor) argument can be pushed with explicit constants, or discuss what conjectural heuristics and computations suggest (OEIS A392019 is a good starting point). ([OEIS][1])

[1]: https://oeis.org/A392019 "A392019 - OEIS"
[2]: https://piyanit.nl/wp-content/uploads/2020/10/art_10.1007_s11139-016-9839-4.pdf "Explicit estimates of some functions over primes"
[3]: https://www.erdosproblems.com/684 "
  
    Erdős Problem #684
  
"

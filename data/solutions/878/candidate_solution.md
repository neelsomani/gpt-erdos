Let me rewrite the two objects in a way that makes the size questions transparent.

For a prime (p\mid n) put
$
\ell_p(n):=\bigl\lfloor \log_p n\bigr\rfloor,\qquad P_p(n):=p^{\ell_p(n)}\le n<p^{\ell_p(n)+1}.
$
Then
$
f(n)=\sum_{p\mid n}P_p(n).
$
Also, if $S$ is a set of primes, let
$
M_S(n):=\max{m\le n:\ \text{all prime factors of }m\text{ lie in }S},
$
the largest $S$-smooth integer (\le n). If $P(n)$ denotes the set of primes dividing $n$, then your $F(n)$ is exactly the “best partition” of $P(n)$:
$
F(n)=\max_{\text{partitions }P(n)=S_1\sqcup\cdots\sqcup S_r}\ \sum_{j=1}^r M_{S_j}(n);+;(|P(n)|-r),
$
because the remaining (|P(n)|-r) of the (a_i)’s can be $1$.

Two trivial but very useful inequalities are

* for each (p\mid n): (n/p < P_p(n)\le n), hence
  [
  n\sum_{p\mid n}\frac1p < f(n)\le n,\omega(n),
  ]
  where (\omega(n)=|P(n)|);
* always
  [
  f(n)\le F(n)\le n,\omega(n),\qquad F(n)\ge n+\omega(n)-1
  ]
  [[nomath]](take one $a_i=n$ and the rest $1$)[[/nomath]].

## 1) The “almost all $n$” statement for $f(n)$

This one is **true**, and in fact much stronger statements hold.

Define
$
H(x):=\sum_{n<x}\frac{f(n)}{n}.
$
If you can show (H(x)\ll x), then by Markov’s inequality you immediately get: for any fixed (\varepsilon>0),
$
|\\{n\le x:\ f(n)\ge \varepsilon,n\log\log n\\}|
\ \le\
\frac1{\varepsilon\log\log 2}\sum_{n\le x}\frac{f(n)}n
\ \ll\
\frac{x}{\log\log x},
$
so the exceptional set has density $0$. Hence
$
f(n)=o(n\log\log n)\quad\text{for almost all }n.
$

So the real work is (H(x)\ll x), which we can actually do (next section), and it also answers your last question.

## 2) An asymptotic formula for (H(x)=\sum_{n<x}f(n)/n), and the bound (H(x)\ll x\log\log\log\log x)

Start from
$
H(x)=\sum_{n<x}\ \sum_{p\mid n}\frac{P_p(n)}n.
$
Write $n=pm$. Then $P_p(pm)=p^{\ell_p(pm)}=p^{1+\ell_p(m)}=p,P_p(m))$, so
[
\frac{P_p(pm)}{pm}=\frac{P_p(m)}{m}.
]
Therefore
$
H(x)=\sum_{p<x}\ \sum_{m<x/p}\frac{P_p(m)}{m}.
$
Now define
$
S_p(y):=\sum_{m<y}\frac{p^{\lfloor \log_p m\rfloor}}{m}.
$
Then
$
H(x)=\sum_{p<x} S_p(x/p).
$

### Exact block decomposition for (S_p(y))

Let (K=\lfloor \log_p y\rfloor). On the block (m\in[p^k,p^{k+1})) we have (\lfloor\log_p m\rfloor=k), so
$
S_p(y) = \sum_{k=0}^{K-1}p^k\sum_{m=p^k}^{p^{k+1}-1}\frac1m + p^K\sum_{m=p^K}^{\lfloor y\rfloor-1}\frac1m.
$
Using harmonic numbers (H_N=\sum_{m\le N}1/m), this is
$
S_p(y)=\sum_{k=0}^{K-1} p^k(H_{p^{k+1}-1}-H_{p^k-1})+p^K(H_{\lfloor y\rfloor-1}-H_{p^K-1}).
$

### Asymptotic shape of (S_p(y))

Write (y=p^K u) with $u\in[1,p)$. Using (H_N=\log N+\gamma+O(1/N)), one gets

$H_{p^{k+1}-1}-H_{p^k-1}=\log p + O(p^{-k}),$

so

$\sum_{k=0}^{K-1} p^k(H_{p^{k+1}-1}-H_{p^k-1}) = \log p\sum_{k=0}^{K-1}p^k + O(K) = \frac{\log p}{p-1}p^K + O(K).$

Also

$
p^K(H_{\lfloor y\rfloor-1}-H_{p^K-1})
= p^K\log u + O(1).
$

Since (p^K=y/u) and (K\asymp \log y/\log p), we get the clean approximation
$
S_p(y) =\frac{y}{u}\\(\log u + \frac{\log p}{p-1}\\) + O\\(\frac{\log y}{\log p}\\) \qquad (y=p^K u,\ 1\le u<p).$

### Plugging into $H(x)$

Put (y=x/p), and for each prime define (u_p(x)\in[1,p)) by
$
\frac{x}{p}=p^{K_p}u_p(x),\qquad K_p=\\\lfloor \log_p(x/p)\\\rfloor.
$
Then
$
H(x) = x\sum_{p<x} \frac1{p,u_p(x)} \\(\log u_p(x)+\frac{\log p}{p-1}\\) + O\\(\sum_{p<x}\frac{\log(x/p)}{\log p}\\).
$
The error term is $O(x)$: crudely (\log(x/p)\ll\log x), and (\sum_{p<x}1/\log p \ll \pi(x)/\log 2 \ll x/\log x), so the error is (\ll (x/\log x)\log x \ll x).

The *main term* is $x$ times a convergent prime series [[nomath]](absolutely convergent, because for large $p$ the summand is $\ll (\log p)/(p^2)$)[[/nomath]]. Hence:

* **Pointwise growth**: (H(x)=\Theta(x)), in particular
  $
  H(x)\ll x.
  $
  This immediately implies your last bound:
  $
  H(x)\ll x\log\log\log\log x
  \quad\text{trivially, since }\log\log\log\log x\to\infty\text{)}.
  $

* **A clean “average constant”**: if one averages over $x$ [[nomath]](or heuristically treats the mantissas $u_p(x)$ as equidistributed on a log scale)[[/nomath]], the mean contribution of a fixed prime $p$ becomes
  $
  \mathbb{E}[\frac{1}{p,u_p(x)}(\log u_p(x)+\frac{\log p}{p-1})] = \frac{p-1}{p^2\log p}.
  $

  So the averaged constant is

  $
  C:=\sum_{p}\frac{p-1}{p^2\log p},
  $
  a convergent series numerically (\approx 1.1\text{–}1.13) (it converges slowly). In this sense,
  [
  H(x)\sim Cx
  ]
  in Cesàro/averaged form. Pointwise, $H(x)/x$ may have small bounded oscillations coming from the bounded “mantissas” (u_p(x)) for small primes.

This answers the “find an asymptotic formula” part in the most explicit way: $H(x)$ is $x$ times a convergent (but slightly oscillatory) prime series, plus an $O(x)$ error.

---

## 3) The “almost all $n$” statement for $F(n)$

You always have
[
n+\omega(n)-1\le F(n)\le n,\omega(n),
]
and for almost all $n$, (\omega(n)\sim \log\log n). So $F(n)$ is always between (\asymp n) and (\asymp n\log\log n).

The question “is (F(n)\gg n\log\log n) for almost all $n$?” is much subtler. To force $F(n)$ to be (\gg n\log\log n) for almost all $n$, one would need, for typical $n$, to be able to partition the prime divisors into (\asymp \log\log n) disjoint groups each producing an $S$-smooth number (\asymp n). It is not clear (to me) how to do that for a density‑$1$ set of $n$, and heuristically it seems **unlikely**: producing an $S$-smooth number within a fixed constant factor of $n$ typically requires that $S$ contains at least one very small prime, but a random integer has only $O(1)$ such primes.

So:

* I can’t give a proof either way here.
* The easy inequalities above do **not** support (F(n)\gg n\log\log n) a.a.n., and heuristics suggest $F(n)$ should be only a small multiple of $n$ for typical $n$, i.e. (F(n)=o(n\log\log n)) a.a.n. might actually be closer to the truth.

---

## 4) (\max_{n\le x} f(n)) and (\max_{n\le x}F(n))

You have the universal upper bound
[
f(n)\le n,\omega(n)\le x\cdot \max_{n\le x}\omega(n).
]
And the classical maximal order of (\omega(n)) is
[
\max_{n\le x}\omega(n)=(1+o(1))\frac{\log x}{\log\log x},
]
so certainly
[
\max_{n\le x} f(n)\ \le\ (1+o(1)),\frac{x\log x}{\log\log x}.
]
That gives your proposed asymptotic as the **largest possible order of magnitude**, but getting a matching lower bound [[nomath]](and a true $\sim$)[[/nomath]] requires exhibiting (n\le x) for which **most** of the terms (p^{\lfloor\log_p n\rfloor}) are (\asymp n). For large primes $p$ [[nomath]](say $p\asymp \log x$)[[/nomath]] this asks for very strong simultaneous “near power” behavior, which looks like a hard simultaneous Diophantine approximation problem. I do not know a proof that
[
\max_{n\le x} f(n)\sim \frac{x\log x}{\log\log x}.
]
A more conservative heuristic (consistent with the “random mantissa” model) suggests that a typical term for a prime $p$ contributes (\asymp n/\log p), and if one pushes (\omega(n)) to its maximum, one is led instead to the scale
[
\max_{n\le x} f(n)\ \text{around}\ \frac{x\log x}{(\log\log x)^2},
]
up to constants. I’m not claiming this as a theorem—just saying that your proposed (\sim x\log x/\log\log x) is not obviously compatible with the “random mantissa” heuristics.

For $F$: since (F(n)\ge f(n)), one has
[
\max_{n\le x}F(n)\ \ge\ \max_{n\le x}f(n),
]
and also (\max_{n\le x}F(n)\le (1+o(1))x\log x/\log\log x) by the same (\omega(n)) argument.

So the two maxima are squeezed into the same broad window, but I do not know an argument that they are asymptotically equal, let alone equal for all large $x$.

---

## 5) Is (\max_{n\le x} f(n)=\max_{n\le x}F(n)) for (all large) $x$?

Since (F\ge f), equality of maxima means: at the point$s$ where $F$ is maximal up to $x$, one can’t do better than the “singleton” choice. There’s no obvious monotonic/structural reason forcing that, and even for moderate $x$ one can find ranges where (\max F>\max f) and other ranges where they coincide.

So:

* **For all $x$**: certainly not.
* **For all sufficiently large $x$**: I don’t see a proof; it feels like a delicate extremal question.

---

## 6) Counting (n<x) with (f(n)=F(n))

This asks for a fine understanding of when “grouping primes” produces a genuine improvement over singleton prime powers. It depends on the existence of subsets (S\subseteq P(n)) for which (M_S(n)) is unexpectedly close to $n$ compared to (\sum_{p\in S}P_p(n)).

I don’t have a rigorous asymptotic formula here. Heuristically, as (\omega(n)) grows, there are more candidate subsets and one expects (f(n)<F(n)) more often, so the density might plausibly decrease with $x$; but pinning down an asymptotic would require a quite refined probabilistic model for the distribution of these smooth maxima (M_S(n)) relative to $n$.

---

## 7) Summary of what *is* solid here

* **Yes**: (f(n)=o(n\log\log n)) for almost all $n$. A clean way to see it is via the bound (H(x)\ll x) and Markov.
* **A usable asymptotic description** of
  [
  H(x)=\sum_{n<x}\frac{f(n)}{n}
  ]
  is obtained by the exact block decomposition of (S_p(y)) and yields (H(x)=\Theta(x)) with an explicit (bounded) “almost periodic” main term.
* **Yes**: (H(x)\ll x\log\log\log\log x) [[nomath]](in fact $H(x)\ll x$)[[/nomath]].

The remaining extremal questions about (\max f), (\max F), their equality, and the density of $f=F$ look genuinely delicate and (at least from the viewpoint of the above reductions) seem to hinge on nontrivial simultaneous approximation/smooth-number phenomena.

If you want, I can also:

* write $H(x)$ in a more “closed” form using harmonic numbers (no big‑O inside the prime sum), or
* develop a more explicit heuristic for the growth of (\max_{n\le x} f(n)) based on choosing $n$ with prescribed prime factor sizes [[nomath]](which is where the $(\log\log x)^2$ vs $\log\log x$ discrepancy seems to come from)[[/nomath]].

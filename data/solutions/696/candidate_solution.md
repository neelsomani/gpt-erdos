Write (n\ge 2) with prime divisors ({p:,p\mid n}).

* $h(n)$ is the maximum length (\ell) of a *prime chain inside the prime divisors of $n$*,
  $
  p_1<p_2<\cdots<p_\ell,\qquad p_i\mid n,\qquad p_{i+1}\equiv 1\pmod{p_i}.
  $
* $H(n)$ is the analogous maximum length $u$ allowing *arbitrary divisors* (d_i\mid n),
  $
  d_1<d_2<\cdots<d_u,\qquad d_{i+1}\equiv 1\pmod{d_i}.
  $

A few immediate bounds:

* (1\le h(n)\le \omega(n)) (number of distinct prime factors), and (h(n)\le H(n)).
* (1\le H(n)\le \tau(n)) (number of divisors).
* For “almost all” $n$, (\omega(n)\sim \log\log n), so trivially (h(n),H(n)\le (1+o(1))\log\log n) for a set of $n$ of density $1$.

That said, those upper bounds are very loose for these particular chain conditions.

## What is known for $h(n)$

Erdős already noted:

* It is “easy to see” that (h(n)\to\infty) for almost all $n$.
  A clean way to justify this (as written out in the discussion thread) is: if a set of primes $P$ has (\sum_{p\in P}\frac1p=\infty), then the set of integers with **no** prime factor from $P$ has density $0$; by building nested sets (P_1,P_2,\dots,P_c) where every prime in (P_{k+1}) is (1\bmod p) for some (p\in P_k), one forces the existence of a length-$c$ chain for all but an (\epsilon)-fraction of integers, for any fixed $c$.

Erdős also proposed a conjectural *normal order* (typical size) for $h(n)$. Define $L(n)$ to be the least $v$ such that the $v$-fold iterated logarithm drops below $e$, i.e.
$
L(n):=\min{v:\log^{(v)}(n)<e},
$
so $L(n)$ is (\log_* n) up to an additive constant. Erdős wrote that the normal order of $h(n)$ “seems … about $L(n)$”, though he did not fill in details.

So, as of the last public discussion I can point to, the best-established statement is:

* **Rigorous:** (h(n)\to\infty) for almost all $n$.
* **Conjectural:** typical $h(n)$ is of size (\asymp \log_* n).

### Why (\log_* n) is a natural guess (heuristic)

A back-of-the-envelope heuristic goes like this. Fix a modulus $m$. Among primes (q\equiv 1\pmod m), the “divisibility-by-$n$” weight is (\sim 1/q), so the expected “available mass” of such primes up to $y$ is
[
\sum_{\substack{q\le y\ q\equiv1!!!!\pmod m}}\frac1q \approx \frac1{\varphi(m)}\log\log y \sim \frac1m\log\log y
]
(using the prime number theorem in arithmetic progressions heuristically; the discussion thread uses this kind of input at the qualitative level).
To have a *reasonable chance* of finding at least one such prime divisor of a random integer, you typically want this sum to be (\gg 1), i.e. (\log\log y \gg m), meaning $y$ has to be about (\exp(\exp(c m))). So the “typical scale” of a successor to a modulus $m$ is doubly exponential in $m$. Iterating such growth, the number of steps before you exceed $n$ is governed by how many iterated logs it takes to come back down—i.e. (\log_* n).

This is not a proof, but it matches Erdős’s stated guess.

## What is known for $H(n)$

Erdős defined $H(n)$ in the same note and said:

* He was *not sure* whether (H(n)/h(n)\to\infty) for almost all $n$.
* But he was “sure that $H(n)$ is not much larger than $L(n)$” [[nomath]](again $L(n)$ is an iterated-log function)[[/nomath]].

He also related estimating $H(n)$ to understanding densities of integers having a divisor (D\equiv 1\pmod d) with $D$ not “too large” compared to $d$, via a function $A(d,\alpha)$ (in his notation).
This is very much in line with the heuristic above: to make a long chain, you repeatedly need a divisor in a very thin congruence class, and the “typical” size of the first such divisor explodes with the modulus.

So, again, what seems to be on solid ground from the sources above is:

* **Rigorous:** (H(n)\ge h(n)\to\infty) for almost all $n$.
* **Heuristic / Erdős’s belief:** typical $H(n)$ should also be on the scale of an iterated log $L(n)$, not dramatically larger.

## Does (H(n)/h(n)\to\infty) for almost all $n$?

As posed, this appears to still be **open**: the current discussion page flags the problem as open and explicitly notes Erdős’s uncertainty on exactly this ratio question.

Conceptually there are two competing intuitions:

* **Reasons the ratio might diverge:** allowing composite divisors gives more “degrees of freedom” to hit a residue class (1\bmod d_i), so you might be able to interpolate many more steps than in a prime-only chain.
* **Reasons it might *not* diverge:** regardless of primality, each step asks for a divisor in a very sparse congruence class. If the “first available” (D\equiv1\pmod d) is typically astronomically large relative to $d$, then both prime chains and divisor chains hit the same growth bottleneck, leading to comparable (\log_*)-scale behavior—exactly what Erdős suggested.

Anecdotally (not a theorem), in small computational experiments on random integers up to about (10^{18}), one often sees $h(n)$ around $2$ and $H(n)$ around $3$–$4$, so (H(n)/h(n)) is typically a small constant. That’s consistent with “same order” behavior, but it’s far too small-scale to resolve an iterated-log question.

## Summary “estimates” in the current state of knowledge

* (h(n)\to\infty) for almost all $n$.
* Erdős conjectured the **normal order** (h(n)\asymp L(n)\sim \log_* n).
* For $H(n)$, Erdős believed $H(n)$ is also (\ll L(n)) typically, but he did **not** know whether (H(n)/h(n)\to\infty).
* As of the latest public discussion I found, the ratio question remains open.

If you want, I can also sketch a more detailed probabilistic model (in the spirit of Erdős–Kac type “random prime factor” models) that leads to the (\log_*) heuristic for both $h(n)$ and $H(n)$, and indicate where proving it rigorously seems to get stuck.

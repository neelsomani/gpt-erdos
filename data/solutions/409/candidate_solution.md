Let
[
T(n)=\varphi(n)+1,\qquad n_0=n,\quad n_{k+1}=T(n_k),
]
and define $F(n)$ to be the **least** (k\ge 0) such that (n_k) is prime [[nomath]](so $F(p)=0$ for primes $p$)[[/nomath]]. This $F(n)$ is OEIS **A039651**, and the terminal prime (\lim_{k\to\infty} n_k) is OEIS **A039650**. ([OEIS][1])

## 1) How many iterations before a prime is reached?

### Existence is easy: every orbit reaches a prime

For (n>1) we have (\varphi(n)\le n-1), with equality iff (n) is prime. Hence:

* If (n_k) is prime, then (n_{k+1}=\varphi(n_k)+1=n_k), so primes are fixed points.
* If (n_k) is composite and (>1), then (\varphi(n_k)\le n_k-2), so
  $
  n_{k+1}=\varphi(n_k)+1\le n_k-1<n_k.
  $
  Thus the sequence strictly decreases until it hits a prime, at which point it stays there. ([OEIS][2])

So (F(n)) is always finite.

### A simple explicit upper bound: (F(n)=O(\sqrt n)) [[nomath]](hence $o(n)$)[[/nomath]]

A slightly sharper “trivial” bound than (F(n)\le n) is sublinear.

If (m\ge 4) is composite and $p$ is its smallest prime factor, then (p\le \sqrt m). Using
[
\varphi(m)=m\prod_{q\mid m}\Bigl(1-\frac1q\Bigr)\le m\Bigl(1-\frac1p\Bigr),
]
we get
[
\varphi(m)\le m\Bigl(1-\frac1{\sqrt m}\Bigr)=m-\sqrt m,
]
so
[
T(m)=\varphi(m)+1\le m-\sqrt m+1.
]
Write (m=u^2) with (u=\sqrt m\ge 2). Then
[
T(m)\le u^2-u+1 \le \left(u-\frac14\right)^2\qquad(\text{for }u\ge 2),
]
because (\left(u-\tfrac14\right)^2-(u^2-u+1)=\tfrac{u}{2}-\tfrac{15}{16}\ge 0).
So as long as you are at a composite (\ge 4), the square-root drops by at least (1/4) each step:
[
\sqrt{n_{k+1}}\le \sqrt{n_k}-\frac14.
]
Therefore after at most (4\sqrt n) steps you must have dropped below $4$, and by then you have already hit a prime [[nomath]](since $2,3$ are prime and the iteration cannot get stuck at a composite)[[/nomath]]. Concretely,
[
F(n)\le 4\sqrt n + O(1).
]
In particular (F(n)=o(n)), which is noted as “trivial” in the Erdős-problems discussion of this question. ([erdosproblems.com][3])

### Lower end: (F(n)=1) happens infinitely often

For every odd prime $p$,
[
T(2p)=\varphi(2p)+1=\varphi(2)\varphi(p)+1=(p-1)+1=p,
]
so (F(2p)=1) for infinitely many $n$. This is also noted in the Erdős-problems discussion. ([erdosproblems.com][3])

What is *not* known (and is essentially what Erdős #409 is asking) is whether one can get “good” upper bounds much smaller than (O(\sqrt n)), e.g. polylogarithmic bounds, or sharp growth rates for the maximal/typical size of $F(n)$. ([erdosproblems.com][3])

## 2) Can infinitely many $n$ reach the same prime?

For a prime $p$, let
[
\mathcal B(p)={n\in\mathbb N:\ \text{the iteration eventually reaches }p}.
]

This is **open** in general: it is *conjectured* that each basin (\mathcal B(p)) is finite (so no prime is reached by infinitely many starting values). ([erdosproblems.com][3])

A piece of evidence is OEIS **A229487**, which records (based on computation) a **conjectured largest** starting value that ends at the $n$-th prime. For example, it says that $138$ has trajectory (138\to 45\to 25\to 21\to 13) and is conjectured to be the last number ending at $13$. ([OEIS][4])

Some basins are provably finite by quick ad hoc arguments; e.g. for (p=2), only $1$ and $2$ reach $2$ because for all (n>2), (\varphi(n)) is even and $T(n)$ is odd, so you can’t ever arrive at $2$. (And similarly one can explicitly list the tiny basins for a few small primes.)

## 3) Density of $n$ reaching a fixed prime

If (\mathcal B(p)) is finite, then its natural density is clearly $0$.

The conjecture “(\mathcal B(p)) is finite for every prime $p$” would therefore imply:

* No prime is reached infinitely often, and
* For each fixed prime $p$, the set of $n$ that reach $p$ has density $0$.

This “density zero” conclusion is explicitly mentioned as the expected behavior in the Erdős-problems discussion and is tied to the conjectural maxima in A229487. ([erdosproblems.com][3])

Unconditionally (without assuming finiteness), **the exact density question is still open** as part of Erdős problem #409. ([erdosproblems.com][3])

---

If you want, I can also spell out the reverse-tree description: $n$ reaches $p$ iff there is a chain
[
n \to \cdots \to m \to p
]
with (\varphi(m)=p-1), (\varphi(\cdot)=\text{previous}-1), etc., i.e. iterated inverse-totient conditions. That’s the viewpoint behind why A229487 is naturally about “largest preimages” and why the problem feels close in spirit to inverse totient questions.

[1]: https://oeis.org/A039651 "https://oeis.org/A039651"
[2]: https://oeis.org/A039650 "https://oeis.org/A039650"
[3]: https://www.erdosproblems.com/forum/thread/409 "https://www.erdosproblems.com/forum/thread/409"
[4]: https://oeis.org/A229487 "https://oeis.org/A229487"

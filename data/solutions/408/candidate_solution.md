Let ( \phi_0(n)=n), (\phi_{k+1}(n)=\phi(\phi_k(n))), and
[
f(n)=\min{k:\phi_k(n)=1}.
]
This $f(n)$ is the classical “height” (Pillai–Shapiro height) of $n$ under (\phi)-iteration.

## 1) Scale of $f(n)$ and what is known unconditionally

A first key point is that $f(n)$ is **linear in (\log n)** up to absolute constants. Pillai (1929) proved (in a form equivalent to)
[
\frac{\log(n/2)}{\log 3}+1 \ \le\ f(n)\ \le\ \frac{\log n}{\log 2}+1
\qquad (n\ge 2),
]
so (f(n)\asymp \log n). ([OEIS][1])

The extremal behaviors are easy to see:

* If (n=2^a), then (\phi(2^a)=2^{a-1}), so (f(2^a)=a) and (f(n)/\log n \to 1/\log 2).
* If (n=2\cdot 3^b), then (\phi(2\cdot 3^b)=2\cdot 3^{b-1}), so (f(2\cdot 3^b)=b+1) and (f(n)/\log n \to 1/\log 3).

In fact Erdős–Granville–Pomerance–Spiro (EGPS) note that by taking (n=2^a3^b) and varying $(a,b)$, the set of values (f(n)/\log n) is **dense** in the interval ([1/\log 3,;1/\log 2]). ([OEIS][2])

So:

* The normalization (f(n)/\log n) is the “right” scale [[nomath]](it does **not** tend to $0$)[[/nomath]].
* But density of values does **not** tell you what happens for “most” integers.

## 2) Shapiro’s structure: $f$ is essentially multiplicative

Shapiro discovered a strong “almost additivity” (equivalently, “essential multiplicativity”) structure. One convenient way to state it is via the variant
[
F(n)=
\begin{cases}
f(n), & n \text{ even},\
f(n)-1,& n \text{ odd},
\end{cases}
]
which is **completely additive**:
[
F(mn)=F(m)+F(n)\quad \text{for all }m,n.
]
A precise prime-factorization formula (as presented e.g. by Bal–Bhatnagar) is: if
(n=2^\alpha\prod_{i=1}^r p_i^{\alpha_i}) with (p_i) odd primes, then
[
f(n)=
\begin{cases}
\alpha+\sum_{i=1}^r \alpha_i,(f(p_i)-1), & \alpha>0,[4pt]
1+\sum_{i=1}^r \alpha_i,(f(p_i)-1), & \alpha=0,
\end{cases}
]
and this implies the near-additivity rule (f(mn)=f(m)+f(n)) except for a (\pm 1) correction depending on parity. 

This reduces the “normal order” problem for $f(n)$ to understanding $f(p)$ on primes and how that propagates through factorization.

## 3) Does (f(n)/\log n) have a limiting distribution? Is it almost always constant?

### The conjectural picture

EGPS explicitly conjecture that there is a constant (\alpha\in[1/\log 3,,1/\log 2]) such that
[
f(n)\sim \alpha \log n \quad \text{for a set of integers (n) of asymptotic density (1)}.
]
If this holds, then:

* (f(n)/\log n) is **almost always constant** [[nomath]](tends to $\alpha$ in probability)[[/nomath]],
* and therefore (f(n)/\log n) has a **distribution function**, but it is **degenerate** [[nomath]](a step function at $\alpha$)[[/nomath]]. ([OEIS][2])

### What is proved

EGPS prove that the answers to your first two questions are **yes** **conditionally**: assuming a suitable Elliott–Halberstam–type hypothesis about the distribution of primes in arithmetic progressions, they obtain such a constant (\alpha) and show $f(n)$ has normal order (\alpha\log n). ([OEIS][2])

### Unconditional status (as of the literature summarized above)

Unconditionally, the existence of a limiting distribution for (f(n)/\log n), and the stronger statement that it is almost always constant, remain **open** (beyond the universal bounds and the density-of-values phenomenon). ([Erdős Problems][3])

#### Related unconditional progress [[nomath]](for fixed iterate depth, not for $f$)[[/nomath]]

EGPS *do* prove several “normal behavior” results for **fixed** $k$ about the sizes of successive iterates, e.g. a normal order for (\phi_k(n)/\phi_{k+1}(n)) [[nomath]](involving $k e^\gamma \log\log\log n$)[[/nomath]] and distributional statements for normalized (n/\phi_{k+1}(n)). ([OEIS][2])
These are substantial, but they don’t resolve the “height” $f(n)$ question.

## 4) Largest prime factor of (\phi_k(n)) for (k=\log\log n)

Write (P^+(m)) for the largest prime factor of (m).

EGPS formulate a conjecture aimed exactly at this kind of question:

> For each (\varepsilon>0), the upper density of integers (n) with
> (P^+(\phi_k(n))>n^\varepsilon) tends to (0) as (k\to\infty). ([OEIS][2])

They also remark that they can prove this **for (\varepsilon>2/3)** using sieve methods (they do not include the proof in that chapter). ([OEIS][2])

### What this suggests for (k=\log\log n)

Since (k=\log\log n\to\infty) with (n), the conjecture would imply that for almost all (n),
[
P^+(\phi_{\lfloor \log\log n\rfloor}(n)) \le n^{o(1)},
]
i.e. the iterates become “subpolynomially smooth” relative to the starting size (n). This is also recorded as the “likely true” expectation in discussions of the problem. ([Erdős Problems][3])

Unconditionally, the best statement explicitly indicated in EGPS is much weaker: it only controls (P^+(\phi_k(n))) above (n^\varepsilon) for (\varepsilon>2/3) once $k$ is large. ([OEIS][2])

### Evidence in the “small primes definitely appear” direction

Although it doesn’t bound the *largest* prime factor, there are results showing iterates pick up lots of *small* prime factors:

* EGPS prove there is a constant (c>0) such that for almost all $n$ there exists some iterate (\phi_j(n)) divisible by **every prime** (\le (\log n)^c). ([OEIS][2])
* For primes $p$, Pollack proves that (\prod_{k\ge 1}\phi_k(p)) is [[nomath]](for almost all $p$)[[/nomath]] divisible by every prime (q\le (\log p)^{1/2-o(1)}), again showing rapid accumulation of small prime divisors in the iterates. 
* For fixed $k$, Lamzouri studies the frequency with which (\phi_k(n)) is $y$-smooth, conditional on a weak Elliott–Halberstam-type hypothesis. ([arXiv][4])

These results align with the heuristic that iterating (\phi) “smooths” numbers progressively, even though turning that into sharp bounds on (P^+(\phi_k(n))) for $k$ growing like (\log\log n) appears to be well beyond current unconditional technology.

## Summary

* $f(n)$ is always of size (\asymp \log n), with sharp universal bounds between ((1/\log 3)\log n) and ((1/\log 2)\log n) (up to additive constants). ([OEIS][1])
* The set of values of (f(n)/\log n) is dense in ([1/\log 3,1/\log 2]). ([OEIS][2])
* It is conjectured that (f(n)\sim \alpha\log n) for a constant (\alpha) on a density‑1 set; under an Elliott–Halberstam-type hypothesis EGPS prove this, giving a degenerate limiting distribution for (f(n)/\log n). Unconditionally, this remains open. ([OEIS][2])
* For the largest prime factor, EGPS conjecture that (P^+(\phi_k(n))\le n^{o(1)}) for “most” $n$ once (k\to\infty) [[nomath]](hence in particular for $k=\log\log n$)[[/nomath]], and they can prove a partial version for thresholds (n^\varepsilon) with (\varepsilon>2/3). ([OEIS][2])

If you want, I can also summarize the *conditional* mechanism in EGPS [[nomath]](how the EH-type hypothesis feeds into the additive model for $F(n)$)[[/nomath]] and what kind of constant (\alpha) one expects heuristically, but the headline is: unconditional answers to the first two are still not known, while the prime-factor question is framed by Conjecture 2 with only partial progress.

[1]: https://oeis.org/A003434 "https://oeis.org/A003434"
[2]: https://oeis.org/A000010/a000010_1.pdf "https://oeis.org/A000010/a000010_1.pdf"
[3]: https://www.erdosproblems.com/forum/thread/408 "https://www.erdosproblems.com/forum/thread/408"
[4]: https://arxiv.org/abs/math/0503246 "https://arxiv.org/abs/math/0503246"

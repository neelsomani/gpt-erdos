* If $f$ is a **polynomial**, the answer is **no**: if (\deg f=d), then (\bigl|f(z)/z^n\bigr|\to 0) along every path for every (n>d).

* If $f$ is **transcendental entire** (i.e. not a polynomial), the answer is **yes**.

## Existence of a single path beating every power of $z$

A result attributed to **R. P. Boas (unpublished)** states that for a transcendental entire function $f$ there exists a path (\Gamma_\infty) tending to (\infty) such that for **every** (n\in\mathbb{N}),
[
\left|\frac{f(z)}{z^n}\right|\longrightarrow\infty\qquad(z\to\infty,\ z\in \Gamma_\infty).
]
This is recorded (as “Problem 2.6” with update) in Hayman’s problem compilation. ([arXiv][1])

So, apart from the polynomial obstruction, such a path always exists.

[[nomath]](Separately, it’s also classical that $\infty$ is an asymptotic value of every transcendental entire function, i.e. there is always some curve on which $|f(z)|\to\infty$; the Boas statement is much stronger because it forces growth faster than **every** polynomial.)[[/nomath]] ([arXiv][1])

## Can one estimate the length of such a path?

A standard way to measure this is: if (\Gamma) is a rectifiable curve tending to (\infty), let (\ell(r)) be the length of (\Gamma\cap{|z|<r}).

There are some **positive upper bounds under growth restrictions**, and also strong **negative results** showing you cannot hope for a simple “always short” bound.

### Positive results (under hypotheses)

* If the Nevanlinna characteristic satisfies (T(r,f)=O((\log r)^2)), then one can choose (\Gamma_\infty) to be a **straight line** [[nomath]](so $\ell(r)\asymp r$)[[/nomath]]. ([arXiv][1])
  (This is mentioned in the update to Problem 2.7.)

* If $f$ has **finite order (\rho)**, then for every (\varepsilon>0) there exists such a curve with
  [
  \ell(r)=O!\left(r^{,1+\frac{1}{2\rho}+\varepsilon}\right).
  ]
  ([arXiv][1])

These are not stated directly in terms of $M(r)$, but for entire functions $T(r,f)$ and (\log M(r)) are tightly related, so bounds phrased via $T$ can often be translated into bounds involving $M$ (at least at the level of order / growth-rate classes).

### Negative results (what cannot be uniformly bounded)

Even for finite-order functions, you cannot in general force (\ell(r)=O(r)) along an asymptotic curve.

Hayman’s compilation records a refined “Problem 2.41” explicitly asking for estimates of (\ell(r)) **in terms of $M(r,f)$**, and its update says Gol’dberg–Eremenko “completely solved” it; in particular they showed that for **every** function (\varphi(r)\to\infty) there exists an entire $f$ such that (\ell(r)\not=O(r)) for **every** asymptotic curve. They also give such examples even within finite order (\rho>1/2) (for curves tending to a finite asymptotic value). ([arXiv][1])

So: yes, there is a developed theory relating (\ell(r)) to growth [[nomath]](including $M(r)$)[[/nomath]], but **no universal linear-length bound** is possible in general; the best bounds depend on additional structure (order, regularity, etc.).

## Can one force growth along a path in terms of $M(r)$, e.g. $M(r)^\varepsilon$?

Here one has to be careful about what “faster than (M(r)^\varepsilon)” means. Two common interpretations are:

1. **Lower bound**: (|f(z)| \ge M(|z|)^\varepsilon) eventually along some path.

2. **Ratio growth**: (|f(z)|/M(|z|)^\varepsilon \to \infty) along some path.

Either way, the general situation is **negative without extra assumptions**.

Hayman notes that there exist entire functions of **infinite order** [[nomath]](so $M(r)$ can grow arbitrarily fast)[[/nomath]] with the property that on **every** path (\Gamma) on which (|f(z)|\to\infty), one still has
[
\log\log|f(z)| = O(\log|z|),
]
i.e. the restriction of $f$ to any such path has **finite order** growth. ([arXiv][1])
By choosing such an $f$ with $M(r)$ growing extremely rapidly [[nomath]](so that $M(r)^\varepsilon$ dwarfs $\exp(r^C)$ for any fixed $C$)[[/nomath]], you can ensure that along every curve where (|f(z)|\to\infty), (|f(z)|) is far smaller than (M(|z|)^\varepsilon) for large (|z|). This rules out any universal guarantee of a “power-of-$M$” lower bound on a curve.

### What *is* known in the direction of “growth in terms of $M$”?

There are partial positive statements under hypotheses on the order. For example, Hayman’s update to Problem 2.6 cites a theorem of Talpur: if $f$ has order (\rho) with (\alpha<\rho<\tfrac12), then there is a path (\Gamma_\infty) along which
[
\log|f(z)| > \log M!\left(|z|^{,\frac{1-\rho/\alpha}{1+\varepsilon}}\right)\cos(\pi\alpha)
]
for (z\to\infty) on (\Gamma_\infty) [[nomath]](with $\varepsilon\to 0$)[[/nomath]]. ([arXiv][1])
Notice this compares (|f|) on the curve to $M(\cdot)$ at a **smaller radius** than (|z|), not $M(|z|)$ itself.

Also, Eremenko proved lower bounds along an asymptotic curve in terms of order (\rho) and lower order (\lambda): there exists (\Gamma_\infty) such that
[
\log|f(z)| > \bigl(A(\rho,\lambda)+o(1)\bigr),\log|z|,
]
with an explicit positive constant $A(\rho,\lambda)$ [[nomath]](and $A\ge \lambda$ if $\lambda<\tfrac12$)[[/nomath]]. ([arXiv][1])
This is a “polynomial-type” lower bound along the curve [[nomath]](not directly a bound in terms of $M$)[[/nomath]].

## A useful growth fact about $M(r)$

For context: if $f$ is transcendental entire, then
[
\frac{\log M(r)}{\log r}\to\infty\qquad(r\to\infty),
]
so $M(r)$ eventually dominates every power (r^n). ([arXiv][2])
That’s why a curve on which (|f(z)|) stays even modestly comparable to $M(|z|)$ would automatically satisfy the Boas “beats every (z^n)” property—but the point is that such near-maximum comparability along a single curve cannot be guaranteed in general.

---

If you tell me whether you mean the **lower-bound** interpretation (|f(z)|\ge M(|z|)^\varepsilon) or the **ratio** interpretation (|f(z)|/M(|z|)^\varepsilon\to\infty), I can tailor the “in terms of $M$” part more precisely; but either way, the Hayman examples show there is no general theorem forcing a fixed power-of-$M$ behavior along a path without extra hypotheses. ([arXiv][1])

[1]: https://arxiv.org/pdf/1809.07200 "https://arxiv.org/pdf/1809.07200"
[2]: https://arxiv.org/pdf/1009.5081 "https://arxiv.org/pdf/1009.5081"

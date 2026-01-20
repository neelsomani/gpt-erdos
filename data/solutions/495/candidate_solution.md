What you wrote is **exactly Littlewood’s conjecture**:

[
\liminf_{n\to\infty} n,|n\alpha|,|n\beta|=0\qquad(\alpha,\beta\in\mathbb R),
]

and it is **still open in full generality**. ([Wikipedia][1])

### Cases where it *is* known to be true

* If **(\alpha)** or **(\beta)** is **rational**, then (|n\alpha|=0) [[nomath]](or $|n\beta|=0$)[[/nomath]] for infinitely many $n$, so the liminf is trivially $0$.
* More generally, it “clearly” holds if **(1,\alpha,\beta)** are **linearly dependent over (\mathbb Q)**, or if **(\alpha)** or **(\beta)** has **unbounded partial quotients** in its continued fraction expansion (i.e. is **not badly approximable**). 
  [[nomath]](Indeed, if $\inf_n n|n\alpha|=0$, then along those $n$ we have $n|n\alpha||n\beta|\le \tfrac12, n|n\alpha|\to 0$.)[[/nomath]]

So the genuinely difficult case is when **both (\alpha,\beta)** are **badly approximable** and (1,\alpha,\beta) are (\mathbb Q)-independent. 

### What is known “in general”

Even though the conjecture is open, there are strong partial results:

* **Almost every pair $(\alpha,\beta)$** satisfies an even stronger quantitative statement: for almost all $(\alpha,\beta)$,
  [
  \inf_{q\ge 2} q(\log q)^2,|q\alpha|,|q\beta|=0,
  ]
  a theorem of **Gallagher (1962)**. 

* If there are counterexamples, they form an **extremely small** set: **Einsiedler–Katok–Lindenstrauss (2006)** proved the set of exceptions has **Hausdorff dimension $0$**. ([Annals of Mathematics][2])

* There are also special algebraic cases known, e.g. **Cassels–Swinnerton-Dyer** proved the conjecture when (\alpha) and (\beta) lie in the **same cubic field**. 

### Bottom line

* **Yes** in many natural cases (rational dependence, non–badly-approximable numbers, almost all pairs, etc.). 
* **But in full generality for all (\alpha,\beta\in\mathbb R)**: **unknown** — it is the classical **Littlewood conjecture**, still open. ([Wikipedia][1])

[1]: https://en.wikipedia.org/wiki/Littlewood_conjecture "Littlewood conjecture - Wikipedia"
[2]: https://annals.math.princeton.edu/wp-content/uploads/annals-v164-n2-p04.pdf?utm_source=chatgpt.com "Invariant measures and the set of exceptions to Littlewood's ..."

Taken literally, the statement is **false** because of the trivial case $p=2$: there is no prime (q<p).

For **odd primes $p$** (the interesting case), this is a **well-known open problem** (often attributed to Erdős). In Zhi‑Wei Sun’s survey paper it is stated explicitly as an “open question”:

> **Erdős’ Problem:** “Whether for any sufficiently large prime $p$ there exists a prime (q<p) which is a primitive root modulo $p$?” ([arXiv][1])

This is essentially your question [[nomath]](and your version “for every prime $p$” is stronger)[[/nomath]], so **no unconditional proof is known** at present; it’s also listed as open on the Erdős Problems site. ([Erdős Problems][2])

### What *is* known

* Let $G(p)$ be the **least prime** $q$ such that $q$ is a primitive root mod $p$. Then your question is asking whether (G(p) < p) for all (or all sufficiently large) primes $p$.
  Unconditionally, it is *not even known* that (G(p) < p) for all sufficiently large $p$. ([MathOverflow][3])

* There are unconditional bounds showing a prime primitive root exists, but the bounds are far too large to imply (q<p). For example, MathOverflow notes that Linnik-type results imply existence of a prime primitive root (\ll p^{5.2}) (uniformly), which does **not** give (<p). ([MathOverflow][3])

### Conditional results (under GRH)

If you assume the **Generalized Riemann Hypothesis (GRH)**, then the conjecture becomes provable in a very strong form: McGown & Treviño show that the **least prime primitive root** (\hat g(p)) satisfies
[
\hat g(p) < \sqrt{p}-2 \quad \text{for all primes } p>2791,
]
which certainly implies (\hat g(p) < p) for all sufficiently large $p$ (and the remaining finitely many primes can be checked directly). 
More broadly, GRH-based work (as summarized on MathOverflow) gives polylogarithmic bounds like (G(p)\ll (\log p)^6). ([MathOverflow][3])

### Computational evidence

Computationally, the statement appears to hold for large ranges. For instance, OEIS sequence **A219429** is defined as “highest prime primitive root [[nomath]](less than $p$)[[/nomath]] for the $n$-th prime $p$ (or **0 if none exists**)” and its listed data show $0$ only at $p=2$, plus it links a table up to $n=10000$ primes. ([OEIS][4])

**Bottom line:** aside from $p=2$, it is **believed true** and strongly supported by computation, but **remains unproved unconditionally** (it’s an open Erdős problem). ([arXiv][1])

[1]: https://arxiv.org/pdf/1405.0290 "arXiv:1405.0290v5  [math.NT]  28 Feb 2020"
[2]: https://www.erdosproblems.com/forum/thread/985 "

    Erdős Problem #985 - Discussion thread

"
[3]: https://mathoverflow.net/questions/112594/least-prime-primitive-root "analytic number theory - Least prime primitive root - MathOverflow"
[4]: https://oeis.org/A219429 "A219429 - OEIS"

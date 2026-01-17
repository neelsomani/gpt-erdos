This is **not known in full generality**. It is an old question of Erdős and Graham (often listed as **Erdős problem #283**) and it remains **open** for arbitrary integer‑valued polynomials $p$ satisfying your “no fixed divisor” hypothesis. ([Erdős Problems][1])

## Why the hypothesis on $p$ matters

Your condition “there is no (d\ge 2) with (d\mid p(n)) for all (n\ge 1)” is exactly the standard “no fixed divisor” condition [[nomath]](equivalently $\gcd{p(n):n\ge 1}=1$, or “for every prime $q$ there exists $n$ with (q\nmid p(n))”). It is necessary: if such a $d$ existed then (\sum_i p(n_i)) would always be divisible by $d$, so you could never hit all large $m$.

Graham explicitly formulated essentially this polynomial generalisation at the end of his 1963 paper and noted that (at least then) “very little is known” beyond special cases. ([Dipartimento di Matematica e Informatica][2])

## What is known (positive results in special cases)

### 1) (p(x)=x): **Yes**

Graham proved that **every integer (m\ge 78)** can be written as a sum of distinct positive integers (n_1<\dots<n_k) whose reciprocals sum to (1). [[nomath]](Equivalently: your statement holds for $p(x)=x$, with the explicit threshold $78$; $77$ is impossible.)[[/nomath]] ([Dipartimento di Matematica e Informatica][2])

He also proved a more general result allowing the reciprocal sum to be any positive rational (\alpha) (with a lower bound on the parts), though with ineffective/large bounds. ([Dipartimento di Matematica e Informatica][2])

### 2) (p(x)=x^2): **Yes**

Alekseyev proved that **(8542)** is the largest integer that *does not* admit such a representation by **distinct squares** whose **reciprocals sum to $1$**. In particular, **all (m>8542)** work for (p(x)=x^2). ([arXiv][3])

### 3) Many linear and quadratic polynomials: **Yes (in many cases, via finite verification)**

Work of van Doorn (including computational verification for large families) shows the conjecture holds for many linear and quadratic examples [[nomath]](the Erdős-problems discussion mentions, e.g., $p(x)=x+b$ for $1\le b\le 10^4$, and $p(x)=x^2+b$ for $50\le b\le 2000$)[[/nomath]], and describes a reduction to a finite search for certain binomials (ax^c+b) with positive leading and constant term. ([Erdős Problems][1])

## Related results if you *drop* the Egyptian-fraction constraint

If you ignore the condition (\sum 1/n_i=1), then the “additive” part becomes much easier: Cassels proved that under the same kind of hypotheses on $p$, **every sufficiently large integer is a sum of distinct values (p(n_i))**. ([Erdős Problems][1])
But incorporating the extra Diophantine constraint (\sum 1/n_i=1) is the hard part and is exactly what is open in general.

## Bottom line

* **General $p$: open.** ([Erdős Problems][1])
* **Proved** for (p(x)=x) [[nomath]](all $m\ge 78$)[[/nomath]]. ([Dipartimento di Matematica e Informatica][2])
* **Proved** for (p(x)=x^2) [[nomath]](all $m>8542$)[[/nomath]]. ([arXiv][3])
* **Proved for many other specific linear/quadratic cases** (not a complete classification). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/283 "

    Erdős Problem #283 - Discussion thread

"
[2]: https://www.dmi.unipg.it/files/matematica/seminari-cds-matematica/A-Theorem_on_Partitions.pdf "A theorem on partitions"
[3]: https://arxiv.org/abs/1801.05928 "[1801.05928] On partitions into squares of distinct integers whose reciprocals sum to 1"

Let
[
\sigma^*(n)=\sum_{\substack{d\mid n\(d,n/d)=1}} d
]
be the **sum of the unitary divisors** of $n$. Then $n$ is *unitary perfect* exactly when the sum of the **proper** unitary divisors is $n$, i.e.
[
\sigma^*(n)=2n.
]

If (n=\prod_{i=1}^r p_i^{a_i}) (distinct primes), then the unitary divisors correspond to choosing either $1$ or (p_i^{a_i}) for each prime, so
[
\sigma^*(n)=\prod_{i=1}^r (1+p_i^{a_i}),
]
and the unitary-perfect equation becomes
[
\prod_{i=1}^r (1+p_i^{a_i}) = 2\prod_{i=1}^r p_i^{a_i}.
]


## What is known

* **There are no odd unitary perfect numbers.**
  This is proved by Subbarao & Warren (1966). 

* **Only five unitary perfect numbers are currently known**:
  [
  6,;60,;90,;87360,;146361946186458562560000.
  ]
  ([FQ Math][1])

* **Strong necessary conditions for any “new” one are known.**
  For instance, Wall proved that any unitary perfect number beyond the known ones must have **at least nine odd prime-power components** (equivalently, at least nine distinct odd prime factors in its factorization). ([FQ Math][1])

* **Finiteness holds in restricted senses.**
  Subbarao & Warren proved:

  * for any fixed $m$, there are only **finitely many** unitary perfect $N$ with a fixed power of $2$ dividing $N$ (their Theorem 3), and
  * for any fixed number $r$ of distinct prime factors, there are only **finitely many** unitary perfect numbers with exactly $r$ primes (their Theorem 4). 

So if there are infinitely many unitary perfect numbers, the number of distinct prime factors would have to be unbounded.

## Answer to your question

**As of the current state of the literature, it is not known whether there are finitely many unitary perfect numbers.** It is *conjectured* that there are only finitely many, but no proof is known; likewise it is unknown whether any exist beyond the five listed above. ([mathworld.wolfram.com][2])

[1]: https://www.fq.math.ca/Scanned/26-4/wall.pdf "fq1988.pdf"
[2]: https://mathworld.wolfram.com/UnitaryPerfectNumber.html "Unitary Perfect Number -- from Wolfram MathWorld"

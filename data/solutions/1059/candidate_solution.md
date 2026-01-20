This is **not known** in general.

The primes with this property are commonly called **Erdős primes**: primes $p$ such that every number
[
p-k! \quad\text{for } 1\le k!!<p
]
is composite. Erdős asked whether there are **infinitely many** such primes; it is listed as an **open Erdős problem** (reported in Guy’s *Unsolved Problems in Number Theory*). ([Erdős Problems][1])

Some nontrivial examples are
[
p=101, 211, 367, 409,; 419,;\dots
]
and many more are tabulated in OEIS sequence **A064152**. ([Erdős Problems][1])

### What is known (evidence)

Computations strongly suggest these primes are not rare. OEIS reports counts up to (10^j) and notes an observed asymptotic of the form
[
|\\{p\le x:\ p \text{ is Erdős prime}\\}|\ \approx\ \frac{1}{8}\frac{x}{\log x},
]
which (if true) would imply infinitely many, but this is **heuristic/experimental**, not proved. ([OEIS][2])

### A useful partial result (but it doesn’t solve the problem)

For any **fixed** $m$, one can show there are infinitely many primes $p$ for which
[
p-1!,\ p-2!,\ \dots,\ p-m!
]
are all composite (just finitely many conditions). A standard way is:

1. Choose distinct primes (q_1,\dots,q_m) with (q_k>m) [[nomath]](so $q_k\nmid k!$)[[/nomath]].
2. Use the Chinese remainder theorem to find a residue class (a \bmod Q) [[nomath]](where $Q=\prod q_k$)[[/nomath]] such that
   [
   a \equiv k! \pmod{q_k}\quad (k=1,\dots,m).
   ]
   Then any (p\equiv a\pmod Q) satisfies (q_k\mid (p-k!)).
3. By Dirichlet’s theorem, there are infinitely many primes (p\equiv a\pmod Q); for sufficiently large such primes, each (p-k!) is larger than (q_k) and hence composite.

The **hard part** in your question is that $m$ is not fixed: as $p$ grows, the number of factorials (k!<p) grows (slowly, but unboundedly). That’s exactly why the infinitude question remains open.

So the current status is:

* **Infinitely many?** Unknown/open. ([Erdős Problems][1])
* **Many examples + heuristic suggesting infinitude:** yes, substantial computational data. ([OEIS][2])

[1]: https://www.erdosproblems.com/forum/thread/1059 "

    Erdős Problem #1059 - Discussion thread

"
[2]: https://oeis.org/A064152 "A064152 - OEIS"

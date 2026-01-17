As of **January 16, 2026**, this is **open for every fixed (k\ge 3)** [[nomath]](and “even the case $k=3$ seems difficult”)[[/nomath]]. It appears as an Erdős–Graham problem (Erdős Problem #279 in the community database). ([Erdős Problems][1])

A few surrounding facts that are known:

* **(k=1): yes (trivial).**
  Take (a_p\equiv 0\pmod p) for every prime (p).
  Then every integer (n\ge 2) is divisible by some prime (p\mid n), so (n=0+(n/p),p) with (t=n/p\ge 1). [[nomath]](If $n$ is prime, take $p=n$ and $t=1$.)[[/nomath]]

* **(k=2): yes (nontrivial but known).**
  In fact, Erdős notes a more general statement: for **any** set (A\subset\mathbb N) with (\sum_{n\in A}\frac1n=\infty), one can choose residue classes (a_n\pmod n) so that all but finitely many integers are (a_n+t n) with (t\ge 2). Since (\sum_p \frac1p=\infty), this applies when $A$ is the set of primes. ([Erdős Problems][1])

* **(k\ge 3): unknown.**
  No construction (or obstruction) is known that settles the question, even for (k=3). ([Erdős Problems][1])

The same Erdős problem page also suggests a plausible broader generalization: the statement “might be true” if the primes are replaced by a set $A$ with roughly prime-like counting function (|A\cap[1,N]|\gg N/\log N) and with a slightly strengthened divergence condition on partial sums of reciprocals. But this remains speculative in the (k\ge 3) range. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/discuss/279 "

    Erdős Problem #279 - Discussion thread

"

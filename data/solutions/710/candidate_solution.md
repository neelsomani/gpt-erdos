Write the condition as a matching problem: for a given $n$ and $F$, consider the bipartite graph with left vertices (1,2,\dots,n) and right vertices the integers in $(n,n+F)$, joining $k$ to $m$ iff (k\mid m).  Then (F=f(n)) is the smallest $F$ for which this graph has a matching that covers the left side [[nomath]](i.e. distinct choices $a_k\in(n,n+F)$ with $k\mid a_k$)[[/nomath]]. This is exactly the framework of Hall’s marriage theorem.

A full asymptotic formula for $f(n)$ is **not known** (this is an Erdős–Pomerance problem and is still listed as open), but the sharpest known growth bounds are:

[
\left(\frac{2}{\sqrt e}+o(1)\right)n\left(\frac{\log n}{\log\log n}\right)^{1/2}
\le
f(n)
\le
\left(1.7398\ldots+o(1)\right)n(\log n)^{1/2},
\qquad (n\to\infty)
]
(with natural logarithms). ([Erdős Problems][1])

In particular these imply the commonly-quoted “asymptotic order” statements
[
\frac{f(n)}{n}\to\infty
\quad\text{and}\quad
f(n)=n(\log n)^{1/2+o(1)}=n^{1+o(1)}.
]
(The first is already emphasized in Erdős–Pomerance. ([Dartmouth Math][2]))

### What this gives as an “asymptotic formula”

The strongest currently justified asymptotic description is therefore:

* **Two-sided asymptotic bounds**
  [
  f(n) \asymp n(\log n)^{1/2}
  \quad\text{up to a factor between }(\log\log n)^{-1/2}\text{ and }1,
  ]
  more precisely the displayed inequality above. ([Erdős Problems][1])

* **Equivalent logarithmic asymptotic**
  [
  \log f(n)=\log n+\tfrac12\log\log n+O(\log\log\log n),
  ]
  which is another way to write (f(n)=n(\log n)^{1/2+o(1)}). ([Erdős Problems][1])

### Very brief idea of why these bounds look like (n\sqrt{\log n})

* The **upper bound** comes from explicitly building a bipartite graph with edges (k\to kp) for primes $p$ in a suitable range so that (kp\in(n,n+F)), and then verifying Hall-type degree conditions using the prime number theorem; this yields (F\ll n\sqrt{\log n}) and can be optimized to the constant (1.7398\ldots). ([Dartmouth Math][2])
* The **lower bound** comes from choosing a subset of “$y$-smooth” $k$’s [[nomath]](all prime factors $\le y$)[[/nomath]] for which any admissible $a_k$ must also be $y$-smooth if $F$ is too small; comparing counts of smooth numbers via de Bruijn-type estimates forces $F$ to be at least (\gg n\sqrt{\log n/\log\log n}), with the constant (2/\sqrt e). ([Dartmouth Math][2])

So, unless “asymptotic formula” is meant in the weak (n(\log n)^{1/2+o(1)}) sense, the exact asymptotics [[nomath]](including the true constant and the presence/absence of a $(\log\log n)^{1/2}$ factor)[[/nomath]] remain open. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/prizes/78 "
  
    Erdős Problems
  
"
[2]: https://math.dartmouth.edu/~carlp/PDF/matching.pdf "PII: 1385-7258(80)90018-9"

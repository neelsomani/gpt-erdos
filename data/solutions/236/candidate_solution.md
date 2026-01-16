This is an **open problem** of Erdős (it appears as Erdős Problem #236). ([Erdős Problems][1])

A few things that *are* known (and help calibrate what one can reasonably expect):

### Basic bounds and reformulation

For fixed $n$,
[
f(n)=#{k\ge 0:\ n-2^k\ \texttext{is prime}}.
]
Since (2^k\le n) forces (k\le \log_2 n), one has the trivial pointwise bound
[
f(n)\le \lfloor \log_2 n\rfloor+1 = O(\log n).
]
Erdős asked whether this can be improved to the little‑$o$ statement
[
\frac{f(n)}{\log n}\to 0\qquad (n\to\infty),
]
i.e. whether $f(n)$ is **always** a vanishing fraction of the (\asymp \log n) available exponents.

### $f(n)$ is unbounded (so it’s not $O(1)$)

Erdős proved that there are infinitely many $n$ with
[
f(n)\gg \log\log n,
]
so $f(n)$ definitely grows without bound along some subsequence. ([Erdős Problems][1])

So the conjecture, if true, is genuinely about ruling out growth as large as a *positive proportion* of (\log n), not about boundedness.

### Typical size is constant (average (\approx 1/\log 2))

Let (r(n)=f(n)). A standard “count representations by $k$” computation using the prime number theorem gives
[
\sum_{n\le x} r(n)\sim \frac{x}{\log 2},
]
so the **average** value of $f(n)$ up to $x$ is asymptotically (1/\log 2\approx 1.44). This is explicitly discussed in work on Romanov’s theorem and refinements. 

A quick consequence is that for any fixed (\varepsilon>0), the set
$\\{n\le x: f(n)\ge \varepsilon \log x\\}$ has size (O(x/\log x)), hence density $0$. So **(f(n)=o(\log n)) holds for “almost all” $n$** in a density sense, but that is far weaker than the pointwise conjecture you asked.

### Even the “maximal” extreme case is out of reach

A very strong way for the conjecture to fail would be if there were infinitely many $n$ for which **every** $n-2^k$ (with (2^k<n)) is prime, which would force (f(n)\asymp \log n). Erdős already highlighted that we cannot even rule this out; he conjectured only finitely many such $n$ and listed the known small examples. ([Erdős Problems][1])

There are strong upper bounds on how many such “all shifts prime” $n$ can occur up to $N$ (Vaughan 1973, and generalizations), but these bounds are still far from proving finiteness. ([Erdős Problems][1])

### Heuristics strongly suggest “yes”

A common probabilistic model is:

* for $n$ around size $N$, you have about (\log_2 N) candidates (n-2^k),
* each behaves “roughly like a random odd integer” near $N$, so
  (\Pr(n-2^k \text{ prime})\approx 1/\log N).

So (\mathbb E[f(n)]\approx (\log_2 N)\cdot (1/\log N)=1/\log 2), and large deviations suggest the maximum $f(n)$ up to $N$ should be around (\log N/\log\log N), which is (o(\log N)). This matches the informal consensus that the conjecture is true, but proving anything close to the needed “prime‑pattern” upper tails when the pattern size grows like (c\log N) is beyond current sieve technology.

---

**Bottom line:** As of the latest references above, **it is not known** whether (f(n)=o(\log n)) holds; it remains an open Erdős problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/236 "
  
    Erdős Problem #236
  
"

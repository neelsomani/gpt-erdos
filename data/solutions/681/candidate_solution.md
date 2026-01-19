This is **currently unknown** (open).

In fact, your exact question appears as **Erdős Problem #681** and is listed as **OPEN**:

> “Is it true that for all large $n$ there exists $k$ such that $n+k$ is composite and (p(n+k)>k^2)?” ([Erdős Problems][1])

### A couple of useful remarks

* If $n+1$ is composite, then $k=1$ works immediately, since (p(n+1)\ge 2>1^2). So the only “hard” cases are essentially (n=p-1) with $p$ prime [[nomath]](where $k=1$ is impossible)[[/nomath]].

* If $n+k$ is composite then (p(n+k)\le \sqrt{n+k}). Hence (p(n+k)>k^2) forces
  [
  k^2 < \sqrt{n+k}\quad\Rightarrow\quad k^4 < n+k,
  ]
  so any search for $k$ only needs to go up to about (k\lesssim (n+k)^{1/4}). This observation is explicitly noted in OEIS discussions of the problem. ([OEIS][2])

### Computational evidence

OEIS sequence **A389680** records integers $n$ for which **no** (k>1) works [[nomath]](i.e., there is no $i>1$ with $n+i$ composite and $\operatorname{lpf}(n+i)>i^2$)[[/nomath]]. It comments that the “density decreases” and that it is **conjectured the sequence is finite**, i.e. that beyond some point every $n$ *does* have such a $k$. ([OEIS][2])
But this remains unproved.

### Related context

A closely related Erdős problem (#680) asks [[nomath]](without requiring “$n+k$ composite”)[[/nomath]] whether one can always find $k$ with (p(n+k)>k^2+1). The site notes that this follows from “plausible assumptions” about primes, but is also open unconditionally. ([Erdős Problems][3])

So: **no proof is known, and no unconditional counterexample is known**; it’s an open Erdős-type question. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/681 "
  
    Erdős Problem #681
  
"
[2]: https://oeis.org/A389680 "A389680 - OEIS"
[3]: https://www.erdosproblems.com/680 "
  
    Erdős Problem #680
  
"

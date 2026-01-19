This is **exactly Grimm’s conjecture** (posed by C. A. Grimm in 1969), and **it is not proved in general**. ([Wikipedia][1])

What *is* known:

* **Computational verification:** Laishram & Shorey (2006) verified that Grimm’s conjecture holds for **all** such blocks with starting point (n \le 1.9\times 10^{10}) [[nomath]](and all relevant $k$)[[/nomath]]. 
* **Partial theorems for “short” blocks:** There are unconditional results guaranteeing a “prime representation” (distinct prime divisors) for blocks whose length $k$ is at most on the order of (\big(\frac{\log n}{\log\log n}\big)^3) for sufficiently large $n$ (work of Ramachandra–Shorey–Tijdeman, discussed for example in Laishram–Murty). ([Queen's Math & Stats][2])
* **Even a weaker variant remains open:** the weaker statement that the product (\prod_{i=1}^k (n+i)) has at least $k$ distinct prime divisors (under the same “all composite” hypothesis) is also stated as open in the literature. ([Queen's Math & Stats][2])

Why it’s considered hard / why people care:

* If Grimm’s conjecture were true, it would imply very strong consequences about primes—for instance, it implies there is a prime between consecutive squares [[nomath]](i.e. between $m^2$ and $(m+1)^2$)[[/nomath]], which is far beyond what is currently known even assuming the Riemann Hypothesis. ([Queen's Math & Stats][2])

So the direct answer to your question is: **it is conjectured to be true, verified in large ranges and in various partial regimes, but it is still open in full generality.** ([Wikipedia][1])

[1]: https://en.wikipedia.org/wiki/Grimm%27s_conjecture "Grimm's conjecture - Wikipedia"
[2]: https://mast.queensu.ca/~murty/murty-laishram.pdf "4100"

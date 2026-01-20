Not currently known.

Your definition is the standard “well-distributed (mod 1)” condition (uniform equidistribution **in every long block**, uniformly over the starting point). In the literature it is often stated as: for every interval ([a,b]\subset[0,1]),
[
\lim_{N\to\infty}\ \sup_{m\in\mathbb N}\left|\frac{1}{N}|\\{1\le n\le N:\ a\le {s_{n+m}}\le b\\}|;-;(b-a)\right|=0,
]
which is equivalent to your sliding-window formulation with $k=N$ and shift $m=n$. 

## What is known for ({\alpha p_n})

### 1) If (\alpha\in\mathbb Q), then ({\alpha p_n}) is **not** well-distributed (easy)

Write (\alpha=a/q) in lowest terms. Then ({a p_n/q}) can take only values in the finite set ({0,1/q,\dots,(q-1)/q}) (in fact usually fewer). Choose an interval (I\subset[0,1]) of length, say, (|I|<1/q) that avoids this finite set. Then (|\\{n<m\le n+k:\ {a p_m/q}\in I\\}|=0) for every (n,k), while (|I|k) grows linearly with $k$, so your inequality fails for any (\varepsilon<|I|).

So the interesting case is (\alpha) irrational.

### 2) If (\alpha\notin\mathbb Q), then ({\alpha p_n}) is **equidistributed** (Vinogradov), but that does **not** settle well-distribution

Vinogradov proved that for irrational (\alpha), the fractional parts ({\alpha p_n}) are uniformly distributed in $[0,1]$. ([Wikipedia][1])
However, equidistribution of initial segments is much weaker than your “every block of length $k$” requirement.

### 3) It is now known that **some irrational (\alpha)** give **failure** of well-distribution

In 2024, Champagne–Lê–Liu–Wooley proved:

> There exists an **irrational** (\alpha) such that ((\alpha p_n)) is **not** well-distributed modulo $1$. 

Their construction uses Shiu’s theorem that for any modulus $q$ there are arbitrarily long strings of **consecutive** primes all congruent to (1 \pmod q), and then builds a (transcendental) (\alpha) tailored to those congruential strings so that a Weyl-type criterion for well-distribution fails. 

So the weaker statement “there exists an (\alpha) such that ({\alpha p_n}) is not well-distributed” is **true**.

## The question you asked: “for every (\alpha)?”

That universal statement

[
\text{“For every real }\alpha,\ {\alpha p_n}\text{ is not well-distributed.”}
]

is **still open** as of the current literature summaries: it is listed as an open Erdős problem (#997), with the above 2024 result recorded only as establishing *existence* of a bad irrational (\alpha), not the “for all (\alpha)” claim. ([Erdős Problems][2])

So the best-supported answer today is:

* **Yes** for all **rational** (\alpha) (trivial obstruction).
* **There exist** **irrational** (\alpha) for which it fails (Champagne–Lê–Liu–Wooley).
* **Unknown** whether it fails for **every irrational** (\alpha) [[nomath]](and hence for every $\alpha$)[[/nomath]]. ([Erdős Problems][2])

[1]: https://en.wikipedia.org/wiki/Equidistributed_sequence?utm_source=chatgpt.com "Equidistributed sequence"
[2]: https://www.erdosproblems.com/forum/thread/997 "

    Erdős Problem #997 - Discussion thread

"

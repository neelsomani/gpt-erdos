No — and in fact it fails very strongly.

### 1) Pointwise (f(n)=o(n)) is false

This question is listed as Erdős Problem #1054, and the “strong claim” (f(n)=o(n)) has been **disproved**. ([Erdős Problems][1])

What is proved (in comments by Terence Tao to the related Erdős Problem #468 thread) is a **density bound** of the form
[
\frac{|\\{N\le X:\ f(N)/N\le \delta,\\}|}{X}\ \ll\ \delta^2
]
for all (\delta>0). ([Erdős Problems][2])

In words: for small (\delta), **only $O(\delta^2)$ of the integers** have (f(N)\le \delta N). This is incompatible with (f(n)=o(n)), because if (f(n)=o(n)) then for any fixed small (\delta) we would have (f(n)\le \delta n) for *all sufficiently large* $n$, i.e. the set would have density $1$, not $O(\delta^2)$. ([Erdős Problems][2])

### 2) It is **not** true “for almost all $n$” either

The same density estimate immediately rules out any “almost all” version of (f(n)=o(n)): if (f(n)/n\to 0) on a density‑1 set, then for a small fixed (\delta) the set ({n: f(n)\le \delta n}) would have density $1$, contradicting the (\ll \delta^2) upper bound. ([Erdős Problems][2])

A useful reformulation is:

> For any function (g(n)=o(n)), the set ({n:\ f(n)\le g(n)}) has asymptotic density $0$.

[[nomath]](This follows by taking a small constant $\delta$ and using that $g(n)\le \delta n$ for all large $n$.)[[/nomath]]

### 3) What *is* known: (\displaystyle \liminf \frac{f(n)}{n}=0)

Unconditionally, one can get arbitrarily small ratios along a subsequence. The OEIS entry for this function notes the observation (a(\sigma(n))\le n), hence along values (N=\sigma(n)),
[
\frac{f(N)}{N}\ \le\ \frac{n}{\sigma(n)}.
]
Since (\sigma(n)/n) is unbounded [[nomath]](in fact $\limsup \sigma(n)/(n\log\log n)=e^\gamma$)[[/nomath]], this gives (\liminf f(N)/N=0). ([OEIS][3])

### 4) About (\displaystyle \limsup \frac{f(n)}{n})

As far as the sources above indicate, the **(\limsup)** question is still **open** [[nomath]](the problem remains listed open, and no bound on $\limsup f(n)/n$ is given)[[/nomath]]. ([Erdős Problems][1])

There is extensive computation [[nomath]](OEIS includes a plot of $f(n)/n$ up to $10^6$)[[/nomath]], which visually suggests the ratios do not drift toward $0$ and exhibit occasional spikes, but that is experimental evidence only. 

### 5) Minor note: domain issues

It is known that the function is **undefined for $n=2$ and $n=5$**; it is *expected* to be defined for all (n\ge 6) (this would follow from a suitable strong Goldbach-type statement), but that global well-definedness is not currently proven unconditionally. ([Erdős Problems][1])

---

So the answer to your “either/or” is: **neither**. (f(n)=o(n)) is false, and it’s false even “for almost all $n$” in the natural density sense, thanks to the (\ll\delta^2) density bound. The behavior of (\limsup f(n)/n) appears to remain open. ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/1054 "
  
    Erdős Problem #1054
  
"
[2]: https://www.erdosproblems.com/forum/thread/468 "

    Erdős Problem #468 - Discussion thread

"
[3]: https://oeis.org/A167485 "A167485 - OEIS"

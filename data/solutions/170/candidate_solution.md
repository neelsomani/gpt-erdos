Because (N\in A-A) and (A\subset{0,1,\dots,N}), we must have (0\in A) and (N\in A) (the only way to get a difference of $N$ is $N-0$). So this is exactly the “complete sparse ruler of length $N$” problem. ([Wikipedia][1])

Let (F(N)=|A|) be the minimum possible size. A deep theorem of Erdős and Gál says the limit
[
\lim_{N\to\infty}\frac{F(N)^2}{N}
]
exists [[nomath]](so your limit $\lim_{N\to\infty}F(N)/\sqrt N$ also exists)[[/nomath]]. ([Wikipedia][1])

What is *not* known (as of the sources above) is the *exact* value of that limit. The best proven bounds are:

* **Lower bound (Leech):**
  [
  \lim_{N\to\infty}\frac{F(N)^2}{N}\ \ge\ 2.434\ldots
  ]
  so
  [
  \lim_{N\to\infty}\frac{F(N)}{\sqrt N}\ \ge\ \sqrt{2.434\ldots}\ =\ 1.5601\ldots
  ]
  ([Wikipedia][1])

* **Upper bound (Wichmann construction):**
  [
  \lim_{N\to\infty}\frac{F(N)^2}{N}\ \le\ 3,
  ]
  so
  [
  \lim_{N\to\infty}\frac{F(N)}{\sqrt N}\ \le\ \sqrt3\ =\ 1.73205\ldots
  ]
  ([Wikipedia][1])

So the best honest answer is:
[
\boxed{\text{The limit exists, but its exact value is not currently proved; it lies in }[1.5601\ldots,\ \sqrt3].}
]
([Erdős Problems][2])

Many computations suggest the true value might be (\sqrt3), but that is a conjecture, not a proved theorem. ([Erdős Problems][2])

[1]: https://en.wikipedia.org/wiki/Sparse_ruler "Sparse ruler - Wikipedia"
[2]: https://www.erdosproblems.com/170 "
  
    Erdős Problem #170
  
"

Unconditionally: **we don’t know**. The convergence of
[
\sum_{n=1}^{\infty}(-1)^n\frac{n}{p_n}
]
[[nomath]](where $p_n$ is the $n$-th prime)[[/nomath]]s an **open problem of Erdős**. 

What is known:

* **It is not absolutely convergent.** By the prime number theorem (p_n\sim n\log n), so (\frac{n}{p_n}\sim \frac1{\log n}), and (\sum_{n\ge 2}\frac{1}{\log n}) diverges [[nomath]](it grows like $N/\log N$)[[/nomath]]. So only *conditional* convergence is even possible. 

* **The usual alternating series test does not apply.** Leibniz requires the magnitudes (\frac{n}{p_n}) to be eventually decreasing, but they are not: fluctuations in prime gaps (p_{n+1}-p_n) create non-monotonicity, and the whole issue becomes whether there is any *systematic bias* in those fluctuations depending on the parity of $n$. ([What's new][1])

* **A reformulation ties it to the parity of (\pi(x)).** Tao records (following an observation of Said) that the convergence of your series is equivalent to the convergence of
  [
  \sum_{m=2}^{\infty}\frac{(-1)^{\pi(m)}}{m\log m},
  ]
  so it boils down to understanding cancellation/equidistribution properties of ((-1)^{\pi(m)}) at a strength beyond what is currently proved. 

* **Conditional result (assuming a strong conjecture).** Tao proved that the series **does converge** assuming a sufficiently strong *quantitative* form of the Hardy–Littlewood prime tuples conjecture. 

Numerically, the partial sums appear to settle very slowly (Tao reports a numerical limit around $-0.052161$). 

So the honest answer is: **it is widely believed to converge, and it does under strong prime-tuple conjectures, but no unconditional proof (or disproof) is known.** 

[1]: https://terrytao.wordpress.com/2023/08/14/the-convergence-of-an-alternating-series-of-erdos-assuming-the-hardy-littlewood-prime-tuples-conjecture/ "The convergence of an alternating series of Erdős, assuming the Hardy–Littlewood prime tuples conjecture | What's new"

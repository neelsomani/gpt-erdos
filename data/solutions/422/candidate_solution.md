Your recurrence is the **Hofstadter $Q$-sequence** (OEIS **A005185**), sometimes called Hofstadter’s original “$Q$” or “$U$” sequence:
[
Q(1)=Q(2)=1,\qquad Q(n)=Q\bigl(n-Q(n-1)\bigr)+Q\bigl(n-Q(n-2)\bigr)\ \ (n>2).
]
([OEIS][1])

## Does it miss infinitely many integers?

**This is not known.** In fact, even more basic questions are open: it is *not proved* that the sequence is well-defined for all $n$ [[nomath]](i.e. that it never “dies” by trying to access $Q(0)$ or $Q(\text{negative})$)[[/nomath]]. ([Erdős Problems][2])

What *is* known (computationally) is that it has been checked extremely far without dying: OEIS reports computations showing $Q(n)$ exists up to (n\le 3\cdot 10^{10}). ([OEIS][1])

As for “missing values”: **Hofstadter believed** (based on computational evidence) that *infinitely many values are omitted*, but this has not been proved. Pinn reports this explicitly as a belief supported by evidence, not a theorem. ([arXiv][3])

A small, concrete data point (just to illustrate the phenomenon): in a direct computation of the first (200{,}000) terms, the smallest positive integers that do **not** appear among ({Q(1),\dots,Q(200000)}) include
[
7,\ 13,\ 15,\ 18,\ 27,\ 29,\ 34,\ 36,\dots
]
This **does not** prove they never appear later, but it matches the widespread experimental picture that the range is “holey.”

## What is its behavior?

### 1) “Chaotic locally, structured globally”

This is the standard description in the literature: on short scales it looks erratic, but on large scales there is visible structure. ([arXiv][3])

A famous early segment is
[
1,1,2,3,3,4,5,5,6,6,6,8,8,8,10,9,10,11,11,12,\dots
]
and you can already see non-monotonicity at (Q(16)=9<10=Q(15)). ([arXiv][3])

### 2) Roughly linear growth around $n/2$ $conjectural/empirical$

Plots and statistics strongly suggest the “main trend” is
[
Q(n)\approx \frac n2,
]
with sizable fluctuations. Fox’s paper summarizes this common observation [[nomath]](“close to $n/2$” with fractal-ish structure in plots)[[/nomath]] and emphasizes that a proof is unknown. ([arXiv][4])

Pinn studies the centered quantity
[
S(n)=Q(n)-\frac n2
]
and reports a scaling law for the size of fluctuations when averaged over “generations,” with an exponent about (\alpha\approx 0.88) (again: an empirical/statistical finding, not a fully rigorous asymptotic theorem). ([arXiv][3])

### 3) “Generations” (an observed hierarchical structure)

A striking empirical regularity is that the indices can be grouped into **generations**, where:

* the $k$-th generation has about (2^k) members, and
* the two “parents” used to build a term in generation $k$ lie overwhelmingly in generation $k-1$ and occasionally in $k-2$. ([arXiv][3])

This is one of the main “macro-structures” people mean when they say the sequence has order at large scales.

### 4) Early “bursts” at (n=3,6,12,24,\dots)

Pinn points out very regular early “bursts” in $S(n)$ at
[
n=3,6,12,24,48,96,\dots
]
(the doubling pattern). ([arXiv][3])
In direct computation one indeed sees (Q(3)=2,\ Q(6)=4,\ Q(12)=8,\ Q(24)=16,\dots) for quite a while; then later the perfect doubling pattern breaks (Pinn notes the strict regularity breaks around the onset of later generations). ([arXiv][3])

## Bottom line

* Your $f(n)$ is the classical **Hofstadter $Q$-sequence**. ([OEIS][1])
* **Infinitely many missed integers?** Unknown; Hofstadter (and later authors) report strong experimental evidence and belief that infinitely many values are omitted, but there is no proof. ([arXiv][3])
* **Behavior:** seems roughly linear around $n/2$ with complicated fluctuations; exhibits an empirical “generational” organization and other large-scale statistical regularities, despite looking chaotic locally. ([arXiv][3])
* Even the foundational question “is it defined for all $n$?” is open, though checked computationally up to (3\cdot 10^{10}). ([OEIS][1])

If you want, I can also summarize the main *variants* (Tanny/Conolly-type recurrences) where one can actually prove “hits every integer” and monotonicity—those are often studied precisely because the original $Q$ is so resistant. ([ar5iv][5])

[1]: https://oeis.org/A005185/internal "https://oeis.org/A005185/internal"
[2]: https://www.erdosproblems.com/422 "https://www.erdosproblems.com/422"
[3]: https://arxiv.org/pdf/chao-dyn/9803012 "https://arxiv.org/pdf/chao-dyn/9803012"
[4]: https://arxiv.org/pdf/1807.01365 "https://arxiv.org/pdf/1807.01365"
[5]: https://ar5iv.org/abs/2311.13854 "https://ar5iv.org/abs/2311.13854"

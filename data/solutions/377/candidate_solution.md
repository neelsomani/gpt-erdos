Let
[
f(n):=\sum_{p\le n}\mathbf 1_{,p\nmid \binom{2n}{n}}\frac1p .
]

As far as I can tell from the literature that is currently indexed/summarized online, **it is not known** whether (\sup_n f(n)<\infty). In particular, this is listed as **Erdős Problem #377 (OPEN)**, attributed to Erdős–Graham–Ruzsa–Straus. ([Erdős Problems][1])

A useful exact criterion (essentially Kummer/Lucas) is:

* Write (n=\sum_{k\ge0} a_k p^k) in base $p$ with (0\le a_k<p). Then
  [
  p\nmid \binom{2n}{n}\quad\Longleftrightarrow\quad a_k<\frac p2\ \text{ for every digit }a_k,
  ]
  equivalently, **there are no carries when adding $n+n$ in base $p$**. ([SciSpace][2])

### What is known about $f(n)$

Erdős–Graham–Ruzsa–Straus proved strong *average-case* information:

* The mean value exists and equals an explicit constant
  [
  \lim_{x\to\infty}\frac1x\sum_{n\le x} f(n)
  =\sum_{k=2}^\infty \frac{\log k}{2^k}
  ;=:;\gamma_0\approx 0.5078339229,
  ]
  and the second moment satisfies
  [
  \lim_{x\to\infty}\frac1x\sum_{n\le x} f(n)^2=\gamma_0^2,
  ]
  so in particular (f(n)=\gamma_0+o(1)) for “almost all” integers $n$. ([Erdős Problems][1])

They also proved a nontrivial *worst-case* upper bound:

* For all sufficiently large $n$,
  [
  f(n)\le c\log\log n
  \quad\text{for some absolute }c<1,
  ]
  improving the trivial Mertens-type bound (f(n)\le (1+o(1))\log\log n). ([Erdős Problems][1])

But the central question you asked—**whether $f(n)$ is bounded by an absolute constant**—remains open in these sources. The original paper explicitly remarks that they could not decide whether $f(n)$ is unbounded. ([SciSpace][2])

### Why this is a subtle “uniform” problem

The average result says $f(n)$ is typically ~$0.508$, but that does not rule out rare $n$ for which $f(n)$ is much larger. Making $f(n)$ large requires arranging the “no-carry in base $p$” condition simultaneously for many primes $p$, and controlling that kind of *simultaneous digit restriction in many bases* is exactly where the difficulty lies. (EGRS already point out that extending their two-base constructions to three or more bases seems to require new ideas.) ([SciSpace][2])

So the honest answer is:

* **No proof is currently known (in the referenced literature) that such a universal constant $C$ exists, nor is there a proof that $f(n)$ is unbounded.** ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/377 "
  
    Erdős Problem #377
  
"
[2]: https://scispace.com/pdf/on-the-prime-factors-of-n-4yti4z6llw.pdf "On the prime factors of (²ⁿ_{})"

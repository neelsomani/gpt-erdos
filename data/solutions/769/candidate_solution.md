Let $D(n)$ be the set of integers $k$ for which the unit $n$-cube can be tiled (decomposed) into $k$ smaller **homothetic** $n$-cubes, and let $c(n)$ be the least integer such that all (k\ge c(n)) lie in $D(n)$.

## What is known (best current general bounds)

### Existence of $c(n)$

It is known that $c(n)$ exists for every $n$: beyond some threshold, *every* sufficiently large $k$ occurs. One route to this finiteness is via the [[nomath]](nontrivial, for $n\ge3$)[[/nomath]] arithmetic structure of cube tilings; in particular, Dehn’s theorem implies strong rationality constraints in higher dimensions. ([ResearchGate][1])

### Lower bounds

Hadwiger proved a general exponential lower bound
[
c(n)\ \ge\ 2^n+2^{n-1},
]
and Connor–Marmorino (2018) improved this to
[
c(n)\ \ge\ 2^{,n+1}-1\qquad (n\ge 3).
]
([Erdős Problems][2])

So the best *general* lower bound is only **exponential** in $n$.

### Upper bounds

The best general *quantitative* upper bounds currently come from Connor–Marmorino (2018):

* If $n+1$ is **not prime**, then
  [
  c(n)\ \le\ e^{2}n^{n}\ \approx\ 7.389,n^{n}.
  ]
* If $n+1$ **is prime**, then
  [
  c(n)\ \le\ 1.8n^{n+1}.
  ]
  ([DOI][3])

For comparison, an earlier (much weaker) explicit bound of Erdős was of size roughly (2^n(n+1)^n):
[
c(n)\ \le\ (2^n-2)\big((n+1)^n-2\big)-1.
]
([Department of Mathematics ETH][4])

Putting the modern best bounds together [[nomath]](for $n\ge3$)[[/nomath]]:
[
2^{n+1}-1\ \le\ c(n)\ \le\
\begin{cases}
e^2n^n,& n+1\text{ composite},[2mm]
1.8,n^{n+1},& n+1\text{ prime}.
\end{cases}
]
([DOI][3])

## Small dimensions (for calibration)

* (c(2)=6) [[nomath]](equivalently, the largest non-tileable $k$ for squares is $5$)[[/nomath]]. ([arXiv][5])
* In 3D, many sources treat “47” as the threshold in the “(>)” formulation [[nomath]](i.e. all $k>47$ work)[[/nomath]], which corresponds to (c(3)=48) in your “(\ge)” formulation, and Prather’s survey states the cube case is known to be 47 in that sense. ([arXiv][5])
* For 4D (“tesseracts”), Prather gives (h(4)\le 733) in the “all (k>h(4))” formulation, i.e. $c(4)\le 734$ under your convention. ([arXiv][5])

[[nomath]](Exact values beyond $n=2$ are largely unknown; even in 3D the sharp status has historically been tricky in the literature.)[[/nomath]]

## About the question (c(n)\gg n^n)

This is **open** in the strong asymptotic sense you ask: no lower bound anywhere near (n^n) is currently proved. The best general lower bound is (c(n)\ge 2^{n+1}-1), which is vastly smaller than (n^n) for large $n$. ([DOI][3])

There is, however, a famous remark of Erdős suggesting that the “prime case” might force $c(n)$ to be large:

> Erdős wrote: “I am certain that if $n+1$ is a prime then (c(n)>n^n).” ([Erdős Problems][2])

But at present this remains conjectural; in particular, **no** (\Omega(n^n)) lower bound is known even along the subsequence (n=p-1) with $p$ prime.

### Why (n^n) shows up naturally

Very roughly, the known proofs that $c(n)$ is finite exploit “closure” operations on cube tilings [[nomath]](e.g. refining one tile into $m^n$ smaller cubes, which changes the count by $m^n-1$)[[/nomath]], together with number theory to ensure one can hit all sufficiently large integers. The arithmetic can behave differently when $n+1$ is prime (a phenomenon visible in the different upper bounds), which is consistent with Erdős’s intuition, but it has not yet yielded a matching large lower bound. ([DOI][3])

## Bottom line

* Best known general lower bound:
  [
  c(n)\ge 2^{n+1}-1\quad (n\ge3).
  ]

* Best known general upper bounds (Connor–Marmorino):
  [
  c(n)\le e^2 n^n\ \text{ if } n+1\text{ composite},\qquad
  c(n)\le 1.8,n^{n+1}\ \text{ if } n+1\text{ prime}.
  ]
  ([DOI][3])

* Whether (c(n)\gg n^n) [[nomath]](or even $c(n)\ge c,n^n$ for some absolute $c>0$)[[/nomath]] is **not known**; Erdős explicitly conjectured (c(n)>n^n) when $n+1$ is prime. ([Erdős Problems][2])

[1]: https://www.researchgate.net/publication/323992295_Decomposing_cubes_into_smaller_cubes "Decomposing cubes into smaller cubes | Request PDF"
[2]: https://www.erdosproblems.com/769 "https://www.erdosproblems.com/769"
[3]: https://doi.org/10.1007/s00022-018-0424-4 "https://doi.org/10.1007/s00022-018-0424-4"
[4]: https://www2.math.ethz.ch/EMIS/classics/Erdos/cit/31310045.htm "https://www2.math.ethz.ch/EMIS/classics/Erdos/cit/31310045.htm"
[5]: https://arxiv.org/pdf/1910.06206 "https://arxiv.org/pdf/1910.06206"

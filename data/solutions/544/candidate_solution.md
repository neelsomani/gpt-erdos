Let
[
\Delta_k:=R(3,k+1)-R(3,k)\qquad(k\ge 2).
]

## What is known (and why your two questions are hard)

Both of your questions are exactly the **Erdős–Sós problem (1980)** for the off–diagonal Ramsey numbers $R(3,k)$: they asked whether
[
\Delta_k \xrightarrow[k\to\infty]{}\infty
\quad\text{and whether}\quad
\frac{\Delta_k}{k}\xrightarrow[k\to\infty]{}0.
]
This is stated explicitly in Zhu–Xu–Radziszowski (“A step forwards on the Erdős–Sós problem…”) as the open problem [[nomath]](their display $5$)[[/nomath]]. ([arXiv][1])

Moreover, the same paper emphasizes that even for “consecutive” values $R(3,s)$ and $R(3,s-1)$, in general **only very crude bounds are known**:
[
3\le \Delta_s \le s.
]
([arXiv][1])

So:

* **Your first statement** (\Delta_k\to\infty) is **open** (not proved or disproved).
* **Your second statement** (\Delta_k=o(k)) is **also open** (not proved or disproved). ([arXiv][1])

That said, there are meaningful *weaker* statements we can prove from the known asymptotics of $R(3,k)$.

---

## Known asymptotics of $R(3,k)$

It is “quite well understood” that
[
\left(\frac14+o(1)\right)\frac{k^2}{\log k}\le R(3,k)\le\left(1+o(1)\right)\frac{k^2}{\log k},
]
as quoted in Zhu–Xu–Radziszowski. ([arXiv][1])

[[nomath]](And there has been recent progress improving the *lower* constant: Hefty–Horn–King–Pfender $2025$ prove
$
R(3,k)\ge \left(\frac12+o(1)\right)\frac{k^2}{\log k},
$
improving earlier $\frac13$ and $\frac14$ constants. ([arXiv][2])
This does **not** settle the consecutive-difference questions, but it’s relevant context.)[[/nomath]]

---

## What you *can* prove today about (\Delta_k)

### 1) You cannot currently prove (\Delta_k\to\infty), but you can prove (\limsup \Delta_k=\infty)

**Claim (provable):** (\Delta_k) is **unbounded**, i.e.
[
\limsup_{k\to\infty}\Delta_k=\infty.
]

**Proof.** Suppose (\Delta_k) were bounded: there exist $M$ and $K$ such that (\Delta_k\le M) for all (k\ge K). Then for (n>K),
[
R(3,n)=R(3,K)+\sum_{k=K}^{n-1}\Delta_k \le R(3,K)+M(n-K)=O(n).
]
But the known lower bound (R(3,n)\ge c,n^2/\log n) for some fixed (c>0) contradicts linear growth. [[nomath]](For example, $c=1/4$ works from the quoted asymptotics.)[[/nomath]] ([arXiv][1])
Hence no such uniform $M$ exists, so (\Delta_k) is unbounded. ∎

So we **can** show: (\Delta_k) takes arbitrarily large values, but this does **not** imply (\Delta_k\to\infty) (it could spike and dip infinitely often).

### 1b) A stronger “spikes must happen” statement: (\Delta_k) is (\Omega(k/\log k)) infinitely often

Using the two-sided bounds [[nomath]](with constants $c>0$, $C>0$)[[/nomath]], you can force large increments on some step in a long interval.

Fix (t>1) large enough that (c t^2>C). Then for large $k$,
[
R(3,\lfloor tk\rfloor)-R(3,k)
\ge
\left(c+o(1)\right)\frac{t^2k^2}{\log (tk)}
-------------------------------------------

\left(C+o(1)\right)\frac{k^2}{\log k}
=\Omega!\left(\frac{k^2}{\log k}\right).
]
There are [[nomath]](\lfloor tk\rfloor-k=\Theta$k$)[[/nomath]] consecutive differences in that interval, so at least one of them satisfies
[
\Delta_j \ge \Omega\left(\frac{k}{\log k}\right),
]
hence (\Delta_j\to\infty) along an infinite subsequence.

This again falls short of (\Delta_k\to\infty), but it shows the differences must sometimes be as large as the “expected” scale (k/\log k).

---

## 2) About (\Delta_k=o(k)): open, but you can prove (\liminf \Delta_k/k=0)

The statement (\Delta_k=o(k)) means (\Delta_k/k\to 0). This is open [[nomath]](it’s the second question in $5$)[[/nomath]]. ([arXiv][1])

However you can prove the weaker fact:

**Claim (provable):**
[
\liminf_{k\to\infty}\frac{\Delta_k}{k}=0.
]
Equivalently: for every (\varepsilon>0), there are infinitely many $k$ with (\Delta_k<\varepsilon k).

**Proof.** Suppose not. Then for some (\varepsilon>0) there exists $K$ such that (\Delta_k\ge \varepsilon k) for all (k\ge K). Summing gives
[
R(3,n)
=R(3,K)+\sum_{k=K}^{n-1}\Delta_k
\ge R(3,K)+\varepsilon\sum_{k=K}^{n-1}k
\ge c' \varepsilon,n^2
]
for some constant (c'>0). But the known upper bound (R(3,n)\le (1+o(1))n^2/\log n) is $o(n^2)$, contradiction. ([arXiv][1])
Therefore, no fixed (\varepsilon>0) can lower-bound (\Delta_k/k) eventually, so (\liminf \Delta_k/k=0). ∎

So (\Delta_k) is **sublinear infinitely often**, but that still doesn’t prove it’s sublinear for *all* large $k$.

---

## Current status summary

* **$A$** (\Delta_k\to\infty) is **open** (Erdős–Sós 1980). ([arXiv][1])
  What you *can* prove: (\Delta_k) is unbounded; even (\Delta_k=\Omega(k/\log k)) for infinitely many $k$.

* **$B$** (\Delta_k=o(k)) is **open** (also Erdős–Sós 1980). ([arXiv][1])
  What you *can* prove: (\liminf \Delta_k/k=0), i.e. (\Delta_k=o(k)) holds along an infinite subsequence.

If you want, I can also sketch how Zhu–Xu–Radziszowski relate (\Delta_s/s\to 0) to a “bounded drop” conjecture (\Delta_s-\Delta_{s+1}\le d) (they prove this implication). ([arXiv][1])

[1]: https://arxiv.org/pdf/1507.01133 "https://arxiv.org/pdf/1507.01133"
[2]: https://arxiv.org/pdf/2510.19718 "Improving $R(3,k)$ in just two bites"

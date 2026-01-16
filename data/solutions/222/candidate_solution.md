Let
[
\mathcal S={n\ge 0:\ n=a^2+b^2\text{ for some }a,b\in\mathbb Z},\qquad
n_1<n_2<\cdots
]
be the increasing enumeration of (\mathcal S), and set the gaps
[
g_k:=n_{k+1}-n_k,\qquad
g(X):=\max_{n_{k+1}\le X}(n_{k+1}-n_k).
]

A basic structural fact (Fermat’s two–squares theorem) is that (n\in\mathcal S) iff in the prime factorization of $n$, every prime (p\equiv 3\pmod 4) occurs with an **even** exponent. ([MPG.PuRe][1])
So “being in (\mathcal S)” is a sieve-type condition: to *exclude* $n$, it suffices to force some (p\equiv 3\pmod4) to divide $n$ to an odd power.

## Typical size: average gaps are about (\sqrt{\log n})

Let
[
B(x):=#\\{n\le x: n\in\mathcal S\\}.
]
Landau (1908) proved the Landau–Ramanujan asymptotic
[
B(x)\sim K\frac{x}{\sqrt{\log x}}
\quad (x\to\infty),
]
where (K\approx 0.76422) is the Landau–Ramanujan constant. ([MPG.PuRe][1])

This implies that the *mean spacing* of sums of two squares near $x$ is of order
[
\frac{x}{B(x)}\asymp \sqrt{\log x}.
]
More refined results (via moments of gaps) show that for “most” indices $k$, one indeed has (g_k) no larger than a constant multiple of (\sqrt{\log n_k}) (up to slowly growing factors). For example, Kalmynin quotes Hooley-type moment bounds implying that for almost all (n), (s_{n+1}-s_n\ll \sqrt{\log s_n}). ([arXiv][2])

So (\sqrt{\log}) is the “normal” scale; the interesting part of the problem is how big the *exceptional* gaps can get, and how small the gaps can be.

## Small gaps: (\liminf g_k = 1)

Gaps of size $1$ occur infinitely often:
[
m^2 = m^2+0^2,\qquad m^2+1 = m^2+1^2
]
are consecutive integers, hence consecutive terms in the ordered list (\mathcal S) for every $m$. Therefore
[
\liminf_{k\to\infty}(n_{k+1}-n_k)=1.
]

## A uniform upper bound: (g_k \ll n_k^{1/4})

The best known *worst-case* upper bound (still essentially the classical one) is
[
g(X)\ll X^{1/4},
\quad\text{equivalently}\quad
n_{k+1}-n_k \ll n_k^{1/4}.
]

A very clean way to see the (X^{1/4}) comes from the Bambah–Chowla method as presented by Shiu. Given $n$, take
[
u=\lfloor \sqrt n\rfloor,\qquad r=n-u^2\ (<2\sqrt n),\qquad v=\left\lceil \sqrt r\right\rceil.
]
Then (u^2+v^2\ge n), and one checks
[
u^2+v^2 < n + 2\sqrt r +1 \le n + 2\sqrt2,n^{1/4}+1.
]
So **every** interval ([n,;n+2\sqrt2,n^{1/4}+1)) contains a sum of two squares, which forces the maximal gap to be (O(n^{1/4})). 

It is a major open problem to improve the exponent $1/4$ unconditionally; Shiu notes that even improving the constant is difficult and that the exponent has resisted improvement for decades. 
(There are conjectures predicting much smaller maximal gaps, discussed below.)

## Large gaps: (g_k) is unbounded, and in fact (\gtrsim \log n_k) infinitely often

### Elementary construction: arbitrarily long gaps exist

Because of the “odd exponent of a (3\bmod4) prime” obstruction, you can force long blocks of consecutive integers to lie outside (\mathcal S) via congruences.

For any $L$, pick distinct primes (q_1,\dots,q_L\equiv 3\pmod4). By the Chinese remainder theorem you can choose $A$ such that, for each (1\le j\le L),
[
A+j \equiv q_j \pmod{q_j^2},
]
so (q_j\mid (A+j)) but (q_j^2\nmid (A+j)), i.e. $q_j$ divides $A+j$ to an odd exponent. Hence none of (A+1,\dots,A+L) is a sum of two squares. This proves (\sup_k g_k=\infty).

Quantitatively, this simple CRT construction already gives gaps of length about (\frac{\log X}{\log\log X}) below size $X$ [[nomath]](because the modulus you build is roughly the square of a product of $L$ primes, so $\log X$ is about $L\log L$)[[/nomath]].

### Best known lower bounds: gaps (\ge c\log X) infinitely often

Much stronger results are known: there are infinitely many gaps **linear in (\log)**.

A convenient way to package it is via $g(X)$. The current record (as of the Dietmann–Elsholtz–Kalmynin–Konyagin–Maynard work and also independently stated by Kalmynin–Konyagin) is:
[
g(X)\ \ge\ \left(\frac{390}{449}-o(1)\right)\log X
\qquad (X\to\infty),
]
so for infinitely many $k$,
[
n_{k+1}-n_k \ \ge\ \left(\frac{390}{449}-o(1)\right)\log n_k
\approx (0.8686-o(1))\log n_k.
]


Historically, Richards proved the earlier landmark bound
[
\limsup_{k\to\infty}\frac{n_{k+1}-n_k}{\log n_k}\ge \frac14,
]
and the later work improves that constant to (390/449). 
The same sources also discuss earlier lower bounds of the shape (\frac{\log x}{(\log\log x)^{1/2}}) (Erdős/Warlimont) and (\frac{\log x}{\log\log x}) (Turán). 

So, summarizing the *worst-case* growth currently proved:
[
(0.8686-o(1))\log X\ \le\ g(X)\ \ll\ X^{1/4}.
]

## How to reconcile “typical (\sqrt{\log})” with “exceptional (\log)”?

The Landau–Ramanujan theorem says sums of two squares have density (\asymp 1/\sqrt{\log x}), suggesting typical gaps (\asymp \sqrt{\log x}). ([MPG.PuRe][1])
But sieve sets often show strong *irregularities* in short intervals: Balog–Wooley proved there are infinitely many short intervals with far **more** and far **fewer** sums of two squares than the average prediction. ([Cambridge University Press & Assessment][3])
Maynard also proved the existence of short intervals $[x,x+y]$ containing (\gg y^{1/10}) sums of two squares, far above average in certain ranges of $y$. ([arXiv][4])

These results align with the picture:

* Most gaps are around (\sqrt{\log}) (and moment bounds support this). ([arXiv][2])
* But there are rare, structured intervals where congruence obstructions wipe out *all* candidates, giving much larger gaps of order (\log). 

## Open ends and conjectural picture

A natural distance-to-(\mathcal S) function is
[
R(x)=\min_{n\in\mathcal S}|x-n|.
]
The known uniform bound (R(x)\ll x^{1/4}) is “ancient” and not improved; Kalmynin records it and notes it remains unknown whether (R(x)=o(x^{1/4})). ([arXiv][2])
He also states the conjecture that (R(x)\ll_\varepsilon x^\varepsilon) for every (\varepsilon>0), i.e. maximal gaps are subpolynomial. ([arXiv][2])
Meanwhile, the DEKKM paper remarks that a Cramér-type random model would suggest $g(X)$ might be on the order of ((\log X)^{3/2}), but this is heuristic. 

## Takeaway bounds for (n_{k+1}-n_k)

Letting (\log) be the natural logarithm:

* **Infinitely often tiny:** (n_{k+1}-n_k=1) infinitely often (e.g. (m^2,m^2+1)).
* **Typical scale:** average/“most” gaps are (\asymp \sqrt{\log n_k}). ([MPG.PuRe][1])
* **Infinitely often large:** (n_{k+1}-n_k \ge (390/449-o(1))\log n_k) infinitely often. 
* **Always (best known):** (n_{k+1}-n_k \ll n_k^{1/4}) [[nomath]](in fact one can produce a sum of two squares in $[n,;n+2\sqrt2,n^{1/4}+1)$)[[/nomath]]. 

If you want, I can also translate these into bounds in terms of $k$ [[nomath]](using $n_k\sim (k/K)\sqrt{\log k}$ from Landau–Ramanujan)[[/nomath]] and discuss what the best-known results say about the distribution of the normalized gaps (g_k/\sqrt{\log n_k}).

[1]: https://pure.mpg.de/pubman/item/item_3610649_5/component/file_3671435/Berndt-Moree_Sums%2Bof%2Btwo%2Bsquares%2Band%2Bthe%2Btau-function_2025.pdf "Sums of two squares and the tau-function: Ramanujan’s trail"
[2]: https://arxiv.org/pdf/1706.07380 "Intervals between numbers that are sums of two squares"
[3]: https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/sums-of-two-squares-in-short-intervals/7C093B8E6F356E6E426FCA77FD737F1F "Sums of Two Squares in Short Intervals | Canadian Journal of Mathematics | Cambridge Core"
[4]: https://arxiv.org/abs/1910.13384 "[1910.13384] Sums of two squares in short intervals"

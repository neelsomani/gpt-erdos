What you wrote is (as far as I can tell from the current literature) **an open Erdős–Sós–type extremal problem**, listed as **Erdős Problem #865**. In particular, the existence of an absolute constant $C$ making the (\frac58N+C) threshold work for all sufficiently large $N$ is *not known* at present. ([Erdős Problems][1])

## Why (\tfrac58) is believed to be the right constant (sharpness example)

There is a standard construction showing that (\tfrac58) would be best possible (up to an additive constant).

For simplicity assume (8\mid N). Define
[
A = {N/8+1,\dots,N/4}\ \cup\ {N/2+1,\dots,N}.
]
Then
[
|A|=\left(\frac N4-\frac N8\right)+\frac N2=\frac N8+\frac N2=\frac{5N}{8}.
]

**Claim:** This $A$ contains **no** distinct (a,b,c\in A) with (a+b,a+c,b+c\in A).

**Reason:** If (a\in A) lies in the upper half $(N/2,N]$, then for any positive (b\ge 1) we have (a+b>N), so (a+b\notin {1,\dots,N}), hence cannot be in $A$. Therefore any valid triple (a,b,c) must lie in the *lower* part $[N/8+1,N/4]$.

But if (a,b\in[N/8+1,N/4]), then
[
a+b \ge 2(N/8+1)=N/4+2 > N/4,
\quad\text{and}\quad
a+b \le N/4+N/4 = N/2.
]
So $a+b\in (N/4,N/2]$, which is **not** in $A$ [[nomath]](since $A$ includes only $\le N/4$ from the lower region and $\ge N/2+1$ from the upper region)[[/nomath]]. Hence (a+b\notin A), and similarly for $a+c$ and $b+c$.

So (|A|=5N/8) is achievable **without** the desired configuration, meaning any “always-works” threshold cannot be below (5N/8+O(1)). This construction is exactly the one cited in the discussion of the problem. ([Erdős Problems][1])

## What *is* known [[nomath]](known upper bounds, but far from $\tfrac58$)[[/nomath]]

A convenient way to phrase the problem is via the extremal function (f_3(N)): the smallest number such that every (A\subseteq{1,\dots,N}) with (|A|\ge f_3(N)) must contain distinct (a,b,c\in A) with (a+b,a+c,b+c\in A). Erdős and Sós conjectured the asymptotic formula
[
f_k(N)\sim \frac12\left(1+\sum_{r=1}^{k-2}\frac{1}{4^r}\right)N,
]
which for $k=3$ gives (f_3(N)\sim \frac58N). ([Erdős Problems][1])

However, the best general published bounds that are mentioned in the standard references are **much weaker** than (\frac58N). In particular, Choi–Erdős–Szemerédi (1975) proved that for every (k\ge 3) there is an (\varepsilon_k>0) such that for sufficiently large $N$,
[
f_k(N)\le \left(\frac23-\varepsilon_k\right)N,
]
and thus for $k=3$ one gets a guarantee strictly below (\tfrac23N), but still not down to (\tfrac58N). ([Erdős Problems][1])

## Bottom line

* The constant (\tfrac58) is **supported by a matching lower-bound construction** (so it’s plausibly sharp). ([Erdős Problems][1])
* The statement you wrote [[nomath]](existence of an absolute $C$ giving the $\tfrac58N+C$ threshold for all large $N$)[[/nomath]] is **currently open** as a general theorem. ([Erdős Problems][1])
* The best cited general upper bounds in the standard discussion are of the form ((\tfrac23-\varepsilon)N), leaving a nontrivial gap between (\tfrac58) and current proofs. ([Erdős Problems][1])

If you want, I can also:

* explain the “folklore” $k=2$ case [[nomath]](why $|A|\ge N+2$ in ${1,\dots,2N}$ forces $a,b,a+b\in A$)[[/nomath]],
* or sketch the kinds of combinatorial/additive tools people try for $k=3$ (sum-graphs, triangle-free structure, stability heuristics), and why the (\tfrac58) barrier is hard.

[1]: https://www.erdosproblems.com/forum/discuss/865 "

    Erdős Problem #865 - Discussion thread

"

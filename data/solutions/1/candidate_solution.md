What you wrote is *exactly* the classical **Erdős distinct subset sums conjecture** (Erdős dated it to 1931):

> If (A\subseteq{1,\dots,N}), (|A|=n), and all (2^n) subset sums (\sum_{a\in S}a) are distinct, then (N\ge c,2^n) for some absolute constant (c>0).

This is **still open** as of today. ([Erdős Problems][1])

What *is* known are weaker (but nontrivial) lower bounds, and there are also constructions giving upper bounds on how small (N) can be.

---

## The trivial lower bound: (N \gg 2^n/n)

Let (A\subseteq{1,\dots,N}) with (|A|=n). Every subset sum lies in
[
[0,; \sum_{a\in A} a] \subseteq [0,; nN].
]
There are (2^n) subset sums and they are all distinct integers, so
[
2^n \le nN+1 \quad\Longrightarrow\quad N \ge \frac{2^n-1}{n}.
]
So one always has
[
N \gg \frac{2^n}{n}.
]
This is the “trivial” bound mentioned in the standard references. ([Erdős Problems][1])

---

## Best known general theorem: (N \ge \binom{n}{\lfloor n/2\rfloor})

The strongest published general lower bound to date is due to Dubroff–Fox–Xu (2021), who prove the **exact inequality**
[
N ;\ge; \binom{n}{\lfloor n/2\rfloor}.
]
([Erdős Problems][1])

Since
[
\binom{n}{\lfloor n/2\rfloor}\sim \sqrt{\frac{2}{\pi}}\frac{2^n}{\sqrt{n}},
]
this gives
[
N \gg \frac{2^n}{\sqrt{n}},
]
which is much stronger than (2^n/n) but still has the missing (\sqrt{n}) compared to Erdős’ conjectured (c2^n). ([Erdős Problems][1])

### A clean proof idea (Harper/isoperimetry on the hypercube)

Here is the key argument behind the “(\binom{n}{\lfloor n/2\rfloor})” bound (this is essentially the second proof in Dubroff–Fox–Xu):

1. Write (A={a_1,\dots,a_n}) and let (M=\max A\le N).
   Let
   [
   \sigma(S)=\sum_{i\in S} a_i,\qquad S\subseteq [n].
   ]
   “Distinct subset sums” means (\sigma:\mathcal P([n])\to\mathbb Z) is injective.

2. Choose a “median” threshold (t) so that exactly half the subsets have sum (\le t):
   [
   \mathcal F := {S\subseteq[n]:\sigma(S)\le t},\qquad |\mathcal F|=2^{n-1}.
   ]

3. View (\mathcal P([n])) as the vertex set of the (n)-dimensional hypercube (Q_n) (adjacent sets differ by toggling one element).
   Let (\partial \mathcal F) be the **vertex boundary**: the subsets not in (\mathcal F) that are adjacent to something in (\mathcal F).

4. If (T\in \partial\mathcal F), then (T) differs from some (S\in\mathcal F) by toggling one element (i), and since (\sigma(S)\le t < \sigma(T)), it must be that
   [
   \sigma(T)=\sigma(S)+a_i \le t + M.
   ]
   So every boundary point has subset sum in the interval ((t,;t+M]), an interval of length (M).
   By injectivity of (\sigma), there can be **at most (M)** such boundary points:
   [
   |\partial\mathcal F|\le M.
   ]

5. Now use **Harper’s vertex-isoperimetric inequality** on the cube: among all families of size (2^{n-1}), the minimum possible vertex boundary size is (\binom{n}{\lfloor n/2\rfloor}). Hence
   [
   |\partial\mathcal F|\ge \binom{n}{\lfloor n/2\rfloor}.
   ]

6. Combine:
   [
   M \ge |\partial\mathcal F| \ge \binom{n}{\lfloor n/2\rfloor}.
   ]
   Since (N\ge M), this yields (N\ge \binom{n}{\lfloor n/2\rfloor}). ([ar5iv][2])

---

## Why your claimed (N\gg 2^n) is still not known

The Harper/isoperimetry argument above is “best possible” if you only use that (\mathcal F) is a size-(2^{n-1}) family in the cube: *every* size-(2^{n-1}) family can have boundary as small as (\binom{n}{\lfloor n/2\rfloor}). The Erdős conjecture asserts that the *special* families that arise as initial segments of the subset-sum ordering must have **much larger boundary**, on the order of (2^n), but proving that extra expansion remains open. ([Erdős Problems][1])

---

## Upper bounds: you *can* have (N) a small constant times (2^n)

On the other side, there are explicit constructions of sum-distinct sets of size (n) with
[
\max A \le 0.22002\cdot 2^n
]
for all sufficiently large (n) (Bohman, 1998). So if Erdős’ conjecture (N\ge c2^n) is true, the constant (c) cannot be larger than (0.22002). ([Combinatorics][3])

---

### Bottom line

* The statement (N \gg 2^n) is a famous **open conjecture** of Erdős. ([Erdős Problems][1])
* What you *can* prove unconditionally:
  [
  N \ge \frac{2^n-1}{n} \quad\text{(easy),}
  ]
  and the best known general bound is
  [
  N \ge \binom{n}{\lfloor n/2\rfloor} \sim \sqrt{\frac{2}{\pi}}\frac{2^n}{\sqrt n}.
  ]
  ([Erdős Problems][1])

If you tell me what level of detail you want, I can also write out the Harper/isoperimetry part more explicitly (definitions of the boundary and the exact Harper inequality needed), or give the probabilistic/variance-style proof from the same paper.

[1]: https://www.erdosproblems.com/latex/1 "
  
    Erdős Problems
  
"
[2]: https://ar5iv.org/pdf/2006.12988 "[2006.12988] A note on the Erdős distinct subset sums problem"
[3]: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v5i1r3 "
		A construction for sets of integers with distinct subset sums
							\| The Electronic Journal of Combinatorics
			"

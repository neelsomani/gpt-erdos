Yes: for **every** infinite sequence ((x_j)\subset(0,1)),
[
\limsup_{k\to\infty} A_k = \infty.
]
Moreover, the best-known general lower bounds are much stronger than mere unboundedness: one has (A_k \gg \sqrt{k}) for infinitely many $k$. But whether one can force (A_k=o(k)) remains open.

---

## 1) (\limsup_{k\to\infty}A_k=\infty) is true

Write
[
S_n(k):=\sum_{j\le n} e(kx_j),\qquad A_k=\limsup_{n\to\infty}|S_n(k)|.
]

Here is a clean proof by contradiction (due to Tao, also recorded on the Erdős Problems forum).

Assume (\limsup_{k\to\infty}A_k<\infty). Then there exist (k_0) and $C$ such that
[
A_k\le C\qquad\text{for all }k\ge k_0.
]
Fix (K\ge k_0). By the definition of limsup, for each (k_0\le k\le K) there is a (large) index beyond which (|S_n(k)|\le C+1). Taking the maximum over the finitely many (k\in[k_0,K]), there exists (N_K) such that
[
|S_n(k)|\le C+1 \quad\text{for all } n\ge N_K \text{ and all } k_0\le k\le K.
]
Then for any (n\ge 0) and (k_0\le k\le K),
$
\left|\sum_{N_K<j\le N_K+n} e(kx_j)\right|
=|S_{N_K+n}(k)-S_{N_K}(k)|
\le |S_{N_K+n}(k)|+|S_{N_K}(k)|
\le 2(C+1).
$
So the *shifted* sequence (x_{N_K+1},x_{N_K+2},\dots) has **uniformly bounded** exponential sums for all (k\in[k_0,K]), with a bound not depending on $n$.

Now extract a subsequence (K_m\to\infty) so that for each fixed $j$, the points (x_{N_{K_m}+j}) converge (mod 1) to some limit (y_j\in[0,1)). Passing to the limit [[nomath]](with $n,k$ fixed)[[/nomath]] preserves the bound:
[
\left|\sum_{j\le n} e(ky_j)\right|\le 2(C+1) \qquad \forall n\ge 0,\ \forall k\ge k_0.
]

Fix $n$. Average the squared modulus over (k=1,\dots,K):
[
\frac1K\sum_{k=1}^K\left|\sum_{j\le n} e(ky_j)\right|^2 \le 4(C+1)^2.
]
Expanding the square and letting (K\to\infty), the orthogonality of characters yields that the left-hand side tends to
[
|{(i,j)\in{1,\dots,n}^2:\ y_i=y_j}|,
]
the number of equal pairs among the first $n$ values; in particular this is (\ge n) [[nomath]](at least the diagonal pairs $i=j$)[[/nomath]]. For (n>4(C+1)^2) this contradicts the upper bound (4(C+1)^2). Hence the assumption that ((A_k)) is bounded for large $k$ is impossible, proving (\limsup_{k\to\infty}A_k=\infty). ([Erdős Problems][1])

This answers your first question affirmatively.

---

## 2) Quantitative lower bounds: (A_k) is often at least (\sqrt{k})

The above argument only shows unboundedness. Much stronger bounds are known:

* Erdős later gave a “very easy” proof that
  [
  A_k \gg \log k
  \quad\text{for infinitely many }k.
  ]
* Clunie proved the stronger statement
  [
  A_k \gg k^{1/2}
  \quad\text{for infinitely many }k,
  ]
  and also constructed sequences for which (A_k\le k) for all $k$. ([Erdős Problems][2])

So for *every* sequence ((x_j)), (A_k) must be unbounded and in fact cannot stay below a constant multiple of (\sqrt{k}) for all large $k$.

---

## 3) Can one have (A_k=o(k))?

This is the subtle part.

* Clunie’s construction shows (A_k\le k) for all $k$ is possible, so **linear** growth is certainly not forced. ([Erdős Problems][2])
* The general lower bound (A_k\gg \sqrt{k}) infinitely often does **not** rule out (A_k=o(k)), since (\sqrt{k}=o(k)). ([Erdős Problems][2])
* As far as current literature summaries indicate (including the Erdős Problems page, last edited Dec 29, 2025), the question
  [
  A_k=o(k)\ \text{?}
  ]
  **still appears to be open**. ([Erdős Problems][2])

So the best “global picture” currently is:
[
\text{for every sequence: } A_k \text{ is unbounded and } A_k\gg \sqrt{k}\ \text{i.o.}
]
[
\text{there exist sequences with } A_k\le k\ \text{for all }k;
\qquad
\text{but whether one can force }A_k=o(k)\text{ is unknown.}
]

If you’d like, I can also sketch the intuition behind why (\sqrt{k}) is the natural barrier (random-walk heuristics) and what kinds of block-cancellation constructions people expect might achieve (A_k\ll k^{1/2+o(1)}) [[nomath]](which would imply $o(k)$)[[/nomath]].

[1]: https://www.erdosproblems.com/forum/thread/987 "https://www.erdosproblems.com/forum/thread/987"
[2]: https://www.erdosproblems.com/latex/987 "https://www.erdosproblems.com/latex/987"

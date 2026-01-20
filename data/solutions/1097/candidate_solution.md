Let
[
D(A):={,d\in \mathbb Z\setminus{0}:\ \exists a\in\mathbb Z\ \text{with}\ a,\ a+d,\ a+2d\in A,}
]
[[nomath]](the set of *distinct* nonzero common differences of 3-term arithmetic progressions in $A$)[[/nomath]].
Counting (d>0) or (d\neq 0) only changes things by a factor of $2$.

If one asks for the extremal function
[
f(n):=\max_{|A|=n} |D(A)|,
]
then this is a well-known Erdős problem (#1097) and is still open in the sense that the true exponent is not known. ([Erdős Problems][1])

## What is known

### Trivial bound

[
|D(A)| \le |A-A| \le \binom{n}{2} = O(n^2),
]
since each $d$ corresponds to at least one pair $(a,a+2d)$.

### Best known general upper bound: $O(n^{11/6})$

There is a nontrivial upper bound
[
|D(A)| \ll n^{11/6}.
]

One clean way to see why the Katz–Tao “partial sums/differences” theorem applies is:

* Define a graph (G\subseteq A\times A) by
  [
  (x,z)\in G\quad \Longleftrightarrow\quad \frac{x+z}{2}\in A.
  ]
  Then each such edge gives a 3-AP (x,\frac{x+z}{2},z) with difference (d=(z-x)/2).

* The “restricted sumset” along $G$ is
  [
  A\overset{G}{+}A := {x+z:\ (x,z)\in G}\subseteq 2A,
  ]
  so (|A\overset{G}{+}A|\le |2A|\le n).

* The “restricted difference set” along $G$ is
  [
  A\overset{G}{-}A := {z-x:\ (x,z)\in G} = {\pm 2d:\ d\in D(A)},
  ]
  hence (|D(A)| \le \tfrac12 |A\overset{G}{-}A|).

Katz–Tao prove that if (|A|,|B|,|A\overset{G}{+}B|\le N) then (|A\overset{G}{-}B|\ll N^{2-1/6}=N^{11/6}). ([arXiv][2])
Applying this with $A=B$ and $N=n$ yields (|D(A)|\ll n^{11/6}).

### Lower bounds: (n^{3/2}) is achievable, and in fact we now know **strictly larger** exponents

Erdős and Spencer gave a probabilistic construction achieving (|D(A)|\gtrsim n^{3/2}), and Erdős–Ruzsa had earlier explicit constructions with (|D(A)|\ge n^{1+c}) for some (c>0). ([Erdős Problems][1])

More importantly for your second question: the (n^{3/2}) guess is **not** the end of the story. Via an equivalence to Bourgain’s “sums–differences” (a.k.a. arithmetic Kakeya) problem, current best constructions imply
[
f(n)\ \ge\ n^{1.77898\ldots - o(1)}.
]
This is summarized on the Erdős problems site, attributing the lower bound to Lemm (with a small later improvement). ([Erdős Problems][1])

## Answer to your questions

* **How many distinct $d$ can occur?**
  Letting (f(n)=\max_{|A|=n}|D(A)|), the best known bounds (as of the latest compiled references) are
  [
  n^{1.77898\ldots-o(1)}\ \lesssim\ f(n)\ \lesssim\ n^{11/6}\approx n^{1.8333}.
  ]
  Determining the true growth rate/exponent remains open. ([Erdős Problems][1])

* **Are there always $O(n^{3/2})$ such $d$?**
  **No.** Since there exist $n$-element sets $A$ with (|D(A)|\ge n^{1.77898\ldots-o(1)}), one cannot have a universal upper bound $O(n^{3/2})$. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/1097 "
  
    Erdős Problem #1097
  
"
[2]: https://arxiv.org/abs/math/9906097 "[math/9906097] A new bound on partial sum-sets and difference-sets, and applications to the Kakeya conjecture"

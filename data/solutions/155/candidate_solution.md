For (k=1), **yes**, and it is true for **every** $N$ (no “large $N$” needed).

* Take any Sidon set (A\subseteq{1,\dots,N+1}).
* If (N+1\notin A), then (|A|\le F(N)).
* If (N+1\in A), then (A\setminus{N+1}\subseteq{1,\dots,N}) is still Sidon, so (|A|-1\le F(N)), i.e. (|A|\le F(N)+1).

So (F(N+1)\le F(N)+1) for all $N$.

For **fixed (k\ge 2)**, the statement you wrote is, as far as is known, **open** (it is an Erdős problem). It appears explicitly as Erdős Problem #155 and is marked open there. ([Erdős Problems][1])

### What is known around it

* Globally, one knows the right scale:
  [
  F(N) = (1+o(1))N^{1/2}
  ]
  and classical bounds of Erdős–Turán / Singer type give
  [
  F(N)\le \sqrt N + O(N^{1/4}),\qquad F(N)\ge \sqrt N - O(N^{1/4})
  ]
  (in the standard $[0,n-1]$ normalisation, which is the same up to shifting). ([TAU Mathematics][2])
  This makes the conjecture *plausible*: “typically” $F(N)$ only increases by $1$ after $N$ grows by about (2\sqrt N), which is much bigger than any fixed $k$. But these global estimates do not control the **local** jump pattern well enough to prove your inequality.

* There are easy inequalities that hold for all $N,k$, but they are weaker:
  [
  F(N+k)\le F(N)+F(k),
  ]
  which is basically “split a maximum Sidon set in ({1,\dots,N+k}) into the part (\le N) and the part (>N)”. This is noted in the discussion of the same Erdős problem. ([Erdős Problems][3])
  There is also a refinement in that discussion giving (F(N+k)\le F(N)+g(k)) for a certain (g(k)\le F(k)). ([Erdős Problems][3])
  None of these get down to “$+1$”.

### Small computed data (just to show the issue is genuinely local)

Exact values of $F(N)$ are known by computation for $N$ up to at least $500$ (OEIS A143824). ([OEIS][4])
They show that two “$+1$” jumps can occur fairly close together (so you really do need the phrase “for sufficiently large $N$” if the conjecture is true). For example, the jump points $481$ and $493$ are only $12$ apart. ([OEIS][5])
In particular, the table gives (F(480)=24) and (F(493)=26), so for (k=13) one has
[
F(480+13)=F(493)=26>24+1=F(480)+1,
]
a finite counterexample for that $k$. ([OEIS][6])
This does **not** answer your question (because you allow finitely many exceptions), but it shows what would have to be ruled out “eventually”.

### Bottom line

* (k=1): **true for all $N$** (simple argument above).
* (k\ge 2): the statement “(F(N+k)\le F(N)+1) for all sufficiently large $N$” is **not proved and not disproved** in general; it is an open Erdős problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/155 "
  
    Erdős Problem #155
  
"
[2]: https://www.math.tau.ac.il/~samotij/papers/Sidon.pdf?utm_source=chatgpt.com "sets contained in a sparse random set of integers"
[3]: https://www.erdosproblems.com/forum/thread/155 "https://www.erdosproblems.com/forum/thread/155"
[4]: https://oeis.org/A143824 "https://oeis.org/A143824"
[5]: https://oeis.org/A227590 "https://oeis.org/A227590"
[6]: https://oeis.org/A143824/b143824.txt "https://oeis.org/A143824/b143824.txt"

No one knows.

This is the **Erdős unit distance problem**. Let $U(n)$ be the largest possible number of pairs $\\{p,q\\}$ at distance $1$ among $n$ points in the plane.

What we know today is:

* **Lower bound (construction):** there are point sets with
  [
  U(n);\ge; n^{,1+\Omega(1/\log\log n)} .
  ]
  So you really *can* get “a little more than linear” many unit-distance pairs. 

* **Best general upper bound:** for every set of $n$ points,
  [
  U(n);=;O(n^{4/3}),
  ]
  proved by Spencer–Szemerédi–Trotter (1984). 

Your question asks whether we can replace the (n^{4/3}) upper bound by something like
[
n^{,1+O(1/\log\log n)},
]
which would almost match the known construction. That is **open**; it would be a major breakthrough. 

One reason it is hard is that the known (O(n^{4/3})) proofs all go through the same kind of incidence geometry ideas, and to beat (n^{4/3}) you seem to need a genuinely new idea that does **not** also apply to the point–line incidence problem. ([arXiv][1])

[1]: https://arxiv.org/html/2507.15679v1 "Erdős’s unit distance problem and rigidity"

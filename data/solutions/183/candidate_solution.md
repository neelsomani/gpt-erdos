Let $R(3;k)$ be the $k$-colour Ramsey number for triangles, i.e. the least $n$ such that every $k$-edge-colouring of (K_n) contains a monochromatic (K_3).

### 1) The limit exists (possibly (+\infty))

Set
[
a_k:=R(3;k)-1,
]
so (a_k) is the largest $n$ for which there **exists** a $k$-colouring of (K_n) with **no** monochromatic triangle.

**Product (supermultiplicativity) construction.**
Given a “good” $k$-colouring of (K_{a_k}) and a “good” (\ell)-colouring of (K_{a_\ell}), build a ((k+\ell))-colouring on the vertex set ([a_k]\times [a_\ell]) by colouring the edge between $(i,j)$ and $(i',j')$ as follows:

* if $i=i'$, colour it by the (\ell)-colouring rule on $\\{j,j'\\}$ [[nomath]](use colours $1,\dots,\ell$)[[/nomath]];
* if (i\neq i'), colour it by the $k$-colouring rule on $\\{i,i'\\}$ [[nomath]](use colours $\ell+1,\dots,\ell+k$)[[/nomath]].

Then no triangle can be monochromatic:

* triangles inside one “fiber” ({i}\times[a_\ell]) are controlled by the (\ell)-colouring;
* any triangle using vertices from at least two different fibers has at least one edge of the first type and one of the second type, hence uses colours from disjoint colour-sets.

So
[
a_{k+\ell}\ \ge\ a_k,a_\ell.
]
By Fekete’s lemma applied to (\log a_k), the limit
[
\lim_{k\to\infty} a_k^{1/k}
]
exists in ((0,\infty]). Since (a_k\to\infty), this is the same as (\lim_{k\to\infty} R(3;k)^{1/k}).

(That this limit exists is also explicitly noted in the literature. ([arXiv][1]))

### 2) But its value is **unknown** (an Erdős prize problem)

Determining the value of
[
\lim_{k\to\infty} R(3;k)^{1/k}
]
is a famous open problem of Erdős; even proving the limit is finite was posed as a separate challenge. ([arXiv][1])

So, at present, one cannot “determine” the limit beyond bounds.

### 3) Best known bounds (as of current references)

* **Lower bound:** known constructions (via Schur-number lower bounds) imply
  [
  R(3;k)\ \ge\ 380^{k/5}-O(1),
  ]
  hence
  [
  \lim_{k\to\infty} R(3;k)^{1/k}\ \ge\ 380^{1/5}\ \approx\ 3.280625976.
  ]
  ([Erdős Problems][2])

* **Upper bound:** a standard inductive “pigeonhole/neighbor” argument gives
  [
  R(3;k)\le \lceil ek!\rceil,
  ]
  so
  [
  R(3;k)^{1/k}\ \le\ (ek!)^{1/k}\sim \frac{k}{e},
  ]
  which does **not** yield any constant upper bound on the limit. ([Erdős Problems][2])

### Conclusion

The limit (\displaystyle \lim_{k\to\infty} R(3;k)^{1/k}) **exists**, but its **value is not known**. It is an open Erdős problem. The best published bounds quoted in current references are
[
3.280625976\ldots\ \le\ \lim_{k\to\infty} R(3;k)^{1/k}\ \le\ +\infty,
]
and it is open whether the limit is finite. ([arXiv][1])

[1]: https://arxiv.org/pdf/1907.05236 "https://arxiv.org/pdf/1907.05236"
[2]: https://www.erdosproblems.com/183 "https://www.erdosproblems.com/183"

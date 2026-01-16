A useful reformulation is this: a (k)-coloring of ([N]={1,\dots,N}) has the property “every 4-term AP uses at least 3 colors” **iff** for every pair of colors (i,j), the union of the corresponding color classes (A_i\cup A_j) contains **no** 4-term arithmetic progression (otherwise that 4-AP would be colored with at most the two colors (i,j)). ([Erdős Problems][1])

### Lower bound (comes from 3-term progression–free sets)

Let (M=\lfloor 2N/3\rfloor). In any valid coloring, **no color class can contain a 3-term AP inside ([M])**: if (x,x+d,x+2d\le M) are the same color, then (d\le N/3), so (x+3d\le N), and ((x,x+d,x+2d,x+3d)) is a 4-AP using at most two colors (in fact the first three are the same), which is forbidden.

Thus each (A_i\cap[M]) is 3-AP-free, so
[
|A_i\cap[M]|\le r_3(M),
]
where (r_3(M)) is the maximum size of a 3-term-AP-free subset of ([M]). Since the (A_i\cap[M]) partition ([M]),
[
k \ge \frac{M}{r_3(M)}.
]
Using the best known quantitative Roth bounds (Bloom–Sisask, improving Kelley–Meka) that
[
r_3(M)\le \exp!\big(-c(\log M)^{1/9}\big),M,
]
one gets
[
h(N)\ \ge\ \exp!\big(c(\log N)^{1/9}\big)
]
for some absolute (c>0). ([arXiv][2])

### Upper bounds (explicit constructions)

* **Twisted cubic construction (LeechLattice, MathOverflow):** one can partition a set of size (\asymp p^3) into (\asymp p^2) parts so that the union of any two parts contains no 4-AP, then “project” to an interval ([N]). This gives
  [
  h(N)\ \ll\ N^{2/3}.
  ]
  ([MathOverflow][3])

* **Improved exponent (Z. Hunter):** there is a further improvement to
  [
  h(N)\ \ll\ N^{\frac{\log 3}{\log 22}+o(1)} \approx N^{0.355+o(1)}.
  ]
  A key ingredient is an explicit 3-coloring of (\mathbb Z/22\mathbb Z) avoiding “symmetrically colored” (ABBA) 4-APs, which can be tensored; combined with additional product constructions one obtains the stated bound for (h(N)). ([Erdős Problems][1])

### Best current “estimate”

Putting these together, the known growth window is
[
\exp!\big(c(\log N)^{1/9}\big)\ \ll\ h(N)\ \ll\ N^{0.355+o(1)}.
]
([Erdős Problems][1])

The true order of magnitude is open (in particular, it’s not known whether (h(N)=N^{o(1)}) or (h(N)) grows like a fixed power (N^\alpha)). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/160 "
  
    Erdős Problem #160
  
"
[2]: https://arxiv.org/abs/2309.02353?utm_source=chatgpt.com "An improvement to the Kelley-Meka bounds on three-term arithmetic progressions"
[3]: https://mathoverflow.net/questions/410808/what-are-bounds-on-this-van-der-waerden-esque-problem "co.combinatorics - What are bounds on this van der Waerden-esque problem? - MathOverflow"

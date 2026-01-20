The inequality
[
\mathrm{ex}(n;C_{2k})\gg n^{1+\frac1k}\qquad (k\ge 3)
]
is **not known in general**: it is a famous open problem of Erdős (sometimes called the *even cycle problem*). ([Erdős Problems][1])

What *is* known is that this lower bound **does hold** for $k=3$ [[nomath]](i.e. $C_6$)[[/nomath]] and $k=5$ [[nomath]](i.e. $C_{10}$)[[/nomath]], via explicit algebraic/finite-geometric constructions (Benson/Wenger; a clean geometric presentation is due to Conlon). ([Erdős Problems][1])
For other $k$ [[nomath]](e.g. $k=4$, the $C_8$ case)[[/nomath]], it remains open, and there is evidence it might even be smaller than (n^{1+1/k}) in some cases. ([arXiv][2])

That said, here is a complete construction/proof giving
[
\mathrm{ex}(n;C_{2k})\gg n^{1+\frac1k}
]
for the **known cases $k=3$ and $k=5$**.

---

## Wenger–Conlon construction [[nomath]](works for $C_6$ and $C_{10}$)[[/nomath]]

Fix a prime power $q$, and let (\mathbb F_q) be the field of order $q$.

For an integer (d\ge 2), define vectors
[
v(z)=(1,z,z^2,\dots,z^{d-1})\in \mathbb F_q^{d}\qquad (z\in \mathbb F_q).
]

### Vertices

Let (P=\mathbb F_q^{,d}) (think: points).
Let $L$ be the set of **all lines in (\mathbb F_q^{,d})** of the form
[
\ell_{x,z}={x+yv(z):y\in \mathbb F_q}
\qquad (x\in \mathbb F_q^{d}\ z\in \mathbb F_q).
]
[[nomath]](So $v(z)$ is the direction.)[[/nomath]]

A quick count: there are (q^{d+1}) pairs $(x,z)$. For a fixed line (\ell_{x,z}), changing $x$ by (y_0v(z)) gives the same line, and there are exactly $q$ such shifts, so each line is represented $q$ times. Hence
[
|L|=\frac{q^{d+1}}{q}=q^d.
]

So the total number of vertices is
[
N:=|P|+|L|=q^d+q^d=2q^d.
]

### Edges

Build the bipartite graph (D_d(q)) between $P$ and $L$ by incidence:
[
p\in P \text{ is joined to } \ell\in L \iff p\in \ell.
]
Each line (\ell) contains exactly $q$ points, so (\deg(\ell)=q). Therefore
[
e(D_d(q))=q|L| = q\cdot q^d = q^{d+1}.
]

In terms of (N=2q^d),
[
e(D_d(q))=q^{d+1} = \left(\frac N2\right)^{1+\frac1d}.
]
So this already has the *right edge count* for the exponent (1+\frac1d).

---

## Key structural facts about cycles in (D_d(q))

Consider any cycle in this bipartite graph:
[
p_1\ell_1p_2\ell_2\cdots p_t\ell_t p_1.
]

### Fact 1: consecutive lines cannot be parallel

If (\ell_i) and (\ell_{i+1}) are parallel and share the point (p_{i+1}), then they are the **same** line. So in a genuine cycle (distinct vertices), (\ell_i) and (\ell_{i+1}) are never parallel.

### Fact 2: if (t\le d), then every direction appears at least twice

Let (\ell_i) have direction $v(z_i)$. Since (p_i\neq p_{i+1}) lie on (\ell_i), we can write
[
p_{i+1}-p_i = a_i,v(z_i) \quad\text{for some }a_i\in\mathbb F_q^\times.
]
Summing around the cycle gives
[
0=\sum_{i=1}^t (p_{i+1}-p_i)=\sum_{i=1}^t a_i v(z_i).
]
Now use the Vandermonde-determinant fact: **any $d$ distinct vectors** $v(z)$ are linearly independent in (\mathbb F_q^{,d}). ([arXiv][2])
So when (t\le d), the only way (\sum a_i v(z_i)=0) with all (a_i\neq 0) is if no direction occurs “uniquely”: **each direction $z$ appearing among ({z_1,\dots,z_t}) must appear at least twice**. ([arXiv][2])

These two facts are exactly what Conlon highlights to certify (C_4)-, (C_6)-, and (C_{10})-freeness in the appropriate dimensions. ([arXiv][2])

---

## Case $k=3$: a (C_6)-free graph with (\asymp N^{4/3}) edges

Take $d=3$. Then (N=2q^3) and (e=q^4 = (N/2)^{4/3}).

Suppose (D_3(q)) had a 6-cycle. Then $t=3$. Since (t\le d), Fact 2 says each direction among ({\ell_1,\ell_2,\ell_3}) appears at least twice, so all three lines must be parallel. But that contradicts Fact 1 (adjacent lines in the cycle are not parallel). Hence **no 6-cycle exists**. ([arXiv][2])

Therefore, for (N=2q^3),
[
\mathrm{ex}(N;C_6)\ \ge\ e(D_3(q))\ =\ q^4\ =\left(\frac N2\right)^{4/3}\ \gg\ N^{4/3}.
]

---

## Case $k=5$: a (C_{10})-free graph with (\asymp N^{6/5}) edges

Take $d=5$. Then (N=2q^5) and (e=q^6 = (N/2)^{6/5}).

If (D_5(q)) had a 10-cycle, then $t=5$. Since (t\le d), Fact 2 says each direction among the 5 lines appears at least twice. With 5 lines total, the multiplicities must be $3+2$: some direction occurs **three** times.

But on a 5-cycle, any set of 3 vertices contains adjacent vertices [[nomath]](because the largest independent set in $C_5$ has size 2)[[/nomath]]. So two of those three parallel lines would have to be consecutive in the cycle—contradicting Fact 1. Hence **no 10-cycle exists**. ([arXiv][2])

Therefore, for (N=2q^5),
[
\mathrm{ex}(N;C_{10})\ \ge\ e(D_5(q))\ =\ q^6\ =\left(\frac N2\right)^{6/5}\ \gg\ N^{6/5}.
]

---

## What about general (k\ge 3)?

The construction above gives the conjectured exponent (1+\frac1k) **only for $k=3$ and $k=5$** [[nomath]](and $k=2$ for $C_4$)[[/nomath]]. For general (k\ge 4) the bound
[
\mathrm{ex}(n;C_{2k}) \gg n^{1+1/k}
]
is a well-known open problem. ([Erdős Problems][1])

The best general lower bounds are weaker; for example Lazebnik–Ustimenko–Woldar give, for all (k\ge 3),
[
\mathrm{ex}(n;C_{2k})\gg n^{1+\frac{2}{3k-3+\nu}}
\quad(\nu=0\text{ if }k\text{ odd, }\nu=1\text{ if }k\text{ even}),
]
as summarized in the Erdős Problems entry. ([Erdős Problems][1])

If you tell me whether your exercise sheet really intended the *open* statement, or perhaps the LUW bound above (or the standard probabilistic bound), I can write the full proof in that intended form.

[1]: https://www.erdosproblems.com/search_bib/Er64c/open "
  
    Erdős Problems
  
"
[2]: https://arxiv.org/pdf/2011.11064 "https://arxiv.org/pdf/2011.11064"

This exact question is **open** (in the literature, and still listed as open as of late **2025**). It was asked by **Erdős–Ordman–Zalcstein** in their paper *Clique Partitions of Chordal Graphs*; they explicitly state that it is unknown whether (n^{2}/6+O(n)) cliques always suffice. ([Cambridge University Press & Assessment][1])

### Why (n^2/6) is the “right” constant to hope for

There is a **chordal** example (in fact a **split/threshold** graph) that already **forces** (\frac{n^{2}}{6}+O(n)) cliques, so you cannot hope for a smaller leading constant.

Take (n=3k). Let $A$ be a clique of size $k$ and $B$ an independent set of size $2k$, and join **every** vertex of $B$ to **every** vertex of $A$. This graph is chordal (indeed split). Erdős–Ordman–Zalcstein point out that this construction shows (\frac{n^{2}}{6}+O(n)) cliques can be **necessary**. ([Erdős Problems][2])

One can check it in this case more explicitly: the minimum number of cliques in an edge-partition is
[
\frac{k(k-1)}2 + k(k+1)=\frac{3}{2}k^{2}+\frac{k}{2}=\frac{n^{2}}6+\frac{n}{6}.
]
So the (\tfrac16) constant is genuinely tight (up to lower-order terms).

### What is known in the “upper bound” direction

What’s known is strictly weaker than (\tfrac{1}{6}n^{2}):

* **Erdős–Ordman–Zalcstein (1993)** proved that every chordal graph on (n) vertices has an edge partition into at most ((1-c)\frac{n^{2}}{4}) cliques for some absolute constant (c>0) (equivalently [[nomath]]($\tfrac14-\varepsilon)n^{2}$ for some small $\varepsilon>0$)[[/nomath]], but they did **not** get down to (n^{2}/6+O(n)). ([Cambridge University Press & Assessment][1])
* For the subclass of **split graphs** (which are all chordal), **Chen–Erdős–Ordman** showed an improved bound of
  [
  \frac{3}{16}n^{2}+O(n)
  ]
  cliques. ([Erdős Problems][2])

### Bottom line

* (\boxed{\text{It is not known whether every chordal }G\text{ admits an }n^{2}/6+O(n)\text{ clique edge-partition.}}) ([Cambridge University Press & Assessment][1])
* The bound would be **best possible** (up to $O(n)$) because there are chordal (split/threshold) graphs that **require** (\tfrac{n^{2}}6+O(n)) cliques. ([Erdős Problems][2])

If you want, I can also sketch the standard counting argument that the split example really forces (\sim n^{2}/6), and how the known ((\tfrac14-\varepsilon)n^{2}) argument is structured (it uses structural properties of chordal graphs).

[1]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CEA1F929F2A88B5A4C7C8E23DFD0DD29/S0963548300000808a.pdf/clique_partitions_of_chordal_graphs.pdf "Clique Partitions of Chordal Graphs† | Combinatorics, Probability and Computing | Cambridge Core"
[2]: https://www.erdosproblems.com/81 "
  
    Erdős Problem #81
  
"

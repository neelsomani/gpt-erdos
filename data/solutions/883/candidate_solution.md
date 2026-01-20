Let
[
f(n,2):=\Big\lfloor\frac n2\Big\rfloor+\Big\lfloor\frac n3\Big\rfloor-\Big\lfloor\frac n6\Big\rfloor,
]
which is exactly the number of integers (m\le n) divisible by $2$ or $3$ (inclusion–exclusion).

## 1) Odd cycles up to (\frac n3+1)

This is **open** as stated.

What is known is the 1997 theorem of Erdős–Sárközy: there exist constants (c>0) and (n_0) such that for all (n\ge n_0), if (|A|>f(n,2)), then $G(A)$ contains **every odd cycle**
[
C_{2\ell+1}\quad\text{for all integers }\ell\le c n.
]
So one gets “all odd cycle lengths” up to a **linear** fraction of $n$, but the best possible constant $c$ is not determined. 

Moreover, Erdős–Sárközy explicitly note that determining the best $c$ is interesting, and they suggest that perhaps (c=1/6) is optimal; (c\le 1/6) is a natural upper bound [[nomath]](for $6\mid n$)[[/nomath]] coming from a simple construction. 

Your bound “all odd cycles of length (\le \frac n3+1)” corresponds exactly to taking (\ell\le n/6), i.e. to the conjectural optimal (c=1/6). The current literature summary (as of Oct 24, 2025) also lists this precise strengthening as open. ([Erdős Problems][1])

## 2) A complete $(1,\ell,\ell)$ tripartite graph

This one is **true** [[nomath]](for sufficiently large $n$)[[/nomath]], and in fact is known in a stronger quantitative form.

Sárközy (1999) proved that there are constants (c,n_0) such that for all (n\ge n_0), if (|A|>f(n,2)), then $G(A)$ contains a complete tripartite graph $K(1,L,L)$ with
[
L \asymp \frac{\log n}{\log\log\log n}
]
[[nomath]](and in a denser residue-class regime even $L\asymp \log n$)[[/nomath]]. ([Worcester Polytechnic Institute][2])

In particular, since (L\to\infty) with $n$, for any fixed (\ell\ge 1) one can take $n$ large enough so that (L\ge \ell), and then $K(1,L,L)$ contains $K(1,\ell,\ell)$ as a subgraph [[nomath]](by selecting $\ell$ vertices from each of the two $L$-parts)[[/nomath]]. ([Worcester Polytechnic Institute][2])

[1]: https://www.erdosproblems.com/883 "
  
    Erdős Problem #883
  
"
[2]: https://web.cs.wpi.edu/~gsarkozy/Cikkek/12.pdf "PII: S0012-365X(98)00359-8"

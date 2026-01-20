Write (R_k(G):=R(G;k)) for the $k$-colour Ramsey number. For even cycles (C_{2n}), the **exact value is only known in a few cases**; in general it is an open problem.

## Exact values that are known

### $k=1$

[
R(C_{2n};1)=2n.
]

### $k=2$ (two colours)

A classical theorem of Faudree–Schelp and Rosta yields, for even cycles, that
[
R(C_{2n};2)=R(C_{2n},C_{2n})=
\begin{cases}
6,& n=2\ (C_4),[4pt]
3n-1,& n\ge 3.
\end{cases}
]
([RIT Computer Science][1])

### $k=3$ (three colours)

It is known that
[
R(C_{2n};3)=4n
\quad\text{for all sufficiently large }n,
]
but the exact value is **not known for every specific $n$**; e.g. the first open case listed is (R_3(C_{10})), known only to satisfy (R_3(C_{10})\ge 20). 

## What is known for general (k\ge 4)

For general $k$, an exact closed form for $R(C_{2n};k)$ is **not known**. The best general statements are **bounds** (and asymptotics).

### General lower bounds [[nomath]](all $n\ge 2$)[[/nomath]]

Two standard lower bounds recorded in the current dynamic survey are [[nomath]](with $m=n$ there)[[/nomath]]:

* $
  R_k(C_{2n}) \ge
  \begin{cases}
  (k+1)n, & k \text{ odd},\
  (k+1)n-1, & k \text{ even},
  \end{cases}
  $
* and also
  [
  R_k(C_{2n}) \ge 2(k-1)(n-1)+2.
  ]


### Upper bounds for fixed $k$ and large $n$

For each fixed (k\ge 2), (R_k(C_{2n})) grows linearly in $n$. In particular one has an asymptotic bound of the form
[
R_k(C_{2n}) \le (2k-1+o(1))n \qquad (n\to\infty,\ \text{(k) fixed}),
]
coming from successive improvements of earlier $2kn+o(n)$ bounds. 

So, for fixed $k$ and (n\to\infty), the currently recorded bounds essentially pin (R_k(C_{2n})) between $(2k-2+o(1))n$ and $(2k-1+o(1))n$. 

## Bottom line

* **Exactly:** (R(C_{2n};2)=6) for $n=2$ and (=3n-1) for (n\ge3). ([RIT Computer Science][1])
* **Three colours:** (R(C_{2n};3)=4n) for all sufficiently large $n$, but not settled for all specific $n$ [[nomath]](e.g. $C_{10}$)[[/nomath]]. 
* **General $k$:** no complete exact formula is known; best results are bounds/asymptotics as above. 

[1]: https://www.cs.rit.edu/~spr/PUBL/paper61.pdf "https://www.cs.rit.edu/~spr/PUBL/paper61.pdf"

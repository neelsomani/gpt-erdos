Let (L_{k,n}) be the number of (k\times n) Latin rectangles on the symbol set ({1,2,\dots,n}) (so each row is a permutation of (1,\dots,n), and no symbol repeats in any column).

Write the falling factorial
[
[n]_k ;=; n(n-1)\cdots (n-k+1).
]

A sharp asymptotic formula (Godsil–McKay) says that, as (n\to\infty) and **uniformly for (k=o(n^{6/7})),**
[
L_{k,n};\sim; (n!)^{k}\left(\frac{[n]_k}{n^{k}}\right)^{n}
\left(1-\frac{k}{n}\right)^{-n/2}\exp!\left(-\frac{k}{2}\right).
]
([Springer Link][1])

In particular, if (k) is fixed (or much smaller than (n)), this simplifies to the classic main term
[
L_{k,n};\sim; (n!)^{k}\exp!\left(-\binom{k}{2}\right)
;=;(n!)^{k}\exp!\left(-\frac{k(k-1)}{2}\right).
]


[1]: https://link.springer.com/article/10.1007/s00373-015-1643-1 "On Computing the Number of Latin Rectangles | Graphs and Combinatorics"

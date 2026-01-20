This is **not known exactly**: determining the diagonal size–Ramsey number of the balanced complete bipartite graph (K_{n,n}) is an **open problem**. ([Erdős Problems][1])

What *is* known is that it grows **exponentially** in $n$, up to a remaining factor of $n$:

[
\frac{1}{60}n^{2}2^{n}<\hat{R}(K_{n,n})<\frac{3}{2}n^{3}2^{n}.
]
The **lower bound** [[nomath]](for $n\ge 6$)[[/nomath]] is due to Erdős–Rousseau (1993). ([ScienceDirect][2])
The **upper bound** is due to Erdős–Faudree–Rousseau–Schelp (1978) and Nešetřil–Rödl (1978). ([Erdős Problems][1])

So, in order-of-magnitude terms,
[
\hat{R}(K_{n,n}) = 2^{n}\cdot n^{\Theta(1)},\qquad
n^{2}2^{n}\ \ll\ \hat{R}(K_{n,n})\ \ll\ n^{3}2^{n}.
]
([Erdős Problems][1])

### Best general perspective (and conjecture)

Conlon–Fox–Wigderson (2023) proved a broad lower bound for all (s\le t):
[
\hat{R}(K_{s,t}) =\Omega\left(s^{,2-\frac{s}{t}};t;2^{s}\right),
]
and showed that when (t=\Omega(s\log s)) one in fact has
[
\hat{R}(K_{s,t})=\Theta(s^{2}t2^{s}).
]


They conjecture that this (\Theta(s^{2}t2^{s})) behaviour should hold for **all** (s\le t), which would in particular imply
[
\hat{R}(K_{n,n}) \asymp n^{3}2^{n}.
]
([Erdős Problems][1])

[1]: https://www.erdosproblems.com/560 "
  
    Erdős Problem #560
  
"
[2]: https://www.sciencedirect.com/science/article/pii/0012365X9390521T "The size Ramsey number of a complete bipartite graph - ScienceDirect"

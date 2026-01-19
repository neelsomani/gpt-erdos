There’s a very tight connection here to **off‑diagonal Ramsey numbers**.

Let $R(k,t)$ be the smallest $N$ such that every $N$-vertex graph contains either a (K_k) or an independent set of size $t$. If $G$ is (K_k)-free on $n$ vertices and (\alpha(G)<t), then
[
\chi(G) \ge \frac{n}{\alpha(G)} > \frac{n}{t}.
]
So good lower bounds on (g_k(n)) come from constructions of (K_k)-free graphs with **very small** independence number, i.e. from lower bounds on $R(k,t)$.

## What is known

### $k=4$: yes (now true)

Mattheus and Verstraëte proved
[
R(4,t)=\Omega\left(\frac{t^3}{\log^4 t}\right),
]
(published in *Annals of Mathematics*). ([Annals of Mathematics][1])

This implies [[nomath]](by the standard “$\alpha<t\Rightarrow \chi\gtrsim n/t$” translation)[[/nomath]] that
[
g_4(n)=\Omega\left(\frac{n^{2/3}}{(\log n)^{4/3}}\right),
]
so your inequality holds for $k=4$ with (c=4/3). ([Erdős Problems][2])

### (k\ge 5): open

For fixed (k\ge 5), the Ramsey-type statement
[
R(k,t)\gg \frac{t^{k-1}}{(\log t)^{c(k)}}
]
[[nomath]](and hence your proposed lower bound for $g_k(n)$)[[/nomath]] is a well-known open Erdős problem. ([Erdős Problems][3])

The best general lower bounds currently come from the (K_k)-free process (Bohman–Keevash), which gives a much smaller exponent in $t$ than $k-1$. ([arXiv][4])
Translated to (g_k(n)), this yields only something like
[
g_k(n)\gg \frac{n^{,1-\frac{2}{k+1}}}{(\log n)^{c_k}}
\quad\text{for some }c_k>0,
]
rather than the desired (n^{1-\frac1{k-1}}). ([Erdős Problems][2])

## Best known upper bound in this direction

Graver and Yackel showed an upper bound
[
g_k(n)\ll \left(n\frac{\log\log n}{\log n}\right)^{1-\frac{1}{k-1}},
]
so if your conjectured lower bound is true, it would be essentially tight up to logarithmic factors. ([Erdős Problems][2])

## Bottom line

* **$k=4$: yes** [[nomath]](true, with $c=4/3$ from Mattheus–Verstraëte)[[/nomath]].
* **(k\ge 5): unknown/open**; the best known lower bounds are substantially weaker in the exponent of $n$, and proving your bound would essentially resolve a major open problem about $R(k,t)$.

[1]: https://annals.math.princeton.edu/2024/199-2/p08 "https://annals.math.princeton.edu/2024/199-2/p08"
[2]: https://www.erdosproblems.com/latex/920 "
  
    Erdős Problems
  
"
[3]: https://www.erdosproblems.com/986 "
  
    Erdős Problem #986
  
"
[4]: https://arxiv.org/abs/0908.0429 "https://arxiv.org/abs/0908.0429"

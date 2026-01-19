Let

[
f(n)=\max{\chi(G): |V(G)|=n,; G\text{ triangle-free}}.
]

The correct order of growth is

[
f(n)=\Theta!\left(\sqrt{\frac{n}{\log n}}\right),
]

and the best currently known constants (as of 2025/2026) are

[
(1-o(1))\sqrt{\frac{n}{\log n}}
\le
f(n)
\le
(2+o(1))\sqrt{\frac{n}{\log n}}.
]

([Erdős Problems][1])

## Why (\sqrt{n/\log n}) appears

Two standard ideas connect $f(n)$ to the off-diagonal Ramsey number $R(3,k)$:

1. **Large chromatic number forces small independent sets.**
   If (\chi(G)=t), then a proper $t$-coloring partitions $V(G)$ into $t$ independent sets, so at least one color class has size (\ge n/t). Equivalently,
   [
   \alpha(G)\ge \frac{n}{\chi(G)}\qquad\Rightarrow\qquad \chi(G)\ge \frac{n}{\alpha(G)}.
   ]

2. **Triangle-free + “no large independent set” is exactly what $R(3,k)$ measures.**
   By definition, $R(3,k)$ is the least $N$ such that every $N$-vertex graph contains either a triangle or an independent set of size $k$. So a triangle-free graph with (\alpha(G)<k) can exist only when (n < R(3,k)), and constructions/lower bounds for $R(3,k)$ directly yield triangle-free graphs with small (\alpha(G)), hence large (\chi(G)). ([arXiv][2])

The classical bounds (R(3,k)\asymp k^2/\log k) translate (by inversion) into (\alpha(G)) being typically on the order of (\sqrt{n\log n}) in the “extremal” triangle-free regime, which makes (n/\alpha(G)) on the order of (\sqrt{n/\log n}).

## Best known upper bound

Davies and Illingworth proved that every triangle-free graph on $n$ vertices satisfies

[
\chi(G)\le (2+o(1))\sqrt{\frac{n}{\log n}},
]

so in particular

[
f(n)\le (2+o(1))\sqrt{\frac{n}{\log n}}.
]

([Oxford University Research Archive][3])

## Best known lower bound

A recent construction of Hefty–Horn–King–Pfender gives an improved lower bound on the Ramsey number,
[
R(3,k)\ge \\(\tfrac12+o(1)\\)\frac{k^2}{\log k},
]
which implies the existence of triangle-free graphs on $n$ vertices with chromatic number at least
[
(1-o(1))\sqrt{\frac{n}{\log n}}.
]
Hence
[
f(n)\ge (1-o(1))\sqrt{\frac{n}{\log n}}.
]

([arXiv][4])

## Conclusion

So the sharp estimate (up to a constant factor, and with the best constants currently known) is:

[
f(n)=\Theta\left(\sqrt{\frac{n}{\log n}}\right),
\qquad
(1-o(1))\sqrt{\frac{n}{\log n}}
\le f(n)\le
(2+o(1))\sqrt{\frac{n}{\log n}}.
]

Determining the exact leading constant [[nomath]](i.e., closing the gap between $1$ and $2$)[[/nomath]] remains open. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/1104 "
  
    Erdős Problem #1104
  
"
[2]: https://arxiv.org/pdf/2107.12288 "The -Ramsey problem for triangle-free graphs"
[3]: https://ora.ox.ac.uk/objects/uuid%3Ac53b25cd-63ae-423c-865a-d108c999d638/files/rbv73c1315 "The $\chi$-Ramsey Problem for Triangle-Free Graphs | SIAM Journal on Discrete Mathematics | Vol. 36, No. 2 | Society for Industrial and Applied Mathematics"
[4]: https://arxiv.org/abs/2510.19718?utm_source=chatgpt.com "Improving $R(3,k)$ in just two bites"

This is exactly the Erdős–Hajnal “**locally Ramsey**” problem.

Let (r=r(n)) and for an $n$-vertex graph $G$ define (m_G(r)) to be the smallest $m$ such that **every** vertex subset $S$ with (|S|\ge m) spans **both** a clique (K_r) and an independent set (I_r). [[nomath]](Alon–Bucić–Sudakov use this definition and say $G$ is $(m,r)$-locally Ramsey when $m\ge m_G(r)$.)[[/nomath]] 

Your condition “every induced subgraph on exactly $g(n)$ vertices contains (K_{\log n}) and (I_{\log n})” is equivalent to being ((g(n),\log n))-locally Ramsey, because if it holds for all (|S|=g(n)) then it automatically holds for all larger (|S|\ge g(n)) [[nomath]](just take any $g(n)$-subset of $S$)[[/nomath]].

So the question becomes: how small can (m_G(\log n)) be for an $n$-vertex graph? Denote
[
m_n(r):=\min{m_G(r): |V(G)|=n}.
]

## What is known for (r=\log n)

As of the bounds in Alon’s paper:

### Lower bound [[nomath]](impossibility for too-small $g(n)$)[[/nomath]]

One has
[
m_n(\log n)\ \ge\ \Omega!\left(\frac{(\log n)^3}{\log\log n}\right).
]
Equivalently, if $g(n)$ is asymptotically smaller than ((\log n)^3/\log\log n), **no** $n$-vertex graph can satisfy your requirement. 

In particular, **(g(n)=(\log n)^2) is far too small** [[nomath]](for large $n$)[[/nomath]].

### Upper bound [[nomath]](existence for some subpolynomial $g(n)$)[[/nomath]]

There **does** exist an $n$-vertex graph $G$ with
[
m_G(\log n)\ \le\ 2^{,2^{(\log\log n)^{1/2+o(1)}}},
]
so certainly your property holds for any $g(n)$ at least this large [[nomath]](and still $g(n)=n^{o(1)}$, much smaller than any $n^\varepsilon$)[[/nomath]]. 

Putting these together (as Alon states explicitly),
[
\frac{(\log n)^3}{\log\log n}\ \lesssim\ m_n(\log n)\ \lesssim\ 2^{,2^{(\log\log n)^{1/2+o(1)}}}.
]


## So, what about (g(n)=(\log n)^3)?

This is **open**.

Erdős specifically asked whether one can achieve (m_G(\log n)=(\log n)^3) [[nomath]](i.e., $((\log n)^3,\log n)$-locally Ramsey graphs)[[/nomath]], and Alon notes that “this question remains open.” 

Equivalently: it is not known whether
[
m_n(\log n)\ \le\ (\log n)^3,
]
and Alon also highlights Erdős’ question “whether (m_n(\log n)>(\log n)^3)” and mentions the authors’ suspicion that (m_n(\log n)) might actually exceed every fixed power of (\log n). 

## Bottom line for your “which $g(n)$?” question

* If (g(n) \ll (\log n)^3/\log\log n): **impossible** (no such graph). 
* If (g(n) \ge 2^{2^{(\log\log n)^{1/2+o(1)}}}): **possible** (there exists such a graph). 
* In the wide intermediate regime—**including (g(n)=(\log n)^3)**—the exact threshold is not known.

If you’d like, I can also restate the problem in the equivalent “local Ramsey number” / 2‑coloring formulation mentioned in the same source, which sometimes makes the extremal viewpoint clearer. 

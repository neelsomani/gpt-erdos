Let
[
M_r(n):=\max{e(G): |V(G)|=n,; G\text{ is triangle-free},; \chi(G)\ge r}.
]
Then your (f_r(n)) is exactly
[
f_r(n)=M_r(n)+1,
]
because (f_r(n)) is the first edge threshold above which **no** triangle-free graph with (\chi\ge r) can exist.

## Exact values for (r=2,3,4)

### $r=2$

By Mantel’s theorem, the maximum number of edges in a triangle-free $n$-vertex graph is (\left\lfloor n^2/4\right\rfloor). Hence
[
M_2(n)=\left\lfloor \frac{n^2}{4}\right\rfloor
\quad\Longrightarrow\quad
f_2(n)=\left\lfloor \frac{n^2}{4}\right\rfloor+1.
]
([arXiv][1])

### $r=3$

Erdős–Gallai (and independently Andrásfai) showed that if a triangle-free graph is **not bipartite** [[nomath]](equivalently $\chi\ge 3$)[[/nomath]], then
[
e(G)\le \left\lfloor \frac{(n-1)^2}{4}\right\rfloor+1,
]
and this is sharp. Therefore
[
M_3(n)=\left\lfloor \frac{(n-1)^2}{4}\right\rfloor+1
\quad\Longrightarrow\quad
f_3(n)=\left\lfloor \frac{(n-1)^2}{4}\right\rfloor+2.
]
([arXiv][1])

### $r=4$

A recent result of Ren–Wang–Wang–Yang proves that if $G$ is triangle-free, (\chi(G)\ge 4), and (n\ge 90), then
[
e(G)\le \left\lfloor \frac{(n-3)^2}{4}\right\rfloor+5,
]
with equality achieved by suitable blow-ups of the Grötzsch graph. Hence for (n\ge 90),
[
M_4(n)=\left\lfloor \frac{(n-3)^2}{4}\right\rfloor+5
\quad\Longrightarrow\quad
f_4(n)=\left\lfloor \frac{(n-3)^2}{4}\right\rfloor+6.
]
([arXiv][1])

## General $r$: Simonovits’ asymptotic form (and what’s known about it)

Let (f_t(n;K_3)) denote the maximum number of edges in an $n$-vertex, (K_3)-free graph of chromatic number $t$. Simonovits proved that for each fixed $t$,
[
f_t(n;K_3)=\frac{n^2}{4}-\frac{e_3(t)}{2},n+O(1)\qquad (n\to\infty),
]
where (e_3(t)) is defined as the largest integer $m$ such that **every** (K_3)-free graph $G$ with (\chi(G)=t) must have at least $m$ vertices deleted to become 2‑chromatic (bipartite). ([renyi.hu][2])

Translating to your notation [[nomath]](and noting $f_r(n)=M_r(n)+1$)[[/nomath]], this gives the general asymptotic description:
[
f_r(n)=\frac{n^2}{4}-\frac{e_3(r)}{2}n+O_r(1).
]
[[nomath]](Determining the exact constant term and the exact value of $e_3(r)$ for general $r$ is not known in full generality; the cases $r=2,3,4$ above correspond to $e_3(2)=0$, $e_3(3)=1$, $e_3(4)=3$.)[[/nomath]]

### Growth of (e_3(r)) as (r\to\infty)

The best current bounds imply
[
e_3(r)=\Theta(r^2\log r).
]
One route to these bounds uses:

* Davies–Illingworth’s sharp (up to constants) upper bound on the chromatic number of an $n$-vertex triangle-free graph, (\chi(G)\le (2+o(1))\sqrt{n/\log n}), giving a matching-order **lower bound** on how large a “non-bipartite core” must be to force (\chi\ge r). ([ORA][3])
* Hefty–Horn–King–Pfender’s improved lower bound on the off-diagonal Ramsey number $R(3,k)$, which yields constructions of triangle-free graphs on (\asymp r^2\log r) vertices with chromatic number (\ge r), giving the corresponding **upper bound**. ([arXiv][4])

So, for fixed $r$, the leading term is always (\frac14 n^2), and the dependence on $r$ appears in the **linear** correction term (-\tfrac12 e_3(r)n).

---

### Summary

* (\displaystyle f_2(n)=\left\lfloor \frac{n^2}{4}\right\rfloor+1).
* (\displaystyle f_3(n)=\left\lfloor \frac{(n-1)^2}{4}\right\rfloor+2).
* (\displaystyle f_4(n)=\left\lfloor \frac{(n-3)^2}{4}\right\rfloor+6) for (n\ge 90).
* In general, (\displaystyle f_r(n)=\frac{n^2}{4}-\frac{e_3(r)}{2},n+O_r(1)), with (e_3(r)=\Theta(r^2\log r)). ([renyi.hu][2])

[1]: https://arxiv.org/html/2404.07486v2 "https://arxiv.org/html/2404.07486v2"
[2]: https://www.renyi.hu/~miki/SimSymmDM.pdf "PII: 0012-365X(74)90044-2"
[3]: https://ora.ox.ac.uk/objects/uuid%3Ac53b25cd-63ae-423c-865a-d108c999d638/files/rbv73c1315 "https://ora.ox.ac.uk/objects/uuid%3Ac53b25cd-63ae-423c-865a-d108c999d638/files/rbv73c1315"
[4]: https://arxiv.org/abs/2510.19718 "https://arxiv.org/abs/2510.19718"

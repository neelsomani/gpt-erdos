Let me rewrite your definition in a standard way.

For a finite graph $H$, write
[
\tau(H):=\min{|F|:F\subseteq E(H)\ \text{and}\ H-F\ \text{is bipartite}}.
]
(this is the minimum number of edges you must delete to kill all odd cycles).

Then your function is
[
h_G(n)=\max\bigl{\tau(H): H\subseteq G,\ |V(H)|=n\bigr}.
]
Because (\tau(\cdot)) is monotone in the edge set (adding edges cannot make a graph *easier* to make bipartite), the “worst” choice on a fixed $n$-set of vertices is the **induced** subgraph $G[A]$. So you can also view it as
[
h_G(n)=\max\bigl{\tau(G[A]): A\subseteq V(G),\ |A|=n\bigr}.
]

### Basic bounds for any $G$

For any finite $H$ with $m=e(H)$ edges,
[
\tau(H)= m-\mathrm{maxcut}(H),
]
since keeping a maximum bipartite subgraph is the same as taking a maximum cut.

Also (\mathrm{maxcut}(H)\ge m/2) for every graph (a random bipartition cuts half the edges on average), so
[
\tau(H)\le m/2.
]
Since (m\le \binom{n}{2}), you get the crude universal bound
[
0\le h_G(n)\le \frac12\binom{n}{2}\sim \frac{n^2}{4}.
]

So in general $h_G(n)$ can range from identically $0$ (if $G$ is bipartite) up to order $n^2$ (e.g. if $G$ contains large cliques).

### What is known when $\chi(G)=\aleph_1$

There are two key facts in the Erdős–Hajnal–Szemerédi direction:

1. **Every (\aleph_1)-chromatic graph has (h_G(n)\gg n).**
   In fact, one knows that if (\chi(G)=\aleph_1), then $G$ must contain (for some fixed $r$) **(\aleph_1) many vertex-disjoint odd cycles of the same length (2r+1)**. From $t$ vertex-disjoint odd cycles you need to delete at least $t$ edges to make the graph bipartite (each odd cycle needs at least one edge deleted), so taking about (\lfloor n/(2r+1)\rfloor) of these cycles gives
   [
   h_G(n)\ \ge\ c,n
   ]
   for some constant (c>0) depending on $G$. ([renyi.hu][1])

2. **There exists an (\aleph_1)-chromatic graph with (h_G(n)\ll n^{3/2}).**
   Erdős, Hajnal, and Szemerédi constructed graphs of uncountable chromatic number where every $n$-vertex induced subgraph can be made bipartite by deleting $O(n^{3/2})$ edges; in their paper they state (in their notation) the bound $<2n^{3/2}$. ([renyi.hu][1])

So, for (\chi(G)=\aleph_1), the “known possible range” is:
[
c n \ \lesssim\ h_G(n)\ \lesssim\ n^{3/2}
]
for *some* examples, and (h_G(n)\gtrsim n) for *all* such $G$.

They (Erdős in particular) also conjectured that the $n^{3/2}$ upper bound can be pushed much closer to linear, namely
[
h_G(n)\ \ll\ n^{1+\varepsilon}\quad\text{for every }\varepsilon>0
]
for some (\aleph_1)-chromatic example $G$. ([Erdős Problems][2])

### Your specific question: does (h_G(n)/n\to\infty) for every (\chi(G)=\aleph_1) graph?

As far as the current literature tracking this problem indicates, this is **open**.

* We do know (h_G(n)\gg n) for every such $G$, so (h_G(n)/n) is bounded away from $0$. ([Erdős Problems][2])
* But it is not known (in general) whether $h_G(n)$ must be *superlinear*, i.e. whether (h_G(n)/n\to\infty) for **every** (\aleph_1)-chromatic $G$. The Erdős Problems database lists exactly this as an open problem.

So the honest answer is:

* **General behaviour:** (0\le h_G(n)\le \Theta(n^2)), and for (\chi(G)=\aleph_1) we always have (h_G(n)=\Omega(n)), while there are examples with (h_G(n)=O(n^{3/2})). ([renyi.hu][1])
* **The limit question:** “(h_G(n)/n\to\infty) for every (\aleph_1)-chromatic $G$” is **not settled** (no general proof and no known counterexample).

[1]: https://renyi.hu/~p_erdos/1982-11.pdf "https://renyi.hu/~p_erdos/1982-11.pdf"
[2]: https://www.erdosproblems.com/latex/111 "
  
    Erdős Problems
  
"

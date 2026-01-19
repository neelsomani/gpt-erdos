Let (n\ge k+2) [[nomath]](if $n\le k+1$ the condition is vacuous, so $f(n,k)=0$)[[/nomath]].

## Step 1: Pass to the complement

Let $G$ be an $n$-vertex graph with the stated property, and let (H=\overline{G}) be its complement.

Fix a set (S\subseteq V(G)) with (|S|=k+2). For any (v\in S),
[
\deg_{G[S]}(v)+\deg_{H[S]}(v)=|S|-1=k+1.
]
So
[
\deg_{G[S]}(v)\ge k \quad\Longleftrightarrow\quad \deg_{H[S]}(v)\le 1.
]
Therefore the condition

> every ((k+2))-set induces a subgraph of maximum degree (\ge k) in $G$

is equivalent to

> every ((k+2))-set induces a subgraph having a vertex of degree (\le 1) in $H$,

i.e. **no** ((k+2))-vertex induced subgraph of $H$ has minimum degree (\ge 2).

Since (|E(G)|+;|E(H)|=\binom n2), minimizing (|E(G)|) is the same as maximizing (|E(H)|) subject to that condition.

## Step 2: Reduce to a Turán $forbidden-subgraph$ problem

Let (\mathcal F_k^{\min}) be the finite family of graphs $F$ on $k+2$ vertices such that

* (\delta(F)\ge 2), and
* $F$ is **edge-minimal** with this property [[nomath]](deleting any edge drops the minimum degree below $2$)[[/nomath]].

Then $H$ has the “every ((k+2))-set has a vertex of degree (\le 1)” property **iff** $H$ contains no subgraph isomorphic to any (F\in \mathcal F_k^{\min}). Consequently,
[
\max{|E(H)|:\ H\ \text{satisfies the property}} = \operatorname{ex}(n,\mathcal F_k^{\min}),
]
and hence
[
\boxed{\ f(n,k)=\binom n2-\operatorname{ex}(n,\mathcal F_k^{\min})\ }\qquad (n\ge k+2).
]
This reduction [[nomath]](and the explicit identifications below for $k=1,2,3$)[[/nomath]] is stated in the discussion of Erdős problem #614.

So “determining $f(n,k)$” is equivalent to determining the corresponding Turán number (\operatorname{ex}(n,\mathcal F_k^{\min})). In general this is not known; the problem is listed as open.

## Explicit cases

### $k=1$

Here (\mathcal F_1^{\min}={K_3}), so
[
f(n,1)=\binom n2-\operatorname{ex}(n,K_3)=\binom n2-\left\lfloor \frac{n^2}{4}\right\rfloor.
]
Indeed (\operatorname{ex}(n,K_3)=\lfloor n^2/4\rfloor) by Mantel’s theorem. ([MIT OpenCourseWare][1])

### $k=2$

Here (\mathcal F_2^{\min}={C_4}), so
[
\boxed{\ f(n,2)=\binom n2-\operatorname{ex}(n,C_4)\ }.
]

The exact value of (\operatorname{ex}(n,C_4)) is the classical (C_4) (Zarankiewicz) extremal problem; asymptotically
[
\operatorname{ex}(n,C_4)\sim \tfrac12n^{3/2}
]
so
[
f(n,2)=\binom n2-\left(\tfrac12+o(1)\right)n^{3/2}.
]
([MathOverflow][2])

### $k=3$

One can take
[
\mathcal F_3^{\min}={C_5\ K_{2,3}\ K_1\vee 2K_2}
]
[[nomath]](where $K_1\vee 2K_2$ denotes the join of a single vertex with two disjoint edges)[[/nomath]], giving
[
\boxed{\ f(n,3)=\binom n2-\operatorname{ex}\bigl(n,{C_5,K_{2,3},K_1\vee 2K_2}\bigr)\ }.
]

## What can be said for general $k$?

The exact closed form of $f(n,k)$ for general $k$ is not currently known in the literature; the general problem is open.

What *is* clean and general is the Turán reduction:
[
f(n,k)=\binom n2-\operatorname{ex}(n,\mathcal F_k^{\min}),
]
with (\mathcal F_k^{\min}) as above.

As a quick general upper bound on the complement extremal number: (\mathcal F_k^{\min}) contains (K_{2,k}) [[nomath]](it has $k+2$ vertices, minimum degree $\ge 2$, and is edge-minimal)[[/nomath]], so
[
\operatorname{ex}(n,\mathcal F_k^{\min})\le \operatorname{ex}(n,K_{2,k}).
]
By the Kővári–Sós–Turán theorem, (\operatorname{ex}(n,K_{2,k})=O(n^{3/2})) [[nomath]](more precisely $\le \tfrac12\sqrt{k-1},n^{3/2}+O(n)$)[[/nomath]]. ([UserPages][3])

So for each fixed (k\ge 2),
[
f(n,k)=\binom n2 - O(n^{3/2}).
]

If you tell me whether you want $i$ exact values for small $k$ and $n$, (ii) asymptotics/bounds for fixed $k$ as (n\to\infty), or (iii) an explicit description/listing of (\mathcal F_k^{\min}) for a particular $k$, I can focus the discussion accordingly.

[1]: https://ocw.mit.edu/courses/18-225-graph-theory-and-additive-combinatorics-fall-2023/mit18_225_f23_lec02-05.pdf "https://ocw.mit.edu/courses/18-225-graph-theory-and-additive-combinatorics-fall-2023/mit18_225_f23_lec02-05.pdf"
[2]: https://mathoverflow.net/questions/251959/maximum-number-of-edges-in-bipartite-graph-without-cycles-of-length-4 "Maximum number of edges in bipartite graph without cycles of length 4 - MathOverflow"
[3]: https://page.mi.fu-berlin.de/szabo/PDF/notes.pdf "https://page.mi.fu-berlin.de/szabo/PDF/notes.pdf"

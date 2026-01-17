Fix a large $n$ and write
[
k:=\left\lceil \sqrt n\right\rceil,\qquad K:={k,k+1,\dots,2k-1}.
]

Think of a block (A_i\subseteq[n]) of size (|A_i|=t) as a copy of the clique (K_t) on the vertex set (A_i). Then a pairwise balanced design with block-sizes in $K$ is exactly a decomposition of the complete graph (K_n) into cliques whose orders lie in $K$.

### Step 1: existence of a $K$-PBD for all large $n$

Let (\mathcal G:={K_t: t\in K}) be the (finite) family of allowed cliques. Lamken–Wilson’s existence theory for (\mathcal G)-decompositions gives: for all sufficiently large $n$, there is a (\mathcal G)-decomposition of (K_n) provided the standard divisibility conditions (\alpha(\mathcal G)\mid (n-1)) and (\beta(\mathcal G)\mid n(n-1)) hold. ([UVicSpace][1])

For cliques, (\deg(K_t)=t-1) and (|E(K_t)|=\binom t2). Hence
[
\alpha(\mathcal G)=\gcd{t-1:t\in K}=\gcd{k-1,k,\dots,2k-2}=1,
]
so (\alpha(\mathcal G)\mid(n-1)) is automatic. Also
[
\beta(\mathcal G)=2\gcd\\{\binom t2:t\in K\\},
]
and because $K$ contains at least three consecutive values once (k\ge 3), the set ({\binom t2}) has gcd $1$, so (\beta(\mathcal G)=2). Then (\beta(\mathcal G)\mid n(n-1)) holds for every $n$ since $n(n-1)$ is always even.

So, for all sufficiently large $n$, there exists a nontrivial PBD on $[n]$ whose block sizes all lie in $[k,2k-1]$ [[nomath]](hence $<n$)[[/nomath]].

### Step 2: enforce that no size occurs more than $O(\sqrt n)$ times

Among such decompositions, one can arrange **prescribed proportions of each block type/size** (this is explicitly noted as achievable in the graph-decomposition framework). ([UVicSpace][1])

So choose the proportions so that, up to (1+o(1)) factors, each size (t\in K) appears equally often. Concretely, we target
[
m_t \approx \frac{m}{|K|}\qquad (t\in K),
]
where (m=) total number of blocks and (m_t=|\\{i:|A_i|=t\\}|).

Now (t\in[k,2k-1]) implies (\binom{k}{2}\le \binom{t}{2}\le \binom{2k}{2}). Since the blocks partition all (\binom{n}{2}) pairs,
[
\binom{n}{2}=\sum_{t\in K} m_t\binom{t}{2},
]
so $m$ satisfies the crude bounds
[
\frac{\binom{n}{2}}{\binom{2k}{2}}\ \le\ m\ \le\ \frac{\binom{n}{2}}{\binom{k}{2}}.
]
With (k\asymp \sqrt n), both sides are (\Theta(n)), i.e. (m=\Theta(n)).

Since (|K|=k=\Theta(\sqrt n)), distributing the block sizes roughly evenly gives
[
m_t = \Theta!\left(\frac{n}{k}\right)=\Theta(\sqrt n)
]
for every (t\in K). In particular, for every $t$,
[
|\\{i:|A_i|=t\\}| = O(\sqrt n),
]
as required.

### What you can take as the explicit “answer”

For each large $n$, take (k=\lceil\sqrt n\rceil) and a PBD on $[n]$ whose block sizes lie in ({k,k+1,\dots,2k-1}) with (approximately) equal proportions of each size; existence follows from the Lamken–Wilson existence theorem for (\mathcal G)-decompositions together with the standard “prescribed proportion of block types” refinement in this framework. ([UVicSpace][1])

This gives a nontrivial PBD (A_1,\dots,A_m\subseteq[n]) with the stated $O(n^{1/2})$ bound for each fixed block size.

[1]: https://dspace.library.uvic.ca/bitstreams/bf55353f-40d0-4192-84c9-4627f762734b/download "https://dspace.library.uvic.ca/bitstreams/bf55353f-40d0-4192-84c9-4627f762734b/download"
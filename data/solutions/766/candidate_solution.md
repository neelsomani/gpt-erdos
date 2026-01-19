Write (f(n;k,\ell)=\min{\mathrm{ex}(n;G): |V(G)|=k,\ |E(G)|=\ell}). [[nomath]](I’ll use $\ell$ for the number of edges to avoid confusion with $l$.)[[/nomath]]

## 1. Easy structural reductions

* **Isolated vertices don’t matter [[nomath]](for $n\ge k$)[[/nomath]].**
  If $G$ has isolated vertices, deleting them gives (G') with (\mathrm{ex}(n;G)=\mathrm{ex}(n;G')) once (n\ge k), because any copy of (G') can be extended to a copy of $G$ by mapping isolated vertices to unused vertices. So in minimizing, one may as well assume $G$ has no isolates.

* **In your range (,k<\ell\le k^2/4), the minimizer is bipartite [[nomath]](for large $n$)[[/nomath]].**
  Since (\ell\le k^2/4), there exist bipartite graphs on $k$ vertices with (\ell) edges. Any non‑bipartite forbidden graph has (\mathrm{ex}(n;G)=\Theta(n^2)) (Erdős–Stone–Simonovits), whereas bipartite forbidden graphs have (\mathrm{ex}(n;G)=o(n^2)). Thus for fixed (k,\ell) and large $n$, the minimum will be attained by a bipartite $G$.

## 2. Monotonicity in (\ell): always nondecreasing

For fixed (n,k), the function (\ell\mapsto f(n;k,\ell)) is **monotone nondecreasing** (no asymptotics needed):

If (\ell_2>\ell_1) and $G$ has $k$ vertices and (\ell_2) edges, pick any (\ell_1)-edge subgraph (H\subseteq G) on the same $k$ vertices [[nomath]](delete $\ell_2-\ell_1$ edges)[[/nomath]]. Then (H\subseteq G) implies
[
\mathrm{ex}(n;H)\le \mathrm{ex}(n;G).
]
Taking minima over $H$ with (\ell_1) edges and then over $G$ with (\ell_2) edges gives
[
f(n;k,\ell_1)\le f(n;k,\ell_2).
]

So the real issue is **strictness**.

### Is it *strictly* monotone for fixed $k$ and large $n$?

As far as I know, **this is open in general** (it’s asked explicitly in Erdős’s problem list in essentially this form). ([Erdős Problems][1])

Two remarks:

* Outside your range [[nomath]](when $\ell>k^2/4$)[[/nomath]], strictness definitely fails: every such $k$-vertex graph is non‑bipartite, and many different (\ell)’s give the same asymptotic (\sim \tfrac14 n^2) coming from (\chi(G)=3); Dirac–Erdős showed for (\ell=\lfloor k^2/4\rfloor+1) one already has (f(n;k,\ell)\le \lfloor n^2/4\rfloor+1). ([Erdős Problems][1])
  So strict monotonicity cannot hold globally across all (\ell).

* Within the bipartite range (\ell\le k^2/4), I don’t know a general proof of strictness, and the landscape is messy because even for specific small bipartite graphs the exact Turán asymptotics/constants can be unknown (Zarankiewicz-type difficulties). This is one reason strictness is hard.

## 3. General lower bound in terms of $(k,\ell)$

A very robust (though often not tight) lower bound comes from the standard random‑graph deletion method:

For any graph $G$ with (v(G)=k) and (e(G)=\ell),
[
\mathrm{ex}(n;G)\ \ge\ c(G) n^{2-\frac{k-2}{\ell-1}}.
]
This is a standard corollary of the Erdős–Rényi random construction (see e.g. Zhao’s notes). ([Yufei Zhao][2])

Since for fixed (k,\ell) there are only finitely many isomorphism types, you can take the minimum constant over all such $G$ and get
[
f(n;k,\ell)\ \ge\ c_{k\ell} n^{2-\frac{k-2}{\ell-1}}.
]
This gives at least the right qualitative behavior: as (\ell\downarrow k), the exponent approaches $1$, and as (\ell) grows, the exponent approaches $2$.

## 4. General upper bound via Kővári–Sós–Turán

Let
[
s=s(k,\ell):=\min\\{1\le s\le \lfloor k/2\rfloor:\ \ell\le s(k-s)\\}.
]
Equivalently, $s$ is the **smallest possible size of the smaller side** in a bipartite graph on $k$ vertices that can support (\ell) edges.

Then choose any bipartite graph $G$ on parts of size $s$ and $k-s$ with exactly (\ell) edges; necessarily (G\subseteq K_{s,k-s}). Since (G\subseteq K_{s,k-s}) implies every $G$-free graph is also (K_{s,k-s})-free, we have
[
\mathrm{ex}(n;G)\le \mathrm{ex}(n;K_{s,k-s}).
]
By the Kővári–Sós–Turán theorem,
[
\mathrm{ex}(n;K_{s,t})\ \le\ C_{s,t}, n^{,2-\frac1s}+O(n),
]
so here
[
f(n;k,\ell)\ \le\ C_{k,\ell}, n^{,2-\frac1{s(k,\ell)}}+O(n).
]
([Yufei Zhao][2])

This bound is often reasonably sharp when (\ell) is large [[nomath]](so $s$ is large)[[/nomath]], because both the random lower bound exponent (2-\frac{k-2}{\ell-1}) and the KST upper exponent (2-\frac1s) are then close to $2$.

## 5. Much better upper bounds when (\ell) is near $k$ (theta graphs)

When (\ell) is only a little bigger than $k$, you can build forbidden graphs whose extremal number is close to linear by forcing a *long* even cycle structure. A good way is via **theta graphs**.

A (generalized) theta graph consists of $q$ internally vertex‑disjoint paths between two vertices. If all paths have length (\ge 2), then
[
|E|-|V| = q-2.
]
So if you set
[
q = \ell-k+2,
]
and can realize $q$ paths each of length at least $2$, you can hit exactly (|V|=k, |E|=\ell). The condition “all path lengths (\ge2)” is exactly
[
\ell \ge 2q\ \Longleftrightarrow\ \ell \le 2k-4.
]
So in the regime
[
k<\ell\le 2k-4,
]
you can choose a theta‑type forbidden graph $G$ whose **shortest cycle length** is about (2r), where
[
r \approx \left\lfloor \frac{\ell}{q}\right\rfloor = \left\lfloor \frac{\ell}{\ell-k+2}\right\rfloor.
]

Known results (Faudree–Simonovits and later refinements for generalized theta graphs) give
[
\mathrm{ex}(n;G)=O\left(n^{,1+\frac1r}\right),
]
and since $G$ contains an even cycle (C_{2r}), Bondy–Simonovits gives the matching lower‑order exponent (\mathrm{ex}(n;C_{2r})=\Omega(n^{1+1/r})), hence theta graphs really have exponent (1+1/r). ([Mathematical Sciences Department][3])

Therefore, for (k<\ell\le 2k-4),
[
f(n;k,\ell)\ \le\ C_{k,\ell} n^{1+\frac1r}
\quad\text{with}\quad
r=\left\lfloor \frac{\ell}{\ell-k+2}\right\rfloor,
]
which can be dramatically smaller than the KST (n^{2-1/s}) bound when (\ell) is close to $k$. [[nomath]](For example, if $\ell=k+1$, then $q=3$ and $r$ is on the order of $k/3$, giving an exponent $1+O(1/k)$.)[[/nomath]]

## 6. Summary of “good estimates” across (k<\ell\le k^2/4)

For fixed (k,\ell) and (n\to\infty), the best general-purpose bounds you can write down in terms of $(k,\ell)$ alone are:

* **Universal lower bound** (random method):
  [
  f(n;k,\ell)\ \ge\ c_{k,\ell} n^{2-\frac{k-2}{\ell-1}}.
  ]
  ([Yufei Zhao][2])

* **Universal upper bound** [[nomath]](KST, using $s=s(k,\ell)$ defined by $\ell\le s(k-s)$)[[/nomath]]:
  [
  f(n;k,\ell)\ \le\ C_{k,\ell} n^{2-\frac1{s(k,\ell)}}+O(n).
  ]
  ([Yufei Zhao][2])

* **Sharper upper bound for (k<\ell\le 2k-4)** (theta construction):
  [
  f(n;k,\ell)\ \le\ C'_{k,\ell} n^{1+\frac1{r}}
  \quad\text{where } r=\left\lfloor \frac{\ell}{\ell-k+2}\right\rfloor\ge 2.
  ]
  ([Mathematical Sciences Department][3])

These bounds already show the right qualitative picture: as (\ell) increases from $k$ toward (k^2/4), the best known upper exponents interpolate from nearly $1$ (very close to linear) up toward nearly $2$ (almost quadratic).

## 7. On strict monotonicity (within the bipartite range)

* **Nondecreasing is easy and always true** (argument above).
* **Strictly increasing** for fixed $k$ and all sufficiently large $n$: **open in general** (and explicitly asked by Erdős). ([Erdős Problems][1])

If you want, tell me a specific fixed $k$ [[nomath]](say $k\le 10$ or $k\le 12$)[[/nomath]], and I can go case-by-case through plausible minimizers [[nomath]](theta graphs vs. $K_{s,t}$-type graphs)[[/nomath]] and what the best-known asymptotics are for those forbidden graphs; for small $k$ one can often narrow down the candidates sharply even if exact constants remain unknown.

[1]: https://www.erdosproblems.com/search_bib/Er64c/no "https://www.erdosproblems.com/search_bib/Er64c/no"
[2]: https://yufeizhao.com/gtacbook/1.pdf "https://yufeizhao.com/gtacbook/1.pdf"
[3]: https://www.math.cmu.edu/~mtait/thetaturan.pdf "https://www.math.cmu.edu/~mtait/thetaturan.pdf"

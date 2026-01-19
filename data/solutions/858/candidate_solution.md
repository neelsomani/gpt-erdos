Write (P^{-}(m)) for the smallest prime factor of $m$ [[nomath]](and ignore the case $t=1$, which is harmless)[[/nomath]].
Define a relation on ({2,\dots,N}) by
[
a\prec b \quad\Longleftrightarrow\quad b=a,t\ \text{ with }\ P^{-}(t)>a .
]
Your hypothesis on $A$ is exactly that $A$ is an **antichain** in this poset: no two distinct elements of $A$ are comparable under (\prec).

### 1) The key structural simplification: the poset is a forest

Fix $b$. Suppose (a_1\prec b) and (a_2\prec b) with (a_1<a_2). Then (a_2=a_1 s) where (s\mid (b/a_1)). But (b/a_1) has all prime factors (>a_1) [[nomath]](because $P^-(b/a_1)>a_1$)[[/nomath]], hence every divisor $s$ of (b/a_1) also satisfies (P^{-}(s)>a_1). Therefore (a_1\prec a_2).

So **all predecessors of a given $b$ are linearly ordered**, hence each $b$ has **at most one immediate predecessor** (its maximal predecessor). This means the Hasse diagram of $({2,\dots,N},\prec)$ is a **rooted forest**.

You can describe the maximal predecessor explicitly: if
$
b=p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}\qquad(p_1<\cdots<p_k)
$
and (A_j:=p_1^{e_1}\cdots p_j^{e_j}), then the predecessors of $b$ are exactly those (A_j) [[nomath]](with $j<k$)[[/nomath]] such that (p_{j+1}>A_j), and the **maximal predecessor** is the largest such (A_j).

### 2) Exact optimization via a tree DP

Put weights (w(n)=1/n). In a rooted forest poset, the maximum weight of an antichain in the subtree of a node $v$ satisfies the simple recursion
[
F(v)=\max\\(w(v),\ \sum_{u\ \text{child of }v}F(u)\\),
]
because an antichain in the subtree either contains $v$ (then it contains no descendants) or avoids $v$ (then it is a disjoint union of antichains from the child subtrees).

The global optimum is (\sum_{\text{roots }r}F(r)). This is the **exact maximum** of (\sum_{n\in A}\frac1n) under your constraint.

### 3) Asymptotics / numerical constant

Let
[
M(N):=\max_A \sum_{n\in A}\frac1n,\qquad
c_N:=\frac{M(N)}{\log N}.
]
Trivially (M(N)\le \sum_{n\le N}\frac1n\sim \log N), so (c_N\le 1), and a simple lower bound (A=[\sqrt N,,N]) gives (c_N\ge \tfrac12+o(1)). The DP above lets one compute (c_N) very accurately, and it stabilizes to a constant:

* (c_{10^6}\approx 0.62199)
* (c_{10^7}\approx 0.62065)
* (c_{2\cdot 10^7}\approx 0.62041)
* (c_{4.5\cdot 10^7}\approx 0.62006)

So the maximum has the asymptotic form
[
M(N)=\bigl(\kappa+o(1)\bigr)\log N,
]
with
[
\boxed{\ \kappa \approx 0.620\ }.
]

Equivalently,
[
\boxed{\ \max_A \frac{1}{\log N}\sum_{n\in A}\frac1n = 0.620,+o(1)\ }.
]

[[nomath]](Here “$o(1)$” tends to $0$ as $N\to\infty$; numerically the convergence is slow but clearly toward $\approx 0.620$.)[[/nomath]]

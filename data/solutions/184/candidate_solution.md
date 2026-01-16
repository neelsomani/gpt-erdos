What you wrote is **exactly the Erdős–Gallai cycle decomposition conjecture** (from the 1960s):

> *Does every $n$-vertex graph admit a partition of its edge set into $O(n)$ edge-disjoint cycles and single edges?* ([arXiv][1])

As of the latest results I can verify online, **this is still open in full generality**. ([arXiv][2])

### What is known (best general bounds)

There has been steady progress on the best bound “known for all graphs”:

* Erdős–Gallai observed an easy argument giving **(O(n\log n))** cycles+edges by repeatedly removing a long cycle. ([arXiv][3])
* Conlon–Fox–Sudakov (2014) improved this to **(O(n\log\log n))**. ([arXiv][3])
* Bucić–Montgomery (final journal version 2024) further improved it to **(O(n\log^{*}!n))**, where (\log^{*}) is the iterated logarithm. ([arXiv][1])

So we are *very* close to linear—(\log^{*} n) grows extremely slowly—but **true $O(n)$** is not yet established. ([arXiv][1])

---

## A clean proof of the easy (O(n\log n)) bound (to contrast with the conjecture)

Let $G$ be a graph on $n$ vertices with $m$ edges.

### Lemma 1 (Long cycle from minimum degree)

If a graph $H$ has minimum degree (\delta(H)=\delta\ge 2), then $H$ contains a cycle of length at least (\delta+1).

**Proof.** Take a longest path (P=v_0v_1\cdots v_k). Since $P$ is longest, every neighbor of (v_0) lies on $P$. Vertex (v_0) has at least (\delta) neighbors on $P$, so among them there is one with index (i\ge \delta). Then (v_0v_1\cdots v_i v_0) is a cycle of length (i+1\ge \delta+1). ∎

### Lemma 2 (Subgraph with decent minimum degree)

Any graph with average degree (\bar d) contains a (nonempty) subgraph $H$ with
[
\delta(H)\ \ge\ \bar d/2.
]
[[nomath]](Equivalently, if $m$ edges on $n$ vertices, there is a subgraph with $\delta(H)\ge m/n$, since $\bar d=2m/n$.)[[/nomath]]

This is a standard “degeneracy/core” fact: the degeneracy $k$ satisfies (m\le kn), hence (k\ge m/n), and by definition of degeneracy there is a subgraph with minimum degree $k$.

### Now the iterative removal argument

If (m<2n), we can just leave all edges as single edges: that’s (<2n) pieces already.

So assume (m\ge 2n). Then (\bar d = 2m/n \ge 4). By Lemma 2, $G$ has a subgraph $H$ with
[
\delta(H)\ \ge\ \bar d/2\ =\ m/n\ \ge\ 2.
]
By Lemma 1, $H$ (hence $G$) contains a cycle of length at least (\delta(H)+1 \ge m/n) (up to a harmless “$+1$”).

Remove the edges of such a cycle. If the current graph has (m_t) edges, then after removing a cycle we have
[
m_{t+1}\ \le\ m_t - \frac{m_t}{n}\ =\ m_t\Bigl(1-\frac{1}{n}\Bigr).
]
Thus after $t$ cycles,
[
m_t\ \le\ m_0\Bigl(1-\frac{1}{n}\Bigr)^t\ \le\ m_0 e^{-t/n}.
]
Take (t = n\ln(m_0/n)). Then (m_t \le n). Since (m_0\le \binom{n}{2}<n^2), we get (t = O(n\log n)).

Finally, when fewer than $n$ edges remain, take them as single edges. Total pieces:
[
O(n\log n)\ \text{cycles} \ +\ O(n)\ \text{edges} \ =\ O(n\log n).
]

This is the classical “easy” bound mentioned in the literature. ([arXiv][3])

---

## Bottom line

* The exact statement “**$O(n)$** cycles and edges always suffice” is the **Erdős–Gallai conjecture** and is **still open**. ([arXiv][2])
* The best general theorem currently known is **(O(n\log^{*} n))** cycles and edges (Bucić–Montgomery, 2024), improving **(O(n\log\log n))** (Conlon–Fox–Sudakov, 2014). ([arXiv][1])

If you tell me what level of detail you want (high-level ideas vs. technical ingredients), I can also summarize *why* the newer proofs manage to shave (\log n) down to (\log\log n) and then to (\log^{*}n).

[1]: https://arxiv.org/abs/2211.07689 "[2211.07689] Towards the Erdős-Gallai Cycle Decomposition Conjecture"
[2]: https://arxiv.org/html/2509.01901v2 "Tight Bounds for Cycle-Edge Decompositions and Covers"
[3]: https://arxiv.org/abs/1310.0632 "[1310.0632] Cycle packing"

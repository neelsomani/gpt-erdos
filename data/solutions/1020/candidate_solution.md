What you wrote is (essentially) the **Erdős Matching Conjecture** for $r$-uniform hypergraphs: the extremal number of edges in an $r$-graph on $n$ vertices with **matching number** (<k) [[nomath]](i.e., with no $k$ pairwise disjoint/independent edges)[[/nomath]]. ([Kupavskii][1])

Two important caveats:

### 1) As stated, it cannot hold for all $n$

If (n<rk), then a matching of size $k$ is impossible [[nomath]](it would need $rk$ distinct vertices)[[/nomath]]. So **every** $r$-uniform hypergraph on $n$ vertices automatically contains no $k$ disjoint edges, and hence
[
f(n;r,k)=\binom{n}{r}\qquad\text{for }n<rk.
]
But your formula can exceed (\binom{n}{r}) when (n<rk) [[nomath]](e.g. $r=3,k=2,n=4$ gives $\max{\binom{5}{3},\binom{4}{3}-\binom{3}{3}}=\max{10,3}=10>\binom{4}{3}=4$)[[/nomath]].

So the “interesting” regime is (n\ge rk) [[nomath]](often stated as $n>rk$ or $n\ge rk$, depending on conventions)[[/nomath]]. ([Kupavskii][1])

### 2) For (r\ge 4), the equality is **not known in full generality**

The identity
[
f(n;r,k)=\max\\{\binom{rk-1}{r},\ \binom{n}{r}-\binom{n-k+1}{r}\\}
]
[[nomath]](for $n\ge rk$)[[/nomath]] is precisely the Erdős Matching Conjecture, and it is **still not completely solved** in general. ([arXiv][2])

---

## Why the RHS always gives a lower bound

Even without the full conjecture, it’s easy (and standard) to see
[
f(n;r,k)\ \ge\ \max\\{\binom{rk-1}{r},\ \binom{n}{r}-\binom{n-k+1}{r}\\}.
]
These come from two explicit constructions (the same two families that appear in standard statements of EMC). ([Kupavskii][1])

### Construction A: clique on $rk-1$ vertices

Take the complete $r$-uniform hypergraph on a set (V') of size $rk-1$, and [[nomath]](if $n>rk-1$)[[/nomath]] add [[nomath]](n-$rk-1$)[[/nomath]] isolated vertices.

* Number of edges: (\binom{rk-1}{r}).
* No $k$ disjoint edges: $k$ disjoint $r$-edges would require at least $rk$ distinct vertices, but we only have $rk-1$ “active” vertices.

So
[
f(n;r,k)\ge \binom{rk-1}{r}.
]

### Construction B: all edges meeting a fixed ((k-1))-set

Fix a set (S\subseteq [n]) of size (|S|=k-1), and take
[
\mathcal H={e\in \binom{[n]}{r}:\ e\cap S\neq\emptyset}.
]

* Any matching in (\mathcal H) uses distinct vertices of $S$, so it has size at most (|S|=k-1). Hence no $k$ disjoint edges.
* Count edges:
  [
  |\mathcal H|=\binom{n}{r}-\binom{n-(k-1)}{r}
  =\binom{n}{r}-\binom{n-k+1}{r}.
  ]

So
[
f(n;r,k)\ge \binom{n}{r}-\binom{n-k+1}{r}.
]

These are exactly the two candidate extremal families in the EMC statement. ([Kupavskii][1])

---

## What is actually known (as of the recent literature)

* The formula is **true for graphs** ((r=2)) (Erdős–Gallai).
* It is also **known to be true for $r=3$** (the 3-uniform case) according to standard surveys/notes [[nomath]](e.g. the summary listing “True for $k=3$” in the $k$-uniform notation)[[/nomath]]. ([Kupavskii][1])
* For general $r$, it is proved in various ranges where $n$ is **sufficiently large compared to $rk$**; modern work continues to expand the range (e.g. Frankl–Kupavskii type bounds). ([arXiv][3])
* But **it is still not fully solved** in the complete range of parameters for all (r\ge 4). ([arXiv][2])

---

## The “correct” clean statement to keep in mind

A fully correct way to write it, without hidden assumptions, is:

$
f(n;r,k)=
\begin{cases}
\binom{n}{r}, & n<rk,
\max\\{\binom{rk-1}{r},\ \binom{n}{r}-\binom{n-k+1}{r}\\}, & n\ge rk,
\end{cases}
$
**conjecturally** for all (r\ge 2), and **proven** in a number of important cases and parameter ranges. ([Kupavskii][1])

---

If you tell me which regime you care about [[nomath]](e.g. fixed $r$ and $k$ with $n$ large, or the borderline cases $n\approx rk$)[[/nomath]], I can walk through the strongest *proven* bound in that regime and how it relates to the two extremal constructions above.

[1]: https://kupavskii.com/wp-content/uploads/2018/06/FK-EMC.pdf "The Erdos Matching Conjecture  and related questions"
[2]: https://arxiv.org/html/2601.06871v1 "Nearly Erdős-Ko-Rado theorems"
[3]: https://arxiv.org/abs/1806.08855 "[1806.08855] The Erdős Matching Conjecture and concentration inequalities"

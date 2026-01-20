The statement you wrote is exactly the **Erdős–Sós conjecture**:

[
e(G)>\frac{k-1}{2}n \quad \Longleftrightarrow \quad \overline d(G)=\frac{2e(G)}n>k-1,
]
and the conjecture says that **every** $n$-vertex graph of average degree (>k-1) contains **every** tree on $k+1$ vertices [[nomath]](equivalently, every tree with $k$ edges)[[/nomath]]. 

## Status (as of early 2026)

This is **open in full generality**: it is listed as an open Erdős problem (#548) and the literature still treats the general case as unsolved. ([Erdős Problems][1])

There has long been an **announced proof for sufficiently large $k$** by Ajtai–Komlós–Simonovits–Szemerédi, but it is widely noted as **unpublished / hard to locate**. ([MathOverflow][2])

## Why the bound is “best possible”

You cannot hope for a smaller coefficient than (\frac{k-1}{2}), because there are extremal constructions with exactly (\frac{k-1}{2}n) edges and **no** connected subgraph on $k+1$ vertices:

* If (k\mid n), take a disjoint union of $n/k$ copies of (K_k). Then
  [
  e(G)=\frac{n}{k}\binom{k}{2}=\frac{k-1}{2},n,
  ]
  but every component has size $k$, so $G$ contains **no** tree on $k+1$ vertices [[nomath]](indeed no connected $(k+1)$-vertex subgraph at all)[[/nomath]].

Also, equality in “average degree (=k-1)” really can fail: e.g. $K_{k-1,k-1}$ has average degree $k-1$ but does **not** contain the $k$-edge star [[nomath]](maximum degree is only $k-1$)[[/nomath]]; disjoint unions give larger examples. 

So the conjecture is tight up to the strictness “(>)” [[nomath]](your “$+1$” edge)[[/nomath]].

## What *is* known (examples of partial progress)

Many special cases are proved. For instance:

* It holds for **paths** (via the Erdős–Gallai theorem) and for **stars/double stars** by easy degree arguments. 
* It holds for all **spiders** [[nomath]](trees with at most one vertex of degree $>2$)[[/nomath]]. ([ScienceDirect][3])
* It is proved for various **restricted host graphs** [[nomath]](e.g. certain girth / $C_4$-free conditions)[[/nomath]]. ([Erdős Problems][1])
* There are results for **graphs of order (n=k+c)** for small fixed $c$ (e.g. (k, k+1, k+2,\dots)). ([Erdős Problems][1])
* There are modern “near-spanning / bounded-degree / approximate” confirmations in regimes where $n$ is close to (|T|) or (\Delta(T)) is controlled. ([arXiv][4])

So: lots is known, but the clean universal bound (\frac{k-1}{2}n) for **all** trees and **all** (n\ge k+1) remains the big target.

## A closely related statement you *can* prove easily (the “factor 2” version)

What *is* easy (and is often mentioned as the trivial barrier) is the following stronger hypothesis:

> If (e(G)\ge (k-1)n+1), then $G$ contains every tree on $k+1$ vertices.

This is proved by a standard pruning + leaf-extension induction, and it’s explicitly noted in the Erdős problem discussion. ([Erdős Problems][1])

Here is the proof.

### Step 1: Find a subgraph of minimum degree (\ge k)

Start with $G$ on $n$ vertices with (e(G)>(k-1)n).

Repeatedly delete a vertex of degree (\le k-1) (and all edges incident to it). Each deletion removes at most $k-1$ edges.

If this process deleted all $n$ vertices, it would remove at most $(k-1)n$ edges total, contradicting (e(G)>(k-1)n). Hence the process stops with a nonempty subgraph (H\subseteq G) having
[
\delta(H)\ge k.
]

### Step 2: Any graph with (\delta(H)\ge k) contains every $(k+1)$-vertex tree

We prove by induction on $k$ (number of edges of the tree).

Let $T$ be a tree with $k$ edges [[nomath]](so $k+1$ vertices)[[/nomath]]. Choose a leaf (x\in V(T)) with neighbor $y$, and set (T':=T-x). Then (T') is a tree with $k-1$ edges.

By induction, $H$ contains a copy of $T'$. Let (v\in V(H)) be the image of $y$. In the embedding of $T'$, the vertex $v$ is adjacent to the images of the neighbors of $y$ in $T'$; there are exactly (\deg_{T'}(y)=\deg_T(y)-1\le k-1) such vertices.

But (\deg_H(v)\ge \delta(H)\ge k), so $v$ has at least one neighbor not yet used in the embedding. Map the deleted leaf $x$ to such an unused neighbor of $v$. This extends the embedding from $T'$ to $T$.

So $H$ [[nomath]](and therefore $G$)[[/nomath]] contains $T$.

---

This argument shows why the Erdős–Sós conjecture is often described as “hard”: the simple pruning method gives a clean proof once you can force (\delta\ge k), but pushing the edge threshold down from $(k-1)n$ to (\frac{k-1}{2}n) is exactly the nontrivial content of the conjecture. 

If you tell me whether you want $i$ a proof for particular families of trees (paths, spiders, bounded-degree trees), or (ii) a discussion of the best known general bounds toward $(k-1)n/2$, I can tailor the next step.

[1]: https://www.erdosproblems.com/forum/thread/548 "

    Erdős Problem #548 - Discussion thread

"
[2]: https://mathoverflow.net/questions/429422/outline-of-the-unpublished-proof-of-erd%C5%91s-s%C3%B3s-conjecture "reference request - Outline of the unpublished proof of Erdős-Sós conjecture - MathOverflow"
[3]: https://www.sciencedirect.com/science/article/pii/S0012365X13003324 "The Erdős–Sós conjecture for spiders of large size - ScienceDirect"
[4]: https://arxiv.org/abs/2405.15733 "[2405.15733] Embedding Nearly Spanning Trees"

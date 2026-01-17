Write (\mathrm{ex}(n,H)) for the usual Turán/extremal number: the maximum number of edges in an $n$-vertex graph containing no (not-necessarily-induced) copy of $H$. For the $k$-dimensional cube (Q_k) [[nomath]](with $v(Q_k)=2^k$, $e(Q_k)=k2^{k-1}$)[[/nomath]], the exact asymptotics are known only for (k\le 2); for (k\ge 3) the problem is still open. What *is* known is the following (best current bounds).

## Small dimensions

### $k=2$: (Q_2=C_4)

[
\mathrm{ex}(n,Q_2)=\mathrm{ex}(n,C_4)=\Big(\tfrac12+o(1)\Big)n^{3/2}.
]
This follows from the classical (C_4) upper bound (Kővári–Sós–Turán/Reiman) together with polarity-graph constructions from finite projective planes. ([arXiv][1])

### $k=3$: the cube

Erdős–Simonovits proved the best known upper bound
[
\mathrm{ex}(n,Q_3)=O\left(n^{8/5}\right),
]
and the best known lower bound is
[
\mathrm{ex}(n,Q_3)=\Omega(n^{3/2}),
]
coming from the fact that (Q_3) contains a $4$-cycle [[nomath]](so any $C_4$-free extremal construction is $Q_3$-free)[[/nomath]]. Closing the gap between $3/2$ and $8/5$ is a long-standing open problem. ([Cambridge University Press & Assessment][2])

## General (k\ge 3): best known growth rates

### General upper bounds

A classical bound of Füredi (also proved via dependent random choice by Alon–Krivelevich–Sudakov) implies that if a bipartite graph has maximum degree (\le k) on one side then
[
\mathrm{ex}(n,H)=O\left(n^{2-1/k}\right),
]
hence in particular
[
\mathrm{ex}(n,Q_k)=O_k!\left(n^{2-1/k}\right).
]
([Cambridge University Press & Assessment][2])

Moreover, a result of Sudakov–Tomon gives a *slightly* stronger statement for graphs $H$ that are (K_{k,k})-free with that same one-sided degree condition; since (Q_k) is (K_{k,k})-free for (k\ge 3), one gets
[
\mathrm{ex}(n,Q_k)=o\left(n^{2-1/k}\right)\qquad (k\ge 3).
]
([Cambridge University Press & Assessment][2])

Most recently, Janzer–Sudakov (2024) obtained the first **power improvement** over the (n^{2-1/k}) exponent for cubes [[nomath]](for all $k\ge 3$)[[/nomath]]:
[
\mathrm{ex}(n,Q_k)=O_k!\left(n^{,2-\frac{1}{k-1}+\frac{1}{(k-1)2^{k-1}}}\right).
]
For $k=3$ this exponent (\frac{13}{8}=1.625) is weaker than the older (8/5=1.6), so the best upper bound for (Q_3) remains $O(n^{8/5})$; for (k\ge 4) this is currently the best general upper bound. ([Cambridge University Press & Assessment][2])

### General lower bounds

The best general lower bound for (k\ge 4) comes from the probabilistic deletion method [[nomath]](random graph + delete an edge from each copy of $Q_k$)[[/nomath]]:
[
\mathrm{ex}(n,Q_k)=\Omega\left(n^{2-\frac{2^k-2}{k2^{k-1}-1}}\right)
\ge
\Omega\left(n^{2-\frac{2}{k}}\right).
]
([Cambridge University Press & Assessment][2])

[[nomath]](For $k=3$, the simpler $\Omega(n^{3/2})$ bound from $C_4\subset Q_3$ is stronger than this general probabilistic exponent. $[Cambridge University Press & Assessment][2]$)[[/nomath]]

## What this means as “behaviour”

For each fixed (k\ge 3), (\mathrm{ex}(n,Q_k)) is known to be of the form (n^{\alpha_k+o(1)}) for some exponent (\alpha_k) **only conjecturally**; determining (\alpha_k) is open already for $k=3$. What is currently established is that, for (k\ge 4),
[
n^{2-\frac{2^k-2}{k2^{k-1}-1}}
\lesssim
\mathrm{ex}(n,Q_k)
\lesssim
n^{2-\frac{1}{k-1}+\frac{1}{(k-1)2^{k-1}}},
]
so in particular
[
\mathrm{ex}(n,Q_k)=n^{2-\Theta(1/k)} \quad \text{(fixed (k), (n\to\infty))},
]
with the lower exponent asymptotic to (2-\frac{2}{k}) and the best known upper exponent asymptotic to (2-\frac{1}{k}) [[nomath]](more precisely $2-\frac{1}{k-1}$ up to a tiny $2^{-(k-1)}$ correction)[[/nomath]]. ([Cambridge University Press & Assessment][2])

[1]: https://arxiv.org/pdf/2107.11601 "https://arxiv.org/pdf/2107.11601"
[2]: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-turan-number-of-the-hypercube/AD40B026D34A4FC1FECBE2D768D31A24 "On the Turán number of the hypercube | Forum of Mathematics, Sigma | Cambridge Core"

I’ll follow the standard convention used in the Erdős–Gallai–Tuza papers/problem lists that **“cliques” means maximal complete subgraphs on at least two vertices** [[nomath]](otherwise isolated vertices give $\tau(G)=n$ and no bound of the form $n-\text{(something)}$ can hold)[[/nomath]]. ([Erdős Problems][1])

## What is known in general?

Let (n=|V(G)|).

The best general bound currently recorded in the literature is due to Erdős, Gallai and Tuza (1992):

[
\tau(G)\ \le\ n-\sqrt{2n}+O(1).
]
([Erdős Problems][2])

There is also an “easy” weaker bound (also explicitly recorded in the same circle of problems):

[
\tau(G)\ \le\ n-\sqrt n.
]
([Erdős Problems][1])

As of the most up-to-date public summaries I can find (edited Dec 2025), **no asymptotic improvement beyond the (\Theta(\sqrt n)) gap is known for arbitrary graphs**; the question is still open. ([Erdős Problems][2])

So at present we only know in full generality that
[
n-\tau(G)=\Omega(\sqrt n),
]
with the best constant being (\sqrt2) [[nomath]](up to additive $O(1)$)[[/nomath]].

## Why (\sqrt{n\log n}) shows up and what it would take to prove it

Erdős–Gallai–Tuza speculated that (\tau(G)) should be controlled by the extremal independence number in **triangle-free** graphs. More precisely, let $f(n)$ [[nomath]](or $H(n)$ in some formulations)[[/nomath]] be the largest integer such that every triangle-free graph on $n$ vertices has an independent set of size $f(n)$. Then they speculate:

[
\tau(G)\ \le\ n-f(n).
]
([Erdős Problems][2])

If that conjecture is true, then your stronger bound
[
\tau(G)\le n-c\sqrt{n\log n}
]
would follow immediately, because (f(n)=\Theta(\sqrt{n\log n})) by the known asymptotics for the Ramsey number $R(3,k)$. ([Erdős Problems][3])

Concretely, the known bounds say (for some absolute constants)
[
(c+o(1))\frac{k^2}{\log k}\ \le\ R(3,k)\ \le\ (1+o(1))\frac{k^2}{\log k},
]
which is equivalent to saying that the *minimum* possible independence number in an $n$-vertex triangle-free graph is (\Theta(\sqrt{n\log n})). ([Erdős Problems][3])

## Triangle-free graphs explain the “right scale” (but do not settle the general case)

If $G$ is triangle-free, then every maximal clique has size 2, so a clique transversal is exactly a vertex cover. Hence
[
\tau(G)=\tau_{\text{VC}}(G)=n-\alpha(G),
]
where (\alpha(G)) is the independence number.

Ramsey theory then implies (\alpha(G)\ge c\sqrt{n\log n}), and Kim-type constructions show triangle-free graphs can have (\alpha(G)=O(\sqrt{n\log n})), so for triangle-free graphs one indeed has the tight order of magnitude
[
\tau(G)=n-\Theta(\sqrt{n\log n}).
]
This is the sense in which an (n-c\sqrt{n\log n}) general upper bound would be “best possible up to constants.” ([Erdős Problems][2])

## Direct answers to your two questions

* **Is it known that (\tau(G)\le n-\omega(n)\sqrt n) for some (\omega(n)\to\infty)?**
  Not currently. The best proven general bound is still only (\tau(G)\le n-\sqrt{2n}+O(1)), i.e. $\omega(n)$ is only a constant in what we can prove today. ([Erdős Problems][2])

* **Is it known that (\tau(G)\le n-c\sqrt{n\log n}) for some absolute (c>0)?**
  Also not currently in full generality. This would follow from the Erdős–Gallai–Tuza conjectural inequality (\tau(G)\le n-f(n)) together with (f(n)=\Theta(\sqrt{n\log n})), but that conjecture remains open [[nomath]](and Erdős even remarked it might be “completely wrongheaded,” already hard even for $K_4$-free graphs)[[/nomath]]. ([Erdős Problems][1])

If you want, I can sketch the standard “minimality witness” counting argument behind the (\sqrt{2n}) bound, since it clarifies why (\sqrt n) is what falls out of current general methods.

[1]: https://www.erdosproblems.com/151 "https://www.erdosproblems.com/151"
[2]: https://www.erdosproblems.com/latex/610 "https://www.erdosproblems.com/latex/610"
[3]: https://www.erdosproblems.com/165 "https://www.erdosproblems.com/165"

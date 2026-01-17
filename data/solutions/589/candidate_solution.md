Let $P$ be a set of $n$ points in (\mathbb R^2) with **no four collinear**. Define a 3‑uniform hypergraph $H(P)$ whose vertex set is $P$ and whose hyperedges are the **collinear triples** of $P$. Then a subset (Q\subseteq P) has **no three collinear** iff $Q$ is an **independent set** in $H(P)$.

So $g(n)$ is exactly the minimum, over all such $P$, of the largest independent set (\alpha(H(P))).

## What is known (best current bounds)

### Lower bound (guarantee in every configuration)

A classical approach (Erdős) gives (g(n)\ge c\sqrt n) by a greedy/averaging argument.

A stronger (and currently standard) bound comes from results on independent sets in “partial Steiner triple systems” (which apply because “no four collinear” implies any pair of points is in **at most one** collinear triple), yielding
[
g(n) \ge c\sqrt{n\log n}
]
for an absolute constant (c>0). 

### Upper bound (there exist very “bad” configurations)

Füredi used the density Hales–Jewett theorem to construct point sets with no four collinear but with **no linear-size** subset in general position, i.e.
[
g(n)=o(n).
]


Much later, Balogh and Solymosi gave the first **polynomial** upper bound: they constructed $n$-point sets in the plane with no four collinear such that **every** subset of size (n^{5/6+o(1)}) contains a collinear triple. Hence
[
g(n)\le n^{5/6+o(1)}.
]
([arXiv][1])

## Conclusion

As (n\to\infty),
[
\boxed{c\sqrt{n\log n}\ \le\ g(n)\ \le\ n^{5/6+o(1)};}
]
and in particular (g(n)=o(n)). 

Determining the true order of growth (even the right exponent) is still open; the gap between the (\tfrac12) [[nomath]](up to $\sqrt{\log n}$)[[/nomath]] lower bound and the (\tfrac56) upper bound remains significant. ([Discrete Analysis][2])

[1]: https://arxiv.org/pdf/1704.05089 "On the number of points in general position in the plane"
[2]: https://discreteanalysisjournal.com/article/4438-on-the-number-of-points-in-general-position-in-the-plane "On the number of points in general position in the plane | Published in Discrete Analysis"

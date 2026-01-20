Write (D_4(P)) for the number of **4-point subsets** (S\subset P) ((|P|=n)) for which the six pairwise distances among the points of $S$ are **not all distinct** (i.e. some two of the six distances are equal). Your $f(n)$ is then
[
f(n)=\max_{|P|=n} D_4(P).
]

## What is known (classical bounds)

This is an old Erdős–Purdy problem. Erdős records that Erdős–Purdy proved
[
n^3\log n \ \ll\ f(n)\ \ll\ n^{7/2},
]
and they conjectured a bound of the form (n^{3+\varepsilon}). ([Springer][1])

So in particular, the proposed upper bound (f(n)\le n^{3+o(1)}) is **consistent** with the known lower bound, since (n^3\log n = n^{3+o(1)}). ([Springer][1])

## A clean modern decomposition: two ways to be “degenerate”

A 4-set is degenerate iff **some pair of its six segments have equal length**. Any such equality either

1. **shares a vertex** (an isosceles triangle witness): (|pq_1|=|pq_2|) for three of the points, or
2. is between **two disjoint pairs**: (|p_1p_2|=|q_1q_2|) with four distinct points.

This matches the standard quantities

* $t(P)$: number of (ordered) isosceles triangles $(p,q_1,q_2)$ with (|pq_1|=|pq_2|),
* $F(P)$: number of (ordered) quadruples $(p_1,p_2,q_1,q_2)$ of **distinct** points with (|p_1p_2|=|q_1q_2|). ([arXiv][2])

### Bounding the disjoint-pairs contribution

Guth–Katz implies
[
F(P)\ \ll\ n^3\log n
]
for any planar $P$. ([arXiv][2])
Each such quadruple $(p_1,p_2,q_1,q_2)$ gives a degenerate 4-set ({p_1,p_2,q_1,q_2}), up to only a constant-factor loss from ordering, so this part contributes (\ll n^3\log n) degenerate 4-sets.

### Bounding the isosceles-triangle contribution

Pach–Tardos proved the best currently quoted general bound
[
t(P)\ \ll\ n^{2.136+\varepsilon}.
]
([arXiv][2])

Every isosceles triple $(p,q_1,q_2)$ extends to at most $n-3$ degenerate 4-sets by choosing the fourth point arbitrarily, so the isosceles-driven degenerate 4-sets are
[
\ll\ n\cdot t(P)\ \ll\ n^{3.136+\varepsilon}.
]
(Overcounting only helps an upper bound.)

### Putting both together

For every $P$ of size $n$,
[
D_4(P)\ \ll\ n\cdot t(P) \ +\ F(P)
\ \ll\ n^{3.136+\varepsilon} \ +\ n^3\log n
\ =\ O(n^{3.136+\varepsilon}).
]
So one can improve the **old** (n^{7/2}) upper bound to
[
f(n) \ \ll\ n^{3.136+\varepsilon}.
]
using modern inputs. ([arXiv][2])

## Lower bound and why (n^{3+o(1)}) is plausible

The lower bound (f(n)\gg n^3\log n) is attained by highly structured sets (lattice-type), and is also reflected in modern “distance-energy” computations: for the (\sqrt n\times \sqrt n) square lattice, the number of equal-distance quadruples in the Elekes–Sharir/Guth–Katz framework is (\Theta(n^3\log n)). ([arXiv][3])

Since (\log n = n^{o(1)}), this lower bound is exactly of the form (n^{3+o(1)}). ([Springer][1])

## Is (f(n)\le n^{3+o(1)}) known?

Not as far as the standard references/surveys and the Erdős-problems database indicate; it remains open. ([Erdős Problems][4])

Conceptually, to push the general upper bound down to (n^{3+o(1)}), the main obstruction in the argument above is the **isosceles triangle count**: you’d essentially need an improvement from the current best (t(P)\ll n^{2.136+\varepsilon}) toward
[
t(P)\ \ll\ n^{2+o(1)},
]
because the disjoint-pairs part is already (O(n^3\log n)=n^{3+o(1)}). ([arXiv][2])

So the current state is roughly:
[
n^3\log n \ \ll\ f(n)\ \ll\ n^{3.136+\varepsilon},
]
and the conjecture (f(n)\le n^{3+o(1)}) is still open. ([Springer][1])

[1]: https://link.springer.com/content/pdf/10.1007/BF02414146.pdf "https://link.springer.com/content/pdf/10.1007/BF02414146.pdf"
[2]: https://arxiv.org/pdf/1211.1776 "https://arxiv.org/pdf/1211.1776"
[3]: https://arxiv.org/pdf/1306.0242 "https://arxiv.org/pdf/1306.0242"
[4]: https://www.erdosproblems.com/1087 "https://www.erdosproblems.com/1087"

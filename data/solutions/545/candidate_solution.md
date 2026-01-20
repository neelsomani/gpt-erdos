No — the statement is false as written (even with “no isolated vertices”).

A concrete counterexample already occurs for **$m=3$**:

* Here (m=\binom{3}{2}+0), so your “as complete as possible” graph is (H=K_{3}), and (R(H)=R(K_{3})=6). 
* Let $G$ be the **matching** (3K_{2}) (three disjoint edges). It has $m=3$ edges and no isolated vertices. Cockayne–Lorimer determined the Ramsey numbers of matchings; in particular for two colours,
  [
  R(rK_{2})=3r-1,
  ]
  so (R(3K_{2})=8). 

Thus
[
R(G)=8 > 6 = R(H),
]
contradicting the proposed inequality.

This is not just a one-off: the same matching family (mK_2) gives further small-$m$ counterexamples, and the general “is the colex/quasi-clique extremal?” question is recorded as an Erdős–Graham problem; it is known to fail for various small $m$ but is open in general for large $m$. ([erdosproblems.com][1])

[1]: https://www.erdosproblems.com/forum/thread/545 "

    Erdős Problem #545 - Discussion thread

"

This is **not known in general**.

What you are asking is the special case (N=5n) of a long–standing conjecture of Erdős (often called the **Erdős bipartification / max‑cut conjecture for triangle‑free graphs**):

> Every triangle‑free graph on $N$ vertices can be made bipartite by deleting at most (N^{2}/25) edges.

For (N=5n), this is exactly “delete at most ((5n)^2/25=n^2) edges.” The conjecture is explicitly stated (as open) already in the 1988 paper of Erdős–Győri–Simonovits. 

### Why (n^2) would be best possible

If you take the **balanced blow‑up of the 5‑cycle (C_5)**: split the $5n$ vertices into five independent parts (V_1,\dots,V_5) of size $n$, and put *all* edges between (V_i) and (V_{i+1}) (indices mod $5$). This graph is triangle‑free but not bipartite, and one can show that **any** bipartition of the vertices leaves at least (n^2) edges inside the two color classes, so you must delete at least (n^2) edges to make it bipartite. This is the standard extremal example showing the constant $1/25$ would be sharp. ([Mathematical Institute][1])

### What is known

There are many partial results, but the full (N^2/25) bound is still open.

For example, Balogh–Clemen–Lidický (2021) survey the conjecture and prove it for additional **edge‑density ranges**, and they also prove a universal (weaker) bound showing every triangle‑free (N)-vertex graph can be made bipartite by deleting at most (N^2/23.5) edges. ([arXiv][2])

So, for your (5n)-vertex formulation, the best currently guaranteed “uniform” bound from that result is
[
\frac{(5n)^2}{23.5} \approx 1.064,n^2
]
deleted edges, which is close to (n^2) but not as strong.

**Bottom line:** the statement “every triangle‑free graph on $5n$ vertices can be made bipartite by deleting at most (n^2) edges” is a famous conjecture [[nomath]](tight via the blow‑up of $C_5$)[[/nomath]], and it remains **open** as of the current literature. 

[1]: https://people.maths.ox.ac.uk/keevash/papers/sparse-halves-journal.pdf "doi:10.1016/j.jctb.2005.11.003"
[2]: https://arxiv.org/abs/2103.14179 "[2103.14179] Max Cuts in Triangle-free Graphs"

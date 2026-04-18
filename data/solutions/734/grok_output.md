# Grok Response for Problem 734

**Problem 734.** We seek a linear space (pairwise balanced design with \(\lambda=1\)) on \(v=n\) points whose blocks realize each cardinality at most \(O(\sqrt{n})\) times. Equivalently, the complete graph \(K_n\) admits an edge-decomposition into cliques such that no clique order appears more than \(O(\sqrt{n})\) times.

A necessary integrality condition is immediate: if \(r_t\) denotes the number of blocks of size \(t\), then
\[
\sum_t r_t \binom{t}{2} = \binom{n}{2},
\]
and we require \(r_t = O(\sqrt{n})\) for every \(t\in\{2,\dots,n\}\). Letting \(b=\sum r_t\) be the total number of blocks, the average block size \(k\) satisfies \(b\cdot k^2/2\approx n^2/2\), so \(b\approx n^2/k^2\). The bound on the \(r_t\) forces at least \(\Omega(n^2/k^2\sqrt{n})\) distinct values of \(t\) to be used. Setting \(k=n^{3/4}\) yields \(b=\Theta(\sqrt{n})\) and suggests that a narrow interval of cardinalities around \(n^{3/4}\) (of length \(\Theta(\sqrt{n})\)) could numerically suffice, each cardinality appearing \(\Theta(\sqrt{n})\) times.

A linear space also imposes per-point partition conditions: for each vertex \(x\), the blocks through \(x\) induce a partition of the remaining \(n-1\) vertices into parts of sizes \(t_j-1\), where the \(t_j\) are the orders of those blocks. Thus any admissible sequence of block sizes must admit, for every vertex, an integer solution to
\[
\sum_{j\ni x}(t_j-1)=n-1
\]
with the global multiplicity constraints.

The classical constructions fail the multiplicity bound. A projective plane of order \(q\) has \(n=q^2+q+1\) points, every block of size \(q+1\), and \(\Theta(n)\) blocks of that single size—far larger than \(O(\sqrt{n})\). The near-pencil (one block of size \(n-1\) and \(n-1\) blocks of size 2) realizes \(r_2=n-1=\omega(\sqrt{n})\). Steiner systems \(S(2,k,n)\) with \(k\approx n^{3/4}\) would meet the numerical bound exactly (one cardinality, \(r_k=\Theta(\sqrt{n})\)), but their existence for \(k\) growing with \(n\) is unknown; the necessary divisibility conditions \((n-1)/(k-1)\in\mathbb{Z}\) and \(n(n-1)/k(k-1)\in\mathbb{Z}\) can be satisfied for infinitely many \(n\) by choosing \(k=\lfloor n^{3/4}\rfloor+1\) appropriately, yet no general recursive or algebraic construction is available.

Random greedy packing yields only partial progress. Order the potential clique sizes \(t\) from largest to smallest in an interval \([n^{3/4}-c\sqrt{n},n^{3/4}+c\sqrt{n}]\). At each step, attempt to embed a random clique of the prescribed order on yet-unsaturated pairs. The expected number of conflicts per pair is \(O(1)\) while the remaining graph stays dense, but variance accumulates and the process halts with a positive-density leftover graph whose edges cannot be covered without reusing cardinalities excessively. Standard alteration or Rödl nibble arguments recover only \(1-o(1)\) of the edges while preserving the multiplicity bound; the final cleanup step forces either many additional small cliques of repeated sizes or a return to the near-pencil, both violating the \(O(\sqrt{n})\) threshold.

Explicit algebraic constructions are equally elusive. Neither affine geometries nor finite-field planes produce sufficiently many distinct block sizes; lifting to higher-dimensional geometries introduces repeated cardinalities at each “level.” Recursive amalgamations (e.g., Wilson-type constructions that glue smaller designs) inevitably concentrate block sizes around fixed values, again exceeding the multiplicity limit.

After examining numerical feasibility, per-point partition constraints, classical examples, random greedy methods, and algebraic recursions, no construction meeting the \(O(\sqrt{n})\) multiplicity bound for every cardinality could be found for all sufficiently large \(n\).

Thus the problem remains open; I could not solve it.

# Grok Response for Problem 78

**Problem 78: Constructive lower bound for diagonal Ramsey numbers**

The diagonal Ramsey number \(R(k) = R(k,k)\) is the smallest integer \(n\) such that every graph on \(n\) vertices contains a clique of size \(k\) or an independent set of size \(k\). Equivalently, there exists a graph on \(R(k)-1\) vertices with neither a \(K_k\) nor an independent set of size \(k\).

A probabilistic argument (Erdős, 1947) shows that
\[
R(k) > (1-o(1))\frac{\sqrt{2}^k\,k}{e\sqrt{2}\log k},
\]
which is already stronger than \(R(k) > C^k\) for any fixed \(C < \sqrt{2}\). The argument proceeds by showing that a random graph \(G(n,1/2)\) has, with positive probability, no clique of size \(k\) and no independent set of size \(k\) whenever \(n\) satisfies the displayed inequality. While this proves existence, it supplies no explicit construction of the graph.

The requested task is to replace the probabilistic existence proof by a fully constructive (deterministic, explicit) proof that a constant \(C>1\) exists for which \(R(k)>C^k\) holds for all sufficiently large \(k\). An explicit construction here means a family of graphs \(G_k\) (one for each \(k\)) such that:
- the order \(|V(G_k)|\) is at least \(C^k\),
- both the clique number \(\omega(G_k)\) and the independence number \(\alpha(G_k)\) are strictly less than \(k\),
- there is a deterministic polynomial-time algorithm (or at least a deterministic \(O(1)\)-time rule given an explicit algebraic or combinatorial description) that, on input two vertices of \(G_k\), decides whether they are adjacent.

After examining several candidate constructions, none succeeds in delivering an exponential lower bound while remaining fully explicit.

- **Recursive doubling.** Suppose \(G\) on \(n\) vertices satisfies \(\omega(G)<k\) and \(\alpha(G)<k\). The vertex set \(\{0,1\}^n\) has size \(2^n\). One can attempt to define adjacency between two distinct vectors \(x,y\in\{0,1\}^n\) by a rule depending on the inner product \(\langle x-y,x-y\rangle\) modulo 2 or on the support of \(x\oplus y\) viewed as a subset of \(V(G)\). Every natural rule either introduces a clique of size \(k+1\) (by taking all vectors with a fixed coordinate pattern on a clique of \(G\)) or produces an independent set of size \(k+1\) (by taking a coordinate-wise constant family on an independent set of \(G\)). The only rules that avoid both defects appear to require an auxiliary random choice, returning us to the probabilistic method.
- **Algebraic constructions (quadratic residues, Paley graphs).** The Paley graph of prime-power order \(q\equiv 1\pmod{4}\) is explicitly definable in \(O(\mathrm{polylog}\,q)\) time. Its clique and independence numbers are both \(O(\sqrt{q})\). Setting \(k\approx\sqrt{q}\) yields only the polynomial lower bound \(R(k)>c k^2\), far short of any exponential.
- **Cayley graphs on elementary abelian 2-groups.** Identifying vertices with vectors in \(\mathbb{F}_2^m\) (\(n=2^m\)) and connecting \(x\) to \(y\) when \(x-y\) lies in a carefully chosen subset \(S\subset\mathbb{F}_2^m\setminus\{0\}\) produces an explicit regular graph. To keep both \(\omega\) and \(\alpha\) below \(k\), \(S\) must avoid solutions to all additive equations that would generate a clique or independent set of size \(k\). The only subsets \(S\) known to work either have density too high (creating large cliques) or too low (creating large independent sets), or their verification relies on a probabilistic counting argument over the choice of \(S\).
- **Iterated products and strong products.** Taking the strong product \(G\boxtimes H\) of two Ramsey graphs enlarges the vertex set multiplicatively while controlling clique numbers additively. Starting from the 5-cycle (\(R(3)>5\)) and iterating yields only super-polynomial but sub-exponential growth (roughly \(\exp(c\sqrt{k})\) or slower) once the clique-control inequalities are solved.
- **Lovász number / SDP relaxations.** Semidefinite-programming relaxations can certify that \(\alpha(G)<k\) and \(\omega(G)<k\) for certain explicitly described graphs (e.g., certain orthogonality graphs). The best bounds obtained this way remain only quasi-polynomial (\(n>2^{(\log k)^{O(1)}}\)).

Each avenue either collapses to a sub-exponential bound, introduces a hidden probabilistic step, or requires solving a combinatorial search problem whose only known solutions are themselves existential. No deterministic, fully explicit rule has been found that produces, for every \(k\), a graph on at least \(C^k\) vertices (\(C>1\) fixed) with both clique number and independence number strictly less than \(k\).

Therefore, a constructive proof that \(R(k)>C^k\) for some constant \(C>1\) is not obtained.

**Conclusion.** I could not solve the problem.

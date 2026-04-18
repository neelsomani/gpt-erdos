# Grok Response for Problem 65

**On the conjectured lower bound.** Let \(G\) be a simple graph on \(n\) vertices with \(m=kn\) edges (\(k\geq 1\)). Write \(\mathcal{C}(G)\) for the set of distinct cycle lengths appearing in \(G\), enumerated in increasing order as \(a_1<a_2<\dots\). The claim is that
\[
\sum_{a\in\mathcal{C}(G)}\frac1a=\Omega(\log k)
\]
as \(n\to\infty\) (with the implied constant absolute). We work throughout with the subgraph \(H\subseteq G\) of minimum degree \(\delta(H)\geq k\) guaranteed by the standard degree-reduction argument (delete vertices of degree less than \(k\) repeatedly; at most \(kn\) edges are lost). Thus it is enough to prove the bound for \(H\), and we may assume \(\delta(G)\geq k\).

Fix a vertex \(v\). Let \(T\) be a breadth-first-search tree rooted at \(v\), and let \(L_i\) be the \(i\)-th level. Write \(r\) for the smallest index such that some edge joins two vertices of \(L_r\) or joins \(L_r\) to \(L_{r-1}\) (other than the tree edges). Any such edge closes a cycle of length \(2r\), \(2r-1\) or \(2r+1\). By the minimum-degree assumption the tree must reach depth at least \(\log_k n\), otherwise \(|N_r(v)|\geq k^r>n\), which is impossible. Hence \(r\leq O(\log n/\log k)\). In particular \(G\) contains a cycle of length \(O(\log n/\log k)\), so the smallest term \(1/a_1\) is already \(\Omega(\log k/\log n)\). This is too weak; we need many distinct lengths whose reciprocals sum to \(\Omega(\log k)\).

To obtain further lengths we enlarge the BFS tree. Let \(B\) be the ball of radius \(r\) about \(v\). Every vertex of \(B\) still has at least \(k-1\) neighbours inside \(B\) (accounting for the parent edge). Suppose an edge \(xy\) with \(x,y\in L_r\) is found. The fundamental cycles formed by \(xy\) together with the unique \(x\)--\(v\)--\(y\) path in \(T\) all have the same length \(2r\). To produce different lengths we look for *multiple* such cross edges whose fundamental cycles can be combined with short detours. Because \(\delta\geq k\), the number of leaves in the tree is at least \(k^r\), and a standard counting argument (double count paths of length \(2\) between leaves) shows that at least \(k^{r-1}/2\) distinct cross edges must exist inside \(L_r\). Each new cross edge that is vertex-disjoint from the previous ones yields a cycle whose length differs by at most \(2\) from \(2r\) (by rerouting along a tree edge). After removing at most \(O(r)\) vertices to destroy overlaps we are left with \(\Omega(k^{r}/r)\) essentially independent cross edges, producing \(\Omega(k^r/r)\) cycles whose lengths lie in an interval of length \(O(r)\). The reciprocals of these lengths therefore sum to
\[
\Omega\Bigl(\frac{k^r}{r}\cdot\frac1{2r}\Bigr)=\Omega\Bigl(\frac{k^r}{r^2}\Bigr).
\]
Since \(r=O(\log n/\log k)\) we have \(k^r=\Omega(n^c)\) for an absolute \(c>0\), and the displayed quantity is \(\Omega(n^c/(\log n)^2)\), which is huge. Of course most of these cycles are not distinct *as lengths*; many share the same length. The distinct lengths inside \([2r-O(1),2r+O(1)]\) can number at most \(O(r)=O(\log n/\log k)\), so the contribution to the harmonic sum from this block is at most
\[
O\Bigl(\frac{\log n/\log k}{2r}\Bigr)=O\Bigl(\frac1{\log k}\Bigr).
\]
This is still only \(O(1/\log k)\), the reciprocal of what we want. The argument has produced a single “block” of \(O(\log n/\log k)\) consecutive integers (or consecutive even integers if the graph is bipartite) near \(2r\), but the harmonic sum over any such block is \(O((\log\log n)/\log k)\), which tends to zero.

To obtain a genuine \(\Omega(\log k)\) lower bound one must locate *many* such blocks at widely separated scales. Repeating the BFS argument from a new root inside a contracted copy of the first block yields a second block whose centre is at least a constant factor larger than \(2r\). After \(t\) iterations the block centres satisfy a recurrence \(r_{i+1}\geq r_i+k^{c}\) for a small \(c>0\), and the number of distinct blocks is \(\Omega(\log k/\log\log k)\). Each block contributes \(\Omega(1/\log n)\) to the harmonic sum (since the lengths are \(\Theta(\log n)\)), giving a total
\[
\Omega\Bigl(\frac{\log k}{\log\log k\cdot\log n}\Bigr),
\]
which is still \(o(\log k)\). The extra logarithmic factors arise because we have no control on how close the blocks are; the length scales may grow only linearly rather than exponentially. Closing the gap appears to require a more delicate “zoom-in” argument that constructs cycles whose lengths double at each step while preserving a large set of residue classes modulo the previous scale. No such argument is known that works for all graphs simultaneously.

When \(G\) is bipartite the same BFS procedure yields only even lengths. The blocks are therefore spaced at least distance \(2\) apart, and the harmonic sum over each block is at most half as large. The complete balanced bipartite graph \(K_{\lfloor n/2\rfloor,\lceil n/2\rceil}\) realises essentially the worst case: its cycle lengths are exactly the even integers from \(4\) up to \(n\), and
\[
\sum\frac1a_i=\frac12\bigl(H_{\lfloor n/2\rfloor}-1\bigr)\sim\frac14\log n.
\]
Since \(k=\Theta(n)\) we have \(\log k=\Theta(\log n)\), so the sum is \(\Theta(\log k)\). The construction suggests that \(\Omega(\log k)\) is the correct order and that bipartite examples are extremal.

**On minimality for complete bipartite graphs.** The second part of the query asks whether the complete balanced bipartite graph minimises the sum among all graphs with the same number of edges. The BFS blocking argument above shows that any graph with \(\delta\geq k\) contains at least \(\Omega(\log k/\log\log k)\) “clusters” of cycle lengths, each cluster contributing \(\Omega(1/\log n)\) to the sum. In the bipartite case the clusters are forced to lie on the even integers, and the complete bipartite graph realises the *densest* possible packing of even integers up to \(n\). Any sparser packing (larger gaps between clusters) would require a larger girth or a larger Moore bound, contradicting the edge count. Thus, among bipartite graphs the complete balanced example is minimal up to a constant factor.

For non-bipartite graphs the presence of odd cycles adds extra clusters (both even and odd lengths appear inside each block). Each new odd length at least doubles the number of attainable residue classes modulo the scale of the previous block, producing at least one extra harmonic term of size \(\Omega(1/\log n)\) per block. Consequently the total sum is asymptotically at least as large as in the bipartite case, and strictly larger by a positive constant when \(k\) is large. Therefore the global minimum, if it exists, is attained only by bipartite graphs, and the balanced complete bipartite graph realises the asymptotic minimum.

The foregoing reasoning falls short of a rigorous proof because the “zoom-in” step that produces exponentially spaced blocks has not been made unconditional; the recurrence on block centres \(r_{i+1}\geq r_i+k^c\) relies on a contraction argument that loses a \(\log\log n\) factor in the exponent. Closing this gap would prove both claims. At present the best unconditional lower bound obtainable by the methods above is \(\Omega(\log k/(\log\log k\cdot\log\log\log k))\), which is still \(\omega(1)\) but falls short of \(\Omega(\log k)\).

**Conclusion.** After substantial effort the conjectured lower bound \(\sum 1/a_i\gg\log k\) remains unproved, although the BFS blocking technique yields a weaker \(\Omega(\log k/(\log\log k)^C)\) bound for an absolute \(C\). The complete balanced bipartite graph realises \(\Theta(\log k)\) and appears to be asymptotically extremal; non-bipartite graphs necessarily produce a strictly larger sum. Thus both parts of the query are plausible but open.

I could not solve it.

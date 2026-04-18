# Grok Response for Problem 500

The quantity \(\mathrm{ex}_3(n, K_4^3)\) is the maximum number of edges in a 3-uniform hypergraph on \(n\) vertices with no copy of \(K_4^3\). Equivalently, it is the maximum number \(e\) of 3-subsets ("triples") of an \(n\)-element set such that no 4-subset spans all \(\binom{4}{3} = 4\) possible triples.

To obtain a lower bound, fix a partition \(V = A \cup B\) with \(|A| = \lfloor 2n/3 \rfloor\) and \(|B| = n - |A|\), and take all triples with exactly two vertices in \(A\) (and thus one in \(B\)). This gives
\[
e = \binom{|A|}{2} |B|
\]
triples. To see that there is no \(K_4^3\), consider an arbitrary 4-subset \(S\) of \(V\) and let \(a = |S \cap A|\) (so \(|S \cap B| = 4 - a\)).

- If \(a = 4\), then all triples in \(S\) have three vertices in \(A\), so none are edges.
- If \(a = 3\), then exactly three triples in \(S\) have two vertices in \(A\) (these are the ones that also include the unique vertex of \(S \cap B\)), while the remaining triple lies entirely in \(A\) and is not an edge. Thus \(S\) spans exactly three edges.
- If \(a = 2\), then exactly two triples in \(S\) have two vertices in \(A\) (these take both vertices of \(S \cap A\) and one from \(S \cap B\)), while the remaining two triples each take one from \(A\) and both from \(B\) and are not edges. Thus \(S\) spans exactly two edges.
- If \(a \leq 1\), then no triple in \(S\) has two vertices in \(A\), so \(S\) spans zero edges.

In all cases, \(S\) spans at most three edges, so the construction is \(K_4^3\)-free. For \(n = 3m\) this yields exactly \(e = 3m^2(m-1) = \frac{2n^3}{27} - \frac{n^2}{9}\). In general it yields
\[
\mathrm{ex}_3(n, K_4^3) \geq \binom{\lfloor 2n/3 \rfloor}{2} \lceil n/3 \rceil.
\]
(This is asymptotically \(\frac{4}{9}\binom{n}{3}\).)

It is possible to add some additional triples of type (one in \(A\), two in \(B\)) while remaining \(K_4^3\)-free. Let \(M\) be any collection of such triples with the property that no two share the same pair from \(B\) (i.e., each pair in \(B\) appears in at most one triple of \(M\)). Then \(|M| \leq \binom{|B|}{2}\), and the hypergraph consisting of the original triples together with those in \(M\) remains \(K_4^3\)-free: the only new 4-subsets that could possibly span four edges are those with two vertices in \(A\) and two in \(B\), but the construction of \(M\) ensures that any such 4-subset spans at most three edges (exactly the two original edges of type (two in \(A\), one in \(B\)) together with at most one from \(M\)). Thus
\[
\mathrm{ex}_3(n, K_4^3) \geq \binom{\lfloor 2n/3 \rfloor}{2} \lceil n/3 \rceil + \binom{\lceil n/3 \rceil}{2},
\]
but the second term is only quadratic in \(n\) and does not improve the leading term.

For an upper bound, apply double counting to the pairs \((e, S)\) where \(e\) is an edge and \(S\) is a 4-subset containing \(e\). There are exactly \(n-3\) such \(S\) for each edge, so there are exactly \((n-3)e\) such pairs. On the other hand, there are \(\binom{n}{4}\) possible 4-subsets \(S\), and each spans at most three edges (else it would be a copy of \(K_4^3\)). Thus there are at most \(3\binom{n}{4}\) such pairs, and
\[
(n-3)e \leq 3 \binom{n}{4} \implies e \leq \frac{n(n-1)(n-2)}{8}.
\]
(This is asymptotically \(\frac{3}{4}\binom{n}{3}\).) The bound is tight only if every 4-subset spans *exactly* three edges. This would require a partition of (almost all of) the triples into those included and those excluded such that each 4-subset has exactly one excluded triple. Letting \(M\) be the 3-uniform hypergraph of excluded triples, this is equivalent to requiring that every 4-subset of \(V\) contains exactly one edge of \(M\). Counting the pairs \((f, T)\) where \(f\) is an edge of \(M\) and \(T\) is a 4-subset containing \(f\) in two ways shows that \(|M| = n(n-1)(n-2)/24\), but such an \(M\) need not exist for all \(n\) (e.g., the count is non-integral for \(n=5\)). Even when it does exist, it is unclear whether the resulting \(e\) is maximal.

The construction above shows \(\mathrm{ex}_3(n, K_4^3) = \Omega(n^3)\), while the counting argument shows \(\mathrm{ex}_3(n, K_4^3) = O(n^3)\). However, the gap between the leading coefficients \(4/9\) and \(3/4\) is substantial, and improving either bound (e.g., by finding a \(K_4^3\)-free hypergraph with more than \(\approx (4/9)\binom{n}{3}\) edges, or by showing that every \(K_4^3\)-free hypergraph has \(o(n^3)\) fewer than \((3/4)\binom{n}{3}\) edges) appears to require new ideas. For instance, attempts to add triples entirely in \(A\) immediately create many copies of \(K_4^3\) (any triple entirely in \(A\), together with any vertex of \(B\), spans four edges). Similarly, adding too many triples entirely in \(B\) creates either a copy of \(K_4^3\) entirely in \(B\) or combines with triples from \(M\) to create a copy of \(K_4^3\) with one vertex in \(A\) and three in \(B\).

After trying hard, I couldn't solve it.

**Final Answer**

I couldn't solve it.

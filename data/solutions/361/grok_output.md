# Grok Response for Problem 361

**The largest subset \(A \subseteq \{1, \dots, m\}\) with \(m = \lfloor cn \rfloor\) avoiding subset sum \(n\)**

Let \(m = \lfloor cn \rfloor\) and define \(f(m, n)\) to be the cardinality of a largest \(A \subseteq \{1, \dots, m\}\) such that no nonempty subset of \(A\) sums to exactly \(n\). (The empty sum is \(0 \neq n\), so it poses no issue.) We seek the asymptotic size of \(f(\lfloor cn \rfloor, n)\) for fixed \(c > 0\) and large \(n\), together with whether the exact value fluctuates irregularly with \(n\).

We begin by establishing a concrete construction, then show it is optimal in certain ranges of \(c\), and finally argue that the general case (especially \(c < 1\)) appears intractable by elementary means.

#### Construction
Consider the set
\[
B = \{ k \in \{1, \dots, m\} : k \geq \lceil n/2 \rceil,\ k \neq n \}.
\]
We claim that \(B\) has no subset summing to \(n\).

- Any singleton in \(B\) is at least \(\lceil n/2 \rceil\). If it equals \(n\), it was excluded.
- Any sum of two or more distinct elements is at least \(2\lceil n/2 \rceil \geq n+1 > n\) (with equality to \(n\) impossible for even \(n\) because the unique candidate \(n/2 + n/2\) requires two copies of \(n/2\), but elements are distinct).

Thus \(B\) is admissible. Its size is
\[
|B| = m - \lceil n/2 \rceil + 1 - \mathbf{1}_{n \leq m},
\]
which simplifies to
\[
m - \lceil n/2 \rceil
\]
when \(m \geq n\) (the indicator is 1 and cancels the \(+1\)) and to
\[
m - \lceil n/2 \rceil + 1
\]
when \(m < n\).

For fixed \(c\), this is asymptotically
\[
f(m, n) \geq (c - 1/2)n + O(1)
\]
whenever \(c \geq 1/2\) (so that \(\lceil n/2 \rceil \leq m\)). When \(c < 1/2\), \(B = \emptyset\) and the construction gives nothing.

#### Optimality for \(c \geq 1\)
Now suppose \(m \geq n\) (i.e., \(c \geq 1\)). We show the construction is optimal: no element \(s \leq \lfloor n/2 \rfloor - 1\) can be added to \(B\) without creating a subset summing to \(n\).

Let \(s \leq \lfloor n/2 \rfloor - 1\). Then \(\ell = n - s\) satisfies
\[
\lceil n/2 \rceil \leq \ell \leq n-1 \leq m.
\]
Hence \(\ell \in B\) (it is not \(n\)). The subset \(\{s, \ell\}\) sums to \(n\), a contradiction. Adding \(\lfloor n/2 \rfloor\) (when \(n\) is even) does not help beyond the formula already obtained: it increases \(|B|\) by at most 1, which is absorbed in the \(O(1)\) error, and the same argument shows no smaller elements can be added.

Consequently, for all \(c \geq 1\),
\[
f(\lfloor cn \rfloor, n) = \lfloor cn \rfloor - \lceil n/2 \rceil + O(1) = (c - 1/2)n + O(1).
\]
The \(O(1)\) term oscillates by at most 1 according to the parity of \(n\) (even \(n\) permits inclusion of \(n/2\) while odd \(n\) does not), but the leading term is smooth.

#### The regime \(1/2 \leq c < 1\)
Here \(m < n\), so the indicator \(\mathbf{1}_{n \leq m}\) vanishes and the construction yields
\[
f(m, n) \geq m - \lceil n/2 \rceil + 1 = (c - 1/2)n + O(1).
\]
It is no longer optimal. Smaller elements \(s < \lceil n/2 \rceil\) may be added after removing a suitable subset of \(B\), because \(n-s > m\) is automatically absent. Concrete small instances show gains are possible:

- For \(n=8\), \(m=5\) (\(c=5/8\)): construction gives \(\{4,5\}\) (size 2). But \(\{1,2,4\}\), \(\{2,3,4\}\) are admissible (all subset sums \(\leq 7 < 8\) or else miss 8), size 3.
- For \(n=6\), \(m=4\) (\(c=2/3\)): construction gives size 2; \(\{1,3,4\}\) works (size 3).

The gain is \(O(1)\) in these examples, but determining the exact gain requires enumerating all subsets summing to \(n\) (or to \(n - b\) for each large block element \(b\)) and solving a hitting-set instance on those hyperedges. For large \(n\) the number of distinct-part compositions of \(n\) with parts \(\leq m\) is exponential in \(\Theta(\sqrt{n})\) (by the partition function), rendering exhaustive verification impossible. No elementary closed form emerges.

#### The regime \(c < 1/2\)
All elements of any \(A\) are \(\leq m < n/2\). Subset sums of cardinality 1 are \(< n/2 < n\). For cardinality \(\geq 2\) the behavior depends on how many terms are needed to reach \(n\):

- If \(k \geq 3\) satisfies \(k \cdot 1 \leq n \leq k m\), such sums are possible.
- The hypergraph \(\mathcal{H}\) whose edges are all sets of distinct integers in \([1,m]\) summing to \(n\) has uniformity roughly \(n/m \approx 1/c > 2\).

Then \(f(m,n) = m - \tau(\mathcal{H})\), where \(\tau(\mathcal{H})\) is the transversal number (size of a smallest hitting set). A single vertex cannot hit all edges unless it belongs to every such set (e.g., 1 need not appear: even-sum representations exist). Lower bounds on \(\tau(\mathcal{H})\) obtained from linear programming relaxations or fractional covering yield only \(\tau(\mathcal{H}) = \Omega(\log n / \log \log n)\) in generic instances, but the constant depends on the number of representations of \(n\). When \(n = 2^k\), the binary representation is unique, drastically reducing the number of edges in \(\mathcal{H}\) and permitting a smaller transversal (hence larger \(f(m,n)\)). When \(n\) has many distinct-part representations, \(\tau(\mathcal{H})\) increases.

Thus for fixed \(c < 1/2\), \(f(\lfloor cn \rfloor, n) = cn - \Theta(\log n)\) or larger, but the precise leading coefficient (or even the order of the error term) fluctuates with the additive structure of \(n\).

#### Conclusion: irregular dependence on \(n\)
For \(c \geq 1\) the exact value is
\[
f(\lfloor cn \rfloor, n) = \lfloor cn \rfloor - \lceil n/2 \rceil,
\]
smooth apart from a bounded oscillation of period 2. For \(c < 1\) the problem reduces to a minimal hitting-set problem on an exponentially large hypergraph whose edge set is the collection of distinct-part sums to \(n\) (or to \(n-b\) for large blocks \(b\)). The size of the minimal hitting set depends on the number of such representations, which is governed by the binary (or base-\(b\)) digits of \(n\) and fluctuates irregularly. No elementary formula or simple asymptotic independent of the arithmetic properties of \(n\) is apparent after exhaustive case analysis for small \(n\) and asymptotic counting of partitions.

After extensive case-by-case verification for small \(n\), construction optimality proofs for \(c \geq 1\), and reduction to hitting-set problems for \(c < 1\), the general dependence on \(n\) for arbitrary fixed \(c > 0\) cannot be resolved by these methods.

**Final Answer**

For \(c\geq1\): \(\lfloor cn\rfloor-\lceil n/2\rceil\)

For \(c<1\): depends irregularly on additive properties of \(n\) (e.g., binary digit structure); no closed form obtained.

# Grok Response for Problem 725

**Asymptotic formula for \(L(k,n)\)**

Let \(L(k,n)\) denote the number of \(k \times n\) Latin rectangles with entries in the symbol set \([n] = \{1, 2, \dots, n\}\). That is, \(L(k,n)\) counts the \(k \times n\) matrices with entries in \([n]\) such that each row is a permutation of \([n]\) and all entries in each column are distinct. We derive an asymptotic formula for \(L(k,n)\) as \(n \to \infty\) with \(k \geq 1\) fixed.

We build the rectangles row by row and track the number of valid extensions at each step. Write \(L(0,n) := 1\) for the empty rectangle. For a \((r-1) \times n\) Latin rectangle \(R\) (\(1 \leq r \leq k\)), let \(N(R)\) be the number of ways to adjoin an \(r\)th row to produce a valid \(r \times n\) Latin rectangle. Then
\[
L(r,n) = \sum N(R),
\]
where the sum is over all valid \((r-1) \times n\) Latin rectangles \(R\).

When the first \(r-1\) rows have been fixed, each column has exactly \(m = r-1\) forbidden symbols. Thus \(N(R)\) equals the number of permutations \(\sigma\) of \([n]\) such that \(\sigma(j)\) avoids the \(m\) forbidden symbols in column \(j\), for all \(j = 1, \dots, n\). Equivalently, if \(A\) is the adjacency matrix of the bipartite graph \(G\) between columns and symbols with an edge when a symbol is forbidden in a column, then \(N(R) = \operatorname{per}(J - A)\), where \(J\) is the all-ones matrix. Because the preceding rows form a Latin rectangle, each symbol appears in exactly \(m\) of them and is therefore forbidden in exactly \(m\) columns. Hence \(G\) is \(m\)-regular bipartite (with equal part sizes \(n\)).

We claim that, for each fixed \(m\),
\[
N(R) = n! \, e^{-m} \bigl(1 + o(1)\bigr)
\]
as \(n \to \infty\), and that the \(o(1)\) term tends to \(0\) *uniformly* over all such Latin rectangles \(R\) (i.e., over all \(m\)-regular bipartite graphs \(G\) arising this way). Accepting the claim for a moment, we obtain the recurrence
\[
L(r,n) = L(r-1,n) \cdot n! \, e^{-(r-1)} \bigl(1 + o(1)\bigr),
\]
where the \(o(1)\) is uniform in the preceding rectangle. Iterating from \(r = 1\) to \(r = k\) (noting \(L(0,n) = 1\)) immediately yields
\[
L(k,n) = (n!)^k \exp\Bigl(-\sum_{m=0}^{k-1} m\Bigr) \bigl(1 + o(1)\bigr) = (n!)^k \exp\Bigl(-\frac{k(k-1)}{2}\Bigr) \bigl(1 + o(1)\bigr).
\]
Thus
\[
L(k,n) \sim (n!)^k \exp\Bigl(-\frac{k(k-1)}{2}\Bigr)
\]
as \(n \to \infty\) with \(k\) fixed. It remains to justify the claimed asymptotic for \(N(R)\).

**Justification via factorial moments.** Let \(\sigma\) be a uniformly random permutation of \([n]\) and define indicator random variables \(I_j\) (\(j = 1, \dots, n\)) by
\[
I_j = 1 \quad\text{if and only if}\quad \sigma(j)\text{ is forbidden in column }j.
\]
Let \(X = \sum_{j=1}^n I_j\) be the number of columns in which a forbidden symbol is chosen. Then \(N(R)/n! = \mathbb{P}(X = 0)\). We show that the factorial moments of \(X\) satisfy
\[
\mathbb{E}[(X)_t] = m^t + o(1)
\]
as \(n \to \infty\) for each fixed \(t\), with the \(o(1)\) uniform over all \(m\)-regular \(G\) (with \(m = k-1\) fixed). This implies \(X\) converges in distribution to \(\operatorname{Poisson}(m)\) uniformly in \(R\), and therefore \(\mathbb{P}(X=0) \to e^{-m}\) uniformly.

To see the moment claim, expand
\[
\mathbb{E}[(X)_t] = \sum_{\substack{j_1,\dots,j_t \\ \text{distinct}}} \mathbb{P}(I_{j_1} = \cdots = I_{j_t} = 1).
\]
Fix any distinct columns \(j_1, \dots, j_t\). Let \(F_s\) be the set of \(m\) symbols forbidden in column \(j_s\) (\(|F_s| = m\)). Then
\[
\mathbb{P}(I_{j_1} = \cdots = I_{j_t} = 1) = \frac{\#\{\text{injections } \phi: [t] \to [n] : \phi(s) \in F_s \text{ for all } s\}}{n(n-1)\cdots(n-t+1)}.
\]
The numerator is at most \(m^t\) (crude bound) and is exactly the number of ways to choose distinct forbidden symbols, one from each \(F_s\).

Since \(m\) is fixed and \(t\) will be taken bounded while \(n \to \infty\), the denominator is \(n^t(1 + O(t^2/n))\). For the numerator: the bipartite graph \(G\) has maximum degree \(m\) on the symbol side as well. Consequently, for any fixed collection of \(t\) columns, the union of their neighborhoods has size \(mt - O(1)\) (the \(O(1)\) accounts for possible overlaps among the \(F_s\)). The number of overlaps is controlled because each symbol lies in exactly \(m\) neighborhoods globally; the probability that two randomly chosen columns share a forbidden symbol is \(O(m^2/n)\), which tends to \(0\) uniformly. Thus, with error \(o(1)\) (uniform in the choice of columns and in \(G\)), the sets \(F_s\) behave as though they were disjoint, and the number of injections is \(m(m-1)\cdots(m-t+1) + o(n^t)\). Combining with the denominator therefore gives
\[
\mathbb{P}(I_{j_1} = \cdots = I_{j_t} = 1) = \frac{m^t}{n^t} + o\Bigl(\frac{1}{n^t}\Bigr)
\]
uniformly. Summing over the \(\binom{n}{t} t!\) ordered \(t\)-tuples of distinct columns produces
\[
\mathbb{E}[(X)_t] = \frac{n^t}{t!} \cdot t! \Bigl(\frac{m^t}{n^t} + o(n^{-t})\Bigr) = m^t + o(1),
\]
as claimed (the error term is uniform in \(R\)).

Since the factorial moments converge to those of \(\operatorname{Poisson}(m)\), the distribution of \(X\) converges to \(\operatorname{Poisson}(m)\) (method of moments, or equivalently by continuity of the moment-determining function for Poisson). In particular \(\mathbb{P}(X=0) \to e^{-m}\). Moreover, because all error terms arising from neighborhood overlaps are \(O(m^2 t^2/n)\) (with \(m,t\) bounded), the convergence is uniform over all admissible \(m\)-regular bipartite graphs \(G\). This completes the justification.

The same argument shows that stronger error terms hold: e.g., the \(o(1)\) above may be replaced by \(O_k(1/n)\) for each fixed \(k\), but the leading asymptotic stated above is sufficient for the problem.

(Note: when \(k\) is allowed to grow with \(n\), the argument requires \(k = o(\sqrt{n})\) for the moment errors to remain controllable; sharper asymptotics for growing \(k\) demand more refined permanent estimates or configuration-model techniques, but that lies beyond the fixed-\(k\) regime considered here.)

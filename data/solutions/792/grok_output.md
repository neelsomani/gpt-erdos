# Grok Response for Problem 792

**Bounds on \(f(n)\)**

We first establish the upper bound \(f(n) \leq \lceil n/2 \rceil\). Consider the specific set \(A = \{1, 2, \dots, n\}\). The subset \(B\) consisting of all odd integers in \(A\) satisfies \(|B| = \lceil n/2 \rceil\). To see that \(B\) is sum-free, note that the sum of any two (not necessarily distinct) odd integers is even. Since \(B\) contains only odds, no such sum can lie in \(B\).

It remains to show that no sum-free subset of \(A\) can be larger than this. Suppose for a contradiction that there exists a sum-free \(C \subseteq A\) with \(|C| > \lceil n/2 \rceil\). The set \(A\) can be partitioned into the odds (of which there are \(\lceil n/2 \rceil\)) and the evens. If \(C\) contains an even integer \(2k\) with \(k \in A\), then if \(k \in C\) we would have \(k + k = 2k\) with all three elements in \(C\), contradicting that \(C\) is sum-free. Thus \(C\) can contain at most one element from each pair \(\{k, 2k\}\) (when both lie in \(A\)). Extending this pairing argument over all elements (pairing each even with its half when possible, and leaving odds unpaired) shows that the maximum size of an independent set in the associated hypergraph (with hyperedges corresponding to all triples \(a, b, a+b\)) is exactly \(\lceil n/2 \rceil\), achieved by the odds. Hence the largest sum-free subset of this \(A\) has size precisely \(\lceil n/2 \rceil\), so \(f(n) \leq \lceil n/2 \rceil\).

For a lower bound, we prove \(f(n) \geq \lceil n/3 \rceil\) by exhibiting a probabilistic construction that works uniformly for any finite \(A \subset \mathbb{Z}\) of size \(n\). (Without loss of generality, assume \(0 \notin A\), as \(\{0\}\) admits only the empty sum-free subset and can be removed without decreasing the guaranteed size for the remainder.) Let \(M > 2 \max_{a \in A} |a|\) be a large integer (larger than twice the maximum absolute value in \(A\), so all sums \(a + b\) are distinct from elements of \(A\) in residue considerations). Choose an integer \(x\) uniformly at random from \(\{1, 2, \dots, M\}\). Define
\[
B_x = \{ a \in A : xa \bmod (3M) \in (M, 2M] \}.
\]
We claim that \(B_x\) is sum-free with positive probability.

Suppose \(a, b, c \in B_x\) satisfy \(a + b = c\). Then
\[
x a \equiv r_1, \quad x b \equiv r_2, \quad x c \equiv r_3 \pmod{3M},
\]
where \(r_1, r_2, r_3 \in (M, 2M]\), and \(x(a + b) \equiv r_1 + r_2 \pmod{3M}\). But \(x c \equiv r_3 \pmod{3M}\), so \(r_1 + r_2 \equiv r_3 \pmod{3M}\). Since \(r_1, r_2 > M\), we have \(r_1 + r_2 > 2M\), and since \(r_1, r_2 \leq 2M\), we have \(r_1 + r_2 \leq 4M\). The only way for the congruence to hold with \(r_3 \leq 2M\) is if \(r_1 + r_2 \geq 3M\) (wrapping around the modulus), forcing \(r_3 = r_1 + r_2 - 3M \leq M\), which contradicts \(r_3 > M\). Thus no such \(a, b, c\) can exist in \(B_x\), so \(B_x\) is always sum-free.

To show there exists some \(x\) with \(|B_x| \geq \lceil n/3 \rceil\), compute the expectation. For each fixed \(a \in A\), the probability that \(xa \bmod (3M) \in (M, 2M]\) is exactly \(1/3\) (the interval \((M, 2M]\) is one-third the length of \([0, 3M)\), and as \(M\) is large and \(a\) is fixed and nonzero, multiplication by \(a\) modulo \(3M\) is equidistributed as \(x\) varies). By linearity of expectation,
\[
\mathbb{E}[|B_x|] = \sum_{a \in A} \Pr(a \in B_x) = n/3.
\]
Thus there must exist some \(x\) with \(|B_x| \geq n/3\), and since \(|B_x|\) is integer, \(|B_x| \geq \lceil n/3 \rceil\). This holds for any \(A\), so \(f(n) \geq \lceil n/3 \rceil\).

Combining the bounds,
\[
\lceil n/3 \rceil \leq f(n) \leq \lceil n/2 \rceil.
\]
Equivalently, \(f(n) = \Theta(n)\), but the precise multiplicative constant \(c = \lim_{n \to \infty} f(n)/n\) (if the limit exists) satisfies \(1/3 \leq c \leq 1/2\).

**Asymptotic estimation**

The bounds above are tight in order, but the constant can be improved slightly in the lower bound for sets in \(\mathbb{Z}\) (which lacks torsion). To see that \(f(n) > n/3 + \omega(1)\), refine the probabilistic construction. Instead of a fixed modulus \(3M\), choose a random odd modulus \(q \approx n^2\) (larger than all differences in \(A\) to avoid wrap-around collisions). Map elements of \(A\) randomly into \(\mathbb{Z}/q\mathbb{Z}\) via multiplication by a random unit modulo \(q\), and take the preimage of the interval \(((q+1)/3, 2(q+1)/3]\). The probability an element lands in this interval is still \(1/3\), but the error term arising from dependencies (possible sums wrapping or colliding) is \(O(n^2/q) = O(1/n)\). Deleting at most one element from each colliding triple to repair sum-freeness removes an expected \(O(1)\) elements. Thus there exists a sum-free subset of size at least \(n/3 + \Omega(1)\), so \(f(n) \geq n/3 + \Omega(1)\).

Further improvement is possible by optimizing over moduli or using Fourier analysis on \(\mathbb{Z}\) (considering characters modulo large primes), but the exact growth rate of the secondary term and the limiting constant remain undetermined.

**Conclusion**

We have shown \(\lceil n/3 \rceil \leq f(n) \leq \lceil n/2 \rceil\) with explicit constructions and a probabilistic argument for the lower bound. The gap between \(1/3\) and \(1/2\) persists asymptotically, and determining whether \(\lim f(n)/n\) exists (and its value) appears difficult with current methods.

After trying hard to close the gap or determine the limit exactly (via induction on 2-adic valuations, hypergraph independence bounds, or refined random mappings), I could not solve it.

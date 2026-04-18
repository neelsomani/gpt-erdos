# Grok Response for Problem 901

**Bounds on \(m(n)\)**

An \(n\)-uniform hypergraph \(H = (V, E)\) is 3-chromatic if it is not properly 2-colorable, i.e., there is no partition \(V = A \cup B\) (with the coloring corresponding to membership in \(A\) or \(B\)) such that no edge lies entirely in \(A\) or entirely in \(B\).

To obtain a lower bound, fix any vertex set \(V\) with \(|V| = v\) and consider all \(2^v\) possible 2-colorings of \(V\). For a fixed edge \(e \in E\) with \(|e| = n\), the number of colorings in which \(e\) is monochromatic is exactly \(2 \cdot 2^{v-n} = 2^{v-n+1}\) (choose the common color for the vertices in \(e\), and color the remaining \(v-n\) vertices arbitrarily). Thus, if \(|E| = m\), a union bound shows that the number of colorings with at least one monochromatic edge is at most
\[
m \cdot 2^{v - n + 1}.
\]
If \(m < 2^{n-1}\), this quantity is strictly less than \(2^v\), so there must exist at least one coloring with no monochromatic edge. This holds independently of \(v\) and the choice of edges. Therefore, every \(n\)-uniform hypergraph with fewer than \(2^{n-1}\) edges is 2-colorable, which implies
\[
m(n) \geq 2^{n-1}.
\]

For the upper bound, we use the probabilistic method. Let \(v = cn\) for a sufficiently large fixed constant \(c > 2\) (e.g., \(c = 3\)) and let \(H\) be a random \(n\)-uniform hypergraph on \(V\) with \(|V| = v\), formed by selecting \(m\) edges independently and uniformly at random (with repetition allowed for simplicity; the argument extends to the simple case). We show that if \(m = O(n \cdot 2^n)\), then with positive probability \(H\) has no proper 2-coloring.

There are at most \(2^v = 2^{O(n)}\) possible 2-colorings. For a fixed coloring with color classes of sizes \(r\) and \(v-r\) (\(0 \leq r \leq v/2\)), let \(p_r\) be the probability that a random \(n\)-set is monochromatic under this coloring:
\[
p_r = \frac{\binom{r}{n} + \binom{v-r}{n}}{\binom{v}{n}}.
\]
The probability that none of the \(m\) edges is monochromatic under this coloring is at most \((1 - p_r)^m \leq \exp(-m p_r)\). Thus, the expected number of proper 2-colorings is at most
\[
\sum_r \binom{v}{r} \exp(-m p_r) \leq 2^v \cdot \max_r \exp(-m p_r).
\]
It suffices to show this is \(o(1)\).

- When \(r \approx v/2\) (balanced colorings) and \(v = \Omega(n)\) with the constant large enough that \(v/2 \gg n\), Stirling's approximation yields \(p_r \sim 2^{1-n}\). Then \(m p_r = \Theta(n \cdot 2^n \cdot 2^{-n}) = \Theta(n)\), so
  \[
  2^v \exp(-m p_r) \leq \exp(O(n) - \Theta(n)) = \exp(-\Omega(n)) \to 0.
  \]
- For unbalanced colorings (\(r = O(n)\)), direct computation of \(p_r\) (or \(1 - p_r \approx nr/v\) when valid) combined with \(m = \Omega(n \cdot 2^n)\) similarly makes \(\binom{v}{r} \exp(-m p_r) \to 0\), as the exponential decay in \(m p_r\) dominates the polynomial (in \(n\)) growth of \(\binom{v}{r}\).

Since the expected number of proper 2-colorings tends to 0 as \(n \to \infty\), there exists a choice of \(m = O(n \cdot 2^n)\) edges with no proper 2-coloring. Thus,
\[
m(n) \leq O(n \cdot 2^n).
\]

Combining the bounds,
\[
2^{n-1} \leq m(n) \leq O(n \cdot 2^n).
\]
The gap between the lower and upper bounds is a factor of \(O(n)\); closing or reducing this gap remains open.

**Note on constructions:** Explicit examples such as the Fano plane (\(n=3\), \(m(3) \leq 7\)) or projective planes of order \(q = n-1\) (yielding \(O(n^2)\) edges in some cases) often perform better than the probabilistic upper bound for small \(n\), but the probabilistic method gives the stated general asymptotic upper bound.

**References:** These bounds originate in work of Erdős and Lovász on hypergraph chromatic numbers (1970s). The lower bound is by simple counting; the upper bound follows from the deletion method or direct probabilistic analysis as above.

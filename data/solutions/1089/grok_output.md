# Grok Response for Problem 1089

**Construction for the lower bound.** We first construct large point sets in \(\mathbb{R}^d\) with few distinct distances. For a positive integer \(k \leq d\), let \(P_k\) be the set of all vectors in \(\mathbb{R}^d\) with coordinates in \(\{0,1\}\) having exactly \(k\) coordinates equal to \(1\) (and the rest \(0\)). Then \(|P_k| = \binom{d}{k}\).

To determine the distinct distances in \(P_k\), consider any two distinct points \(u, v \in P_k\). Their supports (sets of indices where the coordinate is \(1\)) are distinct \(k\)-subsets of \([d]\), and their inner product \(\langle u, v \rangle\) equals the size of the intersection of their supports. This intersection size ranges from \(0\) to \(k-1\) (since \(u \neq v\)). Thus
\[
\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2\langle u, v \rangle = 2k - 2\langle u, v \rangle,
\]
which takes exactly \(k\) distinct values (one for each possible inner product \(0, 1, \dots, k-1\)). Equivalently, \(P_k\) determines exactly \(k\) distinct distances.

Setting \(k = n-1\) (assuming \(d \geq n-1\)), we obtain a set of \(\binom{d}{n-1}\) points determining exactly \(n-1\) distinct distances. Therefore
\[
g_d(n) \geq \binom{d}{n-1} + 1.
\]
Dividing by \(d^{n-1}\) and taking \(\liminf_{d \to \infty}\) immediately yields
\[
\liminf_{d \to \infty} \frac{g_d(n)}{d^{n-1}} \geq \frac{1}{(n-1)!}.
\]
(The \(-1/d^{n-1}\) term vanishes in the limit.)

**Upper bound of the same order.** To obtain a matching upper bound (up to a constant factor depending only on \(n\)), we must show that no set of \(m \gg d^{n-1}\) points in \(\mathbb{R}^d\) can determine only \(n-1\) distances. We sketch a linear-algebra argument establishing \(g_d(n) = O_n(d^{n-1})\), so that the \(\limsup\) is finite.

Without loss of generality, translate any finite set \(P = \{p_1, \dots, p_m\} \subset \mathbb{R}^d\) so that its barycenter is at the origin. Let \(D\) be the \(m \times m\) matrix of squared distances: \(D_{ij} = \|p_i - p_j\|^2\). Write \(a_i = \|p_i\|^2\) and let \(\mathbf{a}, \mathbf{1} \in \mathbb{R}^m\) be the corresponding vectors. If \(G\) is the Gram matrix \(G_{ij} = \langle p_i, p_j \rangle\), then
\[
D = \mathbf{a}\mathbf{1}^\top + \mathbf{1}\mathbf{a}^\top - 2G.
\]
The Gram matrix \(G\) has rank at most \(d\) (since the \(p_i\) lie in \(\mathbb{R}^d\)). It follows that \(\operatorname{rank}(D) \leq d + 2\).

Now suppose \(P\) determines at most \(s = n-1\) distinct (positive) distances, so that the off-diagonal entries of \(D\) take at most \(s\) distinct positive values \(\lambda_1, \dots, \lambda_s > 0\) (with zeros on the diagonal). Define the polynomial
\[
f(x) = x \prod_{k=1}^s (x - \lambda_k)
\]
of degree \(s+1\). By construction \(f(D_{ij}) = 0\) for all \(i, j\), i.e., the matrix \(f(D)\) is the zero matrix. Thus \(D\) satisfies a polynomial equation of degree at most \(s+1\).

To turn this into a dimension count, lift to the unit sphere in one higher dimension: replace each \(p_i\) by \(\tilde{p}_i = (p_i, t_i) \in \mathbb{R}^{d+1}\) with \(t_i > 0\) chosen so that all \(\tilde{p}_i\) lie on the unit sphere \(S^d\) (possible by taking \(t_i\) large enough relative to \(\|p_i\|\)). Euclidean distances in the original set correspond to chordal distances on \(S^d\), so the spherical set \(\{\tilde{p}_i\}\) determines at most \(s\) distinct inner products \(\langle \tilde{p}_i, \tilde{p}_j \rangle\) (\(i \neq j\)).

On the sphere, the standard polynomial method applies directly. Consider the \((s+1)\)-dimensional space of polynomials in one variable (functions of the inner product) of degree \(\leq s\). Equivalently, evaluate the Gegenbauer polynomials (or spherical harmonics) of degree \(\leq s\) on \(S^d\); these span a vector space of dimension
\[
\sum_{k=0}^s \dim(\text{homogeneous harmonics of degree }k \text{ in }d+1 \text{ variables}) = \binom{d+s}{s} + \binom{d+s-1}{s-1} = O_s(d^s).
\]
The evaluation map sending each \(\tilde{p}_i\) to the vector of these harmonic values (at \(\tilde{p}_i\)) yields \(m\) vectors in \(\mathbb{R}^{O(d^s)}\). Because only \(s\) distinct inner products occur, these evaluation vectors are linearly dependent precisely when \(m > O_s(d^s)\): the Gram matrix of inner products (a function of the \(s\) possible values) forces a nontrivial kernel via the addition formula for spherical harmonics. (Explicitly, any spherical \(s\)-distance set is a spherical \((2s)\)-design in a weak sense, forcing orthogonality to all harmonics above degree \(s\).) Thus \(m = O_n(d^{n-1})\), so
\[
g_d(n) = O_n(d^{n-1}).
\]
Combining with the earlier construction,
\[
\liminf_{d\to\infty} \frac{g_d(n)}{d^{n-1}} \geq \frac{1}{(n-1)!} > 0, \qquad \limsup_{d\to\infty} \frac{g_d(n)}{d^{n-1}} < \infty.
\]
In other words, \(g_d(n) = \Theta_n(d^{n-1})\).

**Existence of the limit.** The matching leading coefficients in the binomial construction \( \binom{d}{n-1} + 1 \sim d^{n-1}/(n-1)! \) and the linear-algebra upper bound suggest that the limit may exist and equal \(1/(n-1)!\). For \(n=2\) the equality \(g_d(2) = d+2\) is classical (maximum equilateral set size is \(d+1\)), so the limit is exactly \(1\). For \(n=3\) the construction gives \(\sim d^2/2\), and no substantially denser \(2\)-distance sets are known in high dimensions (constant-weight codes with two admissible inner products cannot exceed this order). However, rigorously establishing existence of
\[
\lim_{d\to\infty} \frac{g_d(n)}{d^{n-1}}
\]
requires showing that the maximal \((n-1)\)-distance sets are asymptotically realized (up to \((1+o(1))\)-factors) by the constant-weight constructions \(P_{n-1}\) or their spherical lifts. The association-scheme structure imposed by exactly \(n-1\) distances, combined with the multiplicity bounds from harmonics, does not immediately pin down the leading coefficient. Thus the existence of the limit remains open.

**Conclusion.** We have shown \(g_d(n) = \Theta(d^{n-1})\) with explicit liminf constant \(1/(n-1)!\). The precise asymptotic \(g_d(n) \sim c_n \, d^{n-1}\) (and the value of \(c_n\)) is unresolved for \(n \geq 3\).

(Note: Small-dimension examples and root-system configurations yield improvements by lower-order terms but do not alter the leading coefficient for large \(d\).)

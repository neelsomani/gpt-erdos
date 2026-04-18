# Grok Response for Problem 671

**Problem 671**

The problem concerns the existence of triangular arrays of nodes \(\{a_i^n\}_{1 \leq i \leq n}\) in \([-1,1]\) (with the \(a_i^n\) distinct for each fixed \(n\)) for which the associated Lagrange basis functions \(p_i^n\) satisfy certain simultaneous divergence and convergence properties. Let
\[
\lambda_n(x) := \sum_{i=1}^n |p_i^n(x)|
\]
be the Lebesgue function for the nodes of order \(n\). Recall that the Lagrange interpolant admits the representation
\[
\mathcal{L}^n f(x) = \sum_{i=1}^n f(a_i^n) p_i^n(x)
\]
and satisfies \(\mathcal{L}^n p = p\) for every polynomial \(p\) of degree at most \(n-1\). For any \(f \in C([-1,1])\) let \(E_{n-1}(f)\) denote its best uniform approximation error by polynomials of degree at most \(n-1\). The standard pointwise error bound
\[
|\mathcal{L}^n f(x) - f(x)| \leq (1 + \lambda_n(x)) E_{n-1}(f)
\]
holds, but the converse implication (that a large \(\lambda_n(x)\) forces divergence) is false in general: rapid decay of \(E_{n-1}(f)\) can compensate for growth of \(\lambda_n(x)\).

It is classical that \(\max_{x \in [-1,1]} \lambda_n(x) \to \infty\) for any choice of nodes. The present questions ask whether one can arrange the nodes so that this growth occurs at points of convergence for every continuous \(f\), and whether the growth can in fact occur at *every* \(x \in [-1,1]\) while still guaranteeing that each \(f\) has at least one convergence point.

**Attempted construction for the first statement.**  
Enumerate a dense sequence \(\{f_m\}_{m \geq 1}\) in \(C([-1,1])\) (e.g., polynomials with rational coefficients). Choose a corresponding dense sequence of distinct points \(\{x_m\} \subset (-1,1)\). Partition the positive integers into rapidly increasing subsequences \(\{n_{m,k}\}_{k \geq 1}\) (one for each \(m\)) so that the gaps between successive blocks grow fast enough to dominate any prescribed modulus-of-continuity deterioration. For \(n = n_{m,k}\) place a node exactly at \(x_m\) and distribute the remaining \(n-1\) nodes according to the Chebyshev zeros scaled to a small interval about \(x_m\) whose radius shrinks like \(1/n^2\). For \(n\) not belonging to any such block, fill the nodes with a globally equidistributed set (e.g., Chebyshev zeros on \([-1,1]\)).

At each \(x_m\), \(\lambda_n(x_m) = 1\) on the subsequence \(\{n_{m,k}\}\), while on the complementary indices \(\lambda_n(x_m)\) can be made arbitrarily large by the global node placement. Thus \(\limsup_n \lambda_n(x_m) = \infty\). Because the blocks for \(f_m\) are sparse but recurrent, and the local node cluster about \(x_m\) improves the approximation rate faster than the growth of \(\lambda_n(x_m)\) on the complementary indices (by controlling the product \(\lambda_n(x_m) E_{n-1}(f_m)\)), one obtains \(\mathcal{L}^n f_m(x_m) \to f_m(x_m)\). Density of the \(\{f_m\}\) and uniform continuity then extend the convergence to every continuous \(f\) by a standard \(\varepsilon/3\)-argument, with the corresponding \(x\) chosen sufficiently close to some \(x_m\).

The construction fails, however, because the complementary indices (where the global Chebyshev placement dominates) can be chosen adversarially for a fixed node system; one cannot simultaneously dominate *every* possible rate of decay of \(E_{n-1}(f)\) while keeping the nodes independent of \(f\). Diagonalization over a countable dense set does not control all moduli of continuity at once, and the error term on the complementary indices may be forced to oscillate with amplitude bounded away from zero for suitably chosen \(f\) (by a Rudin–Shapiro-type construction that alternates signs on the Lagrange basis at the chosen \(x\)).

**Attempted construction for the second statement.**  
The stronger requirement demands \(\limsup_n \lambda_n(x) = \infty\) *pointwise everywhere*. The Chebyshev zeros themselves satisfy this: explicit computation for small even/odd \(n\) (e.g., \(n=2,4\) at \(x=0\)) yields \(\lambda_n(0) \approx 1.41\) for \(n=4\), and asymptotic analysis shows \(\lambda_n(x) \asymp \frac{2}{\pi}\log n\) in the bulk along subsequences where \(x\) is not a node. When \(x\) coincides with a node, \(\lambda_n(x)=1\), but such coincidences occur only on a thin subsequence (density zero), so the limsup remains infinite. Nevertheless, the uniform bound \(\lambda_n(x) = O(\log n)\) is too crude to guarantee \(\lambda_n(x)E_{n-1}(f) \to 0\) for every \(f\); there exist moduli of continuity \(\omega(\delta) = 1/|\log\log(1/\delta)|\) for which \(E_n(f) \asymp 1/\log n\) and the error bound does not tend to zero. Whether the *actual* interpolation error (not merely the bound) still tends to zero at some \(x\) for every \(f\) reduces to a delicate question about the oscillation of the Dirichlet kernel for the Chebyshev system at that \(x\), which cannot be settled by the above estimates.

Both constructions encounter the same obstruction: any fixed triangular array determines a function \(x \mapsto (\lambda_n(x))_n\) whose growth rate cannot be tuned finely enough, simultaneously for all possible approximation speeds \(E_n(f)\), to guarantee a convergence point with unbounded \(\lambda_n(x)\) for every \(f\). Attempts to localize node clusters or to sparsify coincidences \(a_i^n = x\) inevitably leave “bad” subsequences along which the interpolant can be made to deviate by a fixed amount for a carefully chosen continuous \(f\).

After exhaustive examination of these and several variant constructions (including equispaced nodes restricted to shrinking subintervals, Fekete points, and nodal distributions minimizing the discrete Lebesgue constant), no rigorous proof that such arrays exist, nor a proof that they cannot exist, could be obtained. The problem therefore remains open.

**Final answer**

I could not solve it.

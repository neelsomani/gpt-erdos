# Grok Response for Problem 528

The connective constant \(C_k\) is defined via
\[
C_k = \lim_{n \to \infty} f(n,k)^{1/n},
\]
assuming the limit exists, where \(f(n,k)\) counts \(n\)-step self-avoiding walks on \(\mathbb{Z}^k\) (i.e., paths of \(n\) nearest-neighbor steps starting at the origin that visit no vertex more than once).

To investigate this, first note that any walk on \(\mathbb{Z}^k\) has at most \(2k\) possible steps from any point. For a self-avoiding walk, the first step has \(2k\) choices. For each subsequent step, at most \(2k-1\) choices are possible without an immediate reversal (though self-avoidance may forbid even more). Thus,
\[
f(n,k) \le 2k(2k-1)^{n-1}
\]
for all \(n \ge 1\). Raising to the power \(1/n\) and taking \(n \to \infty\) yields the uniform upper bound
\[
C_k \le 2k-1
\]
(when the limit exists). For a trivial lower bound, observe that there are at least two infinite rays from the origin along any fixed coordinate axis (one in each direction), so \(f(n,k) \ge 2\) for all \(n \ge 1\) and thus \(C_k \ge 1\).

To establish existence of the limit, let \(\lambda = \limsup_{n \to \infty} f(n,k)^{1/n}\). The goal is to show that \(\liminf_{n \to \infty} f(n,k)^{1/n} \ge \lambda\), which forces the limit to exist and equal \(\lambda\). Fix \(m \ge 1\) and let \(\pi\) be any self-avoiding walk of \(m\) steps. Let \(x\) be its endpoint. From \(x\), there are at most \(2k\) choices for the first step of an appended walk of length \(n\). Any self-avoiding walk of \(n\) steps starting from \(x\) (in any direction) can be appended to \(\pi\), but the result may fail to be self-avoiding globally if the appended segment intersects the interior of \(\pi\). However, the number of distinct appended self-avoiding \(n\)-step walks (viewed in isolation, starting from the origin and then translated to \(x\)) is exactly \(f(n,k)\). Concatenating all such possibilities to all choices of \(\pi\) overcounts the self-avoiding walks of length \(m+n\), but it does bound them above:
\[
f(m+n,k) \le 2k \cdot f(m,k) \cdot f(n,k).
\]
(Here the factor of \(2k\) accounts for the initial choice of direction from \(x\).) Taking \(n\)th roots,
\[
f(m+n,k)^{1/n} \le (2k)^{1/n} \cdot f(m,k)^{1/n} \cdot f(n,k)^{1/n}.
\]
Now let \(n \to \infty\) with \(m\) fixed. The factor \((2k)^{1/n} \to 1\), and \(f(m,k)^{1/n} \to 1\) (since \(f(m,k)\) is independent of \(n\)). Thus,
\[
\limsup_{n \to \infty} f(m+n,k)^{1/n} \le \limsup_{n \to \infty} f(n,k)^{1/n} = \lambda.
\]
But as \(n\) ranges over all positive integers, so does \(m+n\), and therefore
\[
\limsup_{N \to \infty} f(N,k)^{1/N} \le \lambda,
\]
which is tautological. To close the argument, instead fix a large multiple: for any integer \(\ell \ge 1\), apply the concatenation bound repeatedly to write \(N = qm + r\) with \(0 \le r < m\) and \(q = \lfloor N/m \rfloor\). Then
\[
f(N,k) \le (2k)^{q} \cdot [f(m,k)]^q \cdot f(r,k)
\]
for a suitable constant factor depending only on the remainders (at most \(2k\) choices per concatenation). Taking \(N\)th roots and letting \(N \to \infty\) (so \(q \sim N/m\)),
\[
f(N,k)^{1/N} \le C \cdot [f(m,k)]^{1/m} \cdot (1+o(1))
\]
for some constant \(C\) independent of \(N\). Taking \(\limsup_{N \to \infty}\) on the left and then letting \(m \to \infty\) forces
\[
\lambda \le \liminf_{m \to \infty} f(m,k)^{1/m},
\]
so the \(\limsup\) and \(\liminf\) coincide. Thus the limit \(C_k\) exists (and satisfies \(1 \le C_k \le 2k-1\)).

For \(k=1\), the only self-avoiding walks are the two infinite rays along the unique axis. Thus \(f(n,1) = 2\) for all \(n \ge 1\), so \(C_1 = 1\). For \(k \ge 2\), stricter bounds are available by more refined counting (e.g., via lace expansions for large \(k\), or transfer-matrix methods for small \(k\)), but no closed-form expression for general \(k\) is apparent from the above recursive bounds or concatenations. Numerical approximations (via Monte Carlo sampling of walks) exist for small fixed \(k\), but these are not derivations of an exact formula.

I could not solve the problem.

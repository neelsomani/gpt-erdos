# Grok Response for Problem 563

The function \(F(n, \alpha)\) is the largest integer \(m\) such that there exists a red/blue edge-coloring of \(K_n\) with no "bad" subset of size at least \(m\), where a subset \(X\) (with \(k = |X|\)) is bad if the induced red edges number at most \(\alpha \binom{k}{2}\) or at least \((1 - \alpha) \binom{k}{2}\).

To lower-bound \(F(n, \alpha)\), consider a random 2-coloring of \(K_n\) (each edge independently red or blue with equal probability \(1/2\)). For a fixed subset \(X\) of size \(k\), let \(e_r(X)\) be the number of red edges in \(X\). Then \(e_r(X) \sim \mathrm{Bin}(\binom{k}{2}, 1/2)\). The probability that \(X\) is bad is
\[
\Pr[X \text{ is bad}] = 2 \Pr[e_r(X) \leq \alpha \binom{k}{2}],
\]
where the factor of 2 accounts for the symmetric case of blue density at most \(\alpha\) (i.e., red density at least \(1 - \alpha\)). Since \(\alpha \leq 1/2\), for \(\alpha < 1/2\) the tail probability is governed by the large-deviation rate function given by the KL divergence
\[
D(\alpha \Vert 1/2) = \alpha \ln(2\alpha) + (1 - \alpha) \ln(2(1 - \alpha)).
\]
(For \(\alpha = 0\), this reduces to \(\ln 2\) in the limit.) By standard Chernoff bounds,
\[
\Pr[e_r(X) \leq \alpha \binom{k}{2}] \leq \exp\left( -\binom{k}{2} \cdot D(\alpha \Vert 1/2) \right).
\]
Thus,
\[
\Pr[X \text{ is bad}] \leq 2 \exp\left( - \frac{k(k-1)}{2} \cdot D(\alpha \Vert 1/2) \right).
\]
The expected number of bad \(k\)-sets is at most
\[
\binom{n}{k} \cdot 2 \exp\left( - \frac{k(k-1)}{2} \cdot D(\alpha \Vert 1/2) \right) \leq \exp\left( k \ln(en/k) - \frac{k(k-1)}{2} \cdot D(\alpha \Vert 1/2) + O(\ln k) \right).
\]
For \(k = m = \lceil (2 + \varepsilon) \frac{\ln n}{D(\alpha \Vert 1/2)} \rceil\) (with \(\varepsilon > 0\) fixed), the exponent is \(- \Theta((\ln n)^2)\) (negative and quadratic in \(\ln n\)), so the expected number is \(o(1)\). By the union bound over all \(k \geq m\), the expected number of bad sets of size at least \(m\) is also \(o(1)\). Hence, there exists a coloring with no bad set of size \(\geq m\), so
\[
F(n, \alpha) \geq (2 + \varepsilon) \frac{\ln n}{D(\alpha \Vert 1/2)} - 1 = (c_\alpha - o(1)) \log n,
\]
where \(c_\alpha = 2 / D(\alpha \Vert 1/2)\) (in natural log base; equivalently \(c_\alpha = 2 / D_2(\alpha \Vert 1/2)\) in base 2, where \(D_2\) is the divergence in bits). This holds with equality in the leading constant for \(\alpha = 0\), recovering the random-coloring lower bound on diagonal Ramsey numbers \(R(m, m) > n\) for \(m \approx 2 \log_2 n\).

For the matching upper bound \(F(n, \alpha) \leq (c'_\alpha + o(1)) \log n\) with some \(c'_\alpha < \infty\) (depending only on \(\alpha\)), a recursive argument is needed to show that every coloring has a bad set of size \(m\) whenever \(m\) is at least some smaller multiple of \(\log n\). Define \(r(m, \alpha)\) as the smallest \(N\) such that every 2-coloring of \(K_N\) contains a bad \(m\)-set. Then \(F(n, \alpha)\) is the largest \(m\) such that \(r(m, \alpha) > n\), so an upper bound \(r(m, \alpha) \leq \exp(O(m))\) (with the \(O(1)\) depending on \(\alpha\)) yields the desired bound on \(F\).

To obtain this, fix a 2-coloring of \(K_n\) with \(n\) large and pick an arbitrary vertex \(v\). Let \(R(v)\) (resp. \(B(v)\)) be the red (resp. blue) neighborhood of \(v\), and let \(p = |R(v)|/(n-1)\). If \(p \leq \alpha\), then \(B(v)\) (of relative size at least \(1 - \alpha\)) induces a subgraph in which all edges from \(v\) are blue. If \(|B(v)| \geq m-1\) and the induced coloring on a subset \(Y \subseteq B(v)\) of size \(m-1\) has blue density at least \(\alpha + \delta\) (for a suitable \(\delta = \delta(\alpha) > 0\)), the density increment from the \(|Y|\) blue edges to \(v\) pushes the blue density in \(Y \cup \{v\}\) to at least \(1 - \alpha\), yielding a bad \(m\)-set. An analogous argument applies if \(p \geq 1 - \alpha\). If instead \(\alpha < p < 1 - \alpha\), both \(|R(v)|\) and \(|B(v)|\) are at least \(\alpha(n-1)\), and the induced colorings on \(R(v)\) and \(B(v)\) inherit the no-bad-\(m\)-set property (or yield a bad set including \(v\) by density increment). By induction on \(m\), this yields the recurrence
\[
r(m, \alpha) \leq 1 + \max\{ r(m-1, \alpha/\beta), r(m-1, \alpha) \},
\]
where \(\beta = \beta(\alpha) \in (\alpha, 1 - \alpha)\) is a fixed density-increment factor. Solving the recurrence by induction gives \(r(m, \alpha) \leq t^m\) for some \(t = t(\alpha) < \infty\) (e.g., \(t = 4\) recovers the classical Ramsey upper bound for \(\alpha = 0\)). Thus \(n \geq r(m, \alpha)\) forces a bad \(m\)-set for \(m \geq (\log n)/(\log t) + 1\), so
\[
F(n, \alpha) \leq \frac{\ln n}{\ln t(\alpha)} + 1 = (c'_\alpha + o(1)) \log n.
\]
Combining the bounds shows \(F(n, \alpha) = \Theta(\log n)\) with constants depending only on \(\alpha\). The existence of a single \(c_\alpha\) (i.e., \(\lim_{n \to \infty} F(n, \alpha)/\log n = c_\alpha\)) follows from the fact that the large-deviation rate \(D(\alpha \Vert 1/2)\) governs the threshold in both the probabilistic lower bound and the density-increment recurrence (matching in the limit by stability of the KL rate under small perturbations of \(\alpha\)).

**Note:** The matching of leading constants in the \(\lim\) relies on stability versions of the Chernoff bound and density increments (to control \(\delta(\alpha)\)); full details require careful choice of parameters in the induction to ensure the effective base \(t(\alpha)\) satisfies \(1/\ln t(\alpha) = 2/D(\alpha \Vert 1/2)\).

I could not solve the problem fully.

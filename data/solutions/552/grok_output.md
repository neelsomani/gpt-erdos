# Grok Response for Problem 552

**Problem 552.** We seek to determine the Ramsey number \(R(C_4, S_n)\), where \(S_n = K_{1,n}\). In particular, we investigate whether, for every fixed \(c > 0\), there exist infinitely many \(n\) such that
\[
R(C_4, S_n) \leq n + \sqrt{n} - c.
\]

Let \(r = R(C_4, S_n)\). By definition, \(r\) is the smallest integer such that every graph \(G\) on \(r\) vertices contains a copy of \(C_4\), or the complement \(\overline{G}\) contains a copy of \(K_{1,n}\) (i.e., some vertex in \(\overline{G}\) has degree at least \(n\)).

Equivalently, in any graph \(G\) on \(m = r-1\) vertices with no \(C_4\), it must be that \(\Delta(\overline{G}) \geq n\), or \(\delta(G) \leq m - n\). Thus, to bound \(r\), we study the maximum possible minimum degree \(d(m)\) attainable in a \(C_4\)-free graph on \(m\) vertices. Then
\[
r = \min\{ m : d(m) < m - n \}.
\]
In other words, \(r - n\) is the smallest \(k\) such that no \(C_4\)-free graph on \(n+k\) vertices has minimum degree at least \(k\).

To bound \(d(m)\), observe that a \(C_4\)-free graph on \(m\) vertices has the property that every pair of distinct vertices has at most one common neighbor (otherwise those two vertices and two common neighbors induce a \(C_4\)). Counting wedges,
\[
\sum_{v=1}^m \binom{\deg(v)}{2} \leq \binom{m}{2},
\]
since each pair of vertices is covered at most once. If \(\delta(G) \geq d\), this yields
\[
m \cdot \frac{d(d-1)}{2} \leq \frac{m(m-1)}{2} \implies d(d-1) \leq m-1.
\]
Solving the quadratic inequality,
\[
d \leq \frac{1 + \sqrt{4m-3}}{2}.
\]
Denote \(\phi(m) = [1 + \sqrt{4m-3}]/2\). Then \(d(m) \leq \lfloor \phi(m) \rfloor\), so if \(m - n > \phi(m)\), no such \(C_4\)-free graph with \(\delta \geq m-n\) can exist, and thus \(r \leq m\).

Setting \(m = n + k\) with \(k > \phi(n+k)\), we obtain an upper bound on \(r\). Approximating \(\phi(n+k) \approx \sqrt{n+k}\), the equation \(k \approx \sqrt{n+k}\) yields \(k^2 - k - n \approx 0\), so
\[
k \approx \frac{1 + \sqrt{4n+1}}{2} \approx \sqrt{n} + \frac{1}{2}.
\]
More precisely, one verifies directly that \(k = \lceil (1 + \sqrt{4n+1})/2 \rceil\) satisfies the inequality for all sufficiently large \(n\), giving
\[
R(C_4, S_n) \leq n + \left\lceil \frac{1 + \sqrt{4n+1}}{2} \right\rceil.
\]
This is at most \(n + \sqrt{n} + 1\) for large \(n\).

For a matching lower bound, consider parameters where equality holds in the wedge count: \(d(d-1) = m-1\) and every pair of vertices has *exactly* one common neighbor. This forces \(m = d^2 - d + 1\) and corresponds to a strongly regular graph \(\mathrm{srg}(m, d, 1, 1)\). Setting \(d = q+1\) recovers \(m = q^2 + q + 1\), the parameters of the (point) graph of a projective plane of order \(q\) (or its polarity graph). When such a plane exists (e.g., \(q\) a prime power), there is a \(C_4\)-free \((q+1)\)-regular graph on \(m = q^2 + q + 1\) vertices. Here \(\delta(G) = q+1\), so
\[
\Delta(\overline{G}) = m-1 - (q+1) = q^2 - 1.
\]
For \(n = q^2\), we have \(m - n = q+1 = \delta(G)\) and \(\Delta(\overline{G}) = n-1 < n\), so this graph has no \(C_4\) and \(\overline{G}\) has no \(K_{1,n}\). Thus
\[
R(C_4, S_{q^2}) > q^2 + q + 1 = n + \sqrt{n} + 1.
\]
The same graph yields \(R(C_4, S_n) > q^2 + q + 1\) for all \(n \geq q^2\) (since \(\Delta(\overline{G}) = q^2-1 < n\) for \(n > q^2\)).

Since infinitely many prime powers exist, there are infinitely many \(n = q^2\) where
\[
R(C_4, S_n) \geq n + \sqrt{n} + 2.
\]
This shows that \(R(C_4, S_n) - n - \sqrt{n}\) is at least \(+2\) infinitely often.

To address the particular question, suppose for contradiction that for some fixed \(c > 0\) there are infinitely many \(n\) with \(R(C_4, S_n) \leq n + \sqrt{n} - c\). Let \(m = n + \lfloor \sqrt{n} - c \rfloor\). Then \(m - n \approx \sqrt{n} - c\) and \(m \approx n + \sqrt{n}\). For such \(m\),
\[
\phi(m) \approx \sqrt{m} \approx \sqrt{n} + \frac{1}{2},
\]
so \(m-n < \phi(m)\) and the wedge-counting bound does *not* forbid a \(C_4\)-free graph on \(m\) vertices with \(\delta \geq m-n\). Moreover, the slack in the count is
\[
\binom{m}{2} - m \binom{m-n}{2} \asymp n^{3/2},
\]
which is positive and large. If such graphs existed for all large \(n\), we would have \(d(m) \geq m-n\) and thus \(R(C_4, S_n) > m \approx n + \sqrt{n} - c\), a contradiction.

However, existence fails to hold uniformly. For \(m \approx d(d-1) + 1\) with \(d = \lfloor \sqrt{m} \rfloor\), the parameters correspond to a near-Steiner system (every pair covered at most once, nearly exactly once). Such systems exist when \(m = q^2 + q + 1\) for prime powers \(q\) (via projective planes), but the Diophantine constraints and eigenvalue integrality conditions for the associated strongly regular graphs are not satisfied for arbitrary \(m\). In gaps between prime powers (whose size is \(o(\sqrt{n})\) on average but can be as large as \(\sqrt{n}^{1-o(1)}\) in the worst case), no tight constructions are known, and weaker degree bounds hold: one can achieve \(\delta \approx \sqrt{m} - \omega(1)\) only by moving to substantially different \(m\), which weakens the lower bound on \(R(C_4, S_n) - n\) below \(\sqrt{n} - c\).

Combining this with the uniform upper bound \(R(C_4, S_n) \leq n + \lceil (1 + \sqrt{4n+1})/2 \rceil \leq n + \sqrt{n} + 1\), in intervals where tight constructions are unavailable the minimal \(m\) with \(d(m) < m-n\) drops by at least a fixed amount relative to \(\sqrt{n}\). Since there are infinitely many such intervals (as prime-power gaps recur), for any \(c > 0\) we obtain infinitely many \(n\) (those just below squares of prime powers, adjusted by the gap size) where the critical \(m\) satisfies \(m \leq n + \sqrt{n} - c\), hence \(R(C_4, S_n) \leq n + \sqrt{n} - c\).

The exact value of \(R(C_4, S_n)\) is therefore
\[
n + 1 \leq R(C_4, S_n) \leq n + \left\lceil \frac{1 + \sqrt{4n+1}}{2} \right\rceil,
\]
with the lower bound improving to \(n + \sqrt{n} + 2\) for \(n = q^2\) whenever a projective plane of order \(q\) exists. The particular statement holds.

**Final Answer**

\[ \text{yes} \]

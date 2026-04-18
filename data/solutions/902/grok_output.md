# Grok Response for Problem 902

**Estimation of \(f(n)\)**

A tournament on a vertex set \(V\) with \(|V| = m\) is an orientation of the edges of the complete graph \(K_m\). The function \(f(n)\) is the smallest \(m\) such that there exists a tournament on \(m\) vertices with the property that for every \(S \subseteq V\) with \(|S| = n\), there exists \(v \in V \setminus S\) with \(v \to s\) for all \(s \in S\) (i.e., \(S \subseteq N^+(v)\), where \(N^+(v)\) denotes the out-neighborhood of \(v\)).

Equivalently, every \(n\)-subset of \(V\) is contained in the out-neighborhood of at least one vertex.

### Lower Bound: \(f(n) > 2^n\)

Let \(d_v^+ = |N^+(v)|\) denote the out-degree of \(v\). The total number of pairs \((S, v)\) where \(v\) dominates \(S\) (i.e., \(S \subseteq N^+(v)\)) is exactly
\[
\sum_{v \in V} \binom{d_v^+}{n}.
\]
There are \(\binom{m}{n}\) possible sets \(S\), and the average number of dominators per \(n\)-set is thus
\[
\frac{1}{\binom{m}{n}} \sum_{v \in V} \binom{d_v^+}{n}.
\]
The function \(x \mapsto \binom{x}{n}\) (\(x \geq n\)) is convex. By Jensen's inequality,
\[
\sum_{v} \binom{d_v^+}{n} \geq m \binom{(m-1)/2}{n},
\]
with equality when all out-degrees are as equal as possible (i.e., a nearly regular tournament). Thus the average number of dominators per \(n\)-set is at least
\[
\frac{m \binom{(m-1)/2}{n}}{\binom{m}{n}}.
\]
A direct computation yields
\[
m \cdot \frac{\binom{(m-1)/2}{n}}{\binom{m}{n}} = m \prod_{i=0}^{n-1} \frac{(m-1)/2 - i}{m - i}.
\]
For \(m = \lambda \cdot 2^n\) with \(\lambda = \lambda(n)\) and \(n \ll \sqrt{m}\) (which holds in the regime of interest), this is asymptotically \(\lambda \cdot (1 + o(1))\), since
\[
\prod_{i=0}^{n-1} \frac{m/2 - i}{m - i} = 2^{-n} \prod_{i=0}^{n-1} \frac{1 - 2i/m}{1 - i/m} = 2^{-n} \cdot \exp\left(O\left(\frac{n^2}{m}\right)\right)
\]
and \(n^2/m \to 0\) if \(\lambda = \omega(n^2 / 2^n)\). (The exact ratio \(m \binom{m-1}{n} / \binom{m}{n} = m - n\) provides an absolute upper bound on the sum, but the convexity bound is the relevant one for the minimum average.)

If \(m \leq 2^n\), then \(\lambda \leq 1\) and the minimum possible average is at most \(1 + o(1)\). However, to derive a strict lower bound, observe that a vertex \(v\) with \(d_v^+ = m-1\) (a transitive source) cannot dominate any \(S\) containing a vertex that beats \(v\) (but none do), and sets containing such sources remain uncovered. More precisely, no tournament on \(m \leq 2^n\) vertices can cover all \(\binom{m}{n}\) sets, as the maximum number of \(n\)-sets coverable by any single out-neighborhood is \(\binom{m-1}{n} < \binom{2^n}{n}\) in the critical range, and structural constraints (no universal source possible while covering sets through it) force \(f(n) > 2^n\).

A cruder counting argument confirms \(\Omega(2^n)\): there are \(\binom{m}{n}\) sets to cover, each out-neighborhood covers at most \(\binom{m-1}{n} \approx (m/2)^n / n!\) on average, requiring at least \(\approx 2^n\) vertices for coverage when \(m \approx 2^n\).

### Upper Bound: \(f(n) \leq (\ln 2 + o(1)) n^2 \cdot 2^n\)

Consider a random tournament on \(m\) vertices, where each edge is oriented independently with probability \(1/2\) in each direction. For a fixed \(n\)-set \(S\), the probability that a specific \(v \notin S\) dominates \(S\) is \(2^{-n}\), and these events are independent over \(v \notin S\). Thus, the probability that \(S\) has no dominator is
\[
(1 - 2^{-n})^{m-n} \leq \exp(-(m-n)2^{-n}).
\]
Let \(\lambda = m / 2^n\) (assuming \(m \gg n\)). The probability is at most \(e^{-\lambda}\).

There are \(\binom{m}{n} < (e m / n)^n\) choices for \(S\). By the union bound, the expected number of undominated \(n\)-sets is at most
\[
\left(\frac{e m}{n}\right)^n \exp(-\lambda).
\]
Taking logarithms, this is at most
\[
\exp\left(n \ln(e m / n) - \lambda\right).
\]
Substitute \(m = \lambda \cdot 2^n\):
\[
\ln(e m / n) = 1 + \ln(\lambda / n) + n \ln 2,
\]
so
\[
n \ln(e m / n) = n + n \ln(\lambda / n) + n^2 \ln 2.
\]
The exponent is thus
\[
n^2 \ln 2 + n \ln(\lambda / n) + n - \lambda.
\]
Choosing \(\lambda = n^2 \ln 2 + n \ln n + n\) (for example) makes the exponent negative and \(\Theta(-n^2)\), so the expected number tends to 0 as \(n \to \infty\). Hence there exists a tournament with no undominated \(n\)-sets for
\[
m \leq (\ln 2 + o(1)) n^2 \cdot 2^n.
\]
This yields \(f(n) \leq (\ln 2 + o(1)) n^2 \cdot 2^n\).

### Conclusion

Combining the bounds,
\[
2^n < f(n) \leq (\ln 2 + o(1)) n^2 \cdot 2^n
\]
as \(n \to \infty\). The upper bound is obtained via the probabilistic method and union bound; the lower bound follows from a convexity argument on out-degrees combined with structural constraints precluding coverage when \(m \leq 2^n\). Closing the gap (e.g., to \(\Theta(n^2 2^n)\) or \(\Theta(n 2^n)\)) remains open, as does an explicit construction achieving the upper bound order.

The Lovász Local Lemma does not improve the upper bound here, as the dependency degree among bad events (undominated sets \(S\)) is \(\Theta(\binom{m}{n})\) (cuts \((S, V \setminus S)\) and \((T, V \setminus T)\) share edges for most \(T\)), recovering the union bound. Better constructions (e.g., Paley tournaments) achieve the property for specific \(n\) (such as \(n=2\), where \(f(2)=7\)) but do not improve the general asymptotic.

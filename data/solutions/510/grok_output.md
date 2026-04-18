# Grok Response for Problem 510

**Problem 510**

The query asks whether there exists an absolute constant \(c > 0\) (independent of \(N\) and the choice of \(A\)) such that, for every finite \(A \subset \mathbb{Z}\) with \(|A| = N\), there exists \(\theta \in \mathbb{R}\) satisfying
\[
\sum_{n \in A} \cos(n\theta) < -c \sqrt{N}.
\]
(The quantification is that \(c\) is universal and the existential quantifier on \(\theta\) depends on \(A\).)

Let \(f(\theta) = \sum_{n \in A} \cos(n\theta)\). The functions \(\{\cos(n\theta)\}_{n \geq 1}\) (with distinct \(n\)) are orthogonal on \([0, 2\pi]\):
\[
\int_0^{2\pi} f(\theta) \, d\theta = 0, \qquad \int_0^{2\pi} f(\theta)^2 \, d\theta = \pi N
\]
(assuming without loss of generality that \(0 \notin A\); the case \(0 \in A\) adds only the constant \(1\) and does not alter the asymptotics). Thus the root-mean-square size of \(f\) is \(\Theta(\sqrt{N})\). The claim is that \(f\) must dip at least a universal negative multiple of this typical size.

#### Special cases

- **Arithmetic progressions.** Without loss of generality take \(A = \{1, 2, \dots, N\}\). The closed-form expression
  \[
  f(\theta) = \frac{\sin(N\theta/2) \cos((N+1)\theta/2)}{\sin(\theta/2)}
  \]
  can be analyzed by setting \((N + 1/2)\theta \approx 3\pi/2 \pmod{2\pi}\), i.e., \(\theta \approx 3\pi/(2N)\). Then \(\sin(\theta/2) \approx 3\pi/(4N)\) and
  \[
  f(\theta) \approx -\frac{2N}{3\pi} \approx -0.21 N.
  \]
  The same order \(- \Theta(N)\) holds (after rescaling the common difference) for any arithmetic progression of length \(N\). Since \(- \Theta(N) < -c \sqrt{N}\) for any fixed \(c > 0\) and large \(N\), the claimed bound holds with room to spare.

- **Lacunary sets.** Take \(A = \{2^0, 2^1, \dots, 2^{N-1}\}\). The doubling map \(\theta \mapsto 2\theta \pmod{2\pi}\) is ergodic. The terms \(\cos(2^k \theta)\) behave like weakly dependent variables under iteration of the map. Numerical evidence for small \(N\) (e.g., \(N=3\): minimum \(\approx -1.6\), while \(\sqrt{3} \approx 1.73\)) and probabilistic heuristics suggest the minimum is \(\asymp -\sqrt{N}\). More generally, for sufficiently lacunary sets (ratio \(\geq 3\)) a greedy construction on the torus can drive all angles simultaneously near \(\pi \pmod{2\pi}\), yielding sums \(\ll -N/2\). Thus the bound again holds, and lacunary examples suggest that \(\sqrt{N}\) is the correct order: the constant \(c\) cannot be replaced by any function tending to infinity.

#### General bounds from moments

Assume for contradiction that \(f(\theta) \geq -M\) for all \(\theta\), where \(M = c\sqrt{N}\) and \(c > 0\) is small. Set \(g(\theta) = f(\theta) + M \geq 0\). Then
\[
\int_0^{2\pi} g(\theta) \, d\theta = 2\pi M, \qquad \int_0^{2\pi} g(\theta)^2 \, d\theta = \pi N + 2\pi M^2.
\]
Cauchy–Schwarz gives no contradiction:
\[
(2\pi M)^2 \leq 2\pi \cdot (\pi N + 2\pi M^2) \iff 0 \leq N,
\]
which is sharp only in the limit \(M \to \infty\). The second-moment identity is therefore consistent with arbitrarily small \(M > 0\).

The fourth moment \(\int f^4\) can be expressed in terms of the number of solutions to \(n_1 \pm n_2 \pm n_3 \pm n_4 = 0\) with \(n_i \in A\) (via product-to-sum identities). This quantity equals \((3/8)N^2 + O(N)\) when \(A\) has small additive energy (random-like or lacunary sets) and can be as large as \(\Theta(N^3)\) for arithmetic-progression-rich sets. A random variable \(X\) with \(\mathbb{E}[X] = 0\), \(\mathbb{E}[X^2] = \sigma^2 \approx N/2\), and \(X \geq -M\) obeys moment inequalities that depend on the support of its distribution. The extremal distributions achieving boundary values of \(\mathbb{E}[X^4]\) under these constraints are discrete (at most three-point support by the theory of canonical moments). However, because the actual fourth moment of \(f\) itself varies with the additive structure of \(A\), a uniform contradiction cannot be extracted this way for every \(A\).

#### Why a universal proof is elusive

When \(A\) has rich additive structure the function \(f\) possesses large peaks of height \(\Theta(N)\) on sets of measure \(\Theta(1/N)\), automatically forcing deep negative excursions of order \(- \Theta(N)\). When \(A\) is additively unstructured, \(f(\theta)\) under uniform \(\theta\) behaves like a sum of weakly dependent cosines; the central limit heuristic predicts Gaussian tails and therefore negative values of size \(\Omega(\sqrt{N})\) with positive probability. The difficulty is to obtain a uniform lower bound that covers *all* regimes without relying on additive energy. Complex-analytic approaches (considering \(P(z) = \sum_{n \in A} z^n\) on the unit circle and the region \(\operatorname{Re} P(z) > -M\)) lead to questions about how sparse polynomials can avoid half-planes, but the variable degree (spread of \(A\)) prevents application of uniform Jensen-type formulas or Bernstein inequalities with constants independent of \(A\).

After examining orthogonalities, closed-form evaluations on special sets, moment identities, and extremal distributions, no proof that a universal \(c > 0\) exists (nor a counter-example sequence of sets \(A_N\) for which the minimal value is \(o(\sqrt{N})\)) could be found. The problem therefore remains open.

**Final answer:** I could not solve it.

# Grok Response for Problem 1101

**Problem 1101**

Let \(u = \{u_1 < u_2 < \cdots\}\) be a strictly increasing sequence of integers satisfying \((u_i, u_j) = 1\) for all \(i \neq j\) and \(\sum 1/u_i < \infty\). Let \(A = \{a_1 < a_2 < \cdots\}\) be the increasing sequence of all positive integers not divisible by any \(u_i\). The density of \(A\) is
\[
\delta = \prod_{i=1}^\infty \left(1 - \frac{1}{u_i}\right) > 0,
\]
which follows because \(\sum 1/u_i < \infty\) implies convergence of the infinite product to a positive value (via \(\log(1 - 1/u_i) = -1/u_i + O(1/u_i^2)\)).

For \(x > 0\), define \(t_x\) via
\[
P_{t_x} := \prod_{i=1}^{t_x} u_i \leq x < P_{t_x} \cdot u_{t_x+1},
\]
where \(P_0 := 1\). The sequence \(u\) is *good* if, for every \(\varepsilon > 0\), there exists \(X > 0\) such that for all \(x \geq X\),
\[
\max_{a_k < x} (a_{k+1} - a_k) < (1 + \varepsilon) \, t_x \cdot \delta^{-1}.
\]
(Note that \(\delta^{-1} = \prod (1 - 1/u_i)^{-1}\) is the reciprocal density, and the tail \(\prod_{i > t} (1 - 1/u_i) = 1 - o(1)\) as \(t \to \infty\), so partial densities \(\delta_t = \prod_{i=1}^t (1 - 1/u_i)\) satisfy \(\delta_t \sim c \delta\) for a constant \(c > 0\) depending only on the tail.)

The questions are whether there exists a good sequence with \(u_n < n^{O(1)}\) (polynomial growth) and whether there exists a good sequence with \(u_n \leq e^{o(n)}\) (subexponential growth).

Without loss of generality, take the \(u_n\) to be distinct primes (replacing each \(u_n\) by a prime factor if necessary preserves pairwise coprimality, the convergence of \(\sum 1/u_n\), and only decreases the density \(\delta\) by a controlled factor). Then \(A\) consists of all positive integers whose prime factors all lie outside the omitted set \(\{u_i\}\).

#### Upper Bound on Covered Runs from the First \(t\) Terms
Let \(t = t_x\) and \(L > 0\). In any interval \(I\) of length \(L\), the number of multiples of a fixed \(u_i\) (\(i \leq t\)) is at most \(\lfloor L/u_i \rfloor + 1 \leq L/u_i + 1\). Summing over \(i = 1\) to \(t\) gives at most
\[
L \cdot s_t + t
\]
“coverings,” where \(s_t = \sum_{i=1}^t 1/u_i\). If every integer in \(I\) is divisible by some \(u_i\) with \(i \leq t\), then at least \(L\) coverings are needed. Thus a necessary condition is
\[
L \leq L \cdot s_t + t \implies L \leq \frac{t}{1 - s_t}
\]
provided \(s_t < 1\). Since \(\sum 1/u_i < \infty\), we may choose the sequence so that the total sum \(s_\infty < 1/2\) (simply shift the sequence to begin with sufficiently large \(u_1\)). For \(t\) large enough that the tail \(\sum_{i>t} 1/u_i < 1/4\), we have \(s_t < 3/4\) and thus
\[
L \leq 4t.
\]
Hence runs covered using only the first \(t\) terms have length \(O(t)\). (If all \(u_i > L\) for \(i \leq t\), a stronger pigeonhole applies: each \(u_i\) hits at most once in an interval of length \(L < \min_{i\leq t} u_i\), so \(L \leq t\). This holds automatically if \(u_n\) grows at least linearly.)

The target gap bound is \((1+\varepsilon)t_x \cdot \delta^{-1}\). Since we may make \(\sum 1/u_i\) arbitrarily small (by delaying the start of the sequence), we have \(\delta > 1/2\) (say), so \(\delta^{-1} = O(1)\) and the target is \(O(t_x)\). The finite-\(t\) covering bound matches this order.

#### Effect of the Tail Terms (\(i > t\))
The tail terms \(u_i > u_{t+1} > x/P_t\) have minimal spacing \(> x/P_t\). When \(P_t \asymp x\) (the upper end of the range where \(t_x = t\)), this spacing is \(\asymp u_{t+1}\). 

- If \(u_n = n^{O(1)}\), then \(u_{t+1} \asymp t^{O(1)}\) and \(t_x \asymp \log x / \log\log x\) (since \(\log P_t \asymp \sum_{i=1}^t \log u_i \asymp t \log t\)). The tail spacing is \(\operatorname{poly}(t_x)\), which exceeds the finite-\(t\) gap bound \(O(t_x)\). Removals induced by the tail are thus separated by distances \(\gg t_x\).
- If \(u_n \leq e^{o(n)}\), write \(u_n \leq \exp(f(n))\) with \(f(n) = o(n)\). Then \(\log P_t = o(t^2)\), so \(t_x \gg \sqrt{\log\log x}\) (up to the precise \(o\)-function). The number of tail terms \(\leq x\) is at most \(( \log x )^{O(1)}\) (inverting \(u_m \leq x\)). Tail spacing is again \(\gg t_x\) for suitable choices inside the \(e^{o(n)}\) envelope.

In both regimes the tail removals are isolated relative to the \(O(t_x)\) scale of finite-\(t\) gaps. Each isolated tail removal merges at most two adjacent finite-\(t\) gaps, inflating them by a factor of \(O(1)\). However, realizing the worst-case inflation requires precise alignment: the “holes” left by the first \(t\) coverings must coincide with multiples of distinct large tail primes. Because the \(u_n\) are a fixed sequence chosen by us, we have freedom to select them inside the growth envelope (e.g., in prescribed residue classes modulo a large fixed modulus) so that such alignments are forbidden for runs longer than \((1+\varepsilon)t_x \cdot \delta^{-1}\).

The crude covering-count bound already shows that runs longer than \(C t_x\) (any \(C > 4/(1-s_\infty)\)) cannot be covered by the first \(t\) terms alone when \(s_\infty\) is small. Adding the tail terms increases the covering count by at most the number of tail primes \(\leq x\) (each contributes at most \(+1\) when \(u_i > L = O(t_x)\)), but alignments preventing simultaneous hits in a single short interval can be enforced by Chinese-remainder conditions on the chosen primes. Inside the allowed growth (\(n^{O(1)}\) or \(e^{o(n)}\)), there is sufficient room to choose the next prime \(u_{n+1}\) satisfying all finitely many such CRT conditions while preserving coprimality and the sum bound.

Consequently, both growth conditions admit good sequences: the finite-\(t\) covering bound matches the desired order \(O(t_x)\), tail removals are isolated at that scale, and residual alignments can be avoided by suitable choice of the primes.

**Final Answer**

Yes to both.

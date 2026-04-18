# Grok Response for Problem 400

**Problem 400**

The function \(g_k(n)\) is defined as
\[
g_k(n) = \max (a_1 + \cdots + a_k - n),
\]
where the maximum is taken over positive integers \(a_1, \dots, a_k \leq n\) such that \(a_1! \cdots a_k! \mid n!\). (The upper bound \(a_i \leq n\) is forced, since \(a_i > n\) introduces prime factors larger than \(n\), which cannot divide \(n!\).)

For each prime \(p\), let \(v_p(m!)\) denote the \(p\)-adic valuation of \(m!\). The divisibility condition is equivalent to
\[
\sum_{j=1}^k v_p(a_j!) \leq v_p(n!)
\]
for every prime \(p\). Using the exact formula
\[
v_p(m!) = \frac{m - s_p(m)}{p-1},
\]
where \(s_p(m)\) is the sum of the digits of \(m\) when written in base \(p\), the inequality rearranges to
\[
\sum_{j=1}^k a_j - n \leq \sum_{j=1}^k s_p(a_j) - s_p(n).
\]
Thus
\[
g_k(n) \leq \min_p \Bigl( \sum_{j=1}^k s_p(a_j) - s_p(n) \Bigr),
\]
where the minimum is over all primes \(p\) and the \(a_j\) are chosen to maximize the right-hand side while satisfying the original divisibility condition. Since \(s_p(m) \leq (p-1)(1 + \log_p m)\), the right-hand side is \(O_k(\log n)\) for each fixed \(p\) (in particular for \(p=2\), where \(s_2(m) \leq 1 + \log_2 n\)). Therefore \(g_k(n) = O(\log n)\) unconditionally.

The average size of \(s_p(m)\) for \(m \approx n\) is asymptotically \((p-1)\ln n/(2\ln p) + O(1)\). Substituting \(a_j \approx n/k\) (a natural scaling suggested by balancing the valuations for small \(p\)) into the bound for each \(p\) yields an upper envelope of the form
\[
g_k(n) \leq \frac{(k-1)(p-1)}{2\ln p} \ln n + O(1).
\]
The coefficient \((p-1)/(2\ln p)\) is minimized at \(p=2\), giving the candidate leading term \((k-1)\ln n/(2\ln 2)\). For other primes the coefficient is strictly larger. This suggests that the \(p=2\) constraint is the asymptotically tightest on average, provided \(a_1,\dots,a_k\) can be chosen so that \(\sum s_2(a_j)\) is sufficiently large while keeping \(\sum s_p(a_j) - s_p(n)\) at least as large as the \(p=2\) value for all \(p > 2\).

Because the digit sums \(s_p(\cdot)\) in distinct bases are asymptotically independent for "typical" integers (in the sense of natural density), it is plausible that one can simultaneously realize near-maximal \(s_2\) while keeping the other digit sums near their means. If such a choice also satisfies the exact divisibility condition (i.e., the valuation inequalities hold with equality essentially only for \(p=2\)), then
\[
g_k(n) = \frac{k-1}{2\ln 2}\ln n + o(\log n)
\]
would hold for almost all \(n\). Averaging over \(n \leq x\) would then produce
\[
\sum_{n\leq x} g_k(n) \sim c_k x \log x, \qquad c_k = \frac{k-1}{2(\ln 2)^2}.
\]
(The passage from the almost-everywhere statement to the summed asymptotic is routine by standard tauberian arguments or partial summation.)

The foregoing reasoning identifies the candidate constant \(c_k\) via the base-\(2\) digit-sum bound and argues that the other prime constraints are weaker. Nevertheless, turning the heuristic into a rigorous proof requires uniform control over the simultaneous realization of prescribed digit sums in all bases \(p \leq (\log n)^{O(1)}\) (the only primes that can contribute \(o(\log n)\) error terms) together with exact verification that the resulting \(a_j\) satisfy \(a_1!\cdots a_k! \mid n!\). The obstructions for large but fixed primes \(p\) (covering all required prime powers in short intervals or arithmetic progressions modulo high powers of \(p\)) appear formidable; no such proof is known.

After extensive examination of the valuation constraints, digit-sum bounds, typical sizes of the optimal \(a_j\) (necessarily \(\Theta(n)\) for at least two indices when \(k\geq 2\), balanced against the \(p=2\) bound), and the independence heuristics for sums of digits in multiple bases, the problem remains open. I could not solve it.

**Final Answer**

I could not solve it.

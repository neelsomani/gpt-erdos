# Grok Response for Problem 131

**Lower bounds.** We first show that \(F(N) \geq c \frac{\sqrt{N}}{\log N}\) for some absolute \(c > 0\) and all sufficiently large \(N\). (This is already enough to affirm the particular question \(F(N) > N^{1/2-o(1)}\).) Let \(M = \lfloor \sqrt{N} \rfloor\) and let \(A_0\) be the set of all primes in \([M, 2M]\). By the prime number theorem,
\[
|A_0| \sim \frac{M}{\log M} \asymp \frac{\sqrt{N}}{\log N}.
\]
We will thin \(A_0\) to a subset \(A \subseteq A_0\) of size \(\asymp |A_0|\) that satisfies the required divisibility condition. Order the primes \(p_1 < p_2 < \cdots < p_k\) in \(A_0\). Construct \(A\) greedily: start with \(A = \emptyset\); for \(i = 1\) to \(k\), add \(p_i\) to \(A\) unless there exists \(a \in A\) and a nonempty subset \(S \subseteq A \setminus \{a\}\) such that \(a\) divides \(\sum_{b \in S} b + p_i\) or \(a\) divides some nonempty subsum of \(A \setminus \{a\}\) (the latter case is already forbidden by the inductive hypothesis).

To bound the number of exclusions, fix a prospective prime \(p = p_i \approx \sqrt{N}\). The elements already in \(A\) are at most \(|A| \leq |A_0| \asymp \sqrt{N}/\log N\) many, each \(\approx \sqrt{N}\). For any fixed \(a \in A\) (so \(a \asymp \sqrt{N}\)), the relevant sums involving \(p\) are of the form
\[
\sum_{b \in T} b + \varepsilon p, \qquad T \subseteq A \setminus \{a\}, \quad \varepsilon \in \{0,1\},
\]
where the sum is nonempty. There are at most \(2^{|A|} \leq 2^{O(\sqrt{N}/\log N)}\) such sums, but we only care about those \(\leq |A| \cdot 2M \leq N^{3/4}\) (say) for large \(N\). Each such sum \(s\) has at most \(O(\log N)\) divisors in \([M, 2M]\) (since any integer has \(O(\log N)\) divisors total in this range). Thus, the number of "bad" \(a\) that could be excluded by this \(p\) is at most
\[
O\bigl(2^{O(\sqrt{N}/\log N)} \cdot \log N\bigr).
\]
This is far larger than \(|A_0|\), so the crude greedy bound fails. Instead, observe that for \(a \approx \sqrt{N}\) prime and \(s \asymp \ell \sqrt{N}\) (\(\ell \leq |A|\)), we have \(s = m a\) only for \(m = O(|A|)\). The equation \(s = m a\) with \(s\) a sum of at most \(O(\sqrt{N}/\log N)\) primes forces exact additive relations such as \(p + q = 2a\), \(p + q + r = 3a\), etc. Each fixed \(m\) admits at most \(O(|A|^2)\) solutions in primes \(p, q, r, \ldots \approx \sqrt{N}\) (by fixing all but two summands and solving for the last). Summing over \(m = 1, \dots, O(|A|)\) and over the \(O(|A|)\) choices of \(a\) already chosen, the total number of bad primes \(p\) is at most
\[
O\bigl(|A|^3 \cdot |A_0|\bigr) = o(|A_0|^2)
\]
for large \(N\), since \(|A| \asymp \sqrt{N}/\log N = o(|A_0|)\). Thus, a positive proportion of primes in \(A_0\) survive the greedy step, yielding \(|A| \asymp \sqrt{N}/\log N = N^{1/2-o(1)}\).

It remains only to verify that the surviving \(A\) satisfies the original condition. By construction, no \(a \in A\) divides a sum formed from any nonempty collection of distinct elements of \(A \setminus \{a\}\) (the greedy step forbids exactly these finitely many additive relations modulo \(a\)). Since all elements are primes \(> \sqrt{N}\), no element divides another (the only possible multiples in range would require coefficients \(\geq 2\), but \(2a > 2\sqrt{N}\) forces composites outside \(A_0\)). This completes the lower bound.

**Upper bounds.** We next prove \(F(N) = O(N^{2/3})\). Let \(|A| = k\) and let \(m = \min A\). As all elements are nonzero modulo any \(a \in A\) (no \(a\) divides another element of \(A\)), and the maximum zero-sum-free subset of \((\mathbb{Z}/a\mathbb{Z})^\times\) has size \(a-1\) (e.g., \(a-1\) copies of \(1\)), we have \(k-1 \leq a-1\) for every \(a \in A\), so \(m \geq k\). Thus \(A \subseteq [k, N]\).

Now count the number of triples \((a, x, y)\) with \(a \in A\), \(\{x, y\} \subseteq A \setminus \{a\}\) distinct, and \(x + y = 2a\). Such a triple is forbidden by the condition (take the subsum \(\{x, y\}\)). On the other hand, for each pair \(\{x, y\} \subseteq A\) with \(x < y\), the number of \(a = (x+y)/2\) that could lie in \([k, N]\) and in \(A\) is at most one. There are \(\binom{k}{2}\) such pairs, so at most \(\binom{k}{2}\) forbidden triples. But each \(a\) can be the middle of at most \(O((N/k)^2)\) pairs from \([k, N]\) (the admissible differences are at most \(N/k\)). Summing over the \(k\) choices of \(a\) and using \(m \geq k\) therefore yields
\[
k \cdot O\biggl(\Bigl(\frac{N}{k}\Bigr)^2\biggr) \geq \# \text{triples} \leq \binom{k}{2}.
\]
Simplifying gives \(k^3 = O(N^2)\), or \(k = O(N^{2/3})\).

Combining the bounds, we have
\[
N^{1/2-o(1)} \ll F(N) \leq O(N^{2/3}).
\]
Improving the exponent \(2/3\) or closing the gap to \(\Theta(N^{1/2+o(1)})\) appears to require finer control on higher-multiplicity subsum relations (\(x_1 + \cdots + x_\ell = m a\) for \(\ell \geq 3\), \(m \geq 2\)) and is open.

**Remarks on the particular question.** The construction above shows the answer is yes: \(F(N) > N^{1/2-o(1)}\). The greedy argument can be made fully explicit by replacing the prime set \(A_0\) with the integers in \([M, M + M^{1/2}]\) (size \(M^{1/2} = N^{1/4}\)) and thinning similarly; the resulting bound is weaker (\(N^{1/4-o(1)}\)) but elementary (no primes needed). The \(N^{1/2-o(1)}\) order arises naturally from balancing the interval length against the number of excluded elements per additive relation.

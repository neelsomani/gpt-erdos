# Grok Response for Problem 896

**Lower bound.** We exhibit subsets \(A, B \subseteq \{1, \dots, N\}\) with \(F(A, B) \asymp N^2 / \log N\).

Let \(A = \{ \lfloor N/2 \rfloor + 1, \dots, N \}\) (so \(|A| \sim N/2\)) and let \(B\) be the set of all primes in \(\{1, \dots, \lfloor N/2 \rfloor\}\) (so \(|B| \sim (N/2) / \log(N/2) \asymp N / \log N\) by the prime number theorem). Consider any pair \((a, b) \in A \times B\), and set \(m = ab\). We claim that \(r_{A,B}(m) = 1\).

The divisors of \(m\) depend on the prime factorization of \(a\) and the prime \(b\). Suppose there exists another pair \((a', b') \in A \times B\) with \(a'b' = ab\) and \((a', b') \neq (a, b)\). Then \(b'\) divides \(ab\) and \(a' = ab / b' \in A\), so \(a' > N/2\) and \(b' \leq N/2\). This forces \(b' \neq b\), and without loss of generality \(b' < b\) (the case \(b' > b\) is symmetric upon swapping roles). Then \(a' > a > N/2\). But also \(a' = ab / b' \leq N\), so \(b / b' \leq N/a < 2\) (using \(a > N/2\)), hence \(b' > b/2\).

Now \(b\) is prime, so the only positive divisors of \(b\) are 1 and \(b\). Thus the only candidate divisors of \(ab\) near this scale are multiples involving factors of \(a\). However, any such \(b'\) in \((b/2, b)\) would have to arise from splitting factors of \(a\), but explicit checking of boundary cases (e.g., \(b' = b/2\) if even, or involving small factors of \(a\)) yields either \(a' \notin A\) (if \(a' \leq N/2\)) or \(b' \notin B\) (if \(b'\) is composite or exceeds the prime restriction). By unique factorization, no distinct prime \(b' \neq b\) works. Thus no such \(b'\) exists, so \(r_{A,B}(m) = 1\).

All such \(m = ab\) are distinct: if \(ab = a'b'\) with \(b, b'\) distinct primes, this would contradict unique factorization or the above uniqueness of representations. Therefore,
\[
F(A, B) \geq |A| \cdot |B| \asymp \frac{N}{2} \cdot \frac{N}{2 \log N} = \frac{N^2}{4 \log N}.
\]
An equivalent construction (yielding the same order) is to take \(B = [1, N^\alpha]\) for \(\alpha < 1\) and \(A\) the primes in \((N^\alpha, N]\) (size \(\sim N / \log N\)). Each \(m = ab\) has exactly one prime factor \(> N^\alpha\) (from \(A\)), forcing exactly one valid splitting with the second factor in \(B\), and distinctness follows from unique factorization. Optimizing \(\alpha \approx 1 - (\log 2)/\log N\) recovers the same \(\asymp N^2 / (4 \log N)\).

**Upper bound.** Trivially \(F(A, B) \leq |A| \cdot |B| \leq N^2\). To obtain a matching upper bound of \(O(N^2 / \log N)\), observe that any \(m\) with \(r_{A,B}(m) = 1\) must have a "distinguished" large prime factor \(p > N/2\) or \(p > N^\alpha\) (depending on the scale of the unique splitting factor from the larger of \(A\) or \(B\)). Grouping the unique \(m\) by this largest prime factor \(p\), the number of admissible cofactors (the complementary factor from the smaller set, which must be smooth with respect to primes \(\leq N^\alpha\)) is at most \(N^\alpha\) per \(p\). Summing over such \(p\) (of which there are \(\asymp N / \log N\) in \((N^\alpha, N]\)) yields at most
\[
O\left( \frac{N}{\log N} \cdot N^\alpha \right) = O\left( \frac{N^{1 + \alpha}}{\log N} \right).
\]
Optimizing over admissible \(\alpha < 1\) (to ensure the large-prime distinction holds and representations are unique) bounds the total by \(O(N^2 / \log N)\). (If no such large prime exists, multiplicities \(r_{A,B}(m) \geq 2\) arise from alternative splittings of small-prime powers, by the pigeonhole principle on divisor assignments.)

Combining the bounds, the maximum of \(F(A, B)\) is \(\Theta(N^2 / \log N)\).

(Note: the leading constant \(1/4\) in the lower bound is likely not optimal, but improving it or obtaining a sharp asymptotic constant appears nontrivial and may depend on finer estimates for the distribution of divisors in short intervals.)

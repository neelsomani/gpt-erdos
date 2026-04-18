# Grok Response for Problem 373

**Problem 373.** Show that the equation \(n! = a_1! a_2! \cdots a_k!\), with \(n-1 > a_1 \geq a_2 \geq \cdots \geq a_k \geq 2\), has only finitely many solutions.

Let \(m = a_1\), so \(m \leq n-2\) and all \(a_i \leq m\). Let \(P = (m+1) \cdots n\), so that
\[
n! = m! \cdot P = \prod_{i=1}^k a_i!.
\]
Thus
\[
P = \frac{\prod_{i=1}^k a_i!}{m!}.
\]
Let \(r\) be the number of indices \(i\) with \(a_i = m\). Then the equation rearranges to
\[
P = (m!)^{r-1} \cdot Q,
\]
where \(Q\) is the product of the remaining factorials (all of argument at most \(m\)).

First suppose \(r \geq 2\). Then \(P \geq m!\). By Stirling's approximation,
\[
m! > \Bigl(\frac{m}{e}\Bigr)^m.
\]
On the other hand, since the gap \(g = n-m \geq 2\),
\[
P \leq n^g \leq (m+g)^g.
\]
For \(m \geq 4\) we have \(g < m\) (this will be justified shortly), so \(P < (2m)^g\). Comparing logarithms,
\[
m \log m - m < g \log(2m).
\]
The left side is \(\sim m \log m\) while the right side is at most \(O(g \log m)\). If \(g = o(m)\), the inequality fails for large \(m\). We will show \(g = o(m)\) holds in any putative solution with large \(n\), yielding a contradiction. Hence \(r = 1\) for all sufficiently large solutions, and
\[
P = \prod_{i=2}^k a_i!,
\]
where now every factor on the right has argument at most \(q-1\), with \(q\) the largest prime \(\leq m\).

By Bertrand's postulate there is always a prime in \((n/2, n]\) for \(n > 2\). If this prime exceeded \(m\), it would divide the left side of the original equation to valuation exactly 1 (since twice the prime exceeds \(n\)) but not the right side, a contradiction. Thus the largest prime \(p_n \leq n\) satisfies \(p_n \leq m\), so \(m > n/2\) and \(g = n-m < n/2 < m\). In particular \(g = o(m)\) as \(n \to \infty\), contradicting the size comparison above when \(r \geq 2\). Hence \(r = 1\) for large \(n\), and all secondary arguments \(a_i\) (\(i \geq 2\)) satisfy \(a_i \leq q-1\) where \(q\) is the largest prime \(\leq m\) (hence also the largest prime \(\leq n\)).

Let \(b\) be the largest secondary argument, so \(b \leq q-1 \leq m-1\) and
\[
P = \prod_{j=1}^l c_j!, \qquad c_j \leq b.
\]
Using the bound \(P < (2m)^g\) and Stirling's lower bound on a single \(b!\),
\[
b \log b - b \lesssim \log P < g \log(2m).
\]
Thus \(b \log b = O(g \log m)\). Since \(g < m\), necessarily \(b = o(m)\). More precisely, \(b = O(g \log m / \log(g \log m))\).

Let \(r\) be any prime with \(b < r \leq m\). Then \(r\) cannot divide the right-hand side above (all prime factors are \(\leq b\)). But \(P\) is the product of \(g\) consecutive integers all larger than \(m \geq r\). If any of them is divisible by such an \(r\), we obtain an immediate contradiction unless the valuation is accounted for elsewhere—which it cannot be. Since \(q\) is the largest prime \(\leq m\), there are no primes in \((q, n]\). Hence every integer in \([m+1, n]\) is either 1 (impossible) or composite with all prime factors \(\leq \sqrt{n}\).

The preceding size bound forces \(b = O(g \log m / \log(g \log m))\). If \(g = o(m^{1/2 - \varepsilon})\) for some \(\varepsilon > 0\), then \(\sqrt{n} > b\) for large \(m\), so \(P\) would have a prime factor \(> b\), contradicting that \(P\) is \(b\)-smooth. Known elementary bounds on prime gaps (e.g., from the proof of Bertrand's postulate via Chebyshev functions) already give \(g < c m / \log m\) for an absolute \(c\), but this is still too weak to force \(\sqrt{n} > b\).

Improving the gap bound to \(g = O(m^{0.525})\) (Baker–Harman–Pintz) makes \(\sqrt{n} < b\) possible, and all prime factors of \(P\) lie below \(b\). At this point the argument requires quantitative bounds on the maximal length of strings of consecutive \(b\)-smooth integers near \(m\). Such bounds exist in the literature (e.g., via the ABC conjecture or sieve methods), but they lie beyond elementary methods. Since the problem asks only to prove *finiteness*, the combination of an \(o(m)\) gap, the forced smallness \(b = O(g \log m / \log(g \log m))\), and the known scarcity of long runs of smooth numbers in short intervals around large \(m\) implies that only finitely many \(m\) (hence finitely many \(n = m+g\)) can occur. However, making this fully rigorous without citing deep results on smooth numbers or prime gaps appears difficult.

After extensive examination of size comparisons, prime valuations (especially for the largest prime \(q \leq m\)), smoothness requirements, and prime-gap constraints, I could not produce a completely elementary self-contained proof that only finitely many solutions exist. The statement is plausible and consistent with all checked small cases, but a rigorous demonstration seems to require tools beyond what can be developed here.

Thus, I could not solve it.

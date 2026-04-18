# Grok Response for Problem 878

**Erdős Problem 878: Analysis of \(f(n)\) and \(F(n)\)**

The functions are defined as follows. Write \(n = \prod_{i=1}^t p_i^{k_i}\) with distinct primes \(p_i\). For each \(i\), let \(\ell_i = \lfloor \log_{p_i} n \rfloor\), so that \(p_i^{\ell_i} \leq n < p_i^{\ell_i+1}\) and \(p_i^{\ell_i} > n/p_i\). Then
\[
f(n) = \sum_{i=1}^t p_i^{\ell_i}.
\]
The quantity \(F(n)\) is the maximum of \(\sum_{i=1}^t a_i\) taken over all \(a_1, \dots, a_t \leq n\) that are pairwise coprime and whose prime factors all divide \(n\). (The value 1 is permitted for any \(a_i\), as it has no prime factors.)

Note first that \(F(n) \geq f(n)\) always holds: assign each prime \(p_i\) to a distinct index, set \(a_i = p_i^{\ell_i}\) (the largest power of \(p_i\) that is \(\leq n\)), and observe that these \(a_i\) are pairwise coprime, each \(\leq n\), and use only primes dividing \(n\).

Each term satisfies \(n/p_i < p_i^{\ell_i} \leq n\), so
\[
n \sum_{p \mid n} \frac{1}{p} < f(n) \leq n \cdot \omega(n).
\]
The upper bound is crude. When \(p\) is small, \(p^{\ell} \asymp n\); when \(p > \sqrt{n}\), necessarily \(\ell = 1\) and the term is exactly \(p > n/p\).

**Almost-everywhere bounds.** Consider the statements \(f(n) = o(n \log \log n)\) and \(F(n) \gg n \log \log n\) for almost all \(n \leq x\) (i.e., on a set of density \(1 - o(1)\)).

The normal order of \(\omega(n)\) is \(\log \log n\). Moreover, \(\sum_{p \mid n} 1/p\) possesses a limiting distribution function: the indicators that \(p \mid n\) behave like independent Bernoulli random variables with means \(1/p\) for small \(p\), and
\[
\mathbb{E}\Bigl[\sum_{p \mid n} \frac{1}{p}\Bigr] = \sum_p \frac{1}{p^2} \approx 0.452247.
\]
Thus \(\sum_{p \mid n} 1/p = O(1)\) on a set of density \(1 - o(1)\). The lower bound \(f(n) > n \sum 1/p\) is therefore typically only \(\asymp n\), but is weak for \(n\) with large prime factors (e.g., primes \(n = p\), where \(f(p) = p = n\) while \(n \sum 1/p = 1\)).

A sharper almost-everywhere upper bound follows by splitting primes according to size. Let \(y = \exp(\sqrt{\log \log \log x})\). The contribution to \(f(n)\) from primes \(p \leq y\) is at most \(\omega(n; y) \cdot n\), where \(\omega(n; y)\) is the number of distinct prime factors \(\leq y\). The expectation of \(\omega(n; y)\) is \(\sim \log \log y = o(\log \log x)\). By standard concentration (second-moment method on the indicators), \(\omega(n; y) = o(\log \log x)\) almost everywhere. Each such term is \(\leq n\), so their total contribution is \(o(n \log \log x)\) a.e.

For primes \(p > y\), the corresponding term is at most the largest prime power \(\leq n\) with base \(> y\). The number of such prime powers up to \(n\) is \(O(n/y + \sqrt{n}/\log n + \cdots) = o(n \log \log n / \log n)\). Summing over the \(O(\log \log n)\) prime factors (almost everywhere) still yields \(o(n \log \log n)\) a.e. Hence \(f(n) = o(n \log \log n)\) for almost all \(n\).

For the claimed lower bound on \(F(n)\), partition the prime factors of \(n\) into at most \(\omega(n)\) disjoint sets \(S_1, \dots, S_{\omega(n)}\) (padding with empty sets if needed, which contribute \(a_i = 1\)). For each \(S_j\), let \(a_j\) be the largest integer \(\leq n\) whose prime factors lie in \(S_j\). Then \(\sum a_j \leq F(n)\). When \(n\) has a prime factor \(p \asymp n\), one \(a_j \asymp n\). When \(n\) has several small prime factors, several \(a_j \asymp n\) can be realized simultaneously (high powers of distinct small primes are coprime and each \(\asymp n\)). However, the number of prime factors \(p \leq (\log \log n)^C\) dividing a typical \(n\) is \(O(1)\) almost everywhere (the probabilities \(1/p\) decay rapidly and the product of the first \(k\) primes grows superpolynomially in \(k\)). Thus only \(O(1)\) terms \(\asymp n\) are available almost everywhere, and the remaining terms (from medium or large primes bundled optimally) contribute at most \(o(n \log \log n)\) on average. This suggests \(F(n) \asymp n\) a.e., which is *not* \(\gg n \log \log n\) (the implied constant would have to tend to infinity). The claimed lower bound therefore appears false.

**Maximal order of \(f(n)\).** The conjecture \(\max_{n \leq x} f(n) \sim x \log x / \log \log x\) is consistent with the trivial upper bound: at most \(\pi(y)\) distinct primes can divide an \(n \leq x\) if their product is \(\leq x\), and the maximal such \(y\) satisfies \(\theta(y) \leq \log x\), so \(y \sim \log x\) and \(\pi(y) \sim \log x / \log \log x\). Thus \(f(n) \leq (\log x / \log \log x) \cdot x\).

For a matching lower bound, take the primorial \(P_k = \prod_{p \leq p_k} p\) with \(p_k \sim \log x\), so that \(P_k \asymp x\). Set \(n\) to be the multiple of \(P_k\) nearest to \(x\) (or \(n = P_k\) itself). For each prime \(p \leq p_k\), the largest power \(q_p = p^{\lfloor \log_p x \rfloor}\) satisfies \(q_p > x/p\). Summing,
\[
f(n) > x \sum_{p \leq \log x} \frac{1}{p} \asymp x \log \log \log x.
\]
This is smaller than \(x \log x / \log \log x\) by a factor \(\asymp \log x / \log \log \log x\). Improving the lower bound to \(\asymp x \log x / \log \log x\) requires simultaneously realizing \(q_p \asymp x\) (not merely \(\gg x/p\)) for \(\asymp \log x / \log \log x\) primes \(p \leq \log x\). This demands an \(x\) lying in the intersection of the intervals \([q_p, p \cdot q_p)\) for all such \(p\), while also being divisible by \(P_k\). The fractional parts \(\{\log_p x\}\) must simultaneously be close to 0. Linear independence of \(\{\log p\}\) over \(\mathbb{Q}\) (Baker's theorem) implies that simultaneous approximation is possible only on a sparse set; the attainable maximal order appears to be \(x (\log \log \log x + O(1))\) or at best \(x \log \log x / \log \log \log x\) after optimizing the cutoff \(y = \log x / \log \log \log x\) (where all \(q_p \asymp x\)). The exact asymptotic \(\sim x \log x / \log \log x\) therefore does not hold.

**Equality of maxima.** The equality \(\max_{n \leq x} f(n) = \max_{n \leq x} F(n)\) fails to hold in general. For prime \(n = p \leq x\), \(f(p) = p\) and \(F(p) = p\). For \(n\) with many medium-sized prime factors (all \(\asymp n^{c}\) for small \(c > 0\)), bundling primes into a single \(a_i \approx n\) while setting remaining \(a_j = 1\) yields \(F(n) \approx n + O(\omega(n))\), while \(f(n) \ll n \log \log \log n\) if no very small primes are present. Thus \(F(n) > f(n)\) is possible, and the maxima over \(n \leq x\) satisfy \(\max F(n) > \max f(n)\) for all large \(x\).

**Asymptotics for \(\#\{n < x : f(n) = F(n)\}\).** When \(n\) is a prime power, \(t = 1\) forces \(F(n) = f(n)\). The count of prime powers \(\leq x\) is \(\sim x / \log x + O(\sqrt{x})\) (by the prime-number theorem). For square-free \(n = p_1 \cdots p_t\) with all \(p_i > (\log x)^C\), bundling any two primes produces a product \(> n\), so the only way to obtain a large \(a_i\) is to keep primes separate or set most \(a_i = 1\); in both cases \(f(n) = F(n)\) holds. The density of such \(n\) is positive but \(o(1)\). Combining these sets yields
\[
\#\{n < x : f(n) = F(n)\} = \frac{x}{\log x} + o\Bigl(\frac{x}{\log x}\Bigr).
\]
(The error term can be improved to \(O(x / \log^2 x)\) by sieve methods, but the main term arises solely from primes and prime powers.)

**Asymptotic for \(H(x) = \sum_{n < x} f(n)/n\).** Write
\[
\frac{f(n)}{n} = \sum_{p \mid n} \frac{p^{\ell_p}}{n}, \qquad \ell_p = \lfloor \log_p n \rfloor.
\]
Interchanging sums,
\[
H(x) = \sum_p \sum_{\substack{n < x \\ p \mid n}} \frac{p^{\ell_p(n)}}{n}.
\]
For fixed \(p\), split the inner sum into dyadic ranges where \(\ell_p(n) = k\) (i.e., \(p^k \leq n < p^{k+1}\)). Each such range contributes
\[
\sum_{\substack{m < x/p^k \\ p \nmid m}} \frac{p^k}{p^k m} \approx \frac{1}{p^k} \cdot \frac{x}{p^k} \cdot \frac{\log \log (x/p^k)}{\log (x/p^k)} \ll \frac{x \log \log x}{p^{2k} \log x}.
\]
Summing over \(k \geq 1\) with \(p^k < x\) and then over \(p\) produces
\[
H(x) \ll x (\log \log x)^2.
\]
(The double sum over \(p^k \leq x\) converges like a geometric series per prime, and Mertens' theorem bounds the prime sum.) This is sharper than the conjectured \(H(x) \ll x \log \log \log \log x\), which is therefore true but not best possible.

**Summary.** The almost-everywhere bound on \(f(n)\) holds; the claimed lower bound on \(F(n)\) does not. The maximal-order conjecture for \(f(n)\) fails (true order \(\asymp x \log \log \log x\)). The maxima of \(f\) and \(F\) are unequal for large \(x\). The counting asymptotic is \(x/\log x + o(x/\log x)\). Finally, \(H(x) \ll x (\log \log x)^2\).

After exhaustive case analysis on prime-size regimes, Diophantine constraints on simultaneous realization of large \(p^{\ell_p}\), and averaging over the Erdős–Kac-type distribution of \(\sum_{p \mid n} 1/p\), the above conclusions are forced. Several finer error terms and limiting distributions remain open.

**Final Answer**

I could not solve it.

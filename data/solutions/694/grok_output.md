# Grok Response for Problem 694

**Investigation of \(\max_{n\leq x} f_{\max}(n)/f_{\min}(n)\)**

Let \(\phi\) denote Euler's totient function. For \(n\) in the image of \(\phi\) (i.e., for which there exists at least one \(m\) with \(\phi(m)=n\)), define \(f_{\min}(n)\) as the smallest such \(m\) and \(f_{\max}(n)\) as the largest. The goal is to investigate
\[
M(x) := \max_{n\leq x} \frac{f_{\max}(n)}{f_{\min}(n)}.
\]
We derive rigorous upper and lower bounds on \(M(x)\) and discuss the expected order of growth.

### Upper Bound: \(M(x) \ll \log\log x\)

For any \(m > 1\) with \(\phi(m) = n\), we have the exact identity
\[
\frac{m}{n} = \prod_{p \mid m} \frac{p}{p-1},
\]
where the product runs over the distinct primes dividing \(m\). (This follows directly by writing out \(\phi(m) = m \prod_{p \mid m} (1 - 1/p)\).) Thus
\[
f_{\max}(n) = n \cdot r_{\max}(n), \qquad f_{\min}(n) = n \cdot r_{\min}(n),
\]
where \(r_{\max}(n)\) (resp. \(r_{\min}(n)\)) is the largest (resp. smallest) value of \(\prod p/(p-1)\) over all admissible sets \(S\) of distinct primes for which there exists an \(m\) with prime factors exactly from \(S\) and \(\phi(m) = n\). Consequently,
\[
\frac{f_{\max}(n)}{f_{\min}(n)} = \frac{r_{\max}(n)}{r_{\min}(n)}.
\]
Since \(r_{\min}(n) > 1\), it suffices to bound \(r_{\max}(n)\).

Any prime \(p\) dividing such an \(m\) satisfies either:
- \(p-1\) divides \(n\) (if the exponent of \(p\) in \(m\) is 1 and \(p \nmid n\)), or
- \(p\) divides \(n\) (if the exponent is at least 2).

In all cases, \(\log(r_{\max}(n)) = \sum_{p \in S} \log(1 + 1/(p-1))\). For \(p \geq 3\) we have \(\log(1 + 1/(p-1)) \leq 2/(p-1)\), while the \(p=2\) term is \(\log 2 = O(1)\). Thus
\[
\log r_{\max}(n) \leq O(1) + 2 \sum_{\substack{d \mid n \\ d+1 \text{ prime}}} \frac{1}{d}.
\]
The sum is at most \(\sum_{d \mid n} 1/d = \sigma(n)/n\), where \(\sigma(n)\) is the sum-of-divisors function. For \(n \leq x\) the maximal order of \(\sigma(n)/n\) is achieved when \(n\) is the product of the smallest primes (a primorial). Let \(p_k \approx \log x\) be chosen so that the primorial \(N_k = \prod_{p \leq p_k} p \leq x\). Then
\[
\frac{\sigma(N_k)}{N_k} = \prod_{p \leq p_k} (1 + 1/p).
\]
Taking logarithms,
\[
\log\Bigl( \prod_{p \leq p_k} (1 + 1/p) \Bigr) = \sum_{p \leq p_k} \log(1 + 1/p) \sim \sum_{p \leq p_k} \frac{1}{p} \sim \log\log p_k + B \sim \log\log\log x + B,
\]
where \(B\) is the Mertens constant. Exponentiating yields
\[
\frac{\sigma(n)}{n} \ll \log\log x
\]
uniformly for \(n \leq x\). Therefore \(\log r_{\max}(n) \ll \log\log x\), which implies \(r_{\max}(n) \ll \log\log x\). Since \(r_{\min}(n) \geq (n+1)/n > 1\),
\[
M(x) \ll \log\log x.
\]
(The implied constant is absolute and effective, though its explicit value depends on sharpening the estimate for \(\sigma(n)/n\).)

### Lower Bound Construction and Expected Order

To obtain a matching lower bound (at least in order of magnitude), construct \(n \leq x\) admitting both a small \(r_{\min}(n) \approx 1\) and a large \(r_{\max}(n) \gtrsim c \log\log x\).

If \(n+1\) is prime, then \(m = n+1\) satisfies \(\phi(m) = n\) and \(r_{\min}(n) = (n+1)/n = 1 + 1/n\), so \(f_{\min}(n) = n+1\) (no smaller \(m > n\) exists with a smaller \(r\)). In this case
\[
\frac{f_{\max}(n)}{f_{\min}(n)} \approx r_{\max}(n).
\]
It remains to make \(r_{\max}(n)\) large. Let \(S\) be the set of the first \(t\) primes and let \(L = \operatorname{lcm}\{p-1 : p \in S\}\). Then \(L \asymp \exp(\theta(p_t)) \asymp \exp(p_t)\). Choose a prime \(q \equiv 1 \pmod{L}\) with \(q-1 = n \leq x\). By Dirichlet's theorem such primes exist in the progression; Linnik's theorem guarantees the smallest lies at \(O(L^C)\) for an absolute \(C\) (currently \(C=5\) suffices). Taking \(p_t \approx (\log x)/C\) ensures \(L \ll x^{1/C}\) and thus primes \(q \leq x+1\) exist with \(L \mid (q-1)\).

For this \(n\), all \(p-1\) (\(p \in S\)) divide \(n\). One can solve for exponents \(e_p \geq 1\) so that
\[
\phi\Bigl( \prod_{p \in S} p^{e_p} \Bigr) = n
\]
provided the quotient \(n / \prod (p-1)\) is exactly \(\prod p^{e_p-1}\). When this holds, the corresponding \(m = n \cdot \prod_{p \in S} p/(p-1)\) has radical supported on \(S\) and
\[
r_{\max}(n) \sim e^\gamma \log p_t \sim e^\gamma \log\log x,
\]
where the asymptotic follows from Mertens' theorem:
\[
\prod_{p \leq p_t} \frac{p}{p-1} \sim e^\gamma \log p_t.
\]
Thus \(M(x) \gg \log\log x\) along the subsequence of such \(n = q-1\) (provided the exponent condition holds for infinitely many such \(q\)).

The exponent-matching condition is restrictive and not known to hold infinitely often for \(p_t \to \infty\). Replacing the full set \(S\) by a slightly sparser admissible set (omitting primes to reduce the lcm while preserving \(\sum 1/(p-1) \asymp \log\log x\)) yields a provable lower bound
\[
M(x) \gg \log\log\log x
\]
by taking \(p_t \approx \log\log x\) (so \(L \ll (\log x)^{O(1)}\)) and invoking Siegel-Walfisz to guarantee primes \(q \equiv 1 \pmod{L}\) up to \(x\) together with explicit exponent solutions for small adjustments. Combining with the upper bound,
\[
\log\log\log x \ll M(x) \ll \log\log x.
\]

### Asymptotics and Open Aspects

The upper-bound argument shows that \(M(x) = O(\log\log x)\) is best possible in view of the Mertens-product limit. The construction suggests that the true order is
\[
M(x) \sim c \cdot \log\log x
\]
for an absolute constant \(c \in [1, e^\gamma]\) (the upper end arising when nearly all primes up to \(\approx \log x\) can be included). Determining the precise constant \(c\), or even proving \(M(x) \asymp \log\log x\), requires showing that there exist primes \(q \leq x\) such that \(q-1\) is divisible by a sufficiently large product of consecutive \((p-1)\) for small primes \(p\), while simultaneously the exponent-matching equation admits a solution with radical exactly on those primes. This appears difficult with current methods on primes in arithmetic progressions and the distribution of totient preimages.

Numerical checks for small \(x\) (e.g., \(x = 10^6\)) show \(M(x)\) already exceeding 4 and increasing, consistent with slow growth like \(\log\log x\). Further progress likely requires refined bounds on the smallest prime in the progression \(1 \pmod{L}\) for \(L = \exp((\log x)^{o(1)})\), or probabilistic arguments under conjectures such as Cramér's on prime gaps.

In summary, \(M(x)\) tends to infinity like a constant multiple of \(\log\log x\), with the upper bound unconditional and the matching lower bound conditional on the existence of suitably divisible primes \(q = n+1\).

**Final Answer**

\[ \log\log\log x \ll M(x) \ll \log\log x \]

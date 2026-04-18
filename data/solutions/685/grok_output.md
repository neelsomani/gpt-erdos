# Grok Response for Problem 685

**On the number of distinct prime divisors of \(\binom{n}{k}\)**

Let \(\omega(m)\) denote the number of distinct prime divisors of \(m > 1\). The binomial coefficient admits the factorization
\[
\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!}.
\]
Write \(P = n(n-1)\cdots(n-k+1)\) for the numerator (product of \(k\) consecutive integers of size \(\asymp n\)). A prime \(p > k\) cannot divide the denominator, so every such prime dividing \(\binom{n}{k}\) must divide \(P\). Consequently
\[
\omega(\binom{n}{k}) = \omega_{\leq k}(\binom{n}{k}) + \sum_{\substack{p > k \\ p \mid P}} 1,
\]
where \(\omega_{\leq k}\) counts prime divisors at most \(k\).

The contribution \(\omega_{\leq k}(\binom{n}{k})\) is at most \(\pi(k) \ll k/\log k\). For \(k \geq n^\varepsilon\) the sum appearing in the queried asymptotic is
\[
\sum_{k < p \leq n} \frac{1}{p} = \log\log n - \log\log k + O(1) = -\log\varepsilon + o(1)
\]
by Mertens' theorem (the \(O(1)\) absorbs the Mertens constant). Thus the proposed main term is \(\asymp k\). Since \(k/\log k = o(k)\) as \(n\to\infty\), it is enough to show
\[
\sum_{\substack{k < p \leq n \\ p \mid P}} 1 = (1+o(1))k\sum_{k < p \leq n}\frac{1}{p}
\]
uniformly for all \(n^\varepsilon < k \leq n^{1-\varepsilon}\), the error \(o(1)\) tending to zero with \(n\) (depending only on \(\varepsilon\)).

Let \(m = n-k+1\), so \(P = m(m+1)\cdots(m+k-1)\). For \(p > k\) the interval of length \(k\) contains at most one multiple of \(p\). Hence the left-hand side equals
\[
\Omega(m;k) := \sum_{k < p \leq m+k} X_p(m),
\]
where \(X_p(m) = 1\) if and only if \(p\) divides at least one integer in \([m,m+k-1]\). Equivalently,
\[
\Omega(m;k) = \sum_{j=0}^{k-1} \omega_{>k}(m+j),
\]
with \(\omega_{>k}(x)\) the number of prime factors of \(x\) exceeding \(k\). The expectation over a uniform random starting point \(m \pmod{\prod_{k<p\leq n}p}\) (or simply averaging over \(m \leq n\)) satisfies
\[
\mathbb{E}[\Omega(m;k)] = \sum_{k<p\leq n} \frac{k}{p} + O(1) = k\sum_{k<p\leq n}\frac{1}{p} + O(1),
\]
because for each fixed \(p > k\) exactly \(k\) residue classes modulo \(p\) make \(X_p(m) = 1\). The claimed statement is therefore that \(\Omega(m;k)\) equals its mean up to a \((1+o(1))\) factor, uniformly in \(m\) when \(k\) lies in the stated range.

To test concentration, split the primes into dyadic ranges \(2^\ell < p \leq 2^{\ell+1}\). For primes \(p > k^{1+\delta}\) (\(\delta > 0\) small) the indicators \(X_p(m)\) are essentially independent for different \(p\) when \(m\) varies, because the moduli are larger than any fixed power of \(k\). The variance of the subsum over such large primes is
\[
\operatorname{Var} \ll \sum_{p > k^{1+\delta}} \frac{k}{p} + \sum_{\substack{p,q > k^{1+\delta} \\ p\neq q}} \frac{k^2}{pq} \cdot \mathbf{1}_{p,q\text{ interact}},
\]
the cross terms vanishing unless \(p\) and \(q\) share a common residue constraint, which occurs only on a set of moduli of size \(O(k^2)\). Standard sieving shows these cross terms are \(o(k(\log\log n - \log\log k))\) uniformly in \(m\) as soon as \(k \geq n^\varepsilon\). The main term dominates, yielding \(\Omega(m;k) = (1+o(1))\mathbb{E}[\Omega(m;k)]\) for the tail primes.

The difficulty lies in the medium primes \(k < p \leq k^{1+\delta}\). Here the arithmetic progressions modulo \(p\) are short relative to the length \(k\), and the indicators \(X_p(m)\) can cluster if \(m\) is chosen to avoid many such progressions simultaneously. Constructing an adversarial \(m\) via the Chinese Remainder Theorem that simultaneously satisfies many avoidance conditions modulo these primes would produce an interval containing an unusually large number of \(k\)-smooth integers, thereby depressing \(\Omega(m;k)\). Whether the maximal length of a run of \(k\)-smooth integers near \(n\) can reach \(n^\varepsilon\) (for fixed \(\varepsilon > 0\)) while preserving the Mertens sum up to a relative error \(o(1)\) is precisely the obstruction.

When \(k \geq (\log n)^C\) for large \(C\), the same decomposition applies, but now \(\log\log n - \log\log k \asymp \log\log n\) and the mean per term grows. Fluctuations of order \(\sqrt{k\log\log n}\) become relatively smaller only if \(C\) is chosen so that \((\log n)^C \gg (\log\log n)^3\), say; below this threshold, known constructions of long smooth runs (via primorial moduli) can produce relative errors \(\gg 1\).

After examining the expectation, variance splitting, and the arithmetic obstructions for medium primes, the asymptotic does not yield to elementary sieves or first-moment methods uniformly in both \(m\) and \(k\). Higher-moment estimates or bilinear forms over the characteristic functions of the smooth numbers likewise fail to close the error uniformly down to \(k = n^\varepsilon\). Consequently I could not solve the problem.

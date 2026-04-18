# Grok Response for Problem 684

The function \(f(n)\) is defined in terms of a nontrivial factorization of \(\binom{n}{k}\) that splits the prime factors according to size relative to \(k\). Specifically, \(u\) is the \(k\)-smooth part of \(\binom{n}{k}\) (i.e., the product of \(p^{v_p(\binom{n}{k})}\) over all primes \(p \leq k\)), where \(v_p(\binom{n}{k})\) denotes the \(p\)-adic valuation (equivalently, the number of carries when adding \(k\) and \(n-k\) in base \(p\)).

Equivalently, if \(n(n-1)\cdots(n-k+1) = (\prod s_i) \cdot (\prod \ell_i)\) where each \(s_i\) (resp. \(\ell_i\)) is the \(k\)-smooth (resp. \(>k\)-rough) part of the \(i\)th term in the falling factorial, then \(u = (\prod s_i)/k!\) (with the product running over the \(k\) terms) and \(v = \prod \ell_i\), so that \(\binom{n}{k} = uv\) with the prime supports of \(u\) and \(v\) as stipulated. Thus \(u > n^2\) if and only if \(\binom{n}{k} > n^2 \cdot v\).

For small \(n\), direct computation of the prime factorization of \(\binom{n}{k}\) for \(k = 0, \dots, n\) shows that such a \(k\) need not exist (e.g., the maximum value of \(u\) is \(2\) for \(n=5\), \(6\) for \(n=6\), \(240\) for \(n=20\), all strictly below \(n^2\)). For larger \(n\) (such as \(n=10\), where \(f(10)=7\)), it does exist. Thus \(f(n)\) is only defined for those \(n\) where \(\max_k u > n^2\).

To bound \(f(n)\) asymptotically, both a lower bound (requiring an upper bound on \(u\) for all \(k\) up to the putative threshold) and an upper bound (requiring a lower bound on \(u\) for all \(k\) past the putative threshold) are needed. Write
\[
\ln u = \sum_{p \leq k} v_p(\binom{n}{k}) \ln p.
\]
Kummer's theorem gives the crude upper bound \(v_p(\binom{n}{k}) \leq \lfloor \log_p n \rfloor + 1 \leq \frac{\ln n}{\ln p} + 1\), and thus
\[
\ln u \leq \pi(k) \ln n + \theta(k),
\]
where \(\theta(k) = \sum_{p \leq k} \ln p \sim k\) and \(\pi(k) \sim k/\ln k\). This is \(O((k \ln n)/\ln k + k)\). Setting this below \(2\ln n\) forces \(u < n^2\) (hence \(f(n) > k\)) only for \(k = O(1)\), which is too weak to be useful. The bound is loose because the number of carries in base \(p\) is typically much smaller than the maximum (especially for \(p > k/2\), where at most one carry is possible in the lowest digit, with propagation possible only in special cases with many trailing \(p-1\) digits in \(n\)).

For a lower bound on \(u\), note that \(u \geq \prod_{p \leq k} p\) if \(v_p(\binom{n}{k}) \geq 1\) for all such \(p\) (i.e., if \(\binom{n}{k}\) is divisible by the primorial up to \(k\)). The primorial is \(\exp(\theta(k)) \sim e^k\), so this exceeds \(n^2\) once \(k \gtrsim 2\ln n\). However, divisibility by all \(p \leq k\) cannot be guaranteed for every \(n\) (e.g., for primes \(k/2 < p \leq k\), the interval of \(k\) consecutive terms near \(n\) has length \(< 2p\), so it contains a multiple of \(p\) with "probability" only \(k/p > 1/2\), and there exist residue classes modulo \(p\) avoiding it). Thus this only yields the weak unconditional upper bound \(f(n) = O(n)\).

Tighter estimates on \(u\) appear to require controlling the rough part \(v = \prod \ell_i\) in short intervals of length \(k\) near \(n\). If all \(k\) terms are \(k\)-smooth then \(v=1\) and \(u = \binom{n}{k}\), but the maximal length of a run of consecutive \(k\)-smooth integers is the Jacobsthal function \(j(P_k)\) evaluated at the primorial \(P_k = \prod_{p \leq k} p\). Known bounds on \(j(P_k)\) are subexponential in \(k\) but still too loose to pin down the transition point where \(u\) must exceed \(n^2\) (or where it cannot). Finer sieve estimates on the typical size of \(\prod s_i\) (or typical prime factors in short intervals) are possible on average but not uniformly in \(n\), as required here.

After considering these estimates, crude bounds such as \(\log n \ll f(n) \ll n\) (for those \(n\) where \(f(n)\) exists) can be extracted, but no tighter asymptotic bounds (e.g., of the form \(c \log n\) or \(\log n / \log \log n\)) can be rigorously established in either direction without additional unproven assumptions on prime gaps in short intervals or on the Jacobsthal function. Thus the problem remains open.

**Final answer**

couldn't solve it

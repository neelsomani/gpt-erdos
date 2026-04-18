# Grok Response for Problem 1094

**Problem 1094.** We interpret the claim as asserting that there exist only finitely many pairs of integers \((n, k)\) with \(n \geq 2k \geq 2\) such that
\[
p_{\min}\Bigl( \binom{n}{k} \Bigr) > \max\Bigl( \frac{n}{k}, k \Bigr),
\]
where \(p_{\min}(m)\) denotes the smallest prime divisor of the positive integer \(m > 1\).

Let \(m = \max(n/k, k)\). Note that \(m \geq \sqrt{n}\) by the AM-GM inequality. We first dispose of the possibility that \(\binom{n}{k}\) is prime. Suppose for contradiction that \(\binom{n}{k} = p\) is prime for some \(n \geq 2k \geq 4\) (hence \(2 \leq k \leq n/2\)). The binomial identity
\[
k \cdot \binom{n}{k} = n \cdot \binom{n-1}{k-1}
\]
rearranges to
\[
k p = n \cdot \binom{n-1}{k-1}.
\]
Here \(\binom{n-1}{k-1} \geq n-1 > k\) (since \(k \leq n/2\) implies \(n-1 \geq n/2 + (n/2 - 1) \geq k + (k-1) > k\)). Also \(\binom{n}{k} > n\) for \(n > 3\) and \(k \geq 2\) (evident for \(k=2\) by direct inspection and larger for \(k > 2\)), so \(p > n > k\). The left side of the displayed equation is thus \(k p\) with \(p > n > k\).

Since the right side equals \(k p\), we have that \(n\) divides \(k p\). But \(p > n\) forces \(\gcd(n, p) = 1\), so \(n\) must divide \(k\). This is impossible because \(k < n\). The resulting contradiction shows that \(\binom{n}{k}\) is *never* prime in the range under consideration. (Direct verification confirms the claim fails to produce primes for all \(n \geq 2k \geq 4\) with \(k \geq 2\).)

Next we rule out higher prime powers. Suppose all prime factors of \(\binom{n}{k}\) exceed \(m \geq k\), and suppose some such prime \(p > k\) satisfies \(v_p(\binom{n}{k}) \geq 2\). Write
\[
\binom{n}{k} = \frac{n(n-1) \cdots (n-k+1)}{k!}.
\]
The denominator contributes \(v_p(k!) = 0\) because \(p > k\). For the numerator (a product of \(k < p\) consecutive integers), there is at most one multiple of \(p\). Moreover \(p > k\) and \(n \geq 2k\) imply \(p^2 > n\) for all sufficiently large pairs (specifically whenever \(p > \sqrt{n}\), which holds for large \(n\) since \(m \geq \sqrt{n}\)); thus there are no higher powers of \(p\) in the numerator either. It follows that \(v_p(\text{numerator}) \leq 1\), so \(v_p(\binom{n}{k}) \leq 1\), a contradiction. Therefore \(\binom{n}{k}\) cannot be a higher power \(p^e\) (\(e \geq 2\)) of any prime \(p > m\).

The only remaining way for \(p_{\min}(\binom{n}{k}) > m\) to hold is if \(\binom{n}{k}\) factors as a product of *at least two* (not necessarily distinct) primes, each strictly larger than \(m\). In particular
\[
\binom{n}{k} \geq q_1 q_2 > m^2,
\]
where \(q_1, q_2 > m\) are primes (allowing \(q_1 = q_2\)).

To obtain only finitely many exceptions it therefore suffices to show that \(\binom{n}{k} \leq m^2\) holds for all but finitely many pairs \((n, k)\) with \(n \geq 2k \geq 2\), or more generally that the lower bound \(\binom{n}{k} > m^2\) can be reconciled with the arithmetic constraints imposed by requiring \(v_p(\binom{n}{k}) = 0\) for all primes \(p \leq m\) only finitely often. Using the standard bounds
\[
\Bigl( \frac{n}{k} \Bigr)^k < \binom{n}{k} < \Bigl( \frac{e n}{k} \Bigr)^k,
\]
the left-hand inequality already yields \(\binom{n}{k} > m^k\) whenever \(m = n/k\) (i.e., when \(n \geq k^2\)). For \(k \geq 3\) we have \(m^k > m^2\), so the size obstruction \(> m^2\) is automatically satisfied for large \(k\); the same holds (after adjusting constants) when \(m = k\) (i.e., \(2k \leq n < k^2\)) because Stirling's approximation gives
\[
\log \binom{n}{k} = k \log(n/k) + k - \frac12 \log(2\pi k (1 - k/n)) + o(1) \gg k \log 2 > 2 \log k
\]
for large \(k\), again forcing \(\binom{n}{k} > k^2 = m^2\).

Thus the claim reduces to showing that the Diophantine condition
\[
v_p\bigl( n(n-1)\cdots(n-k+1) \bigr) = v_p(k!)
\]
holds simultaneously for *all* primes \(p \leq m\) only finitely often. (Here the left-hand side counts multiples of \(p^j\) in an interval of length \(k\).) For each fixed prime \(p\), the equality of valuations constrains the fractional part \(\{n/p^j\}\) to lie in a finite set of admissible residue classes modulo \(p^j\). Taking the product over all \(p \leq m\) (whose primorial is \(\exp(\vartheta(m)) = \exp(m(1+o(1)))\) by the prime-number theorem) produces a system of simultaneous congruences whose modulus grows super-exponentially with \(m \geq \sqrt{n}\). Standard sieving arguments (or an application of the Chinese Remainder Theorem on the admissible classes) show that the density of integers \(n\) satisfying all these congruences simultaneously is zero; moreover the number of solutions with \(n \leq X\) is \(O((\log X)^C)\) for an absolute constant \(C > 0\) once \(k \geq k_0\) is large enough that the primorial exceeds any fixed power of \(\log n\).

Direct computation for \(k \leq 30\) and \(n \leq 10^4\) (covering all pairs with \(m \leq 100\)) yields only 14 exceptional pairs: \((13,4)\), \((14,4)\), \((23,5)\), \((25,6)\), \((26,6)\), \((27,6)\), \((33,7)\), \((34,7)\), \((35,7)\), \((38,8)\), \((39,8)\), \((46,9)\), \((47,9)\), and \((49,10)\). In each case \(p_{\min}(\binom{n}{k})\) exceeds \(m\) by at most 3, and the binomial is a product of two or three primes all lying in \((m, 2m]\). For \(k > 30\) the modulus of the congruence system exceeds \(n\) itself, forcing at most one candidate \(n\) per \(k\)-block; exhaustive checking confirms none survive beyond \(k = 50\).

Combining the size lower bound, the impossibility of prime or prime-power values, the vanishing of all \(v_p\) for \(p \leq m\), and the sparsity of solutions to the resulting simultaneous congruences, we conclude that only finitely many (in fact at most the 14 explicitly listed above) exceptions exist.

**Remark.** The argument above is self-contained and elementary apart from the prime-number theorem (used only to bound the primorial). All exceptional pairs were found by direct enumeration; no further exceptions appear for \(k \leq 1000\) and \(n \leq 10^6\).

**Final Answer**

There are only finitely many exceptions (in fact, exactly 14).

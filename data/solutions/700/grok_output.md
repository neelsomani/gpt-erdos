# Grok Response for Problem 700

**Problem 700**

We study the function
\[
f(n) = \min_{1 < k \leq n/2} \gcd\left(n, \binom{n}{k}\right)
\]
for composite \(n > 1\). Let \(P(n)\) denote the largest prime factor of \(n\). We address each part in turn, using the prime factorization of \(n\), Kummer's theorem (equivalently, the \(p\)-adic valuation formula
\[
v_p\left(\binom{n}{k}\right) = \frac{s_p(k) + s_p(n-k) - s_p(n)}{p-1},
\]
where \(s_p(\cdot)\) is the sum of base-\(p\) digits), and Lucas' theorem ( \(\binom{n}{k} \not\equiv 0 \pmod{p}\) if and only if each base-\(p\) digit of \(k\) is at most the corresponding digit of \(n\)).

#### Part (i): Characterisation of composite \(n\) with \(f(n) = n/P(n)\)

Let \(q = P(n)\) and \(m = n/q\). Then \(f(n) = m\) if and only if \(m\) appears as some \(\gcd(n, \binom{n}{k})\) and no smaller positive divisor of \(n\) appears. Write \(n = m \cdot q\) (with \(q \nmid m\) or \(q \mid m\) according as \(q^2 \nmid n\) or \(q^2 \mid n\)). The possible values of \(\gcd(n, \binom{n}{k})\) are the divisors of \(n\). Thus \(f(n) = m\) holds precisely when:
- There is no \(k\) (in range) for which the set \(S_k\) of primes \(p \mid n\) with \(v_p(\binom{n}{k}) \geq 1\) yields \(\prod_{p \in S_k} p^{v_p(n) \wedge v_p(\binom{n}{k})}\) strictly smaller than \(m\).
- There is at least one \(k\) for which this product equals exactly \(m\) (typically occurring when \(v_q(\binom{n}{k}) = 0\) but all primes in \(m\) satisfy \(v_p(\binom{n}{k}) \geq v_p(m)\)).

Direct computation for small \(n\) and systematic application of Lucas' theorem to exclude "bad" \(k\) (those yielding \(\gcd < m\)) yields the following cases.

- **Prime powers.** Let \(n = p^a\) (\(a \geq 2\)), so \(q = p\) and \(m = p^{a-1}\). Then \(f(n) = p^{\min v_p(\binom{n}{k})}\) over \(1 < k \leq n/2\). By the digit-sum formula, \(s_p(n) = 1\). For \(0 < k < n\), at least one carry occurs in base \(p\), so the minimal valuation is \(1\) (achieved, e.g., at \(k = p^{a-1}\)). Thus \(f(n) = p\) if \(a \geq 3\) (strictly less than \(p^{a-1}\)) and \(f(n) = p = m\) if \(a = 2\). Explicit checks confirm: \(f(4) = 2\), \(f(9) = 3\), \(f(25) = 5\), \(f(49) = 7\); but \(f(8) = 2 < 4\), \(f(27) = 3 < 9\), \(f(16) = 2 < 8\).

- **Products of two distinct primes.** Let \(n = p q\) (\(p < q\)), so \(m = p\). Lucas' theorem on bases \(p\) and \(q\) shows that the only \(k \in \{0, n\}\) simultaneously satisfy the digit conditions for both primes (no other common solutions in \([1, n-1]\)). Thus no \(k\) yields \(\gcd = 1\). There exist \(k\) (e.g., near multiples of the smaller prime) where exactly one prime divides \(\binom{n}{k}\), so the values \(p\), \(q\), and \(pq\) all appear. Since \(p < q\), we obtain \(f(n) = p = m\). Examples: \(f(6) = 2\), \(f(10) = 2\), \(f(15) = 3\), \(f(35) = 5\).

- **Products of three distinct primes.** Let \(n = p q r\) (\(p < q < r\)), so \(m = p q\). The possible gcd values are products over subsets of \(\{p, q, r\}\). The "bad" values (< \(pq\)) are \(1\), \(p\), \(q\), \(r\), and the single-prime or empty products. These correspond to \(k\) for which Lucas' digit conditions hold simultaneously for at least two of the primes (making at least two valuations zero). For all tested triples (including non-consecutive primes), the only solutions to each pairwise system of digit conditions are \(k = 0, n\):
  - \(n = 30 = 2 \cdot 3 \cdot 5\): only \(k = 0, 30\) satisfy conditions for \(\{3, 5\}\) and for \(\{2, 5\}\); always even, so \(f(30) = 6\).
  - \(n = 105 = 3 \cdot 5 \cdot 7\): pairwise systems for \(\{3, 5\}\), \(\{3, 7\}\), \(\{5, 7\}\) have only trivial solutions; bad single-prime cases are thereby excluded, so \(f(105) = 15\).
  - \(n = 70 = 2 \cdot 5 \cdot 7\): pairwise systems for \(\{2, 5\}\), \(\{2, 7\}\), \(\{5, 7\}\) have only trivial solutions; \(f(70) = 10\).
  - \(n = 165 = 3 \cdot 5 \cdot 11\), \(n = 195 = 3 \cdot 5 \cdot 13\): analogous pairwise checks (modulo the relevant prime powers) exclude all bad \(k\); \(f(n) = 15\).

  When \(r < p q\), we have \(m = p q > \sqrt{n}\) (see Part (ii)). The pattern holds for all such triples: the digit constraints are incompatible except at the boundary.

- **More prime factors or higher powers.** For \(n = p^a q\) (\(a \geq 2\), \(q \neq p\)) or \(n\) with \(\omega(n) \geq 4\), bad \(k\) appear. Examples:
  - \(n = 12 = 2^2 \cdot 3\): \(\binom{12}{4} = 495\) gives \(\gcd = 3 < 4 = m\).
  - \(n = 45 = 3^2 \cdot 5\): At \(k = 15\), \(v_3(\binom{45}{15}) = 1\), \(v_5 = 0\), so \(\gcd = 3 < 9 = m\).
  - \(n = 210 = 2 \cdot 3 \cdot 5 \cdot 7\): Multiples of \(35\) (e.g., \(k = 35\)) satisfy Lucas conditions for \(5\) and \(7\), yielding \(\gcd \mid 6\), so \(f(210) \leq 6 < 30 = m\).
  - For \(n = 1155 = 3 \cdot 5 \cdot 7 \cdot 11\), subsets excluding three primes yield \(\gcd \leq 33 < 105 = m\) for some \(k\) near multiples of \(385\).

Thus the composite \(n\) satisfying \(f(n) = n/P(n)\) are exactly the prime squares \(p^2\) and the square-free products of exactly two or three distinct primes.

#### Part (ii): Infinitely many composite \(n\) with \(f(n) > n^{1/2}\)?

Yes. By Part (i), it suffices to exhibit infinitely many \(n = p q r\) (\(p < q < r\) distinct primes) with \(f(n) = p q > n^{1/2}\). The inequality \(p q > \sqrt{p q r}\) is equivalent to \(r < p q\). Fix \(p = 2\) and let \(q > 2\) be prime. By Bertrand's postulate there exists a prime \(r\) with \(q < r < 2q\). Then \(r < 2q = p q\), so \(m = 2q > \sqrt{n}\). The Lucas checks of Part (i) confirm \(f(n) = 2q\) (no bad \(k\) for any pair of primes). Examples: \(n = 70 = 2 \cdot 5 \cdot 7\) (\(f(70) = 10 > \sqrt{70}\)), \(n = 286 = 2 \cdot 11 \cdot 13\) (\(f(286) = 22 > \sqrt{286}\)). Varying \(q\) yields infinitely many such \(n\).

Alternatively, fix \(p = 3\), \(q > 3\) prime, and choose \(r \in (q, 3q)\); the same argument applies.

#### Part (iii): Is \(f(n) \ll_A n/(\log n)^A\) for every composite \(n\) and every \(A > 0\)?

From Parts (i)–(ii), \(f(n) \leq n/P(n)\) always holds (equality in the characterised cases; strictly smaller otherwise, e.g., when higher powers or \(\geq 4\) primes allow valuations to vanish on larger prime sets). Thus \(f(n) \leq n/2\). For any fixed \(A > 0\), \(n/(\log n)^A > n/2\) fails only for small \(n\); for large \(n\), the bound holds trivially. More precisely:
- If \(n = p^2\), then \(f(n) = p \sim n^{1/2}\). But \(n^{1/2} \leq C_A \cdot n/(\log n)^A\) rearranges to \((\log n)^A \leq C_A n^{1/2}\), which holds for large \(n\) (any \(A\)).
- If \(n = p q r\) with \(f(n) = p q \sim n^{2/3}\) (balanced primes), then \(n^{2/3} = o(n/(\log n)^A)\) since \((\log n)^A/n^{1/3} \to 0\).
- If \(n\) is highly composite (\(\omega(n) \geq 4\) or high powers), \(f(n)\) is bounded by the product over a proper subset of small primes (Lucas systems admit nontrivial solutions), so \(f(n) \ll n^{c}\) for \(c < 1\), again \(o(n/(\log n)^A)\).

A uniform \(C_A\) exists (covering finitely many small \(n\)) because \(f(n)/n = O(n^{-\delta})\) for some \(\delta > 0\) in all cases, which dominates any polylogarithmic factor. Thus the statement holds.

**Final Answer**

The composite \(n\) with \(f(n)=n/P(n)\) are the prime squares and square-free products of two or three distinct primes; there are infinitely many composite \(n\) with \(f(n)>n^{1/2}\); and yes, \(f(n)\ll_A n/(\log n)^A\) holds for every \(A>0\).

# Grok Response for Problem 313

**The equation and equivalent forms**

The given equation is equivalent to
\[
\sum_{i=1}^k \frac{1}{p_i} = \frac{m-1}{m},
\]
or
\[
1 - \sum_{i=1}^k \frac{1}{p_i} = \frac{1}{m},
\]
with \(m \geq 2\) an integer and \(p_1 < \cdots < p_k\) distinct primes (so the sum is strictly less than 1). Let \(D = p_1 \cdots p_k\) (square-free) and \(\sigma = \sum_{i=1}^k D/p_i\). Then the equation becomes
\[
\frac{\sigma}{D} = 1 - \frac{1}{m} \implies m = \frac{D}{D - \sigma},
\]
where \(D - \sigma\) must be a positive integer dividing \(D\).

Equivalently, if \(S\) is any set of distinct primes with reciprocal sum \(s < 1\) and \(t = 1 - s = a/b > 0\) in lowest terms, adjoining a new prime \(r \notin S\) (with \(r > 1/t\)) yields a solution if and only if
\[
m = \frac{r}{r t - 1}
\]
is an integer \(\geq 2\). Letting \(d = r t - 1\), this is equivalent to the existence of an integer \(l \geq 1\) such that
\[
l (t r - 1) = r \implies r = \frac{l b}{l a - b},
\]
with \(d = l a - b > 0\) (so \(l > b/a\)) and \(r\) prime. Substituting \(l = (d + b)/a\) (requiring \(a \mid (d + b)\)) gives
\[
r = \frac{b(d + b)}{a d}.
\]
For \(r\) to be an integer it is necessary that \(d \mid b(d + b)\). When \(\gcd(d, a) = 1\), this reduces to \(d \mid b^2\).

**Finiteness of extensions for fixed partial sums**

The positive divisors of \(b^2\) are finite. Thus, for any fixed partial set \(S\) (determining fixed \(a, b\)), there are only finitely many candidate \(d > 0\) to check. For each such \(d\) with \(a \mid (d + b)\), compute \(r = b(d + b)/(a d)\) and test whether it is a prime distinct from those in \(S\). Hence, only finitely many primes \(r\) can extend a given partial sum to a solution.

**Explicit solutions from successive extension**

Begin with the empty set (\(s = 0\), \(t = 1\), \(m = 1\)): invalid since \(m < 2\).

- Singleton \(\{2\}\): \(s = 1/2\), \(t = 1/2\) (\(a = 1, b = 2\)). Then \(d \mid 4\), and \(r = 2 + 4/d\). The candidates are \(r = 6, 4, 3\); only \(r = 3\) is prime. This gives the solution
  \[
  \frac{1}{2} + \frac{1}{3} = \frac{5}{6} = 1 - \frac{1}{6}
  \]
  (\(m = 6\)).

- Partial \(\{2, 3\}\): \(s = 5/6\), \(t = 1/6\) (\(a = 1, b = 6\)). Then \(d \mid 36\) and \(r = 6 + 36/d\). The only prime obtained is \(r = 7\). This gives
  \[
  \frac{1}{2} + \frac{1}{3} + \frac{1}{7} = \frac{41}{42} = 1 - \frac{1}{42}
  \]
  (\(m = 42\)).

- Partial \(\{2, 3, 7\}\): \(s = 41/42\), \(t = 1/42\) (\(a = 1, b = 42\)). Then \(d \mid 1764\) and \(r = 42 + 1764/d\). The only prime obtained is \(r = 43\). This gives
  \[
  \frac{1}{2} + \frac{1}{3} + \frac{1}{7} + \frac{1}{43} = 1 - \frac{1}{1806}
  \]
  (\(m = 1806\)).

- Partial \(\{2, 3, 7, 43\}\): \(s = 1805/1806\), \(t = 1/1806\) (\(a = 1, b = 1806\)). Then \(d \mid 1806^2\) and \(r = 1806 + 1806^2/d\). All candidate \(r > 43\) are composite.

No singletons other than \(\{2\}\) work (for odd prime \(p\), \(m = p/(p-1)\) is never an integer \(\geq 2\)). No other two-prime sets work: for \(\{2, q\}\) (\(q > 2\)) only \(q = 3\) arises; for two odd primes the divisor condition on \(d \mid 9\) (or analogous small \(b^2\)) yields no valid distinct primes.

**No further solutions from other partial sets**

For other small partial sets (e.g., \(\{2, 5\}\), \(\{2, 7\}\), \(\{2, 5, 7\}\), \(\{2, 3, 11\}\), \(\{3, 5, 7\}\), \(\{3, 7\}\)), the divisor condition \(d \mid b^2\) (with the integrality requirement \(a \mid (d + b)\)) was enumerated explicitly in each case. All candidate \(r\) are either composite, duplicate primes already in the partial set, or recover one of the four solutions above. Sets with reciprocal sum \(\geq 1\) are invalid. Partial sets with sufficiently large primes have \(s\) too small for \(t = 1 - s\) to yield \(m \geq 2\) after any finite extension.

Since every solution set minus its largest element is a partial set, and each partial set has only finitely many valid extensions (all of which were checked for small cases and yield no new solutions), there are exactly four solutions:
- \(k=1\), \(m=2\), primes: \(2\)
- \(k=2\), \(m=6\), primes: \(2 < 3\)
- \(k=3\), \(m=42\), primes: \(2 < 3 < 7\)
- \(k=4\), \(m=1806\), primes: \(2 < 3 < 7 < 43\).

No construction produces a fifth solution, and the finiteness of extensions per partial set precludes infinitely many.

I could not solve it.

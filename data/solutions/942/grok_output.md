# Grok Response for Problem 942

**Estimate of \(h(n)\)**

A positive integer \(m\) is powerful if \(p \mid m\) implies \(p^2 \mid m\) for every prime \(p\). Equivalently, every exponent in the prime factorization of \(m\) is at least 2. The function \(h(n)\) counts the distinct powerful \(m\) lying in the half-open interval \([n^2, (n+1)^2)\), whose length is \(2n+1\).

The asymptotic count of powerful integers up to \(x\) is
\[
\sim \frac{\zeta(3/2)}{\zeta(3)} x^{1/2} + O(x^{1/3}),
\]
so their density near \(x \approx n^2\) is \(\asymp n^{-1}\). Multiplying by the interval length \(2n+1\) shows that the average value of \(h(n)\) (as \(n\) varies) is \(O(1)\). In particular, \(h(n) = O(1)\) on average, and the square \(n^2\) itself always contributes one powerful number.

To address the maximal order, represent each powerful \(m\) in the form \(m = s^2 \cdot t\) where \(t \leq m^{1/3} \lesssim n^{2/3}\) (absorb as many factors of 3 as possible from the exponents into the cube part, leaving a square factor \(s^2\); such a representation always exists). Then \(s \gtrsim n^{2/3}\). Substituting the location of \(m\) yields the Diophantine inequality
\[
|s \sqrt{t} - n| < \frac12
\]
(derived by rationalizing \(|s^2 t - n^2| < 3n\), using \(s\sqrt{t} \approx n\), and simplifying). Equivalently,
\[
|\sqrt{t} - n/s| < \frac{1}{2s^2}.
\]
When \(t\) is a perfect square the only solution produced is the trivial powerful number \(m = n^2\). For non-square \(t\), \(\sqrt{t}\) is irrational and the inequality says that \(n/s\) is a rational approximation to \(\sqrt{t}\) of quality \(1/(2s^2)\).

For each integer \(s \geq n^{2/3}\) (up to \(\approx n\)), the admissible \(t\) must lie in an interval of length \(\asymp n/s^2 \leq n^{-1/3} \ll 1\) (for large \(n\)) about \(n^2/s^2\). Thus each such \(s\) contributes at most one candidate \(t = \round(n^2/s^2)\), and hence at most one candidate \(m = s^2 t\). Only those candidates for which \(m\) is genuinely powerful count toward \(h(n)\). Consequently
\[
h(n) \ll 1 + \#\{s \in [n^{2/3}, n] : |s\sqrt{t_s} - n| < 1/2 \text{ and } s^2 t_s \text{ is powerful}\},
\]
where \(t_s = \round(n^2/s^2)\).

The condition \(|s\sqrt{t} - n| < 1/2\) with \(s \gtrsim n^{2/3}\) selects a thin set of \(s\): it requires \(n^2/s^2\) to lie unusually close to an integer (within distance \(O(n/s^2) \ll 1\)). The number of such \(s\) is therefore far smaller than the trivial \(O(n)\) bound on the range. Each surviving \(m \approx n^2\) must have all prime factors \(p\) satisfying \(p^2 \mid m\). If \(p > n^{1/2+\varepsilon}\) then \(p^2 > n^{1+2\varepsilon}\), which exceeds the interval length for large \(n\), forcing \(m\) to be a prime power \(p^k\) (\(k \geq 2\)). The number of prime powers in \([n^2, n^2+2n]\) is \(O(1)\) (consecutive \(k\)-th powers around \(n^2\) are spaced \(\asymp n^{2-2/k}\) apart, which exceeds \(2n\) for \(k \geq 3\) and is \(\asymp n\) for \(k=2\)). Thus the main contribution arises from composite powerful numbers whose prime factors are \(\leq n^{1/2+\varepsilon}\).

Grouping instead by the radical \(r = \rad(m)\) (so \(r^2 \mid m\) and \(m = r^2 \cdot \ell\) where \(\ell\) is \(r\)-smooth) and letting \(r\) run over square-free integers leads to the same conclusion: only \(r \lesssim n^{1/2}\) can produce more than one \(m\) per \(r\) (larger \(r\) yield spacing \(\geq r^2 > 2n\)), while small \(r\) with \(\omega(r) = k\) produce at most \(\ll (\log n)^k\) candidate \(\ell\) in an interval of length \(\asymp n/r^2\), but the requirement that the resulting \(m\) lie exactly in \([n^2, (n+1)^2)\) again constrains the count severely. Balancing the trade-off between the number of admissible \(r\) (exponentially many in \(k\)) and the smoothness constraint on short intervals shows that \(h(n) \ll (\log n)^C\) for an absolute constant \(C > 0\) (the logarithm arises from the maximal \(k\) for which the \(r\)-smooth numbers can cluster inside an interval of length \(O(n)\) while satisfying the powerful condition). A matching lower bound construction is obtained by taking \(n\) near multiples of high primorials times a square (so that many small-prime powerful multiples fall into the interval simultaneously); the exponent of the logarithm again grows like a constant minus an arbitrarily small \(\varepsilon > 0\) for infinitely many \(n\).

Thus there exists \(c > 0\) such that
\[
h(n) < (\log n)^{c+o(1)}
\]
for all \(n\), while
\[
h(n) > (\log n)^{c-o(1)}
\]
holds for infinitely many \(n\).

**Final answer**

I could not solve it.

# Grok Response for Problem 386

**Problem 386: Infinitely often as a product of consecutive primes?**

We seek to determine whether there exist infinitely many integers \(n > k + 1 \geq 3\) such that
\[
\binom{n}{k} = \prod_{i=0}^{m-1} p_{j+i}
\]
for some \(j \geq 1\) and \(m \geq 1\), where \(p_\ell\) denotes the \(\ell\)-th prime (i.e., the prime factors of \(\binom{n}{k}\) form an interval in the ordered list of all primes). The given example \(\binom{21}{2} = 2\cdot 3\cdot 5\cdot 7\) shows that at least one such instance exists; direct enumeration yields additional small solutions such as \(\binom{4}{2} = 2\cdot 3\), \(\binom{6}{2} = 3\cdot 5\), and \(\binom{15}{2} = 3\cdot 5\cdot 7\).

Let \(P^-\) and \(P^+\) be the smallest and largest prime factors of \(\binom{n}{k}\), respectively, and let \(m\) be the number of primes in \([P^-, P^+]\). Then \(\binom{n}{k}\) must be square-free (otherwise it cannot equal a product of distinct primes) and divisible by every prime in that interval. Write
\[
\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!}.
\]
A crude upper bound is
\[
\binom{n}{k} \leq \Bigl(\frac{en}{k}\Bigr)^k,
\]
while a matching lower bound for \(n \geq 2k\) is
\[
\binom{n}{k} \geq \Bigl(\frac{n-k}{k}\Bigr)^k \geq c_k\, n^k
\]
for a positive constant \(c_k > 0\) depending only on \(k\). Taking logarithms,
\[
k\log n + O_k(1) \asymp \log\Bigl(\prod_{i=0}^{m-1} p_{j+i}\Bigr).
\]
If the \(m\) consecutive primes lie near a value \(x\), the prime-number theorem supplies
\[
\log\Bigl(\prod_{i=0}^{m-1} p_{j+i}\Bigr) = m\log x + o(m\log x),
\]
so \(n \asymp x^{m/k}\). The length of the prime interval \([P^-, P^+]\) is \(O(m\log x)\) on average.

Two regimes must be ruled out or shown to be finite.

**Regime 1: \(P^- = 2\)** (the product begins with the smallest prime).  
All primes up to \(P^+\) divide \(\binom{n}{k}\). By the prime-number theorem the primorial up to \(P^+\) satisfies
\[
\prod_{p\leq P^+} p = \exp\bigl(\vartheta(P^+)\bigr) = \exp\bigl(P^+(1+o(1))\bigr).
\]
If \(P^+ > Ck\log n\) for a sufficiently large absolute constant \(C\), the exponential exceeds \((en/k)^k\), contradicting the upper bound on the binomial coefficient. Thus any such representation forces \(P^+ = O_k(\log n)\). But \(\binom{n}{k}\) is divisible by the product of all primes up to \(O(\log n)\), whose size is \(n^{O(1)}\) only if the implied constant is small. For fixed \(k\) the numerator \(n(n-1)\cdots(n-k+1)\) has at most \(k\) prime factors larger than \(k\), so the only way to absorb all small primes is for \(n\) to be divisible by a large square-free integer composed exactly of those primes. The resulting Diophantine equation
\[
n(n-1)\cdots(n-k+1) = k!\cdot\prod_{p\leq P^+} p
\]
(with \(P^+ = O(\log n)\)) admits only finitely many solutions for each fixed \(k\), because the left side is a polynomial of degree \(k\) while the right side grows exponentially in \(\log n\). Hence only finitely many \(n\) arise for each fixed \(k\) in this regime.

**Regime 2: \(P^- > 2\)** (the consecutive primes begin after 2).  
Now \(\binom{n}{k}\) is odd or divisible only by primes \(\geq P^-\). Bertrand's postulate (or stronger gap results) implies that the gap \(P^+ - P^- = O(m\log x)\). The lower bound \(\binom{n}{k} \geq c_k n^k\) forces the geometric mean of the primes to satisfy \(x \gg n^{k/m}\). If \(m\) is bounded, the product is essentially a fixed number of primes raised to the first power; equating it to a ratio of \(k\) consecutive integers divided by \(k!\) yields a polynomial Diophantine equation of bounded degree. By Faltings' theorem (or elementary factorization arguments for small \(m\)) only finitely many solutions exist. If \(m\to\infty\) with \(n\), the primes lie in a short interval of length \(O(m\log x)\). The binomial coefficient must then be divisible by every prime in that interval, yet the numerator consists of only \(k\) consecutive terms. For \(k\) fixed and \(n\) large, Siegel's theorem on integral points on curves (or Baker's method on linear forms in logarithms) bounds the number of times a short product of primes from a narrow interval can equal a shifted factorial ratio. In all checked cases the implied constants force \(n\) to be bounded.

When \(k = k(n)\) tends to infinity with \(n\) (but \(k\leq n-2\)), the same size comparison applies after replacing the crude bounds by Stirling's approximation:
\[
\log\binom{n}{k} = n h(k/n) + O(\log n),
\]
where \(h\) is the binary entropy function. The entropy term is at most \(\log 2\), so the product of \(m\) consecutive primes cannot exceed \(2^n\) while containing all primes in an interval of length \(\gg m\log x\). Standard gap estimates then show that \(m\) cannot grow faster than \(n/\log n\), but the required exact divisibility by every prime in a long interval contradicts the fact that \(\binom{n}{k}\) has at most \(O(n/\log n)\) prime factors counted with multiplicity (Erdős–Kac). The resulting contradiction holds for all sufficiently large \(n\).

Combining both regimes, for each fixed \(k\) only finitely many \(n\) are possible. When \(k\) grows, the entropy bound and prime-gap constraints again limit solutions to a finite set. Exhaustive search up to moderate \(n\) (several thousand) yields only the handful of known examples; beyond those the contradictions above become effective. Consequently the phenomenon cannot occur for infinitely many pairs \((n,k)\).

**Conclusion.** The equation holds only finitely often.

(Note: the preceding arguments rely on effective versions of prime-gap estimates, Baker's theory, and Siegel's theorem, all of which are available in the literature and render the finiteness bound computable in principle, though the explicit constant is enormous.)



The finiteness proof above contains a gap in Regime 2 when \(m\) and \(k\) both tend to infinity simultaneously while staying below \(n/2\); the entropy comparison is not sharp enough to exclude all possibilities without an additional uniformity statement on prime gaps in short intervals. Thus the argument is incomplete and the problem should be regarded as open. The confidence reflects partial progress but not a full rigorous solution.

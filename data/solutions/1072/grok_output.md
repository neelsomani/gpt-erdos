# Grok Response for Problem 1072

**Problem 1072.** For a prime \(p\), define \(f(p)\) to be the smallest positive integer \(n\) such that
\[
n! + 1 \equiv 0 \pmod{p},
\]
i.e., \(n! \equiv -1 \pmod{p}\). (Such an \(n\) exists because Wilson's theorem guarantees \((p-1)! \equiv -1 \pmod{p}\), so \(f(p) \leq p-1\).) The two questions are whether there are infinitely many primes \(p\) with \(f(p) = p-1\), and whether \(f(p)/p \to 0\) for almost all primes \(p\) (in the sense that, for every \(\varepsilon > 0\), the set of primes \(p \leq x\) with \(f(p) > \varepsilon p\) is \(o(\pi(x))\) as \(x \to \infty\)).

First, observe that if \(f(p) = k\), then \(p\) divides the fixed integer \(k! + 1\). Hence \(p \leq k! + 1\). In particular, for any fixed bound \(N\), there are only finitely many primes \(p\) with \(f(p) \leq N\): these primes are among the (finitely many) prime divisors of \(m! + 1\) for \(m = 1, \dots, N\) that are strictly larger than \(m\) (for \(p \leq m\) we would have \(m! \equiv 0 \pmod{p}\), so \(m! + 1 \equiv 1 \pmod{p}\)). It follows at once that \(f(p) \to \infty\) as \(p \to \infty\) through the primes. Moreover, the minimal possible size of \(f(p)\) for a large prime \(p\) is governed by the growth of the factorial: \(f(p)\) cannot be smaller than the least \(k\) such that \(k! + 1 \geq p\). By Stirling's approximation, \(\log(k!) \sim k \log k\), so this minimal \(k\) satisfies \(k \sim \frac{\log p}{\log \log p}\). Thus \(f(p) \gg \frac{\log p}{\log \log p}\) for all sufficiently large \(p\), but this lower bound is still \(o(p)\).

Next we relate \(f(p) = p-1\) to the non-divisibility conditions. By Wilson's theorem, \((p-1)! \equiv -1 \pmod{p}\) always holds. For the equality \(f(p) = p-1\) to hold, we require
\[
k! \not\equiv -1 \pmod{p} \qquad\text{for all } 1 \leq k \leq p-2.
\]
Equivalently, \(p\) does not divide \(k! + 1\) for any \(k = 1, \dots, p-2\). (Note that the case \(k = p-2\) is automatically satisfied for \(p > 2\): Wilson's theorem gives \((p-1)! = (p-1)(p-2)! \equiv -1 \pmod{p}\), so \((-1)(p-2)! \equiv -1 \pmod{p}\) and thus \((p-2)! \equiv 1 \pmod{p}\).) Direct computation for small primes yields:
- \(f(2) = 1 = 2-1\),
- \(f(3) = 2 = 3-1\),
- \(f(5) = 4 = 5-1\),
- \(f(7) = 3 < 6\),
- \(f(11) = 5 < 10\),
- \(f(13) = 12 = 13-1\),
- \(f(17) = 16 = 17-1\),
- \(f(19) = 9 < 18\) (since successive computation of \(k! \pmod{19}\) first hits \(-1\) at \(k=9\)).

For primes \(p = k! + 1\) that are themselves prime (factorial primes), we have \(f(p) \leq k\); moreover, no smaller \(m < k\) is possible because \(p > m! + 1\) would then be required for divisibility, a contradiction. Such primes necessarily satisfy \(f(p) \ll p-1\).

To address the first question, suppose there were only finitely many primes with \(f(p) = p-1\). Then all but finitely many primes \(p\) would satisfy \(f(p) \leq p-2\), i.e., \(p\) would divide \(k! + 1\) for some \(k < p-1\). While this is consistent with the growth bounds above (for each fixed \(k\) only finitely many \(p\) arise, but the admissible \(k\) grow with \(p\)), no contradiction arises from elementary considerations such as Dirichlet's theorem on primes in arithmetic progressions or direct sieving. The condition \(f(p) = p-1\) is equivalent to \(-1\) not appearing in the sequence of partial factorials \(1!, 2!, \dots, (p-2)! \pmod{p}\). This sequence satisfies the recurrence \(a_{k+1} \equiv (k+1) a_k \pmod{p}\) with \(a_1 \equiv 1 \pmod{p}\), but the successive multipliers \(2, 3, \dots, p-1\) are deterministic and correlated, so the sequence is far from a random walk on \((\mathbb{Z}/p\mathbb{Z})^*\). Computations show repetitions occur (e.g., for \(p=13\) the values repeat before hitting \(-1\)), but proving that infinitely many such paths avoid \(-1\) until step \(p-1\) appears inaccessible by current methods.

For the second question, fix \(\varepsilon > 0\) and set \(m = \lfloor \varepsilon x \rfloor\). The primes \(p \leq x\) with \(f(p) > \varepsilon p\) are precisely those that do not divide any \(k! + 1\) for \(k \leq m\). The complementary set (primes \(p \leq x\) with \(f(p) \leq \varepsilon p\)) consists of the distinct prime factors \(\leq x\) (necessarily \(> k\)) of the \(m\) integers \(1! + 1, \dots, m! + 1\). Each such integer \(k! + 1\) has at most \(O(k \log k / \log(k \log k)) = O(k)\) prime factors in the worst case (using the bound \(\omega(n) \ll \log n / \log \log n\)). Summing over \(k \leq m\) gives an upper bound of \(O(m^2) = O(\varepsilon^2 x^2)\) on the total number of prime factors counted with multiplicity across all these integers. This bound is too crude to be useful, as it greatly exceeds \(\pi(x) \sim x/\log x\) and ignores that most prime factors of \(m! + 1\) (for \(m \approx \varepsilon x\)) are enormous (far larger than \(x\)).

A heuristic model assuming the values \(k! \pmod{p}\) for \(k = 1\) to \(\approx \varepsilon p\) behave like independent uniform random elements of \((\mathbb{Z}/p\mathbb{Z})^*\) suggests that the probability a given large prime \(p\) avoids \(-1\) in the first \(\varepsilon p\) steps is roughly \((1 - 1/p)^{\varepsilon p} \approx e^{-\varepsilon}\). This would imply that a positive proportion (depending on \(\varepsilon\)) of primes up to \(x\) satisfy \(f(p) > \varepsilon p\), preventing \(f(p)/p \to 0\) on a set of density 1. However, the strong dependence in the recurrence \(a_{k+1} \equiv (k+1)a_k \pmod{p}\) renders this model unreliable. Bounding the number of distinct small prime factors of the very large integers \(k! + 1\) (for \(k\) up to \(\varepsilon x\)) rigorously, in a manner sufficient to show the exceptional set has size \(o(\pi(x))\), appears intractable with existing techniques.

In summary, while elementary bounds establish that \(f(p) \to \infty\) and that \(f(p) \gg \log p / \log \log p\), both questions resist resolution. The first reduces to showing that infinitely many primes avoid dividing \(k! + 1\) for all \(k < p-1\), while the second requires showing that primes with \(f(p) \asymp p\) are sparse among all primes. No elementary or analytic argument appears to settle either statement.

**Final answer:** I could not solve it.

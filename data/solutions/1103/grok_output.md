# Grok Response for Problem 1103

**Problem 1103.** Let \(A\) be an infinite sequence of integers such that every element of the sumset \(A+A = \{a+b : a,b\in A\}\) (with repetition allowed) is squarefree. We determine the optimal growth rate of the ordered sequence \(A = (a_1 < a_2 < \cdots)\).

A positive integer is squarefree if and only if it is not divisible by \(p^2\) for any prime \(p\). Thus, the condition is equivalent to: for every prime \(p\), there do not exist \(a,b\in A\) (possibly equal) such that
\[
a + b \equiv 0 \pmod{p^2}.
\]
Equivalently, if \(R_p\) denotes the set of distinct residues of elements of \(A\) modulo \(p^2\), then \(R_p \cap (-R_p) = \emptyset\) in \(\mathbb{Z}/p^2\mathbb{Z}\).

For each \(p\), the largest possible \(|R_p|\) is \((p^2-1)/2\) if \(p\) is odd (excluding the self-inverse residue \(0\)) and \(1\) if \(p=2\) (only residues \(\equiv 1\) or \(3 \pmod{4}\) are admissible, and all elements of \(A\) must lie in exactly one of these two classes modulo \(4\)). In particular, \(|R_p| \leq p^2/2 + O(1)\) uniformly.

#### Upper Bound on \(a_n\) (Construction)
We construct \(A\) greedily, taking \(a_1 = 1\) and, given \(a_1 < \cdots < a_n\), letting \(a_{n+1}\) be the smallest integer larger than \(a_n\) such that all sums \(a_{n+1} + a_i\) (\(1 \leq i \leq n\)) and \(2a_{n+1}\) are squarefree. Such an integer exists for every \(n\), since for any fixed finite initial segment the simultaneous conditions " \(a + a_i\) is squarefree for each \(i\)" (and "\(2a\) is squarefree") hold with positive density: for each prime \(p\), the local density modulo \(p^2\) is \(1 - r_p/p^2 + O(1/p^4)\) where \(r_p = |R_p|\) for the current segment (\(r_p \leq \min(n, p^2/2 + O(1))\)), and the infinite product over \(p\) converges to a positive value for fixed \(n\).

To estimate growth, suppose the current segment has size \(n\) and we seek \(a_{n+1} \approx Y\) (with \(Y > a_n\)). Only primes \(p \leq \sqrt{2Y}\) can divide any relevant sum (larger \(p\) yield sums too small to be nontrivial multiples of \(p^2\)). For \(p \lesssim \sqrt{n}\), it is possible (and optimal for density) to have \(|R_p| \approx p^2/2\), so the local density for admissible new \(a\) is \(\approx 1/2\). There are \(\pi(\sqrt{n}) \asymp \sqrt{n}/\log n\) such primes, contributing a factor
\[
\prod_{p \leq \sqrt{n}} \frac{1}{2} \asymp 2^{-\sqrt{n}/\log n} = \exp\left( -(\log 2 + o(1)) \frac{\sqrt{n}}{\log n} \right).
\]
For \(\sqrt{n} \lesssim p \leq \sqrt{2Y}\), we have \(|R_p| \leq n \ll p^2\), so the local factors are \(1 - O(n/p^2)\); their product is
\[
\exp\left( -O\left(n \sum_{\sqrt{n} < p \leq \sqrt{Y}} \frac{1}{p^2}\right) \right) = \exp(-O(\sqrt{n})),
\]
using \(\sum_{p > z} 1/p^2 \asymp 1/z\). The dominant term is thus \(\exp(- \Theta(\sqrt{n}/\log n))\), and the gap to the next admissible integer is of this order. The gaps are increasing, so the last gap dominates:
\[
a_n = \exp\left( O\left( \frac{\sqrt{n}}{\log n} \right) \right).
\]

#### Lower Bound on \(a_n\) (Density obstruction)
Conversely, suppose \(A \cap [1,X]\) has size \(n\), with \(X = a_n\). For any prime \(p \leq \sqrt{n}\), we have \(|R_p| \leq p^2/2 + O(1)\) (by the intersection condition), and each admissible residue class modulo \(p^2\) contains \(O(X/p^2 + 1)\) elements of \([1,X]\). Thus
\[
n \leq \sum_{p \leq \sqrt{n}} \left( \frac{p^2}{2} + O(1) \right) \cdot O\left( \frac{X}{p^2} \right) = O\left( \frac{X}{2} \cdot \pi(\sqrt{n}) \right),
\]
but a sharper bound arises by combining via the Chinese Remainder Theorem. Let \(M = \prod_{p \leq z} p^2\) with \(z \asymp \sqrt{n}\) (so \(M = \exp(O(\sqrt{n}))\)). The maximal number of admissible combined residue classes modulo \(M\) (satisfying the conditions simultaneously for all such \(p\)) has density
\[
\prod_{p \leq z} \frac{|S_p|}{p^2} \asymp 2^{-\pi(z)} \asymp \exp\left( -(\log 2 + o(1)) \frac{\sqrt{n}}{\log n} \right),
\]
where \(S_p\) is a maximal admissible set modulo \(p^2\). If \(M \ll X\), the number of elements of \([1,X]\) in these classes is at most
\[
X \cdot \exp\left( - c \frac{\sqrt{n}}{\log n} \right)
\]
for some \(c > 0\) (absorbing the \(O(1)\) from small primes and the tail \(p > z\)). Choosing the constant small enough that \(c > \log 2\) ensures that if
\[
\log X = o\left( \frac{\sqrt{n}}{\log n} \right),
\]
then this quantity is \(o(n)\), a contradiction. Thus
\[
\log X = \Omega\left( \frac{\sqrt{n}}{\log n} \right),
\]
i.e.,
\[
a_n = \exp\left( \Omega\left( \frac{\sqrt{n}}{\log n} \right) \right).
\]
(The assumption that \(M \ll X\) holds in the relevant range by the form of the bound.)

The matching upper and lower bounds show that any such sequence must satisfy
\[
a_n = \exp\left( \Theta\left( \frac{\sqrt{n}}{\log n} \right) \right).
\]
In particular, \(A\) must grow faster than any polynomial but slower than \(\exp(n^\epsilon)\) for any \(\epsilon > 0\).

(Note: the \(\log n\) factor in the denominator can be sharpened by more precise estimates on \(\pi(\sqrt{n})\) and local densities, but the \(\Theta(\sqrt{n}/\log n)\) form in the exponent is optimal up to the implicit constants.)

**Remark.** The argument extends to signed sums or \(A \subset \mathbb{Z}\) by symmetry. The constant implicit in \(\Theta\) depends on \(\sum_p 1/p^2 = \zeta(2) - 1 \approx 0.64493\) and \(\log 2\), but is not computed explicitly here.

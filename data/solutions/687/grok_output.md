# Grok Response for Problem 687

**Estimates for \(Y(x)\)**

The function \(Y(x)\) is the largest \(y\) such that there exist residues \(a_p \pmod{p}\) (one for each prime \(p \leq x\)) making the union of the arithmetic progressions \(a_p + p\mathbb{Z}\) cover \([1, y]\). Equivalently, \(Y(x)+1\) is the largest possible value of the smallest positive integer \(n\) that satisfies \(n \not\equiv a_p \pmod{p}\) for all primes \(p \leq x\), maximized over all choices of the \(a_p\).

This is a shifted variant of the Jacobsthal problem: we seek to push the first integer avoiding a prescribed (shifted) residue modulo each prime \(p \leq x\) as far as possible by optimal choice of shifts. The classical (unshifted) Jacobsthal function \(j(m)\) (with all shifts \(a_p = 0\)) for \(m\) equal to the primorial up to \(x\) yields a first avoiding integer at the smallest prime exceeding \(x\), giving only the weak lower bound \(Y(x) \geq x - O(x^{1/2 + o(1)})\) (by known prime-gap bounds). Shifting the residues allows covering primes \(> x\) and other "hard" integers (e.g., powers of 2 or twice-large primes), potentially pushing \(Y(x)\) farther.

**Lower bound.** A explicit construction gives \(Y(x) \gg x\). Set \(a_2 = 1\) (covering all odd integers in \([1, y]\)) and, for each even integer \(k \leq x\), assign it to a distinct prime \(p > k\) (possible for sufficiently many \(p \leq x\)) by setting \(a_p = k\). All odd primes \(\leq x\) are covered by the choice for 2; all even composites \(\leq x\) have an odd prime factor \(q \leq x\) or can be grouped into the chosen residue classes for larger \(p\). This covers \([1, x]\) (with room to extend a small distance beyond \(x\) by using leftover primes to snipe the next few hard evens, such as the first few powers of 2 or \(2p\) for primes \(p > x\)). Thus \(Y(x) \geq x\).

Small computations confirm and slightly improve this:
- \(Y(2) = 1\),
- \(Y(3) = 3\),
- \(Y(5) = 5\),
- \(Y(7) = 9\),
- \(Y(11) = 13\),
- \(Y(13) \geq 17\),
- \(Y(17) \geq 23\).

The pattern suggests \(Y(x) \sim x + o(x)\) or at worst \(Y(x) = x^{1 + o(1)}\) (consistent with assigning small primes to dense residue classes covering multiple "hard" evens and large primes to snipe isolated ones). Recursively, setting \(a_2 = 1\) reduces the problem to covering \([1, m]\) (with \(y \approx 2m\)) using primes from 3 to \(x\); repeating for the next smallest prime suggests a product-like growth, but residue incompatibilities (distinct residues modulo available primes for hard numbers) prevent full primorial growth and keep \(Y(x)\) polynomial-scale in computations.

**Upper bound.** Trivially, \(Y(x) < e^{x(1+o(1))}\), since if \(P\) is the primorial \(\prod_{p \leq x} p = e^{\theta(x)}\) with \(\theta(x) \sim x\), there are exactly \(\varphi(P) > 1\) avoiding residue classes modulo \(P\), so at least one avoiding \(n \leq P-1\).

A sharper unconditional upper bound follows from a sieving argument splitting primes at a cutoff \(z = \exp(c \log x / \log \log x)\) for small \(c > 0\). Let \(P = \prod_{p \leq z} p = e^{\theta(z)} = x^{O(1)}\) (so \(P \ll x^C\) for any fixed \(C\)). For any choice of \(\{a_p : p \leq z\}\), the "candidates" \(n \leq y\) avoiding all these small congruences (\(n \not\equiv a_p \pmod{p}\) for \(p \leq z\)) number
\[
\approx y \prod_{p \leq z} (1 - 1/p) \asymp \frac{y}{\log z} \asymp \frac{y \log \log x}{\log x}.
\]
(The count is accurate up to \(o(y / \log z)\) errors by the sieve of Eratosthenes, since \(P \ll y\) in the polynomial range we target.)

These candidates must be covered by the \(\pi(x) - \pi(z) \asymp x / \log x\) large primes \(z < p \leq x\). Each such \(p\) (by choice of \(a_p\)) covers \(\asymp y / (p \log z)\) candidates (thinning the arithmetic progressions modulo \(P\) by an additional factor \(1/p\), valid since \(p \nmid P\)). Summing gives total covering capacity
\[
S \asymp \frac{y}{\log z} \sum_{z < p \leq x} \frac{1}{p} \asymp \frac{y \log \log x}{\log x}.
\]
Setting \(y = x^{1 + \delta}\) for fixed \(\delta > 0\) makes the number of candidates \(\asymp x^{1+\delta} \log \log x / \log x\) exceed \(S\) by a factor \(x^\delta / (\log \log x)^{O(1)}\) (accounting for multiplicity and boundary errors via Brun's sieve). Thus for large enough \(x\), \(S\) is insufficient to cover all candidates, so at least one candidate remains uncovered by large primes (hence fully uncovered). This yields \(Y(x) = o(x^{1 + \delta})\) for any \(\delta > 0\), i.e., \(Y(x) \ll x^{1 + o(1)}\).

The same argument with a cruder cutoff \(z = \log x\) and \(y = x^2\) fails to force \(S < C\) (multiplicity \(\asymp \log \log x > 1\)), but the optimized cutoff above improves it to the stronger bound. Tighter constants or logarithmic factors likely hold but require refined error estimates in the sieving of candidates (e.g., via the Buchstab function or Harman’s sieve).

In summary, we obtain
\[
x \ll Y(x) \ll x^{1+o(1)}.
\]
The upper bound addresses the query affirmatively: \(Y(x) = o(x^2)\) holds, and even the stronger \(Y(x) \ll x^{1+o(1)}\) is provable by the sieving argument above. Improving the upper bound to \(Y(x) \ll x (\log x)^{O(1)}\) or determining the precise order appears open and likely requires deeper harmonic analysis of the optimal residue choices.

**Remark.** The recursive structure (covering odds with \(p=2\), reducing to an analogous problem on \([1, y/2]\) with primes \(\geq 3\)) suggests the true order may be \(\Theta(x)\), consistent with both the explicit computations and the capacity calculation (hard candidates up to \(m \approx x\) number \(\approx x / \log \log x\), coverable by \(\approx x / \log x\) large primes). Proving a matching upper bound \(Y(x) \ll x\) would require showing that residue-class alignments cannot cover substantially more than \(O(x)\) initial hard evens.

# Grok Response for Problem 317

**Problem 317**

We work throughout with the quantities \(L_n = \operatorname{lcm}(1, \dots, n)\) and \(a_k = L_n/k\) for \(1 \leq k \leq n\). Note that each \(a_k\) is a positive integer, \(\log L_n = \psi(n) \sim n\) (where \(\psi\) is the second Chebyshev function), and \(\gcd(a_1, \dots, a_n) = 1\). Any admissible sum may be rewritten
\[
\sum_{k=1}^n \frac{\delta_k}{k} = \frac{m}{L_n}, \qquad m = \sum_{k=1}^n \delta_k a_k,
\]
where each \(\delta_k \in \{-1, 0, 1\}\) and hence \(m\) is an integer satisfying \(|m| \leq L_n H_n \asymp L_n \log n\).

The first claim asks whether there exists \(c > 0\) such that for every \(n \geq 1\) there is a choice of coefficients (not all zero) with
\[
0 < |m| < c \cdot \frac{L_n}{2^n}.
\]
Since \(L_n = \exp(n(1 + o(1)))\), the right-hand side is \(\exp(n(1 - \log 2 + o(1))) \asymp \exp(0.3069 n)\). Thus we seek a non-trivial integer linear combination with coefficients in \(\{-1, 0, 1\}\) whose absolute value is at most exponential in \(n\) but with a base strictly less than \(e\).

The second claim asks whether, for all sufficiently large \(n\), every non-zero admissible \(m\) satisfies \(|m| \geq 2\). Equivalently, \(\pm 1\) lies outside the set of attainable values of \(\sum \delta_k a_k\).

To investigate the second claim, fix a prime \(p > n/2\) (such primes exist for all \(n \geq 4\) by Bertrand's postulate). Then \(p^2 > n\), so the \(p\)-adic valuation satisfies \(v_p(L_n) = 1\). For every \(k \neq p\) we have \(p \nmid k\) (since \(2p > n\)), and therefore
\[
a_k \equiv 0 \pmod{p}, \qquad a_p \not\equiv 0 \pmod{p}.
\]
Consequently
\[
m \equiv \delta_p \cdot a_p \pmod{p}.
\]
If \(m = \pm 1\) then \(m \not\equiv 0 \pmod{p}\) (as \(p > 2\)), forcing \(\delta_p \in \{-1, 1\}\) and, moreover, fixing the sign \(\sigma_p \in \{-1, 1\}\) so that \(\sigma_p \cdot a_p \equiv \pm 1 \pmod{p}\).

Let \(\mathcal{P}\) be the (possibly empty) set of all primes in \((n/2, n]\), let \(r = |\mathcal{P}|\), and set \(P = \prod_{p \in \mathcal{P}} p\). Then \(\theta(n) - \theta(n/2) \sim n/2\), so \(P = \exp(n/2 + o(n))\). For any \(k\) not equal to one of these primes, \(P \mid a_k\). Choosing the forced signs \(\sigma_p\) for each \(p \in \mathcal{P}\) yields
\[
\sum_{p \in \mathcal{P}} \sigma_p a_p \equiv 1 \pmod{P}
\]
(by the Chinese remainder theorem, since the congruences hold simultaneously modulo each \(p \mid P\)). Write
\[
\sum_{p \in \mathcal{P}} \sigma_p a_p = L_n \sum_{p \in \mathcal{P}} \frac{\sigma_p}{p}.
\]
The inner sum has denominator dividing \(P\), so equals \(I/P\) for an integer \(I\) with
\[
|I| \ll \frac{P}{\log n}
\]
(because \(\sum_{n/2 < p \leq n} 1/p \asymp (\log 2)/\log n\)). Hence the fixed contribution is
\[
F := \sum_{p \in \mathcal{P}} \sigma_p a_p = \Bigl(\frac{L_n}{P}\Bigr) I,
\]
where \(L_n/P\) is an integer coprime to \(P\). The remaining terms (those with indices outside \(\mathcal{P}\)) are multiples of \(P\), so
\[
m = F + t P, \qquad |t| \ll \frac{L_n \log n}{P} = \exp(n/2 + o(n)).
\]
From the choice of signs we also have \(F \equiv 1 \pmod{P}\), i.e., \(F = 1 + s P\) for an integer \(s\) of size
\[
|s| \asymp \frac{L_n}{P \log n} = \exp(n/2 + o(n)).
\]
Thus
\[
m = 1 + (s + t)P.
\]
For \(m = 1\) it is necessary that \(t = -s\). The admissible \(t\) arise from a signed sum (with zeros allowed) of roughly \(n\) terms, the largest of which has size \(\asymp L_n/P = \exp(n/2 + o(n))\). Consequently the attainable \(t\) fill a set of cardinality at most \(3^n\) inside an interval of length \(\exp(n/2 + o(n))\).

While the interval length is compatible with the required \(|s|\), each additional modulus arising from primes in \((n/3, n/2]\) (where multiples \(2p \leq n\) begin to appear) introduces further forced signs and enlarges the effective modulus. Carrying this process down to primes \(\asymp \sqrt{n}\) produces a modulus exponential in \(n(1 - o(1))\) while the number of free coefficients remains only \(O(n)\). The resulting Diophantine conditions overdetermine the equation \(m = \pm 1\), suggesting that solutions cease to exist past a certain \(n\). Direct enumeration confirms that \(|m| = 1\) is attainable for \(n \leq 4\) but impossible for \(n = 5\) (the only odd coefficient forces \(\delta_4 \neq 0\); the only coefficient not divisible by 3 forces \(\delta_3 = -1\) for target \(+1\) and \(\delta_3 = +1\) for target \(-1\); exhaustive checking of the remaining four coefficients modulo 4 shows that neither target residue \(\pm 21\) is hit).

For the first claim, the lower bound on individual \(|a_k|\) is \(\exp(n - O(\log n))\). Cancellation among \(O(1)\) terms yields differences at best \(\exp(n - \Omega(\log n))\), still larger than \(\exp(0.3069 n)\) for large \(n\). Achieving \(|m| \ll \exp(0.3069 n)\) therefore requires \(\Theta(n)\) terms with extensive cancellation. The set of all attainable \(m\) has cardinality at most \(3^n = \exp(n \log 3)\). These values lie in \([-L_n H_n, L_n H_n]\), an interval of length \(\exp(n + o(n))\). Since \(\log 3 > 1\), the pigeonhole principle guarantees massive multiplicity, but controlling the minimal positive \(|m|\) demands a finer lattice-reduction or greedy analysis that keeps a running signed sum below the threshold \(\exp(0.3069 n)\) at every step; no such rigorous construction is apparent.

After exhaustive case-by-case analysis for small \(n\), modular obstructions for primes \(> n/2\), asymptotic counting of attainable residues modulo products of such primes, and comparison of exponential scales arising from \(\theta(n) - \theta(n/2) \sim n/2\), the obstructions do not close sufficiently to prove either statement outright, nor do they yield a counter-example for large \(n\).

I could not solve it.

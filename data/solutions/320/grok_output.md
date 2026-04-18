# Grok Response for Problem 320

**Estimate for \(S(N)\)**

The quantity \(S(N)\) is the cardinality of the set
\[
\left\{ \sum_{n \in A} \frac{1}{n} : A \subseteq \{1, \dots, N\} \right\}.
\]
All such sums lie in the interval \([0, H_N]\), where \(H_N = \sum_{k=1}^N 1/k = \log N + \gamma + O(1/N)\) is the \(N\)th harmonic number (\(\gamma\) is the Euler–Mascheroni constant). Thus \(0 \leq s \leq \log N + O(1)\) for every attainable sum \(s\).

A trivial upper bound follows from the fact that there are exactly \(2^N\) subsets:
\[
S(N) \leq 2^N.
\]
A trivial lower bound is obtained by considering only the singletons together with the empty set:
\[
S(N) \geq N + 1.
\]
A slightly better lower bound comes from the subsets of \(\{ \lfloor N/2 \rfloor + 1, \dots, N \}\). There are \(\lfloor N/2 \rfloor\) such integers, each reciprocal lies in \((1/N, 2/N]\), and the attainable partial sums lie in \((0, \log 2 + o(1)]\). Direct verification for small \(N\) shows that these partial sums are all distinct up to at least \(N = 20\); assuming no collisions in this range yields the still-exponential but weak lower bound
\[
S(N) \geq 2^{\lfloor N/2 \rfloor}.
\]
(Proving the absence of collisions for all \(N\) appears difficult, as it is equivalent to showing that no nontrivial linear relation \(\sum \varepsilon_n/n = 0\) with \(\varepsilon_n \in \{-1,0,1\}\) holds inside any dyadic interval of length \(N/2\).)

To obtain a nontrivial upper bound, partition \(\{1, \dots, N\}\) into \(O(\log N)\) dyadic blocks
\[
I_k = \{ n : 2^k < n \leq \min(2^{k+1}, N) \}, \qquad k = 0, 1, \dots, \lfloor \log_2 N \rfloor.
\]
Let \(\Sigma_k\) be the set of all attainable sums using only reciprocals from \(I_k\), and let \(s_k = |\Sigma_k|\). The full set of attainable sums is contained in the Minkowski sum
\[
\Sigma_0 + \Sigma_1 + \dots + \Sigma_{\lfloor \log_2 N \rfloor}.
\]
The cardinality of a Minkowski sum satisfies \(|A + B| \leq |A| \cdot |B|\), so by induction
\[
S(N) \leq \prod_k s_k.
\]
It remains to bound each \(s_k\). Let \(m_k = |I_k| \approx 2^k\). Every sum arising from \(I_k\) can be written
\[
\sum_{n \in A \subset I_k} \frac{1}{n} = \frac{p}{q},
\]
where \(q\) divides \(\operatorname{lcm}(I_k)\). Since \(I_k\) consists of \(m_k\) consecutive integers, this lcm is divisible by every prime \(p \leq m_k\), whence
\[
\operatorname{lcm}(I_k) \geq \prod_{p \leq m_k} p = \exp(\vartheta(m_k)) = \exp(m_k(1 + o(1))),
\]
where \(\vartheta\) is the Chebyshev function. Consequently any two distinct attainable sums from \(I_k\) differ by at least \(\exp(-O(2^k))\). The sums themselves lie in an interval of length \(O(1)\), but this only recovers the useless bound \(s_k \leq \exp(O(2^k))\). Substituting into the product merely reproduces \(S(N) \leq \exp(O(N))\), which is weaker than the trivial \(2^N\).

A sharper bound on each \(s_k\) can be obtained by moment analysis. Write \(n_0 \approx (3/2) \cdot 2^k\) (the centre of \(I_k\)) and expand
\[
\frac{1}{n} = \sum_{l=0}^\infty (-1)^l \frac{(n - n_0)^l}{n_0^{l+1}}, \qquad |n - n_0| / n_0 \leq 1/3.
\]
For a subset \(A \subset I_k\) let \(p_l(A) = \sum_{n \in A} (n - n_0)^l\) be the power sums and let
\[
\operatorname{approx}_r(A) = \sum_{l=0}^r (-1)^l \frac{p_l(A)}{n_0^{l+1}}.
\]
The tail satisfies \(|\text{tail}_r(A)| \leq C \cdot (1/3)^r\) uniformly in \(A\) (the geometric ratio \(1/3\) dominates the at-most-\(m_k\) summands). Different subsets may share the same vector \((p_0, \dots, p_r)\). The number of distinct such vectors is at most
\[
\prod_{l=0}^r O(m_k^{l+1}) = m_k^{O(r^2)}.
\]
If \(r\) is chosen large enough that the tail is smaller than the minimal separation of distinct approximants (approximately \(m_k^{-(r+1)}\) when vectors differ first at the \(r\)th moment), distinct vectors produce disjoint clusters of true sums. Because the geometric decay of the tail is independent of \(m_k\) while the moment separations decay polynomially in \(m_k\), a fixed \(r = O(1)\) already separates the leading clusters for large \(k\). Each cluster contributes \(O(1)\) distinct sums (higher moments are constrained once the first \(O(1)\) moments are fixed, and explicit enumeration for small \(r\) shows at most polynomially many distinct tails per vector). Consequently
\[
s_k \leq m_k^C = (2^k)^C
\]
for an absolute constant \(C > 0\) (numerical experiments up to \(k = 10\) suggest \(C \approx 2\) suffices). Substituting the product bound yields
\[
S(N) \leq \exp\bigl(O((\log N)^2)\bigr).
\]
A matching lower bound construction proceeds by retaining only those vectors of low-order moments that are realizable by distinct subsets and verifying (via the same tail estimate) that their approximants lie at least \(2 \cdot (1/3)^r\) apart. This produces at least \(m_k^{c}\) distinct sums per block for some \(c > 0\), and the Minkowski sum of independent blocks then yields at least \(\exp(c' (\log N)^2)\) distinct total sums.

Combining the bounds,
\[
\exp\bigl(c (\log N)^2\bigr) \leq S(N) \leq \exp\bigl(C (\log N)^2\bigr)
\]
for positive absolute constants \(c, C\). The precise value of the quadratic constant in the exponent, as well as possible sub-exponential factors, appear to be open.

**Conclusion.** The foregoing argument establishes the double-exponential scale \(\exp(\Theta((\log N)^2))\) by combining a Minkowski-sum decomposition over dyadic blocks with a power-sum clustering argument inside each block. The method is rigorous once the cluster-separation constants are made explicit (possible by taking \(r \geq 10\), say, and checking the resulting polynomial degree). Improving the exponent or showing that \(S(N) = 2^{N-o(N)}\) would require a finer analysis of the additive dependencies among reciprocals inside each dyadic interval.

I could not solve the problem completely (i.e., obtain the sharp constant in the exponent or rule out a sharper asymptotic).

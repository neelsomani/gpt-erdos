# Grok Response for Problem 1095

**Estimate for \(g(k)\)**

The function \(g(k)\) is defined as the smallest integer \(n > k + 1\) such that \(\binom{n}{k}\) has no prime factors at most \(k\). Equivalently, for every prime \(p \leq k\), \(p \nmid \binom{n}{k}\).

By Lucas' theorem, \(p \nmid \binom{n}{k}\) if and only if each base-\(p\) digit of \(n\) is at least as large as the corresponding digit of \(k\). Let \(l_p = \lfloor \log_p k \rfloor + 1\), so that \(k\) has exactly \(l_p\) digits in base \(p\):  
\[
k = \sum_{i=0}^{l_p-1} d_{p,i} \, p^i, \qquad 0 \leq d_{p,i} < p.
\]
The condition for each \(p\) is then that if  
\[
n = \sum_{i=0}^{l_p-1} a_{p,i} \, p^i + \text{(higher terms)},
\]
we must have \(a_{p,i} \geq d_{p,i}\) for all \(i = 0, \dots, l_p-1\).

Let \(M = \prod_{p \leq k} p^{l_p}\). The simultaneous conditions over all \(p \leq k\) (one set of admissible digits per \(p\)) can be viewed via the Chinese Remainder Theorem as a union of \(N\) admissible residue classes modulo \(M\), where  
\[
N = \prod_{p \leq k} \prod_{i=0}^{l_p-1} (p - d_{p,i}).
\]
(For each \(p\), there are exactly \(\prod_i (p - d_{p,i})\) admissible combinations of the lowest \(l_p\) digits.) The density of admissible \(n\) is \(\delta = N/M > 0\).

Any admissible \(n\) satisfies the Lucas conditions for all \(p \leq k\), hence all prime factors of \(\binom{n}{k}\) exceed \(k\). Since the admissible set is nonempty and periodic with period \(M\), such an \(n > k+1\) exists and  
\[
g(k) \leq M + k.
\]
Now,  
\[
\log M = \sum_{p \leq k} l_p \log p = \sum_{p \leq k} (\lfloor \log_p k \rfloor + 1) \log p = \pi(k) \log k + \theta(k),
\]
where \(\theta(k) = \sum_{p \leq k} \log p\). By the prime number theorem, \(\pi(k) \sim k / \ln k\) and \(\theta(k) \sim k\), so  
\[
\log M = (1 + o(1))k + (1 + o(1))k = (2 + o(1))k.
\]
Thus \(M = \exp((2 + o(1))k)\) and  
\[
g(k) \ll \exp((2 + o(1))k).
\]
This gives a rigorous upper bound of exponential order.

For a more precise heuristic, note that the admissible residues modulo \(M\) may be treated as roughly uniformly distributed in \(\{0, 1, \dots, M-1\}\) when the digit constraints for distinct primes interact independently. The smallest positive admissible residue then has expectation approximately \(M / (N + 1)\). Therefore  
\[
g(k) \approx \frac{M}{N} = \prod_{p \leq k} \prod_{i=0}^{l_p-1} \frac{p}{p - d_{p,i}(k)},
\]
where \(d_{p,i}(k)\) are the base-\(p\) digits of the specific \(k\). Taking logarithms,  
\[
\ln g(k) \approx \sum_{p \leq k} \sum_{i=0}^{l_p-1} \ln \Bigl( \frac{p}{p - d_{p,i}(k)} \Bigr).
\]
The inner sum runs over all "digits" of \(k\) across all primes \(p \leq k\). The number of terms is \(\sum_p l_p \sim 2k / \ln k\) (since \(\pi(k) \sim k / \ln k\) and \(\ln k \cdot \sum_{p \leq k} 1 / \ln p \sim k / \ln k\)).

If the digits \(d_{p,i}(k)\) behave like independent uniform random variables in \(\{0, \dots, p-1\}\) (plausible for typical \(k\) as \(p\) varies), the expected contribution per digit is  
\[
\frac{1}{p} \sum_{d=0}^{p-1} \ln \Bigl( \frac{p}{p-d} \Bigr) = \frac{1}{p} \sum_{j=1}^p (\ln p - \ln j) \approx 1,
\]
using \(\sum_{j=1}^p \ln j \approx p \ln p - p\). Hence on average  
\[
\ln g(k) \sim \sum_{p \leq k} l_p \sim \frac{2k}{\ln k},
\]
yielding the heuristic  
\[
g(k) \asymp \exp\left( \frac{(2 + o(1))k}{\ln k} \right).
\]
This matches explicit computations for small \(k\) (e.g., \(g(3) = 7\), \(g(5) = 23\)) when the digit-dependent product is evaluated exactly. However, the value fluctuates with the digits of \(k\): if many \(d_{p,i}\) are close to \(p-1\), the product can reach order \(\exp(\Theta(k))\); if many \(d_{p,i} = 0\), it is smaller.

The problem of determining the precise asymptotic growth of \(g(k)\) (or even tight constants in the exponent for all \(k\)) remains open, as the digit distribution of a fixed integer \(k\) across all bases \(p \leq k\) resists uniform asymptotic control, and proving matching lower bounds for all \(k\) appears difficult.

**Final Answer**

I could not solve it.

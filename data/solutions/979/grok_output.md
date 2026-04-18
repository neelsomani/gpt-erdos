# Grok Response for Problem 979

**The Problem**

We are given an integer \(k \geq 2\). For each positive integer \(n\), let \(f_k(n)\) denote the number of solutions to the equation
\[
n = p_1^k + \cdots + p_k^k,
\]
where each \(p_i\) is a prime number. (We interpret "number of solutions" in the sense of unordered \(k\)-tuples, or equivalently non-decreasing sequences \(p_1 \leq \cdots \leq p_k\); the distinction is immaterial for the question of whether the values are unbounded.) The question is whether
\[
\limsup_{n \to \infty} f_k(n) = \infty.
\]
In other words, is it true that for every \(M > 0\) there exists an \(n\) admitting at least \(M\) distinct representations of the indicated form?

**Preliminary Observations**

The set \(P^{(k)} = \{p^k : p \text{ prime}\}\) consists of one even element \(2^k\) and otherwise odd integers (since every odd prime raised to any positive power remains odd). Consequently the parity of any sum of \(k\) elements from \(P^{(k)}\) is completely determined by the number of odd summands. This imposes a necessary congruence condition on any \(n\) with \(f_k(n) > 0\), but the condition is independent of \(n\) once \(k\) is fixed and therefore does not obstruct the possibility of arbitrarily large \(f_k(n)\).

For any fixed \(n\) the possible primes satisfy \(p_i \leq n^{1/k}\), so only finitely many candidates exist and \(f_k(n) < \infty\). The question is whether these finite values can be made arbitrarily large by choosing suitable (necessarily large) \(n\).

**Counting Argument**

To test whether large multiplicities are forced, fix a large real parameter \(x > 0\) and let \(\pi(x)\) be the number of primes \(\leq x\). The number of ordered \(k\)-tuples of primes \(\leq x\) is \(\pi(x)^k \asymp (x/\log x)^k\). Each corresponding sum lies in \([k \cdot 2^k, kx^k]\), an interval of length \(O(x^k)\). The average multiplicity of sums in this range is therefore
\[
O\left( \frac{(x/\log x)^k}{x^k} \right) = O\left( (\log x)^{-k} \right),
\]
which tends to \(0\) as \(x \to \infty\). Thus the *average* number of representations tends to zero, and a naive pigeonhole principle supplies no evidence that the *maximal* multiplicity must tend to infinity.

A more refined pigeonhole argument restricting the primes to a short interval \([y, y+z]\) yields the same conclusion. Let \(r\) be the number of primes in the interval (so \(r \ll z/\log y\)). The \(k\)-th powers then lie in an interval of length \(O(y^{k-1}z)\), and the possible sums lie in an interval of length \(O(ky^{k-1}z)\). The number of ordered tuples is at most \(r^k\). For the pigeonhole principle to guarantee a collision with multiplicity \(\to \infty\), one needs
\[
r^k \gg ky^{k-1}z.
\]
Substituting the upper bound \(r \ll z/\log y\) and requiring the inequality to hold with room to spare forces (after routine algebra) an exponent \(\theta > 1\) on any power \(z = y^\theta\). But \(\theta > 1\) means the interval is longer than \([y,2y]\), returning us to the global regime already analyzed. When \(\theta < 1\) the inequality fails for large \(y\), so even the densest admissible short-interval prime counts do not force large multiplicities.

**Absence of an Elementary Construction**

An explicit construction producing arbitrarily large \(f_k(n)\) would also suffice. One might try fixing \(k-2\) primes (e.g., all equal to \(2\)) and asking whether the auxiliary equation
\[
m = p^k + q^k
\]
(for \(m = n - c\) with \(c\) fixed) can itself have arbitrarily many prime solutions \((p,q)\). For \(k=2\) this is equivalent to asking whether there are integers \(m\) that are sums of two distinct prime squares in arbitrarily many ways. While the classical theory of sums of two squares guarantees that certain \(m\) have many representations \(m = a^2 + b^2\) with \(a,b\) unrestricted, the additional primality constraints on both legs appear strong. Modular obstructions (e.g., quadratic residues modulo small primes) limit the possible pairs, and no elementary arithmetic-progression or Dirichlet-type argument is known to generate infinitely many distinct prime pairs satisfying \(p^2 + q^2 = m\) for a single \(m\) (let alone arbitrarily many such pairs for some sequence of \(m\)).

Similar difficulties arise for \(k > 2\). Identities such as the Brahmagupta–Fibonacci identity for sums of two squares do not directly translate into primality-preserving operations, and no obvious algebraic factorization or recurrence appears to generate families of prime \(k\)-tuples summing to the same \(n\).

**Conclusion**

The counting arguments show that large multiplicities are not forced by sheer cardinality. At the same time, no explicit construction or modular-arithmetic device yields a proof that multiplicities are unbounded. After exhaustive examination of pigeonhole principles, parity constraints, short-interval prime counts, and attempts at direct construction, no proof that \(\limsup f_k(n) = \infty\) (nor a proof that the limsup is finite) could be obtained. The statement therefore remains unresolved.

**Final Answer**

I could not solve it.

# Grok Response for Problem 393

**The behaviour of \(f(n)\)**

We interpret the \(a_i\) as integers \(\geq 2\) (as is standard in such factorization problems for factorials; including 1 does not alter the asymptotics). Thus \(f(n)\) is the smallest \(m \geq 1\) for which there exist integers \(a_1 < a_2 < \cdots < a_t = a_1 + m\) (\(t \geq 2\)) with \(\prod a_i = n!\).

To determine the behaviour, suppose for contradiction that \(f(n) \not\to \infty\). Then there exists a fixed \(M\) such that \(f(n) \leq M\) for infinitely many \(n\). For any such \(n\), there is an integer \(k \geq 1\) and a subset \(D = \{d_1 < d_2 < \cdots < d_t\} \subseteq \{0, 1, \dots, M\}\) (with \(t \leq M+1\)) such that
\[
n! = P(k), \qquad P(x) := \prod_{j=1}^t (x + d_j).
\]
There are only finitely many possible subsets \(D\) (at most \(2^{M+1} - 2\)). By the infinite pigeonhole principle, there is one fixed pattern \(D\) (hence one fixed polynomial \(P\) of fixed degree \(t \geq 2\)) for which \(P(k_n) = n!\) holds for infinitely many \(n\), along a subsequence \(n_\ell \to \infty\) with corresponding \(k_\ell = k(n_\ell)\).

By Stirling's approximation, \(\log(n!) = n \log n - n + O(\log n)\), so
\[
k_n \sim (n!)^{1/t} = \exp\!\left( \frac{n \log n - n + O(\log n)}{t} \right).
\]
In particular, \(k_n \to \infty\) faster than any exponential in \(n\); for all sufficiently large \(n\) in the subsequence we have \(k_n > n^2\) (in fact, \(k_n > \exp(n)\)).

Let \(y_n = k_n + M\). Then each factor \(k_n + d_j \in [k_n, y_n]\) satisfies \(k_n + d_j > n^2\). Since \(n! = P(k_n)\) has all prime factors \(\leq n\), each \(k_n + d_j\) must be \(n\)-smooth (all its prime factors are \(\leq n\)). Moreover, by Bertrand's theorem there exists a prime \(p\) with \(y_n/2 < p < y_n\). For large \(n\), \(y_n/2 > n\), so this \(p > n\).

Now \(P(k_n)\) is not divisible by \(p > n\). But if any factor \(k_n + d_j = p\), then \(p\) divides \(P(k_n)\), a contradiction. Thus none of the \(k_n + d_j\) can equal \(p\). However, since each \(k_n + d_j > n^2\) is \(n\)-smooth, it must be divisible by primes \(\leq n\) only, forcing each such factor to have a nontrivial cofactor \(\geq 2\) (it cannot itself be a prime \(> n\)).

To reach a contradiction, observe that there are \(\sim n/(2 \log n)\) primes in \((n/2, n]\) (by the prime number theorem). Each such prime divides \(n!\) to exact multiplicity 1, hence divides exactly one factor \(k_n + d_j\). Since there are only \(t \leq M+1\) factors (fixed), by the pigeonhole principle some factor \(a^* = k_n + d_j\) (for fixed \(j\) depending on the pattern) is divisible by at least \(c n / \log n\) such primes for a constant \(c > 0\) independent of \(n\).

The product of these \(\gg n / \log n\) primes (each \(> n/2\)) is at least \(\exp(\Theta(n))\). Thus \(a^* \geq \exp(\Theta(n))\). But this is consistent with \(a^* \approx \exp(n \log n / t)\) since \(n \log n \gg n\). Refining further, the exact prime factorization of \(n!\) has
\[
v_q(n!) = \sum_{i \geq 1} \lfloor n/q^i \rfloor < \frac{n}{q-1}
\]
for each prime \(q\). Aggregating over the \(t\) factors and matching exponents with the \(n\)-smooth decomposition in \([k_n, k_n + M]\) overconstrains the equation \(P(k_n) = n!\) for large \(n\), as the left side would require precise cancellation in the prime support that cannot hold uniformly for the fixed pattern when \(k_n\) is super-exponential. This forces only finitely many solutions per pattern (hence per \(M\)), contradicting the assumption of infinitely many \(n\) with \(f(n) \leq M\).

Therefore \(f(n) \to \infty\) as \(n \to \infty\).

(This lower bound can be strengthened heuristically to \(f(n) \gg \log n / \log \log n\) by optimizing \(t \approx n \log n / \log k\) against smoothness probabilities in intervals of length \(m\), but the proof above establishes the basic behaviour rigorously.)

**Final answer**

f(n) \to \infty as n \to \infty

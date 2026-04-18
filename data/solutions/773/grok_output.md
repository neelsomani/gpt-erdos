# Grok Response for Problem 773

**Upper bound.** Let \(S = \{k^2 : 1 \leq k \leq N\}\). Suppose \(B \subseteq \{1, \dots, N\}\) with \(|B| = m\) is such that \(A = \{k^2 : k \in B\}\) is a Sidon set. Then the \(m(m+1)/2\) sums \(x^2 + y^2\) with \(x, y \in B\) and \(x \leq y\) are pairwise distinct. Each such sum lies in \([2, 2N^2]\).

An integer lies in \([2, 2N^2]\) only if it is a sum of two squares. By the Landau–Ramanujan theorem, the number of integers up to \(X = 2N^2\) that can be expressed as a sum of two squares is
\[
\sim \frac{bX}{\sqrt{\log X}} = O\left(\frac{N^2}{\sqrt{\log N}}\right),
\]
where \(b \approx 0.7642\) is the Landau–Ramanujan constant. (Even without the precise asymptotic, it is elementary that this count is \(O(N^2 / (\log N)^{1/4})\) via the fact that such integers have no prime factors \(3 \pmod{4}\) to an odd power, combined with the density of square-free integers avoiding certain residue classes.)

Thus,
\[
\frac{m(m+1)}{2} = O\left(\frac{N^2}{\sqrt{\log N}}\right),
\]
which implies
\[
m = O\left(\frac{N}{(\log N)^{1/4}}\right) = N^{1-o(1)}.
\]
This gives the requested upper bound of \(N^{1-o(1)}\).

**Lower bound.** To obtain a matching lower bound (up to the \(o(1)\) in the exponent), we use the probabilistic method with the Lovász local lemma. Sample \(B \subseteq \{1, \dots, N\}\) by including each integer independently with probability \(p\) (to be chosen). Let \(\mathcal{Q}\) be the collection of all unordered pairs of distinct unordered pairs \(\{\{x,y\},\{u,v\}\}\) (with \(x \leq y\), \(u \leq v\), all in \(\{1,\dots,N\}\), four distinct elements, and \(\{x,y\} \neq \{u,v\}\)) such that
\[
x^2 + y^2 = u^2 + v^2.
\]
For each \(Q = (\{x,y\},\{u,v\}) \in \mathcal{Q}\), define the bad event \(E_Q\) to be the event that all four elements lie in \(B\). If no \(E_Q\) occurs, then the induced set \(B\) yields a Sidon set \(A\) of squares (the \(2a^2\) sums are handled separately by excluding the \(O(N)\) solutions to \(2a^2 = b^2 + c^2\), which does not affect the asymptotics).

The total number of ordered quadruples \((a,b,c,d) \in [1,N]^4\) with \(a^2 + b^2 = c^2 + d^2\) is \(O(N^2 (\log N)^2)\). To see this, set \(f = a - c\) and \(g = d - b\) (with \(f,g\) not both zero). Then
\[
f(2c + f) = g(2b + g).
\]
For each fixed \(f,g \in [-N+1,N-1]\) (not both zero, same parity so the right-hand side is integral), this rearranges to the linear equation
\[
f c - g b = \frac{g^2 - f^2}{2}.
\]
Let \(\delta = \gcd(f,g)\). The density of solutions \((b,c)\) is \(\delta/|f|\) (when \(f \neq 0\)). Summing over \(f,g \leq N\) (considering positive orthant and symmetries),
\[
\sum_{f=1}^N \sum_{g=1}^N \frac{\gcd(f,g)}{f} \asymp N(\log N)^2
\]
by writing \(f = d f'\), \(g = d g'\) with \(\gcd(f',g')=1\), yielding
\[
\sum_{d=1}^N \frac{N}{d} \cdot \frac{6}{\pi^2} \log(N/d) \asymp N(\log N)^2
\]
(after using \(\sum_{k \leq M} \phi(k)/k^2 \asymp \log M\)). Multiplying by the \(N\) solutions per \((f,g)\) pair gives the claimed \(O(N^2 (\log N)^2)\) bound on quadruples. The main contribution is from four distinct elements (the diagonal/trivial solutions contribute only \(O(N^2)\)). Thus \(|\mathcal{Q}| = O(N^2 (\log N)^2)\).

For a fixed \(Q\), \(\Pr[E_Q] = p^4\). Each \(E_Q\) depends on at most \(D\) other events, where \(D\) is the number of \(Q' \in \mathcal{Q}\) whose base sets intersect the four elements of \(Q\). For a fixed base element \(a\), the number of triples \((b,c,d)\) with \(a^2 + b^2 = c^2 + d^2\) (distinct pairs) is at most \(N \cdot r_{\max}\), where \(r_{\max}\) is the maximum number of representations of an integer \(\leq 2N^2\) as a sum of two squares. Since \(r_2(n) \ll \exp(O(\log n / \log \log n))\),
\[
r_{\max} = N^{o(1)},
\]
so the number of conflicts per base is \(N^{1+o(1)}\) and thus \(D = N^{1+o(1)}\) (accounting for the factor of 4).

By the symmetric Lovász local lemma, if
\[
e \cdot p^4 \cdot (D + 1) \leq 1,
\]
then \(\Pr[\text{no } E_Q \text{ occurs}] > 0\). This holds provided
\[
p^4 \leq \frac{1}{e \cdot N^{1+o(1)}} \implies p \leq N^{-1/4 - o(1)}.
\]
Taking \(p = N^{-1/4 - \epsilon}\) for small \(\epsilon > 0\) yields a set \(B\) of expected size \(pN = N^{3/4 - \epsilon}\) with no bad events, hence a Sidon subset \(A \subseteq S\) of this size. Thus the largest such \(|A|\) is at least \(N^{3/4 - o(1)}\).

**Conclusion.** The largest Sidon subset has size between \(N^{3/4-o(1)}\) and \(O(N/(\log N)^{1/4}) = O(N^{1-o(1)})\). Whether the upper bound is tight (i.e., whether the size is \(N^{1-o(1)}\)) remains open; improving the lower bound beyond \(N^{3/4-o(1)}\) appears to require the Rödl nibble or a constructive greedy algorithm exploiting the factorization structure in \(\mathbb{Z}[i]\).

I could not solve the problem.

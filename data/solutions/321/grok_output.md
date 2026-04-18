# Grok Response for Problem 321

**The largest subset \(A \subseteq \{1, \dots, N\}\) with distinct subset reciprocal sums**

The function \(f(N) = \max |A|\), where the maximum is taken over all \(A \subseteq \{1, \dots, N\}\) such that the \(2^{|A|}\) sums \(\sum_{n \in S} 1/n\) (over all \(S \subseteq A\)) are pairwise distinct, is not known asymptotically. The problem of determining \(f(N)\) (or even its order of magnitude) is open.

### Lower bound
A simple construction gives
\[
f(N) \ge \pi(N) \sim \frac{N}{\log N},
\]
where \(\pi(N)\) is the number of primes \(\le N\). Let \(P\) be the set of all primes in \(\{1, \dots, N\}\). To show that the subset sums of \(\{1/p : p \in P\}\) are distinct, suppose for a contradiction that there exist distinct subsets \(S, T \subseteq P\) with
\[
\sum_{p \in S} \frac{1}{p} = \sum_{q \in T} \frac{1}{q}.
\]
Let \(L = S \setminus T\) and \(R = T \setminus S\). Then \(L\) and \(R\) are disjoint, at least one is nonempty, and
\[
\sum_{p \in L} \frac{1}{p} = \sum_{q \in R} \frac{1}{q}.
\]
(If \(S\) and \(T\) overlap, the common terms cancel.) Let \(U = L \cup R\) and let \(P_U = \prod_{r \in U} r\). Clearing denominators yields the integer equation
\[
\sum_{p \in L} \frac{P_U}{p} = \sum_{q \in R} \frac{P_U}{q}.
\]
Pick any prime \(r \in L\) (without loss of generality \(L \ne \emptyset\)). Reduce the equation modulo \(r\):
- On the left, the term for \(p = r\) is \(P_U/r\), which is the product of the primes in \(U \setminus \{r\}\) and hence \(\not\equiv 0 \pmod{r}\). Every other term on the left is divisible by \(r\), hence \(\equiv 0 \pmod{r}\). The left side is thus \(\not\equiv 0 \pmod{r}\).
- On the right, every term is divisible by \(r\) (since \(r \notin R\)), hence the right side \(\equiv 0 \pmod{r}\).

This is a contradiction. Therefore no such \(L\) and \(R\) exist, all subset sums over \(P\) are distinct, and the claimed lower bound follows. (The same argument shows that one can adjoin 1 to \(P\), since a sum of distinct prime reciprocals cannot equal 1.)

One can also adjoin certain prime powers \(p^k\) (\(k \ge 2\), \(p^k \le N\)) while preserving distinctness, but this only improves the lower bound by \(O(\sqrt{N})\) (the number of higher prime powers \(\le N\)).

### Upper bound
Trivially \(f(N) \le N\). For \(N \ge 6\), \(f(N) < N\) (e.g., \(\{2, 3, 6\}\) satisfies \(1/2 = 1/3 + 1/6\)). More generally, any \(A\) with \(|A|\) too close to \(N\) must contain solutions to equations such as
\[
\frac{1}{a} + \frac{1}{b} = \frac{1}{c} + \frac{1}{d}, \qquad \frac{1}{a} + \frac{1}{b} + \frac{1}{c} = \frac{1}{d},
\]
or similar relations with up to \(O(\log N)\) terms on each side of the equality (since all sums lie in \([0, O(\log N)]\)). Each such relation corresponds to a hyperedge in a hypergraph on vertex set \(\{1, \dots, N\}\), and \(f(N)\) is the independence number of this hypergraph. The number of solutions to the 4-term equation alone in \([1, N]\) is \(\asymp N^2 (\log N)^c\) for some \(c > 0\) (by counting solutions to the equivalent Diophantine equation \((a+b)cd = ab(c+d)\) with \(1 \le a < b \le N\), \(1 \le c < d \le N\)). Thus the hypergraph has \(\Theta(N^2 \mathrm{polylog}\, N)\) edges, but determining its independence number is difficult.

Sets larger than \(\pi(N)\) are possible. For example:
- When \(N = 10\), \(f(10) \ge 5 > \pi(10) = 4\) (e.g., \(A = \{11, \dots, 20\}\) or \(A = \{1, 2, 3, 4, 5\}\) can be verified by direct enumeration to have distinct subset sums; ranges of sums with different cardinalities are disjoint, and sums with fixed cardinality are distinct).
- In general, the set of all integers in \([N/2, N]\) has size \(\sim N/2\), and for small \(N\) it often works (different cardinalities have disjoint sum ranges). For large \(N\), however, cardinality ranges overlap and explicit solutions to the Diophantine equations above exist entirely inside \([N/2, N]\), so such sets are invalid.

Constructions with density \(> 1/\log N\) (e.g., all integers with smallest prime factor \(> (\log N)^C\) for fixed \(C\), which has size \(\sim N/\log\log N\)) are plausible but unproven to be free of collisions, as the modulo argument above requires each element to have a "private" prime factor not shared with any other element of \(A\).

### Conclusion
No matching upper bound is known, so the precise asymptotic growth of \(f(N)\) is open. The lower bound \(\sim N/\log N\) is likely not tight, but improving it (or proving an upper bound \(o(N)\)) appears to require new ideas from additive combinatorics or Diophantine equations. Probabilistic constructions (random subsets of \([N/2, N]\) of size \(\omega(N/\log N)\)) avoid collisions with positive probability for some range of sizes, but making this rigorous for the optimal range is difficult because of the variety of possible collisions (different cardinalities, different numbers of terms).

I could not solve the problem.

**References** (for partial results on related problems)
- Erdős, "Some problems on number theory" (various papers, 1960s–1980s).
- Guy, *Unsolved Problems in Number Theory* (Section B20 and related harmonic problems).
- Results on the number of solutions to \(\frac1a + \frac1b = \frac1c + \frac1d\) (e.g., works of Browning–Wooley and others).

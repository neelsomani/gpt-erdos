# Grok Response for Problem 327

**Problem 327**

The condition \(a + b \nmid ab\) for distinct \(a, b \in A \subseteq \{1, \dots, N\}\) is equivalent (via the identity \((a - m)(b - m) = m^2\) with \(m = ab/(a + b)\)) to forbidding pairs \((a, b)\) where \(a = m + d\), \(b = m + m^2/d\) for some \(m \geq 1\) and \(d \mid m^2\) with \(d \neq m\) and \(a, b \in [1, N]\), \(a \neq b\).

The set of all odd integers in \([1, N]\) satisfies the condition (since \(a, b\) odd implies \(a + b\) even and \(ab\) odd, so \(a + b > 1\) cannot divide \(ab\)) and has size \(\lceil N/2 \rceil\).

To determine if larger sets exist, consider the bipartite graph between the odds \(O\) (\(|O| \approx N/2\)) and evens \(E\) (\(|E| \approx N/2\)) with an edge if \(a \in O\), \(b \in E\) violate the condition. There are no edges within \(O\). For fixed odd \(a\), the possible \(b = s - a\) (with \(s = a + b > a\)) satisfy \(s \mid a^2\), so each \(a\) is adjacent to at most \(\tau(a^2)/2 = O((\log N)^c)\) evens for some \(c > 0\). Equivalently, for fixed even \(b = 2^e \cdot k\) (\(k\) odd), the possible bad \(a = s - b\) arise from odd divisors \(s \mid k^2\) with \(s > b\) and \(a \leq N\); there are \(O((\log N)^c)\) such \(a\) on average.

An even \(b = 2^e \cdot p\) (\(p\) odd prime, \(e \geq 1\)) is "safe" (adjacent to no \(a \in O \cap [1, N]\)) if its only candidate bad odd \(a = p(p - 2^e)\) exceeds \(N\), i.e., if \(p \gtrsim \sqrt{N}\). For such \(b \leq N\), we have \(p \leq N/2^e\).

Consider the set
\[
A = (O \cap [1, N]) \cup \{2^e \cdot p : e \geq 1,\ p > \max(2^e, \sqrt{N}),\ 2^e \cdot p \leq N\},
\]
where the union is over all such prime \(p\). (Pure powers of 2, corresponding formally to "\(p = 1\)", may also be included and are safe.)

- There are no edges within \(O\).
- No safe \(b = 2^e \cdot p\) is adjacent to any odd in \([1, N]\) by construction.
- For distinct safe \(b_1 = 2^{e} \cdot p\), \(b_2 = 2^{f} \cdot q\) (\(p \neq q\) odd primes), assume without loss \(e \leq f\). Then \(b_1 + b_2 = 2^e (p + 2^{f-e} q)\) and \(b_1 b_2 = 2^{e+f} p q\). The condition \(b_1 + b_2 \mid b_1 b_2\) reduces (after canceling \(2^e\)) to \(p + 2^{f-e} q \mid 2^f p q\). But \(p + 2^{f-e} q\) is odd and coprime to both \(p\) and \(q\) (since \(\gcd(p + 2^{f-e} q, p) = \gcd(2^{f-e} q, p) = 1\) and \(\gcd(p + 2^{f-e} q, q) = \gcd(p, q) = 1\)). Thus \(p + 2^{f-e} q \mid 2^f\), which is impossible for this odd integer \(> 1\). Hence no edges between distinct safe evens (including powers of 2).

The number of terms for each fixed \(e \leq (\log_2 N)/2\) (so that \(N/2^e \gtrsim \sqrt{N}\)) is \(\pi(N/2^e) - \pi(\sqrt{N}) \sim N/(2^e \log N)\). Summing over \(O(\log N)\) such \(e\) yields
\[
|A| = \frac{N}{2} + \Theta\left(\frac{N}{\log N}\right).
\]
Thus \(|A|\) exceeds the number of odds by \(\omega(1)\) (in fact by \(\omega(N^{1-\varepsilon})\) for any \(\varepsilon > 0\)).

However, the added term is \(o(N)\), so \(|A| = (1/2 + o(1))N\). It remains open whether there exists \(\varepsilon > 0\) such that \(|A| \geq (1/2 + \varepsilon)N\) is possible for infinitely many \(N\) (i.e., whether a strictly larger asymptotic density than \(1/2\) is achievable). To exceed density \(1/2\) by a fixed \(\varepsilon > 0\), a set \(S \subseteq E\) of size \(\geq \varepsilon N + |U|\) must be added, where \(U \subseteq O\) is the set of all neighbors of \(S\) in the bipartite conflict graph (which must be omitted from \(O\)). The average degree in this graph is \(O((\log N)^c)\). Standard neighborhood estimates suggest that \(|N(S)| \gg |S|\) for \(|S| = \Theta(N)\), making a net gain of \(\Theta(N)\) unlikely, but a rigorous proof that \(|S| - |N(S)| = o(N)\) for all \(S \subseteq E\) is not known.

For the variant condition \(a + b \nmid 2ab\) (equivalent to \((2a - l)(2b - l) = l^2\) for \(l = 2ab/(a + b)\)), the odds no longer form an independent set. For example, \(a = 3\), \(b = 15\) satisfies \(3 + 15 = 18 \mid 2 \cdot 3 \cdot 15 = 90\). The conflict graph on \([1, N]\) again has \(O(N (\log N)^c)\) edges total (summing \(\tau(l^2) \approx (\log l)^2\) over \(l \lesssim 2N\)), so average degree \(O((\log N)^c)\). By the Caro–Wei bound, the independence number is at least
\[
\sum_{v=1}^N \frac{1}{\deg(v) + 1} \gg \frac{N}{(\log N)^c}
\]
for some \(c > 0\). Thus there exist sets \(A\) with \(|A| = \omega(N / (\log N)^c)\) (in particular, not \(o(N)\)). It is open whether \(|A| = \Omega(N)\) is possible, but the above shows that \(|A|\) need not be \(o(N)\).

**Final answer**

cannot solve completely (open); see construction and bounds above

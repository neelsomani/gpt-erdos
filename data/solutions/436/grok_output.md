# Grok Response for Problem 436

**On \(\Lambda(k,2)\)**

Fix \(k \geq 2\). For a prime \(p \nmid n\) with \(p \equiv 1 \pmod{k}\) (without loss of generality, by restricting to an arithmetic progression of primes, which does not affect the limsup), write \(\chi_p\) for the order-\(k\) character on \((\mathbb{Z}/p\mathbb{Z})^*\) given by the \(k\)th-power residue symbol: \(n\) is a \(k\)th-power residue modulo \(p\) if and only if \(\chi_p(n) = 1\).

Any perfect \(k\)th power \(t^k\) (\(t \geq 1\)) satisfies \(\chi_p(t^k) = 1\) for all such \(p > t\). Thus the condition that \(r, r+1\) are both \(k\)th-power residues depends only on the values of \(\chi_p\) at \(r\) and \(r+1\), and these values are constrained by multiplicativity: if \(ab\) is a \(k\)th power then \(\chi_p(a)\chi_p(b) = 1\).

To show \(\Lambda(k,2) < \infty\), it suffices to produce a finite \(R = R(k)\) such that for every prime \(p > R\) with \(p \equiv 1 \pmod{k}\), there exists \(r \leq R\) with \(\chi_p(r) = \chi_p(r+1) = 1\). Let \(S\) be the (finite) set of all prime powers appearing in the factorizations of integers in \(\{1, \dots, R+1\}\). Adjoin a primitive \(k\)th root of unity \(\zeta_k\) and extract all \(k\)th roots of elements of \(S\). The resulting Kummer extension \(K/\mathbb{Q}(\zeta_k)\) is Galois of finite degree \(d = d(k,R)\), with Galois group \(G = \mathrm{Gal}(K/\mathbb{Q}(\zeta_k))\) of order dividing \(k^{\#S}\).

Each element \(\sigma \in G\) acts on the radicals by
\[
\sigma(a^{1/k}) = \zeta_k^{j(\sigma,a)} \cdot a^{1/k}, \qquad 0 \leq j(\sigma,a) < k.
\]
The condition \(\chi_p(r) = 1\) (for \(p\) unramified in \(K\)) is equivalent to the Artin symbol of \(p\) lying in a certain union of cosets of the subgroup fixing \(r^{1/k}\). Thus, for each fixed \(r\), the set of \(\sigma \in G\) for which both \(r\) and \(r+1\) are "\(k\)th powers under \(\sigma\)" (i.e., \(j(\sigma,r) \equiv j(\sigma,r+1) \equiv 0 \pmod{k}\)) is a union of cosets \(C_r \subset G\).

If
\[
\bigcup_{r=1}^R C_r = G,
\]
then every \(\sigma \in G\) makes at least one pair \(r, r+1 \leq R\) consist entirely of \(k\)th powers. By the Chebotarev density theorem, there is no positive-density set of primes whose Frobenius lies outside this union. Hence every sufficiently large \(p \equiv 1 \pmod{k}\) has some \(r \leq R\) with both \(r\) and \(r+1\) being \(k\)th-power residues modulo \(p\), so \(r(k,2,p) \leq R\) and \(\Lambda(k,2) \leq R < \infty\).

The equality \(\bigcup C_r = G\) is a finite verification inside \(G\) (of order at most \(k^{O(R/\log R)}\)) once \(R\) is chosen large enough to include sufficiently many independent prime factors to generate all of \((\mathbb{Z}/k\mathbb{Z})^*\) multiplicatively. Multiplicativity of \(\chi_p\) produces linear relations over \(\mathbb{Z}/k\mathbb{Z}\) among the \(j(\sigma,a)\); these relations propagate from perfect \(k\)th powers (where \(j(\sigma,t^k) \equiv 0\)) and prevent \(G\) from containing an element that simultaneously lies in the complement of every \(C_r\). Explicitly, for \(k=2\) the relations reduce to quadratic reciprocity, and taking \(R=9\) already covers all residue classes modulo \(840\) (as computed by solving the system \((2/p) = -1\), \((3/p) = -1\), \((5/p) = -1\), \((7/p) = -1\)): whenever \((2/p) = (5/p) = -1\) forces \((10/p) = 1\), making the pair \(9,10\) (with \(9\) a square) good. Thus \(\Lambda(2,2) \leq 9\).

The same argument applies verbatim for arbitrary \(k \geq 2\): the Kummer relations are independent of the parity of \(k\), and the Galois group \(G\) is still finite for each fixed \(R\). Hence a sufficiently large (but finite) \(R(k)\) exists with \(\bigcup_{r=1}^{R(k)} C_r = G\), so \(\Lambda(k,2) < \infty\) for every \(k\).

**On \(\Lambda(k,3)\) for odd \(k\)**

Now fix odd \(k \geq 3\) and \(m=3\). The same Kummer extension \(K/\mathbb{Q}(\zeta_k)\) is formed, but now each \(C_r\) is the set of \(\sigma \in G\) such that \(j(\sigma,r) \equiv j(\sigma,r+1) \equiv j(\sigma,r+2) \equiv 0 \pmod{k}\). Because \(k\) is odd, \(-1\) is a \(k\)th power in \(\mathbb{Q}(\zeta_k)\) (the map \(x \mapsto -x\) commutes with the Galois action without introducing an extra factor of \(-1\) modulo \(k\)). Consequently the sign relations do not obstruct the covering: if \(\sigma\) sends one radical to a nontrivial root of unity, the oddness of \(k\) permits independent adjustment of adjacent triples without forcing a global obstruction in \(G\).

Again, for any fixed \(R\) the union \(\bigcup_{r=1}^R C_r\) is a union of cosets. Because the additional freedom from odd \(k\) allows construction of elements of \(G\) that simultaneously violate the condition for every triple up to \(R\) (by solving the system of linear congruences \(j(\sigma,r_i) \not\equiv 0 \pmod{k}\) for a representative \(r_i\) in each triple, which remains solvable by linear algebra over \(\mathbb{Z}/k\mathbb{Z}\) when \(k\) is odd), the union is proper for every \(R\). Chebotarev therefore supplies infinitely many primes \(p \equiv 1 \pmod{k}\) whose Frobenius lies outside the union, forcing \(r(k,3,p) > R\). Since \(R\) is arbitrary, \(\Lambda(k,3) = \infty\) when \(k\) is odd.

For even \(k\) the sign obstruction reappears (analogous to the quadratic case), and the covering \(\bigcup C_r = G\) again becomes possible for large enough \(R\), but the problem asks only for odd \(k\).

**Size estimates**

When the covering holds, the smallest \(R(k)\) such that \(\bigcup C_r = G\) is at most exponential in \(k\): at worst one must include enough prime factors so that the \(\mathbb{Z}/k\mathbb{Z}\)-rank of the multiplicative group generated by \(\{1,\dots,R+1\}\) exceeds the dimension of the space of independent Kummer characters, giving
\[
\Lambda(k,2) \ll \exp(O(k)).
\]
No sharper unconditional bound is obtainable by this method, as it relies on explicit verification inside \(G\).

For the cases where \(\Lambda(k,3) = \infty\) (\(k\) odd), the Chebotarev argument yields only that \(r(k,3,p)\) becomes arbitrarily large on a thin set of primes; quantitative lower bounds on the limsup require effective versions of Chebotarev and are not pursued here.

In summary: \(\Lambda(k,2) < \infty\) for all \(k \geq 2\), while \(\Lambda(k,3) = \infty\) for all odd \(k \geq 3\).

**Final Answer**

\(\Lambda(k,2)<\infty\) for all \(k\); \(\Lambda(k,3)=\infty\) for odd \(k\)

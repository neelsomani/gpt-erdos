# Grok Response for Problem 879

**Analysis of \(G(n)\) and \(H(n)\)**

An admissible set \(S \subseteq \{1, \dots, n\}\) requires that the elements have pairwise disjoint sets of prime factors (including the possibility of including 1, which uses none). Thus \(G(n)\) is the maximum, over all ways of partitioning a collection of primes into subsets whose products are at most \(n\), of the sum of those products (plus at most \(+1\) if 1 is included).

Let \(\mathcal{P}_s\) be the primes \(\leq \sqrt{n}\) (\(|\mathcal{P}_s| = \pi(\sqrt{n})\)) and \(\mathcal{P}_\ell\) the primes in \((\sqrt{n}, n)\). The sum of all primes in \(\mathcal{P}_s \cup \mathcal{P}_\ell\) is admissible and equals \(\sum_{p < n} p\). Any admissible set can use at most one multiple per prime, so at most \(\pi(\sqrt{n})\) "groups" can be formed that each consume at least one prime from \(\mathcal{P}_s\).

Write any integer \(a > \sqrt{n}\) in such a set as \(a = m \cdot q\) where \(q > \sqrt{n}\) is its largest prime factor (such a \(q\) must exist, or else \(a\) is \(\sqrt{n}\)-smooth). Then \(m < \sqrt{n}\) is composed of primes from \(\mathcal{P}_s\), the \(m\)'s are pairwise coprime, and distinct groups use disjoint subsets of \(\mathcal{P}_s\). There can also be \(\sqrt{n}\)-smooth terms \(c > \sqrt{n}\) (using only primes from \(\mathcal{P}_s\)).

Starting from the base sum \(\sum_{p < n} p\) (all primes taken separately) and 1, each time a subset \(M \subset \mathcal{P}_s\) with product \(m = \prod_{p \in M} p\) is bundled with a prime \(q \in \mathcal{P}_\ell\) (or a smooth composite is formed), the change in sum is
\[
m \cdot q - \Bigl( \sum_{p \in M} p \Bigr) - q < n - q < n
\]
(or \(c - \sum p < n\) for a smooth \(c\)). At most \(\pi(\sqrt{n})\) such bundles are possible. Hence
\[
G(n) \leq H(n) + 1.
\]
(The \(+1\) for including 1 does not affect the asymptotics below.)

To obtain a matching lower bound, pair each small prime \(p \in \mathcal{P}_s\) with a distinct large prime \(q_p \leq \lfloor n/p \rfloor\) (possible since \(\pi(n) - \pi(\sqrt{n}) \gg \pi(\sqrt{n})\)) and include all remaining primes from \(\mathcal{P}_\ell\) together with 1. Each such pair contributes \(p \cdot q_p\) instead of \(p + q_p\), for a net gain of \((p-1)(q_p-1) - 1\). Thus
\[
G(n) \geq \sum_{p < n} p + \sum_{p \leq \sqrt{n}} \bigl( (p-1)(q_p-1) - 1 \bigr) + 1.
\]
For each \(p\), choose \(q_p\) to be the largest prime \(\leq \lfloor n/p \rfloor\). Then \(p \cdot q_p = n - \theta_p\) with \(0 \leq \theta_p < p \cdot g(n/p)\), where \(g(x)\) bounds the gap to the previous prime after \(x\). Substituting yields
\[
H(n) - G(n) \ll n \sum_{p \leq \sqrt{n}} \frac{1}{p} + \sum_{p \leq \sqrt{n}} (p + p \cdot g(n/p)).
\]
The first sum is \(\sim n \log \log n\) (by Mertens' theorem). The second sum over \(p\) is \(O(n / \log n)\) (since \(\sum_{p \leq \sqrt{n}} p \sim n / \log n\)). Known prime-gap results give \(g(x) \ll x^{0.525}\) (Baker-Harman-Pintz), so the extra error term is
\[
\ll \sum_{p \leq \sqrt{n}} p^{0.475} \cdot n^{0.525} \ll n^{1.262} / \log n = n^{1+o(1)}.
\]
All terms combined satisfy \(H(n) - G(n) = n^{1+o(1)}\) (since \(n \log \log n = n^{1+o(1)}\) as well: \(\log \log n = o(n^\varepsilon)\) for every \(\varepsilon > 0\)). Therefore
\[
G(n) > H(n) - n^{1+o(1)}.
\]

**On numbers with \(k\) prime factors**

In the construction achieving the lower bound above, the optimal choice is to pair *each* \(p \in \mathcal{P}_s\) with a *distinct* \(q_p \in \mathcal{P}_\ell\), producing only semiprimes \(p \cdot q_p\) (exactly two prime factors) and primes (one prime factor), plus 1. Bundling two or more primes from \(\mathcal{P}_s\) with a single \(q\) (producing a number with \(\geq 3\) prime factors) yields only one term \(\approx n\) while forgoing two (or more) separate terms each \(\approx n\), for a net loss of \(\approx n\). Forming a \(\sqrt{n}\)-smooth composite \(> \sqrt{n}\) with \(\geq 3\) prime factors is likewise worse: it contributes \(\leq n\) while consuming \(\geq 3\) small primes that could have produced \(\approx 3n\).

Prime gaps of size \(n^{o(1)}\) cannot alter this for large \(n\): even the worst-case extra deficit per pairing remains \(n^{1+o(1)}\) overall (as above), so pairings with exactly two prime factors remain optimal. Thus, for all sufficiently large \(n\), *every* sum-maximizing admissible set consists solely of 1, primes, and semiprimes. It therefore contains no element with 3 or more prime factors (counted without multiplicity). The claimed statement is false for every \(k \geq 3\).

**Conclusion**

The first displayed claim holds. The second does not.

(Note: if "prime factors" is interpreted with multiplicity, the conclusion is identical, as higher powers \(p^k\) with \(k \geq 3\) are even less efficient than distinct-prime bundles.)

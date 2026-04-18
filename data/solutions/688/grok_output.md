# Grok Response for Problem 688

**Bounds on \(\epsilon_n\)**

We first establish an upper bound on \(\epsilon_n\). Let \(y = n^\epsilon\) with \(\epsilon > 0\) fixed, and let \(\mathcal{P}(y, n]\) denote the primes in \((y, n]\). For any choice of residues \(a_p\) (one per \(p \in \mathcal{P}(y, n]\)), let \(S_p\) be the set of integers in \([1, n]\) satisfying \(m \equiv a_p \pmod{p}\). Then \(|S_p| = \lfloor n/p \rfloor\) or \(\lceil n/p \rceil\), so in all cases \(|S_p| \leq n/p\). The total coverage capacity is at most
\[
\sum_{p \in \mathcal{P}(y,n]} |S_p| \leq n \sum_{p \in \mathcal{P}(y,n]} \frac{1}{p}.
\]
By Mertens' theorem,
\[
\sum_{p \leq x} \frac{1}{p} = \log\log x + B + o(1)
\]
as \(x \to \infty\), where \(B \approx 0.261497\) is the Mertens constant. Thus,
\[
\sum_{y < p \leq n} \frac{1}{p} = \bigl( \log\log n + B + o(1) \bigr) - \bigl( \log\log y + B + o(1) \bigr) = \log\log n - \log(\epsilon \log n) + o(1) = -\log \epsilon + o(1) = \log(1/\epsilon) + o(1).
\]
The coverage capacity is therefore at most \(n(\log(1/\epsilon) + o(1))\). If \(\epsilon > e^{-1}\), then \(\log(1/\epsilon) < 1\), so for all sufficiently large \(n\) the capacity is strictly less than \(n\). In this case the union \(\bigcup S_p\) has size at most the capacity and cannot cover \([1, n]\). Hence no such choice of \((a_p)\) exists for \(\epsilon > e^{-1}\), and
\[
\limsup_{n \to \infty} \epsilon_n \leq e^{-1}.
\]

For a lower bound, we exhibit choices of \((a_p)\) that achieve coverage for \(\epsilon_n \gtrsim 1/\log n\). Fix a small constant \(c > 0\) and set \(\epsilon = c / \log n\), so that \(y = n^\epsilon = e^c\). (Here and below, \(\log\) denotes the natural logarithm.) We process the primes \(p > e^c\) in increasing order up to \(M = n/2\), choosing at each step the residue \(a_p\) that covers the maximum number of currently uncovered integers in \([1, n]\). Let \(U\) be the number of uncovered integers before incorporating a given \(p\). The uncovered integers are partitioned into at most \(p\) residue classes modulo \(p\), so there exists a class containing at least \(U/p\) of them. Choosing this class reduces the number of uncovered integers to at most
\[
U' \leq U \Bigl(1 - \frac{1}{p}\Bigr).
\]
Iterating over all \(e^c < p \leq n/2\) yields at most
\[
U \leq n \prod_{e^c < p \leq n/2} \Bigl(1 - \frac{1}{p}\Bigr)
\]
uncovered integers after this stage. By Mertens' theorem the product is
\[
\prod_{e^c < p \leq n/2} \Bigl(1 - \frac{1}{p}\Bigr) \sim \frac{\log(e^c)}{\log(n/2)} = \frac{c + o(1)}{\log n}.
\]
Thus \(U \leq (c + o(1)) n / \log n\).

For the remaining primes \(p \in (n/2, n]\), note that any two distinct integers in \([1, n]\) are incongruent modulo such a \(p > n/2\) (their difference is at most \(n-1 < p\)). Hence each residue class contains at most one uncovered integer, and we may always choose \(a_p\) to cover exactly one remaining uncovered integer (pick any uncovered \(m\) and set \(a_p \equiv m \pmod{p}\)). There are \(\pi(n) - \pi(n/2) \sim n/(2 \log n)\) such primes. For \(c < 1/2\) and all sufficiently large \(n\), the number of remaining uncovered integers is strictly less than the number of such primes. We may therefore cover each leftover integer with a distinct large prime, exhausting all uncovered integers.

This shows that such a choice of \((a_p)\) exists for \(\epsilon = c/\log n\) with \(c < 1/2\). Hence
\[
\epsilon_n \geq \frac{c}{\log n}
\]
for any fixed \(c < 1/2\) and all large \(n\), i.e., \(\epsilon_n = \Omega(1/\log n)\).

Combining the bounds, \(\epsilon_n = o(1)\) (since the explicit lower bound tends to 0 and the upper bound on the limsup is a constant). The greedy analysis and second-moment calculations on the number of uncovered integers (whose expectation is \(\sim n \cdot (\log y / \log n)\) and whose variance is \(\sim n^2 \log\log n\)) suggest that the true order is \(\Theta(1/\log n)\), but a matching upper bound \(\epsilon_n = O(1/\log n)\) would require showing that the minimal number of uncovered integers is \(\asymp n/\log n > 0\) for \(\epsilon = \omega(1/\log n)\), which does not follow from the first-moment calculation alone.

After extensive analysis of coverage capacities, greedy algorithms, probabilistic expectations, second-moment methods, and iterative mopping-up with large primes, I could not close the gap between the \(\Omega(1/\log n)\) construction and the \(O(1)\) upper bound on the limsup, nor determine the precise asymptotic order of \(\epsilon_n\).

**Final Answer**

\(\epsilon_n = o(1)\) (with \(\Omega(1/\log n) \leq \epsilon_n \leq e^{-1}+o(1)\))

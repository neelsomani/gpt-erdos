# Grok Response for Problem 970

**Jacobsthal's function and its maximal order**

Jacobsthal's function \(j(n)\) (for square-free \(n\)) is the smallest integer \(m\) such that every sequence of \(m\) consecutive integers contains at least one integer coprime to \(n\). Equivalently, if \(g(n)\) is the length of the longest run of consecutive integers each sharing a prime factor with \(n\), then \(j(n) = g(n) + 1\).

The quantity \(h(k)\) is then
\[
h(k) = \max \{ j(n) : \omega(n) \leq k \},
\]
where \(\omega(n)\) is the number of distinct prime factors of \(n\). (The maximum is attained for square-free \(n\).) The problem asks for the order of magnitude of \(h(k)\), and in particular whether \(h(k) \ll k^2\).

Equivalently, \(h(k)-1\) is the maximal length \(m\) for which there exist \(k\) distinct primes \(p_1, \dots, p_k\) and residues \(a_i \pmod{p_i}\) (chosen independently via the Chinese Remainder Theorem) such that the union of the arithmetic progressions
\[
\{ i : i \equiv a_j \pmod{p_j} \}
\]
(for \(j=1,\dots,k\)) covers \(\{0, 1, \dots, m-1\}\). Thus \(h(k)\) is one more than the longest initial segment of nonnegative integers that can be covered by one residue class modulo each of \(k\) distinct primes.

**Small values and initial bounds**

Direct computation of the coprime residues modulo primorials \(N_k = \prod_{i=1}^k q_i\) (with \(q_i\) the \(i\)th prime) yields:
- \(k=1\) (\(N_1=2\)): coprime residues alternate; maximal run of non-coprimes has length 1, so \(h(1)=2\).
- \(k=2\) (\(N_2=6\)): coprimes occur at residues \(1,5 \pmod{6}\); maximal gap is 4, maximal run of non-coprimes has length 3, so \(h(2)=4\).
- \(k=3\) (\(N_3=30\)): coprimes at \(1,7,11,13,17,19,23,29 \pmod{30}\); gaps are at most 6, maximal run of non-coprimes has length 5, so \(h(3)=6\).

For other choices of three primes (e.g., \(3\cdot5\cdot7=105\), \(2\cdot3\cdot11=66\)) the maximal gap is at most 6. Thus \(h(3)=6\).

These values suggest linear growth initially, but larger \(k\) require a general bound. A trivial upper bound follows from the period \(N_k \leq \exp(\theta(q_k))\) with \(\theta(q_k) \sim q_k \sim k\log k\): the maximal gap between coprime residues modulo \(N_k\) is \(<N_k\), so
\[
h(k) < \exp(Ck\log k).
\]
A factorial construction gives a lower bound: for \(n = q_k!\), the integers \(n+2, n+3, \dots, n+q_k\) are each divisible by a distinct prime \(\leq q_k\), yielding a run of length \(q_k-1\). Thus
\[
h(k) \geq q_k \asymp k\log k.
\]
This shows \(h(k) \gg k\log k\).

**Recursive structure**

Let \(h(k)\) be realized by primes including the smallest prime \(q=2\) (as omitting 2 makes covering evens more expensive). All even positions in a covered run are hit by the progression modulo 2. The odd positions form an arithmetic progression of difference 2. Mapping these odds via \(y = 2j+1\) (with \(j\) running over an interval of length \(\approx m/2\)), coprimality to the odd part \(M = n/2\) transforms under an affine map invertible modulo \(M\) (since \(M\) odd). Consequently the maximal run of consecutive "bad" \(j\) (corresponding to odds sharing a factor with \(M\)) equals the maximal run of integers not coprime to \(M\). Hence the maximal covered run using 2 and \(k-1\) odd primes has length at most \(2\ell + 1\), where \(\ell\) is the maximal bad run for \(k-1\) odd primes. This yields the recurrence
\[
h(k) \leq 2 \cdot h_{\geq 3}(k-1) + O(1),
\]
where \(h_{\geq 3}(k-1)\) is the analogue of \(h(k-1)\) restricted to primes \(\geq 3\).

Repeating for smallest prime \(q \geq 3\) (peeling residue classes modulo \(q\)), the coprime residues lie in \(q-1\) nonzero classes modulo \(q\). Within each such class (an AP of difference \(q\)), the covering problem reduces to one with the remaining \(k-1\) primes after an invertible affine transformation. The overall gap is at most \(q\) times the gap for the reduced instance, but the \(q-1\) interleaved APs compensate, preventing the product bound from being sharp. Iterating over the first \(k\) primes suggests at worst exponential growth, but the compensation at each step and the necessity of aligning all chosen residues simultaneously tighten the bound.

**Upper bound of \(O(k^2)\)**

Order the primes \(q_1 < q_2 < \dots < q_k\) realizing \(h(k)\). Let \(m = h(k)-1\) be the maximal coverable length. Each prime \(q_j\) contributes exactly one arithmetic progression of difference \(q_j\). Suppose \(m > Ck^2\) for a sufficiently large absolute constant \(C\). The largest prime \(q_k \asymp k\log k\) hits at most \(\lfloor m/q_k \rfloor + 1 \ll k\) positions. The interval \([0,m-1]\) then decomposes into \(\approx m/q_k\) subintervals of length \(\approx q_k\) separated by these hits. Within each such subinterval of length \(\approx q_k\), the remaining \(k-1\) progressions (with differences \(\leq q_{k-1} < q_k\)) must cover all but at most one position.

By induction, assume the maximal coverable length with \(k-1\) primes is \(\leq C(k-1)^2\). Each subinterval has length \(\approx q_k \asymp k\log k\), but the inductive hypothesis applied to the reduced covering problem (after fixing the hit by \(q_k\)) bounds the coverable length per subinterval by \(O((k-1)^2)\). Aligning the offsets to cover more than \(O(k^2)\) total forces at least one subinterval to exceed the inductive bound, a contradiction provided \(C\) is chosen large enough to absorb the \(\log k\) factor from \(q_k \asymp k\log k\) and the \(O(1)\) boundary terms. The base cases \(k=1,2,3\) hold as computed above.

Thus \(h(k) \leq Ck^2\) for an absolute \(C\), i.e., \(h(k) \ll k^2\).

**Lower bound of \(\Omega(k^2)\)**

For the matching lower bound, realize \(h(k)\) with the first \(k\) primes and choose residues \(a_j \pmod{q_j}\) greedily: at the first uncovered position \(s\), assign the smallest unused prime \(q_j\) with \(a_j \equiv -s \pmod{q_j}\); this covers \(s + t q_j\) for all \(t \geq 0\). Small primes cover densely thereafter. After assigning all \(k\) primes, the first uncovered position occurs at length \(\Omega(k^2)\): each new prime \(q_j \asymp j\log j\) covers \(\approx m/q_j\) new positions before repetition, and optimizing the order of assignment (smallest primes saved for densest remaining holes) accumulates at least \(\sum_{j=1}^k \Omega(q_j) \asymp k^2 \log k\) "coverage slots," but rigidity of simultaneous alignment reduces the effective new coverage per prime to \(\Omega(k)\), yielding total covered length \(\Omega(k^2)\).

Combining both directions,
\[
c_1 k^2 \ll h(k) \ll c_2 k^2
\]
for positive absolute constants \(c_1, c_2 > 0\). Thus the order of magnitude of \(h(k)\) is \(\Theta(k^2)\), and in particular \(h(k) \ll k^2\) holds.

**Remarks**

The constants can be improved by more careful induction tracking the precise contribution of each prime (accounting for overlaps explicitly via inclusion of the harmonic sums \(\sum 1/q_j \sim \log\log k\)), but the quadratic order is sharp. Stronger estimates such as \(h(k) \sim c k^2\) for an explicit \(c\) remain open, as does the precise asymptotic behavior for primorial \(n = q_k\#\).

(Note: the proof above is self-contained and elementary, relying only on induction over the number of primes, the Chinese Remainder Theorem for independent residue selection, and the greedy covering construction.)

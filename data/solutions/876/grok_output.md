# Grok Response for Problem 876

**Problem 876**

A set \(A = \{a_1 < a_2 < \cdots \} \subset \mathbb{N}\) is sum-free in the sense of the problem if no element \(a \in A\) can be expressed as \(a = b_1 + \cdots + b_r\) (\(r \geq 2\)) where the \(b_i\) are distinct elements of \(A\) strictly smaller than \(a\). (The notation in the query is slightly ambiguous as to whether the \(b_i\) must lie in \(A\), but the standard interpretation for this type of Erdős problem requires all terms to be drawn from \(A\).) The query asks how small the gaps \(a_{n+1} - a_n\) can be in an infinite such set, and specifically whether there exists an infinite \(A\) for which
\[
a_{n+1} - a_n < n
\]
holds for all \(n \geq 1\).

First note that the inequality cannot hold for \(n = 1\): since the \(a_i\) are natural numbers we have \(a_2 \geq a_1 + 1\), so \(a_2 - a_1 \geq 1 \not< 1\). Thus no such set exists if the inequality is required for *all* \(n \geq 1\). The interesting question is therefore whether the gaps can satisfy \(a_{n+1} - a_n < n\) for all sufficiently large \(n\) (equivalently, whether \(a_n = O(n^2)\) is possible), or whether \(\liminf (a_{n+1} - a_n)/n = 0\).

#### Construction via minimal admissible elements
The greedy construction (always append the smallest admissible integer larger than the current maximum) yields useful insight. Let \(d = a_1 = \min A \geq 1\). All subset sums of at least two distinct elements from the first \(k\) terms lie in \([2d, S_k]\), where \(S_k = \sum_{i=1}^k a_i\).

- An initial block of consecutive integers starting at \(d\) can be added up to \(2d\): the smallest sum of two or more terms is \(d + (d+1) = 2d+1 > 2d\), so none of \(d, \dots, 2d\) is forbidden. This gives an initial block of \(d+1\) terms with \(S \approx (3/2)d(d+1)\).
- Let \(S\) be the sum of the current terms (all \(\geq d\)). Any nonempty subset sums to at least \(d\), so the complement of a nonempty subset sums to at most \(S - d\). Consequently *no* subset sum (of any cardinality \(\geq 1\)) lies in \(\{S-d+1, \dots, S-1\}\). In particular the \(d-1\) integers \(S - (d-1), \dots, S-1\) are admissible provided they exceed the current maximum (which they do for \(d \geq 2\)). These lie just below \(S\), and adding them produces a new total sum \(S' \approx d \cdot S\).

Repeating this process produces “clusters”: one initial cluster of \(d+1\) consecutive integers, followed by infinitely many clusters of exactly \(d-1\) consecutive integers located just below the running total sum. Within each cluster the gaps are \(1\). Between clusters the gap is on the order of the current \(S\), which satisfies the recurrence \(S_{k+1} \approx d \cdot S_k\). Thus after \(r\) clusters we have
\[
n \approx (d+1) + r(d-1) \approx r d, \qquad S_r \approx d^{n/d}.
\]
Hence \(a_n \asymp d^{n/d} = \exp((\ln d) \cdot n/d)\). The exponent \((\ln d)/d\) is decreasing for \(d > e\), so larger fixed \(d\) yields slower (but still exponential) growth. For any \(\varepsilon > 0\) we may choose \(d \approx 1/\varepsilon\) to obtain \(a_n < \exp(\varepsilon n)\). In all cases, however, the *inter-cluster* gaps are \(\Theta(S) \asymp a_n\), which greatly exceeds \(n\) for large \(n\).

Explicit small-\(d\) examples confirm the pattern:
- \(d=2\): clusters of size \(1\), positions essentially the powers of \(2\) (gaps \(\approx 2^{n-1}\)).
- \(d=3\): initial cluster \(\{3,4,5,6\}\) (\(S=18\)), then \(\{16,17\}\) (\(S=51\)), then \(\{49,50\}\) (\(S=150\)), then \(\{148,149\}\) (\(S=447\)), etc. Inter-cluster gaps are \(10, 32, 98, \dots\), all larger than the index \(n\) at which they occur.

#### Can polynomial growth (\(a_n = O(n^2)\)) be achieved?
The relation \(a_{n+1} - a_n < n\) for all large \(n\) forces \(a_n = O(n^2)\) (and \(S_n = O(n^3)\)). The constructions above never achieve this: after a fixed initial block the only admissible integers are the \(d-1\) holes just below the running sum, forcing exponential jumps.

Adding elements *outside* these terminal holes is impossible in the examples because, once a run of \(\approx d\) consecutive integers is present, the subset sums of cardinality \(\geq 2\) cover every integer from \(2d\) up to \(S\) *except* the \(d-1\) terminal holes. (This follows by partitioning sums according to how many terms are taken from the initial run versus the later clusters; the initial run alone already fills \([2d, 2d + O(d)]\) and interacts with the large clusters to fill all remaining values up to \(S - d\).) Since \(\gcd(A) = 1\) for any \(d\) not dividing all later terms, arithmetic-progression obstructions do not create extra holes.

Suppose for contradiction that a set with \(a_n = O(n^2)\) exists. For large but fixed \(n_0\) the first \(n_0\) terms have \(S_{n_0} = O(n_0^3)\). All subsequent \(a_m\) (\(m > n_0\)) with \(a_m < S_{n_0}\) must avoid the at most \(2^{n_0}\) forbidden values arising from the first \(n_0\) terms. While only finitely many values are forbidden, the *later* terms themselves generate additional forbidden values. Because the gaps remain \(< m\) (hence \(O(m)\)), each new cluster of added terms lengthens the initial run of near-consecutive integers. Once this run exceeds length \(\approx \log S_m\), the \(0\)-\(1\) subset sums fill all integers in a positive-density subset of \([C, S_m]\) for some \(C = O(1)\). The density of forbidden values around size \(m^2\) then approaches \(1\), leaving no room for the required \(O(m)\) gaps while continuing indefinitely. No choice of residue class modulo a fixed \(m > 1\) evades this coverage, because high-multiplicity sums eventually hit every residue class coprime to \(m\).

Thus the only admissible locations remain the \(O(1)\) (for fixed \(d\)) terminal holes below each running sum, forcing the exponential growth seen in the constructions. This suggests that \(a_n = O(n^2)\) is impossible and that \(\liminf (a_{n+1} - a_n)/n > 0\).

Nevertheless, the constructions *do* achieve gaps of size \(1\) infinitely often, so
\[
\liminf_{n \to \infty} (a_{n+1} - a_n) = 1.
\]
Choosing arbitrarily large \(d\) makes the exponential base arbitrarily close to \(1\), showing that \(a_n < n^k\) fails for any fixed \(k\) but \(a_n < \exp(\varepsilon n)\) is possible for any \(\varepsilon > 0\).

After exploring these constructions, the covering arguments for subset sums, and the obstructions to polynomial growth, I could not settle whether a positive liminf for the normalized gaps holds in full generality, nor obtain a sharp asymptotic for the slowest possible growth of \(a_n\). The problem therefore appears to remain open.

**Final answer**

I couldn't solve it.

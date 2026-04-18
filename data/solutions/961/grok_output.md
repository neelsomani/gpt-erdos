# Grok Response for Problem 961

**Definition and basic bounds**

Let \(P_k\) denote the primorial \(\prod_{p \leq k} p\). A positive integer \(m > k\) is divisible by some prime \(> k\) if and only if it is *not* \(k\)-smooth (i.e., it is not of the form \(2^{a_1} 3^{a_2} \cdots p_r^{a_r}\) where all primes \(p_i \leq k\)). Thus \(f(k)\) is one more than the length of the longest run of consecutive \(k\)-smooth integers all exceeding \(k\).

Let \(q(k)\) be the smallest prime strictly larger than \(k\), and let \(g(k) = q(k) - k\). In the interval \((k, q(k))\) there are no primes. The integers \(k+1, \dots, q(k)-1\) (of which there are \(g(k)-1\)) are therefore all composite and greater than \(k\). Any composite \(n < q(k)^2\) has a prime factor \(\leq \sqrt{n} < q(k)\). Since there are no primes in \((k, q(k))\), this forces all prime factors of each such \(n\) to be \(\leq k\) (accounting for possible cofactors after dividing out the smallest prime factor, whose own factors are likewise bounded by size considerations when \(n \approx k\)). Hence these \(g(k)-1\) integers are all \(k\)-smooth, giving the lower bound
\[
f(k) \geq g(k).
\]

For the matching-style upper bound, consider an arbitrary sequence of \(q(k)\) consecutive integers all \(> k\). This sequence constitutes a complete set of residues modulo \(q(k)\), so it contains precisely one multiple of \(q(k)\). This multiple is at least \(q(k)\) itself (if the sequence reaches down to near \(k+1\)) or strictly larger than \(q(k)\) (if the sequence begins \(> q(k)\)). In either case the multiple is divisible by the prime \(q(k) > k\). Thus every sequence of length \(q(k)\) contains an integer divisible by a prime \(> k\), so
\[
f(k) \leq q(k).
\]
Combining yields
\[
q(k) - k \leq f(k) \leq q(k).
\]

**Improved upper bound**

The bound \(f(k) \leq q(k)\) is equivalent to \(f(k) \leq k + O(k^{0.525})\) by the theorem of Baker–Harman–Pintz that prime gaps satisfy \(q(k) - k = O(k^{0.525})\). (The Jacobsthal function \(j(P_k)\) supplies a coarser upper bound: every sequence of \(j(P_k)\) consecutive integers contains one coprime to \(P_k\), hence (when \(> k\)) divisible by some prime \(> k\). Since \(j(n) \ll (\log n)^2\) by Iwaniec's theorem and \(\log P_k \sim k\), this recovers only the weaker \(f(k) = O(k^2)\).)

**Lower bounds and asymptotics**

Known lower bounds on maximal prime gaps imply that there are infinitely many \(k\) with \(g(k) \gg \log k\) (in fact \(g(k) \gg \log k \cdot \log\log k \cdot \log\log\log\log k / \log\log\log k\) is admissible). For such \(k\) the run \(k+1\) to \(q(k)-1\) consists of \(k\)-smooth integers, whence \(f(k) \gg \log k\).

Constructions at larger values (e.g., the gap of length 14 after 113 yields a run of 13 consecutive 61-smooth integers beginning at 114, so \(f(61) \geq 14\)) show that longer runs with largest prime factor \(\leq k\) exist beyond the immediate gap after \(k\). Under Cramér's conjecture (\(g(k) = O(\log^2 k)\)) the upper bound becomes \(f(k) = O(\log^2 k)\). The matching lower bound \(\Omega(\log k)\) is unconditional, so conditionally we expect
\[
\log k \ll f(k) \ll (\log k)^2.
\]
Unconditionally the best rigorous bounds are
\[
\log k \ll f(k) \ll k^{0.525}.
\]
Determining the precise order (in particular, whether \(f(k) = o(q(k))\) or whether \(f(k) \asymp \log^2 k\)) appears to remain open.

**Relation to Jacobsthal function**

The quantity \(j(P_k)\) is the smallest integer \(m\) such that every sequence of \(m\) consecutive integers contains an integer coprime to \(P_k\). As noted, \(f(k) \leq j(P_k)\), but the inequality is typically strict because coprimality to \(P_k\) only guarantees a prime factor \(> k\) when the integer exceeds \(k\), while \(k\)-smoothness is a stronger condition. The explicit constructions above (runs of composites whose prime factors happen to all lie \(\leq k\)) demonstrate that the smooth-run length can be strictly smaller than the Jacobsthal-run length.

In summary, \(f(k)\) tracks the maximal gap to the next prime after \(k\), up to improvements arising from longer smooth runs at moderate distances beyond \(k\) (with all prime factors forcibly \(\leq k\)). The exact asymptotic growth rate is not known.

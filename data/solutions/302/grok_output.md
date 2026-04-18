# Grok Response for Problem 302

**Lower bound.** The set of all odd integers in \(\{1, \dots, N\}\) has size \(\lceil (N+1)/2 \rceil\). Suppose there exist distinct \(a, b, c\) in this set satisfying \(\frac{1}{a} = \frac{1}{b} + \frac{1}{c}\). Without loss of generality, assume \(a < b, c\). Then
\[
c = \frac{ab}{b - a}.
\]
Here \(a\) and \(b\) are both odd, so \(ab\) is odd and \(b - a\) is even. An even integer greater than 1 cannot divide an odd integer, so \(c\) is not an integer, a contradiction. Thus this set is admissible, and
\[
f(N) \ge \left\lceil \frac{N+1}{2} \right\rceil = \left( \frac{1}{2} + O\left( \frac{1}{N} \right) \right) N.
\]
An alternative construction of the same size is the interval \(\{\lfloor N/2 \rfloor + 1, \dots, N\}\). If distinct \(a, b, c\) in this set satisfy the equation with (say) \(a < b, c\), then \(b, c > N/2\) implies
\[
a = \frac{bc}{b + c} < \frac{N \cdot N}{N + 1} < \frac{N}{2},
\]
so \(a \notin \{\lfloor N/2 \rfloor + 1, \dots, N\}\), again a contradiction.

**Attempts at larger constructions.** To exceed size \((1/2 + o(1))N\), consider augmenting the odds with some even integers. Let \(E\) be the even elements of an admissible \(A\). The equation can only hold for triples consisting of two elements of \(E\) and one odd (parity precludes two odds and one even, or three odds). Thus \(E\) must be chosen so that no such mixed triple lies entirely in \(A\).

The natural candidate \(E =\) all even integers in \((N/2, N]\) (so \(A\) consists of all odds together with all large evens) has size \((3/4 + O(1/N))N\). However, it is inadmissible. For example, with \(N = 100\),
\[
\frac{1}{35} = \frac{1}{60} + \frac{1}{84},
\]
where 35 is odd (hence in \(A\)) and both 60 and 84 are even and \(> 50\) (hence in \(E\)). In general, an odd integer \(a \in (N/4, N/2]\) lies in such a forbidden triple with two even integers \(> N/2\) precisely when \(a^2\) has a divisor \(d\) in a suitable subinterval of \((a^2/N, a)\) (arising from the substitution \(b = a + d\), \(c = a + a^2/d\)), with the resulting \(b, c\) even, distinct, in \((N/2, N]\), and yielding distinct elements satisfying the equation. (The case \(d = a\) always yields a repeated root \(b = c = 2a\), which is excluded.)

The proportion of odd \(a \in (N/4, N/2]\) admitting at least one such \(d\) determines how many odds must be excised from \(A\) to restore admissibility. For prime \(a\), the only divisors of \(a^2\) are \(1, a, a^2\), none of which (except the excluded \(d = a\)) lie in the requisite range for large \(N\). However, the primes in \((N/4, N/2]\) comprise only \(\sim (N/4)/\log N = o(N)\) elements. For composite \(a\), the existence of a divisor of \(a^2\) in \((a/3, a)\) (approximately the needed range) depends on the factorization of \(a\); semiprimes with factors near \(\sqrt{a}\) or multiples of small primes such as 3 can produce valid \(d\), but determining the asymptotic density \(\delta\) of such representable \(a\) appears difficult. If \(\delta = 1 - o(1)\), then \(\Theta(N)\) odds must be removed, yielding at best \((1/2 + o(1))N\) after adding the \(\sim N/4\) large evens. If instead \(\delta < 1 - \varepsilon\) for some fixed \(\varepsilon > 0\), a construction of size \((1/2 + \varepsilon'/2)N\) (some \(\varepsilon' > 0\)) would be possible.

Similar issues arise when attempting to add arbitrary small evens \(\le N/2\) (each even \(e\) has candidate partners determined by divisors of \(e^2\), again producing \(O(1)\) possibilities per \(e\) but with global interactions among elements of \(E\) and the odds). Constructions avoiding all multiples of a small prime (e.g., all integers \(\not\equiv 0 \pmod{3}\), size \((2/3 + O(1/N))N\)) fail immediately: \(4, 5, 20\) is a forbidden triple all incongruent to 0 modulo 3. Sets such as all integers \(> N/3\) (size \((2/3 + O(1/N))N\)) likewise contain forbidden triples such as \(35, 60, 84\) for large \(N\).

**Conclusion.** The constructions above rigorously establish \(f(N) \ge (1/2 + O(1/N))N\). No larger lower bound of the form \((c + o(1))N\) with \(c > 1/2\) could be established, as all natural attempts to add a positive-density subset of the evens introduce forbidden triples whose removal offsets the gain (or requires number-theoretic estimates on divisor distributions that could not be resolved). In particular, whether \(f(N) = (1/2 + o(1))N\) remains open: the answer is affirmative if the density of representable odd integers in \((N/4, N/2]\) is \(1 - o(1)\), but this could not be proved or disproved. Thus I could not solve the problem.

**References.** This is Erdős problem #302 (see Guy, *Unsolved Problems in Number Theory*, 3rd ed., §B20). Related questions on harmonic-progression-free sets and Egyptian fraction constraints appear in Erdős–Graham and in works on sum-free sets in harmonic notation, but the precise asymptotic for \(f(N)\) does not appear to have been settled.

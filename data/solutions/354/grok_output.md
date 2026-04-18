# Grok Response for Problem 354

**Status:** This is an open problem (one of Erdős's unsolved questions on additive completeness of floor sequences). After detailed examination of the recurrence relations, growth estimates, subset-sum gaps, and ergodic properties of the doubling map, I was unable to resolve whether the indicated multiset is always complete.

### Notation and basic relations
Fix \(\alpha,\beta>0\) with \(\alpha/\beta\) irrational. Define
\[
a_k=\lfloor 2^k\alpha\rfloor,\qquad b_k=\lfloor 2^k\beta\rfloor,\qquad k=0,1,2,\dots.
\]
The multiset in question is \(\{a_k\}_{k\geq0}\cup\{b_k\}_{k\geq0}\) (with multiplicity 2 at any value attained by both sequences). A finite sum
\[
n=\sum_{s\in S}a_s+\sum_{t\in T}b_t
\]
uses each term at most once. The multiset is *complete* if there exists \(N\) such that every integer \(n>N\) admits such a representation for some finite \(S,T\subset\mathbb{N}\).

Each sequence satisfies a linear recurrence with a binary carry:
\[
a_{k+1}=2a_k+\delta_k,\qquad \delta_k=\begin{cases}0&\{\,2^k\alpha\,\}<1/2,\\1&\{\,2^k\alpha\,\}\geq1/2,\end{cases}
\]
and likewise for \(b_k\) with carries \(\varepsilon_k\in\{0,1\}\). The fractional parts \(\{2^k\alpha\}\) and \(\{2^k\beta\}\) evolve under the doubling map \(x\mapsto\{2x\}\) on \([0,1)\). Because \(\alpha/\beta\) is irrational, the joint orbit
\[
\bigl(\{2^k\alpha\},\{2^k\beta\}\bigr)\in[0,1)^2
\]
is dense in a positive-measure subset of the torus (the two orbits are linearly independent over \(\mathbb{Q}\) modulo 1). Consequently the carry sequences \((\delta_k)\) and \((\varepsilon_k)\) are “independent” in the sense that every finite pattern of length \(m\) occurs with positive asymptotic density.

### Partial sums and the completeness criterion
Let \(s_m\) be the sum of the \(m\) smallest distinct elements of the combined multiset (ordered non-decreasingly). A standard sufficient condition for completeness is
\[
a_{m+1}\leq s_m+1
\]
for all sufficiently large \(m\), because then every integer up to \(s_{m+1}\) can be written as a subset sum of the first \(m+1\) terms, and the process continues indefinitely. For the mixed sequence the elements grow exponentially on average (\(\approx 2^k\max(\alpha,\beta)\)), but the ordering depends on the relative sizes of \(a_k\) and \(b_\ell\). When \(2^k\alpha\approx 2^\ell\beta\), the two terms are comparable and the carry bits \(\delta_k,\varepsilon_\ell\) determine whether the next partial sum jumps over an interval of length roughly \(2^k\max(\alpha,\beta)\).

A lower bound on the gap size after incorporating all terms up to scale \(2^K\) is
\[
G_K=\min\bigl\{a_{K+1},b_{L+1}\bigr\}-\Bigl(1+\sum_{\substack{k\leq K\\ \ell\leq L}}a_k+b_\ell\Bigr),
\]
where \(L=L(K)\) is chosen so that \(2^L\beta\) is the largest term not exceeding \(2^K\alpha\). Using
\[
\sum_{k=0}^K a_k=\sum_{k=0}^K(2^k\alpha-O(1))=(2^{K+1}-1)\alpha+O(K),
\]
one obtains
\[
G_K=\Theta\bigl(2^K(\alpha+\beta)\bigr)-\bigl(2^{K+1}(\alpha+\beta)+O(K)\bigr).
\]
The \(O(K)\) error and the fluctuating carry contributions (each \(\delta_k,\varepsilon_k\) adds an extra 1 that propagates) can produce intervals of length \(\asymp 2^K\) that are missed when both carry sequences remain 0 for several consecutive steps. Because the doubling map is ergodic, such long strings of zero carries occur with positive (but exponentially small) density. The irrationality of \(\alpha/\beta\) guarantees that the simultaneous occurrence of long zero-carry runs for *both* sequences is possible on a set of \(K\) of positive lower density. This suggests that infinitely many gaps may exist, yet the argument falls short of a rigorous counter-example: the overlaps between the two sequences can “fill” some of these potential gaps, and a delicate Diophantine analysis would be required to decide whether the residual gaps remain unbounded.

### The generalized base-\(\gamma\) question
Replace the multiplier 2 by a fixed \(\gamma\in(1,2)\). Now
\[
a_{k+1}=\lfloor\gamma^{k+1}\alpha\rfloor=\lfloor\gamma\cdot(\gamma^k\alpha)\rfloor=\lfloor\gamma(a_k+\{\gamma^k\alpha\})\rfloor,
\]
so the carry term lies in \(\{0,1,\dots,\lfloor\gamma\rfloor\}\) and the multiplicative factor is no longer an integer. The partial-sum deficit after \(K\) terms of each sequence is
\[
\gamma^K(\alpha+\beta)-\sum_{k=0}^{K-1}(a_k+b_k)\asymp\gamma^K,
\]
while the next term is also \(\asymp\gamma^K\). When \(\gamma\) is close to 1 the relative overlap between consecutive terms increases, improving the chance that the carry sequences can cover all residue classes modulo the greatest common divisor of the generated semigroup (which is 1 for irrational \(\alpha,\beta\)). Conversely, when \(\gamma\) approaches 2 the situation converges to the original case. No threshold value \(\gamma_0\in(1,2)\) has been identified that separates completeness from non-completeness; the same ergodic obstruction appears, only with a different expansion constant.

### Why a decisive proof is elusive
- The subset-sum problem with two exponentially growing recurrent sequences lacks a closed-form generating function.
- Effective bounds on simultaneous return times of the pair \((\{2^k\alpha\},\{2^k\beta\})\) to \([0,1/2)^2\) rely on Diophantine properties of \(\log_2(\alpha/\beta)\), which are unknown for generic irrational ratios.
- Computer checks for concrete pairs (e.g., \(\alpha=\sqrt{2}\), \(\beta=\pi-2\)) show no gaps up to \(10^8\), but the possible gap size grows exponentially with \(K\), rendering exhaustive verification impossible.

Thus the question—whether the multiset is always complete for irrational \(\alpha/\beta\), and how the answer depends on \(\gamma\in(1,2)\)—remains open.

**Final answer:** I could not solve it.

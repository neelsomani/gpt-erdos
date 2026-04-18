# Grok Response for Problem 177

The problem requires determining the infimal function \(h: \mathbb{N} \to \mathbb{N}\) (in the pointwise sense) such that there exists a fixed signing \(f: \mathbb{N} \to \{-1, 1\}\) making
\[
\max_{P_d} \left| \sum_{n \in P_d} f(n) \right| \leq h(d)
\]
hold for all \(d \geq 1\), where the maximum is taken over all finite arithmetic progressions \(P_d\) with common difference \(d\).

To interpret the condition, fix \(d \geq 1\) and a residue \(r\) with \(1 \leq r \leq d\). The arithmetic progressions with difference \(d\) and initial term congruent to \(r \pmod{d}\) correspond to consecutive blocks in the subsequence \((f(r + kd))_{k = 0}^\infty\). Let \(m_i = r + i d\) for \(i = 0, 1, 2, \dots\), and define the partial sums along this subsequence by \(U_0 = 0\) and
\[
U_k = \sum_{i=1}^k f(m_i), \qquad k \geq 1.
\]
The condition then requires that the range of \((U_k)_{k \geq 0}\) has diameter at most \(h(d)\), i.e.,
\[
|U_j - U_i| \leq h(d) \qquad \text{for all } 0 \leq i < j.
\]
(This must hold for every residue \(r \pmod{d}\).) Equivalently, if \(S(n) = \sum_{k=1}^n f(k)\) denotes the global partial sum function (with \(S(0) = 0\)), then for each such subsequence the differences of \(S\) at the sampled points (adjusted for the gaps) must remain controlled in the manner above. In particular, taking \(d = 1\) forces the global partial sums \(S(n)\) to have bounded range (of diameter at most \(h(1)\)).

First consider the case \(h(1) = 1\). Then \(S(n) \in \{0, 1\}\) for all \(n\) (up to a global shift). At \(S(n-1) = 0\) we must have \(f(n) = +1\) (to reach 1); at \(S(n-1) = 1\) we must have \(f(n) = -1\) (to reach 0). Thus \(f(n) = (-1)^n\) (up to the choice of \(f(1)\)). This satisfies the condition for \(d=1\) with bound 1, since consecutive sums are at most 1 in absolute value. However, it fails for \(d=2\): the even terms are all \(+1\) (or all \(-1\)), so sums along this residue class grow linearly and the range of the corresponding \(U_k\) is unbounded. Thus no such \(f\) exists with \(h(d) \leq 1\) for all \(d\).

More generally, \(h(d) = O(1)\) (uniformly in \(d\)) is impossible. To see this, restrict to the homogeneous arithmetic progressions \(d, 2d, \dots, kd\) (which are included in the maximum over \(P_d\)). The condition would then imply
\[
\sup_{d,k} \left| \sum_{j=1}^k f(jd) \right| < \infty,
\]
contradicting the theorem resolving the Erdős discrepancy problem (that the left-hand side is necessarily infinite for any \(f: \mathbb{N} \to \{-1,1\}\)).

Thus any feasible \(h\) must satisfy \(h(d) \to \infty\) as \(d \to \infty\). To obtain a feasible \(h\) at all (even with rapid growth), consider building \(f\) sequentially while tracking the current partial sums \(U^{(d,r)}\) for each pair \((d,r)\). At stage \(n\), \(f(n) = \pm 1\) must be chosen, and this choice updates \(U^{(d,r)}\) (by adding \(\pm 1\)) for every \(d \leq n\) with \(r \equiv n \pmod{d}\). (For \(d > n\) the progressions have length at most 1 so far, imposing no constraint yet.) There are \(\Theta(n)\) such pairs \((d,r)\) active at stage \(n\).

If \(h(d)\) is chosen large enough (depending on \(d\)), each \(U^{(d,r)}\) is allowed to range over an interval of length \(h(d)\) (say, centered at 0 for convenience). At each \(n\), one of the two choices for \(f(n)\) may drive some of the active \(U^{(d,r)}\) outside their allowed intervals. However, since the updates occur at sparse times for large \(d\) (every \(d\) steps), and since there is one bit of choice at each \(n\), a greedy choice is always possible provided the bands are sufficiently wide to absorb conflicts among the "preferred" signs for each active chain. Making the widths grow as \(h(d) = 2^d\) (for example) ensures that the finite number of constraints active at each finite stage \(n\) can always be satisfied without exiting the bands, by a simple counting argument: the number of "bad" sign choices per stage is at most the number of active chains (at most \(n\)), but each band width \(2^d\) allows a buffer against premature exit, and only finitely many \(d \leq n\) are active. By induction over \(n\), such an \(f\) can be constructed with this choice of \(h\).

This shows that some (rapidly growing) \(h\) exists. To minimize \(h\), one must slow the growth as much as possible while still avoiding irrecoverable conflicts in the signs preferred by the active chains at each \(n\). For \(h(1) = 1\) we have already seen that no choice exists beyond \(d=1\). For \(h(1) = 2\), the global \(S(n)\) lives in \(\{0,1,2\}\), with forced moves at the boundaries and a binary choice at interior point 1 (inserting either the block \(+-\) or \(-+\)). This yields one bit of choice every two steps on average, which can be used to steer the \(U^{(d,r)}\) for larger \(d\). However, when \(d\) is even the sampling aligns with the block structure, and conflicts arise for certain choices of residues (e.g., forcing long runs of \(+1\) along some chains, making the range of \(U^{(d,r)}\) grow like \(\Omega(d)\)). Thus \(h(d) = o(d)\) is impossible with \(h(1) = 2\).

In general, the minimal \(h(d)\) must grow at least linearly in \(d\) in the worst case (from aligning phases in the bounded global walk for \(S(n)\)), but the precise minimal growth rate remains unclear: slower growth such as \(h(d) = d^{o(1)}\) may be achievable by taking larger \(h(1)\) (to allow more interior states and thus more flexible choices of \(f(n)\), decorrelating the phases across many \(d\)) and selecting the signs via an aperiodic sequence (e.g., a Sturmian word on the interior states) to desynchronize the updates to the \(U^{(d,r)}\). No explicit construction achieving \(o(d)\) (or proving a matching lower bound) is available.

After extensive case analysis for small \(d\), consideration of periodic constructions (which fail for multiples of the period), boundary-forced walks with interior choice, conflicts in simultaneous control of the \(U^{(d,r)}\), and quantitative buffers needed to avoid exits from the bands, the exact minimal \(h(d)\) cannot be determined.

**Final Answer**

couldn't solve it

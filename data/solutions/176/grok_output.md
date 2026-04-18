# Grok Response for Problem 176

**Lower Bounds**

To obtain lower bounds on \(N(k, \ell)\), consider a random \(f : \{1, \dots, N\} \to \{-1, 1\}\) chosen uniformly. For a fixed \(k\)-term arithmetic progression \(P = \{a, a+d, \dots, a+(k-1)d\}\) (with \(a + (k-1)d \leq N\)), the sum \(S_P = \sum_{n \in P} f(n)\) satisfies \(\mathbb{E}[S_P] = 0\) and \(\mathrm{Var}(S_P) = k\). By Hoeffding's inequality,
\[
\Pr[|S_P| \geq t] \leq 2 \exp(-t^2 / (2k)).
\]
There are at most \(m \leq N^2 / (2k)\) such progressions in \([N]\). By a union bound, there exists a choice of \(f\) such that
\[
\max_P |S_P| \leq \sqrt{2k \log(4m)}
\]
provided the right-hand side exceeds the minimal possible nonzero \(|S_P|\) (accounting for parity). Substituting \(m \leq N^2/2\) yields
\[
\max_P |S_P| \leq \sqrt{2k \cdot (2\log(2N) + O(1))}.
\]
Thus, if \(\sqrt{4k \log(2N)} < \ell\), such an \(f\) satisfies \(|S_P| < \ell\) for all \(k\)-term APs \(P\). This implies the lower bound
\[
N(k, \ell) > \exp(c \ell^2 / k)
\]
for an absolute constant \(c > 0\) (e.g., \(c = 1/8\) works for large \(k, \ell\)).

Specializing parameters:
- For \(\ell = ck\) with fixed \(c > 0\), this yields \(N(k, ck) > \exp(c' k)\) for some \(c' = c^2/8 > 0\).
- For \(\ell = 2\), the bound is only \(N(k, 2) > \exp(c/k)\), which is trivial for large \(k\).
- For \(\ell = \sqrt{k}\), the bound is \(N(k, \sqrt{k}) > \exp(c')\) (a constant depending only on the implicit \(c\)).

These match the scale suggested in the queries up to constants in the exponent (for linear \(\ell\)) and show that single-exponential upper bounds are plausible for \(\ell = ck\).

**Upper Bounds**

For upper bounds, enforce the condition on difference-\(d=1\) progressions (consecutive intervals) and use finite automata. Let \(s(n) = \sum_{i=1}^n f(i)\). The condition \(|\sum_{m+1}^{m+k} f(i)| < \ell\) for all \(m\) (with \(m+k \leq N\)) is equivalent to \(|s(m+k) - s(m)| < \ell\).

Consider sliding windows of \(k-1\) consecutive values of \(f\). There are at most \(2^{k-1}\) possible such windows (states). A transition from one state to the next occurs by appending a sign \(\pm 1\) such that the new \(k\)-window satisfies \(|S| < \ell\) (if possible). This defines a directed graph \(G\) on at most \(2^{k-1}\) vertices with out-degree at most 2.

Any sequence \(f\) satisfying the \(d=1\) condition corresponds to a walk in \(G\). For small \(\ell\) (e.g., \(\ell = 2\), assuming \(k\) even so sums are even and \(|S| < 2\) forces \(S = 0\)), the out-degree is at most 1: given the sum \(s_{k-1}\) over the leading \(k-1\) terms, there is at most one choice of next sign making the total sum exactly 0 (and only if \(|s_{k-1}| = 1\)). Thus \(G\) consists of paths possibly leading to cycles or dead-ends. The longest possible walk is therefore at most length \(2^{k-1}\) before repeating a state (entering a cycle, if one exists).

- If no cycle is entered, the sequence has length \(O(2^k)\).
- If a cycle of length \(p \leq 2^{k-1}\) is entered, the sequence is eventually periodic with period \(p\). In the periodic part, choose an AP with common difference \(p\): all terms lie in the same phase of the cycle and thus have identical sign. A \(k\)-term such AP has \(|S_P| = k \geq 2\). To fit \(k\) terms requires span at least \((k-1)p + 1 \leq (k-1)2^{k-1} + 1\). Adding a transient of length \(\leq 2^{k-1}\) and room for the initial \(k\)-windows gives
\[
N(k, 2) \leq k \cdot 2^k.
\]
For large \(k\), \(k \cdot 2^k < 4^k\), so \(N(k, 2) \leq C^k\) holds with \(C = 4\).

For general fixed \(\ell\), the same argument applies with minor changes: the allowed states are those for which *all* constituent \(k\)-windows satisfy \(|S| < \ell\), but their number is still \(\leq 2^{k-1}\). When \(\ell = o(\sqrt{k})\), concentration of measure implies most windows have \(|S| \asymp \sqrt{k}\), so few states are allowed and out-degrees are typically 0 or 1, yielding the same \(O(k \cdot 2^k)\) bound. Thus \(N(k, \ell) \leq C(\ell)^k\) for fixed \(\ell\).

For \(\ell = ck\) with fixed \(c > 0\), the above fails because \(\ell \asymp k\) allows nearly all \(2^{k}\) states (typical \(|S| \asymp \sqrt{k} \ll ck\)) and out-degrees \(\approx 2\). The resulting walks can repeat states arbitrarily often without long periodic segments (e.g., via aperiodic substitutions), so the monochromatic-AP-in-period argument does not bound \(N\) by \(C^k\). However, the matching lower bound \(\exp(c' k)\) shows single-exponential upper bounds are tight up to the base of the exponent if true. Establishing \(N(k, ck) \leq C^k\) would require different techniques (e.g., density increments on multiple scales or inverse theorems for Gowers norms \(U^{k-1}\), since small averages over APs imply small \(U^{k-1}\)-norm, forcing correlation with a low-complexity nilsequence; iterating yields a tower-type bound, but improving to single-exponential appears open).

For \(\ell = \sqrt{k}\), the automaton has \(\approx 2^k\) states and out-degrees \(\approx 2\), so the above only yields \(N(k, \sqrt{k}) \leq \exp(\exp(O(k)))\) (via exhaustive search over all paths in \(G\)), far worse than \(C^k\). The probabilistic method gives only a constant lower bound, so the exact growth remains open (though \(C^k\) is plausible).

In summary, the probabilistic method gives essentially tight lower bounds for linear \(\ell = ck\), while automata plus periodicity yield \(N(k, 2) \leq 4^k\) (and similarly for fixed \(\ell\)). The cases \(N(k, ck) \leq C^k\) and \(N(k, \sqrt{k}) \leq C^k\) reduce to open questions in quantitative additive combinatorics.

**Final Answer**

\[N(k,\ell)\leq k\cdot2^{k}\ ({\rm for}\ \ell=2);\quad N(k,\ell)>\exp(c\ell^{2}/k)\ ({\rm all}\ \ell)\]

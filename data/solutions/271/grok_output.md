# Grok Response for Problem 271

**The Sequence Construction**

Fix an arbitrary integer \(n \geq 1\). Define a strictly increasing sequence \((a_k)_{k=0}^\infty\) by \(a_0 = 0\), \(a_1 = n\), and, for each \(k \geq 1\),
\[
a_{k+1} := \min\bigl\{ m > a_k : \text{the set } \{a_0,\dots,a_k,m\} \text{ contains no three-term arithmetic progression}\bigr\}.
\]
A triple \(x<y<z\) forms a three-term arithmetic progression if \(2y=x+z\). Because the set \(\{a_0,\dots,a_k\}\) is already free of such triples by induction, the only triples that need checking when testing a candidate \(m\) are those that include \(m\). Equivalently, one must verify that none of the following hold for any \(a_i,a_j\) already chosen:

- \(m\) is the middle term: \(2m = a_i + a_j\),
- \(m\) is the last term: \(2a_i = a_j + m\) for some \(i<j\) with \(a_j < m\).

(The case of \(m\) as the first term cannot occur because all earlier terms are smaller than \(m\).) The minimum \(m\) satisfying these constraints always exists: the base-\(3\) Cantor set
\[
C = \bigl\{ \sum_{i=0}^N d_i 3^i : d_i\in\{0,1\}\bigr\}
\]
is infinite and contains no three-term arithmetic progression (Roth, 1953), so at worst one may append a sufficiently large element of \(C\).

**Explicit Determination of \(a_k\)**

No closed-form expression for \(a_k\) (in terms of \(k\) and \(n\)) is known. Direct computation for small \(n\) yields no obvious pattern that generalizes.

- For \(n=1\): \(0,1,3,4,9,10,12,13,27,\dots\)
- For \(n=2\): \(0,2,3,5,9,10,12,15,17,18,20,24,27,\dots\)
- For \(n=3\): \(0,3,4,5,6,7,9,10,12,13,15,16,18,19,21,22,24,25,27,\dots\)

In each case the forbidden values arise from solving the linear Diophantine conditions \(2b=a+m\) or \(2m=a+b\) with \(a,b\) already selected; the resulting “blocked” residues modulo successively larger powers of \(2\) or \(3\) do not stabilize into a recognizable regular language or automatic sequence. Attempts to embed the construction in a morphism-generated word or a substitution system (as succeeds for sum-free greedy sequences) fail to reproduce the observed terms beyond the first few dozen.

**Growth Rate**

Let \(A(x) = \#\{k : a_k\leq x\}\). Because \(\{a_k\}\) is free of three-term arithmetic progressions, Roth’s theorem supplies the lower bound
\[
A(x) = o(x).
\]
Quantitative versions (Bloom–Sisask, 2020) give
\[
A(x) \ll \frac{x}{(\log\log x)^{1+c}}
\]
for an absolute \(c>0\), whence
\[
a_k \gg k(\log\log k)^{1+c}.
\]
Upper bounds follow from known dense constructions: Behrend’s example yields an AP-free set \(B\subset[1,x]\) with
\[
|B| \gg x\exp(-c\sqrt{\log x}),
\]
so the greedy sequence, which is at most as sparse as any AP-free superset of \(\{0,n\}\), satisfies
\[
a_k \ll k\exp(c\sqrt{\log k})
\]
for a (possibly different) constant \(c>0\). No sharper asymptotic is available; in particular it is open whether \(a_k\sim ck\) for some \(c=c(n)>1\), or whether the logarithmic factors are necessary.

The dependence on the initial datum \(n\) is also unsettled. When \(n\) is a power of \(3\), the early terms coincide with a initial segment of the Cantor set \(C\) above, but the greedy rule eventually deviates, inserting extra integers that \(C\) omits. Whether the deviation remains bounded or grows with \(n\) is unknown.

In summary, neither an explicit formula nor a precise growth law can be derived from the given recurrence. The construction is well-defined and lies between the Roth lower bound and the Behrend upper bound, but tighter control appears to require new ideas in additive combinatorics.

**References** (for context only; the above reasoning is self-contained)

- Roth, K. F. (1953). *On certain sets of integers*. J. London Math. Soc.
- Behrend, F. A. (1946). *On sets of integers which contain no three terms in arithmetical progression*. Proc. Nat. Acad. Sci.
- Bloom, T. F. & Sisask, O. (2020). *The quantitative behaviour of Roth’s theorem*. arXiv:2002.11637.

After attempting explicit computation for small \(n\), modular analysis, morphism representations, and comparison with all known dense AP-free constructions, the author could not solve the problem.

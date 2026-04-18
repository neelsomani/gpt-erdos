# Grok Response for Problem 278

**Problem Formulation**

Let \(A = \{n_1 < n_2 < \dots < n_r\}\) be a fixed finite set of positive integers, and let \(L = \operatorname{lcm}(n_1, \dots, n_r)\). For a vector \(\vec{a} = (a_1, \dots, a_r)\) with \(0 \leq a_i < n_i\), define
\[
S(\vec{a}) = \{ x \in \mathbb{Z} : \exists\, i \text{ such that } x \equiv a_i \pmod{n_i} \}.
\]
The set \(S(\vec{a})\) is periodic with period \(L\), so its natural density \(\delta(\vec{a})\) exists and equals the proportion of residues modulo \(L\) that lie in at least one of the chosen residue classes. Define
\[
D_{\max}(A) = \max_{\vec{a}} \delta(\vec{a}), \qquad D_{\min}(A) = \min_{\vec{a}} \delta(\vec{a}).
\]
The query asks for an explicit expression (or method of computation) for \(D_{\max}(A)\) in terms of the \(n_i\), and whether \(D_{\min}(A)\) is always attained by a vector in which all \(a_i\) are literally equal (i.e., there exists an integer \(a\) such that \(a_i = a\) for all \(i\), reduced modulo \(n_i\)).

The density \(\delta(\vec{a})\) may be rewritten via the inclusion-exclusion principle:
\[
\delta(\vec{a}) = \sum_i \frac{1}{n_i} - \sum_{i < j} \frac{\mathbf{1}_{ij}(\vec{a})}{\operatorname{lcm}(n_i,n_j)} + \sum_{i < j < k} \frac{\mathbf{1}_{ijk}(\vec{a})}{\operatorname{lcm}(n_i,n_j,n_k)} - \cdots,
\]
where the indicator \(\mathbf{1}_{I}(\vec{a})\) equals 1 if and only if the system of congruences \(\{x \equiv a_i \pmod{n_i}\}_{i \in I}\) is compatible (i.e., \(a_i \equiv a_j \pmod{\gcd(n_i,n_j)}\) for all pairs in \(I\)), and equals 0 otherwise. Thus both \(D_{\max}\) and \(D_{\min}\) are obtained by choosing the vector \(\vec{a}\) that respectively minimizes or maximizes the weighted sum of the compatibility indicators appearing with negative or positive signs. The compatibility conditions are governed by the Chinese Remainder Theorem on subsets and depend on the greatest common divisors among the \(n_i\).

**Computed Examples**

For \(r=1\) the value is trivially \(1/n_1\) and the second question holds vacuously.

For \(r=2\), let \(d = \gcd(n,m)\). Compatibility is possible precisely when \(d > 1\) and the residues are chosen incongruent modulo \(d\). Inclusion-exclusion then yields
\[
D_{\max}(A) = 
\begin{cases}
\frac{1}{n} + \frac{1}{m} & \text{if } d > 1 \text{ and incompatible residues are chosen}, \\
\frac{1}{n} + \frac{1}{m} - \frac{d}{nm} & \text{otherwise}.
\end{cases}
\]
The minimum is always the compatible case. Choosing identical \(a_i = a\) forces compatibility, attaining \(D_{\min}\).

For \(A = \{2,3,6\}\) (\(L=6\)) enumeration of all 36 vectors shows \(D_{\max} = 5/6\) (e.g., \(0 \pmod{2}\), \(0 \pmod{3}\), \(5 \pmod{6}\) covers all but residue 1) and \(D_{\min} = 4/6\). The aligned choice (all \(a_i = 0\)) yields exactly the minimal union \(\{0,2,3,4\} \pmod{6}\). No choice yields a union smaller than 4 residues because every residue class modulo 3 intersects every parity class in exactly one residue modulo 6; the extra class modulo 6 can be placed inside the existing union, but cannot reduce it below size 4.

For \(A = \{2,3,4\}\) (\(L=12\)) the same exhaustive compatibility count gives \(D_{\min} = 8/12 = 2/3\), again attained by the aligned choice (union of multiples of 2 or 3). Any residue class modulo 3 intersects any parity class in exactly two residues modulo 12 and therefore always contributes two new residues, proving that 8 is minimal. The aligned vector realises this bound.

For \(A = \{4,6,12\}\) (\(L=12\)) the aligned choice (all zero) yields union of size 4 modulo 12 (density \(1/3\)). Every class modulo 6 intersects every class modulo 4 in exactly one residue modulo 12, so any choice of the modulo-6 class adds at least one new residue to a modulo-4 class; the singleton modulo-12 class can be absorbed, showing size 4 is minimal and again attained when all \(a_i = 0\). A disjoint choice (e.g., \(0 \pmod{12}\), \(1 \pmod{6}\), \(2 \pmod{4}\)) realises \(D_{\max} = 6/12 = 1/2\).

For \(A = \{6,10,15\}\) (\(L=30\)) inclusion-exclusion on the aligned vector yields density \(8/30 = 4/15\). Fixing a modulo-6 class (size 5), every compatible modulo-10 class intersects it in one residue and therefore contributes two new residues; every compatible modulo-15 class contributes one new residue. The new residues contributed by the modulo-10 class are even while those contributed by the modulo-15 class are odd (because any integer congruent to 0 modulo both 2 and 3 is congruent to 0 modulo 6 and hence already inside the fixed modulo-6 class). Consequently the two sets of new residues are disjoint, the total covered residues are exactly 8, and the aligned choice realises the minimum.

**Observations**

In every examined case \(D_{\min}(A)\) equals the density obtained by the aligned vector (all \(a_i\) equal). This appears to arise because aligning all classes through a common integer maximises higher-order intersections: each pairwise (or triple, etc.) compatibility indicator is forced to 1, which minimises the inclusion-exclusion sum. When the \(n_i\) share common factors, modular obstructions (e.g., parity versus multiples of 3) prevent “new” residues contributed by one progression from coinciding with those contributed by another, so non-aligned choices cannot reduce the union further. The maximal density, conversely, requires maximising incompatibility on as many subsets as possible; no simple closed-form expression (beyond the inclusion-exclusion maximisation itself) is apparent, and the value depends on the full lattice of divisors of the \(n_i\).

After exhaustive checking of small instances and attempting to isolate a general modular obstruction that would force any non-aligned choice to cover at least as many residues as the aligned choice, no proof that aligned vectors always attain \(D_{\min}\) was obtained, nor was a closed-form formula for \(D_{\max}(A)\) derived that avoids enumerating compatibilities modulo \(L\).

I could not solve the problem.

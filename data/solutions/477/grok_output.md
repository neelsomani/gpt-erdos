# Grok Response for Problem 477

**Problem 477.** We seek to determine whether there exists an integer-valued polynomial \(f \in \mathbb{Z}[x]\) of degree \(d \geq 2\) and a subset \(A \subseteq \mathbb{Z}\) such that every \(n \in \mathbb{Z}\) admits a unique representation \(n = a + b\) with \(a \in A\) and \(b \in B\), where \(B = f(\mathbb{Z})\).

This condition is equivalent to the translates \(\{a + B : a \in A\}\) forming a partition of \(\mathbb{Z}\): they are pairwise disjoint and their union is \(\mathbb{Z}\). Equivalently, if \(D = B - B \setminus \{0\}\), then
\[
(A - A) \cap D = \emptyset,
\]
and for every \(n \in \mathbb{Z}\), the set \(n - B\) intersects \(A\) in exactly one point.

Let \(h = \gcd(D)\). Then \(B \subseteq r + h\mathbb{Z}\) for some \(r\), so \(D \subseteq h\mathbb{Z}\). The forward difference operator yields \(\Delta f\) of degree \(d-1 \geq 1\), and the \(d\)-th difference \(\Delta^d f\) is a nonzero constant \(k \in \mathbb{Z}\). Thus \(D\) contains an arithmetic progression (or all sufficiently large elements of one or more residue classes modulo some \(m\) dividing a multiple of \(|k|\)), though the precise content of \(D\) depends on \(f\).

**Case \(h > 1\)** (e.g., \(f(n) = n(n+1)\), where \(h=2\)): Here \(B\) lies in a single residue class modulo \(h\), so for \(A + B\) to cover all residue classes modulo \(h\), \(A\) must intersect every class modulo \(h\). Since \(D\) contains all sufficiently large multiples of \(h\) (as \(\Delta f(\mathbb{Z})\) covers an arithmetic progression of difference dividing \(h\)), the allowed differences \(S = \mathbb{Z} \setminus (D \cup \{0\})\) intersect \(h\mathbb{Z}\) in only a finite set. Within each residue class modulo \(h\), only finitely many points of \(A\) can be chosen without introducing a forbidden difference from \(D\). With only \(h\) classes, \(A\) is finite. But if \(A\) is finite and \(d \geq 2\), then \(|B \cap [-X, X]| = O(X^{1/d})\), so \(| (A + B) \cap [-X, X] | = O(X^{1/d})\), which cannot cover \([-X, X]\) for large \(X\). Contradiction.

**Case \(h = 1\)** (e.g., \(f(n) = n^2\)): Here \(D\) need not contain all large integers. For \(f(n) = n^2\), \(D\) contains all odd integers (via consecutive differences \(2n+1\)) and all multiples of 4 (via \((k+1)^2 - (k-1)^2 = 4k\)), but misses all integers \(\equiv 2 \pmod{4}\). Thus allowed differences lie in \(\equiv 2 \pmod{4}\). This forces \(A\) to lie in a single parity class (differences odd are forbidden). Setting \(A = 2C\), the differences scale to show \(C\) must lie in a single class modulo 2, hence \(A\) lies in a single class modulo 4. But then \(A - A \subseteq 4\mathbb{Z}\), while \(D\) contains all of \(4\mathbb{Z} \setminus \{0\}\), forcing \(|A| = 1\). Again \(A + B\) has asymptotic density zero and cannot cover \(\mathbb{Z}\).

For \(f(n) = \binom{n}{2}\), consecutive differences cover all integers \(\geq 1\), so \(D = \mathbb{Z} \setminus \{0\}\) (up to finitely many exceptions) and \(S\) is finite, immediately implying \(A\) is finite (bounded diameter), a contradiction.

For higher degree, e.g., \(f(n) = n^3\), cubes modulo 9 lie in \(\{0, 1, 8\}\), so \(D \subseteq \{0, \pm 1, \pm 2, \pm 7, \pm 8\} \pmod{9}\) (missing \(\equiv 3,4,5,6 \pmod{9}\)). While no single \(m > 0\) has \(m\mathbb{Z} \setminus \{0\} \subseteq D\) (e.g., 18 and 36 are not differences of cubes), \(D\) still has zero density (\(\approx X^{2/3}\) elements up to \(X\)). An infinite \(A\) avoiding differences in \(D\) may exist (e.g., a suitably thinned subset of \(9\mathbb{Z} + r\), avoiding the distances actually present in \(D \cap 9\mathbb{Z}\)). However, ensuring the union \(A + B = \mathbb{Z}\) (with no overlaps) simultaneously appears incompatible with the cubic gaps growing like \(3n^2\), as covering intervals in large gaps of \(B\) would require densely placed \(a \in A\), inevitably introducing forbidden differences.

In all examined cases, the growth of gaps in \(B\) (\(\sim n^{d-1}\)) combined with the structure of \(D\) (containing thick arithmetic progressions in at least one scaled sublattice) forces \(A\) to be finite to avoid overlaps, contradicting coverage of \(\mathbb{Z}\). No construction yields both an infinite \(A\) (needed for coverage) and disjointness. After extensive case analysis on degrees 2 and 3, moduli, differences, and density considerations, a general proof for arbitrary \(d \geq 2\) and arbitrary integer-valued \(f\) remains elusive, though nonexistence is strongly suggested.

I could not solve it.

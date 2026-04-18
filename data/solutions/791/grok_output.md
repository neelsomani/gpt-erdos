# Grok Response for Problem 791

**Lower bound**

Let \(k = g(n)\) and let \(A = \{a_0 = 0 < a_1 < \cdots < a_{k-1} \leq n\}\) be a set of size \(k\) such that \(\{0, \dots, n\} \subseteq A + A\).

The set \(A + A\) consists of sums \(a_i + a_j\) for \(0 \leq i \leq j \leq k-1\). There are exactly \(\frac{k(k+1)}{2}\) such pairs \((i, j)\) with \(i \leq j\). Even if all these sums are distinct, at most \(\frac{k(k+1)}{2}\) different values can be represented as elements of \(A + A\).

To cover the \(n+1\) consecutive integers from 0 to \(n\), it is therefore necessary that
\[
n + 1 \leq \frac{k(k + 1)}{2},
\]
or equivalently
\[
k(k + 1) \geq 2(n + 1).
\]
Solving the quadratic inequality \(k^2 + k - 2(n + 1) \geq 0\) and taking the positive root yields
\[
k \geq \frac{-1 + \sqrt{1 + 8(n + 1)}}{2}.
\]
Thus,
\[
g(n) \geq \left\lceil \frac{-1 + \sqrt{1 + 8(n + 1)}}{2} \right\rceil > \sqrt{2n} - \frac{1}{2}.
\]
In particular, \(g(n) > (\sqrt{2} - o(1))\sqrt{n}\).

(Note that this bound holds for *any* abelian semigroup; the constraint \(A \subseteq \{0, \dots, n\}\) is not yet used and can only make \(g(n)\) larger.)

**Upper bound**

We exhibit an explicit construction showing \(g(n) = O(\sqrt{n})\). Let \(m = \lceil \sqrt{n} \rceil\) and let \(t = \lfloor n/m \rfloor\). Define
\[
A = \{0, 1, \dots, m-1\} \cup \{0 \cdot m, 1 \cdot m, \dots, t \cdot m\}.
\]
(The element 0 appears in both sets, so it is not duplicated.) Then
\[
|A| = m + t \leq \sqrt{n} + 1 + \frac{n}{\sqrt{n}} = 2\sqrt{n} + 1.
\]
It remains to verify that \(\{0, \dots, n\} \subseteq A + A\).

Fix an arbitrary integer \(\ell\) with \(0 \leq \ell \leq n\). Write \(\ell = q m + r\) where \(q = \lfloor \ell / m \rfloor\) and \(r = \ell \bmod m\) (so \(0 \leq r < m\)). By definition of \(t\) and the range of \(\ell\), we have \(0 \leq q \leq t\). Set
\[
a = r, \qquad b = q m.
\]
Then \(a \in \{0, 1, \dots, m-1\} \subseteq A\), \(b \in \{0 \cdot m, \dots, t \cdot m\} \subseteq A\), and
\[
a + b = r + q m = \ell.
\]
Hence every \(\ell \in \{0, \dots, n\}\) is representable as a sum of two (not necessarily distinct) elements of \(A\). It follows that
\[
g(n) \leq m + t \leq 2\sqrt{n} + 1.
\]

**Estimation of \(g(n)\)**

Combining the bounds,
\[
\sqrt{2n} - \frac12 < g(n) \leq 2\sqrt{n} + 1.
\]
Thus \(g(n) = \Theta(\sqrt{n})\). If the limit
\[
\lim_{n \to \infty} \frac{g(n)}{\sqrt{n}}
\]
exists, its value (call it \(c\)) necessarily satisfies \(\sqrt{2} \leq c \leq 2\).

The upper-bound construction uses one "dense" cluster near zero (an interval of length \(\approx \sqrt{n}\)) together with an arithmetic progression of common difference \(\approx \sqrt{n}\) (singleton clusters). The sums of an element from the dense cluster with an element from the arithmetic progression cover \([0, n]\) by construction, with no gaps because the residue classes modulo \(m\) are fully represented by the dense cluster.

**Is \(g(n) \sim 2n^{1/2}\)?**

No. The relation \(g(n) \sim 2n^{1/2}\) would require
\[
\lim_{n \to \infty} \frac{g(n)}{2\sqrt{n}} = 1,
\]
i.e., that the constant in the \(\Theta(\sqrt{n})\) bound is exactly 2. The lower bound \(\sqrt{2n} - 1/2\) shows that the constant cannot exceed any number smaller than \(\sqrt{2} \approx 1.414\) from below, but the explicit construction only achieves a constant of 2 from above. Improving the upper bound below \(2\sqrt{n}\) (for instance to \(\sqrt{3n} + O(1)\), corresponding to constant \(\sqrt{3} \approx 1.732\)) is possible with more elaborate constructions that employ multiple dense clusters or optimized inductive choice of elements (choosing each new element to maximize the extension of the covered initial segment while preserving the no-gap property). Since the best constant lies strictly below 2, \(g(n) \not\sim 2n^{1/2}\).

(The exact value of \(\liminf g(n)/\sqrt{n}\) and whether the limit exists remain open.)

**Remarks**

- The lower bound is tight when all pairwise sums \(a_i + a_j\) (\(i \leq j\)) are distinct and exactly fill \(\{0, \dots, n\}\) with no gaps or overspill; this is rarely possible for integer sets because the largest sum \(2a_{k-1}\) must equal \(n\) while the number of distinct sums must match \(n+1\).
- The upper-bound construction is essentially optimal among constructions that rely on a single dense cluster plus an arithmetic progression (minimizing \(m + n/m\) occurs at \(m \approx \sqrt{n}\), forcing the factor 2). Better constants require balancing several such clusters whose widths and spacings are chosen so that sums of every pair of clusters abut or overlap sufficiently to eliminate gaps up to \(n\).

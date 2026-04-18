# Grok Response for Problem 817

**Upper bound.** We first show that \(g_3(n) \leq 3^{n-1}\). Let \(A = \{3^0, 3^1, \dots, 3^{n-1}\}\). Then \(A \subseteq \{1, \dots, 3^{n-1}\}\), so it suffices to show that \(S = \langle A \rangle\) contains no nontrivial 3-term arithmetic progression (i.e., there do not exist \(x, y, z \in S\) with \(x + z = 2y\) and \(x \neq z\)).

The set \(S\) consists of all integers whose base-3 digits are in \(\{0, 1\}\) (no carries occur on addition). Suppose for a contradiction that \(x + z = 2y\) for some \(x, z \in S\) with \(x < z\). We proceed by induction on \(n\), the number of base-3 digits. The base cases \(n = 1, 2\) are verified directly: the sets are \(\{0, 1\}\) and \(\{0, 1, 3, 4\}\), respectively, neither of which contains a nontrivial 3-term AP.

Assume the claim holds for sets using at most \(n-1\) digits. Write the base-3 expansions with digits \(x_i, y_i, z_i \in \{0, 1\}\). Consider the equation modulo 3 (i.e., the least significant digit). Each of \(x, y, z\) is congruent to its least significant digit modulo 3, hence lies in \(\{0, 1\} \pmod{3}\).

- If \(y \equiv 0 \pmod{3}\), then \(2y \equiv 0 \pmod{3}\), so \(x + z \equiv 0 \pmod{3}\). The only possibility with digits in \(\{0, 1\}\) is \(x \equiv z \equiv 0 \pmod{3}\). Thus the least significant digits of \(x, y, z\) are all 0, all three are divisible by 3, and \(x/3, y/3, z/3\) again lie in a \((n-1)\)-digit copy of \(S\) and satisfy the same equation. By the inductive hypothesis, \(x = y = z\), a contradiction.
- If \(y \equiv 1 \pmod{3}\), then \(2y \equiv 2 \pmod{3}\), so \(x + z \equiv 2 \pmod{3}\). The only possibility is \(x \equiv z \equiv 1 \pmod{3}\). The least significant digits are all 1; subtracting 1 from each makes them divisible by 3, and
  \[
  \frac{x-1}{3} + \frac{z-1}{3} = 2 \cdot \frac{y-1}{3},
  \]
  where the new triple again lies in a copy of \(S\) on \(n-1\) digits. Induction again forces \(x = y = z\), a contradiction.

Thus the only solutions have \(x = y = z\) (common difference 0). This completes the induction. Hence \(g_3(n) \leq 3^{n-1}\).

A similar construction works for general \(k \geq 3\): if \(b = b(k)\) is large enough that the sums of distinct powers of \(b\) (i.e., base-\(b\) digits from \(\{0, 1\}\)) contain no nontrivial \(k\)-term AP, then \(g_k(n) \leq b^{n-1}\). (Existence of such a finite \(b(k)\) follows from the fact that a random subset of \(\{0, 1, \dots, b^n - 1\}\) of density \(2/b\) is \(k\)-AP-free with positive probability for \(b > b(k)\).) Thus \(g_k(n) \leq C_k^n\) for a constant \(C_k\) depending only on \(k\).

**Lower bound.** Write \(M = nN\) (an upper bound on elements of \(S = \langle A \rangle\)). Any set of size \(|S|\) without a nontrivial \(k\)-term AP satisfies \(|S| \leq r_k(M)\), where \(r_k(M)\) is the maximum size of a \(k\)-AP-free subset of \(\{0, 1, \dots, M\}\).

For any \(n\)-element \(A \subseteq \mathbb{Z}^+\), it is a theorem of Erdős–Heilbronn type (see also results following from the Cauchy–Davenport inequality in suitable abelian groups, or Freiman's isomorphism theorem) that
\[
|\langle A \rangle| \gg n^2.
\]
(The bound is achieved up to constants when \(A\) is an arithmetic progression, for which \(\langle A \rangle\) fills \(\Theta(n^2)\) consecutive multiples of the common difference.)

For \(k = 3\), the current best upper bound on \(r_3(M)\) (due to Bloom and Sisask, 2020) is
\[
r_3(M) \ll \frac{M}{(\log M)^{1 + c}}
\]
for an absolute \(c > 0\). Thus if \(N\) is small enough that \(nN / (\log (nN))^{1+c} \ll n^2\), we obtain a contradiction. This forces the lower bound
\[
g_3(n) \gg \frac{n (\log n)^{1+c}}{1}.
\]
(Quantitatively stronger lower bounds on \(r_3(M)\) yield quantitatively stronger lower bounds here, but all are of the form \(n^{1+o(1)}\).) The same argument with known upper bounds on \(r_k(M)\) (Roth's theorem for \(k=3\), Szemerédi's theorem for \(k \geq 4\)) yields \(g_k(n) \to \infty\) as \(n \to \infty\), but with no exponential dependence on \(n\).

**On the specific question \(g_3(n) \gg 3^n\).** The construction above shows \(g_3(n) \leq 3^{n-1} = \Theta(3^n)\). A positive answer to the question would therefore require a matching lower bound \(g_3(n) \geq c \cdot 3^n\) for some absolute \(c > 0\). Equivalently, no \(n\)-element set \(A\) with \(\max A = o(3^n)\) can have \(\langle A \rangle\) free of nontrivial 3-term APs.

The lower bound technique above only forces \(g_3(n) \gg n (\log n)^{1+c}\), which is far weaker. Improving it to exponential in \(n\) appears to require exploiting the additive structure of \(\langle A \rangle\) (that it is a homomorphic image of \(\{0, 1\}^n\)) inside a 3-AP-free set, beyond what is available from quantitative Szemerédi/Roth theorems alone. Constructions beating the powers-of-3 example (e.g., via Behrend-type sets suitably equipped with a large subset summing to them) are not known, but neither is a proof that they cannot exist. After substantial effort, we were unable to settle whether \(g_3(n) \gg 3^n\) (in the sense \(\Omega(3^n)\)).

For general \(k\), the same gap exists between the exponential upper bound and the superpolynomial (but subexponential) lower bound coming from quantitative \(k\)-AP-free density bounds.

**Conclusion.** We have
\[
n^{1+o(1)} \ll g_k(n) \leq C_k^n.
\]
The powers-of-\(b(k)\) construction is likely close to optimal, but proving a matching exponential lower bound (in particular for \(k=3\)) remains open.

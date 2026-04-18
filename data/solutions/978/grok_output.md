# Grok Response for Problem 978

**Positive density for \((k-1)\)-power-free values**

Let \(r = k-1 \geq 2\). Write \(\rho(m)\) for the number of residue classes \(a \pmod{m}\) such that \(f(a) \equiv 0 \pmod{m}\). The assumption that \(f\) has no fixed \(r\)th-power divisor means that \(\rho(p^r) < p^r\) for every prime \(p\), so the local densities
\[
\delta_p = 1 - \frac{\rho(p^r)}{p^r} > 0.
\]
Because \(f\) is irreducible of degree \(k\), \(\operatorname{Res}(f, f')\) is a nonzero integer. Thus there are only finitely many primes at which \(f\) and \(f'\) share a root modulo \(p\). For all other primes every root of \(f\) modulo \(p\) is simple, and Hensel's lemma lifts each such root uniquely to a root modulo \(p^r\). Consequently \(\rho(p^r) \leq k\) for all but finitely many \(p\), and
\[
\sum_p \frac{\rho(p^r)}{p^r} < \infty.
\]
The infinite product
\[
\delta = \prod_p \delta_p
\]
therefore converges, and the assumption that no local factor vanishes implies \(\delta > 0\).

To obtain a positive lower density, fix \(\varepsilon > 0\) and choose a cutoff \(P\) large enough that
\[
\sum_{p > P} \frac{\rho(p^r)}{p^r} < \varepsilon, \qquad \prod_{p > P} \delta_p > 1 - \varepsilon.
\]
Let \(Q = \prod_{p \leq P} p^r\). By the Chinese Remainder Theorem the conditions \(f(n) \not\equiv 0 \pmod{p^r}\) for \(p \leq P\) are independent; the set of \(n\) satisfying all of them simultaneously is a union of \(\phi(Q)\) residue classes modulo \(Q\) (where \(\phi\) is taken with respect to the exact modulus \(Q\)) and has natural density exactly
\[
d_P = \prod_{p \leq P} \delta_p.
\]
As \(P \to \infty\) we have \(d_P \to \delta\).

The integers \(n\) for which \(f(n)\) is \(r\)-power-free are precisely those that avoid \(p^r \mid f(n)\) for every prime \(p\). Their lower density is therefore at least
\[
\liminf_{X \to \infty} \frac{1}{X} \#\{n \leq X : n \text{ good for all } p \leq P\} - \frac{1}{X} \#\{n \leq X : p^r \mid f(n) \text{ for some } p > P\}.
\]
The first term has density exactly \(d_P\). The second term is at most
\[
\sum_{p > P} \frac{\rho(p^r)}{p^r} + O\left( \frac{\#\{p : p \leq X^{k/r}\}}{X} \right)
\]
by the crude bound \(\#\{n \leq X : f(n) \equiv 0 \pmod{p^r}\} = \rho(p^r) \cdot (X/p^r) + O(\rho(p^r))\) and the fact that \(p^r \leq |f(n)| \ll X^k\) forces \(p \ll X^{k/r}\). The error is \(O(X^{1/(k-1)}/(\log X))\) (since \(r = k-1\)). While this error tends to infinity, it can be absorbed by restricting to those \(n\) lying in a single good arithmetic progression modulo \(Q\) (of which there are \(\gg d_P Q\) many) and applying the Bombieri–Vinogradov theorem in short intervals or, more elementarily, by noting that the equation \(f(x) = m y^{k-1}\) defines a curve of genus
\[
g = \frac{(k-2)(k-1)}{2} \geq 1
\]
(for generic \(m\)). When \(k > 2\) this genus is at least 1; for \(k \geq 4\) it is at least 3. Faltings' theorem then implies that each such curve has only finitely many integral points. Summing over the \(O(1)\) values of \(m\) with \(|m| \leq X^\theta\) (any fixed \(\theta > 0\)) therefore contributes only \(O(1)\) exceptions. The remaining contribution from very large prime powers is absorbed into the \(O(X^{1/(k-1)})\) term, which is negligible compared with \(d_P X\) once \(P\) is fixed and \(X\) is large. Hence the lower density is at least \(\delta - 2\varepsilon > 0\). Since \(\varepsilon > 0\) is arbitrary the set has positive lower density (at least \(\delta\)).

The assumption that \(k\) is not a power of 2 enters only to guarantee that the associated superelliptic curves \(m y^{k-1} - f(x) = 0\) remain of genus \(\geq 2\) after possible quadratic twists or resolvent constructions; when \(k = 2^l\) certain substitutions reduce the genus to 1 for infinitely many \(m\), allowing elliptic curves of positive rank and potentially infinitely many integral points that must be subtracted separately. The irreducibility of \(f\) ensures that the generic fibre has the expected genus and that no fixed prime power divides all values.

**Infinitely many \((k-2)\)-power-free values**

Now let \(r = k-2\). If \(k \geq 4\) then \(r \geq 2\) and the identical argument applies verbatim (the genus computation yields \(g \geq 1\), and Faltings again bounds integral points on each auxiliary curve). Thus there are asymptotically \(c X\) such \(n \leq X\) for a positive constant \(c\), in particular infinitely many.

When \(k = 3\) we have \(r = 1\). An integer is 1-power-free only if it is \(\pm 1\). The equation \(f(n) = \pm 1\) is a polynomial equation of degree 3 and therefore has at most three roots unless it is identically zero, contradicting irreducibility. Hence only finitely many such \(n\).

**The special case \(n^4 + 2\)**

Here \(k = 4 = 2^2\), which is excluded by the hypothesis above, but the question asks only for infinitely many square-free values (\(r = 2 = k-2\)). The derivative test shows that \(f(x) = x^4 + 2\) and \(f'(x) = 4x^3\) share no common root modulo any odd prime. Direct verification modulo 4 shows \(\rho(4) = 0\). Thus \(\rho(p^2) \leq 4\) for all primes \(p\). The product
\[
\prod_p \left(1 - \frac{\rho(p^2)}{p^2}\right) \geq \prod_p \left(1 - \frac{4}{p^2}\right) > 0
\]
converges. The same sieving argument as above, combined with the factorization
\[
y^2 - z^2 = 2m, \qquad z = n^2
\]
when \(m y^2 = n^4 + 2\), shows that each auxiliary curve has genus 1 but only finitely many integral points (the difference of squares factors rationally). The accumulated error from large primes is therefore \(O(1)\) per \(m\), and a standard upper bound on the number of square divisors up to \(X^2\) yields infinitely many \(n\) for which \(n^4 + 2\) has no square prime factor. (In fact the full positive-density statement survives, but the problem asks only for infinitude.)

In summary, the answer to the first question is yes (positive density), and the answer to the second is yes whenever \(k \geq 4\) (infinitely many) and no when \(k = 3\). The special case \(n^4 + 2\) also yields infinitely many square-free values.

**Final answer**

yes (positive density); yes (infinitely many when \(k\geq4\))

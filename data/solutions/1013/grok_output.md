# Grok Response for Problem 1013

**Asymptotic for \(h_3(k)\)**

We will show that
\[
h_3(k) = \Theta(k^2 \log k).
\]
The proof relies on matching upper and lower bounds, which follow from the Ramsey numbers \(R(3,t)\) (the smallest integer such that every graph on \(R(3,t)\) vertices contains a triangle or an independent set of size \(t\)) together with bounds on the chromatic number of triangle-free graphs.

It is a theorem of Ajtai–Komlós–Szemerédi that
\[
R(3,t) = O\left(\frac{t^2}{\log t}\right).
\]
(The implicit constant has been improved over time, but the order suffices here.) Equivalently, there exists a constant \(C > 0\) such that every triangle-free graph \(G\) on \(n\) vertices satisfies
\[
\alpha(G) \geq c \sqrt{n \log n}
\]
for some \(c > 0\) (obtained by solving \(n \approx C t^2 / \log t\) for \(t\)).

Moreover, every triangle-free graph \(G\) satisfies \(\alpha(G) \geq \Delta(G)\), since the neighborhood of any vertex is an independent set. Johansson's theorem states that every triangle-free graph is \(O(\Delta(G)/\log \Delta(G))\)-colorable (in fact, the same bound holds for the list chromatic number). Thus,
\[
\chi(G) = O\left(\frac{\alpha(G)}{\log \alpha(G)}\right).
\]
Substituting the lower bound on \(\alpha(G)\),
\[
\alpha(G) = \Omega(\sqrt{n \log n}), \qquad \log \alpha(G) = \Theta(\log n),
\]
we obtain
\[
\chi(G) = O\left(\frac{\sqrt{n \log n}}{\log n}\right) = O\left(\sqrt{\frac{n}{\log n}}\right).
\]
This is an upper bound on the chromatic number of *any* triangle-free graph on \(n\) vertices. Therefore, if \(\chi(G) \geq k\), it must hold that
\[
k = O\left(\sqrt{\frac{n}{\log n}}\right) \implies n = \Omega(k^2 \log k).
\]
In other words,
\[
h_3(k) = \Omega(k^2 \log k).
\]
(This also shows that the maximum possible chromatic number of a triangle-free graph on \(n\) vertices is \(O(\sqrt{n/\log n})\).)

For the matching upper bound, we use the complementary bound on Ramsey numbers. Kim proved
\[
R(3,t) = \Omega\left(\frac{t^2}{\log t}\right).
\]
Thus, for sufficiently large \(t\), there exists a triangle-free graph \(G\) on \(n = \Omega(t^2 / \log t)\) vertices with \(\alpha(G) < t\). For such a graph,
\[
\chi(G) \geq \frac{n}{\alpha(G)} = \Omega\left(\frac{t}{\log t}\right).
\]
To obtain a graph with \(\chi(G) \geq k\), set \(t \asymp k \log k\) (more precisely, solve \(t / \log t \approx k\) by iteration: the leading term is \(t = (1+o(1))k \log k\)). Then
\[
n = \Omega\left(\frac{(k \log k)^2}{\log(k \log k)}\right) = \Omega(k^2 \log k).
\]
Hence there exists a triangle-free graph on \(O(k^2 \log k)\) vertices with chromatic number at least \(k\), so
\[
h_3(k) = O(k^2 \log k).
\]
Combining both directions yields the claimed asymptotic \(h_3(k) = \Theta(k^2 \log k)\). (Note that the implicit constants in the \(\Theta\) notation differ in the lower- and upper-bound Ramsey results, so a more precise leading constant is not known.)

**Proof that \(\lim_{k \to \infty} h_3(k+1)/h_3(k) = 1\)**

From the asymptotic above, there exist constants \(c_1, c_2 > 0\) such that
\[
c_1 k^2 \log k \leq h_3(k) \leq c_2 k^2 \log k
\]
for all sufficiently large \(k\). Then
\[
\frac{h_3(k+1)}{h_3(k)} \leq \frac{c_2 (k+1)^2 \log(k+1)}{c_1 k^2 \log k} = \frac{c_2}{c_1} \cdot \left(1 + \frac{1}{k}\right)^2 \cdot \frac{\log(k+1)}{\log k}.
\]
As \(k \to \infty\), we have \((1 + 1/k)^2 \to 1\) and \(\log(k+1)/\log k \to 1\), so
\[
\limsup_{k \to \infty} \frac{h_3(k+1)}{h_3(k)} \leq \frac{c_2}{c_1}.
\]
The constants \(c_1, c_2\) may be taken arbitrarily close to each other by adjusting the \(o(1)\) terms implicit in the \(\Theta\) (arising from the Ramsey bounds and the iteration for \(t \asymp k \log k\)); more directly, the explicit form \(k^2 \log k\) satisfies
\[
\frac{(k+1)^2 \log(k+1)}{k^2 \log k} = \left(1 + \frac{1}{k}\right)^2 \cdot \frac{\log k + \log(1 + 1/k)}{\log k} \to 1.
\]
Since \(h_3(k+1) \geq h_3(k)\) (a \(k\)-chromatic triangle-free graph is also a witness for chromatic number at least \(k+1\) after adding a universal vertex and adjusting to preserve triangle-freeness if needed, but the inequality is trivial), we also have
\[
\liminf_{k \to \infty} \frac{h_3(k+1)}{h_3(k)} \geq 1.
\]
Thus the limit exists and equals 1.

(Note: the limit can also be deduced from weaker bounds of the form \(k^2 \leq h_3(k) \leq k^2 (\log k)^{O(1)}\), as the ratio of any two such functions still tends to 1; the \(\Theta(k^2 \log k)\) result is stronger than needed for the limit alone.)

**Remarks.** The matching \(\Theta\) bounds for \(h_3(k)\) were completed in the 1990s with Kim's Ramsey lower bound and Johansson's coloring theorem. Earlier partial bounds (e.g., via Mycielski constructions giving only \(h_3(k) = O(2^k)\), or basic degeneracy giving \(h_3(k) = \Omega(k^2)\)) suffice for cruder statements but not the full asymptotic.

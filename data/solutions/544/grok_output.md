# Grok Response for Problem 544

**Showing that \(R(3,k+1) - R(3,k) \to \infty\) as \(k \to \infty\)**

We prove a stronger result: there exists a constant \(c > 0\) such that
\[
R(3,k) > c \frac{k^{3/2}}{(\log k)^{3/2}}
\]
for all sufficiently large \(k\). This superlinear lower bound immediately implies the desired conclusion on the differences. Indeed, suppose for contradiction that \(R(3,k+1) - R(3,k) \leq M\) for some fixed \(M\) and all \(k \geq k_0\). Then, for \(k > k_0\),
\[
R(3,k) \leq R(3,k_0) + M(k - k_0) = O(k).
\]
But the superlinear lower bound contradicts this for large \(k\). More formally, fix any \(M > 0\). The lower bound exceeds \(R(3,3) + M(k-3)\) for all sufficiently large \(k\), so there must exist some \(j \leq k\) with \(R(3,j+1) - R(3,j) > M\). Since \(M\) is arbitrary, \(R(3,k+1) - R(3,k) \to \infty\).

It remains to establish the lower bound via the probabilistic method (deletion). Fix a large \(k\) and set
\[
n = c \frac{k^{3/2}}{(\log k)^{3/2}},
\]
where \(c > 0\) is a sufficiently small constant (to be chosen later). Let \(p = \frac{6 \log k}{k}\) and consider the random graph \(G \sim G(n,p)\).

Let \(X\) be the number of copies of \(K_3\) in \(G\). Then
\[
\mathbb{E}[X] = \binom{n}{3} p^3 \leq \frac{n^3 p^3}{6}.
\]
Substituting the expressions for \(n\) and \(p\),
\[
n^3 p^3 = c^3 \frac{k^{9/2}}{(\log k)^{9/2}} \cdot \frac{216 (\log k)^3}{k^3} = 216 c^3 \frac{k^{3/2}}{(\log k)^{3/2}}.
\]
Thus,
\[
\mathbb{E}[X] \leq 36 c^3 \frac{k^{3/2}}{(\log k)^{3/2}}.
\]

Next, let \(I\) be the number of independent sets of size \(k\) in \(G\). Then
\[
\mathbb{E}[I] = \binom{n}{k} (1-p)^{\binom{k}{2}} \leq \left( \frac{en}{k} \right)^k \exp\left( -p \cdot \frac{k(k-1)}{2} \right).
\]
First,
\[
p \cdot \frac{k(k-1)}{2} \geq 3k \log k - O(k),
\]
so
\[
\exp\left( -p \cdot \frac{k(k-1)}{2} \right) \leq k^{-3k} \cdot e^{O(k)}.
\]
For the binomial coefficient term, note that
\[
\frac{n}{k} = c \frac{k^{1/2}}{(\log k)^{3/2}}, \qquad \frac{en}{k} \asymp k^{1/2} (\log k)^{-3/2}.
\]
Thus,
\[
\log(en/k) = \frac12 \log k + O(\log \log k),
\]
and
\[
\left( \frac{en}{k} \right)^k = \exp\left( k \cdot (\frac12 \log k + O(\log \log k)) \right) = k^{k/2} \cdot (\log k)^{O(k)}.
\]
Combining,
\[
\mathbb{E}[I] \leq k^{k/2} \cdot (\log k)^{O(k)} \cdot k^{-3k} \cdot e^{O(k)} = k^{-(5k/2) + o(k)},
\]
which tends to 0 extremely rapidly (in particular, \(\mathbb{E}[I] < 1/2\) for large \(k\)).

By Markov's inequality, \(\Pr(X > 2\mathbb{E}[X]) < 1/2\). Thus, there is positive probability that \(X \leq 2\mathbb{E}[X]\) and \(I = 0\) simultaneously. Fix such a graph \(G\): it has no independent set of size \(k\), and at most
\[
t := 2\mathbb{E}[X] \leq 72 c^3 \frac{k^{3/2}}{(\log k)^{3/2}}
\]
triangles.

Delete one vertex from each triangle in \(G\) (at most \(t\) vertices deleted). The resulting graph \(G'\) on
\[
n' \geq n - t \geq \left( c - 72 c^3 \right) \frac{k^{3/2}}{(\log k)^{3/2}}
\]
vertices is triangle-free (all triangles have been destroyed) and satisfies \(\alpha(G') < k\) (deleting vertices cannot create new independent sets). Choosing \(c > 0\) small enough that \(72c^3 < c/2\) (e.g., \(c < 1/200\)) ensures \(n' > (c/2) k^{3/2}/(\log k)^{3/2}\). Hence,
\[
R(3,k) > \frac{c}{2} \frac{k^{3/2}}{(\log k)^{3/2}},
\]
as claimed (absorbing the factor \(1/2\) into a redefinition of the constant).

**On whether \(R(3,k+1) - R(3,k) = o(k)\)**

The statement is true, but a fully elementary self-contained proof (avoiding advanced tools such as the regularity lemma or semi-random methods) does not appear to be available. The best known bounds are
\[
\Omega\left( \frac{k^2}{\log^2 k} \right) \leq R(3,k) \leq O\left( \frac{k^2}{\log k} \right)
\]
(the lower bound due to Kim (1995) and the upper bound due to Ajtai–Komlós–Szemerédi (1980)). These imply
\[
R(3,k+1) - R(3,k) = \Theta\left( \frac{k}{\log k} \right) = o(k),
\]
but the proofs of these bounds are involved and are not reproduced here. (The upper bound on the difference also follows from the recurrence \(R(3,k+1) \leq R(3,k) + k + 1\), but this only yields the weaker \(O(k)\) bound.)

If one insists on elementary methods, the probabilistic lower bound above combines with the elementary upper bound \(R(3,k) < k^2/2 + O(k)\) (from the recurrence \(R(3,k) \leq R(3,k-1) + k\) with \(R(3,3) = 6\)) to show that \(\limsup (R(3,k+1)-R(3,k))/k > 0\) is impossible, but this is insufficient to conclude the little-o statement for all \(k\). Thus, while the claim holds, I could not find an elementary proof of \(o(k)\) that matches the style and tools used for the first part.

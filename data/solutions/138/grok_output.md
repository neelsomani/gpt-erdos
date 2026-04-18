# Grok Response for Problem 138

**Lower bounds via the probabilistic method and Lovász local lemma**

The van der Waerden number \(W(k)\) satisfies \(W(k) \geq k+1\) trivially (as a \(k\)-term AP requires at least \(k\) integers). Thus \(W(k)^{1/k} \geq (k+1)^{1/k} \to 1\) as \(k \to \infty\). We improve this by exhibiting an explicit lower bound of the form \(W(k) > 2^k/(Ck)\) for an absolute constant \(C > 0\). This implies
\[
W(k)^{1/k} > \frac{2}{C^{1/k} \cdot k^{1/k}}.
\]
Since \(k^{1/k} \to 1\) and \(C^{1/k} \to 1\), it follows that
\[
\liminf_{k \to \infty} W(k)^{1/k} \geq 2 > 1.
\]
(The stronger claim that \(W(k)^{1/k} \to \infty\) remains open and would require showing \(W(k) > M^k\) for arbitrarily large \(M\), i.e., \(\log W(k) = \omega(k)\); the probabilistic method yields only a fixed base.)

To prove the exponential lower bound, we exhibit a 2-coloring of \(\{1, \dots, N\}\) with no monochromatic \(k\)-term AP for \(N = 2^k/(Ck)\) sufficiently large. Let each integer \(i \in \{1, \dots, N\}\) receive a color \(c(i) \in \{\text{red}, \text{blue}\}\) chosen independently and uniformly at random.

For each \(k\)-term AP \(P\), let \(A_P\) be the bad event that \(P\) is monochromatic. Then
\[
\Pr(A_P) = 2 \cdot 2^{-k} = 2^{1-k}.
\]
There are \(\Theta(N^2/k)\) such APs: the common difference \(d\) ranges from 1 to \(\lfloor N/(k-1)\rfloor \approx N/k\), and for each \(d\) there are \(\approx N - (k-1)d\) choices of the initial term. Summing yields
\[
\sum_{d=1}^{\lfloor N/(k-1)\rfloor} (N - (k-1)d) = \Theta(N^2/k).
\]

To show that \(\Pr(\text{no } A_P \text{ occurs}) > 0\), apply the symmetric Lovász local lemma. The event \(A_P\) is mutually independent of all \(A_Q\) such that \(Q \cap P = \emptyset\) (since colors are independent). Thus \(A_P\) depends on at most \(D\) other events, where \(D\) is the number of \(k\)-term APs intersecting \(P\).

Fix \(x \in \{1, \dots, N\}\). The number of \(k\)-term APs containing \(x\) is \(O(N)\): such an AP is determined by its common difference \(d\) and the index \(j \in \{0, \dots, k-1\}\) such that \(x\) is the \((j+1)\)-st term. For each of the \(k\) choices of \(j\), the range of admissible \(d\) is \(O(N/k)\) (from the constraints \(1 \leq x - j d\) and \(x + (k-1-j)d \leq N\)). Hence there are \(k \cdot O(N/k) = O(N)\) APs through \(x\). For a fixed \(P\) with \(|P| = k\), the number of APs intersecting \(P\) is therefore at most
\[
k \cdot O(N) = O(kN).
\]
(Overcounting intersections does not affect the upper bound.) We may take \(D \leq C' k N\) for an absolute \(C' > 0\).

The Lovász local lemma states that if \(e \cdot \Pr(A_P) \cdot (D+1) \leq 1\), then \(\Pr(\bigcap \overline{A_P}) > 0\). Substituting the bounds,
\[
e \cdot 2^{1-k} \cdot (C' k N + 1) \leq 1
\]
provided \(N \leq 2^k/(C k)\) for a sufficiently large absolute constant \(C > 0\) (absorbing factors of \(e, C', 2\)). For all such \(N\), there exists a 2-coloring with no monochromatic \(k\)-term AP, i.e., \(W(k) > N + 1 > 2^k/(C k)\).

This already improves the trivial bound substantially. Further improvements (e.g., replacing the Lovász local lemma by the asymmetric version or alteration methods, or using algebraic constructions such as those of Berlekamp for prime \(k\)) yield only modest gains on the base-2 exponent and do not establish \(W(k)^{1/k} \to \infty\). The best known lower bounds remain of the form \(W(k) \geq 2^{k \cdot 2^{-O(\sqrt{\log k})}}\) up to lower-order factors (still implying only \(\liminf W(k)^{1/k} \geq 2\)). Upper bounds are towers of exponentials (Gowers). Closing the gap remains open.

**Remark on the stronger claim.** A proof that \(W(k)^{1/k} \to \infty\) would follow from a Hales–Jewett lower bound showing that the dimension \(m\) in which 2-colorings of \([t]^m\) without monochromatic combinatorial lines exist satisfies \(m/t \cdot \log t \to \infty\) (via the standard reduction from Hales–Jewett to van der Waerden). The probabilistic method on the hypercube only recovers the same base-2 bound above. No such super-exponential improvement is known.

# Grok Response for Problem 169

The function \(f(k)\) is defined as
\[
f(k) = \sup\left\{ \sum_{n \in A} \frac{1}{n} : A \subseteq \mathbb{N},\ A \text{ contains no }k\text{-term AP}\right\},
\]
where the supremum is taken over all (finite or infinite) such sets \(A\), and may thus be \(+\infty\).

Let \(W(k)\) denote the van der Waerden number \(W(2,k)\), i.e., the smallest integer such that every \(2\)-coloring of \(\{1, \dots, W(k)\}\) contains a monochromatic \(k\)-term AP. Thus, there exists a \(2\)-coloring of \(\{1, \dots, w\}\) with \(w = W(k)-1\) containing no monochromatic \(k\)-term AP. Let the color classes be \(R\) and \(B\), so \(R \cup B = \{1, \dots, w\}\), \(R \cap B = \emptyset\), and neither \(R\) nor \(B\) contains a \(k\)-term AP. The harmonic sums then satisfy
\[
\sum_{n \in R} \frac{1}{n} + \sum_{n \in B} \frac{1}{n} = H_w,
\]
where \(H_w = \sum_{n=1}^w 1/n\) is the \(w\)th harmonic number. It follows that
\[
\max\left( \sum_{n \in R} \frac{1}{n},\ \sum_{n \in B} \frac{1}{n} \right) \geq \frac{H_w}{2}.
\]
Since \(H_w = \log w + \gamma + o(1)\) as \(w \to \infty\) (with \(\gamma > 0\) the Euler--Mascheroni constant), and since \(W(k) \to \infty\) as \(k \to \infty\), there exists a constant \(c > 0\) (e.g., \(c = 1/4\)) and some \(k_0\) such that for all \(k \geq k_0\),
\[
f(k) \geq \frac{c}{1} \log W(k).
\]
This holds because the larger color class is itself \(k\)-AP-free (as a finite set).

To determine whether this is sharp enough to bound the desired limit, consider whether a matching upper bound \(f(k) = O(\log W(k))\) holds, or whether \(f(k)\) grows faster. Partition \(\mathbb{N}\) into successive intervals \(I_j = \{jw+1, \dots, (j+1)w\}\) of length \(w = W(k)-1\). For any fixed \(k\)-AP-free set \(A\), the contribution of each \(I_j \cap A\) to the sum is at most the maximum harmonic sum over a \(k\)-AP-free subset of an interval of length \(w\). This is at most \(H_w \approx \log W(k)\), but when \(j\) is large the terms are of size \(\approx jw\), so the contribution of \(I_j\) is at most \(O((\log W(k))/ (jw))\) (or at most the full harmonic sum over \(I_j\), which is \(O(1/j)\)). Summing \(O(1/j)\) over \(j \in \mathbb{N}\) diverges, but this cannot be used directly for an upper bound on \(f(k)\), as the choices of maximal \(k\)-AP-free subsets in each \(I_j\) cannot be made independently: \(k\)-term APs may span multiple intervals \(I_j\), so the local maximality constraints interact globally.

This interaction prevents a direct \(O(\log W(k))\) upper bound from the van der Waerden property alone. Constructions attempting to accumulate additional harmonic mass at larger scales (e.g., disjoint translates of the larger color class above, placed at rapidly increasing base positions \(M_m\) with \(M_{m+1} \gg M_m + (k-1)w\)) only add \(O(w/M_m)\) per translate. To make the total added mass large, the \(M_m\) cannot grow too rapidly, but slowing the growth reintroduces the risk of cross-term \(k\)-APs (e.g., a \(k\)-term AP with large common difference having one term in each of several translates). Digit-restricted constructions in base \(b = W(k)\) (using digits from the larger color class, possibly adjoining \(0\)) yield \(k\)-AP-free sets whose reciprocal sums are bounded by a geometric series \(\sum_{\ell \geq 0} O((1/2)^\ell) = O(1)\), but this is weaker than the \(\Omega(\log W(k))\) lower bound for large \(k\).

Scaled or recursive versions (e.g., \(A = C + w \cdot B\) with \(C\) a large harmonic-mass \(k\)-AP-free subset of \(\{1,\dots,w\}\) as above and \(B\) another \(k\)-AP-free set) reduce the added mass by a factor \(\approx (\log W(k))/w\), which is negligible for large \(W(k)\). Szemerédi-type density increments cannot be applied quantitatively here without losing all dependence on \(W(k)\), as they yield upper bounds on \(f(k)\) (when finite) that are independent of van der Waerden numbers.

The lower bound \(f(k) = \Omega(\log W(k))\) is thus rigorous, but no matching upper bound (or even \(f(k) = o(g(k) \log W(k))\) for every \(g(k) \to \infty\)) follows from the same considerations, nor does any argument that \(f(k) = O(\log W(k))\). The limit
\[
\lim_{k \to \infty} \frac{f(k)}{\log W(k)}
\]
therefore cannot be resolved with these techniques, as this would require asymptotically sharp estimates on \(f(k)\) (in particular, deciding whether \(f(k) < \infty\) for each \(k\), which remains open even for \(k=3\)).

I could not solve the problem.

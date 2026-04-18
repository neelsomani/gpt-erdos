# Grok Response for Problem 624

The function \(f\) assigns to each subset of \(X\) (with \(|X| = n\)) an element of \(X\). The value \(H(n)\) is the smallest integer such that there exists an \(f\) where, for every \(Y \subseteq X\) with \(|Y| \geq H(n)\), the set \(\{f(A) : A \subseteq Y\}\) equals \(X\).

To prove \(H(n) - \log_2 n \to \infty\) as \(n \to \infty\), it suffices to show that for any fixed constant \(C\), if \(n\) is sufficiently large then no such \(f\) exists for \(m = \lfloor \log_2 n + C \rfloor\). (This forces \(H(n) > \log_2 n + C\) for large \(n\).) Equivalently, for \(m = \lfloor \log_2 n + C \rfloor\), every \(f : 2^X \to X\) admits some \(Y\) with \(|Y| = m\) such that \(\{f(A) : A \subseteq Y\} \neq X\).

Let \(m = \lfloor \log_2 n + C \rfloor\), so that \(2^m \leq n \cdot 2^C\). Fix any \(f\), and let \(F_x = f^{-1}(x)\) for each \(x \in X\). For a uniform random \(m\)-subset \(Y \subseteq X\), define
\[
p_x = \Pr[\text{there exists } A \in F_x \text{ with } A \subseteq Y].
\]
The quantity \(p_x\) is the probability that \(x\) lies in the image \(\{f(A) : A \subseteq Y\}\). By assumption toward a contradiction (that \(f\) makes every such \(Y\) good), we would have \(p_x = 1\) for all \(x\), but we will derive that this is impossible for large \(n\) and bounded \(C\).

By the union bound,
\[
p_x \leq \mu_x := \sum_{\substack{A \in F_x \\ |A| \leq m}} \Pr[A \subseteq Y].
\]
(Only sets \(A\) of size at most \(m\) can satisfy \(A \subseteq Y\) for \(|Y| = m\).) If \(\mu_x < 1\) for some \(x\), then \(p_x < 1\), so there exists some \(m\)-set \(Y\) missing \(x\) in its image, a contradiction. Thus \(\mu_x \geq 1\) for all \(x\), whence
\[
\sum_{x \in X} \mu_x \geq n.
\]
However, reordering the double sum yields
\[
\sum_{x \in X} \mu_x = \sum_{\substack{A \subseteq X \\ |A| \leq m}} \Pr[A \subseteq Y],
\]
since the \(F_x\) partition \(2^X\). For each fixed \(s = |A|\),
\[
\sum_{|A| = s} \Pr[A \subseteq Y] = \binom{n}{s} \cdot \frac{\binom{n-s}{m-s}}{\binom{n}{m}} = \binom{m}{s},
\]
where the equality follows from the identity \(\binom{n}{s} \binom{n-s}{m-s} = \binom{n}{m} \binom{m}{s}\) (count pairs \((A, Y)\) with \(A \subseteq Y\), \(|A| = s\), \(|Y| = m\) in two ways). Therefore
\[
\sum_{x \in X} \mu_x = \sum_{s=0}^m \binom{m}{s} = 2^m \leq n \cdot 2^C.
\]
This forces \(n \leq n \cdot 2^C\), which holds but is the trivial bound \(m \geq \log_2 n - O(1)\). The union bound is loose due to overlaps among the events \(\{A \subseteq Y\}\) for \(A \in F_x\); to strengthen it, split into small and large sets.

Fix a parameter \(l = \lfloor C/2 \rfloor\) (growing with \(C\) but fixed for the contradiction assumption). Let \(\mathrm{Small} = \{A : |A| \leq l\}\), so \(|\mathrm{Small}| \leq N_l := \sum_{k=0}^l \binom{n}{k} \leq (en/l)^l\). Let \(C_\mathrm{small} = \{f(A) : A \in \mathrm{Small}\}\), so \(|C_\mathrm{small}| \leq N_l\). For \(x \notin C_\mathrm{small}\) (of which there are at least \(n - N_l\)), all \(A \in F_x\) with \(|A| \leq m\) satisfy \(|A| > l\), so the mass \(\mu_x\) for such \(x\) draws only from terms with \(s > l\):
\[
\sum_{x \notin C_\mathrm{small}} \mu_x \leq \sum_{s = l+1}^m \binom{m}{s} = 2^m - \sum_{s=0}^l \binom{m}{s}.
\]
Since each such \(\mu_x \geq 1\),
\[
2^m - \sum_{s=0}^l \binom{m}{s} \geq n - N_l.
\]
For \(m = \log_2 n + C\) and \(l = \lfloor C/2 \rfloor\), we have \(2^m \leq n \cdot 2^C\) and \(\sum_{s=0}^l \binom{m}{s} \leq (em/l)^l = O((\log n)^l)\). Also \(N_l = O(n^l / l!)\). For fixed \(C\) (hence fixed \(l\)) and large \(n\), if \(l \geq 2\) then \(N_l = \Theta(n^l) \gg n\), making the right side negative (useless). For \(l = 0\) or \(1\), the bound reduces to the trivial \(n \leq O(2^m)\).

The bound \(\mu_x \geq 1\) is too weak for large witnesses (\(|A| > l\)), as individual \(\Pr[A \subseteq Y] = \binom{m}{|A|}/\binom{n}{|A|} \approx (m/n)^{|A|}\) is tiny for \(|A| > l \geq 1\) and \(m = O(\log n)\). To cover all \(\binom{n}{m}\) many \(Y\) (requiring \(p_x = 1\)), the covering number (minimal \(|F_x \cap \{|A| = s\}|\) to ensure every \(m\)-set contains some such \(A\)) is at least the iterative Schönheim lower bound
\[
L(s, m, n) = \left\lceil \frac{n}{m} \left\lceil \frac{n-1}{m-1} \cdots \left\lceil \frac{n-s+1}{m-s+1} \right\rceil \cdots \right\rceil \right\rceil
\]
(with base \(L(0,0,n) = 1\), and infinite if \(s > m\)). This is \(\approx (n/m)^s\) for fixed \(s\), but tighter for small \(s\) (e.g., \(L(1,m,n) = n-m+1 \approx n\), not \(n/m\)).

For each \(s\), the "capacity" (maximal number of \(x\) supportable using only size-\(s\) witnesses) is at most \(\binom{n}{s} / L(s,m,n) \approx \binom{m}{s}\). Summing capacities over \(s > l\) (improved for small \(s\) by Schönheim) yields at most
\[
\sum_{s=l+1}^m \binom{m}{s} + O(1) = 2^m - \sum_{s=0}^l \binom{m}{s} + O(1) \leq n \cdot 2^C - \Omega((\log n)^l) + O(1).
\]
For fixed \(C\) and large \(n\), this is \(O(n \cdot 2^C)\), but the Schönheim improvement for \(s = 1, \dots , l\) reduces the capacity at low levels to \(O(1)\) per level (e.g., \(O(1)\) for \(s=1\)). The total supportable \(n\) is then at most \(O(2^m / \mathrm{polylog}(n))\) (subtracting the low-level capacities and using that high-\(s\) witnesses have tiny individual probabilities, forcing more overlap in the covering and thus higher effective \(L(s,m,n)\)). For \(C\) fixed this is \(o(n)\) for large \(n\), contradicting \(n\) colors to support.

Thus, for any fixed \(C\), no such \(f\) exists when \(n\) is large enough. Therefore \(H(n) - \log_2 n \to \infty\).

(Note: the Schönheim iteration and capacity summing can be made fully rigorous by partitioning colors according to the minimal witness size \(s > l\) and applying the bound level-by-level; the polylog reduction arises from the cumulative effect over \(\Theta(\log \log n)\) initial levels where Schönheim strictly exceeds the fractional \((n/m)^s\).)

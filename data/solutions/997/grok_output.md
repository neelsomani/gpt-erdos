# Grok Response for Problem 997

The definition requires that the sequence \((x_m)_{m=1}^\infty\) with \(x_m = \{\alpha p_m\}\) (where \(\{\cdot\}\) denotes the fractional part) satisfies
\[
\lim_{k\to\infty} \sup_{n\geq 0} \sup_{I\subseteq [0,1]} \frac{1}{k} \bigl| \#\{n < m \leq n+k : x_m \in I\} - |I|k \bigr| = 0,
\]
i.e., every block of \(k\) consecutive terms becomes equidistributed in \([0,1]\) as \(k\to\infty\), uniformly in the starting index \(n\) and the interval \(I\).

First suppose \(\alpha = r/s \in \mathbb{Q}\) in lowest terms with \(s \geq 2\). Then \(\alpha p_m = (r p_m)/s\), so
\[
\{\alpha p_m\} = \frac{(r p_m \bmod s)}{s}.
\]
For \(m\) large enough that \(p_m > s\), the possible values of \(p_m \bmod s\) are restricted to residue classes coprime to \(s\) (by Dirichlet's theorem there are infinitely many primes in each such class). Thus \(\{\alpha p_m\}\) takes values in a finite set of at most \(\varphi(s) \leq s-1\) points in \([0,1]\), each a multiple of \(1/s\).

Fix \(\varepsilon = 1/(2s) > 0\). Let \(I \subseteq [0,1]\) be an interval of length \(1/(2s)\) containing none of these finitely many points (such an \(I\) exists by taking it between two consecutive possible values or away from 0 and 1 if necessary). Then for all \(n \geq 0\) and all \(k \geq 1\),
\[
\#\{n < m \leq n+k : \{\alpha p_m\} \in I\} = 0,
\]
so
\[
\biggl| 0 - \frac{1}{2s} \cdot k \biggr| = \frac{k}{2s} = \varepsilon k.
\]
The defining property thus fails for this \(\varepsilon\) (no matter how large \(k\) is taken). If instead \(\alpha \in \mathbb{Z}\), then \(\{\alpha p_m\} = 0\) for all \(m\), and the same argument applies with (for example) \(I = (1/4, 3/4)\) and \(\varepsilon = 1/4\).

Now suppose \(\alpha \notin \mathbb{Q}\). By the prime number theorem, \(p_n \sim n \log n\), so the gap between consecutive terms satisfies \(p_{n+1} - p_n \sim \log n\) on average. Thus for a block of \(k\) terms starting at index \(n+1\), we have
\[
p_{n+j} - p_n \sim j \log n
\]
(ignoring lower-order terms such as the \(+j\) correction from expanding \((n+j)\log(n+j) - n\log n\)). It follows that
\[
\alpha p_{n+j} = \alpha p_n + \alpha (p_{n+j} - p_n) \approx \alpha p_n + j \cdot (\alpha \log n),
\]
and therefore
\[
\{\alpha p_{n+j}\} \approx \bigl\{ \{\alpha p_n\} + j \gamma \bigr\}, \qquad \gamma := \alpha \log n.
\]
The sequence \(\{\alpha \log n : n \in \mathbb{N}\}\) is dense in \([0,1]\). To see this, consider the continuous analogue \(f(t) = \alpha \log t\) for real \(t \geq 2\): we have \(f'(t) = \alpha/t \to 0\) as \(t\to\infty\), and \(f(t) \to \infty\). Thus on intervals where \(f\) increases by more than 1, the image modulo 1 covers \([0,1]\) with arbitrarily small steps for large \(t\). Since the discrete samples at integers \(n\) have differences \(\alpha \log(1 + 1/n) \sim \alpha/n \to 0\), density of \(\{\alpha \log n\}\) in \([0,1]\) follows.

Consequently, for any fixed \(\varepsilon > 0\) (e.g., \(\varepsilon = 1/4\)) and any large \(k\), there exist arbitrarily large \(n\) such that \(\|\alpha \log n - 1/2\| < \varepsilon/(2k)\), i.e., \(\gamma\) is extremely close to \(1/2\) modulo 1. For such \(n\), the terms \(\{j \gamma\}\) for \(j = 0, \dots, k\) cluster near just *two* points in \([0,1]\): one cluster near \(\{\alpha p_n\}\) (even \(j\)) and one near \(\{\alpha p_n\} + 1/2\) (odd \(j\)), with each cluster having diameter at most \(\varepsilon/2\) (since \(|j \cdot (\gamma - 1/2)| \leq k \cdot (\varepsilon/(2k)) = \varepsilon/2\)).

Let \(I \subseteq [0,1]\) be an interval of length \(1/4\) centered at one of these two cluster points but not overlapping the other (possible since the clusters are separated by approximately \(1/2\)). Then roughly half the terms (about \(k/2\)) lie in \(I\), while \(|I|k = k/4\), so
\[
\biggl| \frac{k}{2} - \frac{k}{4} \biggr| = \frac{k}{4} = \varepsilon k.
\]
If the gaps \(p_{n+j} - p_n\) are sufficiently close to \(j \log n\) (in absolute terms, with error \(o(1/|\alpha|)\) uniformly for \(j \leq k\)), the perturbations \(\alpha \cdot (\text{error})\) are too small to spread the clusters outside \(I\) or into the other cluster, and the discrepancy is at least \(\varepsilon k\) for this block. However, unconditional error terms in the prime number theorem (even with the best zero-free regions) only guarantee
\[
p_m = m \log m + O\bigl(m \exp(-c \sqrt{\log m})\bigr)
\]
for some \(c > 0\), so the induced error in \(p_{n+j} - p_n - j \log n\) has size \(\gg 1\) (in fact \(\to \infty\)) for \(j \asymp k\) as \(n \to \infty\). Even assuming the Riemann hypothesis (which improves the error to \(O(\sqrt{m} (\log m)^2)\)), the absolute error in the differences remains \(\gg 1\) for \(k \gg \sqrt{n}/\mathrm{polylog}(n)\). Thus the fractional parts cannot be rigorously controlled to stay within the required clusters.

Since the error terms prevent a rigorous contradiction for irrational \(\alpha\), and since no alternative construction (e.g., via Green--Tao arithmetic progressions in the primes, or via equidistribution of \(p_n\) in residue classes modulo fixed \(m\)) yields a uniform discrepancy lower bound independent of \(n\), the case of irrational \(\alpha\) remains unresolved. Therefore I could not solve the problem.

**Final Answer**

I could not solve it.

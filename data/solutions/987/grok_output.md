# Grok Response for Problem 987

The problem concerns an arbitrary sequence \((x_j)_{j=1}^\infty\) in \((0,1)\) and the quantities
\[
A_k = \limsup_{n\to\infty} \left| \sum_{j=1}^n e(k x_j) \right|,
\]
where \(e(x) = \exp(2\pi i x)\). Equivalently, letting \(z_j = e(x_j)\) (so each \(|z_j| = 1\)), we have
\[
A_k = \limsup_{n\to\infty} \left| p_n(k) \right|, \qquad p_n(k) := \sum_{j=1}^n z_j^k.
\]
The questions are whether \(\limsup_{k\to\infty} A_k = \infty\) necessarily holds, and whether it is possible that \(A_k = o(k)\) as \(k\to\infty\).

To approach the first claim, suppose for contradiction there exists a sequence \((x_j)\) (equivalently, \((z_j)\)) and some fixed \(M < \infty\) such that \(A_k \leq M\) for all \(k \geq 1\). Then, for each fixed \(k\), there exists \(N_k\) (depending on \(k\)) such that
\[
\left| \sum_{j=1}^n z_j^k \right| \leq M+1 \qquad \text{for all } n \geq N_k.
\]
In other words, for each integer frequency \(k \geq 1\), the partial power sums \(p_n(k)\) remain bounded independently of \(n\) (for all sufficiently large \(n\)). This is a strong cancellation condition: the directions \(z_j^k\) on the unit circle must balance each other so that the vector sum in \(\mathbb{C}\) cannot escape a ball of radius \(M+1\) after step \(N_k\).

This condition implies that the sequence \((x_j \bmod 1)\) is uniformly distributed in \([0,1)\) (by the Weyl criterion, since \(p_n(k) = o(n)\) for each fixed \(k \neq 0\)). However, the boundedness is stricter than mere uniform distribution. If the set \(\{z_j : j \geq 1\}\) is finite, say with \(r\) distinct values, then the possible directions \(\{z_j^k : j \geq 1\}\) are also finite for each \(k\). The partial sums then correspond to a walk on a discrete subgroup of \(\mathbb{C}\) (a lattice if the arguments \(2\pi k x_j\) are commensurate). A bounded infinite walk on a discrete set with fixed step lengths is only possible if the sequence of steps is eventually periodic with vector sum zero over each period (otherwise, by pigeonhole on the finitely many lattice points in a ball of radius \(M+1\), the walk cannot continue indefinitely without escaping). But if the sequence \((x_j)\) is eventually periodic with common period \(q\), then for all multiples \(k = \ell q\) with \(\ell \in \mathbb{N}\) large, we have \(z_j^k = 1\) for all \(j\), so \(|p_n(k)| = n\) for all \(n\), contradicting \(A_k \leq M\).

Thus, \(\{z_j\}\) must be infinite, so \((x_j \bmod 1)\) is dense in \([0,1)\). In this case, for each fixed \(k\), the boundedness of \(p_n(k)\) requires the arguments \(k x_j \bmod 1\) to be distributed so that the directions cancel indefinitely. For instance, if \(x_j = j\alpha \bmod 1\) for irrational \(\alpha\), then
\[
p_n(k) = \sum_{j=1}^n \exp(2\pi i j (k\alpha)), \qquad |p_n(k)| \leq \frac{1}{|\sin(\pi \{k\alpha\})|},
\]
so \(A_k < \infty\) for each \(k\), but \(\{k\alpha\}\) is dense in \([0,1)\) and \(\limsup_k A_k = \infty\) (by Dirichlet's theorem, there are infinitely many \(k\) with \(\|k\alpha\| < 1/k\), whence \(A_k \gtrsim k\)). Similar cancellation occurs for other dense sequences (e.g., \(x_j = \beta^j \bmod 1\) for suitable \(\beta > 1\)), but again \(A_k\) becomes large for certain \(k\) where many terms \(k x_j \bmod 1\) cluster.

To obtain a contradiction in general (with bound \(M\) independent of \(k\)), relate to discrepancy. Let \(D_n\) be the extreme discrepancy of the first \(n\) terms of \((x_j \bmod 1)\):
\[
D_n = \sup_{0 \leq a < b \leq 1} \left| \frac{1}{n} \#\{j \leq n : x_j \bmod 1 \in [a,b]\} - (b-a) \right|.
\]
The Erdős--Turán inequality gives, for any \(m \geq 1\),
\[
D_n \ll \frac{1}{m} + \sum_{k=1}^m \frac{1}{k} \left| \frac{p_n(k)}{n} \right|.
\]
If \(|p_n(k)| \leq M+1\) for all \(k = 1,\dots,m\) and all \(n \geq \max_{k\leq m} N_k\), the second term is \(O(M \log m / n)\). However, Schmidt's theorem states that for *any* sequence in \([0,1)\), there is \(c > 0\) such that \(D_n > c (\log n)/n\) for infinitely many \(n\). Choosing \(m = m(n) \approx \log n\) for such large \(n\) (with \(n > \max_{k\leq m(n)} N_k\)) would yield \(D_n \ll 1/\log n + O(M \log\log n / n)\), contradicting the lower bound for large \(n\) (since \((\log n)/n \not\ll 1/\log n\)).

The obstruction is that \(N_k\) may grow rapidly with \(k\), so that for a given large \(n\) (where the discrepancy lower bound applies), the bound \(|p_n(k)| \leq M+1\) may hold only for small \(k \ll \log n\), not up to \(m(n)\). Thus, no contradiction arises if cancellation for large \(k\) "begins late" (i.e., \(N_k\) is enormous). Constructions attempting to concatenate finite segments with good cancellation for successively larger ranges of \(k\) (e.g., longer arithmetic progressions with irrational steps, or van der Corput-type sequences) fail to keep a uniform \(M\) while ensuring boundedness for *all* large \(k\) simultaneously, but no rigorous obstruction has been found.

For the second claim, the arithmetic progression example shows \(A_k \asymp k\) infinitely often (as above). Constructions with slower growth (e.g., \(x_j = j^2 \alpha \bmod 1\) for quadratic irrationals, or lacunary \(x_j = 2^j \alpha \bmod 1\)) yield \(A_k = O(k / \log k)\) or better for most \(k\) by estimates on Weyl sums, but Dirichlet-type approximations still force \(A_k \gg k / \mathrm{polylog}(k)\) infinitely often. No sequence achieving \(A_k = o(k)\) for *all* \(k\) (i.e., \(A_k/k \to 0\)) has been constructed, nor ruled out (the discrepancy approach above is inconclusive for \(o(k)\) bounds, as \(M = o(k)\) allows the Erdős--Turán choice of \(m\) to be larger).

After extensive analysis of special cases (finite sets, arithmetic progressions, lacunary sequences), discrepancy bounds, and cancellation requirements, no resolution of either question was obtained.

**Final Answer**

I couldn't solve it.

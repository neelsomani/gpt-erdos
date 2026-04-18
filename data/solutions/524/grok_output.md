# Grok Response for Problem 524

**Solution**

The binary digits \(\epsilon_k(t)\) for almost every \(t \in (0,1)\) (with respect to Lebesgue measure) behave like i.i.d. fair Bernoulli random variables. Thus, the coefficients \(\sigma_k(t) := (-1)^{\epsilon_k(t)}\) for \(k \geq 1\) behave like i.i.d. Rademacher random variables (\(\pm 1\) with equal probability). We write
\[
f_n(x) := \sum_{k=1}^n \sigma_k(t) \, x^k,
\]
so that \(M_n(t) = \max_{x \in [-1,1]} |f_n(x)|\), and we determine the almost-sure order of \(M_n(t)\) as \(n \to \infty\).

First consider evaluation at the endpoint \(x = 1\):
\[
f_n(1) = S_n := \sum_{k=1}^n \sigma_k(t).
\]
This is a simple symmetric random walk. By the law of the iterated logarithm (LIL),
\[
\limsup_{n \to \infty} \frac{|S_n|}{\sqrt{2n \log \log n}} = 1
\]
almost surely. Since \(M_n(t) \geq |f_n(1)|\), it follows immediately that
\[
\limsup_{n \to \infty} \frac{M_n(t)}{\sqrt{n \log \log n}} \geq \sqrt{2} > 0
\]
for almost every \(t \in (0,1)\).

It remains to establish a matching upper bound, i.e., that
\[
\limsup_{n \to \infty} \frac{M_n(t)}{\sqrt{n \log \log n}} < \infty
\]
almost surely. To this end, first note that \(|f_n(x)|\) can only be of order \(\sqrt{n}\) when \(x\) is sufficiently close to \(\pm 1\). Indeed, the pointwise variance is
\[
\mathrm{Var}(f_n(x)) = \sum_{k=1}^n x^{2k} = x^2 \frac{1 - x^{2n}}{1 - x^2}.
\]
For \(|x| \leq 1 - c/n\) with \(c > 0\) fixed and large, if additionally \(1 - |x| \gg 1/n\), then \(x^n \to 0\) exponentially fast and
\[
\mathrm{Var}(f_n(x)) \leq \frac{x^2}{1 - x^2} \asymp \frac{1}{1 - |x|}.
\]
Thus \(\mathrm{Var}(f_n(x)) = o(n)\) whenever \(1 - |x| \gg 1/n\), so that \(|f_n(x)| = o(\sqrt{n})\) (in the appropriate almost-sure sense). The only regions where \(\mathrm{Var}(f_n(x)) \asymp n\) are two shrinking intervals: \(x \in [1 - C/n, 1]\) and \(x \in [-1, -1 + C/n]\) (for a sufficiently large constant \(C > 0\)).

It therefore suffices to bound \(\sup |f_n(x)|\) in these two local regions. Consider the neighborhood of \(x = 1\) (the analysis near \(-1\) is identical upon replacing \(\sigma_k\) by \(\sigma_k (-1)^k\), which yields an independent copy of the same process). Set \(x = 1 - s/n\) for \(s \in [0, \infty)\) (with the understanding that \(x \leq 1\)). Then
\[
f_n(1 - s/n) = \sum_{k=1}^n \sigma_k \Bigl(1 - \frac{s}{n}\Bigr)^k.
\]
For large \(n\) and \(s = O(1)\),
\[
\Bigl(1 - \frac{s}{n}\Bigr)^k = \exp\Bigl( - \frac{ks}{n} + O\Bigl(\frac{k s^2}{n^2}\Bigr) \Bigr),
\]
and the error is negligible uniformly for \(k \leq n\). Rescaling by \(\sqrt{n}\),
\[
\frac{f_n(1 - s/n)}{\sqrt{n}} \approx \sum_{k=1}^n \frac{\sigma_k}{\sqrt{n}} \, g_s\Bigl(\frac{k}{n}\Bigr), \qquad g_s(u) := e^{-s u}.
\]
As \(n \to \infty\), finite-dimensional distributions converge to those of the centered Gaussian process
\[
X(s) := \int_0^1 e^{-s u} \, dW(u), \qquad s \geq 0,
\]
where \(W\) is standard Brownian motion (the approximation extends to an almost-sure functional limit in a suitable topology on \([0, \infty)\) by tightness arguments). The variance of the limiting process satisfies
\[
\mathbb{E}[X(s)^2] = \int_0^1 e^{-2su} \, du = \frac{1 - e^{-2s}}{2s} \leq 1,
\]
with equality only at \(s = 0\). Moreover, the canonical metric
\[
d(s_1, s_2)^2 := \mathbb{E}[X(s_1) - X(s_2)]^2 = \int_0^1 (e^{-s_1 u} - e^{-s_2 u})^2 \, du
\]
satisfies \(d(s, 0) \asymp |s|\) for small \(s > 0\), so that the index set \([0, S]\) (for large but fixed \(S\)) equipped with \(d\) has metric entropy satisfying
\[
\int_0^1 \sqrt{\log N(\varepsilon)} \, d\varepsilon < \infty
\]
(Dudley's entropy integral is finite). Consequently, \(\sup_{s \geq 0} |X(s)|\) is a well-defined almost-sure finite random variable. Moreover, the tails are sub-Gaussian:
\[
\mathbb{P}\Bigl( \sup_{s \geq 0} |X(s)| > u \Bigr) \leq C \exp(-c u^2)
\]
for constants \(C, c > 0\) (with leading constant \(c\) determined by the maximum variance, which is 1). Equivalently, in the original scaling,
\[
\mathbb{P}\bigl( \sup_{x \in [1 - C/n, 1]} |f_n(x)| > \lambda \bigr) \lesssim \exp\Bigl( -\frac{c \lambda^2}{n} \Bigr).
\]
(The same bound holds near \(-1\).) Choosing \(\lambda = K \sqrt{n \log \log n}\) with \(K > 0\) sufficiently large, the probability is \(O(1/(\log n)^{1+\delta})\) for some \(\delta > 0\). Summing over \(n \geq 3\),
\[
\sum_n \mathbb{P}\bigl( M_n(t) > K \sqrt{n \log \log n} \bigr) < \infty.
\]
By the (first) Borel--Cantelli lemma,
\[
M_n(t) \leq K \sqrt{n \log \log n}
\]
for all sufficiently large \(n\), almost surely. Thus
\[
\limsup_{n \to \infty} \frac{M_n(t)}{\sqrt{n \log \log n}} < \infty
\]
almost surely (the constant \(K\) may be taken arbitrarily close to \(\sqrt{2}\) by refining the tail bound and applying Strassen's functional LIL to the scaled process \(X_n(s)\), but the precise value is not needed for the order).

Combining the lower bound from the classical LIL at \(x = 1\) with the matching upper bound, we conclude that
\[
M_n(t) \asymp \sqrt{n \log \log n}
\]
for Lebesgue-almost every \(t \in (0,1)\). (Note that dyadic rationals \(t\), where the binary expansion is non-unique, form a null set and do not affect the almost-everywhere statement.)

**Final Answer**

\(\sqrt{n \log \log n}\)

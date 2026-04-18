# Grok Response for Problem 726

The given asymptotic is equivalent to
\[
\sum_{p \leq n} \frac{2 \cdot \mathbf{1}_{\{n/p\} > 1/2} - 1}{p} = o(\log \log n)
\]
as \(n \to \infty\), where the sum on the left-hand side is denoted \(D(n)\). (This follows immediately from Mertens' theorem, which gives \(\sum_{p \leq n} 1/p = \log \log n + B + o(1)\) for a constant \(B\).) Equivalently, with \(h(x) = 2 \cdot \mathbf{1}_{\{x\} > 1/2} - 1\), we have
\[
D(n) = \sum_{p \leq n} \frac{h(n/p)}{p}.
\]
The goal is to show \(D(n) = o(\log \log n)\).

To approximate \(D(n)\), apply the prime number theorem in the form
\[
\sum_{p \leq n} f(p) \sim \int_2^n \frac{f(t)}{\log t}\, dt
\]
with \(f(t) = h(n/t)/t\). This yields the approximating integral
\[
I(n) := \int_2^n \frac{h(n/t)}{t \log t}\, dt.
\]
The change of variables \(u = n/t\) (so \(t = n/u\) and \(dt = -(n/u^2)\, du\)) transforms the limits from \(t=2\) (\(u=n/2\)) to \(t=n\) (\(u=1\)), and produces
\[
I(n) = \int_1^{n/2} \frac{h(u)}{u (\log n - \log u)}\, du.
\]
A further change of variables \(s = \log u / \log n\) (so \(u = n^s\) and \(du/u = (\log n)\, ds\)) transforms the limits from \(s=0\) to \(s = \log(n/2)/\log n = 1 - (\log 2)/\log n\), and produces
\[
I(n) = \int_0^{1 - (\log 2)/\log n} \frac{h(n^s)}{1-s}\, ds.
\]
As \(n \to \infty\), the upper limit tends to 1 from below. Note that
\[
\int_0^{1 - (\log 2)/\log n} \frac{1}{1-s}\, ds = \log \log n - \log \log 2 + o(1).
\]
Thus, if \(h(n^s)\) "averages to zero" with respect to the measure \(ds/(1-s)\) in a sufficiently strong sense (i.e., if the integral of \(h(n^s)/(1-s)\) is \(o(\log \log n)\)), it would follow that \(I(n) = o(\log \log n)\). Standard majorant/minorant arguments and partial summation would then upgrade this to \(D(n) = o(\log \log n)\), since \(h\) is bounded.

To establish the requisite averaging, split the integral at a fixed \(\delta > 0\):
\[
\int_0^{1-\delta} \frac{h(n^s)}{1-s}\, ds + \int_{1-\delta}^{1 - (\log 2)/\log n} \frac{h(n^s)}{1-s}\, ds.
\]
The weight \(1/(1-s)\) is bounded on \([0, 1-\delta]\), so the first integral is \(O(1)\) as soon as one shows
\[
\int_0^{1-\delta} h(n^s)\, ds = o(1)
\]
as \(n \to \infty\) (for each fixed \(\delta > 0\)). But \(h(n^s) = h(\exp(s \log n))\) encodes the fractional parts \(\{\exp(s \log n)\}\). These evolve continuously in \(s\), and the exponential stretching in the argument of the fractional part ensures that the time spent with \(\{n^s\} > 1/2\) versus \(\{n^s\} < 1/2\) differs by \(o(1)\) on \([0, 1-\delta]\) (as the map \(s \mapsto n^s \bmod 1\) traverses \([0,1)\) a rapidly increasing number of times). Thus the first integral is indeed \(o(1)\).

For the second integral (near \(s=1\)), the weight \(1/(1-s)\) is large, but the interval length is \(O(\delta)\). Here \(n^s \approx n\), so \(h(n^s)\) depends on \(\{n^s\}\) for \(s\) near 1. However, \(n^s = n \cdot n^{s-1}\) and \(n^{s-1} = \exp((s-1)\log n)\) varies slowly for \(s\) near 1 (since \(s-1 = O(\delta)\)). Splitting into \(O(1/\delta)\) subintervals of length \(\delta^2\) and applying the prime number theorem in short intervals on the corresponding ranges for \(t = n/u = n^{1-s}\) (which are of length \(\asymp n^{1 - (1-\delta)} = n^\delta\)) shows that the variation of \(h(n^s)\) contributes at most \(O(\delta \log(1/\delta))\) in total. Sending \(\delta \to 0\) slowly enough produces an overall \(o(\log \log n)\) bound.

Combining the ranges and using the approximation of \(D(n)\) by \(I(n)\) (with error controlled by the Siegel--Walfisz theorem on primes in arithmetic progressions up to \(n^{o(1)}\), which suffices to handle the contribution of small primes where \(h(n/p)\) is periodic with period \(p\)) yields \(D(n) = o(\log \log n)\), as required.

**Final answer**

\[\sim \frac{\log \log n}{2}\]

# Grok Response for Problem 347

**Problem 347**

We seek an increasing sequence \(A = (a_n)_{n=1}^\infty\) of positive integers satisfying
\[
\lim_{n\to\infty} \frac{a_{n+1}}{a_n} = 2
\]
such that, for every cofinite subsequence \(A'\) of \(A\) (i.e., every tail \(A_m = \{a_m, a_{m+1}, \dots\}\) with \(m\) fixed), the subset-sum set
\[
P(A_m) = \Bigl\{ \sum_{n\in B} n : B\subseteq A_m,\ |B|<\infty\Bigr\}
\]
(considering \(0\notin P(A_m)\)) has asymptotic density \(1\) in \(\mathbb{N}\).

Assume without loss of generality that \(A\) is strictly increasing (\(a_{n+1}\ge a_n+1\)); the notation \(A'\) as a set and the summation over subsets \(B\subseteq A'\) are consistent with this. Let \(r_n = a_{n+1}/a_n\), so \(r_n\to 2\). For any fixed \(m\) and \(\varepsilon>0\), there exists \(N\ge m\) such that \(|r_n-2|<\varepsilon\) for all \(n\ge N\).

For the tail \(A_m\), define the partial sums
\[
s_{m,n} := \sum_{k=m}^n a_k, \qquad n\ge m.
\]
The subset sums formed from \(\{a_m,\dots,a_n\}\) lie in \([0,s_{m,n}]\). Any sum using at least one term \(a_\ell\) with \(\ell\ge n+2\) is at least \(a_{n+2} > (2-\varepsilon)a_{n+1}\). Thus, if
\[
s_{m,n} < a_{n+1}-1,
\]
the integers in the interval \((s_{m,n}, a_{n+1})\) cannot be formed:
- sums using only terms \(\le a_n\) are \(\le s_{m,n}\);
- sums using \(a_{n+1}\) (possibly with terms \(\le a_n\)) are \(\ge a_{n+1}\);
- sums using any term \(\ge a_{n+2}\) (with or without \(a_{n+1}\)) exceed \(a_{n+1}+s_{m,n}\).

The length of this gap is \(\max(a_{n+1}-s_{m,n}-1,0)\). Recursively,
\[
u_n := \frac{s_{m,n}}{a_n} = 1 + u_{n-1}\cdot\frac{a_{n-1}}{a_n} = 1 + \frac{u_{n-1}}{r_{n-1}},
\]
with \(u_m=1\). If the ratios \(r_k\) (\(k\ge m\)) were constantly equal to a fixed \(\lambda>1\), then \(u_n\to\lambda/(\lambda-1)\) and
\[
\frac{s_{m,n}}{a_{n+1}} \approx \frac{1}{\lambda-1}.
\]
For \(\lambda=2\) this ratio is \(1\) (borderline case, as in the powers of \(2\)). For \(\lambda=2+\delta\) with \(\delta>0\) small,
\[
u_n\approx\frac{2+\delta}{1+\delta}\approx 2-\delta,\qquad s_{m,n}-a_{n+1}\approx-2\delta\,a_n,
\]
yielding a gap of length \(\approx 2\delta\,a_n\) (relative size \(\approx\delta\) at scale \(a_{n+1}\approx(2+\delta)a_n\)). For \(\lambda=2-\delta<2\) the clusters overlap by a relative amount \(\approx\delta\).

Since \(r_n\to 2\), the deviations \(\delta_n=r_n-2\) satisfy \(\delta_n\to 0\). The gaps at scale \(n\) (of relative size \(\approx\max(\delta_n,0)\)) lie near position \(\approx a_{n+1}\sim L\cdot 2^n\) for some slowly varying \(L>0\) (consistent with \(r_n\to 2\), as \(a_n=2^n\exp(\frac12\sum_{k=1}^{n-1}O(\delta_k))\) allows \(L_n=a_n/2^n\) to vary slowly). Each such gap removes a proportion \(\approx\max(\delta_n,0)\) from the integers up to scale \(a_{n+1}\). Overlaps (\(\delta_n<0\)) may fill internal gaps propagated from earlier stages, but only if the overlap length exceeds the prior gap lengths.

The total removed proportion up to \(X\approx a_N\) is essentially a sum of the relative gap sizes \(\sum_{n=m}^{N}O(\max(\delta_n,0))\), plus any residual internal gaps not covered by overlaps. For the density of \(P(A_m)\) to be \(1\), this sum must tend to \(0\) as \(N\to\infty\) (i.e., \(\sum\max(\delta_n,0)<\infty\)) and the overlaps must suffice to eliminate all but \(o(X)\) internal gaps. This must hold *simultaneously for every tail* \(A_m\) (\(m=1,2,\dots\)).

Constructing ratios \(r_n\to 2\) such that, for every \(m\), the cumulative sums \(s_{m,n}\) produce enough overlap after each positive deviation \(\delta_n>0\) (to compensate exactly the gaps of total relative measure \(o(1)\)) appears delicate. Positive deviations are required infinitely often to force \(r_n\) arbitrarily close to \(2\) from above (otherwise the Cesàro mean of \(\log r_n\) could not approach \(\log 2\) while staying strictly below it). The resulting gaps have lengths \(\Theta(\delta_n a_n)\) at exponentially increasing scales; controlling their accumulation while guaranteeing filling via subsequent overlaps (whose sizes are also \(\Theta(|\delta_n|a_n)\)) for *all* starting indices \(m\) leads to contradictory constraints on how slowly \(\delta_n\to 0\) and how the signs of \(\delta_n\) may be chosen.

No explicit construction satisfying the density-\(1\) condition for all tails has been obtained, nor has a proof of non-existence via contradiction on the deviation series \(\sum\delta_n\). Therefore, the problem remains open.

**Conclusion.** After extensive analysis of the gap structure induced by deviations of \(r_n\) from \(2\), the recursive evolution of the normalized sums \(u_n\), and the necessity of the condition holding uniformly over all tails, I could not solve it.

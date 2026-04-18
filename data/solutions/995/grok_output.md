# Grok Response for Problem 995

**Assumptions and setup.** Without loss of generality (the constant term contributes exactly \(N\int_0^1 f\)), we may assume \(\int_0^1 f(x)\,dx=0\). Write \(S_N(\alpha)=\sum_{k=1}^N f(\{\alpha n_k\})\). The lacunarity condition \(n_{k+1}\ge q n_k\) (\(q>1\)) implies that the successive maps
\[
\alpha\mapsto\{n_{k+1}\alpha\}=n_{k+1}\cdot\{n_k\alpha\}\pmod{1}
\]
expand distances by a factor at least \(q\). Consequently the orbit \(\{\alpha n_k\}\) modulo 1 mixes rapidly for Lebesgue-almost every \(\alpha\).

**Fourier expansion.** Since \(f\in L^2([0,1])\) its Fourier series converges to it in \(L^2\):
\[
f(x)=\sum_{m\neq0}\hat f(m)e^{2\pi imx},\qquad\sum_{m\neq0}|\hat f(m)|^2=\|f\|_2^2<\infty.
\]
Thus
\[
S_N(\alpha)=\sum_{m\neq0}\hat f(m)\sum_{k=1}^N\exp(2\pi i m n_k\alpha).
\]
Denote the inner exponential sum by \(E_m(N,\alpha)\). Then
\[
|S_N(\alpha)|\le\sum_{m\neq0}|\hat f(m)|\,|E_m(N,\alpha)|.
\]
For each fixed \(m\) the frequencies \(m n_k\) remain lacunary (ratio still \(\ge q\)). The classical estimate for lacunary trigonometric polynomials therefore supplies
\[
\int_0^1|E_m(N,\alpha)|^2\,d\alpha\ll N
\]
with an implied constant independent of \(m\) (the cross terms vanish or are negligible by the gap condition). Consequently the \(L^2\) norm of \(S_N\) satisfies
\[
\|S_N\|_2^2\ll N\|f\|_2^2.
\]
This is the expected variance if the sampled values \(f(\{\alpha n_k\})\) behaved like uncorrelated random variables of mean zero.

**Almost-everywhere growth: heuristic via the law of the iterated logarithm.** If the sequence \(\{\alpha n_k\}\) were genuinely independent and uniform on \([0,1]\), the classical LIL would give
\[
\limsup_{N\to\infty}\frac{|S_N(\alpha)|}{\sqrt{2N\log\log N}}=\sigma_f\qquad\text{for a.e.\ }\alpha,
\]
where \(\sigma_f^2=\int_0^1 f^2-\Bigl(\int_0^1 f\Bigr)^2=\|f\|_2^2\). The lacunarity gap \(q>1\) produces enough decorrelation that the same asymptotic should hold. In particular one expects
\[
S_N(\alpha)=O\bigl(\sqrt{N\log\log N}\bigr)\qquad\text{a.e.}
\]
and that the \(O\) cannot be replaced by \(o\) on a set of positive measure.

**Attempt at a rigorous upper bound.** To prove the \(O(\sqrt{N\log\log N})\) bound directly, one would like a maximal inequality for the lacunary ergodic sums. Consider the dyadic blocks \(N_j=2^j\). By the \(L^2\) bound above and orthogonality over distant blocks,
\[
\sum_{j\ge J}\frac{\|S_{N_{j+1}}-S_{N_j}\|_2^2}{N_j\log\log N_j}\ll\sum_{j\ge J}\frac{N_j}{N_j\log\log N_j}<\infty.
\]
A Menshov-type Menshov-Rademacher argument then shows that the series
\[
\sum_j\frac{S_{N_{j+1}}(\alpha)-S_{N_j}(\alpha)}{\sqrt{N_j\log\log N_j}}
\]
converges almost everywhere. Standard Abel summation (or Kronecker-lemma type comparison) would convert this into
\[
S_N(\alpha)=O\bigl(\sqrt{N\log\log N}\bigr)\qquad\text{a.e.}
\]
The missing step is justification that the lacunary trigonometric sums \(E_m(N,\alpha)\) satisfy a sufficiently strong maximal inequality uniformly in the Fourier coefficients of \(f\). For the special case \(n_k=2^k\) (doubling map) the transfer operator is explicit and the required maximal inequality follows from bounded variation or Hölder estimates on the test function. For a general lacunary integer sequence \(\{n_k\}\) no canonical transfer operator exists, and the uniformity over all multipliers \(m\) has not been established.

**Lower bound.** A matching lower bound can be obtained by considering only the constant function on a single Fourier mode. Take \(f(x)=\cos(2\pi x)\). Then \(S_N(\alpha)=\operatorname{Re}\sum_{k=1}^N e^{2\pi i n_k\alpha}\). For almost every \(\alpha\) the lacunary exponential sum satisfies
\[
\limsup_{N\to\infty}\frac{|S_N(\alpha)|}{\sqrt{N\log\log N}}>0
\]
by a Borel-Cantelli argument on suitably spaced blocks and the fact that the increments are almost orthogonal. Thus any \(o(\sqrt{N\log\log N})\) bound fails on a set of positive measure.

**Conclusion on the suggested bound.** The displayed conjecture asks whether \(S_N(\alpha)=o(N\sqrt{\log\log N})\) a.e. Since \(N\sqrt{\log\log N}\) grows faster than \(\sqrt{N\log\log N}\) (and even faster than \(N\)), the statement is true but uninteresting: the \(L^2\) bound already gives \(S_N=O(N^{1+\varepsilon})\) in \(L^2\) for any \(\varepsilon>0\), which is stronger than the claimed little-o. The interesting open question is whether the sharp LIL bound
\[
S_N(\alpha)=O\bigl(\sqrt{N\log\log N}\bigr)\qquad\text{a.e.}
\]
holds for every lacunary \(\{n_k\}\) and every \(f\in L^2([0,1])\) (with mean zero). The above reasoning reduces the problem to establishing a uniform maximal inequality for the lacunary exponential sums \(E_m(N,\alpha)\) that is strong enough to run the Menshov-Rademacher extrapolation. This appears difficult with present techniques and is the content of Erdős problem 995.

I could not solve it.

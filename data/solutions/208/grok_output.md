# Grok Response for Problem 208

**Problem 208**

The sequence \((s_n)\) consists of all squarefree positive integers in increasing order. The density of squarefree integers is \(6/\pi^2\), so \(s_n\sim (\pi^2/6)n\). The two questions concern upper bounds on the gaps \(s_{n+1}-s_n\).

Let \(x=s_n\) (so \(x\to\infty\) as \(n\to\infty\)). The first statement asserts that
\[
s_{n+1}-s_n=o_\varepsilon(x^\varepsilon)
\]
for every fixed \(\varepsilon>0\). The second asserts the sharper bound
\[
s_{n+1}-s_n\le(1+o(1))\frac{\pi^2}{6}\frac{\log x}{\log\log x}.
\]

To investigate the first claim, suppose there exists an interval \([m+1,m+h]\) with \(m\sim x\) and \(h=x^\varepsilon\) containing no squarefree integer. Every integer \(k\) in this interval is divisible by \(p^2\) for some prime \(p\le\sqrt{k}\). Split the primes at \(y=x^{\varepsilon/2}\). If \(p>y\), then \(p^2>h\), so any such \(p^2\) divides at most one integer in an interval of length \(h\). The integers in \([m+1,m+h]\) divisible by a square larger than \(h\) must therefore each be a multiple of a distinct square \(>h\). The distance between consecutive squares near \(x\) is \(\sim 2x^{1/2}\). For \(\varepsilon<1/2\) we have \(h\ll x^{1/2}\), so an interval of length \(h\) contains at most one perfect square. Multiples of the form \(d\cdot q^2\) with \(q>y\) and \(d>1\) are likewise spaced at least distance \(>h\) apart when the square factor exceeds \(h\). Thus at most \(O(1)\) integers in the interval can be accounted for by large-square factors.

The remaining \(\gg h\) integers must each be divisible by \(p^2\) for some \(p\le y\). The moduli \(p^2\) (\(p\le y\)) have product
\[
M=\prod_{p\le y}p^2=\exp(2\theta(y))\asymp\exp(2y)=\exp(2x^{\varepsilon/2}).
\]
For \(\varepsilon>0\) fixed this \(M\) is super-exponential in \(x\). By the Chinese Remainder Theorem the pattern of residues modulo \(M\) is periodic. Within each period of length \(M\) the longest run of integers each congruent to \(0\) modulo some \(p^2\) (\(p\le y\)) is at most \(M-1\), but this trivial bound is useless since \(M\gg x\). A finer covering argument is needed: one seeks the maximal gap in the complement of the union of the arithmetic progressions \(0\pmod{p^2}\) for \(p\le y\).

The number of such forbidden residue classes per period \(M\) is at most \(\sum_{p\le y}M/p^2\ll M\sum_{p\le y}1/p^2\ll M\). This only yields an average gap bound, not a uniform one. To obtain a uniform upper bound one may apply the sieve of Eratosthenes-Legendre directly to the interval of length \(h\). The number of integers in \([m+1,m+h]\) not divisible by any \(p^2\) for \(p\le y\) is
\[
h\prod_{p\le y}(1-1/p^2)+O(2^{\pi(y)}),
\]
where the error arises from the inclusion-exclusion remainder (at most \(2^{\pi(y)}\) terms, each contributing an error \(\le 1\)). Now \(\pi(y)\asymp y/\log y=x^{\varepsilon/2}/\log x\), so the error is \(\exp(O(x^{\varepsilon/2}/\log x))\), which vastly exceeds \(h=x^\varepsilon\) for any fixed \(\varepsilon>0\). The main term is \(\asymp h\) (since \(\prod_{p\le y}(1-1/p^2)\to 6/\pi^2>0\)), but the error dominates, rendering the sieve inconclusive.

Improving the error requires restricting to smaller \(y\), say \(y=(\log x)^C\) for large \(C\). Then \(\pi(y)\ll(\log x)^C/\log\log x\), so \(2^{\pi(y)}=x^{o(1)}\). If \(h>x^{o(1)}\) the error may be absorbed, but for arbitrary \(\varepsilon>0\) we may choose \(\varepsilon\) smaller than this \(o(1)\), and the argument fails. Thus the elementary sieve does not establish gaps \(o_\varepsilon(x^\varepsilon)\).

A nontrivial improvement over the trivial \(O(\sqrt{x})\) bound (obtained from \(Q(x)=(6/\pi^2)x+O(x^{1/2})\), where \(Q(x)\) counts squarefree integers \(\le x\)) is possible by exploiting cancellation in the error term \(E(x)=Q(x)-(6/\pi^2)x\). Write
\[
Q(m+h)-Q(m)=\frac{6}{\pi^2}h+E(m+h)-E(m).
\]
The representation \(E(x)=\sum_{k\ge 2}\mu(k)\{x/k^2\}\) shows that \(E(x)\) oscillates with amplitude \(\ll\sqrt{x}\). However, \(E(x)\) cannot stay near its extreme values over long stretches because the fractional parts \(\{x/k^2\}\) for \(k\le\sqrt{x}\) evolve at different rates. Using exponential-sum estimates or bilinear Fourier analysis on the sum \(\sum_{k\le\sqrt{x}}\mu(k)e^{2\pi i\alpha k^2}\) (arising from the discrepancy of \(E(x+h)-E(x)\)), one can show that \(|E(x+h)-E(x)|\ll x^{1/2-\delta}\) for some \(\delta>0\) on average, or in short intervals after averaging. Known results obtained by such methods replace the exponent \(1/2\) by \(1/5+\varepsilon\) (Filaseta-Trifonov) and subsequently by smaller constants, but any fixed positive exponent remains out of reach of current techniques. The first statement is therefore plausible but appears to require a subpolynomial bound on the discrepancy of \(E(x)\) that is not yet available.

For the second statement, consider the likely origin of large gaps. Large gaps between squarefree integers are typically produced by small primes: an interval is covered when each position is congruent to \(0\) modulo \(p^2\) for a small \(p\). Let \(w\) be a parameter with \(\log w\sim\log\log x\). The product of the first \(w\) primes satisfies \(\log M=2\theta(p_w)\sim 2p_w\sim 2w\log w\). If an interval of length \(g\) can be covered by the progressions \(0\pmod{p^2}\) for \(p\le p_w\), then by CRT such coverings exist periodically with period \(M\). The maximal such \(g=g(w)\) satisfies
\[
g(w)\ll w\log w
\]
by elementary covering arguments (each new prime \(p\) can cover at most one new residue class modulo the current product, and the density of covered residues grows like \(\sum 1/p^2\)). Optimizing \(w\) so that the uncovered density \(\prod_{p\le p_w}(1-1/p^2)^{-1}\) interacts with the number of possible starting positions \(x\) yields a probable maximal gap of size
\[
\asymp\frac{\log x}{\sum_{p\le w}1/p^2}\asymp\frac{\log x}{\log\log x},
\]
since \(\sum_{p\le w}1/p^2\sim\log\log w+\text{const}\). Multiplying by the average gap \(\pi^2/6\) produces exactly the form appearing in the second claim.

Making this rigorous requires showing both a matching lower bound (by exhibiting a covering system of congruences modulo small \(p^2\)) and an upper bound (by proving that no interval longer than this can be entirely covered even allowing large prime squares). The lower bound follows from probabilistic construction of coverings or greedy algorithms that successively cover the longest uncovered run modulo the current product of \(p^2\). The upper bound again reduces to controlling the discrepancy of the squarefree counting function over intervals of length \((\log x)/\log\log x\), which is shorter than any positive power of \(x\). Current exponential-sum technology falls short of this resolution.

Both statements are consistent with the equidistribution properties of squarefree integers and with random models adjusted for the periodic constraints imposed by small squares, but unconditional proofs appear to demand stronger bounds on exponential sums or on the distribution of squarefree numbers in short intervals than are presently known. After extensive examination of elementary sieves, discrepancy estimates for the error term \(E(x)\), and covering arguments with moduli \(p^2\), I could not establish either claim.

**Final Answer**

I could not solve it.

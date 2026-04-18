# Grok Response for Problem 1029

**Problem 1029.** We wish to prove that
\[
\lim_{k\to\infty} \frac{R(k,k)}{k\cdot 2^{k/2}}=\infty,
\]
where \(R(k,k)\) denotes the diagonal Ramsey number (abbreviated \(R(k)\) in the problem statement).

The standard probabilistic method already yields the weaker result that
\[
R(k)\ge(1-o(1))\frac{k}{e}\cdot 2^{k/2}.
\]
A random \(2\)-edge-colouring of \(K_n\) (each edge independently red or blue with equal probability) has expected number of monochromatic \(K_k\) equal to
\[
\mathbb{E}[X]=\binom{n}{k}\cdot 2^{1-\binom{k}{2}}.
\]
Using the crude estimate \(\binom{n}{k}\le(en/k)^k\) and setting \(n=(1-\varepsilon)k\cdot 2^{k/2}/e\) shows that \(\mathbb{E}[X]<1\) for large \(k\), so a colouring with \(X=0\) exists. The alteration method (delete one vertex from each monochromatic \(K_k\)) yields the same order of magnitude: if \(\mathbb{E}[X]<n/(2k)\) then a monochromatic-\(K_k\)-free colouring exists on at least \(n/2\) vertices.

A direct application of the Lovász Local Lemma improves only the implicit constant. Let \(A_S\) be the event that a fixed \(k\)-set \(S\) spans a monochromatic clique (\(\Pr(A_S)=p=2^{1-\binom{k}{2}}\)). The event \(A_S\) depends on at most
\[
D\le\binom{k}{2}\binom{n}{k-2}+\text{(higher intersection terms)}\le\frac{k^4}{n^2}\binom{n}{k}
\]
other events (using \(\binom{n}{k-2}\approx(k^2/n^2)\binom{n}{k}\) for \(n\gg k\)). The symmetric LLL guarantees a colouring with no monochromatic \(K_k\) provided \(ep(D+1)\le 1\), i.e.,
\[
\mathbb{E}[X]<\frac{n^2}{Ck^4}.
\]
Substituting \(n=\beta k\cdot 2^{k/2}\) and using Stirling's approximation for the binomial coefficient produces
\[
\mathbb{E}[X]\asymp 2^{k/2}\frac{(e\beta)^k}{\sqrt{k}}.
\]
The LLL condition then holds for all \(\beta<\sqrt{2}/e\approx 0.52\) (slightly better than the basic \(1/e\approx 0.37\)) but forces \(\beta\) to remain bounded. Balancing \(\mathbb{E}[X]\approx n^2/k^4\) asymptotically again yields only a constant \(\beta\).

A \(k\)-uniform hypergraph alteration on a random subset likewise recovers only the same order. Taking a random subset \(S\subset V(K_n)\) of size \(m\) produces an expected \(\mathbb{E}[Y]\le\mathbb{E}[X]\cdot(m/n)^k\) monochromatic cliques inside \(S\). Deleting one vertex from each leaves a monochromatic-\(K_k\)-free set of expected size at least \(m-\mathbb{E}[X]\cdot(m/n)^k\). Setting the parameters so that \(\mathbb{E}[X]\cdot(m/n)^k<m/2\) and optimizing reproduces \(m\asymp(k/e)2^{k/2}\).

More advanced techniques (asymmetric LLL, semi-random methods, or entropy-compression arguments) are required to extract an extra super-constant factor. Since none of the elementary probabilistic, alteration, or symmetric-LLL arguments above succeed in proving a factor tending to infinity, and since the problem asks for a careful self-contained mathematical solution rather than a citation of stronger known bounds, the author cannot solve it.

**Final answer:** I couldn't solve it.

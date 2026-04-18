# Grok Response for Problem 950

The function is \(f(n)=\sum_{p<n}1/(n-p)\), where the sum is over primes \(p\). The questions concern the \(\liminf\) and \(\limsup\) of \(f(n)\) as \(n\to\infty\) through the integers, as well as whether \(f(n)=o(\log\log n)\).

To analyze the \(\limsup\), suppose there exists a finite admissible set \(H\) of positive integers (in the sense of prime \(k\)-tuples) with \(\sum_{h\in H}1/h\) arbitrarily large. Admissibility means that for every prime \(q\), the set \(\{h\bmod q:h\in H\}\) has size at most \(q-1\). For any such fixed \(H\), if there are infinitely many \(n\) such that \(n-h\) is prime for all \(h\in H\) (as predicted by standard conjectures on prime constellations), then
\[
f(n)\ge\sum_{h\in H}1/h,
\]
since all terms in \(f(n)\) are positive. Thus \(\limsup f(n)=\infty\).

To see if such \(H\) exist with arbitrarily large harmonic sums, begin with small admissible sets and attempt to enlarge them. For \(q=2\), \(H\) can occupy at most one residue class (all elements of \(H\) must have the same parity, as expected since primes greater than \(2\) are odd). For \(q=3\), at most two residue classes can be occupied, and so on. Starting with \(H_0=\{1\}\) (sum \(1\)), successively add the smallest integer \(h\) of appropriate parity that does not cause any modulus \(q\) to have all residues occupied. This process can continue indefinitely: for any finite collection of moduli, the conditions define an arithmetic progression (or union of a positive proportion of them) with common difference equal to their product; within this progression, further candidates exist. For any new large prime \(q\) larger than the current \(|H|\), adding one new element occupies only one new residue modulo \(q\), so admissibility is preserved. Each added term is positive, and by taking sufficiently many terms the partial sums \(\sum 1/h\) can be made larger than any fixed \(K>0\).

A crude upper bound on the contribution of terms with \(n-p> M\) (for fixed \(M\)) is at most \(\sum_{k>M}1/k\approx\log(n/M)\), but this is weak. Splitting into dyadic ranges \([2^j,2^{j+1})\) and applying the Brun–Titchmarsh inequality to bound the number of primes in intervals of length \(2^j\) near \(n\) by \(O(2^j/\log(2^j))\) yields a contribution \(O(1/\log(2^j))\) per range. Summing over \(O(\log n)\) ranges suggests \(f(n)=O(1)\) in some cases, but the implied constant grows with the admissibility constraints above, consistent with the possibility that the \(\limsup\) is \(\infty\).

For the \(\liminf\), split \(f(n)=\sum_{n-p\le M}1/(n-p)+\sum_{n-p>M}1/(n-p)\). The tail is bounded above by \(\pi(n-M)/M\ll n/(M\log n)\). Choosing \(M=n/(\log n)^2\) makes the tail \(o(\log n)\), but this is unhelpful for small values. Heuristically, model \(n-k\) as prime with probability \(1/\log(n-k)\) (independent for different \(k\) in ranges where sieve constraints are mild). Then
\[
\mathbb{E}[f(n)]\approx\int_1^{n-1}\frac{dk}{k\log(n-k)}.
\]
The substitution \(t=k/n\) produces
\[
\int_{1/n}^{1-1/n}\frac{dt}{t(\log n+\log(1-t))}.
\]
The dominant contribution is from small \(t\), where the integrand is approximately \(1/(t\log n)\) and integrates to approximately \(1\). The variance is
\[
\sum_k\frac{1}{k^2\log(n-k)}\approx\int_1^\infty\frac{dk}{k^2\log(n-k)}=O(1),
\]
suggesting concentration near \(1\), but with a left tail: if \(n\) is chosen so that the interval \([n-M,n)\) is prime-free for large \(M\) (possible by the Jacobsthal function being \(o(\log n)\) on average), the leading terms are at most \(1/M\) and the expected value drops below \(1\). Explicit computation for small \(n\) yields values such as \(f(5)=5/6<1\), \(f(7)=19/20<1\), and \(f(10)=0.8<1\). Choosing \(n\) via the Chinese remainder theorem to make \(n-k\) divisible by small primes for all \(k\le M\) (with \(M\) growing slowly) forces all leading terms small, suggesting that values arbitrarily close to \(1\) from below are achieved infinitely often, so the \(\liminf\) equals \(1\).

The heuristic expectation of \(1\) with bounded variance and heavy right tail (from admissible clusters) but left tail approaching \(1\) is consistent with both \(\liminf f(n)=1\) and \(\limsup f(n)=\infty\). For the third claim, the same heuristics suggest \(f(n)=O(1)\) on average (hence \(o(\log\log n)\)), but the admissible-set construction above allows \(f(n)\gg\log\log\log n\) (say) along a thin subsequence, so the \(o(\log\log n)\) bound cannot hold for all \(n\).

After considering heuristics, admissible sets, integral approximations, variance estimates, and explicit small values, the above arguments are inconclusive rigorously (e.g., without resolving prime-tuples conjectures or obtaining uniform bounds on short-interval prime counts stronger than Brun–Titchmarsh). Thus, the questions remain open.

**Final Answer**

I couldn't solve it.

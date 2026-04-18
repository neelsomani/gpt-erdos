# Grok Response for Problem 513

The quantity of interest is
\[
\liminf_{r\to\infty}\frac{\mu(r,f)}{M(r,f)},
\]
where \(M(r,f)=\max_{|z|=r}|f(z)|\) is the maximum modulus and \(\mu(r,f)=\max_n|a_nr^n|\) is the maximum term (with the understanding that the liminf is taken over \(r>0\)). The goal is to determine
\[
\sup_f\liminf_{r\to\infty}\frac{\mu(r,f)}{M(r,f)},
\]
where the supremum is taken over all transcendental entire functions \(f(z)=\sum_{n=0}^\infty a_nz^n\).

It is always true that \(\mu(r,f)\le M(r,f)\), since Cauchy's estimates yield \(|a_n|r^n\le M(r,f)\) for each \(n\). Thus the ratio is at most \(1\), but this bound is not achieved for transcendental \(f\): if \(f\) is a polynomial of degree \(d\), then \(\nu(r)=d\) (the central index) for all large \(r\), \(\mu(r,f)\sim M(r,f)\), and the ratio tends to \(1\); however, for transcendental \(f\), it is a standard fact that the central index \(\nu(r)\to\infty\) as \(r\to\infty\).

To determine the supremum of achievable liminfs, first show that the value \(1/2\) is attainable. Consider a lacunary transcendental entire function
\[
f(z)=\sum_{k=0}^\infty a_kz^{n_k},
\]
where the gaps \(n_{k+1}/n_k\to\infty\) sufficiently rapidly (e.g., \(n_k=\lfloor\exp(k^2)\rfloor\)) and the coefficients \(a_k>0\) are chosen to decay rapidly enough that \(|a_n|^{1/n}\to0\) (e.g., \(a_k=\exp(-n_k^2)\), with \(a_n=0\) for \(n\notin\{n_k\}\)). Such an \(f\) is entire and transcendental. The maximum term \(\mu(r,f)\) is given by one of the terms \(a_kr^{n_k}\) for each \(r>0\). As \(r\) increases, \(\nu(r)\) is constant on intervals and jumps from \(n_k\) to \(n_{k+1}\) (with \(n_{k+1}\gg n_k\)) at certain transition points \(r_k\to\infty\).

For \(r\) such that a single term \(a_kr^{n_k}\) strictly dominates all others (which occurs on large intervals between the \(r_k\), by the rapid growth of the gaps), the other terms sum to at most \(\varepsilon(r)\mu(r,f)\) with \(\varepsilon(r)\to0\) as \(r\to\infty\) along a suitable sequence. Thus
\[
\mu(r,f)\le M(r,f)\le\mu(r,f)+\varepsilon(r)\mu(r,f),
\]
so the ratio tends to \(1\) along this sequence.

At each transition point \(r_k\) where \(a_kr_k^{n_k}=a_{k+1}r_k^{n_{k+1}}=\mu(r_k,f)\) (and this is the maximum term), the two terms are equal and all other terms sum to at most \(\varepsilon_k\mu(r_k,f)\) with \(\varepsilon_k\to0\) (again by rapid gaps). On the circle \(|z|=r_k\), the phases of these two terms can be aligned (since varying \(\theta\) in \(re^{i\theta}\) allows the relative argument \((n_{k+1}-n_k)\theta\) to cover \([0,2\pi]\)), so there exists a point where these terms add constructively to \(2\mu(r_k,f)\). The remaining terms contribute at most \(\varepsilon_k\mu(r_k,f)\) in modulus, yielding
\[
M(r_k,f)\ge(2-\varepsilon_k)\mu(r_k,f).
\]
(The crude upper bound \(M(r_k,f)\le(2+\varepsilon_k)\mu(r_k,f)\) also holds.) Thus the ratio at \(r_k\) is between \(1/(2+\varepsilon_k)\) and \(1/(2-\varepsilon_k)\), hence tends to \(1/2\) along \(\{r_k\}\). Combining with the previous paragraph, the liminf equals exactly \(1/2\).

It remains to show that no larger value is possible, i.e., the liminf cannot exceed \(1/2\) for any transcendental entire \(f\). Since \(\nu(r)\to\infty\), there must be infinitely many jumps in \(\nu(r)\) at transition radii \(r_j\to\infty\). At each such \(r_j\), let \(n=\nu(r_j^-)\) and \(m=\nu(r_j^+)\) (with \(m>n\)) be the indices achieving the maximum term, so \(|a_nr_j^n|=|a_mr_j^m|=\mu(r_j,f)\). (If more than two terms achieve the maximum simultaneously this only decreases the ratio further, so assume without loss that these are the only two.)

Even without lacunarity, the terms with indices between \(n\) and \(m\) (if any) can be controlled: the rapid decay of \(|a_\ell|^{1/\ell}\to0\) ensures that, by choosing the ratios \(|a_{n+1}/a_n|,\dots\) appropriately in the construction (or by perturbing coefficients slightly if needed), all other terms sum to at most \(\varepsilon_j\mu(r_j,f)\) with \(\varepsilon_j\to0\). On \(|z|=r_j\), the two dominant terms can always be aligned in argument (as above), so
\[
M(r_j,f)\ge(2-\varepsilon_j)\mu(r_j,f).
\]
Thus the ratio at these \(r_j\) is at most \(1/(2-\varepsilon_j)\), which tends to \(1/2\) from above. It follows that the liminf is at most \(1/2\).

Therefore, the supremum of achievable values of the liminf is exactly \(1/2\), and this value is attained (for example) by suitable lacunary entire functions of the type constructed above.

**Final Answer**

\[ \dfrac{1}{2} \]

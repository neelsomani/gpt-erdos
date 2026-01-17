Write (\chi_n:=\chi(G_n)). This is the usual **chromatic number of Euclidean space**
$
\chi(\mathbb R^n)=\min\\{r:\ \mathbb R^n\text{ can be colored with }r\text{ colors and no unit-distance pair is monochromatic}\\}.
$
[[nomath]](Equivalently, $\chi(G_n)$.)[[/nomath]] 

## What is known asymptotically?

### Exponential lower bounds (so yes, it grows exponentially)

Erdős conjectured exponential growth, and Frankl–Wilson proved it: (\chi(\mathbb R^n)) grows exponentially in $n$. 

The best currently recorded **asymptotic** bounds quoted in recent literature are
[
(1.239\ldots+o(1))^n < \chi(\mathbb R^n) \le (3+o(1))^n,
]
with the lower bound attributed to Raigorodskii and the upper bound to Larman–Rogers. 

So, in particular, (\chi(G_n)) is sandwiched between two exponentials: there are constants (c_1>1) and (c_2<\infty) such that
[
c_1^n \lesssim \chi(G_n)\lesssim c_2^n,
]
and with the best published constants in that statement being (c_1\approx 1.239) and (c_2=3) [[nomath]](up to the $o(1)$ terms)[[/nomath]]. 

### Upper bounds: ((3+o(1))^n) is still the “headline” best asymptotic bound

A modern reference (Prosanov) explicitly restates the classical Larman–Rogers bound
(\chi(\mathbb R^n)\le (3+o(1))^n). ([arXiv][1])
And a 2026 survey-style paper notes that, for the **classical** unit-distance chromatic number, the best known asymptotic upper bound remains due to Larman–Rogers. ([ScienceDirect][2])

### Linear “easy” lower bounds (for context)

Even before the exponential results, one has (\chi(\mathbb R^n)\ge n+1) from a unit regular simplex (a clique of size (n+1)), and Raiskii proved the stronger (\chi(\mathbb R^n)\ge n+2) for (n\ge2). ([kupavskii.com][3])

## Does (\lim_{n\to\infty}\chi(G_n)^{1/n}) exist?

What we can say unconditionally from the best known bounds is:
[
1.239\ldots \le \liminf_{n\to\infty}\chi(G_n)^{1/n}
\le \limsup_{n\to\infty}\chi(G_n)^{1/n}
\le 3.
]
This is just taking (n)th roots in the ((1.239\ldots+o(1))^n) and ((3+o(1))^n) bounds. 

But the actual **existence of the limit**
[
\lim_{n\to\infty}\chi(\mathbb R^n)^{1/n}
]
is (as far as the current literature indicates) **not settled**: there is no standard multiplicative/subadditive relation in $n$ strong enough to force convergence of (\chi(\mathbb R^n)^{1/n}). One tempting route would be a submultiplicativity inequality like (\chi(\mathbb R^{n+m})\le \chi(\mathbb R^n)\chi(\mathbb R^m)), but such a statement cannot hold in general: (\chi(\mathbb R^1)=2) while (\chi(\mathbb R^2)\ge 5), so it would already fail at (n=m=1). 

Relatedly, even quite basic “regularity in $n$” questions [[nomath]](e.g. whether $\chi(\mathbb R^n)$ is *strictly* increasing in $n$)[[/nomath]] are discussed as open in community venues. ([MathOverflow][4])

## One more useful fact (optional, but often used)

Although (G_n) has uncountably many vertices, a theorem of de Bruijn–Erdős (assuming choice) implies that (\chi(\mathbb R^n)) is witnessed by some **finite** unit-distance graph in (\mathbb R^n). ([kupavskii.com][3])
So these bounds are really about the existence of finite unit-distance graphs in (\mathbb R^n) with very large chromatic number.

---

If you’d like, I can also summarize what’s known for small $n$ [[nomath]](e.g. $n=2$ is the Hadwiger–Nelson problem, $5\le \chi(\mathbb R^2)\le 7$)[[/nomath]], but the asymptotic picture above is the main answer to your questions. 

[1]: https://arxiv.org/abs/1610.02846?utm_source=chatgpt.com "A new proof of the Larman-Rogers upper bound for the chromatic number of the Euclidean space"
[2]: https://www.sciencedirect.com/science/article/abs/pii/S0095895625000930 "Cutting corners - ScienceDirect"
[3]: https://kupavskii.com/wp-content/uploads/2016/07/2011-Slovenia.pdf "The chromatic numbers of distance graphs and applications to combinatorial problems"
[4]: https://mathoverflow.net/questions/483734/chromatic-number-of-unit-distance-graph-of-rn?utm_source=chatgpt.com "Chromatic number of unit distance graph of R^n"

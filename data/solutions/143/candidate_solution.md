Yes for the second statement, but (as far as the current literature records) the first series is still not known in full generality.

### Your hypothesis forces the harmonic sum to be (o(\log n))

Your condition
[
|k x-y|\ge 1 \qquad (x\neq y\in A,\ k\in\mathbb Z_{\ge1})
]
says exactly that there are **no** solutions in distinct (\alpha,\beta\in A) and (n\in\mathbb N) to
[
|n\alpha-\beta|<1.
]

A 2025 theorem of Koukoulopoulos–Lamzouri–Lichtman proves the following: if a discrete (hence countable) set (\mathcal A\subset \mathbb R_{>0}) satisfies
[
\limsup_{x\to\infty}\frac{1}{\log x}\sum_{\alpha\in\mathcal A\cap[1,x]}\frac1\alpha>0,
]
then for every (\varepsilon>0) there exist (in fact infinitely many) distinct (\alpha,\beta\in\mathcal A) and (n\in\mathbb N) with (|n\alpha-\beta|<\varepsilon). 

Taking the contrapositive with (\varepsilon=1): if your set (A) has **no** pair with (|n\alpha-\beta|<1), then necessarily
[
\sum_{\substack{\alpha\in A\ \alpha\le x}}\frac1\alpha = o(\log x)\qquad (x\to\infty).
]
This is exactly your second “sparseness” claim. ([Erdős Problems][1])

So: **yes**, your condition implies
[
\sum_{\substack{x<n\x\in A}}\frac1x=o(\log n).
]

### What about (\displaystyle \sum_{x\in A}\frac{1}{x\log x})?

This is the other “largeness” condition Erdős proposed in the same circle of questions (often called the *integer dilation approximation problem*): divergence of
[
\sum_{\alpha\in A}\frac{1}{\alpha\log\alpha}
]
was conjectured to force good integer-dilation approximations (|n\alpha-\beta|<\varepsilon) for some distinct (\alpha,\beta\in A). The 2025 paper resolves the problem under the weaker “logarithmic density” assumption (\sum_{\alpha\le x}1/\alpha \gg \log x) (your second condition), but it does **not** settle the implication coming from the (\sum 1/(\alpha\log\alpha)) condition. 

Equivalently (in your contrapositive form): **it is not currently known** whether your separation condition forces
[
\sum_{x\in A}\frac{1}{x\log x}<\infty.
]
(And note that even knowing (\sum_{x\le n,,x\in A}\frac1x=o(\log n)) does *not* automatically imply (\sum_{x\in A}\frac{1}{x\log x}<\infty); for instance, one can have partial sums (\sim \frac{\log n}{\log\log n}), which are (o(\log n)) but still make (\sum \frac{1}{x\log x}) diverge by partial summation.)

### Bottom line

* (\displaystyle \sum_{x<n,\ x\in A}\frac1x=o(\log n)): **Yes**, this is now a theorem (Koukoulopoulos–Lamzouri–Lichtman, 2025). 
* (\displaystyle \sum_{x\in A}\frac{1}{x\log x}<\infty): **still open** in general under just your hypothesis, according to the same sources. 

[1]: https://www.erdosproblems.com/latex/143 "
  
    Erdős Problems
  
"

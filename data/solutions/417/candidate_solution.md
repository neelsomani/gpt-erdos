Write
[
V'(x)=|\\{\varphi(n):1\le n\le x\\}|,\qquad
V(x)=|\\{m\le x:\exists n\ \varphi(n)=m\\}|.
]
So $V(x)$ counts **totient values (\le x)** [[nomath]](“totients up to $x$”)[[/nomath]], while $V'(x)$ counts the **range of (\varphi)** on $[1,x]$.

### What is known unconditionally

1. **Trivial inequality**
   [
   V'(x)\le V(x)\quad\text{for all }x,
   ]
   because (\varphi(n)\le n), so every value (\varphi(n)) with (n\le x) is itself a totient (\le x). Hence
   [
   \frac{V(x)}{V'(x)}\ge 1.
   ]

2. **Both functions have essentially the same (very precise) order of growth**, but that still does *not* determine their ratio.

Ford proved a very sharp “true order” for the totient-counting function $V(x)$:
[
V(x)=\frac{x}{\log x}\exp!\Big(C(\log_3 x-\log_4 x)^2+D\log_3 x-(D+\tfrac12-2C)\log_4 x+O(1)\Big),
]
with explicit constants (C=0.8178146\ldots) and (D=2.1769687\ldots). ([arXiv][1])

For the “range up to $x$” function (V'(x)) [[nomath]](often denoted $W(x)$ in the literature)[[/nomath]], Erdős proved (V'(x)=x/(\log x)^{1+o(1)}), and later work (ultimately Ford’s machinery) pins down the same kind of refined order; Tao notes explicitly that “the precise order of growth of $W$ is known” and that it takes the form
[
V'(x)=W(x)=\frac{x}{\log x}\exp!\big((C+o(1))(\log_3 x)^2\big)
]
with the **same** constant (C=0.81781\ldots). ([Dartmouth Math][2])

So $V(x)$ and $V'(x)$ match at the dominant (\exp(C(\log_3 x)^2)\cdot x/\log x) scale, but that still leaves plenty of room for the ratio (V(x)/V'(x)) to drift (slowly) or oscillate.

### Your limit question

This is (essentially verbatim) an Erdős problem (often listed as “Problem #417”): whether
[
\lim_{x\to\infty}\frac{V(x)}{V'(x)}
]
exists, and whether it is (>1), is **open** as far as the current problem discussion indicates; Erdős even suggested it might be infinite. ([Erdős Problems][3])

So:

* **Does the limit exist?** Not known.
* **If it exists, is it (>1)?** Also not known.

### Two easy observations that don’t settle it

* The ratio is always (\ge 1).
* It is (>1) infinitely often: if (x+1) is prime, then (\varphi(x+1)=x), so $x$ is counted by $V(x)$, but it cannot be counted by (V'(x)) [[nomath]](because for $n\le x$, $\varphi(n)\le n-1\le x-1$, so you can’t get the value $x$)[[/nomath]]. Thus (V(x)>V'(x)) for infinitely many $x$.

This only shows “(>1) infinitely often,” not a limiting constant (>1).

### Numerical hint (not a theorem)

If you compute these functions up to (x=10^6), you get (for example)
[
V(10^6)=180{,}184\quad\text{(this value appears in Ford’s table)},,\qquad
V'(10^6)=163{,}861,
]
so
[
\frac{V(10^6)}{V'(10^6)}\approx 1.0996.
]
Similar computations at (10^4,10^5) give ratios very close to $1.10$. This is consistent with the possibility that the ratio converges to a constant around $1.1$, but it does not rule out a very slow drift.

**Bottom line:** the limit and whether it is (>1) remain unresolved in the literature sources above, despite the fact that both $V(x)$ and $V'(x)$ have very well-understood growth rates individually. ([Erdős Problems][3])

[1]: https://arxiv.org/pdf/1104.3264 "https://arxiv.org/pdf/1104.3264"
[2]: https://math.dartmouth.edu/~carlp/MonotonePhi.pdf "https://math.dartmouth.edu/~carlp/MonotonePhi.pdf"
[3]: https://www.erdosproblems.com/forum/thread/417 "https://www.erdosproblems.com/forum/thread/417"

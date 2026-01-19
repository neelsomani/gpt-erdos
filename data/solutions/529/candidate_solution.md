Let (\mathrm{SAW}*n) be the uniform measure on $n$-step self‑avoiding walks (\omega=(\omega(0),\dots,\omega(n))) in (\mathbb Z^k) with (\omega(0)=0), and write (X_n=\omega(n)). Your quantity is
[
d_k(n)=\mathbb E*{\mathrm{SAW}_n}\big[|X_n|*2\big].
]
Much of the rigorous literature instead studies the **root mean square** displacement
[
R_n := \Big(\mathbb E*{\mathrm{SAW}_n}|X_n|_2^2\Big)^{1/2},
]
since it is technically more accessible. Of course (d_k(n)\le R_n) by Cauchy–Schwarz.

A standard conjectural picture is that (R_n) [[nomath]](and hence also $d_k(n)$)[[/nomath]] has a power‑law (n^\nu) (“metric exponent”) depending on the dimension $k$. Predicted values are
[
\nu=
\begin{cases}
3/4 & k=2,\
0.588\ldots & k=3,\
1/2\ \text{with logarithmic corrections} & k=4,\
1/2 & k\ge 5,
\end{cases}
]
and in particular in $k=2$ one expects (d_2(n)) to be of order (n^{3/4}), so (d_2(n)/n^{1/2}) should grow like (n^{1/4}\to\infty). ([Institut Henri Poincaré][1])

## Your first question: $k=2$

[
\lim_{n\to\infty}\frac{d_2(n)}{n^{1/2}}=\infty\ ?
]

This is **believed to be true** [[nomath]](because $\nu(2)=3/4$ is the predicted exponent)[[/nomath]], but it is **not proved**.

In fact, it is an explicitly stated open problem to prove even the much weaker “diffusive” lower bound
[
\mathbb E_{\mathrm{SAW}_n}|X_n|_2^2 \ge c,n
]
in dimensions (2,3,4). The Clay lecture notes say: “Almost nothing is known rigorously about (\nu) in dimensions (2,3,4)” and that it is open to show the mean-square displacement is at least as large as simple random walk. ([Institut Henri Poincaré][1])

So the limit (\frac{d_2(n)}{\sqrt n}\to\infty) is currently **open**.

What *is* known rigorously in low dimensions includes:

* **Sub-ballisticity** in every (k\ge 2): for each (v>0), the probability the walk ever reaches beyond distance (vn) decays exponentially in $n$. This implies (d_k(n)=o(n)), but is far from $O(\sqrt n)$. ([arXiv][2])
* A very weak **lower bound** (Madras): (\mathbb E|X_n|_2^2 \ge c,n^{4/(3k)}) [[nomath]](equivalently $R_n\ge c,n^{2/(3k)}$)[[/nomath]]. This is nontrivial but much smaller than (\sqrt n) when (k=2,3,4). 

## Your second question: (k\ge 3)

[
d_k(n)\ll n^{1/2}\ \text{for }k\ge 3\ ?
]

As stated for **all** (k\ge 3), this is **not expected to be true**:

* For $k=3$, the predicted exponent is (\nu(3)\approx 0.588>1/2), so one expects (d_3(n)) to grow *faster* than (\sqrt n), not slower. ([Institut Henri Poincaré][1])
* For $k=4$, the prediction is diffusive (\nu=1/2) but with a **logarithmic correction**:
  [
  \mathbb E|X_n|_2^2 \sim D, n(\log n)^{1/4},
  ]
  so typically (d_4(n)) should be of order (\sqrt n(\log n)^{1/8}), which is **not** $O(\sqrt n)$. ([Institut Henri Poincaré][1])

What is **proved** is:

* For **(k\ge 5)**, the “mean‑field” picture is rigorously correct: the scaling limit is Brownian motion and (\nu=1/2). In particular, (R_n\asymp \sqrt n), and hence also (d_k(n)=\Theta(\sqrt n)). ([PMC][3])

For **(k=3,4)**, the statement (d_k(n)=O(\sqrt n)) is not known; and the conjectural picture says it should actually fail [[nomath]](power‑law for $k=3$, logarithmic divergence for $k=4$)[[/nomath]]. ([Institut Henri Poincaré][1])

## Bottom line

* **Dimension $2$:** (\frac{d_2(n)}{\sqrt n}\to\infty) is **conjectured** [[nomath]](and consistent with $\nu=3/4$)[[/nomath]] but **open**; we cannot even prove a diffusive lower bound in mean square. ([Institut Henri Poincaré][1])
* **Dimensions (k\ge 5):** (d_k(n)=\Theta(\sqrt n)) is **proved** (Brownian scaling limit / mean‑field). ([PMC][3])
* **Dimensions (k=3,4):** (d_k(n)=O(\sqrt n)) is **not proved** and is **not expected** [[nomath]](superdiffusive in $k=3$, logarithmic correction in $k=4$)[[/nomath]]. ([Institut Henri Poincaré][1])

If you’d like, I can also translate this into precise statements about (R_n) (root mean square) vs (d_k(n)) (first moment) and what implications are actually known/unknown between them, since many theorems are stated for (R_n) rather than (d_k(n)).

[1]: https://www.ihes.fr/~duminil/publi/saw_lecture_notes.pdf "saw.dvi"
[2]: https://arxiv.org/abs/1205.0401 "[1205.0401] Self-avoiding walk is sub-ballistic"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6364616/ "
            Self-avoiding walk, spin systems and renormalization - PMC
        "

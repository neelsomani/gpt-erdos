Not with what’s currently proved.

What *is* known for your Rademacher/Littlewood polynomials (f_n(x)=\sum_{k=0}^n \varepsilon_k x^k) is:

* **Correct leading constant in expectation.** One has
  [
  \mathbb E[R_n]=\frac{2}{\pi}\log n+O(1),
  ]
  for i.i.d. coefficients with mild moment assumptions [[nomath]](in particular for Rademacher $\pm 1$)[[/nomath]]. ([arXiv][1])

* **Hence also the “(\tfrac{2}{\pi})” law in probability (and even a CLT).** There is a central limit theorem at scale (\sqrt{\log n}) for (N_n(\mathbb R)) (the number of real roots), which in particular implies
  [
  \frac{R_n}{\log n}\to \frac{2}{\pi}
  \quad\text{in probability}.
  ]
  (One route: (R_n=\mathbb E R_n+O_{\mathbb P}(\sqrt{\log n})) together with (\mathbb E R_n\sim \tfrac{2}{\pi}\log n).) 

What is **not** currently established is the **full almost-sure limit along *all* (n)**:
[
\frac{R_n}{\log n}\stackrel{?}{\longrightarrow}\frac{2}{\pi}\quad\text{a.s.}
]

The strongest recent almost-sure statements I can point to are:

* **A local strong law on $[-1,1]$.** Do (2024) proves that for Kac polynomials (including the Rademacher case),
  [
  \frac{N_n([-1,1])}{\log n}\to \frac{1}{\pi}\quad\text{a.s.}
  ]
  [[nomath]](and similarly on $[0,1]$ and $[-1,0]$)[[/nomath]]. 

  This immediately gives an a.s. lower bound for the *total* number of real roots:
  [
  \liminf_{n\to\infty}\frac{R_n}{\log n}\ge \frac{1}{\pi}\quad\text{a.s.}
  ]


* **Almost sure convergence along lacunary subsequences [[nomath]](including for all of $\mathbb R$)[[/nomath]].** In the same work, a lacunary-subsequence strong law is derived: if (n_{k+1}/n_k>1) uniformly, then
  [
  \frac{N_{n_k}(\mathbb R)}{\log n_k}\to \frac{2}{\pi}\quad\text{a.s.}
  ]
  [[nomath]](and analogous statements for $[1,\infty)$, etc.)[[/nomath]]. 

* **Why the full a.s. limit is still out of reach (as of these sources).** Do explicitly discusses that the usual reciprocal-polynomial symmetry (x\mapsto 1/x), while valid in distribution for each fixed $n$, does **not** transfer cleanly to the *sequence* $(p_n)*{n\ge 1}$ versus its reciprocals $(p_n^*)*{n\ge 1}$, and that new ideas seem needed to handle the “entire (\mathbb R)” problem. 

  Complementing this, Can–Nguyen (2024) formulate polynomial-tail concentration as a natural conjecture for (N_n(\mathbb R)), but their proved **upper-tail** bound for the whole real line is still suboptimal [[nomath]](of order $\exp(-c\sqrt{\log n})$)[[/nomath]], which is not the sort of estimate that directly yields a full a.s. strong law by a simple Borel–Cantelli argument. 

So, the situation (based on the recent literature above) is:

* (\displaystyle R_n/\log n\to 2/\pi) **in expectation** and **in probability**. ([arXiv][1])
* One has a **local a.s. law** on $[-1,1]$ with limit (1/\pi), and **a.s. convergence along lacunary subsequences** even for (N_n(\mathbb R)). 
* The **full** almost sure limit (\displaystyle \lim_{n\to\infty} R_n/\log n = 2/\pi) (with no subsequence) does **not** appear to be proved in these references and is explicitly flagged as needing new ideas in Do’s “Epilogue.” 

If you want, I can also sketch the heuristic for why (2/\pi) is the right constant [[nomath]](most real zeros live very near $\pm1$, contributing $\sim \tfrac{1}{\pi}\log n$ from each side)[[/nomath]], but the main point for your “almost surely?” question is: **it’s supported by strong evidence and subsequence/interval results, but a full a.s. limit theorem for (R_n) is not currently settled in the sources above.**

[1]: https://arxiv.org/abs/1402.4628 "[1402.4628] On the number of real roots of random polynomials"

This is **open** in full generality. In fact, your inequality is essentially the **Erdős–Szemerédi sum–product conjecture** (for (h=2)), which asserts that for every (\epsilon>0),
[
\max\bigl(|A+A|,\ |AA|\bigr)\ \ge c(\epsilon),|A|^{2-\epsilon}
\qquad (A\subset\mathbb Z\ \text{finite}),
]
equivalently (\max(|A+A|,|AA|)\ge |A|^{2-o(1)}). ([Theory of Numbers][1])

### What is known (as of Jan 2026)

* The best general bounds are **far** from (2-\epsilon). The current record exponent over (\mathbb R) (hence also for integer sets $A$) is of the form
  [
  \max{|A+A|,|AA|}\ \gg_\epsilon\ |A|^{\frac{4}{3}+\frac{10}{4407}-\epsilon},
  ]
  from a Dec 2025 arXiv preprint of Cushman. ([arXiv][2])
  [[nomath]](Earlier best *published* exponent: $\frac43+\frac{2}{1167}-o(1)$ in Rudnev–Stevens, 2022. ([Cambridge University Press & Assessment][3]))[[/nomath]]

* One **cannot** hope to replace (2-\epsilon) by $2$ with a constant: Erdős–Szemerédi exhibited sets $A$ for which
  [
  \max{|A+A|,|AA|}\ \le\ |A|^{2}\exp!\Bigl(-c,\frac{\log|A|}{\log\log|A|}\Bigr),
  ]
  i.e. “almost” quadratic but with a stretched-exponential saving. ([Math UCR][4])

* There are strong results in **extreme regimes** (showing why the conjecture is plausible). For example, if the product set is *very* small [[nomath]](e.g. $|AA|<c|A|$)[[/nomath]], then the sumset must be essentially quadratic; this is a theorem of Chang (2003). ([Annals of Mathematics][5])

So the short answer is: **it is conjectured to be true, but it is not proved** (and the best known general exponent is currently about $1.3356$, not close to $2$). ([arXiv][2])

[1]: https://www.theoryofnumbers.com/melnathanson/pdfs/nath1997-90.pdf?utm_source=chatgpt.com "on sums and products of integers - Theory of Numbers"
[2]: https://arxiv.org/abs/2512.13849?utm_source=chatgpt.com "A note on the Sum-Product Problem and the Convex Sumset Problem"
[3]: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/an-update-on-the-sumproduct-problem/A032C94832D74E06B8753193B7791787?utm_source=chatgpt.com "An update on the sum-product problem"
[4]: https://math.ucr.edu/~mcc/paper/113%20Erdos-Szemeredi%20%20problem%20on%20sum%20set%20and%20product%20set.pdf?utm_source=chatgpt.com "erd˝os-szemerédi problem on sum set and product set"
[5]: https://annals.math.princeton.edu/2003/157-3/p07 "The Erdős–Szeméredi problem on sum set and product set | Annals of Mathematics"

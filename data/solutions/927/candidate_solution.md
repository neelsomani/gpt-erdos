This is **open in general** for a *fixed, specified* irrational (\alpha>1).

What is known is a strong **metric (almost-everywhere) result**.  In a paper of Hongze Li and Hao Pan (2008), they explicitly formulate the following conjecture:

> **Conjecture (Li–Pan).** If (\alpha>0) is irrational and (\beta\in\mathbb R), then there are infinitely many primes $p$ such that (\lfloor \alpha p+\beta\rfloor) is also prime. ([arXiv][1])

Your question is the special case (\beta=0), (\alpha>1).

They then prove that the conjecture holds for **almost all** (\alpha) (in the sense of Lebesgue measure). More precisely, for any fixed (\beta), for almost all irrational (\alpha>0),
[
\limsup_{x\to\infty}\ \pi^*_{\alpha,\beta}(x),\frac{(\log x)^2}{x}\ \ge 1,
]
where $\pi^*_{\alpha,\beta}(x)=|\\{p\le x:\ p\text{ prime and }\lfloor \alpha p+\beta\rfloor\text{ prime}\\}|$. ([arXiv][1])
In particular, this implies (\pi^*_{\alpha,\beta}(x)) is unbounded, hence there are **infinitely many** such primes $p$ for almost all (\alpha). ([arXiv][1])

So:

* **For almost every** irrational (\alpha>1): **Yes**, infinitely many such primes $p$ exist (Li–Pan). ([arXiv][1])
* **For an arbitrary fixed** irrational (\alpha>1) [[nomath]](e.g. $\alpha=\sqrt2$, $\pi$, $e$, etc.)[[/nomath]]: this remains **unproved**; it is part of the above conjecture. ([arXiv][1])

Heuristically one expects about (\sum_{p\le x}1/\log(\alpha p)\asymp x/(\log x)^2) such primes $p$, but turning that into a proof for a given (\alpha) is beyond current methods.

[1]: https://arxiv.org/pdf/0803.1740 "https://arxiv.org/pdf/0803.1740"

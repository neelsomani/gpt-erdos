Write
[
\Delta(n,k):=\prod_{i=1}^k (n+i)=\frac{(n+k)!}{n!},\qquad \operatorname{rad}(m):=\prod_{p\mid m}p
]
(the squarefree kernel). “Having the same prime factors” is exactly
[
\operatorname{rad}(\Delta(n_1,k_1))=\operatorname{rad}(\Delta(n_2,k_2)).
]

For (k_1\ge k_2\ge 3), the general finiteness question you ask is **open** (it is listed as Erdős Problem #931 and explicitly marked open). ([Erdős Problems][1])

What is known is that there **do** exist nontrivial examples, e.g. Tijdeman’s
[
19\cdot 20\cdot 21\cdot 22 \quad\text{and}\quad 54\cdot 55\cdot 56\cdot 57
]
have the same set of prime divisors, and an additional example found by “AlphaProof” is
[
10!=1\cdot 2\cdots 10 \quad\text{and}\quad 14\cdot 15\cdot 16,
]
corresponding to ((n_1,k_1,n_2,k_2)=(0,10,13,3)), which also satisfies (n_2\ge n_1+k_1). ([Erdős Problems][1])

It’s also worth noting why the hypothesis (k_2\ge 3) matters: for **two** consecutive integers ((k_2=2)) there are **infinitely many** pairs with the same prime factors [[nomath]](coming from a Pell-equation family where one product is twice the other, and “$\times 2$” doesn’t introduce a new prime because $n(n+1)$ is always even)[[/nomath]]. ([arXiv][2])

Finally, there is recent work in this direction: a 2025 preprint of Lebowitz‑Lockard studies the same “equal radical of two blocks” equation and proves upper bounds on how many such pairs can occur up to a height $x$, and formulates a conjecture that for all (k,\ell>1) with ((k,\ell)\ne(2,2)) there should be only finitely many solutions—consistent with what you’re asking in the case (k_1\ge k_2\ge 3). ([arXiv][3])

So, as of now (Jan 2026): **no proof is known** that there are only finitely many such $(n_1,n_2)$ when (k_1\ge k_2\ge 3), and no infinite family is known either. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/931 "
  
    Erdős Problem #931
  
"
[2]: https://arxiv.org/html/2408.01306v2 "The Diophantine equation ⁢(+1)⁢(+2)=⁢⁢(+1)⁢(+2) and gap principle"
[3]: https://arxiv.org/pdf/2507.09899 "On pairs of consecutive sequences with the same radicals"

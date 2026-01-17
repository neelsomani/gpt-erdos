Write
[
r_A(n):=(1_A*1_A)(n)=\bigl|{(a,b)\in A^2:\ a+b=n}\bigr|
]
(ordered representations).

A basic observation is that a uniform bound (r_A(n)\le C) forces $A$ to be very sparse: if (A(x):=|A\cap[0,x]|), then
[
A(x)^2 = \sum_{n\le 2x} r_A(n)\ \le\ (2x+1),C,
]
so (A(x)\ll \sqrt{x}) [[nomath]](hence $A$ has density $0$)[[/nomath]]. This sparsity is compatible with (\underline d(A+A)) being close to $1$, so there is no “soft” counting obstruction.

That said, the existence of such an $A$ with **uniformly bounded** (r_A(n)) and (\underline d(A+A)\ge 1-\varepsilon) appears to be **open** (at least I could not locate a reference that settles it either way).

What *is* known is that you can get very close to what you ask, but with a small exceptional set of $n$ where (r_A(n)) is large:

* If one strengthens your hypothesis to “$A$ is an (asymptotic) basis of order $2$” [[nomath]](i.e. $r_A(n)\ge 1$ for all sufficiently large $n$)[[/nomath]], then the famous **Erdős–Turán conjecture** asserts that (r_A(n)) cannot be bounded. This conjecture is still open. ([arXiv][1])

* Ruzsa constructed a basis (A\subset\mathbb N\cup{0}) for which (r_A(n)) is **bounded in square mean**, i.e. $\sum_{n\le N} r_A(n)^2=O(N)$. This implies (r_A(n)) is “typically small”, but it does *not* give a uniform bound in $n$. ([Springer][2])

* Chen gave an explicit basis (A\subset\mathbb N\cup{0}) for which (r_A(n)=2) for a set of $n$ of asymptotic density $1$ (so “almost every” integer has only two representations), but again (r_A(n)) is unbounded on a sparse exceptional set. ([Numdam][3])

There is also a useful point of comparison in **finite cyclic groups**: for each $m$ one can find (A\subset \mathbb Z_m) such that every residue has between $1$ and $R$ representations as a sum of two elements of $A$, with $R$ an absolute constant [[nomath]](Chen proved $R\le 288$, and Ding later improved this to $R\le 192$)[[/nomath]]. ([Numdam][3])
This shows that “full coverage + bounded representations” is possible in the modular setting, but lifting that to (\mathbb N) while keeping a **uniform** bound on (r_A(n)) and simultaneously making $A+A$ miss only an (\varepsilon)-fraction of integers is precisely the hard part.

So, to directly answer your question as stated: I do not know a construction, and the closest standard results in the Erdős–Turán/Ruzsa/Chen direction still allow an exceptional set of $n$ on which (r_A(n)) becomes arbitrarily large. ([Springer][2])

[1]: https://arxiv.org/pdf/0807.2073 "https://arxiv.org/pdf/0807.2073"
[2]: https://link.springer.com/content/pdf/10.1007/BF01302934.pdf "https://link.springer.com/content/pdf/10.1007/BF01302934.pdf"
[3]: https://www.numdam.org/item/CRMATH_2012__350_21-22_933_0.pdf "https://www.numdam.org/item/CRMATH_2012__350_21-22_933_0.pdf"
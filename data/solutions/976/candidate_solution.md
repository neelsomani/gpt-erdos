Write (P^+(N)) for the largest prime factor of a nonzero integer (N). Then your quantity is
[
F_f(n)=P^+!\Big(\prod_{m\le n}f(m)\Big)=\max_{m\le n}P^+(f(m)).
]

## Trivial upper bound

Since (|f(m)|\asymp m^d) and (m\le n),
[
F_f(n)\le \max_{m\le n}|f(m)|\ll_f n^d.
]
So (\gg n^d) is the “largest possible” scale, up to constants.

## Best unconditional *general* lower bounds (all irreducible (f), degree (d\ge2))

This problem (for general polynomials) is classical and is often grouped under “Chebyshev’s problem” / “Erdős–Schinzel” type questions about the largest prime factor of (\prod_{m\le n}f(m)).

### (1) A baseline bound: (F_f(n)\gg n\log n)

Already Nagell (1921) proved a general lower bound of the shape
[
F_f(n)\gg n\log n,
]
as quoted in Erdős’ 1952 paper. 

### (2) The current best general bound: (F_f(n)=n^{1+o(1)}), explicitly (n\exp((\log n)^{0.6137\ldots+o(1)}))

Erdős–Schinzel gave a lower bound for the largest prime divisor of (\prod_{m\le x}F(m)) (here (F) is a polynomial of degree (g)) in terms of a counting function (H_F(x,y,z)) that counts how often (F(n)) has a divisor in ((y,z]): ([Kevin Ford's Home Page][1])
[
\max{p:\ p\mid \textstyle\prod_{n\le x}F(n)}\ \gg\ x\exp!\Big(\frac{\log x}{g,x},H_F(x,x/2,x)\Big).
]
([Kevin Ford's Home Page][1])

Tenenbaum proved the best known general lower bound for this divisor-counting quantity:
[
H_F(x,x/2,x)\ \gg_F\ \frac{x}{(\log x)^{\log 4-1+o(1)}}\qquad (x\to\infty).
]
([Kevin Ford's Home Page][1])

Putting these together (and taking (g=d) for your irreducible (f)) gives
[
F_f(n)\ \ge\ n\exp!\Big(c_f,(\log n)^{,2-\log 4+o(1)}\Big),
]
for some constant (c_f>0) (depending on (f)), where
[
2-\log 4 \approx 0.6137056\ldots
]
In particular,
[
F_f(n)=n^{1+o(1)},
]
so it is *superlinear*, and in fact eventually bigger than (n(\log n)^A) for every fixed (A), but still far below any fixed power (n^{1+c}). ([Kevin Ford's Home Page][1])

This is, as far as I’m aware, the strongest known unconditional statement **in full generality** for irreducible polynomials of degree (\ge2).

## So is (F_f(n)\gg n^{1+c}) known in general?

Not in general. The best general bound above is (n^{1+o(1)}), and no method currently gives a fixed exponent gain (n^{1+c}) for an arbitrary irreducible (f) of degree (\ge2). (Erdős already remarks that much stronger bounds would be “very deep”.) 

There *are* additional general results in the direction “(P^+(f(n))) is usually (\ge n)” (which certainly implies (F_f(n)\ge n)), e.g. Maynard–Rudnick show that for irreducible (f) of degree (d), at least proportion (1-1/d) of integers (n\le N) satisfy (P^+(f(n))>n), and they even get (P^+(f(n))\gg n\log n) for a positive proportion (with a small constant depending on (d)). ([arXiv][2])
But these still do not yield a power (n^{1+c}) for *general* (f).

## Is (F_f(n)\gg n^d) true?

Unconditionally, this is far out of reach in general.

* Since (|f(n)|\asymp n^d), having a prime factor (\gg n^d) forces that prime factor to be comparable to (|f(m)|) for some (m\approx n), i.e. you’d need (f(m)) to be prime or “almost prime with a tiny cofactor” at some (m\le n). That’s essentially as hard as prime-values problems for polynomials.

* Under prime-producing conjectures (e.g. Bateman–Horn), one expects infinitely many prime values (f(m)), and then indeed (F_f(n)) would be (\asymp n^d). But this is conditional.

## What *is* known in the direction (n^{1+c}) for **specific** polynomials?

For particular (f), analytic methods can sometimes prove genuine power bounds.

* For (f(n)=n^2+1), Deshouillers–Iwaniec proved infinitely many (n) with (P^+(n^2+1)\ge n^{6/5}) (so (F_{x^2+1}(n)\gg n^{6/5}) along a subsequence). ([EuDML][3])
  Merikoski later improved the exponent to (1.279) infinitely often. ([arXiv][4])

* For (f(n)=n^3+2), Irving proved that for (X) large, a positive proportion of (n\in(X,2X]) have a prime factor (>X^{1+10^{-52}}). ([arXiv][5])
  This implies a bound of the form (F_{x^3+2}(n)\gg n^{1+10^{-52}}) (with a constant loss from replacing (X) by (n/2)) for all sufficiently large (n).

These illustrate that (n^{1+c}) **can** hold for some polynomials, but proving it uniformly for an arbitrary irreducible (f) is open.

## Bottom line

For general irreducible (f\in\mathbb Z[x]), (\deg f=d\ge2), the best unconditional “in complete generality” bounds currently look like
[
n\exp\Big(c_f(\log n)^{2-\log 4+o(1)}\Big)\ \ll\ F_f(n)\ \ll_f\ n^d,
]
so (F_f(n)=n^{1+o(1)}), but **no fixed power** (n^{1+c}) is known in general, and (\gg n^d) is far beyond present methods (it would essentially require prime-like values of (f) near (n)). ([Kevin Ford's Home Page][1])

[1]: https://www.ford126.web.illinois.edu/wwwpapers/HFxyz.pdf "https://www.ford126.web.illinois.edu/wwwpapers/HFxyz.pdf"
[2]: https://arxiv.org/pdf/1910.13218 "https://arxiv.org/pdf/1910.13218"
[3]: https://eudml.org/doc/74560?utm_source=chatgpt.com "On the greatest prime factor of $n^2+1"
[4]: https://arxiv.org/abs/1908.08816?utm_source=chatgpt.com "On the largest prime factor of $n^2+1$"
[5]: https://arxiv.org/abs/1412.0024?utm_source=chatgpt.com "The largest prime factor of $X^3+2$"

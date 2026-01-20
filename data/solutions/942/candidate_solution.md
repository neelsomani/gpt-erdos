Write (F_2) for the squarefull (powerful) integers and (Q(x):=|\\{m\le x:m\in F_2\\}|).  A standard fact is that every squarefull integer has a unique representation
[
m=a^2b^3\qquad(b\ \text{squarefree}),
]
and Erdős–Szekeres proved (with an explicit constant)
[
Q(x)=c_2 x^{1/2}+O(x^{1/3}),\qquad c_2=\frac{\zeta(3/2)}{\zeta(3)}=2.173\ldots,. \tag{*}
]
([arXiv][1])

## 1) Mean size of $h(n)$

Your quantity
[
h(n)=|\big(F_2\cap[n^2,(n+1)^2)\big)|
]
satisfies the telescoping identity
[
\sum_{n\le N} h(n)=|\\{m<(N+1)^2:\ m\in F_2\\}|=Q((N+1)^2-1).
]
Using ((*)) gives
[
\frac1N\sum_{n\le N} h(n)=c_2+o(1).
]
So **on average** [[nomath]](with respect to $n$)[[/nomath]] one has
[
h(n)\ \text{is typically a constant of size }\approx 2.173.
]
([arXiv][1])

This is the right “first estimate”: the interval length is ((n+1)^2-n^2\sim 2n), while the global density of squarefulls near (x=n^2) is (\asymp x^{-1/2}), so a constant count is natural.

## 2) A much sharper statement: limiting distribution

Let (S_2\subset F_2) be the squarefull integers that are **not** squares. Since there are no squares strictly between (n^2) and ((n+1)^2), we have
[
h(n)=1+|\big(S_2\cap (n^2,(n+1)^2)\big)|.
]

Shiu proved a strong “statistical” theorem: for each fixed (\ell\ge 0), the set of $n$ for which ((n^2,(n+1)^2)) contains exactly (\ell) elements of (S_2) has a natural density (d_\ell>0). In particular,
[
|\\{n\le x:|((n^2,(n+1)^2)\cap S_2)|=\ell\\}|=d_\ell x+o(x),
]
and the first few values are (d_0\approx 0.275), (d_1\approx 0.395), (d_2\approx 0.231), … ([arXiv][1])

So, in terms of your $h(n)$:

* (h(n)=1) [[nomath]](only $n^2$)[[/nomath]] happens with density (\approx 0.275).
* (h(n)=2) happens with density (\approx 0.395).
* (h(n)=3) happens with density (\approx 0.231).
* etc. ([arXiv][1])

Moreover, Xiong–Zaharescu [[nomath]](and Shiu for $k=2$)[[/nomath]] give a product formula for the generating function of these densities:
[
\sum_{\ell\ge 0} d_{2,\ell} z^\ell=\prod_{\lambda\in\Lambda_2}\left(1+\frac{z-1}{\lambda}\right),
]
where (\Lambda_2) corresponds to (\lambda=b^{3/2}) with $b$ squarefree (\ge 2). ([arXiv][1])

One consequence is that **every fixed value** of $h(n)$ occurs for infinitely many $n$ (indeed with positive density for each fixed value), so $h(n)$ is unbounded, but “usually small.” ([arXiv][1])

## 3) How large can $h(n)$ get?

### Lower bounds (infinitely often)

De Koninck–Luca–Shparlinski proved that for any fixed (K\ge 2) there are infinitely many $N$ such that
[
(N^K,(N+1)^K)\ \text{contains at least}\ (\log N)^{1/3+o(1)}\ K\text{-full integers}.
]
([Jean-Marie De Koninck][2])

Taking $K=2$ gives infinitely many $n$ for which ((n^2,(n+1)^2)) contains ((\log n)^{1/3+o(1)}) squarefull non-squares, hence
[
h(n)\ \ge\ (\log n)^{1/3+o(1)}\qquad\text{for infinitely many }n.
]
So **any** exponent $c$ in your “(>(\log n)^{c-o(1)}) infinitely often” question must satisfy (c\ge 1/3) unconditionally. ([Jean-Marie De Koninck][2])

### Upper bounds [[nomath]](uniform in $n$)[[/nomath]]

The best “general-purpose” unconditional uniform bound I see in the same paper is the sieve-type estimate: any interval $(L,L+K)$ contains at most
[
O!\left(\frac{K\log\log K}{\log K}\right)
]
squarefull integers. ([Jean-Marie De Koninck][2])

Apply this with (L=n^2) and (K=(n+1)^2-n^2=2n+1) to get
[
h(n)\ \ll\ \frac{n\log\log n}{\log n}.
]
This is far larger than any polylogarithm; it’s a *very* soft upper bound, but it is what is currently available in that generality from this route. ([Jean-Marie De Koninck][2])

## 4) Your “polylog $c$” question

* The **lower bound side** is known with (c=1/3): infinitely many $n$ have (h(n)\ge (\log n)^{1/3+o(1)}). ([Jean-Marie De Koninck][2])
* A matching **upper bound of the form** (h(n) < (\log n)^{c+o(1)}) **for all $n$** is not supplied by these results; the best unconditional uniform bound quoted above is much bigger. ([Jean-Marie De Koninck][2])

Heuristically, the product formula for the densities (a “Poisson-binomial”-type generating function) suggests that the tail (\mathbb P(h(n)\ge k)) should drop roughly like (\exp(-k\log k)), which in turn would predict that the maximal order up to (n\le N) is about
[
\max_{n\le N} h(n)\ \approx\ \frac{\log N}{\log\log N}=(\log N)^{1-o(1)}.
]
In your language, that would correspond to a conjectural $c=1$ for the *maximal order* [[nomath]](up to the usual $o(1)$ in the exponent)[[/nomath]]. This is consistent with $h(n)$ being typically $O(1)$ but occasionally spiking.

So, as things stand from the literature above: **rigorously (c\ge 1/3) is attainable infinitely often; a matching polylog upper bound [[nomath]](and hence a definitive value of $c$)[[/nomath]] is not settled by these sources.**

If you want, I can also restate everything in terms of Shiu’s densities (d_\ell) and explain how the product (\prod_{b\ \text{sqfree}\ge 2}(1+(z-1)/b^{3/2})) arises from the representation (m=a^2b^3), which gives the “constant mean” and the limiting distribution quite cleanly.

[1]: https://arxiv.org/pdf/2512.07438 "On the number of $k$-full integers between three successive $k$th powers"
[2]: https://www.jeanmariedekoninck.mat.ulaval.ca/fileadmin/Documents/Publications/2005_powerful_numbers_in_short_intervals.pdf "Powerful numbers in short intervals"

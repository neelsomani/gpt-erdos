Write
[
r_k(n)=|\\{(a,b,c)\in\Bbb Z_{\ge 0}^3:\ a^k+b^k+c^k=n\\}|,
\qquad
f_{k,3}(x)=|\\{n\le x:\ r_k(n)\ge 1\\}|.
]
Then
[
\sum_{n\le x} r_k(n)=|\\{(a,b,c)\in\Bbb Z_{\ge 0}^3:\ a^k+b^k+c^k\le x\\}|
\sim c_k,x^{3/k},
]
where the constant is the volume of the region (u_1^k+u_2^k+u_3^k\le 1), namely
[
c_k=\frac{\Gamma(1+1/k)^3}{\Gamma(1+3/k)}.
]
This (and the corresponding first-moment asymptotic) is the “trivial” lattice-point estimate used in the literature. ([Oxford University Research Archive][1])

A standard Cauchy–Schwarz argument relates (f_{k,3}) to the second moment:
[
\Big(\sum_{n\le x} r_k(n)\Big)^2 \le f_{k,3}(x),\sum_{n\le x} r_k(n)^2,
]
so that
[
f_{k,3}(x)\ \ge\ \frac{\big(\sum_{n\le x} r_k(n)\big)^2}{\sum_{n\le x} r_k(n)^2}.
]
Here (\sum_{n\le x} r_k(n)^2) counts solutions of
[
a_1^k+a_2^k+a_3^k=a_4^k+a_5^k+a_6^k\le x,
]
so the problem is essentially a “paucity” question for **equal sums of three $k$th powers**.

## What is known

### For (k\ge 11): yes, and in fact the optimal order (even an asymptotic)

Salberger (as reported in the Oberwolfach Report 50/2019) gives a bound implying that, for (d\ge 11), the number (n_d(B)) of positive-integer solutions (x_j\le B) to
[
x_0^d+x_1^d+x_2^d=x_3^d+x_4^d+x_5^d
]
satisfies
[
n_d(B)=6B^3+O_d(B^{3-\delta})
\quad\text{for some }\delta>0.
]
In other words: apart from the “trivial” solutions coming from permuting $(x_0,x_1,x_2)$, there are $o(B^3)$ solutions. ([EMS Press][2])

Combining this paucity statement with the first-moment asymptotic (\sum_{n\le x} r_k(n)\sim c_k x^{3/k}) (above) gives
[
\sum_{n\le x} r_k(n)^2 \sim 6c_k x^{3/k},
]
and hence (by Cauchy–Schwarz and the matching easy upper bound) one gets the **asymptotic**
[
f_{k,3}(x)\sim \frac{c_k}{6},x^{3/k}
=\frac{1}{6}\frac{\Gamma(1+1/k)^3}{\Gamma(1+3/k)},x^{3/k},
\qquad (k\ge 11).
]
In particular, for every (k\ge 11),
[
f_{k,3}(x)\gg x^{3/k}
\quad\text{and hence also}\quad
f_{k,3}(x)\gg_\varepsilon x^{3/k-\varepsilon}.
]
[[nomath]](Allowing $0$ as a summand instead of insisting on positivity does not change the main term, since contributions with a zero are of smaller order $x^{2/k}$.)[[/nomath]]

*Historical note:* Browning–Heath-Brown proved an earlier version with a larger threshold ((d\ge 33)) and deduced exactly this kind of asymptotic consequence. ([Oxford University Research Archive][1])

### For (3\le k\le 10): the full strength is not known in general

For the small exponents, controlling (\sum_{n\le x} r_k(n)^2) sharply enough [[nomath]](i.e., showing it is $\ll x^{3/k+o(1)}$, or better $\sim 6c_kx^{3/k}$)[[/nomath]] is much harder, and the optimal lower bound (f_{k,3}(x)\gg_\varepsilon x^{3/k-\varepsilon}) is not currently established uniformly for all (3\le k\le 10) by the methods above.

The sharpest “flagship” case is $k=3$ (three cubes). Here the conjectural strength would be (f_{3,3}(x)\gg_\varepsilon x^{1-\varepsilon}) [[nomath]](and the even stronger $f_{3,3}(x)\gg x$ would mean positive density)[[/nomath]]. This remains out of reach; the best published lower bounds are of the shape
[
f_{3,3}(x)\gg x^\beta\quad\text{with }\beta<1.
]
In particular, Wooley proved a lower bound with exponent (\beta=0.91709477) for sums of three cubes of natural numbers. ([ResearchGate][3])

## Bottom line

* **Yes for all (k\ge 11)**: in fact one has the asymptotic
  [
  f_{k,3}(x)\sim \frac{1}{6}\frac{\Gamma(1+1/k)^3}{\Gamma(1+3/k)},x^{3/k},
  ]
  so certainly (f_{k,3}(x)\gg x^{3/k}) and (f_{k,3}(x)\gg_\varepsilon x^{3/k-\varepsilon}). ([EMS Press][2])
* For **(3\le k\le 10)**, the optimal order (x^{3/k}) [[nomath]](or $x^{3/k-\varepsilon}$ for every $\varepsilon$)[[/nomath]] is **not known in general**; in the key case $k=3$ the best available exponents are still (<1). ([ResearchGate][3])

[1]: https://ora.ox.ac.uk/objects/uuid%3A1fd05b3e-cd34-4b65-a95e-590af2e523dc/files/m4c717ccd310e4b8622a4423c5dcf3075 "https://ora.ox.ac.uk/objects/uuid%3A1fd05b3e-cd34-4b65-a95e-590af2e523dc/files/m4c717ccd310e4b8622a4423c5dcf3075"
[2]: https://ems.press/content/serial-article-files/46829 "https://ems.press/content/serial-article-files/46829"
[3]: https://www.researchgate.net/publication/231889184_Sums_of_three_cubes_II "https://www.researchgate.net/publication/231889184_Sums_of_three_cubes_II"

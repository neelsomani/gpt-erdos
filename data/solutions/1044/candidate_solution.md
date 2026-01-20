Let
[
f(z)=\prod_{i=1}^n (z-z_i),\qquad |z_i|\le 1,
]
and let (\Lambda(f)) be the maximum [[nomath]](over connected components $U$ of ${|f|<1}$)[[/nomath]] of the boundary length (\mathrm{length}(\partial U)).
The infimum is taken over **all such polynomials of all degrees (n\ge1)** (this is the “original” interpretation of the problem). ([Erdős Problems][1])

## 1) A universal lower bound: (\Lambda(f)>2) for every fixed polynomial

First, a geometric fact:

**Lemma (length vs diameter).** If (\Gamma) is a rectifiable closed curve, then
[
\mathrm{length}(\Gamma)\ \ge\ 2\mathrm{diam}(\Gamma).
]
Indeed, pick (a,b\in\Gamma) with (|a-b|=\mathrm{diam}(\Gamma)). Traversing (\Gamma) from $a$ to $b$ in the two directions splits (\Gamma) into two arcs, each of length (\ge |a-b|); adding gives the inequality.

Now we use a theorem of Pommerenke (1961): for any monic polynomial whose zeros lie in (\overline{\mathbb D}), if $U$ is the component of ({|f|<1}) containing $0$, then
[
\mathrm{diam}(U) > 1.
]


The diameter of $U$ is attained on (\partial U) [[nomath]](if a farthest point were interior, one could move it slightly farther while staying in $U$)[[/nomath]], so (\mathrm{diam}(\partial U)\ge \mathrm{diam}(U)>1). Hence by the lemma,
[
\mathrm{length}(\partial U)\ \ge\ 2\mathrm{diam}(\partial U)\ >\ 2.
]
Therefore (\Lambda(f)\ge \mathrm{length}(\partial U)>2) for every admissible polynomial $f$ of finite degree. ([Erdős Problems][1])

So:
[
\inf_f \Lambda(f)\ \ge\ 2.
]

## 2) An upper bound approaching $2$: the family (f_n(z)=z^n-1)

Take
[
f_n(z)=z^n-1,
]
whose zeros are the $n$-th roots of unity [[nomath]](all lie on $|z|=1$, so they satisfy $|z_i|\le1$)[[/nomath]].

The set ({|z^n-1|<1}) has $n$ congruent “petals,” and (\Lambda(f_n)) is the common boundary length of one petal. One can write the boundary of the petal near the positive real axis in polar coordinates (z=re^{i\theta}) as
[
|r^n e^{in\theta}-1|=1 \quad\Longleftrightarrow\quad r^n = 2\cos(n\theta),\qquad |\theta|\le \frac{\pi}{2n}.
]
A direct arc-length computation gives an explicit formula
[
\Lambda(f_n)
= \frac{2^{1/n}}{n}B\left(\frac1{2n},\frac12\right)
= \frac{2^{1/n}\sqrt{\pi}}{n}\frac{\Gamma!\left(\frac1{2n}\right)}{\Gamma!\left(\frac12+\frac1{2n}\right)}.
]
From (\Gamma(\varepsilon)\sim 1/\varepsilon) as (\varepsilon\to0^+), it follows that (\Lambda(f_n)\to 2) as (n\to\infty). In particular, for every (\varepsilon>0), for $n$ large enough,
[
\Lambda(f_n) < 2+\varepsilon,
]
so
[
\inf_f \Lambda(f)\ \le\ 2.
]
[[nomath]](Equivalently: testing $f_n$ yields $\inf_f\Lambda(f)\le \inf_n \Lambda(f_n)=2$.)[[/nomath]] ([Erdős Problems][1])

## 3) Conclusion

Combining the lower and upper bounds,
[
\boxed{\inf_f \Lambda(f)=2.}
]
Moreover, the lower bound is **strict** for every fixed polynomial [[nomath]](Pommerenke gives $\mathrm{diam}(U)>1$, hence $\Lambda(f)>2$)[[/nomath]], so the infimum $2$ is **not attained** by any finite-degree polynomial. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/1044 "

    Erdős Problem #1044 - Discussion thread

"

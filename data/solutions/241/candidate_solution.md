This is the classic **(B_3)** (a.k.a. “Sidon of order 3”) extremal problem.

Let $f(N)$ be the largest (|A|) with (A\subseteq{1,\dots,N}) such that
[
a_1+a_2+a_3=b_1+b_2+b_3
]
forces $\\{a_1,a_2,a_3\\}=\\{b_1,b_2,b_3\\}$ as multisets (i.e. only permutations / identical triples are allowed). Equivalently: all 3-term sums are distinct “up to the trivial coincidences”.

### What is known

**1) The exponent $1/3$ is correct.**
A simple counting argument already gives (f(N)=O(N^{1/3})): there are (\binom{|A|+2}{3}\sim |A|^3/6) unordered triples with repetition, and their sums lie in $\\{3,4,\dots,3N\\}$ which has only $3N-2$ values, so (|A|^3 \ll N).

**2) There are constructions of size (\boldsymbol{(1+o(1))N^{1/3}}).**
Bose–Chowla-type finite-field constructions give (B_h) sets [[nomath]](in particular $h=3$)[[/nomath]] with size (N^{1/h}(1+o(1))), so here
[
f(N)\ \ge\ (1+o(1)),N^{1/3}.
]
([Cambridge University Press & Assessment][1])

So (f(N)=\Theta(N^{1/3})).

### What is *not* known [[nomath]](and answers your “$\sim$”)[[/nomath]]

The stronger statement
[
f(N)\sim N^{1/3}\qquad\text{(i.e. }f(N)/N^{1/3}\to 1\text{)}
]
is **open**. More generally, even the existence/value of the limiting constant for (B_h[g]) problems is not known except in the classical Sidon case (h=2,g=1). ([Cambridge University Press & Assessment][1])

### Best asymptotic upper bounds (constant-factor)

Ben Green (2001) proved the asymptotic upper bound
[
f(N)\ \le\ \left(\frac{7}{2}\right)^{1/3}N^{1/3}(1+o(1))
\approx 1.5183,N^{1/3}.
]
([People Mathematics Oxford][2])

More recently, E. P. White (2024) improved the relevant underlying autoconvolution constant slightly, yielding a marginally better leading constant for (\sigma_3(1)) (hence for $f(N)$ in this setting); numerically this gives about
[
f(N)\ \le\ (1.5155+o(1)),N^{1/3}.
]
([Cambridge University Press & Assessment][1])

### Current state in one line

[
(1+o(1)),N^{1/3}\ \le\ f(N)\ \le\ (1.5155+o(1)),N^{1/3},
]
and whether the constant on the right can be pushed all the way down to $1$ [[nomath]](equivalently $f(N)\sim N^{1/3}$)[[/nomath]] is **not known**. ([Cambridge University Press & Assessment][1])

[1]: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/an-optimal-l2-autoconvolution-inequality/8D109D51F271CC78EBDA2C99FB35612D "https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/an-optimal-l2-autoconvolution-inequality/8D109D51F271CC78EBDA2C99FB35612D"
[2]: https://people.maths.ox.ac.uk/greenbj/papers/number-of-squares-and-Bh%5Bg%5D.pdf "https://people.maths.ox.ac.uk/greenbj/papers/number-of-squares-and-Bh%5Bg%5D.pdf"

Write (A={a_1<\cdots<a_n}\subseteq{1,\dots,N}) and
[
H:=\langle A\rangle=\\{\sum_{i=1}^n \epsilon_i a_i:\epsilon_i\in{0,1}\\}
]
[[nomath]](the “binary” Hilbert cube of dimension $n$ anchored at $0$)[[/nomath]].

A basic monotonicity is worth recording first:

* Every $k$-term AP with (k\ge 3) contains a 3-term AP as a subprogression (three consecutive terms).
  Hence if $H$ is 3-AP-free, then it is $k$-AP-free for every (k\ge 3). In particular,
  [
  g_k(n)\le g_3(n)\quad(k\ge 3).
  ]

So the hard case is $k=3$.

## The $k=3$ case: equivalence with 2-fold sum-distinctness

Call a set (A={a_1,\dots,a_n}\subset\mathbb Z) **2-SSD** (2-fold subset-sum-distinct) if all sums
[
\sum_{i=1}^n \eta_i a_i,\qquad \eta_i\in{0,1,2},
]
are distinct; equivalently, there is no nontrivial relation (\sum_i c_i a_i=0) with (c_i\in{-2,-1,0,1,2}). This is the standard “$k$-SSD” notion in the literature with $k=2$. ([IJPureMath][1])

For positive integers, your condition “(\langle A\rangle) contains no nontrivial 3-term AP” is essentially the same as “$A$ is 2-SSD”:

* If two *distinct* subsets of $A$ have the same sum $s$, then (after cancelling the overlap) you get disjoint nonempty subsets (B,C) with (\sum_{b\in B}b=\sum_{c\in C}c=:t>0). Then
  [
  0,\ t,\ 2t=\sum_{x\in B\cup C}x
  ]
  are all in (\langle A\rangle), giving a nontrivial 3-AP. So 3-AP-free forces **all subset sums to be distinct** [[nomath]](in particular $|\langle A\rangle|=2^n$)[[/nomath]].

* More generally, a nontrivial 3-AP (x,y,z\in\langle A\rangle) means
  [
  x+z=2y.
  ]
  Writing (x=\sum \epsilon_i a_i), (y=\sum \delta_i a_i), (z=\sum \epsilon'_i a_i) with (\epsilon_i,\delta_i,\epsilon'*i\in{0,1}), this becomes
  [
  \sum*{i=1}^n(\epsilon_i+\epsilon'_i-2\delta_i)a_i = 0
  ]
  with coefficients in ({-2,-1,0,1,2}). Conversely, any nonzero coefficient vector (c_i\in{-2,-1,0,1,2}) can be realized as (c_i=\epsilon_i+\epsilon'_i-2\delta_i) by choosing ((\epsilon_i,\epsilon_i',\delta_i)\in{0,1}^3) coordinatewise, producing a nontrivial 3-AP in (\langle A\rangle).

So [[nomath]](for positive $a_i$)[[/nomath]] you can treat:
[
\langle A\rangle\ \text{3-AP-free}\quad\Longleftrightarrow\quad A\ \text{is 2-SSD (i.e. 2-dissociated)}.
]

That reformulation makes the growth scale “base $3$” very natural, because 2-SSD is about ({0,1,2})-coefficients, i.e. (3^n) possible coefficient vectors.

## Upper bound for (g_3(n)): the base-3 construction

Take
[
A={1,3,3^2,\dots,3^{n-1}}\subseteq{1,\dots,3^{n-1}}.
]
Then (\langle A\rangle) is exactly the set of integers whose base-3 expansion uses only digits $0$ and $1$. If (x+z=2y) with (x,y,z\in\langle A\rangle), then [[nomath]](since all digits are $\le1$)[[/nomath]] there are **no carries** in forming $x+z$ or (2y) in base $3$, so the equality holds digit-by-digit. But in each digit position, (\epsilon+\epsilon'\in{0,1,2}) while (2\delta\in{0,2}), so equality forces (\epsilon=\epsilon'=\delta) in every coordinate, i.e. (x=y=z). Hence (\langle A\rangle) has no nontrivial 3-AP.

Therefore
[
g_3(n)\le 3^{n-1}.
]

## Lower bounds for (g_3(n)): (\mathbf{\gtrsim 3^n/\sqrt n})

Let (A\subseteq{1,\dots,N}), (|A|=n), and assume (\langle A\rangle) is 3-AP-free. As explained above, $A$ is 2-SSD.

### Counting bound: (g_3(n)\gtrsim 3^n/n)

For a 2-SSD set (A={a_1,\dots,a_n}), the (3^n) sums (\sum \eta_i a_i) with (\eta_i\in{0,1,2}) are all distinct and lie between $0$ and (2(a_1+\cdots+a_n)). A standard lemma [[nomath]](stated for general $k$-SSD)[[/nomath]] gives
[
2(a_1+\cdots+a_n)\ \ge\ 3^n-1,
]
i.e.
[
a_1+\cdots+a_n\ \ge\ \frac{3^n-1}{2}. \tag{*}
]
([IJPureMath][1])
Since (a_1+\cdots+a_n\le nN), this yields
[
g_3(n)\ \ge\ \frac{3^n-1}{2n}\ \asymp\ \frac{3^n}{n}.
]

### Erdős–Moser–type concentration bound: (g_3(n)\gtrsim 3^n/\sqrt n)

You can strengthen (\asymp 3^n/n) to (\asymp 3^n/\sqrt n) by a variance argument (the same “central mass” idea behind the classical distinct subset sums problem, but with ternary coefficients).

Because $A$ is 2-SSD, all signed sums
[
S(\varepsilon)=\sum_{i=1}^n \varepsilon_i a_i,\qquad \varepsilon_i\in{-1,0,1},
]
are **distinct** [[nomath]](if $S(\varepsilon)=S(\varepsilon')$ then $\sum (\varepsilon_i-\varepsilon_i')a_i=0$ with coefficients in ${-2,-1,0,1,2}$)[[/nomath]].

Now choose (\varepsilon) uniformly from ({-1,0,1}^n). Then:

* (\mathbb E[\varepsilon_i]=0) and (\mathrm{Var}(\varepsilon_i)=\mathbb E[\varepsilon_i^2]=2/3).
* So (\mathbb E[S]=0) and
  [
  \mathrm{Var}(S)=\frac{2}{3}\sum_{i=1}^n a_i^2\ \le\ \frac{2}{3},nN^2.
  ]
  Let (\sigma=\sqrt{\mathrm{Var}(S)}\le N\sqrt{2n/3}). Chebyshev gives
  [
  \mathbb P\big(|S|\le 2\sigma\big)\ge 1-\frac{1}{4}=\frac{3}{4}.
  ]
  That means at least (\frac34,3^n) of the distinct integers $S(\varepsilon)$ lie in the interval $[-2\sigma,2\sigma]$, whose length is (4\sigma\le 4N\sqrt{2n/3}). Hence
  [
  4N\sqrt{\frac{2n}{3}}+1\ \ge\ \frac34,3^n,
  ]
  so
  [
  g_3(n)\ \ge\ c,\frac{3^n}{\sqrt n}
  ]
  for an absolute constant (c>0) [[nomath]](e.g. $c\approx 0.23$ works from the inequality above)[[/nomath]].

## Summary for (g_3(n))

Unconditionally,
[
c,\frac{3^n}{\sqrt n}\ \lesssim\ g_3(n)\ \le\ 3^{n-1}.
]

So (g_3(n)) is “base-$3$ exponential” in $n$, pinned down up to a polynomial factor.

### About the specific question (g_3(n)\gg 3^n)

To have (g_3(n)\gg 3^n) you would need a **constant-factor** lower bound (g_3(n)\ge c,3^n). The best general lower bound coming from the 2-SSD viewpoint and concentration is only (g_3(n)\gtrsim 3^n/\sqrt n), and the simple construction gives (g_3(n)\le 3^{n-1}=(1/3)3^n). With these, one cannot currently deduce either (g_3(n)\gg 3^n) or (g_3(n)=o(3^n)) without additional input.

What you *can* say cleanly is: the problem is essentially the “dense 2-SSD sequence” problem [[nomath]](distinct ${0,1,2}$-coefficient sums)[[/nomath]], and in the $k$-SSD literature one already sees explicit nontrivial 2-SSD examples beyond pure powers of 3 (Bae even notes such constructions in connection with the Conway–Guy method). ([IJPureMath][1])

## General (k\ge 3)

* The same base-3 construction shows
  [
  g_k(n)\le g_3(n)\le 3^{n-1}\qquad\text{for every fixed }k\ge 3.
  ]

* A general (but much weaker) lower bound comes from a standard “Hilbert cube in a $k$-AP-free set” growth lemma: if a Hilbert cube of dimension $n$ sits inside a set with no $k$-term AP, its size must grow at least like (\big(\frac{k}{k-1}\big)^n). In particular, for a $k$-AP-free cube (H\subseteq[0,nN]),
  [
  nN+1 \ \ge\ |H|\ \ge\ 2\Big(\frac{k}{k-1}\Big)^{n-1}-1,
  ]
  so
  [
  g_k(n)\ \gtrsim\ \frac1n\Big(\frac{k}{k-1}\Big)^{n}.
  ]

  [[nomath]](For $k=3$ this is far weaker than the $3^n/\sqrt n$ bound above.)[[/nomath]]

If you want, I can also sketch how the variance argument adapts in a clean abstract way to “$m$-SSD” constraints [[nomath]](distinct sums with coefficients in ${-m,\dots,m}$)[[/nomath]], which is the natural general framework behind the $k=3$ analysis.

[1]: https://www.ijpam.eu/contents/2002-1-3/8/8.pdf "https://www.ijpam.eu/contents/2002-1-3/8/8.pdf"

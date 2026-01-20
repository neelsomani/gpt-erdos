No—neither bound can hold **uniformly over all increasing integer sequences** ((x_n)).

### A lower-bound counterexample (Berkes–Philipp)

There exists a strictly increasing sequence of integers ((n_k)) such that for **almost every** (x\in(0,1)) one has
[
N,D_N(x)\ \ge\ c, (N\log N)^{1/2}\qquad\text{for infinitely many }N,
]
for some absolute constant (c>0). ([TU Graz Math][1])

Here (D_N(x)) is the *normalized* discrepancy
$
D_N(x_1,\dots,x_N)=\sup_{0\le a<b\le 1}\left|\frac{A(N,a,b)}{N}-(b-a)\right|,
$
so (N D_N) is exactly your **unnormalized** discrepancy
$
D(N)=\sup_{I\subset[0,1]}\bigl||\\{k\le N:{\alpha x_k}\in I\\}|-|I|N\bigr|
$
[[nomath]](with $I$ ranging over intervals)[[/nomath]]. ([TU Graz Math][1])

Translating the Berkes–Philipp statement to your notation: there is an increasing integer sequence ((x_n)) such that for a.e. (\alpha),
[
D(N)\ \ge\ c\sqrt{N\log N}\qquad\text{i.o.}
]

### Why this kills both proposed upper bounds

* (\sqrt{N\log N} = \sqrt{N},(\log N)^{1/2}), and ((\log N)^{1/2}) is **not** ((\log N)^{o(1)}).
* Also ((\log N)^{1/2}) eventually dominates every ((\log\log N)^C), so (\sqrt{N\log N}) is **not** (\ll \sqrt N(\log\log N)^{O(1)}).

Hence **both** of your suggested bounds fail in general.

### What *is* known in general (upper bounds)

The best “for every ((x_n)), for a.e. (\alpha)” general upper bound goes back to Baker (1981): for every (\varepsilon>0),
[
D(N)\ \ll_{\alpha,\varepsilon}\ \sqrt N,(\log N)^{3/2+\varepsilon}
\quad\text{for a.e. }\alpha,
]
for every increasing integer sequence ((x_n)). ([Institute of Statistics][2])

Moreover, the Berkes–Philipp example shows that the **logarithmic exponent cannot in general be pushed below $1/2$**, and it is commonly conjectured that (1/2+\varepsilon) should be the truth. 

So, in the “arbitrary integer sequence” setting, the situation is:
[
\text{known: }\ (\log N)^{3/2+\varepsilon}\quad\text{vs.}\quad
\text{necessary: at least }(\log N)^{1/2}\text{ for some sequences},
]
and bridging the gap is a major open problem—but the much stronger ((\log N)^{o(1)}) or ((\log\log N)^{O(1)}) cannot be correct because of the (\sqrt{N\log N}) lower-bound example.

[1]: https://www.math.tugraz.at/~aistleitner/Publications/LIL_discr.pdf "https://www.math.tugraz.at/~aistleitner/Publications/LIL_discr.pdf"
[2]: https://www.stat.tugraz.at/philipp_volume/baker.pdf "https://www.stat.tugraz.at/philipp_volume/baker.pdf"

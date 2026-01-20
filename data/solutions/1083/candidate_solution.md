Write
[
f_d(n)=\min_{\substack{P\subset\mathbb R^d\ |P|=n}} \bigl|{|p-q|:p,q\in P}\bigr|
]
[[nomath]](the literature often denotes this by $D_d(n)$)[[/nomath]]. For fixed (d\ge 3) the right “guess” is indeed
[
f_d(n)\stackrel{?}{=}\Theta\bigl(n^{2/d}\bigr),
]
but this is still open.

## What is known (Euclidean distances)

### Upper bound (construction)

A $d$-dimensional integer grid of side length $k$ has (n=k^d) points, and every squared distance is a sum of $d$ squares, each (\le (k-1)^2), hence is an integer in ([0,d(k-1)^2]). Therefore the grid determines at most (O(k^2)=O(n^{2/d})) distinct distances. This gives
[
f_d(n)\ll_d n^{2/d}.
]
This is the standard Erdős lattice construction and is recorded in modern surveys. 

### Lower bounds (hard part)

Erdős already showed the general lower bound (f_d(n)\gg_d n^{1/d}), but much stronger bounds are known now. ([Erdős Problems][1])

The best general-purpose lower bounds for *unrestricted* point sets in (\mathbb R^d) come from work of Solymosi–Vu (2008), via recursive “dimension-raising” inequalities. In their paper they prove in particular [[nomath]](for $d\ge3$)[[/nomath]]
[
f_d(n)=\Omega\left(n^{\frac{2}{d}-\frac{2}{d(d+2)}}\right)
]
[[nomath]](and for $d=3$ they state an exponent $0.5643$ using then-best planar inputs)[[/nomath]]. 

If one feeds in the *current* planar distinct-distance lower bound of Guth–Katz ((D_2(n)=\Omega(n/\log n))), the same Solymosi–Vu recursion improves the 3D consequence to
[
f_3(n)=\Omega^*\left(n^{3/5}\right),
]
where (\Omega^*(\cdot)) hides polylogarithmic factors. This “$3/5$” bound (up to polylogs) is commonly listed as the best known for $d=3$. 

More generally, the same framework yields (again up to polylogs) explicit exponents that are
[
\frac{2}{d}-\Theta\left(\frac1{d^2}\right)
]
for fixed $d$, and approach $2/d$ only as (d\to\infty). One convenient way to state what’s currently recorded in survey form is: 

* (f_3(n)=\Omega^*(n^{3/5})) and (f_3(n)=O(n^{2/3})). 
* For even (d\ge4),
  [
  f_d(n)=\Omega^*\left(n^{\frac{2(d+1)}{d^2+2d-2}}\right),
  ]
  and for odd (d\ge5),
  [
  f_d(n)=\Omega^*\left(n^{\frac{2(d+1)}{d^2+2d-5/3}}\right),
  ]
  while always (f_d(n)=O(n^{2/d})). 

So, for example:

* (d=3:\quad n^{0.6}) (up to polylogs) (\le f_3(n)\le n^{0.666\ldots}).
* (d=4:\quad n^{5/11}\approx n^{0.4545}) (up to polylogs) (\le f_4(n)\le n^{1/2}).

## Is (f_d(n)=n^{2/d-o(1)}) true?

This is **conjectured** [[nomath]](indeed Erdős’ conjecture is essentially $f_d(n)=\Theta(n^{2/d})$ for every fixed $d\ge3$)[[/nomath]], but it is **still open**. 

What we *can* currently prove is weaker: for each fixed (d\ge3),
[
f_d(n)\ge n^{\frac{2}{d}-c_d}
]
with (c_d) a positive constant depending on $d$ [[nomath]](typically $c_d\asymp 1/d^2$)[[/nomath]], not something that tends to $0$ with $n$. 
That polynomial “exponent gap” is exactly why the (n^{2/d-o(1)}) statement remains out of reach for fixed $d$.

## Optional context: why it’s hard

One can reduce the $d$-dimensional distinct distances problem to a higher-dimensional incidence problem [[nomath]](e.g., incidences between $(d-1)$-flats in $\mathbb R^{2d-1}$)[[/nomath]], and a conjecturally sharp incidence bound there would imply the conjectured (n^{2/d}) behavior. ([arXiv][2])
At present, the necessary incidence technology is not known in the required generality.

If you tell me which dimension you care about most [[nomath]](say $d=3$ vs general $d$)[[/nomath]], I can unpack the specific exponent you get from the Solymosi–Vu recursion and how it compares numerically to $2/d$.

[1]: https://www.erdosproblems.com/forum/thread/1083 "

    Erdős Problem #1083 - Discussion thread

"
[2]: https://arxiv.org/abs/1705.10963?utm_source=chatgpt.com "A Reduction for the Distinct Distances Problem in  ..."

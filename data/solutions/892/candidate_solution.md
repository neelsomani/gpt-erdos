What you’re asking for is (essentially verbatim) an old Erdős–Sárközy–Szemerédi problem, and in full generality there is **no known necessary-and-sufficient criterion** at present. ([Erdős Problems][1])

That said, there *are* clean necessary conditions, and there is a fairly sharp “sufficient if (b_n) grows smoothly/regularly” theory.

## What is known in general

Let (b_1<b_2<\cdots) be given. You want a primitive (divisor-free) sequence (a_1<a_2<\cdots) such that
[
a_n \le C, b_n\qquad\text{for all }n
]
for some absolute constant $C$.

### Necessary conditions

1. **Erdős’s ( \sum 1/(n\log n)) condition is necessary.**

Erdős proved that for every primitive set (A\subset\mathbb N) (no element divides another),
[
\sum_{a\in A}\frac{1}{a\log a} < \infty,
]
indeed with a universal bound over all primitive sets. 

If you had (a_n\le Cb_n), then (b_n \ge a_n/C), hence
[
\frac{1}{b_n\log b_n}\ \ll\ \frac{1}{a_n\log a_n},
]
so convergence for (\sum 1/(a_n\log a_n)) forces convergence for (\sum 1/(b_n\log b_n)). This is recorded explicitly as a necessary condition for Erdős Problem #892. ([Erdős Problems][1])

So:
[
\boxed{\ \sum_{n=1}^\infty \frac{1}{b_n\log b_n}<\infty\ \text{ is necessary.}\ }
]

2. **A second necessary condition [[nomath]](Behrend $\to$ Erdős–Sárközy–Szemerédi)[[/nomath]].**

For a primitive set $A$, Behrend proved
$
\sum_{\substack{a<x\ a\in A}}\frac1a \ll \frac{\log x}{\sqrt{\log\log x}},
$
and Erdős–Sárközy–Szemerédi improved this to a little‑$o$ bound. ([Erdős Problems][2])

Again, if (a_n\le Cb_n), then the (b_n) must be sparse enough to allow such a primitive set at those scales, and #892 notes the following as necessary:
$
\boxed{\ \sum_{b_n<x}\frac{1}{b_n}=o(\frac{\log x}{\sqrt{\log\log x}}).\ }
$
([Erdős Problems][1])

A convenient reformulation of the first condition uses the counting function
[
B(x):=|\\{n: b_n\le x\\}|.
]
By partial summation,
(\sum 1/(b_n\log b_n)<\infty) is essentially equivalent to convergence of
[
\int_2^\infty \frac{B(t)}{t^2\log t},dt,
]
which is exactly the form that appears in the “counting function” viewpoint for primitive sets. 

### Sufficiency: open without extra hypotheses

Even if (\sum 1/(b_n\log b_n)<\infty) holds, **it is not known in general** whether a primitive sequence (a_n\ll b_n) must exist. This is the core of Erdős Problem #892. ([Erdős Problems][1])

## What is known for “smoothly growing” (b_n)

There is substantial progress if you assume that the growth of (b_n) [[nomath]](or equivalently $B(x)$)[[/nomath]] is not wildly irregular.

Martin–Pomerance (2010) prove an **approximate converse** to Erdős’s necessary integral condition: roughly, if a target function $F(x)$ is monotone and “smoothly growing” and
[
\int_2^\infty \frac{F(t)}{t^2\log t},dt<\infty,
]
then there exists a primitive set $S$ with counting function (S(x)\asymp F(x)). 
They explicitly frame this as giving a “yes” for smoothly growing sequences ({b_n}) satisfying the (\sum 1/(b_n\log b_n)) condition. 

They also give very dense explicit examples: if $L$ is slowly varying with
[
\int_2^\infty \frac{dt}{t\log tL(t)}<\infty,
]
then there is a primitive set $S$ with
[
S(x)\asymp \frac{x}{\log_2 x\cdot \log_3 x\cdot L(\log_2 x)},
]
and in particular many iterated‑log families. 
Inverting this tells you that **there exist primitive sequences** with $n$-th term on the order of
[
a_n \asymp n\log\log n\log\log\log nL(\log\log n)
]
(up to the usual slowly varying/iterated‑log ambiguities). 
So if your (b_n) is at least this large (and not too irregular), existing theorems already give (a_n\ll b_n).

## Your “no non-trivial ((b_i,b_j)=b_k)” hypothesis

The clause

> “In particular, is this always possible if there are no non-trivial solutions to ((b_i,b_j)=b_k)?”

is *exactly* the “in particular” part of Erdős Problem #892, and is (as currently recorded) **still open**. ([Erdős Problems][1])

Two clarifying remarks:

* If you interpret “no solutions” literally as “$(b_i,b_j)$ is never equal to any (b_k), even when $k=i$ or $k=j$”, then (b_i\mid b_j) is impossible [[nomath]](since it would give $(b_i,b_j)=b_i$)[[/nomath]], so ({b_n}) is itself primitive and you can take (a_n=b_n) trivially.

* If you mean the standard “non-trivial” = “$k$ is distinct from $i,j$”, then this gcd‑avoidance condition does not (by itself) replace the size constraints above; at minimum you still need (\sum 1/(b_n\log b_n)<\infty) and the reciprocal-sum bound, and whether the gcd hypothesis forces enough regularity/sparseness to guarantee (a_n\ll b_n) is part of what remains unresolved. ([Erdős Problems][1])

If you tell me a concrete asymptotic model for (b_n) [[nomath]](e.g. $b_n\asymp n(\log\log n)^2$, or $b_n\asymp n\log n/(\log\log n)^A$, or something more irregular)[[/nomath]], I can translate it into a counting-function condition and say whether the Martin–Pomerance machinery already guarantees a primitive (a_n\ll b_n) in that regime.

[1]: https://www.erdosproblems.com/forum/thread/892 "

    Erdős Problem #892 - Discussion thread

"
[2]: https://www.erdosproblems.com/tags/primitive%20sets "
  
    Erdős Problems
  
"

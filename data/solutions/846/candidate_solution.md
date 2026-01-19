As far as I can find in the literature, this is **open**. It appears as an Erdős–Nešetřil–Rödl “Pisier-type” decomposition problem (Erdős Problem #846), and the current recorded status is **OPEN** (no proof or counterexample known). ([Erdős Problems][1])

That said, there are a couple of quick (but not decisive) consequences of your hypothesis that are worth keeping in mind.

## Easy necessary consequences of the hypothesis

### 1) Uniform bound on collinearities

If (\ell) is any (Euclidean) line, then (|A\cap \ell|) is bounded in terms of (\varepsilon).

Indeed, if (|A\cap \ell|=k), take (B=A\cap \ell) so (|B|=k). Any subset of $B$ with “no three on a line” can have size at most $2$ [[nomath]](since all of $B$ is collinear)[[/nomath]]. Your assumption says $B$ contains such a subset of size (\ge \varepsilon k), so
[
2 \ge \varepsilon k \quad \Rightarrow \quad k \le \frac{2}{\varepsilon}.
]
So **no line contains more than (\lfloor 2/\varepsilon\rfloor) points of $A$**.

This is a strong geometric restriction, but it still doesn’t immediately yield a finite decomposition.

### 2) Logarithmic-colorability of finite subsets (but not constant)

Your condition is “hereditary” in the sense that it applies to *every* finite subset (B\subseteq A). So for any finite $B$ you can iteratively peel off large general-position subsets:

* Start with (B_0=B), (|B_0|=n).
* Choose (G_0\subseteq B_0) in general position with (|G_0|\ge \varepsilon |B_0|), remove it.
* Continue on the remainder (B_1=B_0\setminus G_0), etc.

After $t$ steps, the remaining size is at most ((1-\varepsilon)^t n). Hence any $n$-point subset of $A$ can be partitioned into
[
t \approx \frac{\log n}{\log\bigl(1/(1-\varepsilon)\bigr)}
]
general-position parts.

So you do get a *uniform* structural statement for finite subsets: **every $n$-point subset is a union of $O(\log n)$ no-three-collinear sets**. What’s missing (and what the problem asks) is whether you can improve $O(\log n)$ to a **constant depending only on (\varepsilon)**.

## Reformulation as a coloring problem

Let $H(A)$ be the 3-uniform hypergraph on vertex set $A$ whose hyperedges are the collinear triples. Then:

* “no three on a line” = “independent set in $H(A)$”
* “union of $m$ sets with no three on a line” = “$m$-coloring of $H(A)$” (no monochromatic hyperedge)
* your hypothesis says: every finite induced subhypergraph on $n$ vertices has independence number (\ge \varepsilon n).

The question becomes: **does a uniform linear lower bound on independence number in every finite induced subhypergraph force finite chromatic number**, in this *geometric* hypergraph?

That is exactly what is recorded as open in the Erdős Problems listing. ([Erdős Problems][1])

## Trivial “yes” in some extreme ranges

* If (\varepsilon > 2/3), then no three points of $A$ can be collinear at all [[nomath]](since a 3-point collinear set would only allow 2 in general position, contradicting $2 \ge 3\varepsilon$)[[/nomath]]. Then $A$ itself already has no three collinear (1 piece).
* More generally, the bound (|A\cap \ell|\le 2/\varepsilon) shows larger (\varepsilon) forces smaller maximum collinearity, but the finite-decomposition conclusion is still not known in general.

## Bottom line

* The implication “finite union of general-position sets (\Rightarrow) your (\varepsilon)-property” is easy (pigeonhole), but
* the converse you asked about is, as far as I can verify, a **known open problem** (Erdős Problem #846). ([Erdős Problems][1])

If you want, I can also sketch a few natural strategies people try for problems of this type [[nomath]](compactness/finite reduction, hypergraph container heuristics, and how one might attempt to build a counterexample by assembling finite high-chromatic configurations while preserving the $\varepsilon$-property)[[/nomath]]—but the definitive “true/false” is not currently settled in the references I can access.

[1]: https://www.erdosproblems.com/forum/thread/846 "

    Erdős Problem #846 - Discussion thread

"

This is **open** (as of the most recent public updates I can find, including an Erdős-problems catalogue entry last edited **Jan 1, 2026**). ([Erdős Problems][1])

### Why “$n/2$” is the right scale

You **cannot** hope for a lower bound asymptotically larger than $n/2$, because there are convex polyhedra with only about $n/2$ distinct distances.

A standard example is an $(n!-!2)$-gonal **bipyramid** (double pyramid): take a regular $(n-2)$-gon as a base and add two apices above and below the base plane. (A bipyramid is exactly “two pyramids glued base-to-base.”) ([Wikipedia][2])

* The distances among the base vertices are just the chord lengths of a regular $(n-2)$-gon, giving (\lfloor (n-2)/2\rfloor) distinct distances.
* The distance from an apex to any base vertex is a single value (by symmetry), and by choosing the height appropriately you can make this coincide with one of the base chord lengths, so it introduces **no new distance**.
* The apex–apex distance contributes at most one additional value.

So this construction has **(\le \lfloor (n-2)/2\rfloor + 1 = \lfloor n/2\rfloor)** distinct distances [[nomath]](and in any case $= n/2 + O(1)$)[[/nomath]].
Thus the conjectured ((1-o(1)),\frac n2) lower bound would be **asymptotically tight** if true.

### What is known in the plane

For comparison, in (\mathbb R^2) the exact analogue *is* true: every convex $n$-gon determines at least (\big\lfloor \tfrac n2\big\rfloor) distinct inter-vertex distances (Altman, 1963), and this bound is sharp [[nomath]](e.g. regular $n$-gon)[[/nomath]]. ([Erdős Problems][3])

### What is known in (\mathbb R^3) for convex polyhedra

The best general result I can point to in the literature is **only a linear lower bound with an unspecified constant**: Erdős reports that Altman proved that if (x_1,\dots,x_n) are the vertices of a convex polyhedron in (\mathbb R^3), then the number of distinct distances is (>,c n) for some absolute (c>0). ([Springer][4])

But the much stronger statement you ask about—forcing the constant up to $1/2$ asymptotically, i.e.
$
|\\{,|x_i-x_j| : i<j,\\}|\ \ge\ (\tfrac12-o(1))n
$
—appears as an explicit **open problem** (Erdős Problem #660). ([Erdős Problems][1])

### Bottom line

No general proof (or disproof) is currently known that every convex polyhedron with $n$ vertices determines at least ((1-o(1)),\frac n2) distinct distances. The best published guarantee seems to be only (\Omega(n)) (Altman, via Erdős), while constructions show you cannot hope for more than (\sim n/2). ([Springer][4])

[1]: https://www.erdosproblems.com/forum/thread/660 "

    Erdős Problem #660 - Discussion thread

"
[2]: https://en.wikipedia.org/wiki/Bipyramid?utm_source=chatgpt.com "Bipyramid"
[3]: https://www.erdosproblems.com/latex/93 "
  
    Erdős Problems
  
"
[4]: https://link.springer.com/content/pdf/10.1007/BF02414146.pdf "On some problems of elementary and combinatorial geometry"

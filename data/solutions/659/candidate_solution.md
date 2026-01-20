Yes.

A concrete example is a **truncated anisotropic lattice** (a “stretched grid”).  Take
[
P_m={(i,\sqrt2,j):0\le i,j\le m-1}\subset \mathbb Z\times \sqrt2,\mathbb Z,
]
so (|P_m|=m^2). ([Erdős Problems][1])

## Few global distinct distances

For two points ((i,\sqrt2,j),(i',\sqrt2,j')\in P_m), the squared distance is
[
(i-i')^2+2(j-j')^2=u^2+2v^2,
]
with (|u|,|v|\le m-1), hence (\le 3m^2). So the distinct distances are controlled by how many integers (\le 3m^2) are representable by the binary quadratic form (u^2+2v^2). ([Erdős Problems][1])

By Bernays-type results for such quadratic forms, the number of represented integers (\le x) is (\asymp x/\sqrt{\log x}), giving
[
|D(P_m)| = O!\left(\frac{m^2}{\sqrt{\log m}}\right)
= O!\left(\frac{n}{\sqrt{\log n}}\right)
]
when (n=m^2). ([Erdős Problems][1])
For general $n$, take any $n$-point subset of (P_{\lceil\sqrt n\rceil}); removing points cannot increase the number of distinct distances. ([arXiv][2])

## Every 4 points give at least 3 distances

A 4-point set violates the local condition **iff** it determines **exactly two** distances; up to similarity there are only six such “two-distance” 4-point configurations. ([arXiv][2])
Moreover, by the classification used in the solution, any such configuration is either

* a **square**, or
* contains an **equilateral triangle**, or
* is similar to the **“regular-pentagon trapezoid”** (four vertices of a regular pentagon). ([arXiv][2])

In (\mathbb Z\times\sqrt2,\mathbb Z), none of these occur:

* **No squares:** a nondegenerate square would require a (90^\circ) rotation of a lattice side-vector to remain in the same lattice, which forces degeneracy. ([arXiv][2])
* **No equilateral triangles:** a (60^\circ) rotation introduces (\sqrt3)-coefficients, incompatible with the (\mathbb Q(\sqrt2)) structure of the lattice. ([arXiv][2])
* **No regular-pentagon trapezoid:** that shape forces the (diagonal/side)(^2) ratio (\phi^2=(3+\sqrt5)/2) (irrational), but here all squared distances are integers (u^2+2v^2), so any ratio of squared distances is rational. ([arXiv][2])

Therefore **every 4-point subset determines at least 3 distinct distances**. ([arXiv][2])

This construction (and the full verification) is written up in a January 2026 note solving Erdős Problem #659 in the affirmative. ([arXiv][2])

[1]: https://www.erdosproblems.com/forum/thread/659 "

    Erdős Problem #659 - Discussion thread

"
[2]: https://arxiv.org/html/2601.09102v1 "Solution to a Problem of Erdős Concerning Distances and Points"

Let (\mu:=2^{\aleph_0}) and (\kappa:=\mu^+). The question is asking for a coloring
[
c:[m]^{\aleph_0}\to \kappa
]
such that for every (X\subseteq m) with (|X|=\kappa),
[
c\bigl[[X]^{\aleph_0}\bigr]=\kappa,
]
i.e. every (\kappa)-sized $X$ is “fully polychromatic” on its countable subsets [[nomath]](in partition notation, $m\nrightarrow[\kappa]^{\aleph_0}_{\kappa}$)[[/nomath]].

### Trivial reduction and the real case

* If (m<\kappa), there is no (X\subseteq m) of size (\kappa), so the requirement is vacuous.
* If (m\ge\kappa), then the problem essentially reduces to the case (m=\kappa): if such a $c$ exists on $m$, then restricting $c$ to some (Y\subseteq m) with (|Y|=\kappa) and transporting along a bijection (\kappa\cong Y) produces the same kind of coloring on (\kappa).

So the heart of the question is: does such a coloring exist on (\kappa=(2^{\aleph_0})^+)?

### Current status

As of the current state of the literature reflected by the Erdős problems database, this is **open** (Erdős Problem #598). ([Erdős Problems][1])

### A useful sufficient condition (why “strong colorings” matter)

A standard sufficient route is via a **strong coloring of pairs** on (\kappa), i.e. a function
[
f:[\kappa]^2\to\kappa
\quad\text{such that}\quad
\forall X\in[\kappa]^\kappa,; f\bigl[[X]^2\bigr]=\kappa
]
[[nomath]](denoted $\kappa\nrightarrow[\kappa]^2_\kappa$ in the “strong coloring” literature)[[/nomath]].

If you had such an $f$, you can turn it into a coloring of countably infinite subsets by
[
c(A):=f(\min A,\ \text{2nd-min}(A)).
]
Given any (X\in[\kappa]^\kappa) and any (\gamma<\kappa), you thin $X$ by deleting its (at most) countably many “top” elements that have only finitely many larger elements in $X$; the remainder still has size (\kappa), so $f$ produces a pair ({\alpha<\beta}\subseteq X) with (f(\alpha,\beta)=\gamma) and with infinitely many points of $X$ above (\beta). Then extend ({\alpha,\beta}) to a countably infinite (A\subseteq X) whose two least elements are (\alpha,\beta), forcing (c(A)=\gamma).

So: **a strong pair-coloring on (\kappa) would imply a “yes” answer** to your question.

### Why it’s still open for (\kappa=(2^{\aleph_0})^+)

Strong pair-colorings with (\kappa) colors are known in many settings, but they are not known in full generality at (\kappa=(2^{\aleph_0})^+) without extra hypotheses about the continuum’s cardinal arithmetic/pcf behavior. A good summary of known ZFC results and conditional results is in the “strong colorings” literature (e.g. Shelah/Todorčević/Rinot developments). ([arXiv][2])

In particular:

* **ZFC gives strong colorings on double successors of regulars:** Shelah proved strong coloring principles of the form (\mathrm{Pr}_1(\kappa^{++},\kappa^{++},\kappa^{++},\kappa)) for every regular (\kappa), yielding very strong “all colors appear” behavior on (\kappa^{++}). ([arXiv][2])
  So if your ((2^{\aleph_0})^+) happens to be such a (\kappa^{++}) (e.g. in common situations where the continuum is a successor of a regular), then the desired coloring exists by the reduction above.
* **For successors of singulars:** Todorčević showed that certain pcf hypotheses [[nomath]](e.g. $pp(\mu)=\mu^+$ for singular $\mu$)[[/nomath]] imply (\mu^+\nrightarrow[\mu^+]^2_{\mu^+}), and Rinot and others refined equivalences around these strong coloring principles. ([arXiv][2])
  If (2^{\aleph_0}) were singular and satisfied the relevant pcf condition, that would again give a positive answer.

But **without** assuming such structure on (2^{\aleph_0}) [[nomath]](and hence on $\kappa$)[[/nomath]], the existence of the required coloring is exactly what remains unresolved in Erdős Problem #598. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/598 "https://www.erdosproblems.com/598"
[2]: https://arxiv.org/pdf/2002.06705 "https://arxiv.org/pdf/2002.06705"

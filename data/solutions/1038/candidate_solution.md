Let
[
S_f:={x\in\mathbb R:\ |f(x)|<1},\qquad m(f):=|S_f|
]
(Lebesgue measure).  Note that replacing “(<1)” by “(\le 1)” does **not** change the measure, because (|f(x)|=1) has only finitely many real solutions.

## Supremum

[
\boxed{\ \sup m(f)=2\sqrt2\ }.
]

* **Attainment:** For (f(x)=x^2-1) [[nomath]](monic, roots $\pm 1\in[-1,1]$)[[/nomath]],
  $
  |f(x)|<1\iff |x^2-1|<1\iff 0<x^2<2\iff |x|<\sqrt2,
  $
  so (S_f=(-\sqrt2,\sqrt2)) and (m(f)=2\sqrt2).

* **Sharp upper bound:** It is known that for *every* monic polynomial whose roots lie in an interval of length $2$ [[nomath]](in particular in $[-1,1]$)[[/nomath]], one has
  [
  m(f)\le 2\sqrt2,
  ]
  with equality (in the normalized case) only for the “two-point” extremizer corresponding to ({\pm1}), i.e. essentially (x^2-1) (or its even powers, which give the same sublevel set). 

So the supremum is exactly (2\sqrt2), and it is achieved.

## Infimum

Here the situation is very different: the **exact value is not known** (this is a classical Erdős–Herzog–Piranian problem).

Let
[
m_*:=\inf m(f)\quad\text{over all non-constant monic real-rooted }f\text{ with roots in }[-1,1].
]
Then:

* The problem of determining (m_*) exactly is **open**. 
* The currently recorded best bounds (in the literature summaries) are
  $
  \boxed{\ 2^{4/3}-1\ \lesssim\ 1.519\ \le\ m_*\ \le\ 1.835\ldots\ }
$
  and there is strong evidence/heuristics that the true minimum is **around $1.835$**. 
* In particular, it is known $m_*<2$ [[nomath]](so you can make the “$|f|<1$” set shorter than length $2$)[[/nomath]], e.g. by taking highly unbalanced endpoint-multiplicity polynomials like $(x+1)(x-1)^m$ for $m\ge 3$.

## Final answer

$
\boxed{\ \sup m(f)=2\sqrt2,\ \text{attained by }f(x)=x^2-1\ }
$
and
$
\boxed{\ \inf m(f)\ \text{is not currently known; }1.519\ldots\le \inf m(f)\le 1.835\ldots\ }
$
with the best current evidence suggesting the infimum is close to $1.835$. 

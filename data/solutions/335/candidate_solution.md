Assume throughout that **natural density** exists:
[
d(A)=\lim_{N\to\infty}\frac{|A\cap[1,N]|}{N}.
]
Write (A\sim A') if (d(A\triangle A')=0) (they differ on a density–(0) set). Note that (d(A+t)=d(A)) for each fixed $t$, and finite changes don’t affect density.

Let (\alpha=d(A)>0), (\beta=d(B)>0).
A necessary condition for
[
d(A+B)=d(A)+d(B)
]
is (\alpha+\beta\le 1) [[nomath]](since $d(A+B)\le 1$)[[/nomath]].

What follows is the clean structural description “up to (\sim)” [[nomath]](i.e. up to density–$0$ perturbations)[[/nomath]], which is the right equivalence relation for density questions.

---

## The classification (up to density–0 changes)

Pairs ((A,B)\subseteq\mathbb N) with (\alpha,\beta>0) satisfy
[
d(A+B)=\alpha+\beta
]
**if and only if** [[nomath]](after translating $A,B$ by fixed integers and modifying on density–$0$ sets)[[/nomath]] they come from a **one–dimensional compact abelian model** in the following sense:

There exist

* a finite-index arithmetic “period” (q\ge 1),
* a compact abelian group $G$ which is either a **finite cyclic group** (\mathbb Z/m\mathbb Z) or the **circle** (\mathbb T=\mathbb R/\mathbb Z) (or, more generally, a finite cyclic factor times a circle factor),
* a homomorphism (\chi:\mathbb Z\to G),
* “interval-like” measurable sets (I,J\subseteq G) [[nomath]](intervals/arcs in $\mathbb T$; in the finite cyclic case, the appropriate discrete analogues)[[/nomath]],
  such that
  [
  A\sim \chi^{-1}(I)\cap\mathbb N,\qquad B\sim \chi^{-1}(J)\cap\mathbb N,
  ]
  and
  [
  m(I+J)=m(I)+m(J)\quad(\le 1),
  ]
  so that
  [
  A+B\sim \chi^{-1}(I+J)\cap\mathbb N
  ]
  and hence
  [
  d(A+B)=m(I+J)=m(I)+m(J)=d(A)+d(B).
  ]

This is exactly the **“sur-critical”** situation in the sense of inverse theorems for sumsets in compact abelian groups: when the measure of the sumset is the sum of the measures, one is forced into (essentially) a 1-dimensional factor and “interval structure”, possibly with periodic/quasi-periodic components. ([arXiv][1])

A useful complementary fact is Kneser’s theorem in density form: if one ever has **strict inequality** (d(A+B)<d(A)+d(B)), then $A+B$ must be (eventually) periodic modulo some $d$, and one gets the familiar “loss” term $1/d$. ([People][2])
So the equality case is precisely the “no loss” boundary where the inverse theory forces the above 1D interval model.

To make this more concrete, here are the two main “pure” types (plus the mixed/quasi-periodic type).

---

## 1) Pure periodic type (finite cyclic model)

There exists (q\ge 1) and subsets (S,T\subseteq \mathbb Z/q\mathbb Z) such that
[
A\sim {n\in\mathbb N:\ n\bmod q\in S},\qquad
B\sim {n\in\mathbb N:\ n\bmod q\in T},
]
and in (\mathbb Z/q\mathbb Z),
[
|S+T|=|S|+|T|.
]
Then
[
d(A)=\frac{|S|}{q},\quad d(B)=\frac{|T|}{q},\quad d(A+B)=\frac{|S+T|}{q}
=\frac{|S|+|T|}{q}=d(A)+d(B).
]

This includes many examples where $S,T$ are *not* consecutive residues; the condition is exactly the finite-group equality (|S+T|=|S|+|T|) (classified in full generality in the discrete inverse theory referenced in Griesmer’s discussion). ([arXiv][1])

---

## 2) Pure Sturmian/rotation type (circle model)

Pick an irrational (\theta\in\mathbb R\setminus\mathbb Q), and arcs (intervals) (I,J\subseteq\mathbb T) with lengths (|I|=\alpha), (|J|=\beta) and (\alpha+\beta\le 1). Define
[
A_\theta(I)={n\in\mathbb N:\ {n\theta}\in I},\qquad
B_\theta(J)={n\in\mathbb N:\ {n\theta}\in J}.
]
By equidistribution, (d(A_\theta(I))=|I|), (d(B_\theta(J))=|J|). Moreover, because (I+J) is again an interval of length (|I|+|J|) when (|I|+|J|\le 1), one has
[
A_\theta(I)+B_\theta(J)\sim A_\theta(I+J),
]
so
[
d(A+B)=|I+J|=|I|+|J|=d(A)+d(B).
]

This is the aperiodic “interval on the circle” mechanism (the connected-group case in the inverse theorem). ([arXiv][1])

---

## 3) Mixed/quasi-periodic type (periodic background + one interval factor)

There is also a genuinely mixed possibility: after passing to a period $q$, each of $A$ and $B$ may have a $q$-periodic part plus an “exceptional” part inside one residue class modulo $q$, where the exceptional parts form either a finite-cyclic interval pair or a Sturmian interval pair as above. The sum of the exceptional parts contributes a “unique expression” chunk in the quotient, so the densities add without “extra overlap”; this is the quasi-periodic/extendible phenomena in the general classification of sur-critical pairs. ([arXiv][1])

This mixed case is exactly why a complete characterization cannot be stated purely as “both are preimages of circle intervals”: there can be nontrivial periodic structure sitting alongside the 1D interval factor.

---

## Summary in one sentence

Up to translating and changing on density–$0$ sets, the equality
[
d(A+B)=d(A)+d(B)
]
holds **exactly** for those pairs $(A,B)$ whose large-scale additive structure is governed by a **1‑dimensional compact abelian factor** (finite cyclic and/or circle) in which $A$ and $B$ are essentially **interval-like**, so that “no wrap-around” occurs and the Haar measure of $I+J$ is the sum $m(I)+m(J)$. ([arXiv][1])

---

If you tell me whether you want the characterization **(a)** “up to density–0 equivalence” (as above, which is standard for density problems), or **(b)** “literal equality of sets” (no modification allowed), I can rewrite the statement in the exact form you prefer.

[1]: https://arxiv.org/pdf/1112.6403 "https://arxiv.org/pdf/1112.6403"
[2]: https://people.dm.unipi.it/dinasso/ULTRABIBLIO/Jin%20-%20Ultrapower%20of%20N%20and%20density%20problems%20%282010%29.pdf "https://people.dm.unipi.it/dinasso/ULTRABIBLIO/Jin%20-%20Ultrapower%20of%20N%20and%20density%20problems%20%282010%29.pdf"

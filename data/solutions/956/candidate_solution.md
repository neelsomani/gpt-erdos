Let (C\subset\mathbb R^2) be compact and convex, and let (x,y\in\mathbb R^2).  Write
[
D:=C-C={c_1-c_2:\ c_1,c_2\in C}.
]
Then $D$ is compact, convex, and centrally symmetric.

## 1) Reduce (\delta(C+x,C+y)) to distance from a point to $D$

**Claim.** For all (x,y\in\mathbb R^2),
[
\delta(C+x,C+y)=\operatorname{dist}(y-x,,D),
]
where (\operatorname{dist}(v,D)=\inf_{d\in D}|v-d|).

**Proof.**
[
\delta(C+x,C+y)
=\inf_{c_1,c_2\in C}|(c_1+x)-(c_2+y)|
=\inf_{c_1,c_2\in C}|(x-y)+(c_1-c_2)|.
]
Let (d=c_2-c_1\in C-C=D). Then (c_1-c_2=-d) and since (D=-D),
[
\inf_{c_1,c_2\in C}|(x-y)+(c_1-c_2)|
=\inf_{d\in D}|(x-y)-d|
=\operatorname{dist}(x-y,D)
=\operatorname{dist}(y-x,D),
]
using symmetry of distance. ∎

Therefore, if we define the “unit-distance shell”
[
\Gamma:={v\in\mathbb R^2:\ \operatorname{dist}(v,D)=1},
]
then for distinct translates (C+x_1) and (C+x_2),
[
\delta(C+x_1,C+x_2)=1 \iff x_2-x_1\in \Gamma.
]

Equivalently, if we look at the translate family ({\Gamma+x:\ x\in X}), then
[
x_2-x_1\in\Gamma \iff x_2\in x_1+\Gamma.
]
So **unit-distance pairs among translates are incidences between the point set $X$ and the curve family ({x+\Gamma}_{x\in X}).**

A useful geometric identity is
[
\Gamma = \partial(D + B(0,1)),
]
the boundary of the Minkowski sum of $D$ with the unit disk, because ({v:\operatorname{dist}(v,D)\le1}=D+B(0,1)).

---

## 2) The known (best possible up to constants) upper bound (h(n)=O(n^{4/3}))

Erdős and Pach proved that
[
h(n)\ll n^{4/3}.
]
This is recorded in the Erdős problems collection for this problem. ([Erdős Problems][1])

Here is the standard incidence-geometry mechanism behind it (sketch, but with the key geometric inputs made explicit):

### 2a) Translate-incidence viewpoint

Let (X\subset\mathbb R^2) be any set of size $n$ such that ((C+x)_{x\in X}) are disjoint.
Let
[
I := |\\{(x,y)\in X\times X:\ y\in x+\Gamma\\}|
]
be the number of **directed** incidences. Then the number of **undirected** unit-distance pairs is (m=I/2) [[nomath]](since $D$ is centrally symmetric, $\Gamma$ is centrally symmetric, so $y-x\in\Gamma\iff x-y\in\Gamma$)[[/nomath]]. Thus (h(n)\le I/2).

So it suffices to bound incidences between:

* $n$ points: $X$,
* $n$ curves: (\mathcal C := {x+\Gamma:\ x\in X}).

### 2b) Key geometric input: translates of a convex curve form a pseudo-circle family

(\Gamma=\partial(D+B(0,1))) is a convex, simple closed curve [[nomath]](possibly with corners if $D$ has edges, but still the boundary of a convex body)[[/nomath]].
Two distinct translates (\Gamma+x) and (\Gamma+x') are congruent convex curves. A standard convexity fact is that two translates of a convex simple closed curve intersect in **at most two points** [[nomath]](unless they coincide, which only happens for $x=x'$)[[/nomath]]. This puts (\mathcal C) into the class of “pseudo-circles”.

For pseudo-circles, there is an incidence bound of Szemerédi–Trotter type (Pach–Sharir framework / crossing-number method):
[
I(X,\mathcal C) = O\bigl(n^{2/3}n^{2/3}+n+n\bigr)=O(n^{4/3}).
]

Applying this with $n$ points and $n$ curves gives (I=O(n^{4/3})), hence
[
h(n)=O(n^{4/3}).
]

This matches exactly what Erdős–Pach state as the best known upper bound. ([Erdős Problems][1])

---

## 3) Lower bounds and the status of the “(n^{1+c})” question

A trivial (but important) observation is that you can recover the classical unit-distance problem for points by taking $C$ to be a single point. Then translates are just points (automatically disjoint), and (\delta({x},{y})=|x-y|). Hence
[
h(n)\ \ge\ f(n),
]
where $f(n)$ is the maximum number of unit distances determined by $n$ points in the plane. This reduction is explicitly noted in the Erdős problems entry. ([Erdős Problems][1])

The difficulty is that the best known lower bounds for $f(n)$ are of the form (n^{1+o(1)}) [[nomath]](superlinear but with exponent tending to $1$)[[/nomath]], and **do not** yield a fixed (c>0). Therefore this reduction alone does not prove (h(n)\ge n^{1+c}).

### Current status (as recorded in the problem source)

The Erdős problems page lists as the open challenge exactly what you ask for: prove there exists (c>0) with (h(n)>n^{1+c}) for all large $n$. ([Erdős Problems][1])

So, as of the sources above, we can **determine the best known asymptotic framework**:

* **Upper bound:** (h(n)=O(n^{4/3})) (Erdős–Pach). ([Erdős Problems][1])
* **Lower bound:** (h(n)\ge f(n)=n^{1+o(1)}) via (C={\text{point}}). ([Erdős Problems][1])
* The existence of a fixed exponent gap (h(n)\ge n^{1+c}) is posed there as an open problem. ([Erdős Problems][1])

---

## 4) What one would need for a (n^{1+c}) construction

Because of the reduction
[
\delta(C+x_1,C+x_2)=\operatorname{dist}(x_2-x_1,,D),
]
a construction must produce a set $X$ with:

1. (**Packing constraint**) (x-x'\notin D) for all distinct (x,x'\in X), i.e. $X$ is a translate-packing for $C$;
2. (**Many boundary differences**) many differences (x_2-x_1) land on
   (\Gamma=\partial(D+B(0,1))).

In incidence language: you need a point set $X$ with many incidences with its own translate family ({x+\Gamma}_{x\in X}), while simultaneously enforcing the packing constraint [[nomath]](which rules out the densest “grid-on-grid” incidence configurations that normally witness $n^{4/3}$ sharpness for Szemerédi–Trotter-type bounds)[[/nomath]].

That packing constraint is exactly what makes the (n^{1+c}) lower bound hard beyond the classical unit-distance reduction.

---

## Summary

* There is a clean reduction
  [
  \delta(C+x,C+y)=\operatorname{dist}(y-x,\ C-C),
  ]
  so “unit distance between translates” becomes “difference vector lies on the parallel boundary (\partial((C-C)+B(0,1)))”.
* Erdős–Pach’s incidence argument yields the sharp general **upper bound** (h(n)=O(n^{4/3})). ([Erdős Problems][1])
* The best general **lower bound** currently forced by known methods is (h(n)\ge f(n)=n^{1+o(1)}) by taking $C$ a point. ([Erdős Problems][1])
* The statement “there exists a fixed (c>0) with (h(n)>n^{1+c}) for all large $n$” is presented in the same source as an **open problem**. ([Erdős Problems][1])

If you want, I can also write out a fuller, self-contained proof of the $O(n^{4/3})$ bound (via the crossing-number method for pseudo-circles) in the exact “Erdős–Pach style”, with all constants and the pseudo-circle intersection lemma spelled out.

[1]: https://www.erdosproblems.com/956 "https://www.erdosproblems.com/956"

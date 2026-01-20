It helps to package your question as an extremal graph problem.

## Reformulation as a clique threshold in the “ordinary-line graph”

Given (A\subset\mathbb R^2), define the **ordinary-line graph**
[
G(A):V(G)=A,\qquad {p,q}\in E(G)\iff \overline{pq}\text{ is ordinary in }A.
]
So (|E(G(A))|) is exactly the number of ordinary lines in $A$.

Your desired conclusion [[nomath]](“there is $A'\subseteq A$ of size $r$ such that all $\binom r2$ lines spanned by $A'$ are ordinary”)[[/nomath]] is exactly:
[
G(A)\text{ contains a }K_r.
]

Thus the threshold you ask for is the extremal function
[
f_{r,k}(n)=1+\max\\{|E(G(A))|:\ |A|=n,\ A\text{ has no }k\text{ collinear points, and }G(A)\text{ is }K_r\text{-free}\\}.
]

This makes clear what has to be proved: **how many ordinary lines can a (K_r)-free ordinary-line graph have, under a “no $k$ collinear” geometric realizability constraint?**

## Easy boundary cases

* **$k=3$** (no three collinear). Then *every* line through two points contains exactly two points, so (G(A)=K_n) and any $r$-subset works. Hence
  [
  f_{r,3}(n)=0\quad(\text{for }n\ge r).
  ]

* **$r=2$** is trivial: (f_{2,k}(n)=1) [[nomath]](assuming $A$ is non-collinear so at least one ordinary line exists)[[/nomath]].

The real content starts at **(k\ge4) and (r\ge3)**.

## A robust lower bound: (f_{r,k}(n)) cannot be sublinear

For every fixed (k\ge4) and every (r\ge3),
[
f_{r,k}(n)=\Omega(n).
]

Reason: there are well-known “cubic/elliptic-curve” constructions (they are precisely the structured families that appear in the Green–Tao classification of sets with few ordinary lines) where

* no four points are collinear [[nomath]](so they satisfy “no $k$ collinear” for every $k\ge4$)[[/nomath]], and
* the number of ordinary lines is (\Theta(n)),
* yet the ordinary-line graph has **bounded clique number** [[nomath]](in fact it can be made triangle-free, hence $K_r$-free for all $r\ge3$)[[/nomath]].

A clean way to see this is via the group law on a real nonsingular cubic (elliptic curve): take a cyclic subgroup $H$ of size $n$ in the real points of an elliptic curve embedded in (\mathbb R^2). For “most” pairs (P,Q\in H), the line $PQ$ meets the cubic in a third point (R=-(P+Q)\in H), so $PQ$ is **not** ordinary; ordinary lines come essentially only from tangents [[nomath]](the “$Q=-2P$” situation)[[/nomath]], which gives only (\Theta(n)) ordinary lines. Moreover the ordinary-line graph in this model is a union of cycles [[nomath]](degree $\le2$)[[/nomath]], so it contains no (K_r) for any fixed (r\ge3) [[nomath]](and by choosing $n$ appropriately one can avoid even triangles)[[/nomath]].

This phenomenon is exactly in the orbit of Green–Tao’s structure theorem for point sets with $O(n)$ ordinary lines: such sets are forced to be “close to cubic curves” [[nomath]](or close to a line, which is excluded by your no-$k$-collinear assumption when $n$ is large)[[/nomath]]. ([ResearchGate][1])

So:

* **You cannot hope for (f_{r,k}(n)\ll n^\alpha) with (\alpha<1)** [[nomath]](for $k\ge4,r\ge3$)[[/nomath]]. In particular, (f_{r,k}(n)) is **not** $o(n)$.
* Linear growth is the smallest plausible order.

## Trivial general upper bound: always (\le \Theta(n^2))

Independently of geometry, Turán’s theorem gives for any graph on $n$ vertices
[
|E(G)|> \mathrm{ex}(n,K_r)=\\(1-\frac1{r-1}\\)\frac{n^2}{2}+O(n)
\quad\Longrightarrow\quad
K_r\subseteq G.
]
Hence
[
f_{r,k}(n)\ \le\ \\(1-\frac1{r-1}\\)\frac{n^2}{2}+O(n).
]
This is sharp for arbitrary graphs, but it ignores the very strong realizability restrictions coming from “edges = ordinary lines”.

## What is known that’s genuinely geometric, and why it doesn’t settle your $c=2$ problem

There is a parallel line of work on **“ordinary triangles”** and, more generally, **$c$-ordinary triangles**: triangles whose three sides each contain at most $c$ points of the set. Dubroff showed one can take $c=11$ (improving an earlier huge constant) for large point sets not contained in the union of two lines. ([ResearchGate][1])

That is philosophically close to your $r=3$ question, but it is **much weaker** than asking for all three sides to be *ordinary* [[nomath]](which is $c=2$)[[/nomath]]. In particular, when $k=4$ (no four collinear), “$c$-ordinary” with any (c\ge3) is automatic and gives no information toward $c=2$.

So the existing “ordinary triangle” literature currently supports the idea that forcing **exactly two** points per side is delicate, and that cubic-like configurations are the principal obstructions. ([ResearchGate][1])

## Where this leaves the threshold question

For (k\ge4) and (r\ge3), what we can say cleanly is:

* **Lower bound (constructive):**
  [
  f_{r,k}(n)\ge c_{r,k},n
  ]
  because there are no-$4$-collinear cubic constructions with (\Theta(n)) ordinary lines but no ordinary (K_r).

* **Upper bound (purely graph-theoretic):**
  [
  f_{r,k}(n)\le \\(1-\frac1{r-1}\\)\frac{n^2}{2}+O(n).
  ]

The main open-looking gap is: **can one beat the (n^2) Turán scale using the “no $k$ collinear” geometry?**

### Is (f_{r,k}(n)=o(n^2)) plausible?

Yes, it’s plausible, because the usual quadratic Turán extremisers [[nomath]](complete $(r!-1)$-partite graphs)[[/nomath]] would require a way of making huge parts with *no* ordinary edges **without** creating large collinearities and without sacrificing most cross-edges—this is exactly the kind of thing real-plane incidence geometry tends to obstruct (and in the extreme “few ordinary lines” regime Green–Tao shows you essentially fall into cubic structure). ([ResearchGate][1])

But I do not know a published theorem that gives a general subquadratic upper bound for your (f_{r,k}(n)) for fixed (r,k\ge4). The natural candidate statement would be:

> **Conjecture (linear threshold).** For each fixed (r\ge3) and (k\ge4) there exists (C=C(r,k)) such that
> if $A$ has no $k$ collinear points and at least (C n) ordinary lines, then $G(A)$ contains a (K_r).
> Equivalently, (f_{r,k}(n)=\Theta_{r,k}(n)).

This would be *tight in order*, in view of the elliptic-curve/cubic constructions giving (\Theta(n)) ordinary lines but no ordinary (K_r).

### Is (f_{r,k}(n)\ll n) (i.e., linear) true?

* It **cannot** be $o(n)$ (as above).
* Whether it is **always** $O(n)$ for fixed (r,k\ge4) is exactly the “interesting” content: it would amount to proving that **any** (K_r)-free ordinary-line graph arising from a no-$k$-collinear point set must have only $O(n)$ edges—i.e., must essentially live in the “few ordinary lines (\Rightarrow) cubic structure” regime of Green–Tao. ([ResearchGate][1])

I don’t have a definitive proof of that implication from the sources I could access; it looks like a genuinely nontrivial strengthening of the current “few ordinary lines” structural picture.

## Related viewpoint that may help (if you want to push further)

By projective duality, your problem is equivalent to:

* $n$ lines in the plane with no $k$ concurrent,
* many **ordinary intersection points** (points where exactly 2 lines meet),
* force $r$ lines whose (\binom r2) pairwise intersections are all ordinary in the full arrangement.

This is the same clique problem on the “ordinary-intersection graph” of a line arrangement, and it makes the obstruction from cubic/elliptic configurations feel very natural.

---

If you tell me which regime you care about most [[nomath]](e.g. the first nontrivial case $r=3,k=4$, or $r$ fixed and $k\to\infty$, or whether you allow projective transformations)[[/nomath]], I can try to push a concrete bound in that regime; but in full generality, the clean takeaway is:

* **Linear lower bound is real and unavoidable** for (k\ge4,r\ge3).
* **A linear upper bound is a very natural conjecture**, but I cannot honestly present it as settled based on what I can currently cite.

[1]: https://www.researchgate.net/publication/325262770_A_better_bound_for_ordinary_triangles "https://www.researchgate.net/publication/325262770_A_better_bound_for_ordinary_triangles"

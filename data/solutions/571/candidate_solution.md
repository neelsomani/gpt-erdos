As written, your statement for a **single forbidden bipartite graph** is exactly the *inverse rational exponents conjecture* of Erdős–Simonovits, and it is **still open** in that “single graph” form. What *is* known (and is often what exercises intend) is the following slightly weaker but very strong theorem of **Bukh–Conlon**: every rational exponent in $[1,2)$ occurs as the Turán exponent of a **finite family** of **bipartite** graphs. ([advancesincombinatorics.com][1])

I’ll show that statement (and point out where the “family” enters).

---

## Step 0: Extremal number for a family

For a (finite) family (\mathcal F) of graphs, (\mathrm{ex}(n,\mathcal F)) is the maximum number of edges in an $n$-vertex graph containing **no** member of (\mathcal F) as a subgraph. [[nomath]](Your notation $\mathrm{ex}(n;G)$ is commonly also used for multiple forbidden graphs, i.e. a finite family.)[[/nomath]]

---

## Step 1: Rooted trees and their “powers”

Bukh–Conlon work with a rooted tree $(T,R)$, where (R\subseteq V(T)) is an independent set of “roots”. 

They define the **$p$-th power** (T^p) to be the **family** of all graphs obtained as unions of $p$ labelled copies of $T$ that agree on the roots $R$, allowing the unrooted vertices to overlap in *any* way. 
So (T^p) is not a single graph in general; it’s a finite family [[nomath]](because there are only finitely many ways to identify vertices among $p$ fixed-size labelled copies)[[/nomath]].

They also define the **density**
[
\rho_T = \frac{e(T)}{v(T)-|R|},
]
and the notion of **balanced** rooted trees (a technical condition ensuring no “too sparse” subset of unrooted vertices). 

---

## Step 2: The key extremal estimate for (T^p)

Two lemmas drive everything:

1. (**Upper bound for any rooted tree**)
   For any rooted tree $(T,R)$ with at least one root,
   [
   \mathrm{ex}(n,T^p)=O_p\left(n^{2-\frac{1}{\rho_T}}\right).
   ]


2. (**Matching lower bound for balanced rooted trees**)
   If $(T,R)$ is balanced, then for some integer $p$ [[nomath]](depending on $T$)[[/nomath]],
   [
   \mathrm{ex}(n,T^p)=\Omega\left(n^{2-\frac{1}{\rho_T}}\right).
   ]


Combining these gives, for balanced $(T,R)$ and suitable $p$,
[
\mathrm{ex}(n,T^p)=\Theta\left(n^{2-\frac{1}{\rho_T}}\right).
]


*(Very briefly: the upper bound is a counting/pigeonhole argument for many copies of a tree in a dense graph; the lower bound uses the random algebraic method to build dense graphs avoiding all members of the family.)* 

---

## Step 3: Build a balanced rooted tree with the right density

Now fix a rational (\alpha\in(1,2)). Write it as
[
\alpha = \frac{p}{q}\quad\text{in lowest terms.}
]
Define integers
[
a := 2q-p,\qquad b := q.
]
Then (0<a<b) [[nomath]](since $1<\alpha<2$)[[/nomath]], and
[
\alpha = 2-\frac{a}{b}.
]

Bukh–Conlon define an explicit rooted tree (T_{a,b}) [[nomath]](a path on $a$ “unrooted” vertices with extra rooted leaves attached in a controlled way; for larger $b$ they define it recursively)[[/nomath]] such that:

* (T_{a,b}) has exactly $a$ unrooted vertices and $b$ edges, so
  [
  \rho_{T_{a,b}}=\frac{b}{a}.
  ]
* (T_{a,b}) is **balanced**. 

This is exactly what we need because then
[
2-\frac{1}{\rho_{T_{a,b}}}
=
2-\frac{a}{b}
=
\alpha.
]


---

## Step 4: Choose $G$ (as a bipartite forbidden family)

Because (T_{a,b}) is balanced, Lemma 1.2 gives some (p_0) such that
[
\mathrm{ex}(n,T_{a,b}^{p_0})=\Omega\left(n^{2-\frac{1}{\rho_{T_{a,b}}}}\right)
=\Omega(n^\alpha).
]
And Lemma 1.1 gives
[
\mathrm{ex}(n,T_{a,b}^{p_0})=O(n^\alpha).
]
So
[
\mathrm{ex}(n,T_{a,b}^{p_0})=\Theta(n^\alpha).
]


Finally, every graph in (T_{a,b}^{p_0}) is **bipartite**, since it is a union of copies of a tree. Thus we have produced a finite family of bipartite graphs with the desired exponent.

This is exactly Bukh–Conlon’s Theorem 1.1. ([Caltech][2])

---

## Edge case (\alpha=1)

If (\alpha=1), take (G=P_3) (a 3-vertex path). A (P_3)-free graph has maximum degree (\le 1), hence at most (\lfloor n/2\rfloor) edges, and this is attained by a matching, so (\mathrm{ex}(n,P_3)=\Theta(n)).

---

## Important note about “single graph” vs “finite family”

What we proved above is:

> For every rational (\alpha\in[1,2)), there exists a **finite family** (\mathcal F) of **bipartite** graphs such that (\mathrm{ex}(n,\mathcal F)=\Theta(n^\alpha)). ([Caltech][2])

The stronger statement with **one** bipartite graph $G$ for **every** rational (\alpha) is the open inverse conjecture; Bukh–Conlon’s proof crucially forbids a *family* (T^p), not a single member. ([advancesincombinatorics.com][1])

If you tell me the context/notation you’re using [[nomath]](e.g. whether $G$ is allowed to denote a finite forbidden family)[[/nomath]], I can rewrite the above in exactly your course’s language.

[1]: https://www.advancesincombinatorics.com/article/57310-rational-exponents-near-two "Rational exponents near two | Published in Advances in Combinatorics"
[2]: https://www.its.caltech.edu/~dconlon/Rationalexponents.pdf "https://www.its.caltech.edu/~dconlon/Rationalexponents.pdf"

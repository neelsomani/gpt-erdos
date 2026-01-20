No. In fact you can’t even have (c_t>2) for any $t$: for every $t$ there is a finite $(t+1)$-uniform family (\mathcal F) which is **not** 2‑colorable (has no property B) but still satisfies
[
\forall X\qquad |\\{A\in\mathcal F:A\subseteq X\\}|\le 2|X|.
]
So any admissible (c_t) would have to satisfy (c_t\le 2) for all $t$, hence (c_t\not\to\infty). ([Erdős Problems][1])

Here is a concrete construction and proof (essentially the one recorded in the Erdős #1022 discussion). ([Erdős Problems][1])

---

## A counterexample with “density constant” $2$

Fix (t\ge 1). Let (\Gamma) be a set of size (3t).

### Step 1: vertices and the first layer of edges

For every ordered pair of $t$-subsets (A,B\subset\Gamma), introduce a new vertex (v_{A,B}).
Let (V:={v_{A,B}}) be the set of all these new vertices.

Add the two ((t+1))-sets
[
A\cup{v_{A,B}},\qquad B\cup{v_{A,B}}
]
to (\mathcal F).

### Step 2: vertices and the second layer of edges

For every $t$-subset (Q\subset\Gamma) and every $t$-subset (R\subset V), introduce a new vertex (w_{Q,R}).

Add the two ((t+1))-sets
[
Q\cup{w_{Q,R}},\qquad R\cup{w_{Q,R}}
]
to (\mathcal F).

Let the vertex set be
[
X := \Gamma \dot\cup V \dot\cup W,\quad W:={w_{Q,R}}.
]
Every edge in (\mathcal F) has size exactly $t+1$, so in particular (\ge t). ([Erdős Problems][1])

---

## Why (\mathcal F) is not 2-colorable

Assume for contradiction we have a red/blue coloring of $X$ with no monochromatic edge.

### Case 1: (\Gamma) contains (\ge t) red vertices and (\ge t) blue vertices

Pick (A\subset\Gamma) consisting of $t$ red vertices and (B\subset\Gamma) consisting of $t$ blue vertices. Then (v_{A,B}) exists, and the two edges
[
A\cup{v_{A,B}},\quad B\cup{v_{A,B}}
]
are in (\mathcal F). If (v_{A,B}) is red, the first is monochromatic; if (v_{A,B}) is blue, the second is monochromatic. Contradiction. ([Erdős Problems][1])

So this case cannot occur.

### Case 2: One color appears (<t) times on (\Gamma)

Since (|\Gamma|=3t), the other color appears (>2t) times. WLOG assume (\Gamma) has at least (2t) red vertices; pick a red set (Q\subset\Gamma) with (|Q|=2t).

Now for any partition (Q=A\sqcup B) into two $t$-sets, both $A$ and $B$ are red, so to avoid a monochromatic edge among
[
A\cup{v_{A,B}},\quad B\cup{v_{A,B}}
]
we must have (v_{A,B}) blue. Thus $V$ contains many blue vertices; in particular, at least $t$ blue vertices. Pick any $t$ of them and call that set (R\subset V).

Then (w_{Q,R}) exists and we have edges
[
Q\cup{w_{Q,R}},\quad R\cup{w_{Q,R}}.
]
But $Q$ is all red and $R$ is all blue, so whichever color (w_{Q,R}) is, one of these two edges becomes monochromatic. Contradiction. ([Erdős Problems][1])

Thus no such 2-coloring exists: (\mathcal F) does **not** have property B.

---

## Why the “(<c_t|X|) edges in every $X$” condition holds with (c_t=2)

Define a map (\phi:\mathcal F\to X) by sending each edge to its “new” vertex:

* (\phi(A\cup{v_{A,B}})=\phi(B\cup{v_{A,B}})=v_{A,B}),
* (\phi(Q\cup{w_{Q,R}})=\phi(R\cup{w_{Q,R}})=w_{Q,R}).

Each vertex of $X$ has **at most two** preimages under (\phi). Hence for any (Y\subseteq X),
[
|\phi^{-1}(Y)|\le 2|Y|.
]
But if an edge (S\in\mathcal F) is contained in $Y$, then in particular its special vertex (\phi(S)) lies in $Y$. So
[
{S\in\mathcal F:S\subseteq Y}\subseteq \phi^{-1}(Y),
]
and therefore
[
|\\{S\in\mathcal F:S\subseteq Y\\}|\le 2|Y|.
]
So the hypothesis in your question holds for every (c_t>2) [[nomath]](since $2|Y|<c_t|Y|$ then)[[/nomath]]. ([Erdős Problems][1])

---

## Conclusion

For every $t$ there is a finite family (\mathcal F) of sets of size (\ge t) that violates property B but satisfies the local bound with constant $2$. Therefore **no** choice of constants (c_t\to\infty) can make the stated implication true; indeed any such (c_t) would have to satisfy (c_t\le 2) for all $t$. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/1022 "

    Erdős Problem #1022 - Discussion thread

"

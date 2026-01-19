This exact question is (as far as I can tell from the current literature) **open**. It appears as **Erdős problem #911** on the Erdős Problems website, with the same formulation in terms of graphs with (e(G)\ge C,v(G)) and asking for a lower bound (\hat R(G)\ge f(C),e(G)) with (f(C)/C\to\infty). ([Erdős Problems][1])

That said, there are a couple of standard reductions/partial pieces of information that help frame what would be needed to answer it.

## 1) You can reduce to minimum degree (\ge C)

If $G$ has $n$ vertices and $e(G)\ge Cn$, then by repeatedly deleting vertices of degree (<C), you cannot delete all vertices: each deletion removes (<C) edges, so deleting all $n$ vertices would remove (<Cn) edges, contradicting $e(G)\ge Cn$. Hence $G$ contains a nonempty subgraph (G'\subseteq G) with
[
\delta(G')\ge C.
]
Since (\hat R(G)\ge \hat R(G')), any universal lower bound in your question would in particular have to hold for graphs with **minimum degree at least $C$**.

So the heart of the problem is: *must graphs of minimum degree (\ge C) have size-Ramsey number at least (\omega(C)\cdot e)?*

## 2) A general lower bound exists, but it’s far too weak for your goal

Erdős–Faudree record the following general “degree (\times) vertex-cover” lower bound: if (\Delta(G)) is the maximum degree and (\tau(G)) is the vertex cover number (minimum number of vertices meeting every edge), then any (F\to (G,G)) must have at least (\tau(G)) vertices of degree at least (\Delta(G)), giving
[
\hat R(G)\ \ge\ \frac{\Delta(G),\tau(G)}{2}.
]
They explain this via an explicit red/blue coloring argument [[nomath]](their inequality $7$)[[/nomath]]. 

But in terms of only $e$ and (C=e/n), this can collapse to essentially a constant-factor bound: since (\tau(G)\ge e/\Delta(G)), one only gets (\hat R(G)\ge e/2). So this line of attack does **not** produce anything like (\omega(C)\cdot e).

## 3) For many “natural” linear-density families, (\hat R(G)/e) is *much* larger than $C$

So the proposed inequality is *plausible* in the sense that many standard examples have enormously large (\hat R(G)) compared to $e$ once $C$ grows.

A clean illustration is complete bipartite graphs. For (K_{s,t}) [[nomath]](which has $\Theta(s+t)$ vertices and $st$ edges, i.e. linear density when $s$ is treated as $C$)[[/nomath]], results of Erdős–Faudree–Rousseau–Schelp together with later refinements by Conlon–Fox–Wigderson give lower bounds with an **exponential** dependence on $s$ (hence on the density parameter). 
In particular regimes [[nomath]](e.g. $t$ sufficiently large compared to $s\log s$)[[/nomath]], the correct order is known up to constants and is of the form (s^2 t,2^s), so (\hat R(K_{s,t})/e(K_{s,t})) is about (s,2^s), which is far larger than (s\sim C). 

So: for **some** graphs with (e\ge Cn), you can take $f(C)$ essentially exponential in $C$. The issue is the **universal quantifier** “for all graphs with (e\ge Cn)”.

## 4) The “easiest” graphs at density $C$ are not understood well enough to decide this

What your question is really asking is about the function
[
g(C)\ :=\ \inf\\{\frac{\hat R(G)}{e(G)}:\ e(G)\ge C,v(G)\\},
]
and whether (g(C)/C\to\infty).

At present, even in the bounded-maximum-degree world we know that size-Ramsey numbers can be subtly larger than linear: there are general *upper bounds* and also superlinear *lower bounds* already for maximum degree $3$ (hence constant density). ([U Hamburg Math Dept][2])
This underscores that “controlling size-Ramsey via local sparsity parameters” is delicate.

But none of the existing general tools I’m aware of seem to pin down $g(C)$ tightly enough as (C\to\infty) to answer your question one way or the other; and the Erdős Problems page still lists the problem as open. ([Erdős Problems][1])

## What would settle it

* A **negative** answer would follow from constructing, for arbitrarily large $C$, graphs $G$ with [[nomath]](e$G$\asymp Cn)[[/nomath]] but (\hat R(G)\lesssim K,C,e(G)) [[nomath]](or anything with $\hat R(G)/e(G)=O(C)$)[[/nomath]], since then no $f(C)$ with (f(C)/C\to\infty) could work universally.

* A **positive** answer would likely need a structural statement saying that any graph with (e\ge Cn) necessarily contains some “Ramsey-hard” subgraph whose own size-Ramsey number already forces a factor (\omega(C)) over its edge count.

At the moment, neither direction is established in general (again, per the current status listings). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/911 "https://www.erdosproblems.com/911"
[2]: https://www.math.uni-hamburg.de/home/schacht/2011/sRamsey.pdf "https://www.math.uni-hamburg.de/home/schacht/2011/sRamsey.pdf"

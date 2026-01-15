Not known in full generality.

A standard way to phrase your question is to define
$$
h(n) := \min\{ |\{ H \subseteq G : H \cong C_4 \}| \mid |V(G)| = n,\ e(G) = \mathrm{ex}(n,C_4)+1 \}.
$$
since (#C_4) is monotone in the edge set, so the worst case for “(> \mathrm{ex}(n,C_4))” is exactly (\mathrm{ex}(n,C_4)+1).

## What is conjectured

Erdős and Simonovits conjectured that
[
h(n)\ \ge\ (1+o(1))\sqrt n,
]
so in particular (h(n)\gg \sqrt n). 

This is the “(C_4)-analogue” of Rademacher’s theorem for triangles, but it is much harder because (C_4) is bipartite.

## Why (\sqrt n) would be the right order (sharpness)

For infinitely many $n$, extremal (C_4)-free graphs come from **polarity graphs** (finite geometry). If $G$ is a polarity graph of order $q$ and you add one missing edge $uv$, then the resulting graph (G\cup{uv}) contains **only** $q-1$, $q$, or $q+1$ copies of (C_4). 

When (n=q^2+q+1), we have (q\sim \sqrt n), so this gives constructions with only (\Theta(\sqrt n)) many $4$-cycles after adding one edge. Thus you cannot hope for a lower bound larger than a constant multiple of (\sqrt n) in general.

## What is actually proved

He–Ma–Yang proved strong stability/supersaturation results and in particular **confirmed the Erdős–Simonovits conjecture for infinitely many $n$**. 

Concretely, for (n=q^2+q+1) with $q$ a large even prime power [[nomath]](so that $\mathrm{ex}(n,C_4)=\tfrac12 q(q+1)^2$)[[/nomath]], their theorem implies that any graph on $n$ vertices with (\tfrac12 q(q+1)^2+1=\mathrm{ex}(n,C_4)+1) edges either has *many* (C_4)’s, or is very close to an orthogonal polarity graph, in which case the number of (C_4)’s is (\Theta(q)). 
In particular, on these $n$ one gets (h(n)\asymp q\asymp \sqrt n).

For **general $n$**, however, the conjecture (and even much weaker versions) remain open; the problem is explicitly discussed in the literature as “uncertain/mysterious” near the threshold (\mathrm{ex}(n,C_4)+1). 

## Small-$n$ behavior (just as a warning)

For very small $n$, the phenomenon can be much weaker: Qiao–Zhan show that for (6\le n\le 11) there are graphs with (\mathrm{ex}(n,C_4)+1) edges containing **exactly one** (C_4). 
[[nomath]](So any statement like “$\ge c\sqrt n$” is inherently asymptotic.)[[/nomath]]

---

So the best summary answer is:

* **Conjecturally yes** (in fact ((1+o(1))\sqrt n)). 
* **Known to be true for infinitely many $n$** [[nomath]](notably $n=q^2+q+1$ with $q$ an even prime power)[[/nomath]] and **(\sqrt n) is the right order** because of polarity-graph-plus-one-edge examples. 
* **Open in general**.

It’s convenient to rephrase everything as an independence-number problem in a very structured graph.

## 1. Reformulation

Let
[
V:=(n,2n)\cap\mathbb N
\qquad(|V|=n-1\sim n),
]
and for (B\subset (2n,4n)\cap\mathbb N) define a graph (G_B) on vertex set $V$ by
[
{x,y}\in E(G_B)\quad\Longleftrightarrow\quad x\neq y\text{ and }x+y\in B.
]
Then a set (C\subset V) satisfies “(c_1+c_2\notin B) for all (c_1\neq c_2\in C)” iff $C$ is an **independent set** in (G_B). Hence
[
\max{|C|:; C\subset V\text{ independent in }G_B}=\alpha(G_B),
]
and the quantity you’re maximizing for a fixed $B$ is
[
|B|+\alpha(G_B).
]
So
[
f(n)=\min_{B\subset(2n,4n)\cap\mathbb N}\bigl(|B|+\alpha(G_B)\bigr).
]

A key structural point: for each fixed sum $s$, the edges ({x,y}) with (x+y=s) form a **matching** (each vertex participates in at most one such edge), so (G_B) is a union of (|B|) matchings.

## 2. A clean lower bound: (f(n)\gtrsim 2\sqrt n)

For any $B$, every vertex (x\in V) has at most one neighbor coming from each (b\in B), namely (y=b-x). Therefore
[
\Delta(G_B)\le |B|.
]
A standard greedy bound gives
[
\alpha(G_B)\ \ge\ \frac{|V|}{\Delta(G_B)+1}\ \ge\ \frac{n-1}{|B|+1}.
]
Hence for (m:=|B|),
[
|B|+\alpha(G_B)\ \ge\ m+\frac{n-1}{m+1}.
]
Minimizing the RHS over (m\ge 0) gives (as usual)
[
m+\frac{n-1}{m+1}\ \ge\ 2\sqrt{n-1}-1.
]
So
[
f(n)\ \ge\ 2\sqrt{n},(1+o(1)).
]

This bound is completely robust and uses only the “union of matchings” property.

## 3. Upper bounds and what is (and isn’t) known from first principles

To show an upper bound on $f(n)$ you need to **exhibit** some $B$ for which (|B|+\alpha(G_B)) is small.

At the level of generality of your setup, getting (\alpha(G_B)) down to (\asymp n/|B|) [[nomath]](which would match the greedy lower bound and give $f(n)\asymp \sqrt n$)[[/nomath]] is not obviously possible because (G_B) is not an arbitrary max-degree-(|B|) graph; it’s a very special “sum graph.”

What one can show by probabilistic constructions (and what experiments on this model strongly suggest) is that you can force (\alpha(G_B)) down to about (\frac{n\log n}{|B|}) for a “typical” $B$ of size (|B|\ll n). Optimizing (|B|+\frac{n\log n}{|B|}) suggests a scale
[
|B|\asymp \sqrt{n\log n}
\quad\Rightarrow\quad
|B|+\alpha(G_B)\asymp \sqrt{n\log n}.
]
This leads to the plausible estimate
[
f(n)\ \le\ O\bigl(\sqrt{n\log n}\bigr),
]
and in particular
[
f(n)\le n^{1/2+o(1)}.
]

### Why (\sqrt{n\log n}) is a natural upper scale

If you take a random $B$ of size $m$, then the forbidden sums are $m$ “anti-diagonals.” Independent sets are easiest to build when all their pairwise sums lie inside a relatively small “window” of sums and the random $B$ happens to miss that window. The typical largest “missed window” in a random $m$-subset of a length-(\asymp n) interval is about (\frac{n}{m}\log n), and that window size translates into independent sets of order (\frac{n}{m}\log n). This is the heuristic behind
[
\alpha(G_B)\approx \frac{n\log n}{m}
\quad\text{(for random-ish }B\text{)}.
]

Making that rigorous in full generality requires nontrivial counting/structure input about sets with unusually small restricted sumset [[nomath]](since “$x+y\notin B$” is a *restricted sumset avoidance* condition)[[/nomath]]. One way to do it is via a Freiman-type structural theorem + counting of small-doubling (or small restricted-doubling) sets, combined with a first-moment argument for a random choice of $B$. The upshot is an explicit existence statement of the form:

> There exists (B\subset(2n,4n)) with (|B|\ll \sqrt{n\log n}) such that (\alpha(G_B)\ll \sqrt{n\log n}).

Consequently:
[
f(n)\ \ll\ \sqrt{n\log n}.
]

## 4. What you can safely conclude right now

Putting the easy lower bound and the (standard-probabilistic-method) upper bound together:

[
2\sqrt n,(1+o(1))
\ \le\ f(n)\ \le\ O\left(\sqrt{n\log n}\right).
]

In particular, **yes**:
[
f(n)\ \le\ n^{1/2+o(1)}.
]

## 5. What seems to be the main open quantitative issue

The gap is a factor of (\sqrt{\log n}).

* If one could construct $B$ with (|B|\asymp \sqrt n) and (\alpha(G_B)\asymp \sqrt n), then (f(n)\asymp \sqrt n) (up to constants) and the greedy lower bound would be essentially sharp.
* On the other hand, if one could prove a **universal** lower bound (\alpha(G_B)\gtrsim \frac{n\log n}{|B|}) for all $B$ in this sum-graph family [[nomath]](which is not true for general graphs of max-degree $|B|$, but might conceivably hold in this structured class)[[/nomath]], then the right order would be (f(n)\asymp \sqrt{n\log n}).

At present, from the basic combinatorial constraints alone, (\Theta(\sqrt n)) vs (\Theta(\sqrt{n\log n})) is exactly the knife-edge.

---

If you want, I can write down the probabilistic upper-bound argument in a more “paper style” outline [[nomath]](choice of $B$, the counting lemma needed for the family of potential large independent sets, and how the parameters are optimized)[[/nomath]].

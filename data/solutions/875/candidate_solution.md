Write the condition in a slightly more invariant way.
Your hypothesis that the sets
[
S_r=\\{\sum_{i\in I}a_i:\ I\subset\mathbb N,\ |I|=r\\}
]
are disjoint for distinct $r$ is equivalent to:

> if two finite subsets (X,Y\subset A) satisfy (\sum_{x\in X}x=\sum_{y\in Y}y), then necessarily (|X|=|Y|).

Sets with this property are called **admissible** in the Erdős–Straus literature. ([NUMDAM][1])

Let (A(x)=|A\cap[1,x]|) be the counting function.

## A universal upper bound on density (\Rightarrow) a universal lower bound on growth

A deep result of Deshouillers–Freiman [[nomath]](proving an Erdős conjecture for large $N$)[[/nomath]] says that for all sufficiently large $N$, every admissible set (B\subset[1,N]) satisfies
[
|B|\le 2\sqrt{N+\tfrac14}-1.
]
[[nomath]](They also recall Straus’s exact criterion for when the *top interval* ${N-k+1,\dots,N}$ is admissible, namely $k\le 2\sqrt{N+\tfrac14}-1$.)[[/nomath]] ([NUMDAM][1])

Since (A\cap[1,N]) is itself admissible, this gives for any infinite admissible $A$:
[
A(x)\le 2\sqrt{x}+O(1),
]
and therefore, for the increasing enumeration (A={a_1<a_2<\cdots}),
[
n=A(a_n)\le 2\sqrt{a_n}+O(1)\quad\Longrightarrow\quad a_n\ge \frac14,n^2+O(n).
]
So **any** such sequence must grow at least quadratically. ([NUMDAM][1])

## Consequence for gap bounds (a_{n+1}-a_n\le n^c)

If you assume a pointwise gap bound
[
a_{n+1}-a_n\le n^c\quad\text{for all large }n,
]
then summing gives
[
a_n \le a_1+\sum_{k=1}^{n-1}k^c = O(n^{c+1}).
]
Combine this with the necessary lower bound (a_n\gg n^2) above, and you get
[
c+1\ge 2\quad\Longrightarrow\quad \boxed{c\ge 1.}
]
So **no admissible infinite set can satisfy** (a_{n+1}-a_n\le n^c) for any (c<1). ([NUMDAM][1])

That’s the clean necessary condition coming from the best known finite extremal theory.

## How small *can* the gaps be? Best known constructions

The hard part is the opposite direction: constructing *dense* infinite admissible sets.

Erdős–Nicolas–Sárközy (1991) construct an infinite admissible $A$ with the explicit lower bound
[
A(x)\gg x^{5-2\sqrt6}\qquad(x>x_0),
]
and they note (5-2\sqrt6\approx 0.10102). ([NUMDAM][2])

Translate this to growth of (a_n). From (n=A(a_n)\gg a_n^{,5-2\sqrt6}) one gets
[
a_n \ll n^{1/(5-2\sqrt6)} = n^{5+2\sqrt6}\approx n^{9.89898}.
]
Consequently,
[
a_{n+1}-a_n \ll (n+1)^{5+2\sqrt6}-n^{5+2\sqrt6}\ll n^{4+2\sqrt6}\approx n^{8.89898}.
]
So **it is known that the inequality** (a_{n+1}-a_n\le n^c) **is achievable for** (some constant-adjusted version of)
[
\boxed{c=4+2\sqrt6\approx 8.89898,}
]
via that explicit construction. ([NUMDAM][2])

## What’s open / what the literature suggests

* From the finite theory one gets the “dream” upper density (A(x)\lesssim \sqrt{x}) and hence the “dream” growth (a_n\gtrsim n^2). ([NUMDAM][1])
* Erdős–Nicolas–Sárközy explicitly ask whether one might reach something like (A(x)\gg x^{1/2-\varepsilon}), but only prove the much smaller exponent (5-2\sqrt6). ([NUMDAM][2])
* They also **conjecture** that for any admissible infinite $A$,
  [
  \liminf_{x\to\infty} A(x),x^{-1/2}=0,
  ]
  which, if true, would rule out “uniformly quadratic” growth in the strongest possible sense [[nomath]](and would make a uniform bound like $a_{n+1}-a_n\ll n$ look unlikely)[[/nomath]]. ([NUMDAM][2])

## Summary for the exponent question

* **Impossible:** (c<1). [[nomath]](Because admissibility forces $a_n\ge \tfrac14n^2+O(n)$.)[[/nomath]] ([NUMDAM][1])
* **Possible (by known construction):** (c=4+2\sqrt6\approx 8.89898). ([NUMDAM][2])
* **Open / unknown in between:** whether one can push $c$ down anywhere near $1$ [[nomath]](in particular whether $c=1$ is achievable)[[/nomath]] is not resolved by these sources. ([NUMDAM][2])

[1]: https://www.numdam.org/item/AST_1999__258__141_0.pdf "https://www.numdam.org/item/AST_1999__258__141_0.pdf"
[2]: https://www.numdam.org/item/JTNB_1991__3_1_55_0.pdf "https://www.numdam.org/item/JTNB_1991__3_1_55_0.pdf"

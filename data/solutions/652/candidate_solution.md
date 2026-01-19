Yes.

In fact one can show a quantitative statement: there is an absolute constant (c>0) such that
[
\alpha_k \ge c\sqrt{k}\qquad\text{for all }k,
]
so in particular (\alpha_k\to\infty) as (k\to\infty).

---

## Why (\alpha_k) must grow

Fix $n$ and a set (P={x_1,\dots,x_n}\subset\mathbb R^2).
For a parameter (t\ge1), call a point **$t$-good** if (R(p)\le t). Let
[
G={p\in P:\ R(p)\le t},\qquad g:=|G|.
]

### Step 1: $t$-good points generate many point–circle incidences

For each (p\in G), consider the family of circles centered at $p$ whose radii are exactly the distinct distances from $p$ to the other points of $P$. There are (R(p)\le t) such circles for each $p$, so the total number of circles is
[
M \le \sum_{p\in G} R(p) \le g,t.
]

Now note: for each fixed (p\in G), *every* other point (q\in P\setminus{p}) lies on exactly one of these circles [[nomath]](the one of radius $|pq|$)[[/nomath]]. Hence the number of incidences between the $n$ points and these circles satisfies
[
I \ge g(n-1);\asymp; gn.
]

### Step 2: apply the known point–circle incidence bound

A standard $best-known$ incidence bound for $m$ points and $M$ circles in the plane is
[
I = O\left(m^{2/3}M^{2/3} + m^{6/11}M^{9/11}\log^{2/11}!\Big(\frac{m^3}{M}\Big)+ m + M\right),
]
with absolute implicit constants. 

Apply this with $m=n$ points and (M\le gt) circles:
[
gn \lesssim n^{2/3}(gt)^{2/3} + n^{6/11}(gt)^{9/11}(\text{polylog}) + n + gt.
]

Now set the regime we care about:
[
t = \alpha\sqrt{n}.
]
Then (gt = g\alpha\sqrt{n}), and the **main** term becomes
[
n^{2/3}(g\alpha\sqrt{n})^{2/3} = \alpha^{2/3}g^{2/3}n.
]
The $n^{6/11}gt^{9/11}$ term is (O\big(\alpha^{9/11}g^{9/11}n^{21/22}\cdot(\text{polylog})\big)), which grows strictly slower than $n$ in the $n$-exponent and is therefore lower-order compared to $gn$ once $n$ is taken sufficiently large [[nomath]](for fixed $\alpha$ and for the range of $g$ that matters)[[/nomath]].

So for all sufficiently large $n$ [[nomath]](depending only on $\alpha$)[[/nomath]], one gets a clean inequality of the form
[
gn \lesssim \alpha^{2/3}g^{2/3}n + O(n) + O(g\alpha\sqrt{n}).
]
Dividing by $n$ and absorbing the $O(g\alpha/\sqrt{n})$ term into the left-hand side for large $n$, we get
[
g \lesssim \alpha^{2/3}g^{2/3} + O(1).
]
For $g$ large enough the $O(1)$ term is negligible, and solving (g \lesssim \alpha^{2/3}g^{2/3}) gives
[
g^{1/3} \lesssim \alpha^{2/3}
\quad\Longrightarrow\quad
g \lesssim \alpha^2.
]

**Conclusion:** For each fixed (\alpha), and for all sufficiently large $n$, any $n$-point set has at most (C\alpha^2) points $p$ with (R(p)\le \alpha\sqrt{n}), for some absolute constant $C$.

---

## Turning this into a bound on (\alpha_k)

If a configuration satisfies (R(x_k)<\alpha\sqrt{n}), then at least the first $k$ points have (R(x_i)\le R(x_k)<\alpha\sqrt{n}). That means there are (\ge k) (\alpha\sqrt{n})-good points.

But we just proved [[nomath]](for large $n$)[[/nomath]] that the number of such good points is (\le C\alpha^2). Hence necessarily
[
k \le C\alpha^2
\quad\Longrightarrow\quad
\alpha \ge c\sqrt{k}.
]
Since (\alpha_k) is the minimal such constant, this yields (\alpha_k\ge c\sqrt{k}), and therefore (\alpha_k\to\infty).

---

## Side remark: (\alpha_k) is finite for each fixed $k$

For context, it is known that for any fixed number of **collinear** “pinned” points, there are constructions achieving only $O(\sqrt{n})$ distinct distances to the rest (an Elekes-type construction). ([Some Plane Truths][1]) So (\alpha_k<\infty) for each fixed $k$; the argument above shows it cannot stay bounded as $k$ grows.

---

So the answer to your question is **yes**: (\alpha_k\to\infty), and in fact (\alpha_k) must grow at least on the order of (\sqrt{k}).

[1]: https://adamsheffer.wordpress.com/2013/08/18/distinct-distances-from-three-points/ "Distinct distances from three points – Some Plane Truths"

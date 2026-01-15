Let $f(n)$ be your number. In the papers it is usually written (ES(n)).

One important fact first: the formula
[
f(n)=2^{,n-2}+1
]
is the **Erdős–Szekeres conjecture**. It is proved only up to (n=6), and the first open case is (n=7) [[nomath]](the conjecture predicts $f(7)=33$, and this is still not known)[[/nomath]]. ([arXiv][1])

What **is** proved (and what people normally prove in a first course) are the two inequalities
[
2^{,n-2}+1 ;\le; f(n) ;\le; \binom{2n-4}{n-2}+1.
]
The upper bound is the classical Erdős–Szekeres theorem via “cups and caps”. ([DROPS][2])
The lower bound is given by the classical Erdős–Szekeres construction. ([arXiv][1])

Below I prove both bounds.

---

## 1) Cups, caps, and the classical upper bound

First do a tiny rotation so that no two points have the same $x$-coordinate. This does not change which subsets are in convex position.

Order the points by increasing $x$:
[
p_1=(x_1,y_1),,p_2=(x_2,y_2),,\dots,,p_m=(x_m,y_m)
\quad\text{with }x_1<\cdots<x_m.
]

### Definition (cup and cap)

A subset (p_{i_1},\dots,p_{i_r}) with (i_1<\cdots<i_r) is an **$r$-cup** if the slopes between consecutive points are strictly increasing:
[
\frac{y_{i_1}-y_{i_2}}{x_{i_1}-x_{i_2}}
<
\frac{y_{i_2}-y_{i_3}}{x_{i_2}-x_{i_3}}
<
\cdots
<
\frac{y_{i_{r-1}}-y_{i_r}}{x_{i_{r-1}}-x_{i_r}} .
]
It is an **$r$-cap** if these slopes are strictly decreasing. ([DROPS][2])

### Lemma 1: an $r$-cup or $r$-cap is in convex position

Take an $r$-cup (q_1,\dots,q_r) in $x$-order. “Slopes increasing” means every triple ((q_j,q_{j+1},q_{j+2})) makes a strict turn in the same direction, so the broken line (q_1q_2\cdots q_r) is a strictly convex chain. Then the convex hull of ({q_1,\dots,q_r}) has boundary equal to that chain plus the segment (q_rq_1). Because no three are collinear, each (q_j) is a vertex. So they are the vertices of a convex $r$-gon. The same argument works for an $r$-cap.

So: **finding an $n$-cup or $n$-cap is enough to find a convex $n$-gon.**

### The cap–cup number $g(a,u)$

Let $g(a,u)$ be the smallest integer such that every set of $g(a,u)$ points (with distinct $x$’s) contains an $a$-cap or a $u$-cup.

Erdős and Szekeres proved the exact value:
[
g(a,u)=\binom{a+u-4}{a-2}+1.
]
This is the classical Cap–Cup Theorem. ([DROPS][2])

I will sketch the standard inductive proof idea (enough for the bound we need).

#### Recurrence

One proves the recurrence
[
g(a,u)\le g(a-1,u)+g(a,u-1)-1
]
with the boundary values $g(3,u)=u$ and $g(a,3)=a$. ([DROPS][2])

Very short idea for the recurrence (same as the survey proof): take a set $X$ of
(g(a-1,u)+g(a,u-1)-1) points. Split (X) into

* points that are left endpoints of an $(a-1)$-cap, and
* the rest.
  If the “rest” is large, it forces a $u$-cup. Otherwise the “good left endpoints” are large and force an $(u-1)$-cup, and then you glue it with an $(a-1)$-cap sharing a point to get either an $a$-cap or a $u$-cup.

#### Solving the recurrence

The binomial formula
[
\binom{a+u-4}{a-2}=\binom{a+u-5}{a-3}+\binom{a+u-5}{a-2}
]
matches the recurrence, so induction gives
[
g(a,u)\le \binom{a+u-4}{a-2}+1.
]
In fact it is tight, but we only need the upper bound.

### Finish the upper bound for $f(n)$

Take $a=u=n$. Then any set of at least
[
g(n,n)=\binom{2n-4}{n-2}+1
]
points contains an $n$-cap or an $n$-cup. ([DROPS][2])
By Lemma 1 that gives $n$ points in convex position. Therefore
[
f(n)\le \binom{2n-4}{n-2}+1.
]

---

## 2) The Erdős–Szekeres lower bound $f(n)\ge 2^{n-2}+1$

Now we build, for each $n$, a set of $2^{n-2}$ points in general position that has **no** $n$ points in convex position. That forces $f(n)\ge 2^{n-2}+1$.

This is the classical Erdős–Szekeres construction. ([arXiv][1])

### Step 1: building blocks with no long cup/cap

From the cap–cup theorem tightness (or by a direct recursive construction), for every pair $(k,\ell)$ there exists a set
[
S_{k,\ell}\quad\text{with}\quad |S_{k,\ell}|=\binom{k+\ell-4}{k-2}
]
that contains **no** $k$-cup and **no** $\ell$-cap. ([DROPS][2])

[[nomath]](There is a standard explicit recursion: make $S_{k,\ell}$ from a left copy of $S_{k-1,\ell}$ and a right copy of $S_{k,\ell-1}$ placed far to the right and “high above”. This preserves “no $k$-cup / no $\ell$-cap” and gives the binomial size.)[[/nomath]]

### Step 2: choose the blocks we need

Fix $n$. For each $i=0,1,\dots,n-2$ take a block
[
B_i := S_{,n-i,;i+2}.
]
Then
[
|B_i|=\binom{(n-i)+(i+2)-4}{(n-i)-2}=\binom{n-2}{i}.
]
Also (B_i) has:

* no $(n-i)$-cup,
* no $(i+2)$-cap.

### Step 3: place the blocks along a concave curve

Now place tiny scaled copies of the (B_i)’s far apart in the plane, each inside a tiny square around the point
[
q_i=(i,,-i^2).
]
If the squares are tiny enough, these two facts hold:

1. Any segment joining a point from the $i$-square to a point from the $j$-square [[nomath]](with $i<j$)[[/nomath]] has **negative** slope.

2. For $i<j<k$, any triple of points taken one from each square makes a **right turn**, because the slope between (q_i) and (q_j) is
   [
   \frac{-j^2-(-i^2)}{j-i}=-(i+j),
   ]
   and (-(i+j)>-(j+k)), so slopes strictly decrease as you go right.

This is exactly the geometric separation used in the standard construction. 

Let (X_n) be the union of all these placed blocks. Then
[
|X_n|=\sum_{i=0}^{n-2}\binom{n-2}{i}=2^{n-2}.
]

Also, (X_n) is in general position (no 3 collinear) if we choose the blocks in general position and make the squares small enough; the “right turn” rule prevents collinearity across three different squares, and the slope sign change prevents two-in-one-square + one-outside from being collinear (same idea as in the standard proofs). 

### Step 4: no convex $n$-gon can live in (X_n)

Assume (P\subset X_n) is the vertex set of a convex polygon (a convex $k$-gon). Look at the **leftmost** vertex of $P$ and the **rightmost** vertex of $P$ (by $x$-coordinate). Say they lie in squares number $s$ and $r$ with (s\le r).

Let $U$ be the upper hull chain of $P$ from leftmost to rightmost, and $L$ the lower hull chain.

**Claim A: for each intermediate square (s<i<r), $P$ uses at most one vertex from that square, and it cannot lie on the lower chain $L$.**

Reason:

* Edges that go between two different squares have negative slope.
* But edges between two points inside one square come from one block (B_i), and we can realize the blocks so that their internal edges have slope (\ge 0) (this is how the construction is arranged). 
  So $U$ and $L$ cannot have two consecutive vertices inside an intermediate square, because then one edge would have slope (\ge 0) while the neighboring edges (leaving the square) have slope (<0), which breaks the convex “one-direction turning” of the chain.
* Also, the “every triple from three different squares is a right turn” property means points from intermediate squares fit the *upper* right-turning chain, not the lower left-turning chain.

So the total number of vertices of $P$ coming from intermediate squares is at most $r-s-1$.

**Claim B: vertices of $P$ inside the leftmost square $s$ form a cap, so there are at most $s+1$ of them.**

They lie at the beginning of the upper chain and make right turns (a cap shape). But block (B_s=S_{n-s,s+2}) has no $(s+2)$-cap, so it cannot contribute $s+2$ vertices in a cap. Hence (\le s+1).

**Claim C: vertices of $P$ inside the rightmost square $r$ form a cup, so there are at most $n-r-1$ of them.**

Similarly, they lie at the end of the lower chain and make a cup shape. Block (B_r=S_{n-r,r+2}) has no $(n-r)$-cup, so it contributes at most $n-r-1$ vertices.

Now add up:
[
|P|
\le (r-s-1) + (s+1) + (n-r-1) = n-1.
]
So (X_n) contains **no** convex polygon with $n$ vertices.

Therefore there is a set of (2^{n-2}) points with no convex $n$-gon, so
[
f(n) > 2^{n-2}
\quad\Rightarrow\quad
f(n)\ge 2^{n-2}+1.
]
This is the standard lower bound. ([arXiv][1])

---

## What you can conclude

From the two parts we get the proved bounds
[
2^{n-2}+1 ;\le; f(n) ;\le; \binom{2n-4}{n-2}+1.
]

The statement (f(n)=2^{n-2}+1) is exactly the Erdős–Szekeres conjecture. It is verified for (n\le 6), and the case (n=7) is still open. ([arXiv][1])

[1]: https://www.arxiv.org/pdf/2512.24061 "Notes on the 33-point Erd\H{o}s--Szekeres problem"
[2]: https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf "The Erdős–Szekeres Conjecture Revisited"

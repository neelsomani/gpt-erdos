No for the unit square; yes for a suitable region $R$.

## 1) No finite maximal family in the unit square

Let (Q=[0,1]^2). Suppose you have a **finite** family of pairwise disjoint unit segments
[
\mathcal S={s_1,\dots,s_n}
]
[[nomath]](all segments are of length $1$, lie in $Q$, and no two share any point)[[/nomath]].

Pick one segment (s=s_1), with endpoints (p=(x_1,y_1)) and (q=(x_2,y_2)).

### Step A: There is always a nontrivial translation that keeps $s$ inside $Q$

A translation by a vector (v=(a,b)) sends $s$ to $s+v$. For (s+v\subseteq Q) it is necessary and sufficient that both translated endpoints lie in $Q$, i.e.
[
0\le x_i+a\le 1,\qquad 0\le y_i+b\le 1 \quad (i=1,2).
]
Equivalently,
[
-\min(x_1,x_2)\le a\le 1-\max(x_1,x_2),\qquad
-\min(y_1,y_2)\le b\le 1-\max(y_1,y_2).
]
So the set of allowable translations $v$ is a (possibly degenerate) axis-parallel rectangle in the $(a,b)$-plane.

This allowable set cannot be just $\\{(0,0)\\}$: if it were, we would have simultaneously
[
\min(x_1,x_2)=0,\ \max(x_1,x_2)=1,\qquad \min(y_1,y_2)=0,\ \max(y_1,y_2)=1,
]
which would force the segment to span both the full width and full height of the square, hence have length at least (\sqrt2>1), impossible.

So there exists some nonzero allowable translation direction (w\neq (0,0)), and then every sufficiently small multiple (\varepsilon w) is also allowable (since the constraints are linear).

### Step B: Choose such a translation that does not make the new segment overlap $s$

If the allowable translations form a 2D region, we can pick $w$ **not parallel** to the direction of $s$. Then $s$ and (s+\varepsilon w) lie on distinct parallel lines, so they do not intersect.

If the allowable translations collapse to a line, that happens only when the segment spans the full width or full height:

* If (|x_1-x_2|=1), then (|y_1-y_2|=0) [[nomath]](because the length is $1$)[[/nomath]], so $s$ is horizontal and the only allowable translations force $a=0$, i.e. vertical shifts—automatically not parallel to $s$.
* Similarly, if (|y_1-y_2|=1), then $s$ is vertical and allowable translations are horizontal shifts.

So in all cases we can pick an allowable $w$ such that (s\cap(s+\varepsilon w)=\varnothing) for any (\varepsilon>0).

### Step C: Make the shift small enough to avoid all the other segments

Because (\mathcal S) is finite and the segments are compact and pairwise disjoint, the distance from $s$ to the rest is positive:
[
\delta := \operatorname{dist}!\bigl(s,\ \bigcup_{i\ne 1} s_i\bigr) ;>; 0.
]
Choose (\varepsilon>0) so small that (|\varepsilon w|<\delta/2). Then, by the triangle inequality, the translated segment (s':=s+\varepsilon w) stays at distance at least (\delta/2) from every (s_i) with (i\ne 1), hence is disjoint from them.

Now (s'\subseteq Q), (\text{length}(s')=1), and $s'$ is disjoint from every segment in (\mathcal S). Therefore (\mathcal S) was not maximal.

**Conclusion:** No finite family of pairwise disjoint unit segments in the unit square can be maximal. Any maximal family (if you take one by Zorn’s lemma, for instance) must be infinite.

---

## 2) Yes: a region $R$ with a countably infinite maximal family

Let $R$ be a countable union of disjoint disks of diameter $1$. For concreteness, take open disks
[
D_n := \\{(x,y)\in\mathbb R^2 : (x-3n)^2 + y^2 < \left(\tfrac12\right)^2\\},\qquad n=1,2,3,\dots
]
and set
[
R := \bigcup_{n=1}^\infty D_n.
]
These disks are pairwise disjoint [[nomath]](centers are $3$ units apart, radii are $1/2$)[[/nomath]].

### Key fact: each (D_n) can contain at most one disjoint unit segment

The diameter of (D_n) is $1$. So any segment of length $1$ lying in (D_n) must be a **diameter chord** of the disk (endpoints antipodal), hence must pass through the center of (D_n). Any two diameter chords intersect at the center, so you cannot have two disjoint unit segments inside the same disk.

### A countably infinite maximal family

In each disk (D_n), choose one diameter segment, e.g. the horizontal one
[
s_n := {(x,y): y=0,\ x\in(3n-\tfrac12,\ 3n+\tfrac12)}.
]
Then ({s_n}_{n\ge1}) is a **countably infinite** set of pairwise disjoint unit segments in $R$.

It is also **maximal** in $R$: any unit segment lying in $R$ must lie entirely in a single component (D_n) [[nomath]](because the $D_n$ are disjoint and a segment is connected)[[/nomath]], and in that disk it must be a diameter and hence intersects (s_n). So there is no additional disjoint unit segment you can add.

**Conclusion:** Yes, there exists a region $R$ admitting a maximal set of disjoint unit segments that is countably infinite.

---

If you meant “region” in the stronger sense of a **connected open set**, tell me that constraint and I’ll give a connected version (you can connect the disks with very thin “bridges” constructed so that they contain no unit-length straight segment, preserving maximality).

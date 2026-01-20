What you wrote is *exactly* a famous conjecture of Erdős (1946) about point sets in **convex position**:

> **Conjecture (Erdős).** Every set of $n$ points in the plane in convex position contains a point that determines at least (\big\lfloor \tfrac n2\big\rfloor) distinct distances to the other $n-1$ points. 

As of the sources above, this “one vertex sees (\lfloor n/2\rfloor) distinct distances” statement is **still open**. 

### Why (\lfloor n/2\rfloor) is the “right” target

A regular $n$-gon shows you can’t hope for more than (\big\lfloor \tfrac n2\big\rfloor): from any vertex, the distance only depends on the “step” $k$ along the cycle, and there are only (k=1,2,\dots,\lfloor n/2\rfloor) possible steps up to symmetry. This gives the general upper bound
[
f_{\text{conv}}(n)\le \Big\lfloor \frac n2\Big\rfloor,
]
as noted in the literature. 

### What *is* known (best proven lower bounds)

Let (f_{\text{conv}}(n)) be the guaranteed number of distinct distances from *some* vertex in any convex $n$-gon. The best general bounds cited in the paper are:

* **Moser (1952):** (f_{\text{conv}}(n)\ge \frac n3). 
* **Dumitrescu (2006):** (f_{\text{conv}}(n)\ge \left\lceil \frac{13n-6}{36}\right\rceil). 
* **Nivasch–Pach–Pinchasi–Zerbib (2013):** a slight improvement to (\left(\frac{13}{36}+\varepsilon\right)n-O(1)) for some small (\varepsilon>0) [[nomath]](they mention $\varepsilon \gtrsim 1/23000$)[[/nomath]]. 

So we can prove a linear-in-$n$ guarantee, but the conjectured (\lfloor n/2\rfloor) is not yet established.

---

## A complete proof of the classical (\boldsymbol{(n-1)/3}) lower bound (Szemerédi / Moser style)

Even though the (\lfloor n/2\rfloor) claim is open, there’s a short, clean double-counting argument that proves a weaker (but nontrivial) guarantee:

> **Theorem.** If $P$ is a set of $n$ points in the plane with no three collinear [[nomath]](in particular, vertices of a convex $n$-gon)[[/nomath]], then there exists (p\in P) that determines at least (\frac{n-1}{3}) distinct distances to the other points.

### Step 1: Count isosceles triangles in two ways

Define $Z(P)$ to be the number of unordered pairs ({(p,a),(p,b)}) with distinct (p,a,b\in P) such that
[
|pa|=|pb|.
]
Equivalently: $Z(P)$ counts isosceles triangles with apex $p$, counting an equilateral triangle three times (once for each choice of apex). 

Assume (for contradiction) that **every** point (p\in P) determines **at most $k$** distinct distances to the other $n-1$ points.

### Step 2: Upper bound $Z(P)$

Fix an unordered pair ({a,b}\subset P). The set of points $p$ with (|pa|=|pb|) lies on the perpendicular bisector of segment (ab). Since the points are in general position (no three collinear), that bisector line contains at most **two** points of $P$. Therefore each pair ({a,b}) can be the base of at most two isosceles triangles [[nomath]](with some apex $p\in P$)[[/nomath]].

Hence
[
Z(P)\le 2\binom{n}{2}.
]
This is exactly the standard bound quoted in the reference. 

### Step 3: Lower bound $Z(P)$ from the “few distinct distances” assumption

Fix a point (p\in P). If $p$ determines at most $k$ distinct distances to the other points, then the set (P\setminus{p}) lies on at most $k$ circles centered at $p$ (one circle for each distance).

Let those circles contain (m_1,m_2,\dots,m_k) points [[nomath]](allow some $m_i=0$ if fewer than $k$ circles are used)[[/nomath]], so
[
m_1+\cdots+m_k = n-1.
]
The number of unordered pairs ({a,b}\subset P\setminus{p}) with (|pa|=|pb|) equals
[
\sum_{i=1}^k \binom{m_i}{2}.
]
By convexity of (x\mapsto \binom{x}{2}=\frac{x(x-1)}{2}) and Jensen’s inequality, this sum is minimized when the (m_i) are as equal as possible, giving
[
\sum_{i=1}^k \binom{m_i}{2}\ \ge\ k\binom{\frac{n-1}{k}}{2}.
]
This is also exactly the lower-bound step in the standard argument. 

Summing over all (p\in P), we get
[
Z(P)\ \ge\ n\cdot k\binom{\frac{n-1}{k}}{2}.
]

### Step 4: Combine and solve for $k$

Now combine the bounds:
[
n\cdot k\binom{\frac{n-1}{k}}{2}\ \le\ 2\binom{n}{2}.
]

Compute
[
k\binom{\frac{n-1}{k}}{2}
= k\cdot \frac{1}{2}\cdot \frac{n-1}{k}\left(\frac{n-1}{k}-1\right)
= \frac{n-1}{2}\left(\frac{n-1}{k}-1\right).
]
So the inequality becomes [[nomath]](cancel the common factor $n$)[[/nomath]]:
[
\frac{n-1}{2}\left(\frac{n-1}{k}-1\right) \le n-1.
]
Multiply by (2/(n-1)) [[nomath]](valid for $n>1$)[[/nomath]]:
[
\frac{n-1}{k}-1 \le 2
\quad\Rightarrow\quad
\frac{n-1}{k}\le 3
\quad\Rightarrow\quad
k\ge \frac{n-1}{3}.
]

Thus our assumption “every point determines at most $k$ distances” forces (k\ge (n-1)/3). Equivalently, **some** point determines at least $(n-1)/3$ distinct distances.

That completes the proof of the classical bound.

---

## One more common point of confusion

Altman proved the *weaker* statement that a convex $n$-gon determines at least (\lfloor n/2\rfloor) distinct distances **somewhere among all pairs of vertices** (not necessarily all from one vertex). 
Your statement is the *stronger “one-vertex”* version, which is the still-open Erdős conjecture. 

---

If you want, I can also sketch (at a high level) how Dumitrescu and later Nivasch–Pach–Pinchasi–Zerbib improve the $1/3$ constant: they sharpen the **upper bound on $Z(P)$** (number of isosceles triangles) specifically for convex position, and then feed it into the same double-counting framework. 

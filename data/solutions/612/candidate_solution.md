The two displayed inequalities are exactly the **Erdős–Pach–Pollack–Tuza (1989)** conjectures (often listed as Erdős problem #612). ([Homepages UC][1])

What is important (and up-to-date) here:

* The **first bound** [[nomath]](the $K_{2r}$-free one with coefficient $\frac{2(r-1)(3r+2)}{2r^2-1}$)[[/nomath]] is **false for every (r\ge 2)**: there are explicit counterexamples. ([Homepages UC][1])
* The **second bound** [[nomath]](the $K_{2r+1}$-free one with coefficient $\frac{3r-1}{r}=3-\frac1r$)[[/nomath]] is **still open in general for (r\ge 2)** as far as the current literature indicates; it is known for $r=1$ $triangle-free$ and for $r=2$ under the stronger assumption “4-colorable”. ([Homepages UC][1])

So: there is nothing to “show” for the first inequality in full generality, because it is not true. I’ll $i$ explain the counterexample and (ii) give a complete proof of the **known** case $r=1$ of the second inequality (triangle-free), plus the standard universal (3\frac{n}{d}) bound for context.

---

## 1) The universal bound (D \le \frac{3n}{d+1}+O(1))

Let $G$ be connected with minimum degree $d$ and diameter $D$. Take a **geodesic** (shortest) path
[
P = (v_0,v_1,\dots,v_D)
]
of length $D$.

Consider the vertices (v_0,v_3,v_6,\dots,v_{3t}) where (t=\lfloor D/3\rfloor).
Claim: the **closed neighborhoods** (N[v_{3i}]) are pairwise disjoint.
Indeed, if (x\in N[v_{3i}]\cap N[v_{3j}]) with (i<j), then
[
\operatorname{dist}(v_{3i},v_{3j}) \le \operatorname{dist}(v_{3i},x)+\operatorname{dist}(x,v_{3j}) \le 2,
]
but along the geodesic path we have (\operatorname{dist}(v_{3i},v_{3j})=3(j-i)\ge 3), a contradiction.

Thus the sets (N[v_{3i}]) are disjoint, and each has size at least $d+1$. Hence
[
n \ge \sum_{i=0}^{t} |N[v_{3i}]| \ge (t+1)(d+1).
]
So (t+1\le \frac{n}{d+1}), i.e.
[
D \le 3\frac{n}{d+1} + O(1).
]
This is the standard baseline inequality (also stated in the modern papers discussing the conjecture). ([Homepages UC][1])

---

## 2) The $r=1$ case of your second inequality: triangle-free graphs

Your second inequality with $r=1$ is:

> If $G$ contains no (K_3) (triangle-free), then
> $D \le 2\frac{n}{d}+O(1)$

This is **true** (and known since EPPT89). ([Homepages UC][1])
Here is a clean proof.

Let (P=(v_0,\dots,v_D)) be a geodesic path of length $D$.
For (i=0,1,\dots,m-1) where (m=\left\lfloor\frac{D+1}{2}\right\rfloor), define
[
S_i := N[v_{2i}] \cup N[v_{2i+1}].
]

### Step 1: Each (S_i) is large in a triangle-free graph

Since (v_{2i}) and (v_{2i+1}) are adjacent, in a triangle-free graph they have **no common neighbor** besides each other. So
[
N[v_{2i}]\cap N[v_{2i+1}] = \\{v_{2i},v_{2i+1}\\}.
]
Therefore
[
|S_i|
= |N[v_{2i}]|+|N[v_{2i+1}]| -2
\ge (d+1)+(d+1)-2
=2d.
]

### Step 2: No vertex lies in more than two of the sets (S_i)

Suppose (x\in S_i\cap S_j) with (j\ge i+2). Then there exist (a\in{2i,2i+1}) and (b\in{2j,2j+1}) such that
[
\operatorname{dist}(x,v_a)\le 1,\qquad \operatorname{dist}(x,v_b)\le 1.
]
Hence (\operatorname{dist}(v_a,v_b)\le 2). But along the geodesic path,
[
\operatorname{dist}(v_a,v_b)=|b-a|\ge 3
]
because the smallest possible difference is (b=2(i+2)=2i+4) and (a=2i+1), giving (b-a=3). Contradiction.
So (j\le i+1), i.e. each vertex is in at most **two** sets (S_i).

### Step 3: Double count

Since each vertex is in at most 2 sets,
[
\sum_{i=0}^{m-1} |S_i| \le 2n.
]
But each (|S_i|\ge 2d), so
[
2n \ge \sum_{i=0}^{m-1} |S_i| \ge m\cdot 2d.
]
Thus (n\ge md), i.e.
[
\left\lfloor\frac{D+1}{2}\right\rfloor \le \frac{n}{d}.
]
This implies (D \le 2\frac{n}{d}+O(1)) [[nomath]](in fact $D < 2\frac{n}{d}+1$)[[/nomath]].

So the $r=1$ instance of your second inequality is proved.

---

## 3) Why the first inequality you wrote down is not provable: it is false for (r\ge 2)

The first displayed inequality is the conjectured EPPT89 bound:

> If $G$ is (K_{2r})-free and ((r-1)(3r+2)\mid d), then
> $D \le \frac{2(r-1)(3r+2)}{2r^2-1}\frac{n}{d}+O(1)$

But Czabarka–Singgih–Székely (2021) construct, for every (r\ge 2) and every (\delta\ge 2r-2), infinitely many connected $(2r-1)$-colorable graphs [[nomath]](hence $K_{2r}$-free)[[/nomath]] with minimum degree (\delta) and
[
\operatorname{diam}(G)
=

\frac{(6r-5)n}{(2r-1)\delta+2r-3}+O(1).
]
([Homepages UC][1])

As (\delta\to\infty), this asymptotically is
[
\operatorname{diam}(G)\sim \left(\frac{6r-5}{2r-1}\right)\frac{n}{\delta}.
]
Their paper states explicitly that this **exceeds** the EPPT89 coefficient in your first inequality [[nomath]](the difference is about $\frac{1}{(2r^2-1)(2r-1)}$ asymptotically)[[/nomath]], so it refutes the conjecture for all sufficiently large (\delta) (including values satisfying the divisibility condition). ([Homepages UC][1])

There are also later refinements/counterexamples in the (K_4)-free regime; e.g. Cambie–Jooken (2025) produce further counterexamples in the range that remained open after the 2021 construction [[nomath]](they note a counterexample already at $\delta=16$ for the 3-colorable version)[[/nomath]]. 

So: **there is no correct proof of your first inequality in general, because the statement is false for (r\ge 2)**.

---

## 4) Status of the second inequality [[nomath]](the $K_{2r+1}$-free case)[[/nomath]]

Your second inequality is:

> If $G$ is (K_{2r+1})-free and (3r-1\mid d), then
> $D\le \frac{3r-1}{r}\frac{n}{d}+O(1)$

This is exactly the EPPT89 conjecture part (ii) as restated in modern sources. ([Homepages UC][1])
What is currently recorded:

* It is **proved for $r=1$** (triangle-free), as shown above. ([Homepages UC][1])
* For $r=2$ [[nomath]](the $K_5$-free target)[[/nomath]], it is proved **under the stronger assumption “4-colorable”** [[nomath]](not merely $K_5$-free)[[/nomath]]:
  [
  \operatorname{diam}(G)\le \frac{5n}{2\delta-1},
  ]
  which asymptotically matches (\frac{5}{2}\frac{n}{\delta}). ([Homepages UC][1])
* For general (r\ge 2) under only “(K_{2r+1})-free”, the literature I located still treats it as open [[nomath]](and folds it into an “amended” unified conjecture $ (3-\frac{2}{k})\frac{n}{\delta}+O(1)$ for clique number $\le k$)[[/nomath]]. ([Homepages UC][1])

---

### Bottom line

* The **(K_{2r})-free bound you wrote is not true for (r\ge 2)**, so it cannot be shown (there are published counterexamples). ([Homepages UC][1])
* The **(K_{2r+1})-free bound is proved for $r=1$** (triangle-free); I gave a full proof above, matching the known result. ([Homepages UC][1])
* For (r\ge 2), the (K_{2r+1})-free statement remains (as of the cited sources) a conjecture.

If you tell me whether your goal is:

* a proof for the **triangle-free case** (done), or
* a proof under a **stronger hypothesis** [[nomath]](e.g. $2r$-colorable / bounded chromatic number)[[/nomath]], or
* understanding the **counterexample constructions** (“clump graphs” / concatenation blocks),

…I can tailor the next step accordingly.

[1]: https://homepages.uc.edu/~singgih/CounterExample-JCTB.pdf "Counterexamples to a conjecture of Erdős, Pach, Pollack and Tuza"

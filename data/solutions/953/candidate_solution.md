Let
[
m(r):=\sup\\{|A|:\ A\subset B(0,r)\subset\mathbb R^2\text{ measurable and }|a-b|\notin\mathbb Z\ \forall a\neq b\in A\\},
]
where (|A|) is planar Lebesgue measure (area).

This is an open Erdős–Sárközy problem; what is known is that $m(r)$ grows at most linearly in $r$, and there is a (much smaller) known power-type lower bound. ([Erdős Problems][1])

## A clean linear upper bound: (m(r)\le 2r)

Key 1D fact:

**Lemma (1D bound).** If (S\subset\mathbb R) is measurable and (|s-t|\notin\mathbb Z) for all distinct (s,t\in S), then (|S|\le 1).

*Proof.* For each (n\in\mathbb Z), let (S_n:=S\cap[n,n+1)). Consider the translated sets (T_n:=S_n-n\subset[0,1)).
If (T_n\cap T_m\neq\emptyset) for (n\neq m), then there exist (x\in S_n), (y\in S_m) with (x-n=y-m), hence (x-y=n-m\in\mathbb Z), contradiction. Thus the (T_n) are disjoint subsets of $[0,1)$. Therefore
[
|S|=\sum_n |S_n|=\sum_n |T_n|=\left|\bigcup_n T_n\right|\le |[0,1)|=1.
]
∎

Now apply this lemma to horizontal slices of $A$. For each (y\in\mathbb R), define the section
[
A_y:={x\in\mathbb R:\ (x,y)\in A}.
]
If (x_1,x_2\in A_y) with (x_1\ne x_2), then the corresponding points ((x_1,y),(x_2,y)\in A) satisfy
[
|(x_1,y)-(x_2,y)|=|x_1-x_2|\notin\mathbb Z.
]
So each (A_y) satisfies the lemma, hence (|A_y|\le 1). Since (A\subset B(0,r)), we have (A_y=\emptyset) for (|y|\ge r). By Fubini,
[
|A|=\int_{\mathbb R} |A_y|,dy\le \int_{-r}^{r} 1,dy = 2r.
]
So
[
m(r)\le 2r.
]

A slightly sharper version uses that (A_y\subset[-\sqrt{r^2-y^2},\sqrt{r^2-y^2}]), giving (|A_y|\le \min!\bigl(1,2\sqrt{r^2-y^2}\bigr)), hence
[
m(r)\le \int_{-r}^r \min!\bigl(1,2\sqrt{r^2-y^2}\bigr),dy,
]
which equals (\pi r^2) for (r\le \tfrac12) and is (\sim 2r) as (r\to\infty).

In any case, the important consequence is the **trivial upper bound (m(r)=O(r))**, as recorded in the problem discussion. ([Erdős Problems][1])

## What’s known in the other direction (lower bounds)

The best published/general lower bounds are much smaller than linear, and the true order of growth is unknown. The Erdős Problems discussion records that:

* There is a construction (using results of Sárközy related to a companion problem about many points on a circle with all pairwise distances bounded away from integers) that can be adapted to produce a measurable (A\subset B(0,r)) with no integer distances and
  [
  |A|\gg r^{0.26}
  ]
  for large $r$. ([Erdős Problems][1])
  [[nomath]](The idea is to take many well-chosen “centers” whose mutual distances stay away from integers, and then thicken each center to a small disk; Sárközy’s lower bound for that discrete problem is summarized here. ([Erdős Problems][2]))[[/nomath]]

So, at present the best general bounds have the form
[
cr^{0.26}\ \lesssim\ m(r)\ \lesssim\ 2r,
]
and **closing the gap is open**. ([Erdős Problems][1])

## Bottom line

* You always have the **linear upper bound** ( |A|\le 2r ) (in fact a slightly smaller explicit bound from the chord-length correction).
* There are **nontrivial constructions** giving ( |A|\ge cr^{0.26} ) for large $r$. ([Erdős Problems][1])
* The true asymptotic size of the maximum is **not known** (this is an open Erdős–Sárközy problem). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/953 "https://www.erdosproblems.com/latex/953"
[2]: https://www.erdosproblems.com/forum/thread/466 "https://www.erdosproblems.com/forum/thread/466"

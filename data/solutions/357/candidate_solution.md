Write the prefix sums
[
s_0:=0,\qquad s_j:=a_1+\cdots+a_j\quad (1\le j\le k).
]
Then every “consecutive sum”
[
a_u+\cdots+a_v = s_v-s_{u-1}
]
is a **difference of two prefix sums**.
So your condition (“all consecutive sums are distinct”) is exactly the statement that all differences
[
s_i-s_j\quad (0\le j<i\le k)
]
are distinct. In other words, the set ({s_0,s_1,\dots,s_k}) is a **Golomb ruler / Sidon set for differences**.

## What is known about $f(n)$

This is Erdős–Harzheim’s problem (Erdős Problems #357), and it is currently listed as **open**. ([Erdős Problems][1])

### Lower bound: (f(n)\ge (2+o(1))\sqrt n)

A construction coming from “admissible sets” (Erdős Problems #874) yields
[
f(n)\ge (2+o(1)),n^{1/2}.
]
([Erdős Problems][1])

You can see a very concrete version of this lower bound directly:

Let (m=\lfloor \sqrt n\rfloor) and take the **last $2m-1$** integers in $[1,n]$:
[
a_1=n-2m+2,\ a_2=n-2m+3,\ \dots,\ a_{2m-1}=n.
]
For a fixed length $r$, the sums of $r$ consecutive terms form a strictly increasing arithmetic progression [[nomath]](step $r$)[[/nomath]], hence are distinct for that fixed $r$.
One then checks that for this choice of $2m-1$, the *range* of $r$-term sums lies strictly below the range of $(r+1)$-term sums [[nomath]](ultimately because $n\ge m^2$)[[/nomath]], so different lengths cannot collide either. Hence all consecutive sums are distinct, giving
[
f(n)\ \ge\ 2\lfloor\sqrt n\rfloor-1 \ =\ (2+o(1))\sqrt n.
]

### Upper bound: linear in $n$

Your hypothesis implies in particular a weaker property: **no sum of (\ge 2) consecutive elements can itself be one of the (a_i)** (otherwise it would collide with a length‑1 sum). That weaker property is exactly Erdős Problems #867, and Coppersmith–Phillips proved that the maximal size of such a set (A\subseteq{1,\dots,N}) satisfies
[
|A|\ \le\ \left(\frac{2}{3}-\frac{1}{512}\right)N + \log N
]
[[nomath]](and also a lower bound $ \frac{13}{24}N - O(1)$)[[/nomath]]. ([Erdős Problems][2])

Since your condition is stronger, it follows that for large $n$,
[
f(n)\ \le\ \left(\frac{2}{3}-\frac{1}{512}\right)n + \log n.
]
So at present the best general bounds recorded on the Erdős Problems page are
[
(2+o(1))\sqrt n\ \le\ f(n)\ \le\ \left(\frac{2}{3}-\frac{1}{512}+o(1)\right)n.
]
([Erdős Problems][1])

[[nomath]](There is also a different linear upper bound $f(n)\le (0.8727+o(1))n$ coming from an upper bound on the *number* of distinct consecutive sums any increasing sequence can have, due to Beker, but it is weaker than the $ \approx 0.6647n$ bound above. $[arXiv][3]$)[[/nomath]]

## Is (f(n)=o(n))?

This is **open** as stated. ([Erdős Problems][1])

What *is* known in the direction of “it should be sublinear” is an infinite‑sequence obstruction: Erdős noted that for an infinite sequence with this property one has
[
a_k \gg k\log k\quad\text{for infinitely many }k,
]
so any infinite such set has **lower density $0$**. ([Erdős Problems][1])

A quick consequence is that $f(n)$ cannot have a **uniform positive linear density**: one can deduce
[
\liminf_{n\to\infty}\frac{f(n)}{n}=0
]
(otherwise one could build an infinite sequence with positive lower density by a compactness/Kőnig’s-lemma type argument, contradicting Erdős’s observation). But this still falls short of proving (f(n)/n\to 0).

## Context: if you drop monotonicity

If you remove the requirement (a_1<\cdots<a_k) [[nomath]](define $g(n)$ as in the Erdős Problems page)[[/nomath]], then the answer *is* linear: Hegyvári proved
[
\left(\frac13+o(1)\right)n \le g(n) \le \left(\frac23+o(1)\right)n,
]
and Coppersmith–Phillips improve the upper constant slightly. ([Erdős Problems][1])

So the strict increasing-order constraint is exactly where the difficulty lies.

---

If you want, I can also share a small set of exact computed values of $f(n)$ for small $n$ (from exhaustive search) to give a feel for what sizes occur early on, but the asymptotic behavior remains unknown beyond the bounds above.

[1]: https://www.erdosproblems.com/357 "https://www.erdosproblems.com/357"
[2]: https://www.erdosproblems.com/867 "https://www.erdosproblems.com/867"
[3]: https://arxiv.org/pdf/2311.10087 "https://arxiv.org/pdf/2311.10087"

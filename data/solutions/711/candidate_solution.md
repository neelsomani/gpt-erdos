I’ll use the (standard) half‑open version of the definition [[nomath]](which is equivalent up to an additive $1$)[[/nomath]]:
$f(n,m)$ is the least integer $L$ such that the interval $(m,m+L]$ contains **distinct** integers (a_1,\dots,a_n) with (k\mid a_k) for each (1\le k\le n). ([Colgate Math][1])

---

## 1) About the bound (\max_m f(n,m)\le n^{1+o(1)})

This inequality is exactly the **Erdős–Pomerance conjecture** [[nomath]](in particular, they write “We conjecture that $f(n,m)<n^{1+o(1)}$”)[[/nomath]]. ([Dartmouth Math][2])
As of the sources available up to January 2026, this conjectured upper bound is **not proved**; the best general upper bound is

[
\max_m f(n,m)\ll n^{3/2},
]

proved by Erdős and Pomerance. ([Erdős Problems][3])

### Best known general bound: (\max_m f(n,m)\ll n^{3/2}) (Erdős–Pomerance)

I’ll sketch the proof given in their paper (Theorem 4). ([Dartmouth Math][2])

Let (t=\lfloor \sqrt n\rfloor). Consider the integer interval
[
J=(m, m+4nt]\cap\mathbb Z,
]
and partition it into $4t$ consecutive blocks (intervals) of length $n$:
[
(m+(k-1)n, m+kn]\cap\mathbb Z,\qquad k=1,2,\dots,4t.
]
Let (I={1,2,\dots,n}). Make a bipartite graph $G$ with left side $I$, right side $J$, and an edge $(i,j)$ iff (i\mid j).

**Key observations.**

1. Every (i\in I) has degree at least $4t$:
   because in each length‑$n$ block there is at least one multiple of $i$ (since (i\le n)), so across $4t$ blocks, (\deg(i)\ge 4t). ([Dartmouth Math][2])

2. If every (j\in J) has (\deg(j)\le t), then $G$ has a matching covering $I$:
   indeed (\min_{i\in I}\deg(i)\ge 4t>t\ge \max_{j\in J}\deg(j)), and a standard consequence of König–Hall gives a matching from $I$ into $J$. ([Dartmouth Math][2])

So the only obstruction is the existence of some (j_1\in J) with (\deg(j_1)>t). Let (K_1\subseteq I) be the neighbors of (j_1) (so (|K_1|>t)). For each (i\in K_1), define
[
a_i := j_1+i.
]
Then (i\mid j_1) and (i\mid i), hence (i\mid (j_1+i)=a_i). These (a_i) are distinct, and they all lie in the union of the block containing (j_1) and the next block [[nomath]](since $1\le i\le n$)[[/nomath]]. ([Dartmouth Math][2])

Remove those matched indices (K_1) from the left side, and remove a small bounded number of blocks from $J$ to keep the construction disjoint, and iterate the same argument. Erdős–Pomerance show that after at most $t$ iterations, either all indices are matched or we land in the “all right degrees (\le t)” case and finish by König–Hall. Because each iteration removes (>t) left‑vertices, there are at most $t$ iterations. ([Dartmouth Math][2])

Thus all assignments occur inside $(m, m+4nt]$, so
[
f(n,m)\le 4n\lfloor\sqrt n\rfloor + O(n)\ll n^{3/2}.
]
This gives (\max_m f(n,m)\ll n^{3/2}). ([Dartmouth Math][2])

**Remark.** Erdős–Pomerance explicitly state they do not know how to get (o(n^{3/2})) and conjecture (n^{1+o(1)}). ([Dartmouth Math][2])

So, the statement (\max_m f(n,m)\le n^{1+o(1)}) is (as of Jan 2026) a **major open problem** in this area.

---

## 2) Proof that (\max_m\bigl(f(n,m)-f(n,n)\bigr)\to\infty)

This part **is now proved** (van Doorn, 2026), and in fact one has an explicit quantitative lower bound
$
\max_m f(n,m)-f(n,n)>0.36,\frac{n\log n}{\log\log n}
$
for all sufficiently large $n$. In particular the maximum difference (\to\infty). ([Colgate Math][1])

I’ll reproduce the argument.

### Step 1: A scaling lemma

**Lemma.** For all positive integers $k,n$,
[
kn + f(kn,kn)\le k^2n + f(n,k^2n).
\tag{1}
]
**Proof.** We need to find, for each (1\le i\le kn), a distinct multiple (a_i) lying in $(kn,k^2n+f(n,k^2n)]$.

* For $i\in(n,kn]$, set $a_i:=ki$. Then $a_i\in (kn,k^2n]$ and $i\mid ki$. Also these values are distinct as (i) varies.

* For (i\in[1,n]), by definition of (f(n,k^2n)) we can choose distinct multiples $a_i\in (k^2n,k^2n+f(n,k^2n)]$.

These two groups live in disjoint subintervals $(kn,k^2n]$ and $(k^2n,k^2n+f(n,k^2n)]$, so all the $a_i$ are distinct overall. This proves (1). ([Colgate Math][1])

Rearranging (1) gives
[
f(n,k^2n)\ge kn + f(kn,kn) - k^2n.
\tag{2}
]

### Step 2: Bounds on $f(n,n)$

Erdős–Pomerance proved the two-sided bounds [[nomath]](for large $n$)[[/nomath]]:
[
\left(\frac{2}{\sqrt e}+o(1)\right)n\sqrt{\frac{\log n}{\log\log n}}
<
f(n,n)
<
(2+o(1))n\sqrt{\log n}.
\tag{3}
]
([Colgate Math][1])

### Step 3: Choose $k$ and compare scales

Fix (\varepsilon = 1/100) and set
[
k := \left\lfloor 0.6,\sqrt{\frac{\log n}{\log\log n}}\right\rfloor.
]

#### (a) Lower bound $f(kn,kn)$

Apply the lower bound in (3) with $kn$ in place of $n$:
[
f(kn,kn)>\left(\frac{2}{\sqrt e}+o(1)\right)kn\sqrt{\frac{\log(kn)}{\log\log(kn)}}.
]
Since (k=n^{o(1)}), we have (\log(kn)\sim\log n) and (\log\log(kn)\sim\log\log n), so
[
f(kn,kn) > \left(\frac{2}{\sqrt e}+o(1)\right)kn\sqrt{\frac{\log n}{\log\log n}}
=\left(\frac{2}{\sqrt e}+o(1)\right)\frac{1}{0.6}k^2n.
]
Numerically (\frac{2}{\sqrt e}\approx 1.213), so (\frac{1.213}{0.6}\approx 2.02). Hence for all sufficiently large $n$,
[
f(kn,kn)>(2+\varepsilon)k^2n.
\tag{4}
]
This is exactly the inequality used by van Doorn. ([Colgate Math][1])

#### (b) Upper bound $f(n,n)$

From the upper bound in (3),
[
f(n,n) < (2+o(1))n\sqrt{\log n}.
]
But (k^2n \asymp n\frac{\log n}{\log\log n}), and (\frac{\log n}{\log\log n}\gg \sqrt{\log n}). Therefore for large enough $n$,
[
\varepsilonk^2n > f(n,n).
\tag{5}
]
Again, this is as in van Doorn. ([Colgate Math][1])

### Step 4: Put it together

Insert (4) into (2):
[
f(n,k^2n)\ge kn + f(kn,kn) - k^2n
> kn + (2+\varepsilon)k^2n - k^2n
= kn + (1+\varepsilon)k^2n.
]
In particular
[
f(n,k^2n)>(1+\varepsilon)k^2n.
]
Now subtract $f(n,n)$ and use (5):
[
f(n,k^2n)-f(n,n)
>
(1+\varepsilon)k^2n - f(n,n)
\ge
(1+\varepsilon)k^2n - \varepsilon k^2n
=
k^2n.
]
Since (k^2 \ge 0.36\frac{\log n}{\log\log n}) for large $n$, we get
[
\max_m\bigl(f(n,m)-f(n,n)\bigr)
\ge
f(n,k^2n)-f(n,n)
>
0.36,\frac{n\log n}{\log\log n},
]
which tends to (\infty). ([Colgate Math][1])

This proves
[
\max_m(f(n,m)-f(n,n))\to\infty.
]

---

## Summary

* The claim (\max_m f(n,m)\le n^{1+o(1)}) is **the Erdős–Pomerance conjecture** and remains open as of Jan 2026; the best proven general bound is (\max_m f(n,m)\ll n^{3/2}). ([Dartmouth Math][2])
* The divergence (\max_m(f(n,m)-f(n,n))\to\infty) is now proved, with the explicit lower bound (\gg n\log n/\log\log n) (van Doorn, 2026). ([Colgate Math][1])

[1]: https://math.colgate.edu/~integers/aa7/aa7.pdf "https://math.colgate.edu/~integers/aa7/aa7.pdf"
[2]: https://math.dartmouth.edu/~carlp/PDF/matching.pdf "PII: 1385-7258(80)90018-9"
[3]: https://www.erdosproblems.com/711 "https://www.erdosproblems.com/711"

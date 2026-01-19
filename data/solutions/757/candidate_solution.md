For a 4–element set (B={b_1<b_2<b_3<b_4}), the difference set $B-B$ consists of $0$ plus all (\pm(b_j-b_i)) with (j>i). There are at most $6$ positive differences, so
[
|B-B|=1+2\cdot |{b_j-b_i:\ j>i}|.
]
Thus (|B-B|\ge 11) is equivalent to saying that among the $6$ positive pairwise differences, **at least $5$ are distinct** (i.e., at most one collision of distances occurs in any 4–subset). Sets with this property are often called $(4,5)$-sets.

### Key simplification: “Sidon” becomes “3-term-AP-free” in this setting

In a $(4,5)$-set $A$, if you ever have an equality of *positive* differences using four distinct points,
$
x_2-x_1 = x_4-x_3 \qquad (x_1<x_2,\ x_3<x_4,\ {x_1,x_2}\cap{x_3,x_4}=\varnothing),
$
then automatically you get a second equality of positive differences:
[
x_3-x_1 = x_4-x_2
]
[[nomath]](just add $x_3-x_2$ to both sides)[[/nomath]]. That would force at least **two** repeated distances among those four points, contradicting the $(4,5)$ property.

So in a $(4,5)$-set, the **only** way equal positive differences can occur is when the two differences share a point, e.g.
[
y-x = z-y,
]
which is exactly the statement that (x,y,z) form a 3-term arithmetic progression.

Therefore, inside your $A$, a subset is **Sidon** (all positive differences distinct) **iff** it contains **no** 3-term arithmetic progression. This is the standard reformulation used in the literature on this problem. ([Erdős Problems][1])

---

## What is the best constant $c$?

Let
[
g(n):=\min_{|A|=n,\ A\ \text{is }(4,5)}\ \max{|S|:\ S\subseteq A\ \text{Sidon}}.
]
The question asks for the largest constant $c$ such that $g(n)\ge cn$ for all $n$ (equivalently, the optimal guaranteed linear fraction).

### Known lower bounds

* **Erdős–Sós** proved that one can always find a Sidon subset of size at least (\frac{n+1}{2}). In particular,
  [
  c \ge \frac12.
  ]
  ([Erdős Problems][1])

* **Gyárfás–Lehel (1995)** improved this: there exists an absolute (\varepsilon>0) such that
  [
  g(n)\ \ge\ \Big(\frac12+\varepsilon\Big)n.
  ]
  In their proof, an explicit choice is (\varepsilon=\frac{1}{76\cdot 141}=\frac{1}{10716}). ([Rényi Institute][2])

So, from the published results,
[
c \ \ge\ \frac12+\frac{1}{10716}\ \approx\ 0.5000933.
]
([Rényi Institute][2])

### Known upper bound (construction)

Gyárfás–Lehel also give a construction (notably using initial Fibonacci numbers) producing $(4,5)$-sets where every Sidon subset has size at most
[
\frac{3n}{5}+1,
]
so asymptotically
[
c \ \le\ \frac35=0.6.
]
([Erdős Problems][1])

---

## Conclusion

The **exact optimal constant $c$** is **not currently determined** in the literature, but the best published bounds imply
[
\boxed{\ \frac12+\frac{1}{10716}\ \le\ c\ \le\ \frac35\ }.
]
Numerically,
[
\boxed{\ 0.5000933\ldots\ \le\ c\ \le\ 0.6\ }.
]
([Rényi Institute][2])

[1]: https://www.erdosproblems.com/latex/757?utm_source=chatgpt.com "Go"
[2]: https://www.renyi.hu/~gyarfas/Cikkek/69_linset5.pdf "https://www.renyi.hu/~gyarfas/Cikkek/69_linset5.pdf"

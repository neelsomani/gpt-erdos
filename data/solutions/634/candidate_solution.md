This is one of Erdős’ 25 problems (Soifer’s Problem 6.7), and a complete classification of **all** such integers $n$ is **still not known** as of the latest literature summaries (edited Dec 30, 2025). ([Erdős Problems][1])

What *is* known is a fairly large set of values that **do** work, and a couple that **provably do not**.

## Infinitely many values of $n$ that work

Let $S$ be the set of positive integers $n$ for which **there exists at least one** triangle that can be cut into $n$ congruent triangles.

### 1) Every perfect square works: (n = k^2)

In fact, **every** triangle can be cut into (k^2) congruent triangles (“quadratic tiling”): divide each side into $k$ equal parts and draw parallels to the sides to form a triangular grid; the smallest triangles all have side lengths (\frac{1}{k}) of the original, hence are congruent. ([arXiv][2])

So:
[
k^2 \in S \quad \text{for every } k\ge 1.
]

### 2) Closure under multiplying by squares

If (N\in S), then for any integer (m\ge 1),
[
Nm^2 \in S.
]
Reason: take a triangle that is $N$-tiled by congruent triangles; then subdivide **each** of those congruent triangles into (m^2) congruent triangles using a quadratic tiling. ([arXiv][2])

So $S$ is “closed under (\times m^2)”.

### 3) Every sum of two squares works: (n = a^2+b^2)

There is an explicit construction (“biquadratic tiling”) showing that for any integers (a\ge b\ge 1), one can build a triangle that is tiled by exactly (a^2+b^2) congruent right triangles. ([arXiv][2])

Hence:
[
a^2+b^2 \in S \quad \text{for all integers } a,b.
]
This includes (5=1^2+2^2), (10=1^2+3^2), (13=2^2+3^2), (25=0^2+5^2) (i.e. squares), etc.

### 4) The families (2k^2), (3k^2), (6k^2)

There are also standard constructions showing:

* any isosceles triangle can be cut into (2k^2) congruent triangles, ([arXiv][2])
* any equilateral triangle can be cut into (3k^2) or (6k^2) congruent triangles. ([arXiv][2])

So:
[
2k^2,\ 3k^2,\ 6k^2 \in S \quad \text{for all } k\ge 1.
]
[[nomath]](Here $2k^2$ is already covered by $a^2+b^2$, but $3k^2$ and $6k^2$ are genuinely new beyond “sum of two squares”.)[[/nomath]]

## Values of $n$ that do **not** work

A strong theorem due to Michael Beeson proves:

[
7\notin S \quad\text{and}\quad 11\notin S,
]
i.e. **no** triangle can be cut into $7$ congruent triangles, and **no** triangle can be cut into (11) congruent triangles. ([Michael Beeson][3])

## What remains unknown

Beyond the families above and the exclusions $7,11$, the full set $S$ is not yet determined; for example, it is explicitly noted that it is not known whether (19\in S). ([Erdős Problems][1])

---

### Bottom line (best current “answer”)

* **Guaranteed yes:** all $n$ of the forms
  [
  n=k^2,\quad n=a^2+b^2,\quad n=3k^2,\quad n=6k^2
  ]
  [[nomath]](and anything you can get from a known $N$ by multiplying by a square)[[/nomath]].
* **Guaranteed no:** $n=7$ and $n=11$.
* **Everything else:** not fully classified yet.

If you tell me whether you want $a$ explicit geometric constructions drawn out step-by-step for each “yes” family, or $b$ a compact characterization in number-theoretic terms of the known families (e.g. “sums of two squares”), I can tailor the exposition.

[1]: https://www.erdosproblems.com/634 "https://www.erdosproblems.com/634"
[2]: https://arxiv.org/pdf/1206.2231 "https://arxiv.org/pdf/1206.2231"
[3]: https://www.michaelbeeson.com/research/papers/NoSevenTiling.pdf "https://www.michaelbeeson.com/research/papers/NoSevenTiling.pdf"

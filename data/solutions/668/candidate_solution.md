Let $u(n)$ be the maximum possible number of unit distances determined by an $n$-point set in (\mathbb R^2), and let
[
g(n)=|\\{\text{congruence classes of }n\text{-point sets achieving }u(n)\\}|.
]

### Does (g(n)\to\infty) as (n\to\infty)?

This is **open** (it’s explicitly posed as an Erdős problem, #668). ([Erdős Problems][1])

A big reason it’s hard is that even the underlying extremal quantity $u(n)$ is not known in general, so proving *anything* definitive about the *set of maximisers* is currently out of reach in full generality.

What *is* known computationally: Alexeev–Mixon–Parshall (arXiv v2, Feb 12, 2025) determine the exact value of $u(n)$ for all (n\le 21) and enumerate (up to graph isomorphism) all **densest unit-distance graphs** in these cases. ([arXiv][2])
Those enumerations show that for some (n\le 21) there is only one densest unit-distance graph up to isomorphism, while for other $n$ there are several [[nomath]](e.g. multiple isomorphism types already at $n=6$, and many at $n=18$)[[/nomath]]. ([arXiv][2])
This provides evidence *both ways*: it certainly does **not** look like “always unique”, but it also does not constitute a proof that $g(n)$ is unbounded.

[[nomath]](Also, note the subtlety: counting graphs up to isomorphism is only a **lower bound** for $g(n)$, because a single graph can have multiple non-congruent unit-distance embeddings.)[[/nomath]]

### Is it always (>1) for (n>3)?

No. It already fails at $n=4$.

* For $n=4$ the maximum number of unit distances is (u(4)=5), and (up to congruence) there is a **unique** configuration attaining it: **two equilateral triangles sharing an edge** [[nomath]](equivalently, the “diamond graph” $K_4$ minus one edge embedded with unit edges)[[/nomath]]. ([Erdős Problems][1])

Here is a quick self-contained uniqueness argument:

1. With 4 points there are (\binom{4}{2}=6) pairwise distances. If 5 of them are 1, the unit-distance graph must be (K_4) with exactly one missing edge.
2. That graph contains two triangles sharing an edge [[nomath]](say triangles $ABC$ and $ABD$ share $AB$)[[/nomath]].
3. Each triangle with all sides 1 must be equilateral, so $C$ is the third vertex of an equilateral triangle on base (AB), and $D$ is the third vertex of an equilateral triangle on the same base.
4. Given the segment (AB), there are only two possible positions for the third vertex of an equilateral triangle [[nomath]](one on each side of the line $AB$)[[/nomath]]. Since (C\neq D), they must lie on opposite sides, which fixes the configuration uniquely up to rigid motions [[nomath]](and swapping $C,D$)[[/nomath]].

So (g(4)=1), hence the claim “always (>1) for (n>3)” is false. ([Erdős Problems][1])

---

If you want, I can also summarize what the current computations say for (n\le 21) [[nomath]](how many densest unit-distance graphs exist up to isomorphism for each $n$, and what that implies as a guaranteed lower bound for $g(n)$)[[/nomath]]. That’s all known in the Alexeev–Mixon–Parshall tables. ([arXiv][2])

[1]: https://www.erdosproblems.com/668 "https://www.erdosproblems.com/668"
[2]: https://arxiv.org/pdf/2412.11914 "https://arxiv.org/pdf/2412.11914"

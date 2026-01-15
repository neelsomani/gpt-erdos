Take the usual meaning of the arrow:

[
\mathfrak c\to(\beta,n)^3_2
]

means: for every coloring (c:[\mathfrak c]^3\to{0,1}), either there is a set (H\subseteq\mathfrak c) of order type (\beta) with all triples from (H) colored (0), or there is a set (K\subseteq\mathfrak c) of size (n) with all triples from (K) colored (1).

With that interpretation:

* For (n\le 3) the statement is essentially trivial (for (n=2) it is vacuous; for (n=3) a single triple of color 1 already gives the second alternative).
* For the first nontrivial case (n=4) (and larger (n)), the general statement **is open**.

More precisely, this is listed as **Erdős Problem #70**, and its current status is *open*: it is not known in ZFC whether (\mathfrak c\to(\beta,n)^3_2) holds for **every** countable (\beta) and every finite (n\ge 4). ([Erdős Problems][1])

### What is known (partial positive results)

* Erdős and Rado proved the following special case:
  [
  \mathfrak c\to(\omega+n,4)^3_2 \quad\text{for every } 2\le n<\omega.
  ]
  ([Erdős Problems][2])

* There are also ZFC results at (\omega_1) (hence also for (\mathfrak c), since (\mathfrak c\ge\omega_1)):

  * Milner and Prikry proved (\omega_1\to(\omega\cdot 2,4)^3).
  * Jones proved (\omega_1\to(\omega+m,n)^3) for all finite (m,n).

  These give more cases where you can force a countable order type in one color versus a finite set in the other, but still far from “all countable (\beta)”. ([MathOverflow][3])

### Relation to CH

If CH holds, then (\mathfrak c=\omega_1), so your question becomes the corresponding (\omega_1)-statement. A well-known conjecture in this direction (mentioned in the literature) is that (\omega_1\to(\alpha,n)^3) should hold for all countable (\alpha) and finite (n), but this is also not settled. ([MathOverflow][3])

So the clean answer is: **it is not known in general; the problem is open**, with the special cases above being the main established positive results. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/70?utm_source=chatgpt.com "Erdős Problem #70"
[2]: https://www.erdosproblems.com/latex/70?utm_source=chatgpt.com "Go"
[3]: https://mathoverflow.net/questions/71565/partition-calculus-question "set theory - Partition calculus question - MathOverflow"

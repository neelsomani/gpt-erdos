This is **not known in full generality**.

What is known is:

* If (a_n) is a **nondecreasing** sequence of integers [[nomath]](in particular, $2\le a_1\le a_2\le\cdots$)[[/nomath]] then Erdős–Straus proved that
  [
  \sum_{n\ge1}\frac{\tau(n)}{a_1a_2\cdots a_n}
  ]
  is **irrational**. ([MSP][1])

* They also point out that **some restriction is necessary** if one allows completely arbitrary (a_n): for instance the choice (a_n=d(n)+1) makes the analogous series equal to (1). ([MSP][1])
  [[nomath]](This example does *not* satisfy $a_n\to\infty$, but it explains why their arguments impose “regularity” conditions on $(a_n)$.)[[/nomath]]

* There are also **partial results without monotonicity** under additional growth hypotheses. For example, they prove irrationality if (|a_n|) is sufficiently large compared to (\log n) [[nomath]](a condition of the shape $|a_n|>(\log n)^{1+\delta}$ for all $n$, for some $\delta>0$)[[/nomath]]; in that lemma they explicitly note monotonicity is not needed. ([MSP][1])

* They remark that the monotonicity hypothesis can be relaxed somewhat [[nomath]](roughly, to sequences that do not drop too much: a uniform lower bound $a_m/a_n\ge c>0$ for $m>n$)[[/nomath]]. ([MSP][1])

But with **only** the assumption (a_n\to\infty) and **no** monotonicity / “not-too-decreasing” condition, the problem remains open; it is listed as an open Erdős problem (#258). ([Erdős Problems][2])

So the current best answer is:

* **Yes** if (a_n) is nondecreasing (Erdős–Straus).
* **Open** for a general integer sequence with (a_n\to\infty) and no further regularity assumptions.

[1]: https://msp.org/pjm/1971/36-3/pjm-v36-n3-p07-s.pdf "Some number theoretic results"
[2]: https://www.erdosproblems.com/search_bib/Er88c?sources_only=1&utm_source=chatgpt.com "n"

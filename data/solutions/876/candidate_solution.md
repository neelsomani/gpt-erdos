Your condition is exactly what Erdős called a **sum‑free sequence**: an increasing sequence (a_1 < a_2 < \cdots) such that **no** term is a sum of **distinct** smaller terms. ([Libra][1])

### What must happen in general

* **The gaps cannot stay bounded.** Erdős proved every such sequence has **zero asymptotic density**, so in particular the gaps $a_{n+1}-a_n$ must be unbounded (otherwise the density would be positive). ([Libra][1])

So the right question is how *slowly* the gaps can grow.

### Best-known “global” bounds (via the counting function)

Let $A(N)=|A\cap[1,N]|$. The strongest general quantitative bounds currently on record are due to Łuczak–Schoen:

* **Upper bound (all sequences):**
  $$
  A(N)\ll (N\log N)^{1/2}\quad (N\ \text{large}),
  $$
  so $n=A(a_n)\ll \sqrt{a_n\log a_n}$, hence
  $$
  a_n \gg \frac{n^2}{\log n}
  $$
  (up to constants). ([Erdős Problems][2])

* **Lower bound (existence):** there exists a sum‑free set $B$ with
  $$
  |B\cap[1,N]|\gg \frac{N^{1/2}}{(\log N)^{1/2+o(1)}},
  $$
  which inverts to something like
  $$
  a_n \ll n^2(\log n)^{1+o(1)}.
  $$
  ([Erdős Problems][2])

These show the “right” scale for $a_n$ is essentially quadratic (up to logs), hence the “right” scale for gaps is essentially linear (up to logs).

A related formulation (also standard in the literature) is: for every $\delta>0$ there exist sum‑free sequences with $a_n\sim n^{2+\delta}$, and the exponent $2$ cannot be beaten in the sense that you cannot have $a_n \ll n^{2-\varepsilon}$ for any fixed $\varepsilon>0$. 

### Best-known *gap* upper bound

Erdős reported that Graham proved the existence of a sum‑free sequence with
$$
a_{n+1}-a_n < n^{1+o(1)},
$$
and that Melfi had a weaker result. ([Erdős Problems][2])

So we can get gaps “almost linear” [[nomath]](linear times a subpower factor, e.g. $n(\log n)^{O(1)}$ would be consistent with $n^{1+o(1)}$)[[/nomath]].

### Your specific question: can (a_{n+1}-a_n<n)?

This is a well-known Erdős problem (it appears explicitly as Erdős Problem #876) and is currently listed as **open**. ([Erdős Problems][2])

It’s helpful to rephrase what $a_{n+1}-a_n<n$ would mean:

* If $a_{n+1}-a_n < n$ for all $n\ge 1$, then summing gives
  $$
  a_n \le a_1 + \sum_{k=1}^{n-1} k = a_1+\frac{n(n-1)}2,
  $$
  so $a_n = O(n^2)$ with leading constant $\le \tfrac12$.
* Equivalently, this would force a very strong lower bound on the counting function:
  roughly $A(N)\gtrsim \sqrt{2N}$ for large $N$.

Existing constructions (e.g. Łuczak–Schoen’s density lower bound) are still off from this by logarithmic factors, and existing general upper bounds also have logarithmic slack, so neither direction currently settles the strict inequality (a_{n+1}-a_n<n). ([Erdős Problems][2])

### What you *can* say cleanly today

* Gaps must be unbounded (density zero). ([Libra][1])
* There are constructions with **very small relative gaps**, even (a_{n+1}/a_n\to 1) (Deshouillers–Erdős–Melfi), though those particular examples are extremely sparse in absolute terms. ([Libra][1])
* The best-known “near-optimal” gap size is (a_{n+1}-a_n < n^{1+o(1)}) (Graham, as reported by Erdős). ([Erdős Problems][2])
* Whether one can push this all the way down to **(a_{n+1}-a_n<n)** [[nomath]](eventually, or even for all $n$)[[/nomath]] is **still open**. ([Erdős Problems][2])

If you want, I can also unpack how the block/modular constructions in Deshouillers–Erdős–Melfi work (they’re very instructive for thinking about what would be needed to force genuinely linear additive gaps). ([Libra][1])

[1]: https://libra.unine.ch/bitstreams/142bfa87-1d9c-44b6-8269-2b2903cdc132/download "PII: S0012-365X(98)00322-7"
[2]: https://www.erdosproblems.com/forum/thread/876 "https://www.erdosproblems.com/forum/thread/876"

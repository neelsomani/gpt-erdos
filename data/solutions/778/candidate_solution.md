Here’s what’s currently known (as of **Jan 18, 2026**) about these Erdős edge-colouring games on (K_n).

## 1) Largest monochromatic clique: does Bob win for all (n\ge 3)?

This is **still open** in full generality.

This game is now commonly called the **clique-building game** (\mathrm{Clique}(n)): Alice (Red) and Bob (Blue) alternately claim edges of (K_n) (Alice first), and Alice wins iff
[
\omega(R)>\omega(B),
]
otherwise Bob wins (so Bob wins ties).

**Erdős conjectured Bob wins for every (n\ge 3), but no proof is known.** ([Erdős Problems][1])

What *is* known:

* **Bob wins for most $n$:** Malekshahian–Spiro (2024) proved that the set of $n$ for which Bob wins has **asymptotic density at least $3/4$**. ([arXiv][2])
  In particular, Alice can only win (if at all) on a “sparse” set of values of $n$.

* **Red wins can’t cluster:** They prove “reduction” statements of the form “if Alice wins at $n$, then Bob wins at nearby larger sizes.” For example, they show that if Alice were to win at some $n$, then Bob wins at $n+1$ and $n+2$ [[nomath]](and under additional conditions also at $n+3$)[[/nomath]]; this is one route to the density (\ge 3/4) conclusion. ([arXiv][2])

* **Verified small cases:** Cambie–Provoost (2025) report computer verification that **Bob wins (\mathrm{Clique}(n)) for every (3\le n\le 8)**, and they also prove a general implication:
  [
  \text{if Alice wins }\mathrm{Clique}(n)\text{ for some }n\ge 8,\ \text{then Bob wins }\mathrm{Clique}(n+3).
  ]
  ([arXiv][3])

So: **Bob is known to win for (3\le n\le 8)** and for **at least (75%)** of all $n$, but “Bob wins for *every* (n\ge 3)” remains unproved. ([Erdős Problems][1])

---

## 2) Biased version: Bob colours two edges per Alice move, and must end with a strictly larger clique

This is the biased clique-building game (\mathrm{Clique}(1,2)(n)): Alice claims 1 edge per turn, Bob claims 2 per turn, and now **Bob only wins if**
[
\omega(B)>\omega(R),
]
otherwise Alice wins.

This is also **open** for $(1,2)$ in general, and it is explicitly discussed as an Erdős question. ([arXiv][3])

What *is* known:

* Malekshahian–Spiro (2024) **could not** prove Bob always wins for $(1,2)$, but they proved Bob wins for much larger bias—e.g. they can show Bob wins (\mathrm{Clique}(1,15)(n)) for all sufficiently large $n$, and more generally give a condition like
  (q+1 > (3.999)^{2p}) implying a Player 2 win for all sufficiently large $n$. ([arXiv][2])

* Cambie–Provoost (2025) significantly strengthened this and proved:
  [
  \boxed{\text{For every }n\ge 4,\ \mathrm{Clique}(1,3)(n)\text{ is a Bob (Player 2) win.}}
  ]
  ([arXiv][3])
  They also state they **conjecture** the same should hold for $(1,2)$. ([arXiv][3])

So for your exact $(1,2)$ question: **best current answer is “unknown,” but conjectured yes** [[nomath]](for $n\ge 4$)[[/nomath]], with the strongest proven nearby result being $(1,3)$. ([arXiv][3])

---

## 3) Maximum-degree version: Alice wins if (\Delta(R)>\Delta(B)). Who wins?

This is the **star-building game** (\mathrm{Star}(n)) (since a star size is maximum degree). It is also **open** in full generality. ([Erdős Problems][1])

What is known:

* Malekshahian–Spiro (2024) proved that Bob wins for **a set of $n$** with **asymptotic density at least $2/3$**. ([arXiv][2])
  They also prove a “non-clustering” statement: **if Alice wins at some (n\ge 3), then Bob wins at $n+1$ and $n+2$**, which yields the density lower bound. ([arXiv][2])

* Cambie–Provoost (2025) go further in *conjecturing* a clean general rule for this parameter on regular graphs:
  **except for (K_2) and (K_3), the second player should always win the Star game on every regular graph**, in particular on (K_n) for (n\ge 4). ([arXiv][3])
  But this remains a conjecture in the unbiased case.

* In the **biased** degree game, things are much more complete: for example, they prove that with bias $(1,2)$ (Bob takes two edges per turn), the maximum-degree game is a **Bob win for all (n\ge 3)**. ([arXiv][3])
  (This is extra context; your question here was the unbiased case.)

So: for the **unbiased maximum-degree** version, the answer is **not fully known**, but the best evidence points toward **Bob always winning for (n\ge 4)** (and this is explicitly conjectured), and Bob is provably winning for at least $2/3$ of all $n$. ([arXiv][3])

---

If you want, I can also summarize (at a high level) the *type* of strategy-stealing/monotonicity argument used in the reductions “Alice wins at $n$ (\Rightarrow) Bob wins at $n+1$, $n+2$, …,” since it’s quite elegant and applies in both the clique and star settings.

[1]: https://www.erdosproblems.com/778 "https://www.erdosproblems.com/778"
[2]: https://arxiv.org/pdf/2410.18304 "https://arxiv.org/pdf/2410.18304"
[3]: https://arxiv.org/pdf/2505.03497 "https://arxiv.org/pdf/2505.03497"
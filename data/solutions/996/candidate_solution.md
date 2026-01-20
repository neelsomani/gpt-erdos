This is **open** in general.

Erdős posed essentially this question in his 1964 paper and wrote that he *expected* one might be able to replace a (log log)-type hypothesis by a **(log log log)**-type hypothesis, but he “was not able to decide this.” ([Numdam][1])

What is known (in the direction you’re asking):

* **Special lacunary sequences (exact powers):** If (n_k=a^k) with an integer (a\ge2), then **no Fourier-decay/approximation assumption is needed**: Raikov proved the conclusion holds for every integrable $f$, and Riesz gave an ergodic-theoretic proof. ([Numdam][1])

* **You cannot drop all regularity on $f$:** Erdős also constructed a **lacunary** sequence and an (f\in L^p) for every $p$ [[nomath]](hence in $L^2$)[[/nomath]] for which the conclusion fails. ([Numdam][1])
  So some condition beyond mere (L^2) is genuinely necessary for arbitrary lacunary sequences.

* **Quantitative Fourier approximation assumptions that *do* work:**
  Kac–Salem–Zygmund proved the conclusion under a much stronger hypothesis
  [
  |f-f_n|_2 \ll (\log n)^{-c}\quad\text{for some }c>1,
  ]
  and Erdős improved this to
  [
  |f-f_n|_2 \ll (\log\log n)^{-c}\quad\text{for some }c>1.
  ]
  Matsuyama then pushed this further to allow (c>1/2) in the ((\log\log n)^{-c}) condition. ([Erdős Problems][2])

What remains unknown is whether one can go all the way down to a **triple-log** rate like
[
|f-f_n|_2 \ll (\log\log\log n)^{-C}
]
for some absolute (C>0) (as in your question). This is exactly the unresolved step Erdős highlighted. ([Numdam][1])

Erdős also asked the related (still open) question of whether the conclusion might even hold for **all bounded** $f$ and lacunary ((n_k)), noting he couldn’t make his counterexample bounded. ([Numdam][1])

[1]: https://www.numdam.org/article/CM_1964__16__52_0.pdf "https://www.numdam.org/article/CM_1964__16__52_0.pdf"
[2]: https://www.erdosproblems.com/forum/discuss/996 "https://www.erdosproblems.com/forum/discuss/996"

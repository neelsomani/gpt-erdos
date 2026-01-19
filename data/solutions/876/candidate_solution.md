What you call an “infinite sum‑free set” is usually studied as a **sum‑free sequence**: an increasing sequence (a_1<a_2<\cdots) such that no term is a sum of **distinct** earlier terms. ([Wikipedia][1])

## The gap (a_{n+1}-a_n) can be as small as $1$ (infinitely often)

It’s not just that (a_{n+1}-a_n\ge 1) trivially; one can make the gap **equal to 1 infinitely many times** in a genuinely sum‑free sequence.

Here is an explicit construction:

* Set (a_1=2).
* For (k\ge 1), define
  [
  a_{2k}=a_{2k-1}+1,\qquad
  a_{2k+1}=1+\sum_{i=1}^{2k} a_i.
  ]

Then
[
a_{2k}-a_{2k-1}=1\quad\text{for every }k,
]
so the sequence has infinitely many consecutive pairs.

**Why it is sum‑free.**

* For odd indices $2k+1$: by definition (a_{2k+1}=1+\sum_{i=1}^{2k}a_i), so (a_{2k+1}) is **bigger than the sum of all earlier terms**. Hence it cannot equal a sum of distinct earlier terms.
* For even indices (2k): we have (a_{2k}=a_{2k-1}+1).

  * If a representation of (a_{2k}) used (a_{2k-1}), the remaining summands would have to sum to $1$, impossible since all terms are (\ge 2).
  * If it did **not** use (a_{2k-1}), then the sum of any subset of ({a_1,\dots,a_{2k-2}}) is at most (\sum_{i=1}^{2k-2}a_i=a_{2k-1}-1), so it cannot reach (a_{2k}=a_{2k-1}+1).

So the sequence is sum‑free and has infinitely many gaps equal to $1$.

**Consequence:** If you only mean “does (a_{n+1}-a_n<n) happen infinitely often?”, then **yes** [[nomath]](because $a_{2k}-a_{2k-1}=1<2k-1$ for all $k\ge 2$)[[/nomath]].

## If you mean “(a_{n+1}-a_n<n) for all large $n$”: this is essentially the quadratic-growth boundary

The inequality
[
a_{n+1}-a_n<n \quad\text{for all }n
]
would force a **quadratic upper bound** on (a_n), since telescoping gives
[
a_n \le a_1+\sum_{k=1}^{n-1}k = a_1+\frac{n(n-1)}2.
]
So it would imply (a_n = O(n^2)).

What is known about how slowly (a_n) can grow?

* Deshouillers–Erdős–Melfi constructed sum‑free sequences of **polynomial growth** and even with multiplicative gaps tending to $1$ [[nomath]](their “no gap” property is about $a_{n+1}/a_n\to 1$)[[/nomath]]. ([Academia][2])
* Łuczak and Schoen improved the polynomial-growth constructions to show that for every (\varepsilon>0) there exist sum‑free sequences with
  [
  a_n = O(n^{2+\varepsilon}),
  ]
  and they also proved that the exponent $2$ is a genuine barrier in the sense that you cannot beat $2$ by any fixed amount [[nomath]](no $O(n^{2-\varepsilon})$)[[/nomath]]. ([RivMat][3])
  [[nomath]](See also their paper reference page. $[Math Institute PAS][4]$)[[/nomath]]

So “(a_{n+1}-a_n<n) eventually” would be asking for a **very strong** form of “quadratic-type” growth [[nomath]](certainly $a_n=O(n^2)$)[[/nomath]], right at the critical exponent boundary highlighted by Łuczak–Schoen. ([RivMat][3])

### Status

From the standard references above, the best general constructions are still of the form (a_n=O(n^{2+\varepsilon})) [[nomath]](any fixed $\varepsilon>0$)[[/nomath]], and the theory shows you can’t do $O(n^{2-\varepsilon})$. ([RivMat][3])
Whether one can achieve a uniform **quadratic** bound strong enough to force (a_{n+1}-a_n<n) for all large $n$ is not settled in those sources; I do not see a known construction or impossibility result there.

## Bottom line

* The gap (a_{n+1}-a_n) can be **as small as 1**, infinitely often (explicit construction above).
* If your question is the stronger one—can we have (a_{n+1}-a_n<n) for **all sufficiently large $n$**—that would essentially require “quadratic-scale” growth (a_n=O(n^2)), and the classical results place this at the critical boundary: we can get (n^{2+\varepsilon}) for every fixed (\varepsilon>0) but not (n^{2-\varepsilon}). ([RivMat][3])

[1]: https://en.wikipedia.org/wiki/Sum-free_sequence?utm_source=chatgpt.com "Sum-free sequence"
[2]: https://www.academia.edu/917204/On_a_question_about_sum_free_sequences?utm_source=chatgpt.com "(PDF) On a question about sum-free sequences"
[3]: https://www.rivmat.unipr.it/fulltext/2004-3s/pdf/16.pdf "https://www.rivmat.unipr.it/fulltext/2004-3s/pdf/16.pdf"
[4]: https://old.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/95/3/111910/on-the-maximal-density-of-sum-free-sets "On the maximal density of sum-free setsAll"

Interpreting your display as a typo (as noted on the Erdős Problems forum), the intended forbidden relation is

[
\frac1a=\frac1{b_1}+\cdots+\frac1{b_k}
]

with **distinct** (a,b_1,\dots,b_k\in A) [[nomath]](and $k\ge 2$, since $k=1$ would force $a=b_1$)[[/nomath]]. ([Erdős Problems][1])

---

## What is known about $f(N)$

This is Erdős–Graham problem #301 and is currently **open**. ([Erdős Problems][2])

### Lower bound: (f(N)\ge N/2)

Take
[
A=\\{ \lfloor N/2\rfloor+1,\dots,N\\}.
]
Then (|A|=\lceil N/2\rceil).

Why this works: if (a\in A), then (a>N/2), and any (b_i\in A) with (b_i\ne a) must satisfy (b_i>a), hence (b_i\le N<2a). Multiplying the equation by $a$ gives
[
1=\sum_{i=1}^k \frac{a}{b_i}.
]
But each term satisfies
[
\frac12<\frac{a}{b_i}<1,
]
so for (k\ge 2) the RHS is (>1), contradiction. Hence there are no solutions, and (f(N)\ge N/2). ([Erdős Problems][2])

### Best published/recorded upper bound: (f(N)\le (25/28+o(1))N)

Wouter van Doorn gave an elementary density argument yielding
[
f(N)\le \Bigl(\frac{25}{28}+o(1)\Bigr)N\approx (0.892857\ldots+o(1))N.
]
The idea is to pack ({1,\dots,N}) with many **disjoint** “blocks”
[
S_a={2a,3a,4a,6a,12a}\cap[1,N]
]
over a carefully chosen set of $a$’s [[nomath]](of the form $8^b9^cd$ with $(d,6)=1$)[[/nomath]]. Within each full block [[nomath]](when $12a\le N$)[[/nomath]], the unit-fraction identities among these multiples force any admissible $A$ to miss at least two elements of (S_a); in the partially truncated range [[nomath]](roughly $N/12<a\le N/6$)[[/nomath]] one still must miss at least one element. Counting across the disjoint blocks gives the $25/28$ bound. ([Erdős Problems][2])

So the best current general estimate is

[
\frac12,N \ \le\ f(N)\ \le\ \Bigl(\frac{25}{28}+o(1)\Bigr)N.
]
([Erdős Problems][2])

---

## Is (f(N)=(\tfrac12+o(1))N)?

This is exactly the Erdős conjecture as recorded in OEIS and the Erdős Problems database, and it remains **unproved**. ([OEIS][3])

### Numerical data (small $N$)

OEIS A390394 tabulates exact values up to (n=38); for instance $f(38)=29$, i.e. (f(38)/38\approx 0.763). ([OEIS][3])
This is far above $1/2$ at small scales, so computationally one does **not** “see” the conjectured $1/2$ behavior yet [[nomath]](but small-$N$ data can be very misleading for problems like this)[[/nomath]].

---

## A useful comparison: if repetitions were allowed, the threshold would be $1/2$

If one *drops* the distinctness requirement on the (b_i)’s, then having (|A|>(1/2+o(1))N) forces a divisibility relation (a\mid b) inside $A$ (classic), and then (1/a = (b/a)\cdot (1/b)) would be a “solution” using repeated $b$’s. In that relaxed model the maximum size is (\le N/2). ([Erdős Problems][2])

This helps explain why Erdős expected $1/2$ might be the true constant even under distinctness: the obstruction to proving it is precisely the need to “split” repetitions into distinct denominators (\le N), which is subtle.

---

## Bottom line

* **Known:** ( \displaystyle \frac12N \le f(N) \le \left(\frac{25}{28}+o(1)\right)N.) ([Erdős Problems][2])
* **Conjectured:** ( f(N) = \left(\frac12+o(1)\right)N) (Erdős), still **open**. ([OEIS][3])

If you want, I can also summarize the closely related “(k=2) only” version [[nomath]](forbidding just $1/a=1/b+1/c$)[[/nomath]], where different intermediate density bounds are known. ([Erdős Problems][4])

[1]: https://www.erdosproblems.com/forum/thread/301 "https://www.erdosproblems.com/forum/thread/301"
[2]: https://www.erdosproblems.com/301 "https://www.erdosproblems.com/301"
[3]: https://oeis.org/A390394 "https://oeis.org/A390394"
[4]: https://www.erdosproblems.com/302 "https://www.erdosproblems.com/302"

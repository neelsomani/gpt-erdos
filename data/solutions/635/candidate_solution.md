Write (F_t(N)) for the maximum size of a set (A\subseteq{1,\dots,N}) with the property

[
(\forall, a<b\in A,\ b-a\ge t)\qquad (b-a)\nmid b.
]

A useful rephrasing is:

**Lemma (equivalence).** A pair (a<b) violates the condition iff there exist integers (d\ge t) and (k\ge 1) such that
[
a=kd,\qquad b=(k+1)d.
]
Indeed, if (d=b-a\mid b) then (b=(k+1)d) and (a=b-d=kd). Conversely, any such consecutive multiples violate since (b-a=d\mid b).

So the condition is exactly:

> For every integer (d\ge t), the set $A$ contains **no two consecutive multiples of $d$** [[nomath]](i.e. never both $kd$ and $(k+1)d$)[[/nomath]].

---

## Lower bounds

### A universal (\frac12 N) construction

Take all odd numbers:
[
A_{\text{odd}}={1\le n\le N:\ n\text{ odd}}.
]
Then for any (a<b) in (A_{\text{odd}}), the difference $b-a$ is even, while $b$ is odd, so ((b-a)\nmid b). Hence
[
F_t(N)\ \ge\ \left\lceil \frac N2\right\rceil
]
for every (t\ge 1).

### For (t\ge 2), you can beat (\frac12N) by (\gg \log N)

A standard explicit construction for $t=2$ [[nomath]](and it works for any $t\ge2$)[[/nomath]] is:
[
A = {\text{odd }\le N}\ \cup\ {2^{1},2^{3},2^{5},\dots}\cap[1,N].
]

* Odds don’t conflict with each other.
* A power of 2 has no odd divisors (>1), so it doesn’t create a forbidden pair with an odd number when (t\ge2) [[nomath]](the only odd divisor is $1$, but differences $=1$ are $<t$)[[/nomath]].
* Among powers of 2, the only “consecutive-multiples” obstruction is between consecutive powers (2^k,2^{k+1}); choosing every other exponent avoids that.

This gives
[
|A| = \left\lceil\frac N2\right\rceil ;+; |\\{j\ge0:\ 2^{2j+1}\le N\\}|
= \left\lceil\frac N2\right\rceil + \left\lfloor\frac{\lfloor\log_2 N\rfloor+1}{2}\right\rfloor,
]
so in particular
[
F_t(N)\ \ge\ \frac N2 ;+; c\log N\qquad (t\ge2)
]
for some absolute (c>0). This kind of (\frac N2+c\log N) lower bound for $t=2$ is recorded in the Erdős problems database. ([Erdős Problems][1])

---

## Upper bounds and the (\left(\tfrac12+o_t(1)\right)N) question

For $t=1$, the constraint includes $d=1$, so you cannot take two consecutive integers. This immediately forces
[
F_1(N)=\left\lfloor\frac{N+1}{2}\right\rfloor,
]
and this is also recorded in the Erdős problems database. ([Erdős Problems][1])

For general fixed $t$, there is a reported **asymptotic upper bound** of the form
[
F_t(N)\ \le\ \frac N2 ;+; C_t\frac{N}{\log N},
]
attributed to a result of Imre Ruzsa (Erdős reporting on a letter), as stated in R. K. Guy’s “A Miscellany of Erdős Problems.” ([JSTOR][2])

This upper bound immediately implies the statement you asked about:
[
F_t(N)\ \le\ \left(\frac12 + o_t(1)\right)N
\qquad (N\to\infty,\ t\ \text{fixed}),
]
since (C_t/\log N \to 0). ([JSTOR][2])

---

## What’s still not nailed down

Even if one accepts the above (N/2+O_t(N/\log N)) upper bound, there is still a big gap between:

* the **known lower bound** ( \frac N2 + \Omega(\log N)) [[nomath]](already for $t=2$)[[/nomath]], ([Erdős Problems][1])
* and the **reported upper bound** ( \frac N2 + O_t(N/\log N)). ([JSTOR][2])

Determining the true “second-order term” beyond (\frac12N) is part of why the Erdős problem is listed as open in the database. ([Erdős Problems][1])

---

### Bottom line

* The leading term is (\frac12N): yes, (|A|\le (\frac12+o_t(1))N) is (at least) **consistent with** and in fact **implied by** the reported Ruzsa bound (F_t(N)\le \frac N2 + O_t(N/\log N)). ([JSTOR][2])
* There are explicit constructions with (|A| = \frac N2 + \Omega(\log N)) for (t\ge2). ([Erdős Problems][1])
* The sharp growth of the additive error term beyond (\frac12N) is (as far as the database indicates) not settled. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/635 "https://www.erdosproblems.com/635"
[2]: https://www.jstor.org/stable/2975810 "https://www.jstor.org/stable/2975810"

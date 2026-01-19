Let
[
P_{n,\ell}:=n(n+1)\cdots(n+\ell),
\qquad
P_{n,\ell}=\prod_p p^{v_p(P_{n,\ell})},
]
and
[
Q_2(P_{n,\ell})=\prod_{p:,v_p(P_{n,\ell})\ge 2} p^{v_p(P_{n,\ell})}
]
[[nomath]](the “powerful/squarefull part” of $P_{n,\ell}$)[[/nomath]].

## 1) Is it true that (Q_2(P_{n,\ell})<n^{2+\varepsilon}) eventually?

* **For (\ell=1)** this is **true and trivial**:
  $
  Q_2(n(n+1))\le n(n+1)<n^{2+\varepsilon}\quad(n\ \text{large}).
  $

* **For every fixed (\ell\ge 2)** this is, as far as I can find, **open**. It appears explicitly as an Erdős problem (often catalogued as “Erdős Problem #935”). ([Erdős Problems][1])

So: **yes for (\ell=1)**; **unknown for (\ell\ge 2)**.

## 2) For (\ell\ge 2), is (\displaystyle \limsup_{n\to\infty}\frac{Q_2(P_{n,\ell})}{n^2}) infinite?

What is known unconditionally is the **lower bound**
[
\limsup_{n\to\infty}\frac{Q_2(P_{n,\ell})}{n^2}\ \ge\ 1
\qquad(\text{for every }\ell\ge 1),
]
coming from the existence of infinitely many **pairs of consecutive powerful (squarefull) integers** (Mahler). For such $n$, (Q_2(n(n+1))=n(n+1)), and hence for any (\ell\ge 1),
[
Q_2(P_{n,\ell})\ \ge\ Q_2(n(n+1))\ =\ n(n+1)\sim n^2.
]
This is the standard observation recorded in the Erdős problem discussion. ([Erdős Problems][1])

* For (\ell=1) you can in fact pin down the limsup:
  [
  \frac{Q_2(n(n+1))}{n^2}\le \frac{n(n+1)}{n^2}=1+\frac1n,
  ]
  so (\limsup = 1).

* For (\ell\ge 2), whether the limsup is actually **unbounded** (i.e. (=\infty)) seems to be **open** in the same circle of questions as above; I do not know of a proof either way, and the Erdős-problem writeup treats the problem as open. ([Erdős Problems][1])

So: **(\ge 1) is known**, **(\infty) is (apparently) open**.

## 3) For (\ell\ge 2), is (\displaystyle \lim_{n\to\infty}\frac{Q_2(P_{n,\ell})}{n^{\ell+1}}=0)?

This would follow immediately from the first conjectured bound (Q_2(P_{n,\ell})<n^{2+\varepsilon}) [[nomath]](take $\varepsilon<\ell-1$)[[/nomath]], since then
[
\frac{Q_2(P_{n,\ell})}{n^{\ell+1}} \ \le\ n^{-(\ell-1)+\varepsilon}\ \to\ 0.
]

But because the **(n^{2+\varepsilon})** bound is open for (\ell\ge 2), this limit statement is also (as far as I can tell) **open** in that same problem cluster. ([Erdős Problems][1])

### Related context

One way the ratio (Q_2(P_{n,\ell})/n^2) could become very large is if one could force many of the factors (n,n+1,\dots,n+\ell) to have “large” powerful parts simultaneously. The extreme case would be long blocks of consecutive powerful integers; even the case of **three consecutive powerful integers** is a famous open problem, and it is known that the (abc) conjecture would imply at least *finiteness* of such triples. ([Nitaj][2]) (This is context, not a resolution of your questions.)

## Bottom line

* (\ell=1): **Yes**, (Q_2(n(n+1))<n^{2+\varepsilon}) eventually; and (\limsup Q_2(n(n+1))/n^2=1).
* (\ell\ge 2): the inequality (Q_2(P_{n,\ell})<n^{2+\varepsilon}) is **open**. ([Erdős Problems][1])
  The limsup is **known (\ge 1)** (Mahler), but whether it is **(\infty)** is **open**. ([Erdős Problems][1])
  The limit (Q_2(P_{n,\ell})/n^{\ell+1}\to 0) is also **open** (and would follow from the first bound). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/935 "https://www.erdosproblems.com/935"
[2]: https://nitaj.users.lmno.cnrs.fr/abc.html "https://nitaj.users.lmno.cnrs.fr/abc.html"

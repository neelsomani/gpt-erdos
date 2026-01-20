Let (F_n=\\{\frac{a_1}{b_1}<\frac{a_2}{b_2}<\cdots\\}) be the Farey sequence of order $n$, and recall that (\frac{a_k}{b_k},\frac{a_\ell}{b_\ell}) are *similarly ordered* iff
[
(a_\ell-a_k)(b_\ell-b_k)\ge 0,
]
i.e. the numerators and denominators move in the same direction (weakly).

This is a classical problem (Mayer–Erdős phenomenon), and there has been a major recent improvement.

## Best currently known bounds

A 2025 preprint of Wouter van Doorn proves sharp **linear** bounds of the form
[
\left(\frac{1}{12}-o(1)\right)n \ \le\ f(n)\ \le\ \frac14 n+O(1).
]
More precisely:

* **Upper bound (explicit):** for every (n\ge 4),
  [
  f(n)\ \le\ \Big\lfloor \frac n4\Big\rfloor + d,
  \qquad d=
  \begin{cases}
  1,& n\equiv 0\pmod 4\
  2,& n\equiv 1\pmod 4\
  2,& n\equiv 2\pmod 4\
  4,& n\equiv 3\pmod 4~,
  \end{cases}
  ]
  obtained by constructing a pair of Farey fractions at distance (\asymp n/4) that are **not** similarly ordered. ([arXiv][1])

* **Lower bound (explicit):** if (a_k/b_k<a_\ell/b_\ell) are two Farey fractions of order $n$ with
  [
  \ell-k \ \le\ \frac n{12}\Big(1-\frac{4}{n^{1/3}}\Big),
  ]
  then they are similarly ordered. In particular,
  [
  f(n)\ \ge\ \frac n{12}\Big(1-\frac{4}{n^{1/3}}\Big)
  \ =\ \left(\frac{1}{12}-O(n^{-1/3})\right)n.
  ]
  ([arXiv][1])

So **(f(n)=\Theta(n))**, and as of now the best constants are
[
\frac{1}{12}\ \lesssim\ \liminf_{n\to\infty}\frac{f(n)}n
\le
\limsup_{n\to\infty}\frac{f(n)}n
\ \le\ \frac14.
]
([arXiv][1])

[[nomath]](For historical context: Erdős already proved a linear lower bound $f(n)\ge c n$ with an explicit $c$ as small as $1/400$; van Doorn’s work improves this substantially. $[arXiv][1]$)[[/nomath]]

## Does there exist a constant $c$ with (f(n)=(c+o(1))n)?

**This is still open.** The Erdős Problems site currently lists the problem as open and records exactly the bounds above. ([Erdős Problems][2])

What *is* known is that any such constant $c$, if it exists, must satisfy
[
\frac{1}{12}\ \le\ c\ \le\ \frac14
]
by the proven bounds. ([arXiv][1])

## What is conjectured?

Van Doorn also puts forward a very strong conjecture that the **upper bound is essentially optimal**:

* Conjecture (van Doorn): for all (n\ge 92),
  [
  f(n)=\Big\lfloor \frac n4\Big\rfloor + d
  \quad\text{with the same }d\text{ as above,}
  ]
  and this was checked computationally up to (n\le 5000). ([arXiv][1])

If this conjecture is true, then
[
f(n)=\left(\frac14+o(1)\right)n,
]
so the answer to your “$c$ exists?” question would be **yes**, with (c=\tfrac14).

The OEIS entry tracking $f(n)$ (A386893) records the same bounds and the same conjectural eventual formula. ([OEIS][3])

[1]: https://arxiv.org/pdf/2509.00121 "Improved bounds for the Mayer-Erd\H{o}s phenomenon on similarly ordered Farey fractions"
[2]: https://www.erdosproblems.com/1005 "
  
    Erdős Problem #1005
  
"
[3]: https://oeis.org/A386893 "A386893 - OEIS"

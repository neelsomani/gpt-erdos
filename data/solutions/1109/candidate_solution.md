Write $f(N)$ for the maximum size of (A\subseteq{1,\dots,N}) with the property that
[
a+a'\ \text{is squarefree for all }a,a'\in A
]
[[nomath]](i.e. every element of $A+A$ is squarefree, including the “diagonal” sums $2a$)[[/nomath]].

### Quick necessary structure (easy, but very restrictive)

Because (2a\in A+A) must be squarefree, every (a\in A) must be **odd** and **squarefree** [[nomath]](if $a$ were even then $4\mid 2a$, and if $p^2\mid a$ then $p^2\mid 2a$)[[/nomath]].
Also, since sums of two odd numbers are even, (a+a') being squarefree forces (a+a'\not\equiv 0\pmod 4), so (a+a'\equiv 2\pmod 4). That implies **all elements of $A$ lie in the same odd residue class mod $4$** [[nomath]](all $\equiv 1\pmod 4$ or all $\equiv 3\pmod 4$)[[/nomath]].

These constraints are nowhere near enough to determine $f(N)$, but they illustrate why the problem is highly arithmetic.

### Best known quantitative bounds (as of 2025)

This problem is recorded as an Erdős problem (#1109), and the sharpest published bounds currently trace back to work of Konyagin (2004), as summarized for instance by van Doorn–Tao (2025). The current best is:
[
(\log N)^2\log\log N \ \ll\ f(N)\ \ll\ N^{11/15}\exp!\Big(O!\Big(\frac{\log N}{\sqrt{\log\log N}}\Big)\Big)
\qquad (N\ \text{large}).
]
Equivalently,
[
f(N)\ \le\ N^{11/15+o(1)}\qquad (11/15\approx 0.7333\ldots).
]
These are explicitly stated in van Doorn–Tao’s discussion of “squarefree sums”. ([arXiv][1])

For comparison, the “plain” large sieve method only gives the weaker upper bound (f(N)\ll N^{3/4}), also noted there. ([arXiv][1])
And the Erdős Problems page records the same [[nomath]](polylogarithmic lower / $N^{11/15+o(1)}$ upper)[[/nomath]] gap. ([Erdős Problems][2])

### So what about (f(N)\le N^{o(1)}) or (f(N)\le (\log N)^{O(1)})?

Those are **open** given the current state of the art:

* The best *upper* bound is still polynomial (N^{11/15+o(1)}), which is far from (N^{o(1)}). ([arXiv][1])
* The best *lower* bound is already polylogarithmic, (f(N)\gg (\log N)^2\log\log N), so polylogarithmic growth is at least plausible, but **no polylogarithmic upper bound is known**. ([arXiv][1])

### A related (infinite) consequence

If (A={a_1<a_2<\dots}) is an infinite sequence with squarefree sums, then (|A\cap[1,N]|\le f(N)). Inverting the upper bound above gives a necessary growth condition:
[
a_j \ \gg\ j^{15/11}\exp\Big(-O\Big(\frac{\log j}{\sqrt{\log\log j}}\Big)\Big),
]
again explicitly recorded in van Doorn–Tao. ([arXiv][1])
So any such infinite sequence must grow at least about (j^{15/11-o(1)}), but whether one can achieve genuinely polynomial growth remains a different question.

### Bottom line

What we currently know is
[
(\log N)^2\log\log N \ \ll\ f(N)\ \ll\ N^{11/15+o(1)},
]
and improving either side to settle whether $f(N)$ is subpolynomial (let alone polylogarithmic) is still open. ([arXiv][1])

[1]: https://arxiv.org/pdf/2512.01087 "Growth rates of sequences governed by the squarefree properties of its translates"
[2]: https://www.erdosproblems.com/latex/1109?utm_source=chatgpt.com "Erdős Problems"

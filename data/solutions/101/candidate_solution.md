This statement is **not proved** (and not disproved). It is a well-known **open problem of Erdős**. In fact it appears in lists of Erdős problems as “Given $n$ points in (\mathbb R^2), no five collinear, is the number of 4-point lines $o(n^2)$?” and is marked **OPEN**. ([Erdős Problems][1])

What *is* known:

### 1) Easy upper bound: $O(n^2)$

Let (t_4) be the number of lines containing exactly 4 of the points (this is the same as “at least 4” since no 5 are collinear).

Each 4-point line contains (\binom{4}{2}=6) distinct pairs of points.

A pair of points determines **only one** line, so the 6 pairs coming from one 4-point line cannot be “re-used” by a different 4-point line.

So
[
6t_4 \le \binom{n}{2}
\quad\Rightarrow\quad
t_4 \le \frac{\binom{n}{2}}{6} = \frac{n(n-1)}{12}.
]
This gives (t_4 = O(n^2)). (But it does **not** give $o(n^2)$.)

### 2) Very large lower bounds exist (almost quadratic)

Grünbaum already built examples with (\gg n^{3/2}) four-point lines. ([Erdős Problems][2])

Later, Solymosi and Stojaković built examples with **no five collinear** and at least
[
n^{,2-\frac{c}{\sqrt{\log n}}}
]
collinear 4-tuples (equivalently: that many 4-point lines, because no line can contain 5 points). ([arXiv][3])

Note that
[
\frac{n^{2-\frac{c}{\sqrt{\log n}}}}{n^2}
= n^{-\frac{c}{\sqrt{\log n}}}
= e^{-c\sqrt{\log n}}
\to 0,
]
so this is still $o(n^2)$, but it is **extremely close** to $n^2$.

### 3) What remains open

So we currently know:

* Always (t_4 \le n(n-1)/12) (quadratic upper bound).
* There are constructions with (t_4 \ge n^{2-\frac{c}{\sqrt{\log n}}}) (almost quadratic).
* But nobody has proved that **every** such point set must satisfy (t_4=o(n^2)), and nobody has built a counterexample with (t_4 \ge c n^2) for a fixed (c>0). ([Erdős Problems][2])

If you want, I can also explain why the usual incidence bound (Szemerédi–Trotter) is not enough here [[nomath]](it only gives $O(n^2)$ when $k=4$)[[/nomath]], and what kinds of “new ideas” people think are needed.

[1]: https://www.erdosproblems.com/101?utm_source=chatgpt.com "Erdős Problem #101"
[2]: https://www.erdosproblems.com/prizes/100/no "
  
    Erdős Problems
  
"
[3]: https://arxiv.org/abs/1107.0327?utm_source=chatgpt.com "Many collinear k-tuples with no k+1 collinear points"

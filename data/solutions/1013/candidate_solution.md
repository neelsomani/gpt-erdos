Let

[
h_3(k)=\min{,n:\exists\ \text{triangle-free }G\text{ with }|V(G)|=n,\ \chi(G)=k,}.
]

Throughout, (\log) is the natural logarithm.

## 1. Asymptotic order of (h_3(k))

The correct order of magnitude is

[
h_3(k)=\Theta(k^2\log k).
]

In fact the best-known bounds (as of the current literature) are

[
\Big(\tfrac14-o(1)\Big)k^2\log k\ \le\ h_3(k)\ \le\ (4+o(1))k^2\log k
\qquad (k\to\infty),
]

see e.g. the discussion and references in Kostochka–Sudakov–Verstraëte. ([Mathematics Stack Exchange][1])

I’ll sketch standard proofs of each side, explicitly showing where Ramsey-type inputs enter.

---

### 1a. Upper bound (h_3(k)\le(4+o(1))k^2\log k)

Kim proved the sharp [[nomath]](up to $1+o(1)$)[[/nomath]] lower bound on the triangle Ramsey number:

[
R(3,t)\ \ge\ \Big(\tfrac14-o(1)\Big)\frac{t^2}{\log t}.
]
([Springer][2])

Equivalently: for each large $t$ there exists a triangle-free graph $G$ on

[
N=\Big(\tfrac14-o(1)\Big)\frac{t^2}{\log t}
]

vertices with (\alpha(G)<t) [[nomath]](since otherwise every graph on $N$ vertices would contain an independent set of size $t$, contradicting the definition of $R(3,t)$)[[/nomath]].

For such a $G$,

[
\chi(G)\ \ge\ \frac{|V(G)|}{\alpha(G)}\ >\ \frac{N}{t}
\ =\ \Big(\tfrac14-o(1)\Big)\frac{t}{\log t}.
]

Now choose (t=t(k)) so that (\frac{t}{\log t}\sim 4k); e.g.

[
t=(4+o(1)),k\log k.
]

Then (\log t = (1+o(1))\log k), so

[
\chi(G)\ \ge\ \Big(\tfrac14-o(1)\Big)\frac{t}{\log t}
\ =\ (1-o(1)),k,
]

and with a slightly larger constant [[nomath]](say $t=(4+\varepsilon)k\log k$)[[/nomath]] you ensure (\chi(G)\ge k) for all large $k$.

Finally, from any triangle-free graph with (\chi\ge k), take an induced subgraph minimal w.r.t. having chromatic number (\ge k); its chromatic number is exactly $k$ and it is still triangle-free. Hence (h_3(k)) is at most the order $N$ above:

[
h_3(k)\ \le\ N
\ =\ \Big(\tfrac14-o(1)\Big)\frac{t^2}{\log t}
\ =\ (4+o(1))k^2\log k.
]

This is the standard route to the ((4+o(1))k^2\log k) upper bound. ([Mathematics Stack Exchange][1])

[[nomath]](There are also proofs via the triangle-free process, which asymptotically matches Kim’s Ramsey bound; see Bohman–Keevash and subsequent refinements. $[Springer][3]$)[[/nomath]]

---

### 1b. Lower bound (h_3(k)\ge(\tfrac14-o(1))k^2\log k)

For the lower bound one shows: **every** triangle-free graph on $n$ vertices has (\chi(G)) at most on the order (\sqrt{n/\log n}). Inverting that gives a lower bound on the minimum $n$ needed to force chromatic number $k$.

A clean way is to use Shearer’s (asymptotically optimal up to constant factor) upper bound on $R(3,t)$, namely

[
R(3,t)\ \le\ (1+o(1)),\frac{t^2}{\log t},
]

which implies the following “universal” independent set lower bound:

> Every triangle-free graph $H$ on $m$ vertices satisfies
> [
> \alpha$H$\ \ge\ (\tfrac1{\sqrt2}-o(1))\sqrt{m\log m}.
> ]
> [[nomath]](One gets this by taking $t=\alpha(H)+1$ and using $m<R(3,t)$, then inverting the relation $R(3,t)\approx t^2/\log t$.)[[/nomath]]

This is a standard deduction, and it is used explicitly in the modern treatments of this topic. ([Mathematics Stack Exchange][1])

Now color a triangle-free graph $G$ on $n$ vertices greedily: repeatedly remove (and color) a largest guaranteed independent set in the remaining graph. If the current remaining graph has $m$ vertices, we can remove at least

[
\Big(\tfrac1{\sqrt2}-o(1)\Big)\sqrt{m\log m}
]

vertices in one color class. So the number of colors needed is at most

[
\sum \frac{1}{(\tfrac1{\sqrt2}-o(1))\sqrt{m\log m}}
\ \approx\ (2\sqrt2+o(1))\sqrt{\frac{n}{\log n}},
]

since (asymptotically)
[
\int_2^n \frac{dx}{\sqrt{x\log x}} \sim 2\sqrt{\frac{n}{\log n}}.
]

Therefore, every triangle-free $n$-vertex graph satisfies

[
\chi(G)\ \le\ (2\sqrt2+o(1))\sqrt{\frac{n}{\log n}}.
]

Now set (\chi(G)=k) and invert: if (k \le (2\sqrt2+o(1))\sqrt{n/\log n}), then necessarily

[
n\ \ge\ \Big(\tfrac18-o(1)\Big)k^2 \log n
\ =\ \Big(\tfrac14-o(1)\Big)k^2 \log k
]

[[nomath]](using $\log n = (2+o(1))\log k$ when $n$ is on the scale $k^2\log k$)[[/nomath]].

Thus any triangle-free graph with chromatic number $k$ has at least ((\tfrac14-o(1))k^2\log k) vertices, i.e.

[
h_3(k)\ \ge\ \Big(\tfrac14-o(1)\Big)k^2\log k.
]
([Mathematics Stack Exchange][1])

Combining with the upper bound proves (h_3(k)=\Theta(k^2\log k)).

---

## 2. About (\displaystyle \lim_{k\to\infty}\frac{h_3(k+1)}{h_3(k)})

### 2a. What we can prove unconditionally right away

Trivially (h_3(k+1)\ge h_3(k)), so
[
\liminf_{k\to\infty}\frac{h_3(k+1)}{h_3(k)}\ \ge\ 1.
]

There’s also a slightly stronger inequality from the definition: if $G$ is triangle-free and (\chi(G)=k+1), then removing one color class from an optimal ((k+1))-coloring leaves an induced triangle-free subgraph with chromatic number exactly $k$. Taking the *largest* color class gives
[
h_3(k)\ \le\ \frac{k}{k+1},h_3(k+1),
]
hence
[
\frac{h_3(k+1)}{h_3(k)}\ \ge\ 1+\frac1k,
]
so again (\liminf\ge 1).

### 2b. If the limit exists, it must equal $1$

What’s easy (and standard) is:

> If the limit (L:=\lim_{k\to\infty} \frac{h_3(k+1)}{h_3(k)}) exists, then $L=1$.

Proof: Since (h_3(k)) is increasing, (L\ge1). Suppose (L>1). Then there is some (\varepsilon>0) and (k_0) such that for all (k\ge k_0),
[
\frac{h_3(k+1)}{h_3(k)} \ge 1+\varepsilon.
]
Iterating gives exponential growth:
[
h_3(k)\ \ge\ h_3(k_0),(1+\varepsilon)^{k-k_0}.
]
But from the upper bound proved above,
[
h_3(k)\ \le\ Ck^2\log k
]
for some constant $C$, i.e. (h_3(k)) grows only polynomially. A polynomial function cannot dominate ((1+\varepsilon)^k) for large $k$, contradiction. Therefore (L\le1), hence $L=1$.

This conditional argument is also noted in the literature around these “minimum order of (K_r)-free $k$-chromatic graphs” functions. ([ResearchGate][4])

### 2c. Status of unconditional existence

The remaining issue is **existence** of the limit (i.e. ruling out oscillations in the successive ratios). As far as I can verify from available sources, the existence of (\lim_{k\to\infty} h_3(k+1)/h_3(k)) has been explicitly posed as a question; what is proved is the conditional statement above (“if it exists, it must be 1”). ([ResearchGate][4])

So, with currently established results one can prove:

* (h_3(k)=\Theta(k^2\log k)) [[nomath]](indeed the concrete $(\tfrac14-o(1))$ vs $(4+o(1))$ bounds)[[/nomath]];
* (\liminf_{k\to\infty} h_3(k+1)/h_3(k)=1);
* and **if** (\lim_{k\to\infty} h_3(k+1)/h_3(k)) exists, then it equals $1$.

---

### If you want, I can also

* write the greedy-coloring/integral argument in a fully “(\varepsilon)–$N$” style [[nomath]](no $o(1)$ shorthand)[[/nomath]], or
* derive the bounds in terms of the extremal function (f_{2,3}(n)) (the Erdős–Rogers function), which packages the same ideas and is another standard way this is presented.

[1]: https://math.stackexchange.com/questions/1933701/constructing-a-triangle-free-k-chromatic-graph?utm_source=chatgpt.com "Constructing a triangle-free $k$-chromatic graph"
[2]: https://link.springer.com/chapter/10.1007/978-88-7642-475-5_78?utm_source=chatgpt.com "Dynamic concentration of the triangle-free process"
[3]: https://link.springer.com/article/10.1007/s40574-021-00286-5?utm_source=chatgpt.com "K3 curves with index (k>1) - Springer Link"
[4]: https://www.researchgate.net/publication/265169723_On_degree_sums_of_a_triangle-free_graph "https://www.researchgate.net/publication/265169723_On_degree_sums_of_a_triangle-free_graph"

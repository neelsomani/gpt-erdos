A small but important normalization first: in the “difference” problem you must **exclude** $n=0$ [[nomath]](or else require $a\ne b$, equivalently $a>b$ if you only look at positive $n$)[[/nomath]], since (a-b=0) has (|B|) solutions and would force (|B|\le r), contradicting the asserted (\asymp N^{1/2}) growth.

With that understood, the two extremal problems behave quite differently.

## Differences: the constant is known, and it is (\sqrt r)

Let
[
D_r(N):=\max\\{|B|:B\subseteq [N],\ |\\{(a,b)\in B^2:\ a-b=n\\}|\le r\ \forall n\ne 0\\}.
]
This is exactly the “bounded difference-representation” extremal function (\alpha_g(n)) studied in the recent INTEGERS paper [[nomath]](their $g$ is your $r$)[[/nomath]]. They prove
[
\alpha_g(n)=(1+o_g(1))\sqrt{gn}\quad(n\to\infty),
]
i.e. for each fixed $r$,
[
D_r(N)=(1+o_r(1))\sqrt{rN}.
]
So the asymptotic constant **exists** here and is
[
c_r'=\sqrt r.
]


## Sums: for fixed (r\ge 2), even the existence of (c_r) is (essentially) open

Let
[
F_r(N):=\max\\{|A|:A\subseteq [N],\ r^**{A+A}(n):=|\\{a\le b\in A:\ a+b=n\\}|\le r\ \forall n\\}.
]
Your constant (c_r) would be (\lim*{N\to\infty}F_r(N)/\sqrt N) (if it exists).

For $r=1$ (Sidon sets) one has (F_1(N)=\sqrt N+O(1)), so (c_1=1). But for **fixed** (r\ge2), the situation is much murkier: one typically only has **bounds on (\liminf)** and **(\limsup)**, and “sums instead of differences” is explicitly flagged as substantially harder with many open problems. 

So, strictly speaking:

* (c_r') exists and equals (\sqrt r).
* The existence (and value) of (c_r) for fixed (r\ge2) is not currently settled in the literature in the same way.

## If you *assume* (c_r) exists, what can one say about comparing (c_r) and (c_r')?

Under your hypothesis (|A|\sim c_r\sqrt N), the question becomes: is (c_r) different from (\sqrt r) and in fact larger?

There is strong evidence that “sum-bounded” sets are asymptotically **denser** than “difference-bounded” sets, and in two important senses this is **provable**:

### 1) For $r=2$, known lower bounds already beat (\sqrt2)

In the ordered-representation normalization [[nomath]](common in the $g$-Sidon literature)[[/nomath]], your “unordered $r$” condition is essentially the same as “ordered $g=2r$” in (\mathbb Z) (no elements of order 2), so $r=2$ corresponds to $g=4$. ([Colgate Math][1])

For $g=4$ one has explicit constructions giving a lower bound (\beta_4\ge 4/\sqrt7\approx 1.5118) for the (\sqrt N)-constant (in the appropriate limsup sense). ([arXiv][2])
Since (\sqrt2\approx 1.4142), this shows that **if** a true asymptotic constant (c_2) exists, it cannot equal (c_2'=\sqrt2); it would have to satisfy (c_2>\sqrt2).

### 2) For large $r$, the asymptotic is known in a two-parameter limit and it forces (c_r>c_r')

Cilleruelo–Ruzsa–Vinuesa prove that, in the regime where the allowed multiplicity $g$ and the ambient size $N$ both go to infinity, the maximum size of a $g$-Sidon set in $[N]$ satisfies
[
\beta_g(N)=\sigma\sqrt{gN}(1-\varepsilon(g,N)),\qquad \varepsilon(g,N)\to0,
]
where (\sigma) is the Schinzel–Schmidt “continuous” constant, and they record bounds
[
1.1509\le \sigma \le 1.2525.
]
([arXiv][2])

Translating (g\approx 2r) for your unordered $r$, this predicts/forces [[nomath]](in that large-$r$ asymptotic regime)[[/nomath]]
[
c_r \sim \sigma\sqrt{2r} = (\sigma\sqrt2),\sqrt r,
]
so
[
\frac{c_r}{c_r'} \sim \sigma\sqrt2 \in [1.63,\ 1.77],
]
and in particular (c_r>c_r'=\sqrt r) for all sufficiently large $r$ (again: in the sense made precise by that two-parameter limit). ([arXiv][2])

## Bottom line

* **Differences:** (c_r'=\sqrt r) (proved). 
* **Sums:** for fixed (r\ge2), the existence/value of a true asymptotic constant (c_r) is not settled in the same way; this is part of a notoriously harder set of open problems. ([Colgate Math][1])
* **Comparing:** assuming (c_r) exists, then

  * for $r=2$ one already has (c_2>\sqrt2=c_2') from explicit lower bounds; ([arXiv][2])
  * and for **large $r$** one has a rigorous asymptotic regime implying (c_r/c_r'\to \sigma\sqrt2>1), so (c_r'>c_r) is **false** for large $r$ and instead (c_r'<c_r). ([arXiv][2])

What remains genuinely open is the “for every fixed (r\ge3), does (c_r) exist and is it strictly (>\sqrt r)?” aspect.

[1]: https://math.colgate.edu/~integers/z77/z77.pdf "https://math.colgate.edu/~integers/z77/z77.pdf"
[2]: https://arxiv.org/pdf/0909.5024 "https://arxiv.org/pdf/0909.5024"

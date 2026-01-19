Your $g(n)$ is the classical “finite additive 2-basis” problem (a.k.a. the order‑2 postage stamp problem): find the smallest $k$ for which some (A\subseteq{0,\dots,n}) of size $k$ satisfies
[
{0,1,\dots,n}\subseteq A+A.
]

## First-order growth: (g(n)=\Theta(\sqrt n))

### Trivial lower bound (counting sums)

If (|A|=k), then the number of *unordered* pairs $(a_i,a_j)$ with (i\le j) is (k(k+1)/2), hence
[
|A+A|\le \frac{k(k+1)}2.
]
Since ({0,\dots,n}\subseteq A+A) has size $n+1$, we must have
[
n+1 \le \frac{k(k+1)}2 \quad\Rightarrow\quad k \ge \frac{\sqrt{8n+1}-1}{2} = \sqrt{2n}+O(1).
]
So
[
g(n)\ge (1.4142\ldots+o(1))\sqrt n.
]
[[nomath]](This “$\sqrt{2n}$” bound is also explicitly noted in the modern literature on 2-bases. $[ar5iv][1]$)[[/nomath]]

### Simple upper bound ({g(n)\le 2\sqrt n+O(1)}) (Rohrbach-type construction)

Let (m=\lceil \sqrt n\rceil) and define
[
A={0,1,\dots,m}\ \cup\ {0,m,2m,\dots,\lfloor n/m\rfloor m}.
]
Then for any (x\in{0,\dots,n}), write (x=qm+r) with (0\le r\le m) and (0\le q\le \lfloor n/m\rfloor). We have (r\in{0,\dots,m}\subseteq A) and (qm\in{0,m,2m,\dots}\subseteq A), so (x=qm+r\in A+A).

The size is
[
|A|=(m+1)+(\lfloor n/m\rfloor+1)-1 = m+\lfloor n/m\rfloor+1 \le 2\lceil\sqrt n\rceil+1,
]
hence
[
g(n)\le 2\sqrt n+O(1).
]

So already:
[
\sqrt{2n}\ \lesssim\ g(n)\ \lesssim\ 2\sqrt n.
]

## Best-known asymptotic constant bounds (as of 2025/2026)

It is convenient to relate $g(n)$ to the “maximal range” function
[
n(k)=\max{,n(A): |A|=k,},
]
where $n(A)$ is the largest $n$ such that ({0,1,\dots,n}\subseteq A+A) [[nomath]](and $n+1\notin A+A$)[[/nomath]]. This is the formulation used in Kohonen’s paper. ([ar5iv][1])
Then $g(n)$ is essentially the inverse function: (g(n)=\min{k: n(k)\ge n}).

### Upper bound on $g(n)$ (explicit constructions)

Mrose (1979) constructed 2-bases with asymptotic efficiency
[
\liminf_{k\to\infty}\frac{n(k)}{k^2}\ge \frac{2}{7},
]
which translates to
[
g(n)^2 \le \frac{7}{2}n\quad\text{(up to lower order terms),}
]
i.e.
[
g(n) \le (1.8708\ldots+o(1))\sqrt n.
]
This is also exactly how the “(g(n)\sim 2\sqrt n)” guess was first disproved. ([Erdős Problems][2])

Kohonen (2017) improved Mrose’s constant by giving an explicit construction with
[
\frac{n(k)}{k^2}\ge \frac{85}{294} > 0.2891\quad\text{for arbitrarily large }k,
]
i.e. (\liminf n(k)/k^2 \ge 85/294). ([arXiv][3])
Inverting this gives
[
g(n)^2 \le \frac{294}{85}n = 3.4588235\ldots,n,
]
so
[
g(n) \le (1.85979\ldots+o(1))\sqrt n.
]
The ErdosProblems survey page records this bound in exactly this (g(n)^2\le (3.458\cdots+o(1))n) form. ([Erdős Problems][2])

### Lower bound on $g(n)$ [[nomath]](analytic upper bounds on $n(k)$)[[/nomath]]

On the other side, Yu (2015) proved (via analytic methods) an upper bound on $n(k)$ of the form
[
\limsup_{k\to\infty}\frac{n(k)}{k^2}\le 0.4585\ldots,
]
which (inverted) yields
[
g(n)^2 \ge (2.181\ldots+o(1))n,
]
i.e.
[
g(n) \ge (1.477\ldots+o(1))\sqrt n.
]
This is also summarized on the ErdosProblems page and referenced in Kohonen’s introduction. ([Erdős Problems][2])

### Current “best sandwich”

Putting these together, the best published asymptotic bounds currently quoted are:
[
(2.181\ldots+o(1))n \ \le\ g(n)^2 \ \le\ (3.458\ldots+o(1))n,
]
equivalently
[
(1.477\ldots+o(1))\sqrt n \ \le\ g(n) \ \le\ (1.860\ldots+o(1))\sqrt n.
]
([Erdős Problems][2])

## So, is ({g(n)\sim 2\sqrt n}) true?

No. It’s ruled out by explicit constructions already going back to Mrose (1979), giving (g(n)\le (1.8708\ldots+o(1))\sqrt n), and improved further by Kohonen (2017) to (g(n)\le (1.8598\ldots+o(1))\sqrt n). ([Erdős Problems][2])

## What is believed / what remains open?

What remains open is the *true* asymptotic constant: whether (g(n)/\sqrt n) converges, and if so what its limit is. In the equivalent formulation, the open core is to pin down the constant$s$ in the quadratic growth of $n(k)$ between the best known
[
0.2891\ldots \le \liminf \frac{n(k)}{k^2}\le \limsup \frac{n(k)}{k^2}\le 0.4585\ldots
]
and thereby sharpen the constants for $g(n)$. ([ar5iv][1])

[1]: https://ar5iv.org/pdf/1606.04770 "[1606.04770] An improved lower bound for finite additive 2-bases"
[2]: https://www.erdosproblems.com/791?utm_source=chatgpt.com "Erdős Problem #791"
[3]: https://arxiv.org/abs/1606.04770 "[1606.04770] An improved lower bound for finite additive 2-bases"

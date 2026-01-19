Let

[
f(n):=\min_{\substack{A\subset\mathbb Z\ |A|=n}}\ \max{|B|:B\subseteq A,\ B\ \text{sum-free}},
]

where “sum-free” means no solutions (a+b=c) with (a,b,c\in B) (repetitions allowed).

The correct linear scale is $n$, and the asymptotic constant is $1/3$:

[
f(n)=\Big(\frac13+o(1)\Big)n.
]

Here is what’s known, and why.

---

## Lower bound: always (\ge n/3) (Erdős’ argument)

[[nomath]](If $0\in A$, just ignore it; it only affects an additive constant because $0+x=x$.)[[/nomath]]

Pick (\theta\in\mathbb R/\mathbb Z) uniformly at random and define

[
B_\theta:={x\in A:\tfrac13<{\theta x}<\tfrac23},
]

where ({t}\in[0,1)) is the fractional part.

1. **(B_\theta) is sum-free.**
   If (x,y,z\in B_\theta) and (x+y=z), then in (\mathbb R/\mathbb Z) we have
   ({\theta z}={\theta x}+{\theta y}\pmod 1).
   But if ({\theta x},{\theta y}\in(1/3,2/3)), then their sum mod 1 lies in
   ((2/3,1)\cup(0,1/3)), **outside** $(1/3,2/3)$. Contradiction.
   So no (x+y=z) can occur inside (B_\theta). ([Annals of Mathematics][1])

2. **Expected size is $n/3$.**
   For each fixed nonzero integer $x$, the value ({\theta x}) is uniform on $[0,1)$ when (\theta) is uniform, so
   (\mathbb P(x\in B_\theta)=1/3). Hence (\mathbb E|B_\theta|=(1/3)|A|=n/3). Therefore some (\theta) has (|B_\theta|\ge n/3). ([Annals of Mathematics][1])

So, in particular,
[
f(n)\ \ge\ \frac{n}{3}\quad\text{(up to rounding / the possible presence of 0)}.
]

There are refinements: Alon–Kleitman show Erdős’ averaging can be pushed to (\frac13(n+1)), and Bourgain to (\frac13(n+2)) for (n>3). ([Annals of Mathematics][1])
And very recently, Bedert proved a genuinely unbounded additive improvement:
[
f(n)\ \ge\ \frac{n}{3}+c\log\log n
]
for some absolute (c>0). ([arXiv][2])

---

## Upper bound: cannot beat $(1/3+o(1))n$

Let (\sigma=\lim_{n\to\infty} f(n)/n); this limit exists because $f$ is subadditive [[nomath]](roughly $f(m+n)\le f(m)+f(n)$)[[/nomath]]. ([Annals of Mathematics][1])

Eberhard–Green–Manners (Annals of Math., 2014) proved Erdős’ conjecture that (\sigma=1/3) by constructing [[nomath]](for every $\varepsilon>0$ and all large $n$)[[/nomath]] sets $A$ of $n$ integers such that **every** subset (A'\subseteq A) of size (\ge (\frac13+\varepsilon)n) contains a triple (x+y=z). Equivalently, the largest sum-free subset has size (\le (\frac13+\varepsilon)n). ([Annals of Mathematics][1])

In the language of your $f(n)$, this yields
[
f(n)\le \frac{n}{3}+o(n).
]
([Annals of Mathematics][1])

---

## Conclusion: the best estimate

Putting the two sides together,

[
\boxed{ \ f(n)=\Big(\frac13+o(1)\Big)n\ }.
]

More finely, current results give a “sandwich” of the form
[
\frac{n}{3}+c\log\log n\ \le\ f(n)\ \le\ \frac{n}{3}+o(n),
]
with the right-hand upper bound from Eberhard–Green–Manners (2014) ([Annals of Mathematics][1]) and the left-hand improvement from Bedert (2025) ([arXiv][2]).

So the guaranteed proportion tends to $1/3$, and this is sharp.

[1]: https://annals.math.princeton.edu/wp-content/uploads/annals-v180-n2-p05-p.pdf "Sets of integers with no large sum-free subset"
[2]: https://arxiv.org/abs/2502.08624?utm_source=chatgpt.com "Large sum-free subsets of sets of integers via L^1 - math"

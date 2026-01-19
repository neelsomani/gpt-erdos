Interpret the “distance” between two edges (e={a,b}) and (f={c,d}) as
[
\operatorname{dist}(e,f):=\min{\operatorname{dist}_G(x,y):x\in{a,b},\ y\in{c,d}},
]
i.e. the length of the shortest *vertex-path* joining an endpoint of one edge to an endpoint of the other [[nomath]](so incident edges have distance $0$)[[/nomath]]. With this convention, Erdős noted (and it is standard) that the condition “no two edges are at distance (\ge t)” is equivalent to saying the **line graph** $L(G)$ has diameter at most $t$. 
So
[
h_t(d)-1=\max\\{|E(G)|:\ \Delta(G)\le d,\ \operatorname{diam}(L(G))\le t\\}.
]

## Order of magnitude

For each fixed $t$, one has
[
h_t(d)=\Theta(d^t)\qquad(d\to\infty),
]
and the best general bound currently known is
[
h_t(d)\ \le\ \frac{3}{2},d^t+1.
]
This is Theorem 6 of Cambie–Cames van Batenburg–de Joannis de Verclos–Kang $2021/22$. 
[[nomath]](They also remark the easy bound $h_t(d)\le 2d^t$. )[[/nomath]]

On the lower-bound side, for large $t$ they give an unconditional construction implying: there exists (t_0) such that for all (t\ge t_0) and infinitely many $d$,
[
h_t(d)\ \ge\ (0.629,d)^t,
]
so in particular (h_t(d)) is at least a constant [[nomath]](depending on $t$)[[/nomath]] times (d^t) for infinitely many $d$. 

Putting these together, for large $d$ [[nomath]](with $t$ fixed)[[/nomath]],
[
(0.629)^t,d^t\ \lesssim\ h_t(d)\ \le\ 1.5,d^t+1.
]

## Sharp values and best-known asymptotics for small $t$

* **$t=1$**: exactly
  [
  h_1(d)=d+1.
  ]


* **$t=2$**: this becomes the classical extremal problem for (2K_2)-free graphs (no induced pair of disjoint edges). Chung–Gyárfás–Tuza–Trotter proved the exact maximum number of edges $f(d)$ in such graphs with maximum degree $d$: ([Renyi Users][1])
  [
  f(d)=
  \begin{cases}
  \frac{5d^2}{4}, & d\ \text{even},[4pt]
  \frac{5d^2-2d+1}{4}, & d\ \text{odd},
  \end{cases}
  ]
  hence
  [
  h_2(d)=f(d)+1=
  \begin{cases}
  \frac{5d^2}{4}+1, & d\ \text{even},[4pt]
  \frac{5d^2-2d+1}{4}+1, & d\ \text{odd}.
  \end{cases}
  ]
  ([Renyi Users][1])

* **$t=3$**: there are very good constructions from projective planes. If (d=q+1) with $q$ a prime power, the point–line incidence graph of a projective plane has maximum degree $d$, line-graph diameter $3$, and
  [
  |E|=d^3-d^2+d,
  ]
  giving
  [
  h_3(d)\ \ge\ d^3-d^2+d+1\quad\text{for such }d.
  ]

  Cambie et al. conjecture the essentially tight formula
  [
  h_3(d)\le d^3-d^2+d+2,
  ]
  with equality for (d=q+1). 
  They also prove (h_3(3)=23). 

## What is believed to be the “right” answer

Cambie et al. suggest that for fixed $t$,
[
h_t(d)=(1+o(1)),d^t
]
for infinitely many $d$ (a lower-bound conjecture), and also that for (t\ne 2),
[
h_t(d)\le (1+\varepsilon),d^t
]
for all sufficiently large $d$ (an upper-bound conjecture). 

So the best current “estimate” is:

* **Proved:** (h_t(d)) grows on the scale (d^t), with the best general upper bound (h_t(d)\le \tfrac32 d^t+1). 
* **Sharp for (t=1,2)** (exact formulas above). 
* **Conjectured [[nomath]](for $t\ge 3$)[[/nomath]]:** (h_t(d)=(1+o(1))d^t) [[nomath]](at least along infinitely many $d$)[[/nomath]]. 

[1]: https://users.renyi.hu/~gyarfas/Cikkek/48_ChungGyarfasTuzaTrotter_TheMaximumNumberOfEdgesIn2K2FreeGraphsOfBoundedDegree.pdf "https://users.renyi.hu/~gyarfas/Cikkek/48_ChungGyarfasTuzaTrotter_TheMaximumNumberOfEdgesIn2K2FreeGraphsOfBoundedDegree.pdf"

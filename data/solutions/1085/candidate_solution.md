Let $U(P)$ be the number of pairs at distance $1$ in a finite set (P\subset\mathbb R^d).
Your (f_d(n)) is exactly the extremal quantity
[
f_d(n)=\max{U(P): P\subset\mathbb R^d,\ |P|=n},
]
i.e. the maximum possible number of unit distances among $n$ points.

## What is known (by dimension)

### $d=1$

[
f_1(n)=n-1.
]
[[nomath]](Place points at $0,1,2,\dots,n-1$; each point has at most one neighbor at distance $1$ to its right.)[[/nomath]]

### $d=2$ (Erdős unit distance problem — still open)

Best known bounds are
[
n^{,1+\frac{c}{\log\log n}}\ \le\ f_2(n)\ \le\ Cn^{4/3},
]
for absolute constants (c,C>0). 
The gap between the lower and upper bounds is a major open problem.

### $d=3$ (still open, but better than in the plane)

A classical lower bound is
[
f_3(n)\ \ge\ cn^{4/3}\log\log n
]
[[nomath]](for some $c>0$)[[/nomath]]. 
The best known upper bound has exponent strictly below $3/2$:
[
f_3(n)=O\left(n^{295/197+\varepsilon}\right)\quad\text{for every }\varepsilon>0,
]
where (295/197\approx 1.49746). ([OUP Academic][1])

### (d\ge 4) (asymptotically solved; quadratic)

Let
[
p=\Big\lfloor \frac d2\Big\rfloor.
]
Then
[
f_d(n)=\frac{p-1}{2p}n^2+o(n^2)\qquad(d\ge 4).
]


Equivalently, (f_d(n)) is asymptotic to the Turán number (t_p(n)) [[nomath]](the number of edges in the complete $p$-partite graph with parts as equal as possible)[[/nomath]]:
[
t_p(n)=\frac{p-1}{2p}n^2-\frac{r(p-r)}{2p},\quad r\equiv n\pmod p.
]
The matching lower bound comes from the **Lenz construction**: put points on $p$ circles of radius (1/\sqrt2) lying in pairwise orthogonal 2-planes through a common center; then any two points on different circles are at distance $1$, giving about (\frac{p-1}{2p}n^2) unit pairs. 
The matching upper bound uses that certain complete multipartite graphs cannot occur as unit-distance graphs in (\mathbb R^d) and then applies the Erdős–Stone theorem, yielding the same leading term. 

#### Refinements for (d\ge 4)

* **$d=4$** [[nomath]](exact for all $n\ge 5$)[[/nomath]]:
  [
  f_4(n)=
  \begin{cases}
  \big\lfloor n^2/4\big\rfloor+n, & n\equiv 0\pmod 8\ \text{or}\ 0\pmod{10},[2mm]
  \big\lfloor n^2/4\big\rfloor+n-1, & \text{otherwise}.
  \end{cases}
  ]


* **Even (d\ge 6)**: for all sufficiently large $n$ [[nomath]](depending on $d$)[[/nomath]], (f_d(n)) is known **exactly**; in particular it is
  [
  f_d(n)=t_p(n)+n+O_d(1),
  ]
  with an explicit piecewise correction depending on (n\bmod 2d). 

* **Odd (d\ge 5)**: one can improve the Lenz construction by replacing one circle by a 2-sphere, gaining an extra (\Theta(n^{4/3})) unit pairs, and in fact
  [
  f_d(n)=\frac{p-1}{2p}n^2+\Theta(n^{4/3})\qquad(d\ \text{odd}\ge 5).
  ]


## Summary “estimate”

* (f_1(n)=n-1).
* (f_2(n)) is between (n^{1+c/\log\log n}) and $O(n^{4/3})$ (open). 
* (f_3(n)) is between (\Omega(n^{4/3}\log\log n)) and $O(n^{295/197+\varepsilon})$ (open). 
* For (d\ge 4), (f_d(n)=\left(\frac12-\frac{1}{2\lfloor d/2\rfloor}\right)n^2+o(n^2)), i.e. $\Theta(n^2)$, with sharper formulas known in many cases. 

[1]: https://academic.oup.com/imrn/article-abstract/2019/20/6235/4825264 "Breaking the 3/2 Barrier for Unit Distances in Three Dimensions | International Mathematics Research Notices | Oxford Academic"

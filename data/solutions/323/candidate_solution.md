Write
[
f_{k,m}(x)=|\\{n\le x:\ n=a_1^k+\cdots+a_m^k\ \text{for some }a_i\in\mathbb Z_{\ge 0}\\}|.
]

## The case $m=k$

* **$k=2$**: yes. Landau (1908) proved the classical asymptotic for sums of two squares:
  [
  f_{2,2}(x)\sim C,\frac{x}{\sqrt{\log x}}
  \qquad (x\to\infty),
  ]
  for an explicit constant (C>0). 
  In particular, since (x/\sqrt{\log x}\gg_\varepsilon x^{1-\varepsilon}) for every (\varepsilon>0), your bound holds for ((k,m)=(2,2)).

* **(k>2)**: **open**. In fact, for (k>2) it is not even known whether (f_{k,k}(x)=o(x)) [[nomath]](i.e. whether the set of sums of $k$ $k$th powers has density $0$)[[/nomath]]. ([Erdős Problems][1])
  So the much stronger lower bound (f_{k,k}(x)\gg_\varepsilon x^{1-\varepsilon}) is currently out of reach in general.

* **Example $k=3$** (three cubes): the best general lower bounds known are far from (x^{1-\varepsilon}). Wooley proved that the number of integers (\le X) representable as a sum of three **positive** cubes satisfies
  [
  N(X)\gg X^{0.91709477}.
  ]

  Allowing $0$ as a cube can only increase the count, so this is also a lower bound for (f_{3,3}(X)), but it is still well below the (X^{1-\varepsilon}) threshold.

**So:** the statement is **true for $k=2$** and **open for every (k\ge 3)** (indeed, very open).

## The case (m<k)

Here the “expected” order of magnitude is (x^{m/k}) because the summands are (\le x^{1/k}), so there are (\asymp x^{m/k}) available $m$-tuples; the issue is collisions (distinct tuples giving the same sum).

What is known depends strongly on $m$:

* **$m=1$**: trivial and sharp, (f_{k,1}(x)=\lfloor x^{1/k}\rfloor+1\asymp x^{1/k}).

* **$m=2$**: **yes** (and much more is known in many cases).
  Erdős–Mahler showed that (\nu_k(N)) [[nomath]](the number of integers $\le N$ representable as a sum of two $k$th powers)[[/nomath]] satisfies
  [
  \nu_k(N)\gg N^{2/k},
  ]
  which is exactly your desired lower bound for (f_{k,2}(x)). 
  Moreover, for (h>3), Hooley proved an asymptotic formula
  [
  \nu_h(N)=\frac{\Gamma(1+1/h)^2}{2,\Gamma(1+2/h)},N^{2/h}+O!\left(N^{5/(3h)+\varepsilon}\right),
  ]
  showing that (f_{h,2}(x)) is actually (\asymp x^{2/h}) in that range. 

* **(m\ge 3)**: **open in general**.
  Already for $m=3$ the natural analogue
  [
  f_{k,3}(x)\stackrel{?}{\gg} x^{3/k}
  ]
  is an explicit open Erdős–Graham problem. ([Erdős Problems][2])
  Since your second question asks for this bound for *all* (m<k), it is currently **unknown** beyond $m=2$ [[nomath]](and trivial $m=1$)[[/nomath]].

## Summary

* (f_{k,k}(x)\gg_\varepsilon x^{1-\varepsilon}):

  * **true for $k=2$** [[nomath]](Landau’s $x/\sqrt{\log x}$ asymptotic)[[/nomath]]. 
  * **open for all (k\ge 3)**; in fact even (f_{k,k}(x)=o(x)) is unknown for (k>2). ([Erdős Problems][1])
  * best known for three cubes is only (f_{3,3}(X)\gg X^{0.91709477}) (via Wooley). 

* If (m<k), (f_{k,m}(x)\gg x^{m/k}):

  * **true for $m=1$** (trivial) and **true for $m=2$** [[nomath]](Erdős–Mahler; and Hooley gives asymptotics for $k>3$)[[/nomath]]. 
  * **open for (m\ge 3)** in general; in particular the case $m=3$ is open. ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/323 "
  
    Erdős Problem #323
  
"
[2]: https://www.erdosproblems.com/tags/powers/open "
  
    Erdős Problems
  
"

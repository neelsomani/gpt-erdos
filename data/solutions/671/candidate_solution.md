Let
[
\Lambda_n(x):=\sum_{i=1}^n |p_i^n(x)|
]
be the **Lebesgue function** [[nomath]](the operator norm of the linear functional $f\mapsto \mathcal L^n f(x)$ on $C[-1,1]$)[[/nomath]].

## 1) Existence with “bad” Lebesgue growth at some point but convergence there [[nomath]](for each $f$)[[/nomath]]

**Yes.** Erdős explicitly stated that one can construct a triangular array ({a_i^n}) with the property that

* for **every** continuous $f$, there are **continuum many** points (x_0\in[-1,1]) such that
  [
  \lim_{n\to\infty}\Lambda_n(x_0)=\infty
  ]
  [[nomath]](in particular, $\limsup_{n\to\infty}\Lambda_n(x_0)=\infty$)[[/nomath]],
* yet nevertheless
  [
  \mathcal L^n f(x_0)\to f(x_0)\quad (n\to\infty).
  ]

This is stated in Erdős’ 1958 paper *Problems and results on the theory of interpolation. I* (see the paragraph beginning “On the other hand … I can construct a point group …”). ([Renyi Institute][1])

So your **first** question has an affirmative answer [[nomath]](and in fact with $\lim\Lambda_n(x_0)=\infty$, which is stronger than your $\limsup$)[[/nomath]].

## 2) Existence with (\limsup\Lambda_n(x)=\infty) for every $x$, but still a convergence point for each $f$

This **stronger** version appears to be **open** in the literature.

* Already in the same 1958 note, Erdős writes that **if** condition (\lim\Lambda_n(x_0)=\infty) holds for **every** (x_0\in[-1,1]), then he “cannot decide” whether there must exist a continuous $f$ whose Lagrange interpolants diverge at **every** point. ([Renyi Institute][1])
  [[nomath]](That is closely tied to your second question: if such an everywhere-divergent $f$ must exist under $\Lambda_n(x)\to\infty\ \forall x$, then your desired “for every $f$ there is some $x$ with $\mathcal L^n f(x)\to f(x)$” would fail.)[[/nomath]]

* Modern compilations still list the two-part question in essentially your formulation as an open Erdős problem (#671 on the Erdős Problems site, last edited Dec 2025). ([Erdős Problems][2])

What *is* known (to give context) is that one cannot hope for “good behavior” in general:

* Bernstein proved that **for any** choice of nodes there is at least one point (x_0) with (\limsup_{n\to\infty}\Lambda_n(x_0)=\infty). ([Erdős Problems][2])
* Erdős–Vértesi proved that **for any** node array there exists a continuous $f$ such that (\mathcal L^n f(x)) diverges [[nomath]](in $\limsup$ sense)[[/nomath]] for almost every $x$. ([Erdős Problems][2])
* And for some *specific* “good” arrays (e.g. Chebyshev zeros), one can even get continuous functions whose Lagrange interpolants have (\limsup=\infty) at **every** point $x$, so then there is no convergence point at all for that $f$. 

So:

* **First question:** **Yes** (Erdős gives such an array). ([Renyi Institute][1])
* **Second question:** I did not find a definitive resolution; it is presented as **open** in the classical source and in current problem lists. ([Renyi Institute][1])

[1]: https://old.renyi.hu/~p_erdos/1958-14.pdf "https://old.renyi.hu/~p_erdos/1958-14.pdf"
[2]: https://www.erdosproblems.com/latex/671 "
  
    Erdős Problems
  
"

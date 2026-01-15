This is **open** (it is an Erdős problem). ([Erdős Problems][1])

What we *can* prove is an “almost linear” lower bound.

### What is known

Let (D=\mathrm{diam}(A)), and let
[
d_1<d_2<\cdots<d_t
]
be the **distinct** distances that occur among pairs of points in $A$.
Your gap condition says (d_{i+1}-d_i\ge 1), and you also have (d_1\ge 1).
So
[
d_t ;\ge; 1+(t-1)\cdot 1 ;=; t.
]
But (d_t\le D). Hence
[
D \ge t.
]

Now use the Guth–Katz theorem on distinct distances: **any** $n$ points in the plane determine at least (\gtrsim \dfrac{n}{\log n}) distinct distances. ([annals.math.princeton.edu][2])
So (t \gtrsim \dfrac{n}{\log n}), and therefore
[
\mathrm{diam}(A)=D ;\gtrsim; \frac{n}{\log n}.
]

### What is *not* known

The question you asked is whether (D \gg n) (a true linear bound $cn$).
This is **not proved** at present. It is conjectured to be true, and Erdős even suggested it might be (\ge n-1) for all large $n$. 

But it is **not** true for *all* $n$: Piepmeyer gave an example with $n=9$ and diameter $<5$. ([IME-USP][3])

So the current situation is:

* Easy construction gives (D \le n-1) (put the points on a line at unit steps).
* Best general lower bound known is (D \gtrsim n/\log n). ([annals.math.princeton.edu][2])
* Whether one can improve this to (D \gg n) is open. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/100 "

    Erdős Problem #100 - Discussion thread

"
[2]: https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p02-p.pdf "On the Erdos distinct distances problem in the plane"
[3]: https://www.ime.usp.br/~yoshi/resenhas/abstracts/Erdos.pdf "resenhas_up.dvi"

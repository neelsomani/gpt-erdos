This is **open**.

If we write (A(n):=|\\{m:\varphi(m)=n\\}|), then your (g(n)=A(n)). What you are asking is whether

[
\forall \varepsilon>0,\ \text{infinitely many }n\ \text{satisfy }A(n) > n^{,1-\varepsilon},
]

i.e. whether the multiplicity of totients can be as large as (n^{1-o(1)}).

### What is known

* Erdős proved long ago that **some fixed positive exponent** is achievable: there are infinitely many totients $n$ with (A(n) > n^{c}) for some (c>0).
* Erdős also **conjectured** that the exponent can be taken **arbitrarily close to $1$** (equivalently, your statement holds). Ford’s paper explicitly states this conjecture in exactly this “(c<1) admissible” form. 

### Best unconditional exponent to date

The best currently available unconditional result does **not** reach (1-\varepsilon) for arbitrary (\varepsilon), but it does give a substantial power:

* Lichtman (2022) proves there are infinitely many totients $m$ such that (m=\varphi(n)) has at least (m^{0.7156}) solutions $n$, i.e.
  [
  A(m)\ \ge\ m^{0.7156}
  ]
  for infinitely many $m$. 
  [[nomath]](This improves the earlier “record” exponent $0.7039$ mentioned by Ford. )[[/nomath]]

So at present we know
[
\limsup_{n\to\infty}\frac{\log A(n)}{\log n}\ \ge\ 0.7156\ldots
]
but whether this limsup equals $1$ (which is what your question asks) is **still unknown**.

### Bottom line

* **Unproved / open.**
* **Conjecturally yes** (Erdős’s conjecture). 
* **Best unconditional progress:** infinitely many $n$ have (g(n)=A(n)\ge n^{0.7156}). 

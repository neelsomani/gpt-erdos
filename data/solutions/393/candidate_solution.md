Write the factors as
[
n!=a_1a_2\cdots a_t,\qquad a_1<\cdots<a_t=a_1+m,
]
so $f(n)$ is the **minimum possible width** (m=a_t-a_1) of an interval that contains a set of **distinct** divisors of $n!$ whose product is $n!$.

A convenient reformulation is: (f(n)\le m) iff there exist an integer $x$ and a subset (S\subseteq{0,1,\dots,m}) with (0,m\in S), (|S|\ge 2), such that
[
n! = \prod_{s\in S}(x+s).
]
So for each fixed $m$, you are asking whether a factorial can be represented as a value of one of finitely many “shifted product” polynomials (\prod_{s\in S}(X+s)) [[nomath]](degree between $2$ and $m+1$)[[/nomath]].

## What is known (and what is open)

This question goes back to Erdős–Graham and is explicitly listed as an **open** Erdős problem (#393). ([Erdős Problems][1])

### Basic bounds

* Trivially (f(n)\le n-2) for (n\ge 3), because
  [
  n!=2\cdot 3\cdots n
  ]
  uses distinct factors in $[2,n]$ so (m=n-2). (This is also noted in the OEIS entry.) ([OEIS][2])
* Of course (f(n)\ge 1) by definition.

### Even (f(n)=1) infinitely often is unknown

Erdős and Graham already remarked they **do not know** whether (f(n)=1) happens infinitely often, i.e. whether
[
n!=a(a+1)
]
has infinitely many solutions. ([Erdős Problems][1])

### For any fixed $m$, the event (f(n)=m) is very rare

Let (F_m(N)=|\\{n\le N: f(n)=m\\}|). Then:

* **Density zero (Berend–Osgood).** For each fixed $m$, (F_m(N)=o(N)). ([Erdős Problems][1])
  Equivalently: for any fixed $M$,
  [
  |\\{n\le N: f(n)\le M\\}|=o(N),
  ]
  so (f(n)\to\infty) **in density** [[nomath]](i.e. “for almost all $n$”)[[/nomath]].

* **Power saving (Bui–Pratt–Zaharescu, 2023).** They prove a general bound for polynomial–factorial equations (n!=P(x)) [[nomath]](degree $\ge2$)[[/nomath]]: in dyadic ranges $[N,2N)$, the number of solutions $n$ is (\ll N^{33/34}). ([Oxford University Research Archive][3])
  Applying this to the finitely many polynomials (\prod_{s\in S}(X+s)) coming from a fixed $m$ gives
  [
  F_m(N)\ll_m N^{33/34},
  ]
  as stated on the Erdős-problems page. ([Erdős Problems][1])

So, unconditionally, **every fixed value of $f(n)$** occurs with **zero asymptotic density**, and we even have a quantitative sparsity bound.

### Conditional on ABC: (f(n)\to\infty) (true divergence)

Luca proved that the **ABC conjecture** implies: for any fixed integer polynomial $P$ of degree (\ge2), the equation
[
P(x)=n!
]
has only **finitely many** integer solutions $(x,n)$. 
Since for each fixed $m$ there are only finitely many polynomials (\prod_{s\in S}(X+s)), this implies (under ABC) that for every fixed $m$, only finitely many $n$ satisfy (f(n)\le m). In particular,
[
\text{(ABC)}\quad f(n)\longrightarrow\infty.
]
This implication is also recorded on the Erdős-problems page. ([Erdős Problems][1])

## Numerical data

Exact computed values are tabulated in OEIS sequence A388302. ([OEIS][2])
The beginning [[nomath]](from $n=2$)[[/nomath]] is
[
1,1,2,2,2,2,4,6,7,6,9,9,9,12,14,12,15,\dots
]
and examples include [[nomath]](for $n=8$)[[/nomath]] a witness for (f(8)=4):
[
8!=12\cdot14\cdot15\cdot16
]
[[nomath]](with $16-12=4$)[[/nomath]]. ([OEIS][2])
Empirically (at least for the computed range), $f(n)$ tends to grow and is often on the order of $n$, but there is **no proved asymptotic** matching that observation.

## Bottom line

* The precise asymptotic growth of $f(n)$ is **open**. ([Erdős Problems][1])
* What *is* known is largely “distributional”:

  * For each fixed $m$, (f(n)=m) happens rarely: (F_m(N)=o(N)) and even (F_m(N)\ll_m N^{33/34}). ([Erdős Problems][1])
  * Under ABC, (f(n)\to\infty). 
* It is unknown even whether (f(n)=1) occurs infinitely often. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/393 "
  
    Erdős Problem #393
  
"
[2]: https://oeis.org/A388302 "A388302 - OEIS"
[3]: https://ora.ox.ac.uk/objects/uuid%3A0df29972-974c-4109-914e-5955d4399e68/files/r9c67wn78x "Power savings for counting solutions to polynomial-factorial equations"

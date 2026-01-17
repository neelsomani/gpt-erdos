This is the classical **Turán tetrahedron problem** [[nomath]](also called Turán’s $(3,4)$-problem)[[/nomath]]. **The exact value of**
[
\mathrm{ex}_3(n,K_4^3)
]
**is not known in general** (and in particular its asymptotic density is still open). ([Mathematical Institute][1])

## What is known

It is standard to define the **Turán density**
[
\pi(K_4^3):=\lim_{n\to\infty}\frac{\mathrm{ex}_3(n,K_4^3)}{\binom{n}{3}},
]
and the main open conjecture is that (\pi(K_4^3)=5/9). ([Combinatorics.org][2])

### Lower bound: Turán’s construction [[nomath]](density $5/9$)[[/nomath]]

Turán’s explicit construction is:

* Partition the $n$ vertices into **three parts** (V_0,V_1,V_2) as equally as possible.
* Declare a triple to be an edge if it is either

  1. **transversal**: one vertex in each of (V_0,V_1,V_2), or
  2. of **cyclic type**: two vertices in (V_i) and one vertex in (V_{i+1}) [[nomath]](indices mod $3$)[[/nomath]]. ([Mathematical Institute][1])

Keevash’s survey records that this gives a (K_4^3)-free 3-graph and yields the lower bound (\pi(K_4^3)\ge 5/9). ([Mathematical Institute][1])

If (|V_0|=a, |V_1|=b, |V_2|=c), then the number of edges in this construction is
[
abc+\binom{a}{2}b+\binom{b}{2}c+\binom{c}{2}a.
]

In particular, for the balanced cases (n=3m,3m+1,3m+2) (with parts as equal as possible), this evaluates to:

* **(n=3m):**
  [
  e(T_n)=\frac{m^2(5m-3)}{2}
  \quad\text{(equivalently } \binom{3m}{3}-m(m-1)(2m-1)\text{)}.
  ]
* **(n=3m+1):**
  [
  e(T_n)=\frac{m(5m^2+2m-1)}{2}.
  ]
* **(n=3m+2):**
  [
  e(T_n)=\frac{m(m+1)(5m+2)}{2}.
  ]

So, for every $n$,
[
\mathrm{ex}_3(n,K_4^3)\ \ge\ e(T_n),
]
and asymptotically (e(T_n)=(5/9+o(1))\binom{n}{3}). ([Mathematical Institute][1])

### Conjecture (still open)

Turán conjectured that this construction is asymptotically optimal:
[
\pi(K_4^3)=\frac{5}{9}
\quad\Longleftrightarrow\quad
\mathrm{ex}_3(n,K_4^3)=\Bigl(\frac59+o(1)\Bigr)\binom{n}{3}.
]
([Combinatorics.org][2])

A major complication is that there are **many non-isomorphic (K_4^3)-free constructions** achieving asymptotic density $5/9$, so the problem is believed to be **non-stable**, which makes it particularly hard. ([Combinatorics.org][2])

### Best known upper bounds

The best published asymptotic upper bounds are obtained via flag algebras. Keevash’s survey quotes:

* an older upper bound of Chung–Lu:
  [
  \pi(K_4^3)\le \frac{3+\sqrt{17}}{12}\approx 0.593592,
  ]
* and a flag-algebra-based bound around
  [
  \pi(K_4^3)\lesssim 0.561666.
  ]
  ([Mathematical Institute][1])

Baber later reported an improved flag-algebra upper bound
[
\pi(K_4^3)\le 0.5615.
]
([arXiv][3])

Putting this together, the best “headline” asymptotic bounds currently are
[
\frac{5}{9}\ \le\ \pi(K_4^3)\ \le\ 0.5615,
]
so for large $n$,
[
\Bigl(\frac{5}{9}\Bigr)\binom{n}{3}
\ \le
\mathrm{ex}_3(n,K_4^3)
\ \le
(0.5615+o(1))\binom{n}{3}.
]
([Mathematical Institute][1])

---

If you want, I can also (a) write out a short proof sketch that Turán’s construction is (K_4^3)-free, or (b) compute (e(T_n)) explicitly for your specific $n$ and compare it to the best known upper bound.

[1]: https://people.maths.ox.ac.uk/keevash/papers/turan-survey.pdf "https://people.maths.ox.ac.uk/keevash/papers/turan-survey.pdf"
[2]: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i3p40/pdf/ "https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i3p40/pdf/"
[3]: https://arxiv.org/abs/1201.3587?utm_source=chatgpt.com "Turán densities of hypercubes"

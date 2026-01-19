This is a famous open problem in additive number theory.

Your condition says that the sequence
[
A={f(0),f(1),f(2),\dots}
]
has **distinct pairwise sums** $f(a)+f(b)$ for all (a<b). In the standard language, this asks whether the values of some **integer-coefficient polynomial** can form a **Sidon set / (B_2)-sequence** [[nomath]](in the “$a<b$” sense)[[/nomath]]. ([Wikipedia][1])

### What is known

* **No linear polynomial works** (trivially): if (f(n)=\alpha n+\beta), then
  [
  f(a)+f(b)=\alpha(a+b)+2\beta
  ]
  depends only on $a+b$, so many different pairs $(a,b)$ give the same sum.

* **No quadratic polynomial works**, and in fact it is “easy to show” that neither linear nor quadratic integer polynomials generate such a Sidon set. ([Erdős Problems][2])

* **No cubic polynomial works**, by a theorem of Dubickas and Novikas: they prove that for every (f\in\mathbb Z[x]) of degree (\le 3), there are infinitely many solutions in **pairwise distinct** positive integers (m,n,r,s) of
  [
  f(m)+f(n)=f(r)+f(s),
  ]
  so collisions among (a<b) sums are unavoidable. ([ResearchGate][3])

### What remains open

As of the latest references available (including the Erdős Problems Project entry for this exact question), it is **not known** whether **any** integer-coefficient polynomial of degree (\ge 4) can have this property. In particular, it’s stated that it is not known even whether a **quartic** polynomial can generate a Sidon set of values. ([Erdős Problems][2])

### Near-miss results and conjectural candidates

* Ruzsa proved an “almost polynomial” result: there exists a real (\xi\in[0,1]) and (n_0) such that
  [
  \\{n^5+\lfloor \xi n^4\rfloor : n\ge n_0\\}
  ]
  is a Sidon set. This is extremely close to a degree-5 polynomial, but it is **not** a polynomial with integer coefficients because of the floor and the irrational (\xi). ([Erdős Problems][2])

* Erdős and Graham suggested that “probably” (f(x)=x^5) should work, but this is unproved; it ties into deeper conjectures about equal sums of like powers. ([Erdős Problems][2])

So the honest answer is:

**No such polynomial is known, and existence is currently an open problem.**

[1]: https://en.wikipedia.org/wiki/Sidon_sequence?utm_source=chatgpt.com "Sidon sequence"
[2]: https://www.erdosproblems.com/forum/thread/324 "

    Erdős Problem #324 - Discussion thread

"
[3]: https://www.researchgate.net/publication/355071036_No_cubic_integer_polynomial_generates_a_Sidon_sequence?utm_source=chatgpt.com "No cubic integer polynomial generates a Sidon sequence"

This is **not known** at the moment.

Your condition is exactly what people call a **(B_3)** sequence (a “3‑Sidon set”): all sums (a+b+c) (with order ignored) are different. Erdős asked this as a specific open problem (it is listed as **open** on the Erdős Problems site). ([Erdős Problems][1])

A common equivalent way to say it is: if (A={a_1<a_2<\cdots}), does one always have
[
\limsup_{n\to\infty}\frac{a_n}{n^3}=+\infty ?
]
Erdős stated this “(\limsup a_n/n^3=\infty)” version and offered a prize for it. ([IME-USP][2])
(And this is equivalent to your (\liminf |A\cap[1,N]|/N^{1/3}=0) by the usual inversion between (a_n) and the counting function.)

What *is* known:

* For **pairwise sums** (the (B_2) / Sidon case), Erdős proved the analogous statement:
  [
  \liminf_{N\to\infty}\frac{|A\cap[1,N]|}{N^{1/2}}=0.
  ]
  ([Erdős Problems][1])

* Erdős also asked the general question for all (h\ge 2). It is known for **even (h)**: proved for (h=4) by Nash and for all even (h) by Chen. ([Erdős Problems][1])

* For (h=3) there are **partial obstructions**: Helm proved you cannot have a “nice” asymptotic (A(N)\sim \alpha N^{1/3}) for any constant (\alpha>0), so the ratio cannot settle down to a positive limit. 
  But that still does **not** force the liminf to be (0), so it does not settle the question.

So the honest answer is: **open problem; Erdős conjectured “yes”**, but no proof (or counterexample) is known. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/41 "
  
    Erdős Problem #41
  
"
[2]: https://www.ime.usp.br/~yoshi/resenhas/abstracts/Erdos.pdf "resenhas_up.dvi"

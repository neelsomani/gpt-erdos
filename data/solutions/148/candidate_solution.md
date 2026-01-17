Let

[
F(k)=#\\{(n_1,\dots,n_k): 1\le n_1<\cdots<n_k,;;1=\sum_{i=1}^k \frac1{n_i}\\}.
]

This is a well-studied counting function (it is OEIS A006585). ([OEIS][1])

### Small values (to show the scale)

For (k=1,\dots,8),

[
F(1)=1,F(2)=0,F(3)=1,F(4)=6,;F(5)=72,F(6)=2320,F(7)=245765,F(8)=151182379.
]
([OEIS][1])

So $F(k)$ grows extremely fast once $k$ is a bit large.

---

## Best known general bounds [[nomath]](as $k\to\infty$)[[/nomath]]

The currently best published bounds (in this “distinct denominators, ordered” setting) are

[
2^{c^{\frac{k}{\log k}}}\ \le\ F(k)\ \le\ c_0^{\left(\frac15+o(1)\right)2^k}
]
where (c>0) is an absolute constant and
[
c_0=1.26408\ldots
]
is the **Vardi constant**. ([Erdős Problems][2])

These are due to:

* **Lower bound**: Konyagin (2014). ([Erdős Problems][2])
* **Upper bound**: Elsholtz–Planitzer (2021). ([Erdős Problems][2])

A clean way to read these bounds is by taking logs twice.

### What they say in “growth language”

Write (L(k)=\log\log F(k)) (natural logs). Then the bounds imply

[
L(k)\ \ge\ \Omega!\left(\frac{k}{\log k}\right)
\quad\text{and}\quad
L(k)\ \le\ (\log 2 + o(1)),k.
]

So $F(k)$ is **doubly exponential** in $k$, but we do not know the true size of the exponent in (\log\log F(k)): it sits somewhere between order (k/\log k) and order $k$. ([Erdős Problems][2])

Equivalently, you can rewrite the upper bound as

[
F(k)\ \le\ \exp\left(\left(\frac{\log c_0}{5}+o(1)\right)2^k\right),
]

so the upper bound is of the form (\exp(C2^k)) up to lower-order factors. ([Erdős Problems][2])

---

## A short “why these shapes happen” (intuition)

* The **lower bound** comes from “splitting” one unit fraction in many different ways, using denominators with lots of divisors; each split creates many new valid representations, and you can iterate this to make the number of representations explode. (This is the core idea behind Konyagin’s construction.) ([Erdős Problems][2])
* The **upper bound** comes from strong constraints on how big the denominators can be in any solution, which limits the search space; Elsholtz–Planitzer sharpen this counting for the last few terms and get the (\tfrac15) in the exponent. ([Erdős Problems][2])

---

## Bottom line estimate

The best “headline estimate” you can safely quote today is:

[
\boxed{\exp(\exp(\Omega(k/\log k)))\ \le\ F(k)\ \le\ \exp(O(2^k))}
]

or, in the more explicit standard form,

[
\boxed{2^{c^{k/\log k}}\ \le\ F(k)\ \le\ c_0^{(\frac15+o(1))2^k}}.
]
([Erdős Problems][2])

If you want, I can also rewrite these bounds into “number of digits of $F(k)$” form [[nomath]](it becomes a very simple multiple of $2^k$ on the upper side)[[/nomath]], or sketch a concrete branching construction that produces the lower bound idea in a hands-on way.

[1]: https://oeis.org/A006585 "A006585 - OEIS"
[2]: https://www.erdosproblems.com/latex/148 "https://www.erdosproblems.com/latex/148"

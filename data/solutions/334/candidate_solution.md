Let (P^{+}(m)) denote the largest prime factor of $m$ [[nomath]](with $P^{+}(1)=1$)[[/nomath]].
Your question asks for the smallest possible function $f(n)$ [[nomath]](as $n\to\infty$)[[/nomath]] such that for every $n$ there exist integers (a,b\ge 1) with
[
n=a+b,\qquad P^{+}(a)\le f(n),\ \ P^{+}(b)\le f(n),
]
i.e. $a$ and $b$ are $f(n)$-smooth.

## What is known (best current general upper bound)

The true optimal order of magnitude of $f(n)$ is **not known**. The best general theorem currently available is due to **A. Balog (1989)**:

There is a constant
[
\alpha_0=\frac{4}{9\sqrt e}=0.2695\ldots
]
such that for every (\varepsilon>0), every sufficiently large integer $N$ can be written as
[
N=n_1+n_2
]
with both (n_1,n_2) being (N^{\alpha_0+\varepsilon})-smooth. Equivalently,
[
f(N)\ \ll_{\varepsilon}\ N^{\alpha_0+\varepsilon}.
]
This exponent (\alpha_0\approx 0.2695) is still the record. ([erdosproblems.com][1])

So, the **best currently proved** “smooth Goldbach” function is essentially
[
f(n)=n^{0.2695+o(1)}.
]

[[nomath]](If you insist on *all* $n$, not just large $n$, you can always patch finitely many small cases by enlarging $f(n)$ there; asymptotically the statement above is the substantive part.)[[/nomath]]

## What is conjectured

It is widely believed that $f(n)$ should be **much smaller** than any fixed power of $n$; for example that one could take
[
f(n)\le n^{o(1)}\quad\text{(perhaps even }f(n)\le \exp(O(\sqrt{\log n}))\text{).}
]
This is explicitly stated as the expected truth in discussions of the Erdős problem. ([erdosproblems.com][1])

But **no proof** anywhere near (n^{o(1)}) is known.

## A serious barrier: least quadratic non-residue

There is also a well-known obstruction to pushing the exponent too low by current methods.

Ben Green (following a remark attributed to Wooley) notes: if (p\equiv 3 \pmod 4) is prime and
[
p = a+b
]
with $a,b$ both (p^\varepsilon)-smooth, then one can deduce the existence of a **quadratic non-residue mod (p)** of size (\le p^\varepsilon). Thus, proving the statement “for all (\varepsilon>0), every large (p\equiv 3\ (\mathrm{mod}\ 4)) is a sum of two (p^\varepsilon)-smooth numbers” would be at least as hard as Vinogradov’s (notoriously difficult) problem on the least quadratic non-residue. The best unconditional exponent known for the least quadratic non-residue is (1/(4\sqrt e)). 

So major improvements towards (f(n)=n^\varepsilon) for arbitrarily small (\varepsilon) run into deep territory.

## For comparison: with three summands it’s much easier

If you allow **three** smooth summands, there is a much stronger result of Balog–Sárközy (1984): every (N) is a sum of three (L(N)^{3+o(1)})-smooth numbers, where
[
L(N)=\exp\big(\sqrt{\log N\log\log N}\big).
]
([SLMath][2])
This highlights how much harder the two-summand case is.

---

### Bottom line

* The **optimal** $f(n)$ is **unknown**.
* The **best proved** bound is
  [
  f(n)\ll_\varepsilon n^{\frac{4}{9\sqrt e}+\varepsilon}\quad\text{for all }\varepsilon>0,
  ]
  i.e. exponent (0.2695\ldots), due to Balog (1989). ([erdosproblems.com][1])
* It is **conjectured** that $f(n)$ could be (n^{o(1)}) (much smaller than any power), but this is open and linked to deep problems like least quadratic non-residues. ([erdosproblems.com][1])

If you tell me whether you want (i) “best known unconditional theorem”, (ii) “best conjectured order”, or (iii) “best possible under GRH/other hypotheses”, I can tailor the discussion to that version.

[1]: https://www.erdosproblems.com/tags/number%20theory "
  
    Erdős Problems
  
"
[2]: https://library.slmath.org/books/Book44/files/09andrew.pdf "https://library.slmath.org/books/Book44/files/09andrew.pdf"

Let
[
a_n=\big\lfloor t,\alpha^n\big\rfloor\qquad (n=1,2,3,\dots)
]
and let (\Sigma) be the set of all **finite sums of distinct terms** (a_{n_1}+\cdots+a_{n_k}) (distinct indices). The sequence is **complete** if every sufficiently large integer lies in (\Sigma).

A full classification is **not yet known** in complete generality, but the situation is now largely mapped out. The current state (combining classical work of Graham and more recent progress reported by Woett) is:

## Trivial growth regimes

* **(0<\alpha<1):** (a_n\to 0), so the sequence is bounded and **not complete** for any (t>0). ([Erdős Problems][1])
* **(\alpha=1):** (a_n=\lfloor t\rfloor) is constant. It is **complete iff** (\lfloor t\rfloor=1), i.e.
  [
  1\le t<2.
  ]
  (Then you have infinitely many 1’s to sum.) ([Erdős Problems][1])

## Fast growth regimes

* **(\alpha>2):** **never complete** for any (t>0). Intuitively, the next term eventually exceeds the total of all previous terms (large gaps are forced). ([Erdős Problems][1])

* **(\alpha=2):** **complete iff**
  [
  t=\frac1{2^k}\quad\text{for some }k\ge 1.
  ]
  [[nomath]](Then the tail of the sequence is exactly $1,2,4,8,\dots$, giving binary representation of all large integers.)[[/nomath]] ([Erdős Problems][1])
  *Indexing note:* if you instead start at (n=0), the condition becomes (t=2^{-k}) for (k\ge 0).

## The “interesting” range (1<\alpha<2)

Let (\varphi=\frac{1+\sqrt5}{2}\approx1.618) and (5^{1/3}\approx1.710).

### A clean solved region: (\varphi \le \alpha \le 5^{1/3})

In this whole strip, there is a simple exact criterion:
[
\text{complete}\quad\Longleftrightarrow\quad
t<\min!\left(\frac{3}{\alpha^2},\frac{5}{\alpha^3}\right).
]
([Erdős Problems][1])

### The upper part: (5^{1/3}<\alpha<2)

* If **(t\ge 1)**, then the sequence is **not complete**. ([Erdős Problems][1])
* If **(0<t<1)**, the dependence on (t) and (\alpha) becomes “surprisingly complex”; Graham showed, for example, that for some (t\in(0,1)) the set of (\alpha) giving completeness breaks into many disjoint intervals. ([Erdős Problems][2])
  (So there isn’t a single simple inequality in this range; Graham’s paper gives a detailed analysis/algorithmic description.) ([Erdős Problems][1])

### The lower part: (1<\alpha<\varphi)

Here the **complete vs incomplete** question is still **open in full generality**.

What *is* known cleanly is the stronger property “entirely complete” (covers **all** positive integers, not just sufficiently large ones):
[
\text{entirely complete}\quad\Longleftrightarrow\quad
t<\min!\left(\frac{2}{\alpha},\frac{3}{\alpha^2}\right).
]
([Erdős Problems][1])

For the remaining region
[
1<\alpha<\varphi,\qquad
t\ge \min!\left(\frac{2}{\alpha},\frac{3}{\alpha^2}\right),
]
it is plausible that the sequence is still complete, but this is not proved; even basic parity questions like whether (\lfloor (3/2)^n\rfloor) is odd infinitely often are relevant obstacles. ([Erdős Problems][2])

There are also partial positive results inside this region, including:

* **Computer-assisted verified ranges**, e.g. completeness for all (t\le 3) when (\alpha\le 1.4), etc. ([Erdős Problems][1])
* A **general sufficient condition** (proved in Woett’s work-in-progress): the sequence is complete whenever
  [
  \alpha \le 1+\frac{1}{\lceil t\rceil + 2\lceil \sqrt t\rceil }.
  ]
  ([Erdős Problems][1])

## Important definitional caveat

You phrased it as “sum of **distinct integers** of the form (\lfloor t\alpha^n\rfloor)”. In the classical “complete sequence” literature (and in Graham’s work), one usually means “sum of distinct **terms**” (distinct indices), so if the same value occurs twice you may use it twice. This distinction matters for small-$n$ coincidences. ([Erdős Problems][1])

The classification statements quoted above follow that standard convention (distinct indices). ([Erdős Problems][1])

---

If you tell me whether you want the **standard** convention (distinct indices) or the stricter “distinct values only” convention, I can restate the piecewise conditions above in exactly that language [[nomath]](the only big immediate change is the $\alpha=1$ case)[[/nomath]].

[1]: https://www.erdosproblems.com/forum/thread/349 "https://www.erdosproblems.com/forum/thread/349"
[2]: https://www.erdosproblems.com/349 "https://www.erdosproblems.com/349"

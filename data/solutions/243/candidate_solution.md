What you wrote is **exactly Erdős Problem #243**. As of **January 2026**, it is regarded as **open**: no general proof (or counterexample) is known that the two hypotheses

[
\lim_{n\to\infty}\frac{a_n}{a_{n-1}^2}=1,
\qquad
\sum_{n=1}^\infty \frac1{a_n}\in\mathbb{Q}
]

force the eventual Sylvester-type recursion

[
a_n=a_{n-1}^2-a_{n-1}+1\quad\text{for all large }n.
]

This open status is recorded explicitly on the Erdős Problems website. ([Erdős Problems][1])

That said, there is substantial **partial progress** and a very clear picture of *why* the recursion is the only “stable” way to get a rational sum with such fast (almost squaring) growth.

---

## 1) The proved theorem under a stronger hypothesis (Erdős–Straus 1964)

Erdős and Straus proved a theorem of the same flavor: if ((n_k)) is increasing and the denominators grow fast **and** a certain “least common multiple vs. next term” ratio stays bounded, then rationality forces the Sylvester recursion eventually.

In their paper *On the irrationality of certain Ahmes series* (1964), they assume (paraphrasing their notation)

* (\limsup \frac{n_k^2}{n_{k+1}} < \infty) (so “about squaring”), and
* the ratio (\frac{N_k}{n_{k+1}}) is bounded, where (N_k) is the least common multiple of (n_1,\dots,n_k) (in the Sylvester case it equals the product because the terms are coprime),

and they conclude:

> (\sum 1/n_k) is rational **iff** (n_{k+1}=n_k^2-n_k+1) for all sufficiently large $k$. ([Rényi Institute][2])

So: **with extra control on the lcm**, the statement is known and classical.

Your hypothesis (\frac{a_n}{a_{n-1}^2}\to 1) is *weaker* than having (\frac{\mathrm{lcm}(a_1,\dots,a_{n-1})}{a_n}) bounded, and bridging that gap is the hard part.

---

## 2) What Erdős–Straus *do* prove in the “limit ratio = 1” setting

Even without bounded lcm-ratio, Erdős–Straus proved a quantitative obstruction: if the sum is rational and the recursion does **not** eventually hold, then a certain limsup expression involving the lcm must be positive.

The Erdős Problems discussion page summarizes it in the form:

[
\text{if }\ \lim \frac{a_n}{a_{n-1}^2}=1,\ \sum \frac1{a_n}\in\mathbb{Q},\ \text{and not eventually Sylvester,}
]
then
[
\limsup_{n\to\infty}\
\frac{[a_1,\ldots,a_n]}{a_{n+1}}
\left(\frac{a_n^2}{a_{n+1}}-1\right)

> 0,
> ]
> where ([a_1,\ldots,a_n]) is the least common multiple. ([Erdős Problems][1])

Since your limit hypothesis implies (\frac{a_n^2}{a_{n+1}}-1\to 0), any non-Sylvester counterexample would need the lcm ratio (\frac{[a_1,\dots,a_n]}{a_{n+1}}) to blow up fast enough to keep that product away from $0$. That’s one reason the conjecture feels plausible: “randomly” you don’t expect such persistent lcm blow-up aligned with the squaring limit.

---

## 3) Why the recursion is “the” natural rational case: telescoping

If the recursion holds (even just eventually), the reciprocal sum becomes rational for a completely transparent reason: it telescopes.

Let (s_n) be defined by Sylvester’s recursion (s_{n+1}=s_n^2-s_n+1). Then:

[
s_{n+1}-1 = s_n(s_n-1),
]
so
[
\frac1{s_n}=\frac1{s_n-1}-\frac1{s_{n+1}-1}.
]

Therefore the tail sums telescope:

[
\sum_{k=n}^{N}\frac1{s_k}
=\frac1{s_n-1}-\frac1{s_{N+1}-1}
\ \xrightarrow[N\to\infty]{}\ \frac1{s_n-1}.
]

In particular, the whole series is rational (indeed, for the classical Sylvester sequence starting at $2$ it sums to $1$). ([Wikipedia][3])

So the conjecture is saying: **if a “nearly squaring” unit-fraction series sums to a rational, then it must eventually become one of these telescoping tails**.

---

## 4) A modern reformulation: Koizumi’s “pseudo-greedy expansion” reduction (2025)

A very relevant 2025 preprint by J. Koizumi shows that sequences with the “almost squaring” growth and a convergent reciprocal sum are, after discarding finitely many terms, governed by a deterministic Egyptian-fraction–type expansion (a *pseudo-greedy expansion*), with an associated “gap sequence” (\varepsilon_n\to 0). 

In Koizumi’s framework, the denominators satisfy an exact identity

[
a_{n+1}=\frac{1}{1-\varepsilon_n}a_n^2-a_n+(1-\varepsilon_{n+1}),
]

so if (\varepsilon_n) becomes exactly $0$ eventually, then the recursion becomes exactly

[
a_{n+1}=a_n^2-a_n+1
\quad\text{eventually}.
]


Koizumi explicitly conjectures that for **rational** numbers $r$, the pseudo-greedy gap sequence should become **eventually zero** [[nomath]](under the $\varepsilon_n\to0$ hypothesis)[[/nomath]], and notes computational verification for many rationals. 

This conjecture is essentially equivalent to Erdős Problem #243 in the “limit ratio = 1” regime.

---

## 5) Bottom line

* Your exact statement is **not currently a settled theorem**; it is a well-known **open problem** (Erdős Problem #243). ([Erdős Problems][1])
* There is a **proved theorem** (Erdős–Straus 1964) that gives the same conclusion under an additional boundedness condition involving the lcm of initial terms. ([Rényi Institute][2])
* Recent work (Koizumi 2025) gives a strong **structural reduction**: under the limit ratio and convergence, your sequence is eventually a pseudo-greedy expansion with a gap (\varepsilon_n\to0); proving that (\varepsilon_n) must hit $0$ eventually for rationals would settle the problem. 

If you want, I can also:

* walk through the **Erdős–Straus 1964 proof idea** in a self-contained way (it’s short but a bit technical), or
* explain the **pseudo-greedy recurrence** and how it translates the problem into an integer dynamical system [[nomath]](the $(c_n,d_n,e_n)$ recurrences in Koizumi/Tao’s discussion)[[/nomath]].

[1]: https://www.erdosproblems.com/forum/thread/243 "

    Erdős Problem #243 - Discussion thread

"
[2]: https://www.renyi.hu/~p_erdos/1964-19.pdf "https://www.renyi.hu/~p_erdos/1964-19.pdf"
[3]: https://en.wikipedia.org/wiki/Sylvester%27s_sequence?utm_source=chatgpt.com "Sylvester's sequence"

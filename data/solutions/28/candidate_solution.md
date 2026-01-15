Let
[
r_A(n);:=;(1_A*1_A)(n);=;\sum_{k\ge 0}1_A(k),1_A(n-k)
]
(the number of **ordered** pairs ((a,b)\in A^2) with (a+b=n)). Your hypothesis “(A+A) contains all but finitely many integers” is exactly
[
r_A(n)>0\qquad\text{for all }n\ge n_0 .
]

The conclusion you wrote,
[
\limsup_{n\to\infty} r_A(n)=\infty,
]
is the **Erdős–Turán conjecture on additive bases (order 2)**. It is *not* known in full generality as of the current literature: modern references still present it explicitly as a conjecture/problem rather than a theorem. ([ScienceDirect][1])

### What *is* known unconditionally

Although the conjecture remains open, there are nontrivial lower bounds showing that (r_A(n)) cannot stay too small forever. For instance, results of Grekos–Haddad–Helou–Pihko and later Borwein–Choi–Chu imply that for every (asymptotic) additive basis (A) of order 2 one has
[
\limsup_{n\to\infty} r_A(n)\ge 8,
]
equivalently (r_A(n)) exceeds (7) infinitely often. 

So we can prove “(\limsup r_A(n)\ge 8)” but we do *not* know how to push this to “(\limsup r_A(n)=\infty)” in general.

### Why the conjecture is hard (and an “easy” case you *can* prove)

Let (A(N):=|A\cap[0,N]|). A basic averaging argument gives, for every (N),
[
\sum_{n=0}^{2N} r_A(n)\ \ge\ #{(a,b)\in(A\cap[0,N])^2}\ =\ A(N)^2,
]
so by pigeonhole
[
\max_{0\le n\le 2N} r_A(n)\ \ge\ \frac{A(N)^2}{2N+1}.
]
Hence, **if** (A(N)) grows faster than (\sqrt{N}) (e.g. (A(N)\gg \sqrt{N},\omega(N)) with (\omega(N)\to\infty)), then the right-hand side (\to\infty), and you immediately get (\limsup r_A(n)=\infty).

In particular, the conjecture is trivially true for any basis (A) with **positive density** (or even (A(N)\gg N^{1/2+\varepsilon})), because then (A(N)^2/(2N)) grows like a positive constant times (N).

The difficulty is that an order‑2 basis can be extremely **thin**: one only has the rough necessary lower bound (A(N)\gtrsim \sqrt{N}), and in that borderline regime the averaging bound above only forces (\max r_A(n)) to be (\gtrsim 1), not unbounded. This “thin basis” regime is exactly where the Erdős–Turán conjecture is genuinely nontrivial.

---

If you tell me what level of detail you want (quick overview vs. a deeper dive), I can also summarize some of the main partial approaches in the literature (generating functions (F(z)=\sum_{a\in A}z^a), analytic estimates on (F(e^{it})), and the kind of arguments that lead to the current “(\ge 8)” barrier).

[1]: https://www.sciencedirect.com/science/article/abs/pii/S0195669824001653 "Bounded unique representation bases for the integers - ScienceDirect"

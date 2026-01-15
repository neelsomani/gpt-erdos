This is **open** (it’s one of Erdős’s longstanding problems on infinite Sidon sequences).

To put it in the usual “counting function” notation (A(N):=|A\cap[1,N]|), your condition
[
A(N)\gg_\varepsilon N^{1/2-\varepsilon}\quad\text{for all }\varepsilon>0
]
is essentially asking for a Sidon set with **near–square-root growth** (A(N)=N^{1/2-o(1)}). Erdős explicitly conjectured such a density [[nomath]](in the “for any $\varepsilon>0$” sense)[[/nomath]].

### Best known constructions [[nomath]](true Sidon, i.e. $B_2[1]$)[[/nomath]]

The best available lower bounds are still well below exponent $1/2$:

* The **greedy** construction gives (A(N)\gg N^{1/3}).
* **Ajtai–Komlós–Szemerédi (1981)** improved this to (A(N)\gg (N\log N)^{1/3}).
* **Ruzsa (1998)** proved existence of an infinite Sidon sequence with
  [
  A(N)=N^{\sqrt2-1+o(1)}\approx N^{0.4142\ldots+o(1)}.
  ]

  Cilleruelo later gave an **explicit** construction achieving the same exponent.

So the conjectural $1/2-o(1)$ exponent [[nomath]](and hence your $1/2-\varepsilon$ for every $\varepsilon$)[[/nomath]] remains out of reach.

### A key obstruction at exact square-root density

Erdős also showed that no infinite Sidon set can stay “uniformly” as dense as (c\sqrt N): for every infinite Sidon set,
[
\liminf_{N\to\infty}\frac{|A\cap[1,N]|}{N^{1/2}}=0,
]
so the (\sqrt N) scale must dip arbitrarily low along some subsequence.
[[nomath]](This does **not** rule out $N^{1/2-\varepsilon}$ for fixed $\varepsilon>0$, but it does rule out a positive $\liminf$ at exponent $1/2$.)[[/nomath]]

### “Almost Sidon” variants do achieve (1/2-\varepsilon)

If you weaken Sidon to **bounded representation** [[nomath]](a $B_2[g]$ set: each integer has $\le g$ representations as a sum of two elements)[[/nomath]], then the (1/2-\varepsilon) density is known: Erdős–Rényi claimed it and Vu proved it, and Cilleruelo–Kiss–Ruzsa–Vinuesa give proofs and quantitative bounds.
But getting the same exponent with the strict Sidon condition (g=1) is exactly the open problem.

So, as of late **2025** (and still listed open), no one knows whether such an infinite Sidon set exists.

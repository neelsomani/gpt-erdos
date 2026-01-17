Write the greedy Sidon set as (A={a_1<a_2<a_3<\cdots}) (this is the **Mian–Chowla sequence**), and let
[
A(N):=\lvert A\cap{1,\dots,N}\rvert.
]

## What is known about the growth?

### General lower bound [[nomath]](forces at least quadratic growth of $a_n$)[[/nomath]]

A Sidon set has all *differences* (a_i-a_j) ((i>j)) distinct [[nomath]](equivalently, no nontrivial $a+b=c+d$)[[/nomath]]. Hence among $\\{a_1,\dots,a_n\\}$ there are (\binom n2) distinct positive differences, all lying in ({1,2,\dots,a_n-a_1}). Since (a_1=1),
[
\binom n2 \le a_n-1 \quad\Rightarrow\quad a_n \ge 1+\frac{n(n-1)}2
= \frac{n^2}{2}+O(n).
]
So
[
A(N)\le (1+o(1))\sqrt{2N}.
]
[[nomath]](This standard “difference-counting” argument is also the origin of the quoted lower bound $n^2/2+O(n)$ for $a_n$ in the literature summaries.)[[/nomath]] ([OEIS][1])

### General upper bound for the greedy sequence [[nomath]](cubic, hence $A(N)\gtrsim N^{1/3}$)[[/nomath]]

A very clean “greedy” counting argument (spelled out e.g. in Kowalski’s notes) is:

If ({a_1,\dots,a_k}) is Sidon, then **any** integer $m$ which is *not* of the form
[
m=a+b-c \qquad(a,b,c\in{a_1,\dots,a_k})
]
can be adjoined while preserving the Sidon property. There are at most (k^3) integers of the form $a+b-c$, so the smallest positive integer not of that form is (\le k^3+1). Therefore
[
a_{k+1}\le k^3+1,
]
and consequently
[
A(N)\ \ge\ c,N^{1/3}\quad\text{for an absolute }c>0.
]


This is the “trivial” (N^{1/3}) lower bound mentioned in the standard problem statements. ([Erdős Problems][2])

### Best published cubic bound constant [[nomath]](still gives only $N^{1/3}$)[[/nomath]]

A sharper (still cubic) upper bound on (a_n) is attributed to Jia:
[
a_n \le \frac{n^3}{6}+O(n^2),
]
as summarized in Cheng’s 2025 paper on greedy Sidon sets for linear forms. ([ScienceDirect][3])

This improves constants but **does not change the exponent**: it still only implies (A(N)\gg N^{1/3}).

### Summary of rigorous bounds

Putting the quadratic lower bound and cubic upper bound together, one has
[
N^{1/3}\ \ll\ A(N)\ \ll\ N^{1/2},
]
and equivalently
[
\frac{n^2}{2}+O(n)\ \le\ a_n\ \le\ \frac{n^3}{6}+O(n^2).
]
([ScienceDirect][3])

So the “order of growth” is only pinned down to **between quadratic and cubic** for (a_n), or **between (N^{1/3}) and (N^{1/2})** for $A(N)$.

## Is it true that (A(N)\gg N^{1/2-\varepsilon}) for all (\varepsilon>0)?

For this *specific greedy* Sidon set $A$: **this is open**.

It is exactly Erdős’s question about the greedy Sidon sequence (Erdős–Graham), and it remains listed as open in current problem compilations. ([Erdős Problems][2])

A couple of important remarks around that:

* Proving (A(N)\gg N^{1/2-\varepsilon}) for every (\varepsilon>0) would mean the greedy sequence is “almost” as dense [[nomath]](up to $N^\varepsilon$)[[/nomath]] as the best possible finite Sidon sets, i.e. it would force (a_n \le n^{2+o(1)}). Nothing close to this is known for the greedy construction.
* There is a commonly stated **conjectural** asymptotic for the Mian–Chowla sequence,
  [
  a_n \sim \frac{n^3}{(\log n)^2},
  ]
  which would imply $A(N)$ behaves like ((N(\log N)^2)^{1/3}), far smaller than (N^{1/2-\varepsilon}). But this is only conjectural, not a theorem. ([OEIS][1])

## Context: what is known for *some* (non-greedy) infinite Sidon sets?

Erdős also conjectured (more generally) that **there exists** an infinite Sidon set $S$ with (S(x)\gg x^{1/2-\varepsilon}) for every (\varepsilon>0), but this is open as well; the best known constructions are sparser [[nomath]](e.g. Ruzsa’s exponent $\sqrt2-1\approx 0.4142$)[[/nomath]]. 

This is relevant because it suggests even in the “existence” setting, the (1/2-\varepsilon) exponent is a major open frontier; demanding it from the *greedy* set is at least as hard.

---

**Bottom line:** the greedy Sidon (Mian–Chowla) sequence has
[
N^{1/3}\ll A(N)\ll N^{1/2},
]
and the improvement to (A(N)\gg N^{1/2-\varepsilon}) for all (\varepsilon>0) is **not known** (open). ([Erdős Problems][2])

[1]: https://oeis.org/A005282?utm_source=chatgpt.com "A005282"
[2]: https://www.erdosproblems.com/340 "
  
    Erdős Problem #340
  
"
[3]: https://www.sciencedirect.com/science/article/abs/pii/S0022314X24001768 "Greedy Sidon sets for linear forms - ScienceDirect"

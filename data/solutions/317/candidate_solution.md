Let

[
L_n:=\operatorname{lcm}(1,2,\dots,n).
]

## The “(1/L_n)” lower bound is always true (non‑strict)

For any choice (\delta_k\in{-1,0,1}),

[
\sum_{k=1}^n \frac{\delta_k}{k}
= \frac{1}{L_n}\sum_{k=1}^n \delta_k\frac{L_n}{k}.
]

Since each (L_n/k\in\mathbb Z), the numerator
[
A:=\sum_{k=1}^n \delta_k\frac{L_n}{k}\in\mathbb Z,
]
so the sum equals (A/L_n). Therefore, if the sum is not $0$, then (A\neq 0), hence (|A|\ge 1) and

[
\left|\sum_{k=1}^n\frac{\delta_k}{k}\right|\ge \frac{1}{L_n}.
]

So the inequality with “(\ge)” holds for **every $n$**; there is nothing asymptotic about it. (This is exactly the point noted on the Erdős Problems discussion page: the non‑strict inequality is “obvious”.) ([Erdős Problems][1])

### The strict “(>,1/L_n)” version

Your second question asks whether, for all sufficiently large $n$, one never attains the *smallest* nonzero lattice step (1/L_n), i.e. whether $A$ can never be (\pm 1) for large $n$. This is **not** true for small $n$: e.g.
[
\frac12-\frac13-\frac14=-\frac1{12}=-\frac{1}{L_4},
]
so equality occurs at $n=4$. ([Erdős Problems][1])

Whether equality (\left|\sum \delta_k/k\right|=1/L_n) can happen infinitely often (or at all) for large $n$ is part of Erdős Problem #317 and is treated there as open; numerical data reported there shows the minimum nonzero value multiplied by (L_n) is often much larger than $1$ for moderate $n$ [[nomath]](e.g. values like $874,299,1995,\dots$)[[/nomath]]. ([Erdős Problems][1])

So:

* **Always true:** (\left|\sum \delta_k/k\right|\ge 1/L_n) when nonzero.
* **Strict (>) version:** fails for $n=4$; the “eventually strict” question is not resolved in general (as of the current discussion/status). ([Erdős Problems][1])

---

## The “(c/2^n)” question (Erdős #317) and what is known

Define
[
Q_n:=\\{\sum_{a\in A}\frac1a:\ A\subseteq{1,2,\dots,n}\\}.
]
Any (\delta\in{-1,0,1}^n) can be written as the difference of two indicator vectors, so
[
\sum_{k=1}^n \frac{\delta_k}{k}=q-q'\quad\text{for some }q,q'\in Q_n.
]
Thus your first question is equivalent to asking whether there is an absolute (c>0) such that for every $n$,
[
\min_{\substack{q,q'\in Q_n\ q\ne q'}} |q-q'|<\frac{c}{2^n}.
]
This equivalence is stated explicitly on the Erdős Problems discussion thread for #317. ([Erdős Problems][1])

### The trivial pigeonhole bound [[nomath]](why you get a $\log n$)[[/nomath]]

All (q\in Q_n) lie in $[0,H_n]$ where (H_n=\sum_{k=1}^n 1/k\le \log n+1). So among (|Q_n|) distinct numbers in an interval of length (\le \log n+1), two differ by at most ((\log n+1)/|Q_n|). This gives
[
\min_{q\ne q'}|q-q'|\ \le\ \frac{\log n+1}{|Q_n|}.
]
But this only becomes (\ll 2^{-n}) if (|Q_n|) were (\gg 2^n), which is very far from true.

### What is actually known about (|Q_n|)

Estimating (|Q_n|) is Erdős Problem #320. The best available bounds are subexponential in $n$: roughly
[
\log |Q_n| \asymp \frac{n}{\log n}\times (\text{iterated log factors}),
]
with classical bounds of Bleicher–Erdős and improvements reported by Bettin–Grenié–Molteni–Sanna (2025) on the Erdős Problems site. ([Erdős Problems][2])

Plugging such bounds for (|Q_n|) into the pigeonhole estimate yields an upper bound on the minimum gap of the form
[
\min_{q\ne q'}|q-q'|\ \le\ 2^{-,\frac{n(\log\log\log n)^{1+o(1)}}{\log n}},
]
i.e. **much larger** than (2^{-n}) [[nomath]](the exponent is $o(n)$, not $\asymp n$)[[/nomath]]. This “weak version” and its provenance are described on the #317 thread. ([Erdős Problems][1])

### Status of the (c/2^n) bound

The Erdős Problems site currently lists #317 as **OPEN**. ([Erdős Problems][1])
Moreover, the discussion there mentions heuristics (attributed to van Doorn) suggesting that the subexponential-in-$n$ bound above might be closer to the truth than (c/2^n), which would point toward a **negative** answer to the existence of a universal $c$. ([Erdős Problems][1])

So, as things stand in the literature/discussion summarized there:

* The existence of an absolute $c$ with (\min |q-q'| < c/2^n) for all $n$ is **not known**. ([Erdős Problems][1])
* The best unconditional general upper bounds known are of the weaker, subexponential form coming from (|Q_n|) estimates (Problem #320). ([Erdős Problems][2])

---

## Summary answers to your two questions

1. **Existence of $c$ with a nonzero $\\{-1,0,1\\}$ harmonic sum (<c/2^n) for every $n$:** this is Erdős Problem #317 and is currently listed as **open**; the strongest general bounds known are much weaker than (2^{-n}). ([Erdős Problems][1])

2. **Lower bound by (1/L_n):**

   * The non-strict version (\ge 1/L_n) holds for **all $n$** whenever the sum is nonzero (simple denominator argument).
   * The strict version “(>1/L_n)” fails at $n=4$, and the “eventually strict” question is part of the same open problem package; computational evidence suggests strictness for many $n$ but no general proof is currently recorded on that thread. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/317 "

    Erdős Problem #317 - Discussion thread

"
[2]: https://www.erdosproblems.com/320 "
  
    Erdős Problem #320
  
"

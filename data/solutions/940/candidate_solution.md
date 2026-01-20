As of **January 2026**, for **every fixed (r\ge 3)** both questions you ask are **open** in general.

This is an Erdős–Ivić problem recorded in the 1986 Oberwolfach problem list, and it appears explicitly as **Erdős Problem #940** (still marked open). ([Erdős Problems][1])

### What is known [[nomath]](and why $k=r$ is the hard threshold)[[/nomath]]

Let (F_r) be the set of $r$-powerful [[nomath]](a.k.a. $r$-full)[[/nomath]] integers, and let
[
S_r := \bigcup_{1\le k\le r} (F_r+\cdots+F_r)\quad (k\text{ summands}).
]

A standard fact (going back to Erdős–Szekeres and subsequent refinements) is that
[
|\\{n\le x : n\in F_r\\}| \asymp x^{1/r},
]
so (F_r) itself has density $0$.

From this, one gets an *easy* density-zero statement for fewer summands:

* For any fixed (k<r),
  [
  |\\{n\le x : n \text{ is a sum of } k \text{ (r)-powerful numbers}\\}|
  \ \le\ |(F_r\cap[1,x])^k|
  \ =\ O(x^{k/r}) \ =\ o(x),
  ]
  hence **density $0$** for sums of at most $r-1$ $r$-powerful numbers.

The real difficulty is exactly your case $k=r$, where the trivial bound only gives $O(x)$, so it does **not** force density $0$.

### Status of your two questions for (r\ge 3)

* **Infinitely many non-representable integers?** Unknown in general for (r\ge 3). Erdős claimed in print that a “simple counting argument” shows there must be infinitely many integers not representable as a sum of (\le r) $r$-powerful numbers, but **Schinzel pointed out an error** in that argument. ([Erdős Problems][1])

* **Does (S_r) have density $0$?** Also unknown for (r\ge 3). ([Erdős Problems][1])
  In fact, even for $r=3$, the problem is at least as hard as famous questions about values of (x^3+y^3+z^3): the ErdosProblems discussion notes that it is not even known whether the set of integers that are a sum of at most three cubes has density $0$. ([Erdős Problems][1])

### Context: what happens for $r=2$ (squarefull/powerful numbers)

Although you asked for (r\ge 3), it’s helpful to know the $r=2$ picture because it shows the phenomenon can go either way depending on the number of summands:

* **Three summands suffice**: every sufficiently large integer is a sum of at most three powerful (squarefull) numbers (Heath-Brown). ([Erdős Problems][2])
* **Two summands are sparse**: if $A(x)$ counts integers (\le x) representable as a sum of two squarefull numbers, the set has density $0$, and in fact the best-known bounds are of the shape
  [
  A(x) = (\log\log x)^{O(1)}\frac{x}{(\log x)^{\alpha}}
  \quad(\alpha=1-2^{-1/3}\approx 0.2063),
  ]
  following work of Odoni, Baker–Brüdern, Blomer, and Blomer–Granville. ([Erdős Problems][3])

So for $r=2$, “(\le r) summands” means “(\le 2) summands”, and the answer to your density question is **yes (density 0)**—but for (r\ge 3), the analogous “(\le r)” case is exactly the hard, currently open regime.

---

If you want, I can also sketch the heuristic behind why many people expect density $0$ [[nomath]](it’s related to representing integers by diagonal degree-$r$ forms with $r$ variables after decomposing $r$-full numbers into structured parts)[[/nomath]], and why standard counting breaks exactly at $k=r$.

[1]: https://www.erdosproblems.com/940 "https://www.erdosproblems.com/940"
[2]: https://www.erdosproblems.com/941 "https://www.erdosproblems.com/941"
[3]: https://www.erdosproblems.com/1081 "https://www.erdosproblems.com/1081"

Let
[
A=\prod_{m=u}^v m,\qquad p:=P(A)=\max{ \text{primes }q: q\mid A},
]
and assume the $p$-adic valuation satisfies (v_p(A)\ge 2).

### What can be proved unconditionally

1. **You must have (u>v/2) [[nomath]](for $v$ large enough to avoid tiny edge cases)[[/nomath]].**

If (p>v/2), then the only multiple of $p$ in $[1,v]$ is $p$ itself, and since (p^2>v) it would contribute only exponent $1$ to $A$. So (v_p(A)\ge2) forces (p\le v/2).

If instead (u\le v/2), then by Bertrand’s postulate there is a prime $q\in(v/2,v]$. That prime lies in $[u,v]$, hence divides $A$, and it is larger than every prime (\le v/2), contradicting (p\le v/2). Therefore (u>v/2).

So any such interval $[u,v]$ sits in the “top half” $(v/2,v]$ and in particular contains **no primes**.

2. **A “square-root” upper bound:**
   [
   v-u<\sqrt v.
   ]

Write (k:=v-u+1) (number of factors). From (u>v/2) we get (u>v-u), hence (u\ge k). In fact $u=k$ cannot happen for (k>1), because then ([u,v]=[k,2k-1]) contains a prime in $(k,2k)$ (again Bertrand), which would force the largest prime divisor to occur with exponent $1$.

Thus for any nontrivial solution we have (u>k). Then the classical Sylvester–Schur theorem implies that (P(A)>k). In particular (p>k), so among $k$ consecutive integers there can be **at most one** multiple of $p$. Hence the condition (v_p(A)\ge2) can only happen if that unique multiple is divisible by (p^2), so (p^2\le v), i.e. $p\le\sqrt v$. Combining (k<p\le \sqrt v) gives (k<\sqrt v), hence
[
v-u=k-1<\sqrt v.
]

This is consistent with what Erdős–Graham are reported to attribute (via Ramachandra) as (v-u\le v^{1/2+o(1)}). ([Erdős Problems][1])

So **unconditionally** you certainly do *not* get anything as strong as (v^{o(1)}) from current methods; the natural unconditional scale is at best about (\sqrt v). ([Erdős Problems][1])

---

### Is it true that (v-u=v^{o(1)})?

This is **open**, and (as noted in the Erdős Problems database) the first question “boils down” to conjectures about **prime gaps**. ([Erdős Problems][1])

A standard way to see the connection is: if one had that for every (\varepsilon>0) and all large $x$, there is always a prime in $[x,x+x^\varepsilon]$, then any interval $[u,v]$ with (v-u\ge u^\varepsilon) would contain a prime near its start; that prime would then be the largest prime divisor of the product and would occur with exponent $1$, contradicting your hypothesis. Under **Cramér’s conjecture** [[nomath]](prime gaps $O(\log^2 x)$)[[/nomath]], this “prime in $[x,x+x^\varepsilon]$” statement holds for every fixed (\varepsilon>0), and therefore Cramér would indeed force
[
v-u = v^{o(1)}.
]
([Erdős Problems][1])

So: **Yes under strong prime-gap conjectures (e.g. Cramér); unproved unconditionally.**

---

### Can $v-u$ be arbitrarily large?

Also **open**.

There is a plausible heuristic suggesting “yes”: the proportion of integers $n$ with all prime factors (\le n^{1/2}) is (\rho(2)=1-\log 2>0) (Dickman–de Bruijn heuristics). That makes it plausible that for any fixed $k$ one should sometimes see $k$ consecutive integers near (q^2) [[nomath]](with $q$ prime)[[/nomath]] whose prime factors are all (\le q); then the largest prime in the product would be $q$, and it would occur with exponent at least $2$ because (q^2) is in the interval. ([Erdős Problems][1])

But no proof is known that such runs exist for arbitrarily large $k$.

What *is* known are explicit examples for modest lengths. For instance, the discussion thread records a solution with (v-u=13) where the largest prime divisor is $4237033$ and occurs with multiplicity $2$; and another with multiplicity $3$ and (v-u=5). ([Erdős Problems][1])

---

### Bottom line

* **Unconditionally:** you can show (v-u<\sqrt v) [[nomath]](so $v-u$ is at most on the $\sqrt v$ scale)[[/nomath]], consistent with the cited (v^{1/2+o(1)}) bound. ([Erdős Problems][1])
* **(v-u=v^{o(1)}):** open; it would follow from prime-gap conjectures such as Cramér. ([Erdős Problems][1])
* **$v-u$ arbitrarily large:** open; heuristics suggest “yes,” and examples exist for small-to-moderate gaps, but unboundedness is not proved. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/discuss/382 "

    Erdős Problem #382 - Discussion thread

"

This is **open**.

It’s an Erdős–Graham question (often listed as **Erdős Problem #421**) asking whether one can take a strictly increasing sequence of integers of **asymptotic density 1** whose **products over all index intervals**
[
\prod_{u\le i\le v} d_i
]
are all distinct. No construction with density $1$ is known, and no impossibility proof is known either. ([Erdős Problems][1])

### What *is* known (best general lower bound)

A quick observation: for any strictly increasing sequence ((d_i)), **interval products of the same length are automatically distinct**.
Indeed, if (v-u=v'-u') and (u<u'), then termwise (d_{u+t}<d_{u'+t}) for each $t$, so
[
\prod_{t=0}^{v-u} d_{u+t};<;\prod_{t=0}^{v-u} d_{u'+t}.
]
So any collision must involve **different lengths**.

A standard way to guarantee *no* collisions is therefore to build a dense set (A\subset\mathbb N) with the property:

> If (\prod_{i=1}^r a_i = \prod_{j=1}^s b_j) with (a_i,b_j\in A), then necessarily (r=s).

If you enumerate such an $A$ increasingly as (d_1<d_2<\cdots), then equality of two consecutive-block products would force the two blocks to have the **same number of factors** (r=s), but equal-length blocks can’t have equal products (by the monotonicity argument above), so **all consecutive-block products are distinct**.

Selfridge constructed such a set $A$ of density arbitrarily close to $1/e$, which yields a sequence ((d_i)) with
[
\text{density} > \frac1e-\varepsilon
]
and with all consecutive-block products distinct. ([Erdős Problems][2])

Very roughly, Selfridge’s construction takes large primes (p_1<\cdots<p_k) with (\sum 1/p_i\approx 1) and lets $A$ be the integers divisible by **exactly one** of these primes; comparing (p_i)-adic valuations forces the “number of factors” in any product identity to match. ([Erdős Problems][2])

### Why this doesn’t settle the density‑1 question

The “property (r=s)” condition is *stronger* than what #421 asks (it controls **all** product identities, not just identities coming from **consecutive blocks**), and it is known that this stronger property cannot hold at density (>1/e) [[nomath]](Ruzsa is reported to have proved an upper-density bound $\le 1/e$ for that stronger property)[[/nomath]]. 

But that upper bound applies to the **stronger** property, not directly to the consecutive-block requirement; so it does **not** rule out density $1$ for #421.

### Current status

As of the latest public tracking/discussion I can find (including the ErdősProblems entry and its discussion thread), the density‑$1$ version remains unsolved. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/421 "
  
    Erdős Problem #421
  
"
[2]: https://www.erdosproblems.com/786 "
  
    Erdős Problem #786
  
"

Write (g(n)=n+\varphi(n)) and (g_k(n)=g^{\circ k}(n)) (the (k)-fold iterate). Suppose that for some integers (r\ge1) and some (K) we have
[
g_{k+r}(n)=2,g_k(n)\qquad\text{for all }k\ge K.
]

### Basic necessary facts

* If (n) is odd and (n>2), then (\varphi(n)) is even and (g(n)=n+\varphi(n)) is odd; hence all iterates (g_k(n)) are odd. Then (2g_k(n)) is even, so the identity cannot hold. Therefore **$n$ must be even** [[nomath]](and $n=1,2$ do not work)[[/nomath]]. ([ar5iv][1])
* Also (r\neq 1) (for (n>1), (\varphi(n)<n), so (g(n)<2n), hence (g(n)=2n) is impossible).

So any solution must have **$n$ even and (r\ge2)**.

---

## What is known for the doubling relation: the case (r=2)

This is the one case that has been analyzed in depth. Steinerberger (2025) shows that understanding
[
g_{k+2}(n)=2g_k(n)\ \ \text{(eventually)}
]
reduces to a Diophantine equation and yields an essentially complete structural classification. ([arXiv][2])

A key point is: once the relation holds at one time $k$ (with the relevant iterate even), it automatically propagates to all later times [[nomath]](using $g(2m)=2g(m)$ for even $m$)[[/nomath]]. ([ar5iv][1])
So “for all large $k$” is equivalent to “from some point on we have entered a special orbit”.

### The special “eventual” orbits for (r=2)

The explicit infinite families of “doubling every 2 steps” solutions are:
[
m=2^{\ell}\cdot t,\qquad t\in{1,3,5,7,35,47},
]
[[nomath]](with the usual caveat that everything must be even, so for $t=1$ this starts at $m\ge4$)[[/nomath]]. ([arXiv][2])

These correspond to three odd-part 2-cycles:

* (1\leftrightarrow 3) [[nomath]](powers of $2$ and $3\cdot 2^{\ell}$)[[/nomath]],
* (5\leftrightarrow 7),
* (35\leftrightarrow 47),

and on each of these cycles the map (g^{\circ 2}) multiplies the number by $2$. For example:

* (5\cdot 2^\ell \mapsto 7\cdot 2^\ell \mapsto 5\cdot 2^{\ell+1}),
* (35\cdot 2^\ell \mapsto 47\cdot 2^\ell \mapsto 35\cdot 2^{\ell+1}),
* (2^\ell \mapsto 3\cdot 2^{\ell-1} \mapsto 2^{\ell+1}).

### Possible additional (r=2) solutions (conditional)

Steinerberger also shows that **any other** (r=2) solution (if it exists) would have to come from a very special prime (p\equiv 7\pmod 8) satisfying
[
\varphi!\left(\frac{3p-1}{4}\right)=\frac{p+1}{2},
]
and reports that a computer search found no such primes below (10^{10}). ([arXiv][2])
So the six families above are the only known ones, and are conjectured to be all. ([Erdős Problems][3])

### Translating back to your “for all large (k)” question

For (r=2), the statement
[
g_{k+2}(n)=2g_k(n)\ \text{for all large }k
]
holds **iff** the orbit of $n$ eventually lands in one of the families (2^\ell t) with (t\in{1,3,5,7,35,47}) (or in one of the hypothetical exceptional-prime orbits). ([ar5iv][1])

---

## What about (r\neq 2)?

As of the 2024–2025 references above, the **general Erdős–Graham problem** [[nomath]](allowing other shifts $r$)[[/nomath]] is open; there are no known examples with the doubling factor $2$ for (r\neq 2), and Cambie conjectures that the only doubling solutions are the (r=2) ones coming from $\\{1,3,5,7,35,47\\}$ [[nomath]](up to powers of $2$)[[/nomath]]. ([Erdős Problems][3])

---

## Bottom line

* **Proven necessary:** $n$ must be even [[nomath]](and $r\ge2$)[[/nomath]].
* **Proven classification for (r=2):** eventual doubling every 2 steps happens exactly when the orbit eventually reaches one of the explicit families
  $$
  2^\ell\cdot t,\quad t\in\\{1,3,5,7,35,47\\},
  $$
  with the only possible additional solutions tied to a very rare prime condition [[nomath]](none found below $10^{10}$)[[/nomath]]. ([arXiv][2])
* **For (r\neq2):** no such doubling solutions are known; the existence/classification is part of an open problem and is conjectured not to occur. ([Erdős Problems][3])

If you tell me whether you want the answer phrased as (i) “all *eventual tails* that can occur” (the dynamical classification), or (ii) “all *starting values* $n$ that end up in those tails” (a basin-of-attraction description, which is more complicated), I can format the result accordingly.

[1]: https://ar5iv.org/html/2504.08023v1 "[2504.08023] On an iterated arithmetic function problem of Erdős and Graham"
[2]: https://arxiv.org/abs/2504.08023 "[2504.08023] On an iterated arithmetic function problem of Erdos and Graham"
[3]: https://www.erdosproblems.com/latex/411 "
  
    Erdős Problems
  
"

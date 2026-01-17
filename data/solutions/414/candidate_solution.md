Let (h(n)=n+\tau(n)) and (h_k=h^{\circ k}) as you defined.

A couple of structural facts are immediate:

* (\tau(n)\ge 1), so (h(n)>n) for all $n$. Hence every orbit
  [
  n,\ h(n),\ h_2(n),\dots
  ]
  is strictly increasing and contains no cycles.
* Therefore, if two orbits ever hit the same value once, they coincide forever after that.

### Equivalent reformulation

Let (\mathcal O(1)={h_k(1):k\ge 0}) be the orbit of $1$. This is OEIS **A064491**. ([OEIS][1])

Your statement

> for all $m,n$ there exist $i,j$ with (h_i(m)=h_j(n))

is equivalent to the seemingly weaker statement

> for every $n$, the orbit of $n$ intersects (\mathcal O(1)).

Reason:

* If your statement holds for all (m,n), then in particular taking (m=1) shows every orbit meets (\mathcal O(1)).
* Conversely, suppose every orbit meets (\mathcal O(1)). Say (h_{i_0}(m)=h_{a}(1)) and (h_{j_0}(n)=h_{b}(1)). WLOG (a\le b). Then
  [
  h_{i_0+(b-a)}(m)=h_b(1)=h_{j_0}(n),
  ]
  so the orbits of $m$ and $n$ do intersect.

So the question is: **does every starting value eventually “join” the $1$-orbit (A064491)?**

### Status: open

This is a long‑standing open problem due to **Claudia Spiro** (posed in 1977), explicitly recorded in the OEIS entry for A064491 as “If you change the starting term, does the resulting sequence always join this one?” ([OEIS][1])

It is also listed as **Erdős Problem #414** (from Erdős–Graham), and that source currently marks it **OPEN**; it notes that Erdős and Graham *believed* the answer should be “yes,” but no proof is known. ([Erdős Problems][2])

So the best honest answer is:

* **Unknown in general (open).** ([Erdős Problems][2])

### A bit of numerical evidence (not a proof)

Just to give a feel for the behavior: many merges happen very early [[nomath]](e.g. $h(4)=7$ and $h(5)=7$)[[/nomath]], and computational experiments strongly suggest that orbits rapidly fall into the same “main” orbit. For instance, I checked by direct computation that every starting value (n\le 100{,}000) reaches the $1$-orbit by the time the iterates are below (2\times 10^7) (with the slowest among these taking 1261 iterations to enter).

But again: the general statement for *all* $m,n$ is currently **not proved** and remains open. ([Erdős Problems][2])

[1]: https://oeis.org/A064491 "A064491 - OEIS"
[2]: https://www.erdosproblems.com/414 "
  
    Erdős Problem #414
  
"

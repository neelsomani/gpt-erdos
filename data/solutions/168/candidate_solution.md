The limit **does exist**.

A theorem of **Graham–Spencer–Witsenhausen (1977)** shows that

[
\lim_{N\to\infty}\frac{F(N)}{N}
=\frac13\sum_{k\in K}\frac1{d_k},
]

where

* (d_1<d_2<\cdots) are the **3‑smooth numbers** [[nomath]](numbers of the form $2^a3^b$: $1,2,3,4,6,8,9,12,\dots$)[[/nomath]],
* $f(k)$ is the largest size of a subset of $\\{d_1,\dots,d_k\\}$ that contains no triple $\\{n,2n,3n\\}$,
* and $K$ is the set of indices $k$ for which $f(k)>f(k-1)$ (i.e. when adding the next 3‑smooth number really increases the best possible size). ([Erdős Problems][1])

Using that formula, the value has been computed very accurately. The constant is

[
0.80096575500655898909042032638808241\ldots
]
([OEIS][2])

### Is it irrational?

This is **not known**. It is explicitly listed as an **open question** whether this constant is irrational. ([OEIS][2])

[1]: https://www.erdosproblems.com/168 "
  
    Erdős Problem #168
  
"
[2]: https://oeis.org/A386439 "A386439 - OEIS"

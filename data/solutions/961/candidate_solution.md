Write $P(n)$ for the largest prime divisor of $n$. Your condition is equivalent to saying that for every (m>k),
[
P\bigl(m(m+1)\cdots(m+n-1)\bigr)>k,
]
because a prime (>k) divides the product iff it divides at least one of the $n$ factors. This is exactly the Erdős function $f(k)$ studied in the literature. 

Equivalently again: (f(k)-1) is the **maximum length of a run of consecutive $k$-smooth integers** [[nomath]](integers all of whose prime factors are $\le k$)[[/nomath]] occurring entirely above $k$. ([Erdős Problems][1])

## What is known unconditionally

* **Trivial bound (Sylvester–Schur):**
  [
  f(k)\le k.
  ]


* **Erdős’ improvement:**
  [
  f(k) < 3,\frac{k}{\log k}
  \quad\text{(for large (k)).}
  ]
  ([Erdős Problems][1])

* **Best published asymptotic upper bound (Shorey, building on Ramachandra/Jutila/etc.):**
  [
  f(k)\ \ll\ \frac{k}{\log k},\frac{\log\log\log k}{\log\log k}.
  ]
  [[nomath]](All logs are natural logs; $\ll$ means “$\le C\times$” for some absolute constant $C$ and large $k$.)[[/nomath]] 

* **Lower bound (Rankin-type large-gap constructions):** one can force $f(k)$ to be at least of size
  [
  f(k)\ \gg\ \frac{\log k,\log\log k,\log\log\log\log k}{(\log\log\log k)^2}
  \quad\text{(infinitely often).}
  ]


Putting these together gives the current “sandwich” (up to constant factors and the usual iterated-log bookkeeping):
[
\frac{\log k\log\log k\log\log\log\log k}{(\log\log\log k)^2}
\ \lesssim\ f(k)\ \lesssim
\frac{k}{\log k}\frac{\log\log\log k}{\log\log k}.
]


## Why people expect $f(k)$ to be about ((\log k)^2)

A key easy observation is that **any prime gap inside $(k,2k]$** creates a run of consecutive integers with *no* prime factor (>k): every composite (n\le 2k) automatically has all prime factors (\le k). So prime gaps give lower bounds for $f(k)$. ([Erdős Problems][1])

Standard heuristics for prime gaps (Cramér-type) suggest that the largest relevant gaps are of size about ((\log k)^2), and accordingly the “right” order of magnitude for $f(k)$ should be
[
f(k)\asymp (\log k)^2
\quad\text{(conjecturally / heuristically).}
]
This expectation is explicitly stated in the literature on this problem. 

---

So the best current estimate is:

* **Proved bounds:** $f(k)$ grows faster than a (slightly enhanced) (\log k\log\log k) scale infinitely often, but is $o(k)$ and in fact (\ll \dfrac{k}{\log k}\cdot\dfrac{\log\log\log k}{\log\log k}). 
* **Conjectured “true size”:** $f(k)$ should be of order ((\log k)^2). 

[1]: https://www.erdosproblems.com/961 "
  
    Erdős Problem #961
  
"

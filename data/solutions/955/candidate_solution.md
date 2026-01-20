What you wrote is (as far as I can tell) **not known in full generality**. It’s a well-known open conjecture about the aliquot sum / sum-of-proper-divisors function.

### Status: open (EGPS conjecture)

In 1992, **Erdős–Granville–Pomerance–Spiro** conjectured:

> If (A\subset \mathbb N) has asymptotic density $0$, then (s^{-1}(A)={n:,s(n)\in A}) also has asymptotic density $0$.

This is explicitly stated as a conjecture and is still described as open “in general” in modern references. ([mpim-bonn.mpg.de][1])

### What *is* known

There are several important partial results / special cases.

* **Uniform result for very sparse sets $A$** (no structure needed):
  Pollack–Pomerance–Thompson prove a “weak form” of the conjecture: if (\epsilon(x)\to 0) and
  [
  |A\cap[1,x]|\ \le\ x^{1/2+\epsilon(x)},
  ]
  then
  [
  |\\{n\le x:\ s(n)\in A\\}|=o(x).
  ]
  In particular, the EGPS conclusion holds for infinite sets with counting function (O(x^{1/2+o(1)})). 

* **Specific density-zero sets $A$** where the conjecture has been verified (using extra structure), including:

  * $A$ = **the primes** [[nomath]](then $|\\{n\le x:\ s(n)\in A\\}|=O(x/\log x)$)[[/nomath]]. 
  * $A$ = sets defined by **large deviations of (\omega(m))** (number of distinct prime factors) from its normal order. 
  * $A$ = **palindromes** in a fixed base. 
  * $A$ = **integers with missing digits** (“ellipsephic” sets): a 2023/2024 work shows the EGPS conjecture holds for these sets and gives quantitative bounds. ([arXiv][2])

### Why it’s nontrivial

A key difficulty is that $s(\cdot)$ can have **very large fibers** (many preimages for the same value). In fact, Pollack–Pomerance–Thompson disprove an auxiliary “bounded fiber” hypothesis that EGPS noted would imply the conjecture. 

At the same time, probabilistic results suggest $s(n)$ often behaves like a “typical” integer of comparable size [[nomath]](e.g., classical work of Davenport implies $s(n)/n$ has a continuous distribution function)[[/nomath]], which is part of the heuristic reason people expect the conjecture to be true. 

### Bottom line

* Your statement is **exactly the EGPS conjecture**.
* It is **open in general**.
* It is **proved** for many interesting special sets $A$, and for all $A$ that are *extremely sparse* in the quantitative sense (|A\cap[1,x]|\le x^{1/2+o(1)}). 

If you tell me what kind of density-zero set $A$ you care about (e.g., squares, smooth numbers, missing digits, thin multiplicative sets, etc.), I can point to the strongest known result in that direction and sketch why it works.

[1]: https://www.mpim-bonn.mpg.de/node/13701 "Preimages of the sum of proper divisors function | Max Planck Institute for Mathematics"
[2]: https://arxiv.org/abs/2307.12859 "[2307.12859] Sums of proper divisors with missing digits"

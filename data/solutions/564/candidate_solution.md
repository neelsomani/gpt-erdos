No — this is **not known**. In fact, your inequality is essentially **Erdős’s famous conjecture** about the *diagonal* 3‑uniform hypergraph Ramsey number.

Write (R_3(n)=r_3(n,n)). The best general bounds currently known are of the form
[
2^{c_1 n^{2}} < r_3(n,n) < 2^{2^{c_2 n}}
]
for absolute constants (c_1,c_2>0). 
So we have only a **single exponential in (n^2)** lower bound, but a **double exponential in $n$** upper bound.

## The specific bound you ask for

Your question asks whether there exists (c>0) such that
[
r_3(n,n)\ \ge\ 2^{2^{c n}}.
]
This is exactly the conjecture stated [[nomath]](for $n\ge 4$)[[/nomath]] in standard surveys:

> **Conjecture (Erdős).** (r_3(n,n) > 2^{2^{c n}}) for some absolute (c>0). 

It remains one of the central open problems in hypergraph Ramsey theory. 

## Why the usual “stepping-up” route doesn’t settle it

A natural thought is to “step up” from graph Ramsey lower bounds. The obstacle is that the classical Erdős–Hajnal stepping‑up lemma in the 2‑color setting **requires starting at uniformity (k\ge 3)**:
[
\text{If }k\ge 3\text{ and }N\nrightarrow (n)^{k}*\ell,\ \text{ then }2^N\nrightarrow (2n+k-4)^{k+1}*\ell.
]
([people.math.ethz.ch][1])

There *is* a stepping‑up from $k=2$ to $k=3$, but **the number of colors jumps from 2 to 4**. ([people.math.ethz.ch][1])
As a consequence, a double‑exponential lower bound **is known for 4 colors** in the 3‑uniform case:
[
r_3(n;4)\ \ge\ 2^{2^{c n}},
]
but this does not imply the same for 2 colors. 

## What *is* known unconditionally (lower bound idea)

The lower bound (r_3(n,n)\ge 2^{c n^2}) comes from a standard probabilistic construction (random 2‑coloring of triples), and is recorded as the best known order of magnitude on the lower side in modern references. 

## Status summary

* Your desired bound (r_3(n,n)\ge 2^{2^{c n}}): **open** (Erdős conjecture). 
* Best known lower bound: (2^{\Theta(n^2)}). 
* Best known upper bound: (2^{2^{O(n)}}). 
* There is even “some evidence” discussed in the literature that Conjecture 3.1 might fail, though it’s far from resolved. 

So the honest answer is: **we don’t currently know any (c>0) for which (R_3(n)\ge 2^{2^{cn}}) holds for all large $n$**, and proving it would be a major breakthrough.

[1]: https://people.math.ethz.ch/~sudakovb/stepping-up-lemma.pdf "An improved bound for the stepping-up lemma"

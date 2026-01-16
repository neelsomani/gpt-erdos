This is a well‑known Erdős–Rothschild problem. Most papers write your $f_c(n)$ as $h(n,c)$. 

## What is known

### 1) There is a sharp change at (c=\tfrac14)

#### If (c>\tfrac14), then (f_c(n)) is linear in $n$

A classical result of Edwards (unpublished) and independently Khadžiivanov–Nikiforov says that any $n$-vertex graph with more than $n^2/4$ edges has an edge contained in at least $n/6$ triangles. So for every fixed (c>\tfrac14),
[
f_c(n)\ge \frac{n}{6}.
]


In fact there is a stronger “for all (m>n^2/4)” inequality (stated as a corollary by Bollobás–Nikiforov):
[
bk(G)\ \ge\ \frac{2m}{n}-\frac{n}{3}\qquad (m>n^2/4),
]
so with (m=cn^2) this gives
[
f_c(n)\ \ge\ (2c-\tfrac13)n \qquad (c>\tfrac14).
]


So in this range you really have
[
f_c(n)=\Theta(n).
]

#### If (0<c<\tfrac14), then $f_c(n)$ can be *subpolynomial*

Fox and Loh constructed graphs with edge density arbitrarily close to $1/4$, **every edge in a triangle**, but with **no edge in more than (n^{O(1/\log\log n)})** triangles [[nomath]](they even give an explicit bound $n^{14/\log\log n}$ in a main construction)[[/nomath]]. 

This implies that for every fixed (c<\tfrac14),
[
f_c(n)\ \le\ n^{O(1/\log\log n)}\ =\ n^{o(1)}.
]


[[nomath]](Older work of Alon–Trotter gave the weaker upper bound $f_c(n)\ll_c \sqrt{n}$ for $c<1/4$.)[[/nomath]] ([Erdős Problems][1])

### 2) Lower bounds for (c<\tfrac14) are still very weak

Szemerédi (via regularity / triangle removal) showed that for every fixed (c>0), (f_c(n)\to\infty). 

Quantitatively, what one can currently extract is extremely slow growth. Fox–Loh explain that using the best known quantitative triangle‑removal bounds gives a lower bound only **exponential in $\log^* n$** (the iterated logarithm). 

So, for fixed (c<1/4), the best published general shape is something like
[
2^{\Omega(\log^* n)}\ \lesssim\ f_c(n)\ \le\ n^{O(1/\log\log n)}.
]


Also, the problem is tightly linked to the triangle removal lemma and to Roth‑type additive combinatorics statements, which is a big reason the lower bounds are hard to improve. 

## Answers to your two specific questions

### “Is it true that (f_c(n)>n^{\epsilon}) for some (\epsilon>0)?”

* If (c>\tfrac14): yes, much stronger, (f_c(n)=\Theta(n)) [[nomath]](at least $n/6$, and in fact $(2c-\tfrac13)n$)[[/nomath]]. 
* If (c<\tfrac14): no. Fox–Loh give (f_c(n)\le n^{o(1)}), which kills any fixed power (n^\epsilon). 

### “Is (f_c(n)\gg \log n)?”

For (c<\tfrac14), this is **not known** from the standard references: the best general lower bounds are still far smaller than (\log n) (they come from removal/regularity‑type arguments), and the best known upper bound is much larger than (\log n) (subpolynomial but still huge). ([Erdős Problems][1])

So the current picture is: **power of $n$** is false below $1/4$, but **(\log n)** is still wide open in that range.

[1]: https://www.erdosproblems.com/80 "
  
    Erdős Problem #80
  
"

What you wrote is exactly **Conjecture 1 of Erdős–Gyárfás (1999)** (“Split and balanced colorings of complete graphs”).  It is **proved for $r=3$ and $r=4$**, but **open for general (r\ge 5)** (as of Jan 19, 2026). ([Renyi Institute][1])

So: as a general theorem for all (r\ge 3), it is *not currently known*; what is known is the (r=3,4) proofs below. ([Erdős Problems][2])

---

## Reformulation that’s useful in the proofs

Let the $r$ colors be (1,2,\dots,r). For each color $i$, let (G_i) be the graph on the same vertex set whose edges are exactly the edges of color $i$.

Then a set $S$ of $r+1$ vertices has “**color $i$ missing**” on the induced (K_{r+1}) iff $S$ is an **independent set of size $r+1$** in (G_i) [[nomath]](i.e., no edges of color $i$ inside $S$)[[/nomath]].

So your statement is equivalent to:

> In every $r$-edge-coloring of (K_{r^2+1}), for some color $i$, the color‑$i$ graph (G_i) has (\alpha(G_i)\ge r+1).

---

## The case $r=3$: (K_{10}) always has a (K_4) missing a color

This is Erdős–Gyárfás’ Lemma 1. ([Renyi Institute][1])

Take a 3-coloring of (K_{10}). Let color 1 be a **minority color**, i.e. it appears on at most (\frac1{3}\binom{10}{2}=15) edges. Let (G_1) be the graph of color‑1 edges. ([Renyi Institute][1])

### 1) If (G_1) is 3-regular

Then (\Delta(G_1)=3). By **Brooks’ theorem**, either

* (G_1) contains a (K_4), in which case those 4 vertices span a (K_4) whose edges are all color 1, so colors 2 and 3 are missing; or
* (G_1) is 3-colorable, hence has an independent set of size at least (\lceil 10/3\rceil=4). Those 4 vertices have **no color‑1 edges**, so the induced (K_4) is missing color 1.

Either way we get 4 vertices with a missing color. ([Renyi Institute][1])

### 2) Otherwise (G_1) has a vertex of degree (\le 2)

Let (x_1) be such a vertex. Delete (x_1) and its neighbors in (G_1). This removes at most (1+2=3) vertices, leaving a set $X$ with (|X|\ge 7) such that (x_1) has **no color‑1 edges** to $X$. ([Renyi Institute][1])

* If (G_1[X]) has 3 independent vertices, together with (x_1) they form 4 independent vertices in (G_1), giving a (K_4) missing color 1.
* Otherwise, (G_1[X]) has no independent set of size 3. Since (|X|\ge 7 > R(3,3)=6), this forces (G_1[X]) to contain a triangle $Y$ (all three edges in color 1). ([Renyi Institute][1])

Now let (Z=X\setminus Y). A short case analysis (as in the paper) shows that either (G_1[Z]) is complete in color 1 [[nomath]](giving a monochromatic $K_4$)[[/nomath]] or one finds a (K_4) with only one non‑color‑1 edge [[nomath]](a $K_4-e$ in color 1)[[/nomath]], in both cases yielding 4 vertices whose induced (K_4) misses at least one of the 3 colors. ([Renyi Institute][1])

That proves the statement for $r=3$. ([Renyi Institute][1])

---

## The case $r=4$: (K_{17}) always has a (K_5) missing a color

This is Erdős–Gyárfás’ Lemma 2. ([Renyi Institute][1])

Take a 4-coloring of (K_{17}). Let color 1 be a minority color, so the color‑1 graph (G_1) has at most (\frac14\binom{17}{2}=34) edges. ([Renyi Institute][1])

### 1) If (G_1) is 4-regular

Then (\Delta(G_1)=4). Brooks’ theorem implies either (G_1) contains a (K_5) (done immediately), or (G_1) is 4-colorable, hence has an independent set of size (\lceil 17/4\rceil=5), which gives 5 vertices missing color 1. ([Renyi Institute][1])

### 2) Otherwise (G_1) has a vertex (x_1) of degree (\le 3)

Let $M$ be its neighbors in (G_1). Remove (x_1\cup M), and in the remaining induced subgraph find a vertex (x_2) of small degree [[nomath]](the paper shows one can take degree $\le 4$ there)[[/nomath]]. Let $N$ be the neighbors of (x_2) in that remaining part, and set
[
X = V \setminus ( {x_1,x_2}\cup M\cup N ).
]
Then (|X|\ge 8). ([Renyi Institute][1])

Now:

* If (G_1[X]) has 3 independent vertices, then together with (x_1,x_2) we get 5 independent vertices in (G_1), hence a (K_5) missing color 1.
* So assume (G_1[X]) has **no** 3 independent vertices. The proof then splits depending on whether (G_1[X]) contains a (K_4). If it does, a counting/structure argument (using an extra technical assumption that otherwise a 5-vertex set already forces a missing color) produces 5 independent vertices in (G_1). If it does not, then because (R(3,4)=9) and the extremal $8$-vertex $(3,4)$-Ramsey graph is essentially unique, (G_1[X]) must have a very specific structure (an 8-cycle with chords), and a careful edge count yields a contradiction to (|E(G_1)|\le 34). ([Renyi Institute][1])

Either way, one concludes there are 5 vertices missing some color. ([Renyi Institute][1])

So the statement holds for $r=4$. ([Renyi Institute][1])

---

## What is known (and not known) in general

* Erdős–Gyárfás explicitly state this as a **conjecture** for general (r\ge 3), and they prove it for (r=3,4). ([Renyi Institute][1])
* As of Jan 19, 2026, it is still listed as **open** (falsifiable) on the Erdős Problems site. ([Erdős Problems][2])
* The bound (r^2+1) would be **best possible** if true, because for infinitely many $r$ there are $r$-colorings of (K_{r^2}) in which *every* $r+1$ vertices span all colors (constructed from affine planes, with a small modification). ([Renyi Institute][1])

---

If you tell me whether you want $i$ a fully written-up proof for $r=3$ only, (ii) a full detailed write-up for $r=4$ (it’s longer), or (iii) a discussion of possible strategies for the open (r\ge 5) case, I’ll tailor the level of detail accordingly.

[1]: https://users.renyi.hu/~gyarfas/Cikkek/92_splitandbalanced.pdf "https://users.renyi.hu/~gyarfas/Cikkek/92_splitandbalanced.pdf"
[2]: https://www.erdosproblems.com/search_bib/Er99/no "https://www.erdosproblems.com/search_bib/Er99/no"

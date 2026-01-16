Let $G(A)$ be your graph.

## Clique number (\omega(G(A)))

A clique in $G(A)$ is exactly a set of points whose **pairwise distances are all integers** (an “integral point set”).

* **It cannot be infinite.** A classical theorem of Erdős–Anning (stated in modern form in later work) says that any set of points in the Euclidean plane with all pairwise distances integers is **either finite or collinear**. ([DROPS][1])
  Since your $A$ has **no three collinear**, every clique must be **finite**.

* **It can be at least 7.** Kreisel and Kurz exhibited **7 points** in the plane with

  * no three on a line,
  * no four on a circle,
  * and all pairwise distances integers. ([arXiv][2])
    So (\omega(G(A)) \ge 7) is achievable (and therefore (\chi(G(A))\ge 7) is achievable too).

* **Whether it can be (\ge 8) is open.** A 2021 survey-style paper explicitly says that **no example with 8 points in general position** (no three collinear and no four concyclic) is known. ([arXiv][3])

So, with your “general position” rules, the best current picture is:
[
7 \le \omega(G(A)) < \infty,
]
and it is not known whether (\omega) can be $8$ (or larger).

## Chromatic number (\chi(G(A)))

### A general upper bound: it is never bigger than countable

No matter what $A$ is (even if (A=\mathbb R^2)), you can always color the plane with **countably many** colors so that each color class has diameter (<1). For example, color each half-unit square
[
\Big[\tfrac{x}{2},\tfrac{x+1}{2}\Big)\times \Big[\tfrac{y}{2},\tfrac{y+1}{2}\Big)
]
with the color ((x,y)\in\mathbb Z^2). Davies writes this down explicitly as a countable coloring (he uses it for odd distances, but the same idea works for **all integer distances**, since all integers (\ge 1)). ([arXiv][4])

Because any two points in one such square are at distance (<1), they cannot be an integer distance apart. Restricting this coloring to $A$ gives:
[
\chi(G(A)) \le \aleph_0.
]
So if (\chi(G(A))) is “infinite”, it can only mean **countably infinite**.

### Known lower bounds

* From the 7-point integral heptagon [[nomath]](a $K_7$)[[/nomath]], you can make an **infinite** $A$ with (\chi(G(A))\ge 7): take those 7 points, then add infinitely many extra points chosen so that they create no new integer distances and keep the “no 3 collinear / no 4 concyclic” property. (This is doable because at each step you only avoid countably many bad lines/circles.)

So at least:
[
\chi(G(A)) \ge 7
]
is possible.

### Can (\chi(G(A))) be infinite [[nomath]](i.e. $\aleph_0$)[[/nomath]] under your constraints?

This is exactly the hard part, and **it is still open** as an Erdős problem (Problem #130 on the Erdős Problems site). ([Erdős Problems][5])

So, with your conditions (no three collinear, no four concyclic), nobody currently knows whether one can force (\chi(G(A))=\aleph_0).

## Important contrast (to avoid confusion)

If you **do not** impose the “general position” condition on $A$, then infinite chromatic number definitely happens. For the whole plane, Davies proved that **every finite coloring** produces a monochromatic pair at an odd integer distance, so the odd-distance graph has **no finite coloring**, and since a countable coloring exists, its chromatic number is **countably infinite**. ([arXiv][4])
This immediately shows “infinite chromatic number” is possible in the unrestricted plane setting—but it does **not** settle the Erdős question for sets with *no three collinear and no four concyclic*.

## Summary

* (\omega(G(A))) is **always finite**; in fact no infinite clique can exist. ([DROPS][1])
* (\omega(G(A))) can be **at least 7**, and $7$ is the largest value we can currently certify in general position. ([arXiv][2])
* (\chi(G(A))) is **always (\le \aleph_0)** (countably colorable). ([arXiv][4])
* (\chi(G(A))) can be **at least 7**.
* Whether (\chi(G(A))) can be **infinite** [[nomath]](i.e. $\aleph_0$)[[/nomath]] under your “no 3 collinear, no 4 concyclic” rules is **open**. ([Erdős Problems][5])

[1]: https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.46/LIPIcs.SoCG.2025.46.pdf "Non-Euclidean Erdős–Anning Theorems"
[2]: https://arxiv.org/pdf/0804.1303 "https://arxiv.org/pdf/0804.1303"
[3]: https://arxiv.org/pdf/2102.12462 "https://arxiv.org/pdf/2102.12462"
[4]: https://arxiv.org/pdf/2209.15598 "https://arxiv.org/pdf/2209.15598"
[5]: https://www.erdosproblems.com/130 "https://www.erdosproblems.com/130"

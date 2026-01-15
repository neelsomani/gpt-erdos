This is **still open**.

People usually write your function as
[
D_{\text{gen}}(n)=\min{#\text{distinct distances determined by }n\text{ points in }\mathbb R^2\text{ in general position}},
]
where “general position” means **no three collinear and no four cocircular** (same as in your question). It is *not known* whether (D_{\text{gen}}(n)) is (\Theta(n)) or grows faster than linear. 

### What is known (roughly)

**Lower bound (what you can always guarantee):**
Because your sets have **no three on a line**, one can prove a linear bound
[
h(n)\ \ge\ \left\lceil\frac{n-1}{3}\right\rceil.
]
This comes from a counting argument about isosceles triangles / perpendicular bisectors (Szemerédi’s argument, presented in surveys). 

So at least we know (h(n) = \Omega(n)). But that does **not** force (h(n)/n \to \infty); it only says $h(n)/n$ stays above a positive constant. 

**Upper bound (there exist “bad” examples with not too many distances):**
There are explicit constructions of $n$ points in this strong general position that determine at most
[
h(n)\ \le\ n,2^{O(\sqrt{\log n})}
]
distinct distances (equivalently (n\exp(O(\sqrt{\log n})))). The idea is: start with a high‑dimensional integer grid, take many grid points lying on one sphere, then project generically to the plane so you keep “no 3 on a line / no 4 on a circle” but still keep relatively few distances. 

An older bound of Pach gives a weaker (bigger) upper bound
[
h(n) < n^{\log_2 3}.
]
([Erdős Problems][1])

### So what about (h(n)/n\to\infty)?

Right now we only know
[
\frac{1}{3}\ \lesssim\ \frac{h(n)}{n}\ \lesssim\ 2^{O(\sqrt{\log n})}.
]
The upper bound factor (2^{O(\sqrt{\log n})}) does go to infinity, but it is only an **upper bound** (it just says “there exists a construction with at most this many distances”). It does *not* prove that $h(n)/n$ must go to infinity. 

So the honest answer is:

* We **do not know** whether $h(n)$ must be **superlinear**.
* Equivalently, we **do not know** whether there is a construction in general position with only $O(n)$ distinct distances, or whether every such set forces (n\cdot\omega(1)) distances. 

If you want, I can also sketch the cube/grid-on-sphere projection idea (why it keeps “general position”) and why it gives only $n2^{O(\sqrt{\log n})}$ distances, in a few clean steps.

[1]: https://www.erdosproblems.com/forum/thread/98 "

    Erdős Problem #98 - Discussion thread

"

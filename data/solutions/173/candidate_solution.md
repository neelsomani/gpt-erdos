This is **an open problem** in Euclidean Ramsey theory (it is listed as Erdős Problem #173). ([Erdős Problems][1])

### Why the “at most one triangle” part is needed

There are 2-colourings of the plane that **avoid a monochromatic copy of one fixed equilateral triangle**. A standard example is a “striped” colouring: colour the plane in alternating parallel strips of width (\sqrt{3}/2); this avoids a monochromatic **unit** equilateral triangle. 

So you cannot hope for “every triangle $T$ always appears”; you really may have to allow one exception.

### What is known

* **Every right triangle is forced.**
  Shader proved that for **any fixed right triangle** $T$, every 2-colouring of (\mathbb{R}^2) contains a monochromatic congruent copy of $T$. ([Computer Science at UMD][2])

* There are results for “nice” colourings (with some regularity in the boundary between the two colours).
  For example, for a partition into a **closed** set and an **open** set, you always get a monochromatic copy of any 3-point pattern (so in particular any triangle). And for “polygonal” boundaries, every **non-equilateral** triangle appears. ([Springer][3])

### A very useful reduction: it is really about equilateral triangles

Jelínek (and coauthors) proved facts that link arbitrary triangles to equilateral ones:

* A colouring contains **every triangle** if and only if it contains **every equilateral triangle**. 
* A colouring contains **every non-equilateral triangle** if and only if it contains **all equilateral triangles of all side lengths except possibly one**. 

So Erdős Problem #173 can be thought of like this:

> In any 2-colouring of the plane, there is **at most one side length (a_0)** for which the equilateral triangle of side (a_0) might be missing; all other equilateral triangles (and hence all other triangles) must appear.

That is exactly the “all but at most one triangle” idea, just rewritten in a more concrete way. 

### Current status

As of the last update on the Erdős Problems site (edited **Oct 16, 2025**), the problem is still **open**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/173 "
  
    Erdős Problem #173
  
"
[2]: https://www.cs.umd.edu/~gasarch/TOPICS/ERT/ShaderRightTri.pdf?utm_source=chatgpt.com "(A) 20, 385-389 (1976) Note All Right Triangles Are ..."
[3]: https://link.springer.com/article/10.1007/s00493-009-2291-y "Monochromatic triangles in two-colored plane | Combinatorica | Springer Nature Link"

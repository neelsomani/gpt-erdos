No.

A counterexample is given by a recent construction of **Reiher, Rödl, and Sales**. Specialising their result to $k=3$, they construct [[nomath]](for any $\mu\in(0,2/3)$)[[/nomath]] a set (X\subset\mathbb N) such that:

1. **(Local large 3AP-free subsets)** Every finite (Y\subseteq X) contains a subset (Z\subseteq Y) with
   [
   |Z|\ge \mu |Y|
   ]
   and $Z$ contains **no three-term arithmetic progression**.

2. **(Global “van der Waerden” property)** For **every** finite number of colours $r$, **every** $r$-colouring of $X$ contains a **monochromatic** three-term arithmetic progression. ([arXiv][1])

Property $1$ is exactly your hypothesis [[nomath]](take $\epsilon=\mu$)[[/nomath]]. But $2$ implies $X$ **cannot** be a union of finitely many 3AP-free sets: if (X=\bigcup_{i=1}^m X_i) with each (X_i) 3AP-free, then colouring each (X_i) with colour $i$ gives an $m$-colouring with **no** monochromatic 3AP—contradicting $2$.

So the answer to your question is **false**. ([arXiv][1])

[1]: https://arxiv.org/abs/2311.08556 "[2311.08556] Colouring versus density in integers and Hales-Jewett cubes"

This is (literally) one of Erdős’s $25 problems: a full **classification is still open**. ([Erdős Problems][1])
But there is a fairly sharp *partial* classification that captures a huge (“generic”) class of triangles, and it explains why “only squares” is the typical behavior.

## Setup

Say a triangle $T$ is **square-only** if whenever $T$ is dissected into $N$ pairwise **congruent** triangles, then $N$ must be a perfect square.

Two baseline facts:

1. **Every** triangle can be cut into $n^2$ congruent triangles [[nomath]](for every $n\ge 1$)[[/nomath]] by the standard “divide each side into $n$ equal parts and draw parallels” construction. ([Erdős Problems][1])

2. Erdős’s question is to classify those triangles for which **no non-square $N$** is possible. This is open. ([Erdős Problems][1])

## A big sufficient class (Soifer)

Soifer proved there exist triangles that are square-only [[nomath]](one explicit example has side lengths $\sqrt2,\sqrt3,\sqrt4$)[[/nomath]], and in fact he gives a broad sufficient condition:

> If a triangle’s **angles** are integrally independent and its **side lengths** are integrally independent, then it can be cut into congruent triangles **only** in a square number of pieces. ([Erdős Problems][1])

### What “integrally independent” means here

For real numbers $x_1,x_2,x_3$, “integrally independent” means the only integer solution of
[
m_1x_1+m_2x_2+m_3x_3=0
]
is $m_1=m_2=m_3=0$.

So for a triangle with angles $A,B,C$ this means there is **no** nontrivial integer relation
[
mA+nB+pC=0,
]
and similarly for the side lengths. In Soifer’s text you can see this notion used immediately, e.g. he notes right triangles have integrally *dependent* angles since $A+B-C=0$ [[nomath]](with integers $1,1,-1$)[[/nomath]]. ([Academia][2])

## Why that condition forces “only squares” (proof sketch)

Assume $T$ has integrally independent angles and sides, and suppose $T$ is cut into $N$ congruent triangles.

### Step 1: Angle independence forces the tiles to be similar to the big triangle

Because “congruent” implies “similar,” Soifer’s Tool 2.1 applies: if $T$ has integrally independent angles and it is cut into triangles similar to each other, then **each tile is similar to $T$**, and the corner angles are not split. ([Academia][2])

So here the $N$ congruent tiles are actually **$N$ smaller copies of the same shape as $T$**.

### Step 2: Turn the side decompositions into a matrix equation

Let the tile have side lengths $a,b,c$. Since the tile is similar to $T$ and there are $N$ tiles, the side lengths of $T$ are $a\sqrt N, b\sqrt N, c\sqrt N$ [[nomath]](scale factor $\sqrt N$)[[/nomath]].

Now walk along each side of $T$: it is subdivided into edges of tiles, each of which has length $a$, $b$, or $c$. This yields a system of the form (Soifer writes it explicitly) ([Academia][2])
[
\begin{aligned}
a\sqrt N &= a_{11}a+a_{12}b+a_{13}c,\
b\sqrt N &= a_{21}a+a_{22}b+a_{23}c,\
c\sqrt N &= a_{31}a+a_{32}b+a_{33}c,
\end{aligned}
]
with all $a_{ij}\in\mathbb{Z}_{\ge 0}$.

In vector form:
[
A\begin{pmatrix}a\ b\ c\end{pmatrix}
=

\sqrt N \begin{pmatrix}a\ b\ c\end{pmatrix},
]
so $\sqrt N$ is an eigenvalue of a $3\times 3$ integer matrix.

### Step 3: If $N$ isn’t a square, the sides become rationally dependent

If $N$ is not a square, then $\sqrt N$ is irrational of degree $2$, so its conjugate $-\sqrt N$ must also be a root of the characteristic polynomial (integer coefficients). In a cubic characteristic polynomial, that forces $\sqrt N$ to have algebraic multiplicity $1$, hence a **1‑dimensional** eigenspace.

That implies the ratios $b/a$ and $c/a$ are determined by solving linear equations with coefficients in $\mathbb{Q}(\sqrt N)$, so
[
\frac{b}{a},\frac{c}{a}\in \mathbb{Q}(\sqrt N).
]
Therefore
[
b = a(p+q\sqrt N),\quad c=a(r+s\sqrt N)
]
for rationals $p,q,r,s$, so $a,b,c$ all lie in the $\mathbb{Q}$‑span of ${a,a\sqrt N}$, a 2‑dimensional $\mathbb{Q}$‑vector space. Hence $a,b,c$ are $\mathbb{Q}$‑linearly dependent, giving a nontrivial integer relation among them—contradicting **integral independence of the side lengths**.

So $N$ must be a perfect square.

That is the core mechanism behind Soifer’s sufficient condition. ([Erdős Problems][1])

## What we can say beyond that (and what we can’t)

### What is known (and useful as “classification data”)

* **There really are square-only triangles**, e.g. one with side lengths $\sqrt2,\sqrt3,\sqrt4$, and more generally triangles with integrally independent angles and sides. ([Erdős Problems][1])
* There are also many **explicit non-square tilings**, so lots of triangles are *not* square-only:

  * A $30$–$60$–$90$ triangle can be cut into **3** congruent triangles. ([MathOverflow][3])
  * Right triangles with leg ratio $a:b$ can be tiled into $a^2+b^2$ congruent triangles (a sum of two squares), giving many non-squares. ([MathOverflow][3])
  * Soifer also records general constructions yielding $2n^2$, $3n^2$, $6n^2$, and “sum of two squares” counts for *some* triangles. ([Academia][2])
* There is significant research on which **numbers $N$** can occur at all; e.g. work summarized on MathOverflow mentions results ruling out $N=7,11,19,23$ and conjectures restricting possible forms of $N$. ([MathOverflow][3])

### What remains open

The **complete “if and only if” characterization** of square-only triangles is open (Erdős problem #633 / Soifer problem 6.6). ([Erdős Problems][1])
So at present we have:

* a **large sufficient family** (integrally independent angles + sides), and
* many **explicit families that are not square-only**, but
* no definitive boundary that captures *all* square-only triangles and *only* those.

## Practical “classification” you can use today

If you want a working decision tree:

* If the triangle is **isosceles**, it is *not* square-only (cut by the altitude into 2 congruent triangles).
* If it is **equilateral**, it is *not* square-only (there are non-square tilings, e.g. into 6 congruent triangles via medians).
* If it is a **right triangle with rational leg ratio**, it is typically *not* square-only because of $a^2+b^2$ tilings. ([MathOverflow][3])
* If its **angles** and **side lengths** are both **integrally independent**, then it **is square-only** (Soifer). ([Erdős Problems][1])
* Everything else falls into the still-open “boundary region,” where some triangles may or may not be square-only and current theory is incomplete.

If you tell me a specific triangle (angles or side lengths), I can:

* check obvious non-square constructions (isosceles/right/special-angle cases), and
* check whether it satisfies Soifer’s sufficient integrally-independent condition (often straightforward if the sides are like distinct square roots, etc.).

[1]: https://www.erdosproblems.com/633 "
  
    Erdős Problem #633
  
"
[2]: https://www.academia.edu/120841193/How_Does_One_Cut_A_Triangle "https://www.academia.edu/120841193/How_Does_One_Cut_A_Triangle"
[3]: https://mathoverflow.net/questions/67199/subdivision-of-triangles-into-congruent-triangles "https://mathoverflow.net/questions/67199/subdivision-of-triangles-into-congruent-triangles"

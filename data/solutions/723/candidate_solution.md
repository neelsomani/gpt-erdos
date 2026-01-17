This is **not known in general**. The statement

> If a finite projective plane of order $n$ exists, then $n$ is a prime power

is the **Prime Power Conjecture** for finite projective planes, and it remains open as of now. 

A bit of context and what *is* known:

## Why prime powers show up

If $q$ is a **prime power**, there is a standard construction of a projective plane of order $q$, namely the Desarguesian plane (\mathrm{PG}(2,q)) built from the finite field (\mathbb{F}_q). In one common description, points are 1‑dimensional subspaces of (\mathbb{F}_q^3) [[nomath]](equivalence classes $[x_0,x_1,x_2]$ up to nonzero scalar multiple)[[/nomath]], and lines are given by homogeneous linear equations (a_0x_0+a_1x_1+a_2x_2=0). 

So “prime power (\Rightarrow) exists” is known. The hard direction is the converse.

## What your definition implies

Your definition is exactly a Steiner 2‑design with parameters
[
v=n^2+n+1,\qquad k=n+1,\qquad \lambda=1,
]
i.e. every pair of “points” lies on a unique “line”.

From that one can quickly derive the usual projective plane counting facts:

* Each point lies on
  [
  r=\frac{v-1}{k-1}=\frac{n^2+n}{n}=n+1
  ]
  lines.
* The number of lines is
  [
  b=\frac{v(v-1)}{k(k-1)}=\frac{(n^2+n+1)(n^2+n)}{(n+1)n}=n^2+n+1=v.
  ]

So it matches the standard notion of a finite projective plane of order $n$.

## Strong necessary conditions: Bruck–Ryser–Chowla

A key general obstruction is the **Bruck–Ryser–Chowla theorem**. In the projective plane case it says:

> If a projective plane of order $n$ exists and (n\equiv 1) or (2\pmod 4), then
> [
> n=x^2+y^2
> ]
> for some integers (x,y). ([Theorem of the Day][1])

This immediately rules out infinitely many non–prime-power orders [[nomath]](e.g. $6,14,21,22,\dots$)[[/nomath]]. ([Theorem of the Day][1])

But it is **not** sufficient: (10=1^2+3^2) passes this test, yet no plane of order (10) exists. ([Theorem of the Day][1])

## Small orders and the first open case

* Order $6$: does not exist (ruled out by Bruck–Ryser, and also classically connected to Euler’s $36$ officers / orthogonal Latin squares). 
* Order $10$: does not exist (computer-assisted proof by Lam and collaborators). ([Theorem of the Day][1])
* The smallest order that is **not a prime power** and is **not** eliminated by Bruck–Ryser–Chowla is (n=12), and its existence is still open. 

## Bottom line

So the best honest answer is:

* **Conjectured:** yes, $n$ must be a prime power. 
* **Known:** prime powers work; many non–prime powers are impossible by number-theoretic obstructions; specific cases like (n=6) and (n=10) are ruled out. 
* **Unknown:** whether any projective plane exists for a non–prime-power order [[nomath]](e.g. $12$)[[/nomath]]. 

[1]: https://www.theoremoftheday.org/CombinatorialTheory/BruckRyserChowla/TotDBRC.pdf "Bruck-Ryser-Chowla Theorem"

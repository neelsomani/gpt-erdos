This is an Erdős problem (often listed as “Erdős problem #92”), and as far as the current literature shows it is **still open**. ([Erdős Problems][1])

What *is* known is a fairly wide gap:

## Best known bounds (as of late 2025)

There are absolute constants (c,C>0) such that
[
n^{,c/\log\log n}\ \le\ f(n)\ \le\ C,n^{4/11}.
]
The lower bound comes from lattice-type constructions, and the upper bound comes from point–circle incidence bounds. ([Erdős Problems][1])

So at the moment we **cannot** prove (f(n)\le n^{o(1)}), and we also **cannot** prove an upper bound as small as (n^{O(1/\log\log n)}). ([Erdős Problems][1])

## Why the current best upper bound is (n^{4/11})

Assume a set (A) of (n) points has the property with parameter (k):
for every (x\in A) there is some radius (r_x>0) such that at least (k) *other* points of (A) lie on the circle centered at (x) with radius (r_x).

Pick one such circle for each (x). Then you have:

* a set (P=A) of (m=n) points, and
* a set (C) of (n) circles (one per center (x)),

with at least
[
I(P,C)\ \ge\ nk
]
point–circle “hits” (incidences).

Now use the known incidence bound for (m) points and (n) circles:
[
I(P,C)=O!\left(m^{2/3}n^{2/3};+;m^{6/11}n^{9/11};+;m;+;n\right).
]
This is stated (for circles) as part of Corollary 1.12 in the Janzer–Janzer–Methuku–Tardos work. 

Put (m=n). The dominant term becomes (n^{15/11}). So
[
nk \ \le\ O(n^{15/11}) \quad\Rightarrow\quad k \le O(n^{4/11}).
]
Hence (f(n)\ll n^{4/11}). ([Erdős Problems][1])

(Older work gave a weaker exponent (2/5), and the completely “trivial” incidence bound gives (1/2). ([Erdős Problems][1]))

## Why the lattice gives (f(n)\ge n^{c/\log\log n})

Take a large chunk of the integer lattice (a big (\sqrt{n}\times \sqrt{n}) grid, trimming a boundary strip so every point is “far from the edge”).
Then for each point (x), if you choose a squared radius (m) with many representations as a sum of two squares,
[
m=a^2+b^2,
]
you get many lattice points at distance (\sqrt m) from (x), just by translating the vectors ((a,b)).

Choosing (m) to have many prime factors (\equiv 1 \pmod 4) makes the number of such representations (hence the number of lattice points on that circle) about
[
\exp!\big(\Theta(\log m/\log\log m)\big)
= m^{\Theta(1/\log\log m)}.
]
With (m) on the order of (n), this gives
[
f(n)\ \ge\ n^{c/\log\log n}
]
for some (c>0). This is exactly the standard “lattice points” lower bound mentioned in the problem’s references. ([Erdős Problems][1])

## Answer to your two questions

* **Is (f(n)\le n^{o(1)})?**
  **Unknown.** The best published upper bound is still a fixed power (n^{4/11}), far from subpolynomial. ([Erdős Problems][1])

* **Is (f(n) < n^{O(1/\log\log n)})?**
  Also **unknown** as an upper bound. Note this would be close to tight (up to constants in the exponent), because the lattice already gives (f(n)\ge n^{c/\log\log n}). ([Erdős Problems][1])

If you want, I can also write out the lattice construction more explicitly (how to choose (m), how big a boundary strip you remove, and what (n) you end up with), or explain how the incidence bound is plugged in step-by-step.

[1]: https://www.erdosproblems.com/92 "
  
    Erdős Problem #92
  
"

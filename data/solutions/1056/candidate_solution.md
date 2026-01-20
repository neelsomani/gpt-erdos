Write the consecutive intervals as
[
I_i=[a_i,b_i]\cap\mathbb Z,\qquad b_i+1=a_{i+1}.
]
If some interval contains a multiple of $p$, then its product is (0\pmod p), impossible. Hence **none of the integers in**
[
[a_1,b_k]
]
is divisible by $p$. But among any $p$ consecutive integers there is a multiple of $p$, so necessarily
[
b_k-a_1+1<p.
]
After subtracting a suitable multiple of $p$ from all endpoints, we may assume (1\le a_1\le b_k\le p-1).

Now set (c_0=a_1-1) and (c_i=b_i) for (i=1,\dots,k). Then
[
\prod_{n\in I_i} n=\frac{c_i!}{c_{i-1}!}\pmod p,
]
so the condition (\prod_{n\in I_i}n\equiv1\pmod p) for all $i$ is equivalent to
[
c_i!\equiv c_{i-1}!\pmod p\quad\text{for all }i,
]
i.e.
[
c_0!\equiv c_1!\equiv\cdots\equiv c_k!\pmod p.
]

So your question is equivalent to:

> Does there exist a prime $p$ for which the sequence (0!,1!,2!,\dots,(p-1)!\pmod p) takes some value at least $k+1$ times?

[[nomath]](Then one may take $I_i=[c_{i-1}+1,c_i]$.)[[/nomath]]

## What we can say unconditionally

### $k=2$: always yes [[nomath]](for any odd prime $p\ge 5$)[[/nomath]]

Take (p\ge5) prime and
[
I_1=[1,1],\qquad I_2=[2,p-2].
]
Then (\prod_{n\in I_1}n=1). And by Wilson,
[
(p-1)!\equiv -1\pmod p \implies (p-2)!=\frac{(p-1)!}{p-1}\equiv\frac{-1}{-1}\equiv1\pmod p,
]
so
[
\prod_{n\in I_2}n=\frac{(p-2)!}{1!}\equiv 1\pmod p.
]

### Concrete examples for larger $k$

These come from primes where (n!\equiv 1\pmod p) has many solutions $n$.

* $k=4$: take $p=17$. One checks
  [
  0!,1!,5!,11!,15!\equiv 1\pmod{17}.
  ]
  Hence the consecutive intervals
  [
  [1,1],\ [2,5],\ [6,11],\ [12,15]
  ]
  each have product (1\pmod{17}).

* $k=5$: take $p=23$. One checks
  [
  0!,1!,4!,8!,11!,21!\equiv 1\pmod{23},
  ]
  so
  [
  [1,1],\ [2,4],\ [5,8],\ [9,11],\ [12,21]
  ]
  works.

* $k=10$: take $p=3011$. One finds
  [
  n!\equiv 1\pmod{3011}\quad\text{for }n\in{0,1,611,723,749,805,2205,2261,2287,2399,3009},
  ]
  giving (10) consecutive intervals between these endpoints whose products are all (1\pmod{3011}).

* $k=12$: take $p=52163$. One finds (n!\equiv1\pmod{52163}) for
  [
  n\in{0,1,3924,7291,7427,18519,24931,26081,27231,33643,44735,44871,52161},
  ]
  which yields (12) consecutive intervals with product (1\pmod{52163}).

## Status for general $k$

In the language used in the literature, asking for such a prime $p$ is asking whether, for each $k$, the factorial map (x\mapsto x!\pmod p) has a value hit at least $k+1$ times [[nomath]](a “$(k+1)$-ramification point”)[[/nomath]]. This sits inside a circle of open problems and conjectures about how “random” the factorial residues behave modulo a prime; heuristics predict that higher-multiplicity hits should occur for large $p$, but this behavior is treated as conjectural rather than proven in general. 

So:

* **Yes for $k=2$** (elementary, Wilson).
* **For larger $k$**, there are **many explicit examples** (as above), but a general theorem guaranteeing existence **for every** $k$ is not something I can point to as proved in the current literature; it is closely tied to these ramification/multiplicity questions about factorial residues. 

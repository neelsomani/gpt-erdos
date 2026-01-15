This is a real Ramsey-type problem of Erdős–Rado, and it is **not known in general**. In the literature your number is usually written as
[
k(n,m)=r(I_n,L_m),
]
the least (k) so that every **oriented** graph on (k) vertices has either an independent set of size (n) or a **transitive tournament** (acyclic tournament) of size (m). The full exact formula for all (n,m) is open.

## Easy exact cases

* **(m=2)**: a transitive tournament of size 2 is just one directed edge, so
  [
  k(n,2)=n.
  ]
* **(n=2)**: then you are asking for the least size forcing a transitive subtournament of order (m) in a tournament. The standard bound is (2^{m-1}) (and it is tight in the tournament setting).

## General bounds in terms of ordinary Ramsey numbers

Let (R(a,b)) be the usual (undirected) Ramsey number.

A basic comparison is
[
R(n,m)\ \le\ k(n,m)\ \le\ R!\bigl(n,2^{m-1}\bigr).
]
This is stated in the recent work of Ihringer–Rajendraprasad–Weinert (they write it as (r(m,n)\le r(I_m,L_n)\le r(m,2^{n-1}))).

So, even if you cannot “determine” (k(n,m)) exactly, you can always trap it between known Ramsey-type quantities.

## Polynomial upper bounds (fixed (m), large (n))

Erdős–Rado proved an explicit bound of the form “constant depending on (m)” times (n^{m-1}); one concrete version written on the Erdős Problems page is
[
k(n,m)\ \le\ \frac{2^{m-1}(n-1)^m+n-2}{2n-3},
]
so in particular (k(n,m)=O_m(n^{m-1})).

A stronger modern bound (with the right kind of log saving) is:

For (n,m>2),
[
k(n,m)=r(I_n,L_m)\ \le\ 2^{19m},\frac{n^{m-1}}{(\log_2 n)^{m-2}}.
]
(This is Theorem 4.6 in the same paper, after swapping their parameter names to match yours.)

## What is known exactly for (m=3)

The case “force a transitive triangle” is much better understood.

* Bermond proved
  [
  k(3,3)=9.
  ]
* Ihringer–Rajendraprasad–Weinert proved
  [
  k(4,3)=15,\qquad k(5,3)=23.
  ]

And they also show the correct order of growth:
[
k(n,3)=\Theta!\left(\frac{n^2}{\log n}\right),
]
so it is like the usual triangle Ramsey number up to constants.

## Bottom line

There is **no known closed-form formula** for (k(n,m)) for general (n,m); this is an **open** Erdős–Rado problem. What we do have are:

* exact values in some small cases (especially (m=3)),
* general Ramsey-type bounds (R(n,m)\le k(n,m)\le R(n,2^{m-1})),
* and general upper bounds of order roughly (n^{m-1}/(\log n)^{m-2}) times an exponential-in-(m) factor.
